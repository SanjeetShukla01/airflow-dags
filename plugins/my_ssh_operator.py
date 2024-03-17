import json

from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.utils.decorators import apply_defaults
from