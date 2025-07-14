# Airflow Jungle 001

This is an Airflow project that demonstrates basic DAG creation and task orchestration.

## Features

- Two example DAGs:
  - `learning_airflow.py`: A basic DAG with TaskFlow API usage
  - `manero_dag.py`: A simple DAG with three sequential tasks

## Setup

1. Clone the repository
2. Run Airflow using Docker Compose
3. Access the Airflow UI at http://localhost:8080

## Requirements

- Docker and Docker Compose
- Python 3.x
- Apache Airflow 2.10.0

## Usage

1. Start Airflow:
```bash
docker compose up -d
```

2. Access the Airflow UI:
- URL: http://localhost:8080
- Username: admin
- Password: admin
