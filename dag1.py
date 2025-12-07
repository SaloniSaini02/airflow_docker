from airflow.sdk import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

def my_python_function(name):
    print(f"Hello, {name} from Airflow!")

with DAG(
    dag_id='my_first_dag',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    run_bash_task = BashOperator(
        task_id='print_date',
        bash_command='date'
    )
    run_python_task = PythonOperator(
        task_id='execute_a_function',
        python_callable=my_python_function,
        op_kwargs={'name': 'Sammy'}
    )

    run_bash_task >> run_python_task
