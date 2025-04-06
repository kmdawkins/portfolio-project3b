# ===============================================================
# Utility: db_connector.py
# Purpose: Database connection handlers for PostgreSQL (Airflow ETL)
# Author: Katherina Dawkins
# Version: v3.0.0 (Project 3B – Apache Airflow DAG Automation)
# ===============================================================

import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

# ✅ Load environment variables from .env file (Airflow-safe)
load_dotenv()

def get_database_url() -> str:
    """
    Construct PostgreSQL connection URL for SQLAlchemy engine.
    Format: postgresql://user:password@host:port/dbname
    """
    return (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

def get_psycopg2_conn():
    """
    Return a low-level psycopg2 connection.
    Useful for raw cursor-level operations.
    """
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def get_sqlalchemy_engine():
    """
    Return a SQLAlchemy engine for pandas-style inserts and queries.
    Used in Airflow DAGs for batch inserts.
    """
    return create_engine(get_database_url())

# ✅ Optional CLI debug for local test runs only
if __name__ == "__main__":
    try:
        conn = get_psycopg2_conn()
        print("✅ psycopg2 connection successful!")
        conn.close()

        engine = get_sqlalchemy_engine()
        with engine.connect():
            print("✅ SQLAlchemy connection successful!")

    except Exception as e:
        print(f"❌ Connection failed: {e}")
