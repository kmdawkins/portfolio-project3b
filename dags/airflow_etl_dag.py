# pyright: reportMissingImports=false
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import pandas as pd

# Modular utility imports
from etl_pipeline.utils.file_checker import check_file_exists, validate_file_extension
from etl_pipeline.utils.csv_loader import load_csv_with_fallback

# DAG definition
@dag(
    dag_id="etl_staging_pmo",
    description="Automated ETL for loading pmo.csv into PostgreSQL staging table",
    schedule_interval=None,  # Manual trigger for now
    start_date=days_ago(1),
    catchup=False,
    tags=["project3b", "ETL", "pmo", "local-dev"],
)
def etl_staging_pmo():

    @task()
    def extract() -> str:
        import os
        from loguru import logger

        csv_path = "include/pmo.csv"
        allowed_extensions = [".csv"]

        if not check_file_exists(csv_path):
            raise FileNotFoundError(f"❌ File not found: {csv_path}")

        if not validate_file_extension(csv_path, allowed_extensions):
            raise ValueError(f"❌ Invalid file extension. Must be one of: {allowed_extensions}")

        df = load_csv_with_fallback(csv_path, delimiters=[",", ";", "\t"])

        output_path = "include/intermediate_extract.pkl"
        df.to_pickle(output_path)

        logger.info(f"✅ Extract complete. Rows: {len(df)} | Saved to: {output_path}")
        return output_path

    @task()
    def transform(pickle_path: str) -> pd.DataFrame:
        import pandas as pd
        from loguru import logger

        logger.info("🔁 Starting data transformation...")
        df = pd.read_pickle(pickle_path)

        rename_map = {
            "Old Column A": "new_column_a",
            "Old Column B": "new_column_b",
            # Add more mappings as needed
        }

        df = df.rename(columns=rename_map)
        logger.info(f"📝 Columns renamed: {rename_map}")

        initial_row_count = len(df)
        null_row_count = df.isnull().any(axis=1).sum()

        df_cleaned = df.dropna()
        final_row_count = len(df_cleaned)

        logger.info(f"📊 Initial rows: {initial_row_count}")
        logger.info(f"🗑️ Dropped rows with nulls: {null_row_count}")
        logger.info(f"✅ Final row count after cleaning: {final_row_count}")

        return df_cleaned

    @task()
    def load(clean_df: pd.DataFrame):
        print("⬇️ Load: insert into etl.staging_pmo via SQLAlchemy")

    # ✅ DAG wiring
    pickle_path = extract()
    clean_df = transform(pickle_path)
    load(clean_df)

# Instantiate DAG
etl_staging_pmo()
