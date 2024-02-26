from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate DAG
dag = DAG(
    dag_id='spark_sample_application_bash',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

# Define BashOperator task to submit Spark application
submit_spark_job = BashOperator(
    task_id='submit_spark_job',
    bash_command='spark-submit --class your_main_class --master spark://spark:7077 /path/to/your/spark/job.jar arg1 arg2',
    dag=dag
)

# Add DAG to Airflow globals
globals()['spark_sample_application'] = dag
