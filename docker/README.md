## 📁🐋 docker/

### Purpose
- Containerize Airflow with PostgreSQL backend and volume persistence.
- Isolate development environment from host machine.

### Structure
- `docker-compose.yaml`: Service definitions (Airflow webserver, scheduler, PostgreSQL).
- `airflow_volume/`: Mount for DAGs and plugins.
- `postgres_db/`: PostgreSQL data volume.
- `logs/`: Persisted container logs.

### Notes:
- No secrets are stored in this directory.
- Add `.env` file (outside this folder) for sensitive variables.

## 🏆Best practices
- Keep Docker images lightweight.
- Mount volumes for hot-reload during DAG development.