# from airflow import DAG
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
# from datetime import datetime, timedelta
#
# ###############################################
# # Parameters
# ###############################################
# spark_master = "spark://spark-driver:4040"
#
# # postgres_driver_jar = "/usr/local/spark/resources/jars/postgresql-9.4.1207.jar"
# # movies_file = "/usr/local/spark/resources/data/movies.csv"
# # ratings_file = "/usr/local/spark/resources/data/ratings.csv"
# # postgres_db = "jdbc:postgresql://postgres/test"
# # postgres_user = "test"
# # postgres_pwd = "postgres"
#
# ###############################################
# # DAG Definition
# ###############################################
# now = datetime.now()
#
# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "start_date": datetime(now.year, now.month, now.day),
#     "email": ["airflow@airflow.com"],
#     "email_on_failure": False,
#     "email_on_retry": False,
#     "retries": 1,
#     "retry_delay": timedelta(minutes=1)
# }
#
# dag = DAG(
#         dag_id="spark-test-dag",
#         description="This DAG is a sample dag to test Spark and Airflow together",
#         default_args=default_args,
#         schedule_interval=timedelta(1)
#     )
#
# start = DummyOperator(task_id="start", dag=dag)
#
# spark_job_test_spark = SparkSubmitOperator(
#     task_id="spark_job_test_spark",
#     application="/usr/local/spark/app/load-postgres.py", # Spark application path created in airflow and spark cluster
#     name="test-spark-app",
#     conn_id="spark_default",
#     verbose=1,
#     # conf={"spark.master":spark_master},
#     # application_args=[movies_file,ratings_file,postgres_db,postgres_user,postgres_pwd],
#     # jars=postgres_driver_jar,
#     # driver_class_path=postgres_driver_jar,
#     dag=dag)
#
# end = DummyOperator(task_id="end", dag=dag)
#
# start >> spark_job_test_spark >> end