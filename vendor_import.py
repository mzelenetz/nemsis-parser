import argparse
import pandas as pd
import psycopg2
from database_setup import get_db_connection

VENDOR_SPECS = {
    "imagetrend": {
        "sheets": {
            "DataSetFields": [
                "Field Code",
                "Field Name",
                "Default Label",
                "Data Type",
                "Active",
                "Specific Module",
            ],
            "DataSetFieldValues": [
                "Field Code",
                "Field Name",
                "Data Type",
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Active",
            ],
            "Medication Allergies (eHistory.": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Environmental Food Allergies (e": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Medical Surgical History (eHist": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Current Medications (eHistory.1": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Cause of Injury (eInjury.01)": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Medication Given (eMedications.": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Emergency Department Recorded C": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Emergency Department Procedures": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Emergency Department Diagnosis ": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Hospital Procedures (eOutcome.1": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Hospital Diagnosis (eOutcome.13": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "EMS Condition Code (ePayment.51": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Procedure (eProcedures.03)": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Incident Location Type (eScene.": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Primary Symptom (eSituation.09)": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Other Associated Symptoms (eSit": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Provider's Primary Impression (": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Provider's Secondary Impression": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Patient Activity (eSituation.17": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Controlled Substance Medication": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Medication Ordered (itMedicatio": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Emergency Department Procedure ": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Hospital Procedure (itOutcome.0": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
            "Procedure Ordered (itProcedureO": [
                "Code",
                "Value",
                "Label",
                "Sort Order",
                "Resource Type",
            ],
        }
    },
    # Add more vendors here
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Import vendor Excel data into database."
    )
    parser.add_argument("-file_path", required=True, help="Path to the Excel file")
    parser.add_argument(
        "-vendor", required=True, help="Vendor name (for hardcoded logic)"
    )
    parser.add_argument("-source", required=True, help="Source name (for table naming)")
    return parser.parse_args()


def import_vendor_excel(file_path, vendor, source):
    if vendor not in VENDOR_SPECS:
        raise ValueError(f"Vendor '{vendor}' not supported. Add it to VENDOR_SPECS.")
    conn = get_db_connection()
    for sheet, columns in VENDOR_SPECS[vendor]["sheets"].items():
        print(f"[INFO] Processing sheet: {sheet} with columns: {columns}")
        df = pd.read_excel(file_path, sheet_name=sheet, usecols=columns)
        df = df.dropna(how="all")
        table_name = (
            f"{source.lower()}_{sheet.lower().replace(' ', '_').replace('.', '_')}"
        )
        # Create table
        col_defs = ", ".join([f'"{col}" TEXT' for col in columns])
        create_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({col_defs});'
        with conn.cursor() as cur:
            cur.execute(create_sql)
            conn.commit()
        print(f"[INFO] Created table: {table_name}")
        # Insert data
        for _, row in df.iterrows():
            values = [
                str(row[col]) if pd.notnull(row[col]) else None for col in columns
            ]
            placeholders = ", ".join(["%s"] * len(columns))
            insert_sql = f'INSERT INTO "{table_name}" ({', '.join([f'"{col}"' for col in columns])}) VALUES ({placeholders});'
            with conn.cursor() as cur:
                cur.execute(insert_sql, values)
        conn.commit()
        print(f"[INFO] Inserted {len(df)} rows into {table_name}")
    conn.close()
    print("[INFO] Import complete.")


if __name__ == "__main__":
    args = parse_args()
    import_vendor_excel(args.file_path, args.vendor, args.source)
