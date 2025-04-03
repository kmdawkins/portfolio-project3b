from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from pendulum import datetime

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
    def extract():
        print("✅ Extract: file_checker + csv_loader will be run here")


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