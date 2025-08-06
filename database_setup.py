import psycopg2
import psycopg2.extras
import datetime
import uuid  # For generating initial schema version if needed, or other UUIDs

from config import PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD

# Import PostgreSQL connection details from config.py
# try:
#     from config import PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD
# except ImportError:
#     print("Error: Could not import PostgreSQL configuration from config.py.")
#     print(
#         "Ensure config.py is present and defines PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD."
#     )
#     # Fallback or exit might be needed here if config is critical
#     exit(1)
CONNECTION = psycopg2.extensions.connection


def get_db_connection() -> CONNECTION:
    """Establishes a connection to the PostgreSQL database."""
    if not all([PG_DATABASE, PG_USER, PG_PASSWORD]):
        raise ValueError(
            "Database connection cannot be established: Missing PG_DATABASE, PG_USER, or PG_PASSWORD in config."
        )

    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            port=PG_PORT,
            dbname=PG_DATABASE,
            user=PG_USER,
            password=PG_PASSWORD,
        )
        # conn.row_factory is not a direct attribute. Use cursor_factory for dict-like rows.
        # psycopg2.extras.DictCursor will allow accessing columns by name.
        print(
            f"Successfully connected to PostgreSQL database: {PG_DATABASE} on {PG_HOST}:{PG_PORT}"
        )
        return conn
    except psycopg2.OperationalError as e:
        raise ConnectionError(f"Error connecting to PostgreSQL database: {e}")


def create_xsd_schema_tables(conn):
    """Creates XSD schema metadata tables used by the NEMSIS XSD ingestion."""
    with conn.cursor() as cursor:
        cursor.execute(
            """
            -- Elements and their schema metadata
            CREATE TABLE IF NOT EXISTS XSD_Elements (
              id SERIAL PRIMARY KEY,
              DatasetName TEXT NOT NULL,           -- e.g., 'eResponse'
              ElementNumber TEXT,                  -- e.g., 'eResponse.13'
              ElementName TEXT NOT NULL,           -- human-friendly label when available
              XMLName TEXT NOT NULL,               -- exact XML element @name
              TypeName TEXT,                       -- referenced or inline base type
              GroupName TEXT,                      -- parent group
              Definition TEXT,
              Usage TEXT,
              v2Number TEXT,
              National BOOLEAN,
              State BOOLEAN,
              MinOccurs INTEGER,
              MaxOccurs TEXT,                      -- 'unbounded' or integer as text
              Nillable BOOLEAN DEFAULT FALSE,
              HasSimpleContent BOOLEAN DEFAULT FALSE,
              CreatedAt TIMESTAMP DEFAULT now()
            );
            """
        )

        cursor.execute(
            """
            -- Simple types and their documentation (create before enums)
            CREATE TABLE IF NOT EXISTS XSD_SimpleTypes (
              TypeName TEXT PRIMARY KEY,
              BaseType TEXT,                       -- xs:string, xs:decimal, etc.
              Documentation TEXT
            );
            """
        )

        cursor.execute(
            """
            -- Enumerations for simple types (code -> description)
            CREATE TABLE IF NOT EXISTS XSD_Enumerations (
              TypeName TEXT REFERENCES XSD_SimpleTypes(TypeName) ON DELETE CASCADE,
              Code TEXT,
              CodeDescription TEXT,
              PRIMARY KEY (TypeName, Code)
            );
            """
        )

        cursor.execute(
            """
            -- Element attributes (e.g., NV, CorrelationID with allowed values)
            CREATE TABLE IF NOT EXISTS XSD_ElementAttributes (
              ElementId INTEGER REFERENCES XSD_Elements(id) ON DELETE CASCADE,
              AttributeName TEXT,
              AllowedValues TEXT,                  -- e.g., 'NV.NotApplicable|NV.NotRecorded|NV.NotReporting'
              UNIQUE (ElementId, AttributeName)
            );
            """
        )

        cursor.execute(
            """
            -- Optional: map element -> valueset type (handy join)
            CREATE TABLE IF NOT EXISTS XSD_ElementValueSet (
              ElementId INTEGER REFERENCES XSD_Elements(id) ON DELETE CASCADE,
              TypeName TEXT REFERENCES XSD_SimpleTypes(TypeName) ON DELETE CASCADE,
              PRIMARY KEY (ElementId, TypeName)
            );
            """
        )

        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_xe_dataset_num ON XSD_Elements(DatasetName, ElementNumber);"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_xe_xmlname ON XSD_Elements(XMLName);"
        )

    conn.commit()
    print("Checked/Created XSD_* schema metadata tables and indexes.")


