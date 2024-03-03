from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 21),
    'retries': 1
}

with DAG('test_read_file_dag_sshop', default_args=default_args, schedule_interval=None) as dag:

    start_task = DummyOperator(task_id='start_task')

    read_and_log_task = SSHOperator(
        task_id='read_and_log_content',
        ssh_conn_id='ssh_executor_local',  # Connection ID from Airflow connections
        command="python /usr/local/pyspark_pipeline/my_python_code.py"  # Command to execute on c2
    )

    end_task = DummyOperator(task_id='end_task')

    start_task >> read_and_log_task >> end_task
