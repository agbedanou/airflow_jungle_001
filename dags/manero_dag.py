from datetime import datetime, timedelta
from pendulum import datetime
from airflow import DAG
from airflow.decorators import task

# Task 1
@task
def task1():
    """First task that prints a message"""
    print("Task 1: Starting the process")
    return "Task 1 completed"

# Task 2
@task
def task2(message: str):
    """Second task that receives a message from task1"""
    print(f"Task 2: Received message: {message}")
    return "Task 2 completed"

# Task 3
@task
def task3(message: str):
    """Third task that receives a message from task2"""
    print(f"Task 3: Received message: {message}")
    print("Task 3: Finishing the process")
    return "All tasks completed"

# Create manero DAG
with DAG(
    'manero',
    start_date=datetime(2025, 7, 13),
    schedule='@daily',
    catchup=False,
    tags=['tutorial', 'learning'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    },
    description='A simple learning DAG with 3 tasks'
) as dag:
    
    # Task dependencies
    t1 = task1()
    t2 = task2(t1)
    t3 = task3(t2)
    
    # Set task order
    t1 >> t2 >> t3