def create_tables(conn):
    """Creates the initial database tables if they don't exist (PostgreSQL syntax)."""
    # Using psycopg2.extras.DictCursor for easier row access by name later, though not strictly needed for DDL
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # SchemaVersions Table for PostgreSQL
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS SchemaVersions (
            SchemaVersionID SERIAL PRIMARY KEY, -- PostgreSQL auto-incrementing integer
            VersionNumber TEXT NOT NULL UNIQUE,
            CreationDate TIMESTAMPTZ NOT NULL, -- Use TIMESTAMPTZ for timezone awareness
            UpdateDate TIMESTAMPTZ,
            Description TEXT,
            DemographicGroup TEXT NULL -- Remains for now
        );
        """
        )
        print("Checked/Created SchemaVersions table.")

        # XMLFilesProcessed Table for PostgreSQL
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS XMLFilesProcessed (
            ProcessedFileID TEXT PRIMARY KEY,
            OriginalFileName TEXT NOT NULL,
            MD5Hash TEXT,
            ProcessingTimestamp TIMESTAMPTZ NOT NULL,
            Status TEXT NOT NULL, 
            SchemaVersionID INTEGER,
            DemographicGroup TEXT NULL, -- This will now receive NULL from main_ingest.py v4 logic
            FOREIGN KEY (SchemaVersionID) REFERENCES SchemaVersions(SchemaVersionID)
        );
        """
        )
        print("Checked/Created XMLFilesProcessed table.")

    conn.commit()  # Commit DDL changes
    print(
        "Core database tables (SchemaVersions, XMLFilesProcessed) checked/created successfully for PostgreSQL."
    )


def add_initial_schema_version(
    conn,
    version_number="1.0.0-dynamic-ingestor-v4",
    description="Dynamic table logic v4 (PCR UUID based overwrite).",
    demographic_group=None,
):
    """Adds an initial record to the SchemaVersions table if no versions exist."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(
            "SELECT COUNT(*) AS count FROM SchemaVersions"
        )  # Use AS for column name with DictCursor
        if cursor.fetchone()["count"] == 0:
            creation_date = datetime.datetime.now(
                datetime.timezone.utc
            )  # Use timezone-aware datetime
            try:
                cursor.execute(
                    """
                INSERT INTO SchemaVersions (VersionNumber, CreationDate, Description, DemographicGroup)
                VALUES (%s, %s, %s, %s)
                """,
                    (version_number, creation_date, description, demographic_group),
                )
                conn.commit()  # Commit this insert
                print(
                    f"Initial schema version {version_number} added to SchemaVersions table."
                )
            except psycopg2.IntegrityError:
                conn.rollback()  # Rollback if insert fails (e.g. unique constraint)
                print(
                    f"Schema version {version_number} or another initial version already exists or other integrity error."
                )
            except psycopg2.Error as e:
                conn.rollback()
                print(f"Database error adding initial schema version: {e}")
        else:
            print(
                "SchemaVersions table already contains entries. Skipping initial version addition."
            )


if __name__ == "__main__":
    print(f"Initializing PostgreSQL database defined in config for dynamic schema v4.")
    db_conn = None  # Renamed from conn to avoid conflict with module-level conn if any
    try:
        db_conn = get_db_connection()
        if db_conn:
            create_tables(db_conn)
            create_xsd_schema_tables(db_conn)
            add_initial_schema_version(
                db_conn, demographic_group="SystemInternal_PG_v4"
            )
        else:
            print("Could not establish database connection. Setup aborted.")
    except psycopg2.Error as e:
        print(f"PostgreSQL database error during setup: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during PostgreSQL setup: {e}")
    finally:
        if db_conn:
            db_conn.close()
            print("PostgreSQL database connection closed.")
    print("PostgreSQL Database setup script for dynamic schema v4 finished.")
