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

EPROCEDURES_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "ProcedureGroup",
        "table": "eprocedures_proceduregroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of ProcedureGroup
    {
        "id": "eProcedures.01",
        "table": "eProcedures_01",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.02",
        "table": "eProcedures_02",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.03",
        "table": "eProcedures_03",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.04",
        "table": "eProcedures_04",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.05",
        "table": "eProcedures_05",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.07",
        "table": "eProcedures_07",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.08",
        "table": "eProcedures_08",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.09",
        "table": "eProcedures_09",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.10",
        "table": "eProcedures_10",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.11",
        "table": "eProcedures_11",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.12",
        "table": "eProcedures_12",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.13",
        "table": "eProcedures_13",
        "parent_id": "ProcedureGroup",
        "type": "element",
    },
]

EAIRWAY_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "AirwayGroup",
        "table": "eairway_airwaygroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of AirwayGroup
    {
        "id": "eAirway.01",
        "table": "eairway_01",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "ConfirmationGroup",
        "table": "eairway_confirmationgroup",
        "parent_id": "AirwayGroup",
        "type": "group",
    },
    {
        "id": "eAirway.08",
        "table": "eairway_08",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.09",
        "table": "eairway_09",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.10",
        "table": "eairway.10",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.11",
        "table": "eairway.11",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    # Children of ConfirmationGroup
    {
        "id": "eAirway.03",
        "table": "eairway_03",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.04",
        "table": "eairway_04",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.05",
        "table": "eairway_05",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.06",
        "table": "eairway_06",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.07",
        "table": "eairway_07",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
]

ECREW_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "CrewGroup",
        "table": "ecrew_crewgroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of CrewGroup
    {
        "id": "eCrew.01",
        "table": "ecrew_01",
        "parent_id": "CrewGroup",
        "type": "element",
    },
    {
        "id": "eCrew.02",
        "table": "ecrew_02",
        "parent_id": "CrewGroup",
        "type": "element",
    },
    {
        "id": "eCrew.03",
        "table": "ecrew_03",
        "parent_id": "CrewGroup",
        "type": "element",
    },
]

EDEVICE_STRUCTURE = (
    [
        # Base Group (Parent of all direct children)
        {
            "id": "DeviceGroup",
            "table": "edevice_devicegroup",
            "parent_id": None,
            "type": "group",
        },
        # Direct Children of DeviceGroup
        {
            "id": "eDevice.01",
            "table": "edevice_01",
            "parent_id": "DeviceGroup",
            "type": "element",
        },
        {
            "id": "eDevice.02",
            "table": "edevice_02",
            "parent_id": "DeviceGroup",
            "type": "element",
        },
        {
            "id": "eDevice.03",
            "table": "edevice_03",
            "parent_id": "DeviceGroup",
            "type": "element",
        },
        {
            "id": "eDevice.07",
            "table": "edevice_07",
            "parent_id": "DeviceGroup",
            "type": "element",
        },
        {
            "id": "eDevice.08",
            "table": "edevice_08",
            "parent_id": "DeviceGroup",
            "type": "element",
        },
        {
            "id": "ShockGroup",
            "table": "edevice_shockgroup",
            "parent_id": "DeviceGroup",
            "type": "group",
        },
        {
            "id": "WaveformGroup",
            "table": "edevice_waveformgroup",
            "parent_id": "DeviceGroup",
            "type": "group",
        },
        # Direct Children of DeviceGroup
        {
            "id": "eDevice.04",
            "table": "edevice_04",
            "parent_id": "WaveformGroup",
            "type": "element",
        },
        {
            "id": "eDevice.05",
            "table": "edevice_05",
            "parent_id": "WaveformGroup",
            "type": "element",
        },
        {
            "id": "eDevice.06",
            "table": "edevice_06",
            "parent_id": "WaveformGroup",
            "type": "element",
        },
        # Direct Children of ShockGroup
        {
            "id": "eDevice.09",
            "table": "edevice_09",
            "parent_id": "ShockGroup",
            "type": "element",
        },
        {
            "id": "eDevice.10",
            "table": "edevice_10",
            "parent_id": "ShockGroup",
            "type": "element",
        },
        {
            "id": "eDevice.11",
            "table": "edevice_11",
            "parent_id": "ShockGroup",
            "type": "element",
        },
        {
            "id": "eDevice.12",
            "table": "edevice_12",
            "parent_id": "ShockGroup",
            "type": "element",
        },
    ],
)


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
        # vitals
        filtered_structure = filter_structure(EVITALS_STRUCTURE, cursor)
        view_name = "v_evitals_flat"
        evitals_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{evitals_sql}\n")
        create_view_in_db(conn, view_name, evitals_sql)
        # procedures
        filtered_structure = filter_structure(EPROCEDURES_STRUCTURE, cursor)
        view_name = "v_eprocedures_flat"
        eprocedures_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{eprocedures_sql}\n")
        create_view_in_db(conn, view_name, eprocedures_sql)

        # airway
        filtered_structure = filter_structure(EAIRWAY_STRUCTURE, cursor)
        view_name = "v_eairway_flat"
        eairway_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{eairway_sql}\n")
        create_view_in_db(conn, view_name, eairway_sql)
        # crew
        filtered_structure = filter_structure(ECREW_STRUCTURE, cursor)
        view_name = "v_ecrew_flat"
        ecrew_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{ecrew_sql}\n")
        create_view_in_db(conn, view_name, ecrew_sql)
        # device
        filtered_structure = filter_structure(EDEVICE_STRUCTURE, cursor)
        view_name = "v_edevice_flat"
        edevice_sql = generate_view_sql(view_name, filtered_structure, cursor)
        print(f"\nGenerated SQL for {view_name}:\n{edevice_sql}\n")
        create_view_in_db(conn, view_name, edevice_sql)
        # TODO: eArrest
        # TODO: eDispatch
        # TODO: eDisposition
        # TODO: eExam
        # TODO: eHistory
        # TODO: elnjury
        # TODO: eLabs
        # TODO: eMedications
        # TODO: eNarrative
        # TODO: eOther
        # TODO: eOutcome
        # TODO: ePatient
        # TODO: ePayment
        # TODO: eProcedures
        # TODO: eProtocols
        # TODO: eRecord
        # TODO: eResponse
        # TODO: eScene
        # TODO: eSituation
        # TODO: eTimes

        conn.close()
