import psycopg2
import os
from database_setup import get_db_connection
import re

conn = get_db_connection()

EVITALS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "VitalGroup",
        "table": "evitals_vitalgroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of VitalGroup
    {
        "id": "eVitals.01",
        "table": "evitals_01",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.02",
        "table": "evitals_02",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "CardiacRhythmGroup",
        "table": "evitals_cardiacrhythmgroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "BloodPressureGroup",
        "table": "evitals_bloodpressuregroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "HeartRateGroup",
        "table": "evitals_heartrategroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.12",
        "table": "evitals_12",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.13",
        "table": "evitals_13",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.14",
        "table": "evitals_14",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.15",
        "table": "evitals_15",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.16",
        "table": "evitals_16",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.17",
        "table": "evitals_17",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.18",
        "table": "evitals_18",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "GlasgowScoreGroup",
        "table": "evitals_glasgowscoregroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "TemperatureGroup",
        "table": "evitals_temperaturegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.26",
        "table": "evitals_26",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "PainScaleGroup",
        "table": "evitals_painscalegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "StrokeScaleGroup",
        "table": "evitals_strokescalegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.31",
        "table": "evitals_31",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.32",
        "table": "evitals_32",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.33",
        "table": "evitals_33",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    # Children of CardiacRhythmGroup
    {
        "id": "eVitals.03",
        "table": "evitals_03",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    {
        "id": "eVitals.04",
        "table": "evitals_04",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    {
        "id": "eVitals.05",
        "table": "evitals_05",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    # Children of BloodPressureGroup
    {
        "id": "eVitals.06",
        "table": "evitals_06",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.07",
        "table": "evitals_07",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.08",
        "table": "evitals_08",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    # Children of HeartRateGroup
    {
        "id": "eVitals.10",
        "table": "evitals_10",
        "parent_id": "HeartRateGroup",
        "type": "element",
    },
    {
        "id": "eVitals.11",
        "table": "evitals_11",
        "parent_id": "HeartRateGroup",
        "type": "element",
    },
    # Children of GlasgowScoreGroup
    {
        "id": "eVitals.19",
        "table": "evitals_19",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.20",
        "table": "evitals_20",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.21",
        "table": "evitals_21",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.22",
        "table": "evitals_22",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.23",
        "table": "evitals_23",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    # Children of TemperatureGroup
    {
        "id": "eVitals.24",
        "table": "evitals_24",
        "parent_id": "TemperatureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.25",
        "table": "evitals_25",
        "parent_id": "TemperatureGroup",
        "type": "element",
    },
    # Children of PainScaleGroup
    {
        "id": "eVitals.27",
        "table": "evitals_27",
        "parent_id": "PainScaleGroup",
        "type": "element",
    },
    {
        "id": "eVitals.28",
        "table": "evitals_28",
        "parent_id": "PainScaleGroup",
        "type": "element",
    },
    # Children of StrokeScaleGroup
    {
        "id": "eVitals.29",
        "table": "evitals_29",
        "parent_id": "StrokeScaleGroup",
        "type": "element",
    },
    {
        "id": "eVitals.30",
        "table": "evitals_30",
        "parent_id": "StrokeScaleGroup",
        "type": "element",
    },
]


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


def generate_view_sql(view_name: str, structure: list, cursor) -> str:
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

    select_clauses = [
        f'"{base_alias}"."{col}" AS "{base_alias}{col}"'
        for col in group_columns
        if col in table_columns_cache[base_table_name]
    ]
    from_clause = f'FROM "public"."{base_table_name}" AS "{base_alias}"'
    join_clauses = []

    for element in [e for e in structure if e["parent_id"] is not None]:
        table_name = element["table"]
        alias = sanitize_alias(element["id"])
        aliases[element["id"]] = alias

        parent_alias = aliases[element["parent_id"]]
        cols_to_select = (
            group_columns if element["type"] == "group" else element_columns
        )

        existing_cols = table_columns_cache[table_name]
        for col in cols_to_select:
            if col in existing_cols:
                select_clauses.append(f'"{alias}"."{col}" AS "{alias}{col}"')

        join_clause = (
            f'FULL JOIN "public"."{table_name}" AS "{alias}" '
            f'ON "{parent_alias}"."element_id" = "{alias}"."parent_element_id"'
        )
        join_clauses.append(join_clause)

    final_sql = f"""
CREATE OR REPLACE VIEW public.{view_name} AS
SELECT
  {', '.join(select_clauses)}
{from_clause}
{' '.join(join_clauses)};
"""
    return final_sql

    group_columns = ["element_id", "pcr_uuid_context", "correlationid"]
    element_columns = ["text_content", "nil", "nv", "correlationid", "Etco2type"]

    aliases = {}
    base_element = next(item for item in structure if item["parent_id"] is None)
    base_table_name = base_element["table"]
    base_alias = sanitize_alias(base_element["id"])
    aliases[base_element["id"]] = base_alias

    select_clauses = [
        f'"{base_alias}"."{col}" AS "{base_alias}{col}"' for col in group_columns
    ]
    from_clause = f'FROM "public"."{base_table_name}" AS "{base_alias}"'
    join_clauses = []

    for element in [e for e in structure if e["parent_id"] is not None]:
        table_name = element["table"]
        alias = sanitize_alias(element["id"])
        aliases[element["id"]] = alias

        parent_alias = aliases[element["parent_id"]]
        cols_to_select = (
            group_columns if element["type"] == "group" else element_columns
        )

        for col in cols_to_select:
            select_clauses.append(f'"{alias}"."{col}" AS "{alias}{col}"')

        join_clause = (
            f'FULL JOIN "public"."{table_name}" AS "{alias}" '
            f'ON "{parent_alias}"."element_id" = "{alias}"."parent_element_id"'
        )
        join_clauses.append(join_clause)

    final_sql = f"""
CREATE OR REPLACE VIEW public.{view_name} AS
SELECT
  {', '.join(select_clauses)}
{from_clause}
{' '.join(join_clauses)};
"""
    return final_sql


def create_view_in_db(conn, view_name, view_sql):
    cursor = conn.cursor()
    drop_sql = f"DROP VIEW IF EXISTS {view_name} CASCADE;"
    try:
        cursor.execute(drop_sql)
    except Exception as drop_err:
        print(f"[WARNING] Could not drop view {view_name}: {drop_err}")
    try:
        print(f"\nExecuting CREATE VIEW statement for {view_name}...")
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
        filtered_structure = filter_structure(EVITALS_STRUCTURE, cursor)
        view_name = "v_evitals_flat"
        evitals_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{evitals_sql}\n")
        create_view_in_db(conn, view_name, evitals_sql)
        conn.close()
