# Project 3B: Apache Airflow DAG Automation

## 🎯 Project Objective
Automate a modular ETL pipeline using **Apache Airflow**, with support for:
- DAG scheduling and orchestration
- Task modularization (Extract, Validate, Transform, Load)
- Logging, retries, and error handling
- Integration with PostgreSQL, APIs, and future cloud targets

---

## 🛠️ Tech Stack
- **Apache Airflow** (Docker-based)
- **Python 3.11**
- **PostgreSQL**
- **Docker & Docker Compose**
- **pandas, SQLAlchemy, psycopg2**
- **pytest** (unit testing)
- **loguru** (logging)
- **dotenv** (secrets management)

---

## 📁 Project Structure (Key Folders)
| Folder        | Purpose                                         |
|---------------|--------------------------------------------------|
| `dags/`       | Production DAGs (TaskFlow API)                  |
| `docker/`     | Airflow Docker setup & volume configs           |
| `include/`    | Shared SQL files, templates, scripts            |
| `sandbox/`    | Temporary debug and connection test scripts     |
| `tests/`      | Unit tests for DAG components                   |
| `logs/`       | Airflow and custom task logs                    |

---

## 🔐 Secrets Management
Secrets are stored in a `.env` file and are **never committed** to version control.
This project uses `python-dotenv` to load environment variables securely.

---

## 🚀 Deployment (Docker Quick Start)
```bash
docker compose up airflow-init
docker compose up
