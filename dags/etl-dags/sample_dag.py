import os
import socket
import urllib

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging


def read_file_and_log_content(file_path):

    cwd = os.getcwd()
    logging.info("++++++++++++++++++++")
    logging.info("Host name is:" + socket.gethostname() + "\n")
    logging.info("Current working directory is:" + cwd + "\n")
    logging.info("++++++++++++++++++++")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            logging.info("File content:\n%s", content)
    except FileNotFoundError:
        logging.error("File not found at path: %s", file_path)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 21),
    'retries': 1
}

with DAG('read_file_dag', default_args=default_args, schedule_interval=None) as dag:
    read_and_log_task = PythonOperator(
        task_id='read_and_log_content',
        python_callable=read_file_and_log_content,
        op_kwargs={'file_path': '/home/executor/sample3.txt'}
    )

