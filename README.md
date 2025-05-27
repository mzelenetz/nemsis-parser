# NEMSIS Database Ingestion

This project ingests NEMSIS-compliant XML files into a dynamic PostgreSQL database schema, creating tables or colmns dynamically based based on XML structure. It is designed for scalable, flexible EMS data warehousing and analysis from exported NEMSIS compliant software vendors. As long as the software is set to export agency specfic custom question as well they will included in the database for analysis.

The hope is that by allowing agnecies to build data lakes or datawarehouses internally it will reduce the need for formbuilding or external reporting mechanisms for KPI gathering and quality management systems.

## Features
- **Dynamic Table Creation:** Tables are created based on XML tag structure.
- **UUID-based Overwrite:** Data is keyed by PatientCareReport UUID for safe updates.
- **Table Comments:** Each table stores its XML path as a PostgreSQL table comment.
- **Bulk Ingestion:** Easily process all XML files in a directory.

## Requirements
- Python 3.8+
- PostgreSQL (with a database you can connect to)
- Python packages:
  - `psycopg2`
  - `python-dotenv`

Install dependencies:
```bash
pip install psycopg2 python-dotenv
```

## Configuration
Create a `.env` file in the project root with your PostgreSQL connection details:

```
PG_HOST=localhost
PG_PORT=5432
PG_DATABASE=your_database
PG_USER=your_user
PG_PASSWORD=your_password
```

## Initial Setup
1. **Create the PostgreSQL database** (if it does not exist):
   Connect to your PostgreSQL server and run:
   ```sql
   CREATE DATABASE your_database;
   ```
2. **Create tables and initialize schema:**
   ```bash
   python database_setup.py
   ```
   This will create the required tables in your database.

## Ingesting XML Files
To ingest a single XML file:
```bash
python main_ingest.py nemsis_xml/your_file.xml
```

To ingest **all XML files in a directory** (PowerShell example):
```powershell
Get-ChildItem -Path .\nemsis_xml\*.xml | ForEach-Object { python main_ingest.py $_.FullName }
```

Or (CMD example):
```cmd
for %f in (nemsis_xml\*.xml) do python main_ingest.py "%f"
```

## Output
- Processed XML files are archived in the `processed_xml_archive/` directory.
- Data is available in your PostgreSQL database, with dynamic tables for each XML tag type.

## Notes
- The ingestion script will skip or update data based on the PatientCareReport UUID.
- Table comments in PostgreSQL will contain the XML path for each table.
- You can use standard SQL tools to query and analyze the ingested data.

## Troubleshooting
- **Database connection errors:** Ensure your `.env` is correct and the database exists.
- **Missing dependencies:** Install with `pip install psycopg2 python-dotenv`.
- **Permission errors:** Make sure your PostgreSQL user has rights to create tables and comments.

## License
MIT License
