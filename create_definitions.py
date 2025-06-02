import psycopg2
import requests
import csv

NEMSIS_ENUM_URL = "https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/Ancillary/DEMEMS/Combined_ElementEnumerations.txt"
FIELD_DEF_URL = "https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/Ancillary/DEMEMS/Combined_ElementAttributes.txt"


def create_element_definitions_table(conn):
    """
    Creates the ElementDefinitions table in the database if it does not already exist.
    
    The table includes columns for dataset name, element number, element name, code, and code description.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ElementDefinitions (
            DatasetName TEXT,
            ElementNumber TEXT,
            ElementName TEXT,
            Code TEXT,
            CodeDescription TEXT
        );
    """
    )
    conn.commit()
    cursor.close()
    print("[ElementDefinitions] Table created or already exists.")


def populate_element_definitions_table(conn):
    """
    Downloads and populates the ElementDefinitions table with data from the NEMSIS enumeration source.
    
    Retrieves the latest element definitions from the NEMSIS enumeration URL, parses the pipe-delimited data, and inserts the cleaned records into the ElementDefinitions table after clearing existing entries.
    """
    print("[ElementDefinitions] Downloading data from NEMSIS...")
    response = requests.get(NEMSIS_ENUM_URL)
    response.raise_for_status()
    lines = response.text.splitlines()
    reader = csv.DictReader(lines, delimiter="|")
    rows = [
        (
            row.get("DatasetName", "").strip(),
            row.get("ElementNumber", "").strip(),
            row.get("ElementName", "").strip(),
            row.get("Code", "").strip(),
            row.get("CodeDescription", "").strip(),
        )
        for row in reader
    ]
    print(f"[ElementDefinitions] Downloaded and parsed {len(rows)} rows.")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ElementDefinitions;")
    for row in rows:
        cursor.execute(
            "INSERT INTO ElementDefinitions (DatasetName, ElementNumber, ElementName, Code, CodeDescription) VALUES (%s, %s, %s, %s, %s)",
            row,
        )
    conn.commit()
    cursor.close()
    print(f"[ElementDefinitions] Inserted {len(rows)} rows into the table.")


def create_field_definitions_table(conn):
    """
    Creates the FieldDefinitions table in the database if it does not already exist.
    
    The table includes columns for Dataset, DatasetType, ElementNumber, ElementName, and Attribute.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FieldDefinitions (
            Dataset TEXT,
            DatasetType TEXT,
            ElementNumber TEXT,
            ElementName TEXT,
            Attribute TEXT
        );
    """
    )
    conn.commit()
    cursor.close()
    print("[FieldDefinitions] Table created or already exists.")


def populate_field_definitions_table(conn):
    """
    Downloads and populates the FieldDefinitions table with data from the NEMSIS field definitions source.
    
    The function retrieves a pipe-delimited text file from the NEMSIS field definitions URL, parses its contents, and inserts the relevant fields into the FieldDefinitions table after clearing any existing data.
    """
    print("[FieldDefinitions] Downloading data from NEMSIS...")
    response = requests.get(FIELD_DEF_URL)
    response.raise_for_status()
    lines = response.text.splitlines()
    reader = csv.DictReader(lines, delimiter="|")
    rows = [
        (
            row.get("Dataset", "").strip(),
            row.get("DatasetType", "").strip(),
            row.get("ElementNumber", "").strip(),
            row.get("ElementName", "").strip(),
            row.get("Attribute", "").strip(),
        )
        for row in reader
    ]
    print(f"[FieldDefinitions] Downloaded and parsed {len(rows)} rows.")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM FieldDefinitions;")
    for row in rows:
        cursor.execute(
            "INSERT INTO FieldDefinitions (Dataset, DatasetType, ElementNumber, ElementName, Attribute) VALUES (%s, %s, %s, %s, %s)",
            row,
        )
    conn.commit()
    cursor.close()
    print(f"[FieldDefinitions] Inserted {len(rows)} rows into the table.")


def setup_element_definitions(conn):
    """
    Creates and populates the ElementDefinitions and FieldDefinitions tables in the database.
    
    This function orchestrates the setup process by creating both tables if they do not exist and populating them with data downloaded from external NEMSIS sources. Closes the database connection upon completion.
    """
    print("[ElementDefinitions] Starting setup...")
    create_element_definitions_table(conn)
    populate_element_definitions_table(conn)
    print("[ElementDefinitions] Setup complete.")
    print("[FieldDefinitions] Starting setup...")
    create_field_definitions_table(conn)
    populate_field_definitions_table(conn)
    print("[FieldDefinitions] Setup complete.")
    conn.close()
