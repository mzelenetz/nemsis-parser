import psycopg2
import psycopg2.extras

# Assuming database_setup.py is in the same directory or accessible in PYTHONPATH
from database_setup import get_db_connection

VIEW_SQL = """
CREATE OR REPLACE VIEW ecustomresults_full AS
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

DROP_VIEW_SQL = "DROP VIEW IF EXISTS ecustomresults_full;"


def main():
    conn = get_db_connection()
    if not conn:
        print("Could not connect to the database.")
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute(DROP_VIEW_SQL)
            cursor.execute(VIEW_SQL)
            conn.commit()
            print("View 'ecustomresults_full' created or replaced successfully.")
    except Exception as e:
        print(f"Error creating view: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
