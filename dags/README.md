## 📁 dags/

This folder contains all DAG definitions for Project 3B: Apache Airflow DAG Automation.

### Purpose
- Automate ETL workflows using the Airflow TaskFlow API.
- Schedule, monitor, and orchestrate pipeline tasks.

### Naming Convention
- DAG files follow the format: `airflow_<pipeline_name>_dag.py`
- DAG IDs follow ***snake_case and follow clear workflow purpose*** (e.g., `etl_staging_pmo`).

### Structure
**Each DAG should include:**
- Default arguments
- TaskFlow-based modular functions (`@task`)
- Exception handling and rety logic
- Logging (Airflow-native or custom)

## 🚧 WIP Notes
**Future DAGs will integrate:**
- External APIs
- Lightweight Pandas transformations
- PostgreSQL and cloud destinations