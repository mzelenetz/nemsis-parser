import psycopg2
import psycopg2.extras
from psycopg2 import sql

# Assuming database_setup.py is in the same directory or accessible in PYTHONPATH
from database_setup import get_db_connection


def get_view_sql(view_name, select_sql):
    return f"""
CREATE OR REPLACE VIEW {view_name} AS
{select_sql}
"""


def get_drop_view_sql(view_name):
    return f"DROP VIEW IF EXISTS {view_name};"


def create_view(conn, view_name, select_sql):
    drop_sql = get_drop_view_sql(view_name)
    view_sql = get_view_sql(view_name, select_sql)
    with conn.cursor() as cursor:
        cursor.execute(drop_sql)
        cursor.execute(view_sql)
    print(f"View '{view_name}' created or replaced successfully.")


ECUSTOMRESULTS_FULL_SELECT_SQL = """
SELECT
  ecustomresults_01,
  pcr_uuid_context,
  ecustomresults_02,
  ecustomresults_03
FROM (
  SELECT
    t1.text_content AS ecustomresults_01,
    t1.pcr_uuid_context,
    t2.text_content AS ecustomresults_02,
    t3.text_content AS ecustomresults_03
  FROM
    public.ecustomresults_01 AS t1
    FULL JOIN public.ecustomresults_02 AS t2 ON t1.parent_element_id = t2.parent_element_id
    FULL JOIN public.ecustomresults_03 AS t3 ON t1.parent_element_id = t3.parent_element_id
) sub;
"""

ECUSTOMCONFIGURATION_FULL_SELECT_SQL = """
SELECT
  ecustomconfig1.nemsiselement,
  ecustomconfig1.text_content,
  ecustomconfig1.pcr_uuid_context,
  ecustomconfig2.text_content AS ecustomconfig2_text_content,
  ecustomconfig3.text_content AS ecustomconfig3_text_content,
  ecustomconfig4.text_content AS ecustomconfig4_text_content,
  ecustomconfig5.text_content AS ecustomconfig5_text_content,
  ecustomconfig6.nemsiscode AS ecustomconfig6_nemsiscode,
  ecustomconfig6.text_content AS ecustomconfig6_text_content,
  ecustomconfig6.customvaluedescription AS ecustomconfig6_customval_e1abe582,
  ecustomconfig9.text_content AS ecustomconfig9_text_content
FROM
  public.ecustomconfiguration_01 AS ecustomconfig1
  FULL JOIN public.ecustomconfiguration_02 AS ecustomconfig2 ON ecustomconfig1.parent_element_id = ecustomconfig2.parent_element_id
  FULL JOIN public.ecustomconfiguration_03 AS ecustomconfig3 ON ecustomconfig1.parent_element_id = ecustomconfig3.parent_element_id
  FULL JOIN public.ecustomconfiguration_04 AS ecustomconfig4 ON ecustomconfig1.parent_element_id = ecustomconfig4.parent_element_id
  FULL JOIN public.ecustomconfiguration_05 AS ecustomconfig5 ON ecustomconfig1.parent_element_id = ecustomconfig5.parent_element_id
  FULL JOIN public.ecustomconfiguration_06 AS ecustomconfig6 ON ecustomconfig1.parent_element_id = ecustomconfig6.parent_element_id
  FULL JOIN public.ecustomconfiguration_09 AS ecustomconfig9 ON ecustomconfig1.parent_element_id = ecustomconfig9.parent_element_id;
"""


def main():
    conn = get_db_connection()
    if not conn:
        print("Could not connect to the database.")
        return
    try:
        create_view(conn, "ecustomresults_full", ECUSTOMRESULTS_FULL_SELECT_SQL)
        create_view(
            conn, "ecustomconfiguration_full", ECUSTOMCONFIGURATION_FULL_SELECT_SQL
        )
        conn.commit()
    except Exception as e:
        print(f"Error creating view: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
