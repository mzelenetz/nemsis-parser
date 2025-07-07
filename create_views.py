from database_setup import get_db_connection
import re
from structures import *
import sys
from create_definitions import setup_element_definitions
import pandas as pd

conn = get_db_connection()


def table_exists(cursor, table_name, schema="public"):
    cursor.execute(
        """
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = %s AND table_name = %s
        );
        """,
        (schema, table_name),
    )
    return cursor.fetchone()[0]


def get_table_columns(cursor, table_name, schema="public"):
    cursor.execute(
        """
        SELECT column_name FROM information_schema.columns
        WHERE table_schema = %s AND table_name = %s;
        """,
        (schema, table_name),
    )
    return {row[0] for row in cursor.fetchall()}


def filter_structure(structure, cursor, schema="public"):
    return [item for item in structure if table_exists(cursor, item["table"], schema)]


def sanitize_alias(id_str):
    """Sanitize alias to avoid SQL errors"""
    return re.sub(r"[^a-zA-Z0-9_]", "_", id_str) + "_"


def get_element_map(conn) -> dict:
    element_map = {}
    elements = pd.read_sql(
        """select elementnumber, elementname
            from FieldDefinitions
            where datasettype = 'element'""",
        conn,
    )
    element_list = elements.to_dict("index")
    for _, element in element_list.items():
        element_map[element["elementnumber"]] = element["elementname"]
    return element_map


def generate_view_sql(
    view_name: str, structure: list, cursor, column_name_map: dict
) -> str:
    group_columns = ["element_id", "pcr_uuid_context", "correlationid"]
    element_columns = ["text_content", "nil", "nv", "correlationid", "Etco2type"]

    aliases = {}
    base_element = next(item for item in structure if item["parent_id"] is None)
    base_table_name = base_element["table"]
    base_alias = sanitize_alias(base_element["id"])
    aliases[base_element["id"]] = base_alias

    table_columns_cache = {
        item["table"]: get_table_columns(cursor, item["table"]) for item in structure
    }

    tables_to_join = [struc["table"] for struc in structure]

    # select_clauses = [
    #     f'"{base_alias}"."{col}" AS "{base_alias}{col}"'
    #     for col in group_columns
    #     if col in table_columns_cache[base_table_name]
    # ]
    # from_clause = f'FROM "public"."{base_table_name}" AS "{base_alias}"'
    # join_clauses = []

    # for element in [e for e in structure if e["parent_id"] is not None]:
    #     table_name = element["table"]
    #     alias = sanitize_alias(column_name_map.get(element["id"], element["id"]))
    #     aliases[element["id"]] = alias

    #     parent_alias = aliases[element["parent_id"]]
    #     cols_to_select = (
    #         group_columns if element["type"] == "group" else element_columns
    #     )

    #     existing_cols = table_columns_cache[table_name]
    #     for col in cols_to_select:
    #         if col in existing_cols:
    #             select_clauses.append(f'"{alias}"."{col}" AS "{alias}{col}"')

    #     join_clause = (
    #         f'FULL JOIN "public"."{table_name}" AS "{alias}" '
    #         f'ON "{parent_alias}"."element_id" = "{alias}"."parent_element_id"'
    #     )
    #     join_clauses.append(join_clause)

    final_sql = f"""
CREATE OR REPLACE VIEW public.{view_name} AS
SELECT
  {', '.join(select_clauses)}
{from_clause}
{' '.join(join_clauses)};
"""
    return final_sql


def create_view_in_db(conn, view_name, view_sql):
    """
    Creates or replaces a SQL view in the database using the provided SQL statement.

    Attempts to drop the existing view before creating the new one. Prints status messages and rolls back the transaction if view creation fails.
    """
    cursor = conn.cursor()
    drop_sql = f"DROP VIEW IF EXISTS {view_name} CASCADE;"
    try:
        cursor.execute(drop_sql)
    except Exception as drop_err:
        print(f"[WARNING] Could not drop view {view_name}: {drop_err}")
    try:
        # print(f"\nExecuting CREATE VIEW statement for {view_name}...")
        cursor.execute(view_sql)
        conn.commit()
        print(f"View {view_name} created successfully.")
    except Exception as e:
        print(f"Error creating view {view_name}: {e}")
        conn.rollback()
    cursor.close()


if __name__ == "__main__":
    conn = get_db_connection()
    if not conn:
        print("Could not connect to the database.")
    else:
        cursor = conn.cursor()

        column_name_map = table_column_name_map = get_element_map(conn)
        structures = {
            "vitals": EVITALS_STRUCTURE,
            "procedures": EPROCEDURES_STRUCTURE,
            "airway": EAIRWAY_STRUCTURE,
            "crew": ECREW_STRUCTURE,
            "device": EDEVICE_STRUCTURE,
            "arrest": EARREST_STRUCTURE,
            "dispatch": EDISPATCH_STRUCTURE,
            "disposition": EDISPOSITION_STRUCTURE,
            "exam": EEXAM_STRUCTURE,
            "history": EHISTORY_STRUCTURE,
            "injury": EINJURY_STRUCTURE,
            "lab": ELABS_STRUCTURE,
            "medication": EMEDICATIONS_STRUCTURE,
            "other": EOTHER_STRUCTURE,
            "patient": EPATIENT_STRUCTURE,
            "payment": EPAYMENT_STRUCTURE,
            "protocols": EPROTOCOLS_STRUCTURE,
            "record": ERECORD_STRUCTURE,
            "response": ERESPONSE_STRUCTURE,
            "scene": ESCENE_STRUCTURE,
            "situation": ESITUATION_STRUCTURE,
            "times": ETIMES_STRUCTURE,
            "custom": ECUSTOMCONFIGURATION_STRUCTURE,
        }

        for view_name, structure in structures.items():
            filtered_structure = filter_structure(structure, cursor)
            if len(filtered_structure) == 0:
                print(f"Skipping {view_name} view")
                continue

            sql = generate_view_sql(
                view_name, filtered_structure, cursor, column_name_map
            )
            create_view_in_db(conn, view_name, sql)
            if "--verbose" in sys.argv:
                print(f"\nGenerated SQL for {view_name}:\n{sql}\n")

        setup_element_definitions(conn)

        conn.close()
