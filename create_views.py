import psycopg2
import psycopg2.extras

# Assuming database_setup.py is in the same directory or accessible in PYTHONPATH
from database_setup import get_db_connection

VIEW_SQL = """
CREATE OR REPLACE VIEW ecustomresults_full AS
SELECT
  "public"."ecustomresults_01"."text_content" AS "text_content",
  "public"."ecustomresults_01"."pcr_uuid_context" AS "pcr_uuid_context",
  "Ecustomresults 02 - Parent Element"."text_content" AS "Ecustomresults 02 - Parent Element__text_content",
  "Ecustomresults 03 - Parent Element"."text_content" AS "Ecustomresults 03 - Parent Element__text_content"
FROM
  "public"."ecustomresults_01"
  FULL JOIN "public"."ecustomresults_02" AS "Ecustomresults 02 - Parent Element" ON "public"."ecustomresults_01"."parent_element_id" = "Ecustomresults 02 - Parent Element"."parent_element_id"
  FULL JOIN "public"."ecustomresults_03" AS "Ecustomresults 03 - Parent Element" ON "public"."ecustomresults_01"."parent_element_id" = "Ecustomresults 03 - Parent Element"."parent_element_id";
"""


def main():
    conn = get_db_connection()
    if not conn:
        print("Could not connect to the database.")
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute(VIEW_SQL)
            conn.commit()
            print("View 'ecustomresults_full' created or replaced successfully.")
    except Exception as e:
        print(f"Error creating view: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
