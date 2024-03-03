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
    dag_id='test_spark_bash_op_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

# Define BashOperator task to submit Spark application
submit_spark_job = BashOperator(
    task_id='submit_spark_job',
    # bash_command='spark-submit --class your_main_class --master spark://spark:7077 /path/to/your/spark/job.jar arg1 arg2',
    bash_command='spark-submit --py-files /usr/local/pyspark_pipeline/spark_etl-0.0.1 etl/etl_job.py --master localhost:4040 --job-name air_asia_data_job',
    # bash_command='spark-submit --version',
    dag=dag
)

get_spark_ui_url_task = BashOperator(
    task_id='get_spark_ui_url',
    bash_command='echo Spark UI URL: {{ ti.xcom_pull(task_ids="submit_spark_job") }}',  # Access the URL from a previous task
    dag=dag,
)

print_pwd_task = BashOperator(
    task_id='print_pwd',
    bash_command='pwd',  # Command to print the current working directory
    dag=dag,
)

whoami_task = BashOperator(
    task_id='whoami_task',
    bash_command='whoami',  # Command to print the current working directory
    dag=dag,
)

# Add DAG to Airflow globals
submit_spark_job >> get_spark_ui_url_task >> [print_pwd_task, whoami_task]
