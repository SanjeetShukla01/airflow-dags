# airflow-dags





# How to run a DAG to test
Configure spark connection acessing airflow web UI http://localhost:8080 and going to Connections
![airflow_ui_connection.png](resources/airflow_ui_connection.png)

## ToDo

Airflow Sensors
Xcom
Latest ways to write a dag.
Notifications
Airflow Object Storage

### SQL Library
### Kafka
### Start piecing together


`
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/dags:$(pwd)/dags/test-dags:$(pwd)/dags/etl-dags:$(pwd)/dags/util-dags:$(pwd)/venv/lib/python3.10/site-packages/airflow/providers/apache/spark/operators
`