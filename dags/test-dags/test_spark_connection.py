from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.hooks.base_hook import BaseHook
from pyspark.sql import SparkSession

class CustomSparkHook(BaseHook):
    def __init__(self, conn_id='spark_default'):
        self.conn_id = conn_id
        self.connection = self.get_connection(conn_id)

    def test_connection(self):
        try:
            spark = SparkSession.builder \
                .appName("SparkConnectionTest") \
                .master(self.connection.host) \
                .getOrCreate()
            spark.stop()
            return True, None
        except Exception as e:
            return False, str(e)


def test_spark_connection(conn_id='spark_default'):
    spark_hook = CustomSparkHook(conn_id=conn_id)
    success, message = spark_hook.test_connection()
    if success:
        print("Spark connection test succeeded.")
    else:
        print("Spark connection test failed:", message)


def wrapper_test_spark_connection():
    return test_spark_connection('spark_connection')


dag = DAG('test_spark_connection_dag', description='Test Spark Connection DAG',
          schedule_interval=None, start_date=datetime(2024, 1, 1))

test_task = PythonOperator(
    task_id='test_spark_connection_task',
    python_callable=wrapper_test_spark_connection,
    op_kwargs={'conn_id': 'spark_default'},
    dag=dag,
)


test_sc_task = PythonOperator(
    task_id='test_spark_connection_type',
    python_callable=wrapper_test_spark_connection,
    op_kwargs={'conn_id': 'spark_connection'},
    dag=dag,
)

test_task >> test_sc_task
