# from airflow import DAG
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# from datetime import datetime, timedelta
#
#
# # Define default arguments
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 1, 1),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# # Instantiate DAG
# dag = DAG(
#     dag_id='spark_sample_application',
#     default_args=default_args,
#     schedule_interval=None,
#     catchup=False
# )
#
# # Define SparkSubmitOperator task
# spark_task = SparkSubmitOperator(
#     task_id='spark_job',
#     application='/path/to/your/spark/job.jar',  # Path to your Spark application JAR file
#     total_executor_cores='1',  # Number of executor cores
#     executor_cores='1',  # Number of cores per executor
#     executor_memory='2g',  # Memory per executor
#     driver_memory='1g',  # Memory for Spark driver
#     name='airflow-spark-job',  # Name of the Spark application
#     verbose=True,
#     application_args=['arg1', 'arg2'],  # Additional arguments for your Spark application
#     dag=dag
# )
#
# # Set task dependencies if necessary
# # For example, spark_task.set_upstream(other_task)
#
# # Add DAG to Airflow globals
# globals()['spark_sample_application'] = dag
