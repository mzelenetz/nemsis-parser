from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
import os
import shutil
import uuid
import psycopg2 # For database interaction
import psycopg2.extras # For DictCursor

# Attempt to import project-specific modules
try:
    from database_setup import get_db_connection
    from xml_handler import parse_xml_file # Used by process_xml_file, but good to have if direct parsing is ever needed by API
    from main_ingest import process_xml_file, get_ingestion_logic_schema_id, INGESTION_LOGIC_VERSION_NUMBER
    import config # To access DB credentials if needed, though get_db_connection should handle it
except ImportError as e:
    print(f"Error importing project modules: {e}")
    # Depending on deployment strategy, you might want to raise an error or have default fallbacks
    # For now, we'll let it proceed and potentially fail at runtime if modules are critical

app = FastAPI(
    title="NEMSIS Data API",
    description="API for ingesting NEMSIS XML data and querying processed data.",
    version="1.0.0"
)

# --- Pydantic Models ---

class IngestResponse(BaseModel):
    message: str
    file_id: Optional[str] = None
    original_filename: Optional[str] = None
    status: Optional[str] = None

class QueryParams(BaseModel):
    query_id: str
    date_from: datetime
    date_to: datetime
    diagnosis: Optional[List[str]] = None
    procedures: Optional[List[str]] = None
    medications: Optional[List[str]] = None

class QueryResult(BaseModel):
    query_id: str
    parameters: QueryParams
    count: int
    data: List[Dict]

# --- Helper Functions ---
TEMP_UPLOAD_DIR = "temp_xml_uploads"
os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True)

@app.on_event("startup")
async def startup_event():
    # You can add any startup logic here if needed
    # Ensure the temp upload directory exists
    os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True)
    print(f"FastAPI application startup complete. Temp upload dir: {TEMP_UPLOAD_DIR}")

@app.on_event("shutdown")
def shutdown_event():
    # Clean up the temporary directory on shutdown
    if os.path.exists(TEMP_UPLOAD_DIR):
        try:
            shutil.rmtree(TEMP_UPLOAD_DIR)
            print(f"Cleaned up temporary upload directory: {TEMP_UPLOAD_DIR}")
        except Exception as e:
            print(f"Error cleaning up temporary upload directory {TEMP_UPLOAD_DIR}: {e}")
    print("FastAPI application shutdown complete.")

# --- API Endpoints ---

