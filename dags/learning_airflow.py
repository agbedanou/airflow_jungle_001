from datetime import datetime, timedelta
from pendulum import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

# Task using TaskFlow API (newer way)
@task
def generate_numbers():
    """Generate a list of numbers"""
    numbers = [i for i in range(1, 6)]
    print(f"Generated numbers: {numbers}")
    return numbers

# Task using TaskFlow API (newer way)
@task
def print_numbers(numbers: list):
    """Print the received numbers"""
    print(f"Received numbers: {numbers}")

# Create a DAG using the newer TaskFlow API
with DAG(
    'learning_airflow',
    start_date=datetime(2025, 7, 10),
    schedule='@daily',
    catchup=False,
    tags=['tutorial'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    },
    description='A simple tutorial DAG using modern Airflow features'
) as dag:
    
    # Start marker
    start = EmptyOperator(task_id='start')
    
    # Generate numbers task
    numbers_task = generate_numbers()
    
    # Print numbers task
    print_task = print_numbers(numbers_task)
    
    # Simple Bash task
    bash_task = BashOperator(
        task_id='bash_task',
        bash_command='echo "Hello from bash"',
    )
    
    # End marker
    end = EmptyOperator(task_id='end')
    
    # Define task dependencies
    start >> numbers_task >> print_task >> bash_task >> end
