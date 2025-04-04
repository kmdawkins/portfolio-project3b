# pyright: reportMissingImports=false
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from pendulum import datetime

# Import modular utils
from etl_pipeline.utils.file_checker import check_file_exists, validate_file_extension
from etl_pipeline.utils.csv_loader import load_csv_with_fallback

# DAG metadata
@dag(
    dag_id="etl_staging_pmo",
    description="Automated ETL for loading pmo.csv into PostgreSQL staging table",
    schedule_interval=None, # Manual for now
    start_date=days_ago(1),
    catchup=False,
    tags=["project3b", "ETL", "pmo", "local-dev"],
)
def etl_staging_pmo():


    @task()
    def extract() -> str:
        import os
        import sys
        from pathlib import Path

        # Add etl_pipeline to sys.path
        sys.path.append(str(Path(__file__).resolve().parents[1] / "etl_pipeline"))


        # Define path to raw pmo.csv file
        csv_path = "include/pmo.csv"
        allowed_extensions = [".csv"]


        # Check file exists
        if not check_file_exists(csv_path):
            raise FileNotFoundError(f"❌ File not found: {csv_path}")
        

        # Load CSV into DataFrame
        df = load_csv_with_fallback(csv_path, delimiters=[",", ";", "\t"])


        # Save to intermediate pickle (optional for transform step)
        output_path = "include/intermediate_extract.pkl"
        df.to_pickle(output_path)


        print(f"✅ Extract comple. Rows: {len(df)} | Saved to: {output_path}")
        return output_path


    @task()
    def transform():
        print("🔁 Transform: clean DataFrame (e.g., rename columns, drop nulls)")


    @task()
    def load():
        print("⬇️ Load: insert into etl.staging_pmo via SQLAlchemy")


    # DAG Task Dependencies
    extract_task = extract()
    transform_task = transform()
    load_task = load()


    extract_task >> transform_task >> load_task

# instantiate the DAG
etl_staging_pmo()