@app.post("/ingest_xml/", response_model=IngestResponse, tags=["Data Ingestion"])
async def ingest_xml_file(file: UploadFile = File(...)):
    """
    Accepts an XML file, processes it using existing ingestion logic,
    and stores the data into the database.
    """
    temp_file_path = None
    success = False # Initialize success to False
    try:
        # Ensure the temp upload directory exists (it should from startup, but double-check)
        os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True)

        # Create a unique temporary file path
        temp_file_name = f"{uuid.uuid4()}_{file.filename}"
        temp_file_path = os.path.join(TEMP_UPLOAD_DIR, temp_file_name)

        # Save the uploaded file to the temporary path
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get database connection
        conn = None # Initialize conn to None
        try:
            conn = get_db_connection()
            if conn is None:
                raise HTTPException(status_code=500, detail="Failed to connect to the database.")

            ingestion_schema_id = None
            # Get the schema ID for the current ingestion logic version
            ingestion_schema_id = get_ingestion_logic_schema_id(conn, INGESTION_LOGIC_VERSION_NUMBER)
            if ingestion_schema_id is None:
                # This case should ideally be handled during application startup or have a fallback.
                # If the specific version isn't found, it implies a setup issue.
                raise HTTPException(status_code=500, detail=f"Ingestion logic version {INGESTION_LOGIC_VERSION_NUMBER} not found in database. Setup may be incomplete.")

            # Process the XML file using the existing function from main_ingest.py
            # Note: process_xml_file archives the file upon successful processing.
            # If it fails, the file remains in temp_upload_dir and will be cleaned by the finally block here or shutdown hook.
            success = process_xml_file(conn, temp_file_path, ingestion_schema_id)

            if success:
                # The file is archived by process_xml_file, so we don't need to explicitly delete it from temp_file_path if successful
                return IngestResponse(
                    message="XML file processed and data ingested successfully.",
                    original_filename=file.filename,
                    status="Success"
                )
            else:
                # If process_xml_file returns False, it means an error occurred during its execution.
                # The specific error should have been logged by process_xml_file.
                raise HTTPException(status_code=500, detail="Failed to process XML file. Check server logs for details.")

        finally:
            if conn:
                conn.close()
            # Clean up: if the file still exists at temp_file_path (e.g., processing failed before archiving)
            # and process_xml_file did not archive it, remove it.
            # process_xml_file is expected to archive on success.
            if temp_file_path and os.path.exists(temp_file_path) and not success: # Only remove if not successful, as success implies archiving
                 try:
                    os.remove(temp_file_path)
                 except Exception as e:
                    print(f"Error cleaning up temporary file {temp_file_path}: {e}")


    except HTTPException as http_exc:
        # Re-raise HTTPException to be handled by FastAPI
        raise http_exc
    except Exception as e:
        # Log the exception for debugging
        print(f"An unexpected error occurred during XML ingestion: {e}") # Replace with proper logging
        # Clean up the temp file if it exists and an error occurred
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except Exception as cleanup_e:
                print(f"Error cleaning up temporary file {temp_file_path} after an error: {cleanup_e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    finally:
        # Ensure the file object is closed
        if hasattr(file, 'file') and hasattr(file.file, 'close'):
            file.file.close()

@app.get("/query/", response_model=QueryResult, tags=["Data Querying"])
async def execute_query(
    query_id: str = Query(..., description="The ID of the pre-defined query (view name) to execute, e.g., v_evitals_flat."),
    date_from: datetime = Query(..., description="Start of the date range (ISO format)."),
    date_to: datetime = Query(..., description="End of the date range (ISO format)."),
    diagnosis: Optional[List[str]] = Query(None, description="List of diagnosis codes (e.g., ICD-10 codes from eHistory.01)."),
    procedures: Optional[List[str]] = Query(None, description="List of procedure codes (e.g., from eProcedures.03)."),
    medications: Optional[List[str]] = Query(None, description="List of medication codes (e.g., National Drug Codes from eMedications.03).")
):
    """
    Executes a pre-defined query (SQL View) with date range filtering
    and optional filtering by diagnosis, procedures, or medications.
    """
    if not query_id.replace('_', '').isalnum(): # Basic sanitization for view name
        raise HTTPException(status_code=400, detail="Invalid query_id format. Must be an alphanumeric view name potentially with underscores.")

    # Ensure the query_id (view name) is properly quoted to handle mixed case or special characters if any.
    # PostgreSQL identifiers are case-insensitive unless quoted.
    target_view = f'"{query_id}"'

    sql_query_parts = [f"SELECT * FROM {target_view} main_view"]
    sql_conditions = []
    sql_params = {}

    # This column name is assumed to exist in all views used for querying.
    # It should represent the primary NEMSIS PCR date/time for filtering.
    date_filter_column = "pcr_nemsis_datetime"

    sql_conditions.append(f'main_view."{date_filter_column}" BETWEEN %(date_from)s AND %(date_to)s')
    sql_params["date_from"] = date_from
    sql_params["date_to"] = date_to

    # These table names (ehistory_01, eprocedures_03, emedications_03) and the column 'text_content'
    # are based on common NEMSIS XML shredding patterns. Adjust if your schema differs.
    # Also, 'pcr_uuid_context' is assumed as the common foreign key linking back to the main PCR record.
    # Diagnosis codes (checked in esituation_11 or esituation_12)
    if diagnosis:
        # A record matches if the diagnosis code is in EITHER esituation_11 OR esituation_12
        sql_conditions.append(
            f'''(EXISTS (SELECT 1 FROM esituation_11 diag_codes_11
                         WHERE diag_codes_11.pcr_uuid_context = main_view.pcr_uuid_context
                         AND diag_codes_11.text_content = ANY(%(diagnosis)s))
                 OR EXISTS (SELECT 1 FROM esituation_12 diag_codes_12
                            WHERE diag_codes_12.pcr_uuid_context = main_view.pcr_uuid_context
                            AND diag_codes_12.text_content = ANY(%(diagnosis)s)))'''
        )
        sql_params["diagnosis"] = diagnosis

    if procedures:
        sql_conditions.append(
            f"""EXISTS (SELECT 1 FROM eprocedures_03 proc_codes
                       WHERE proc_codes.pcr_uuid_context = main_view.pcr_uuid_context
                       AND proc_codes.text_content = ANY(%(procedures)s))"""
        )
        sql_params["procedures"] = procedures

    if medications:
        sql_conditions.append(
            f"""EXISTS (SELECT 1 FROM emedications_03 med_codes
                       WHERE med_codes.pcr_uuid_context = main_view.pcr_uuid_context
                       AND med_codes.text_content = ANY(%(medications)s))"""
        )
        sql_params["medications"] = medications

    if sql_conditions:
        sql_query_parts.append("WHERE " + " AND ".join(sql_conditions))

    final_sql_query = " ".join(sql_query_parts)

    # For debugging, print the constructed query and parameters
    # In a production environment, use structured logging.
    print(f"Executing SQL: {final_sql_query} with params: {sql_params}")

    conn = None
    try:
        conn = get_db_connection()
        if conn is None:
            # Using 503 Service Unavailable as the database is a critical external service
            raise HTTPException(status_code=503, detail="Database connection unavailable.")

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(final_sql_query, sql_params)
                results = cursor.fetchall()
            except psycopg2.Error as db_err:
                conn.rollback() # Rollback any transaction in case of error
                # Construct a more user-friendly error message
                error_detail = f"Database error: {db_err}"
                if "column" in str(db_err).lower() and date_filter_column in str(db_err) and "does not exist" in str(db_err).lower():
                     error_detail = f"Database error: The specified date filter column '{date_filter_column}' does not exist in the view '{query_id}'. Please ensure the view contains this column or adjust the API's date filtering logic."
                elif "relation" in str(db_err).lower() and "does not exist" in str(db_err).lower():
                     # Attempt to extract the missing relation name if possible, otherwise use query_id as a guess.
                     missing_relation = str(db_err).split('"')[1] if '"' in str(db_err) else query_id
                     error_detail = f"Database error: A required table or view ('{missing_relation}') does not exist. This could be the main query view ('{query_id}') or a table needed for filtering (e.g., ehistory_01, eprocedures_03, emedications_03). Original error: {db_err}"

                print(f"Database Error: {error_detail}") # Log the detailed error
                raise HTTPException(status_code=500, detail=error_detail)

        # Convert query results (list of psycopg2.extras.DictRow) to list of dicts
        data_as_dicts = [dict(row) for row in results]

        return QueryResult(
            query_id=query_id,
            parameters=QueryParams( # Reconstruct QueryParams for the response
                query_id=query_id, date_from=date_from, date_to=date_to,
                diagnosis=diagnosis, procedures=procedures, medications=medications
            ),
            count=len(data_as_dicts),
            data=data_as_dicts
        )

    except HTTPException as http_exc:
        # Re-raise HTTPExceptions to be handled by FastAPI's default error handling
        raise http_exc
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"Unexpected error during query execution: {e}") # Log the error
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred while executing the query: {str(e)}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    import uvicorn
    # It's good practice to make host and port configurable, e.g., via environment variables
    # For simplicity, hardcoding for now, but for production, consider using config variables.
    uvicorn.run(app, host="0.0.0.0", port=8000)
