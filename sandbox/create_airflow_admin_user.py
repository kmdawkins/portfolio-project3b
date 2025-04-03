import os
from dotenv import load_dotenv

load_dotenv()

# Pull admin creds from .env (do not hardcode)
username = os.getenv("AIRFLOW_ADMIN_USERNAME")
password = os.getenv("AIRFLOW_ADMIN_PASSWORD")
firstname = os.getenv("AIRFLOW_ADMIN_FIRSTNAME")
lastname = os.getenv("AIRFLOW_ADMIN_LASTNAME")
email = os.getenv("AIRFLOW_ADMIN_EMAIL")

# Assemble the CLI command securely (no secrets in shell history)
os.system(
    f'docker compose run airflow-webserver airflow users create '
    f'--username "{username}" '
    f'--firstname "{firstname}" '
    f'--lastname "{lastname}" '
    f'--role Admin '
    f'--email "{email}" '
    f'--password "{password}"'
)
