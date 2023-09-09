"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림.

with DAG(
    dag_id="dags_python_decorator",
    schedule="0 0 * * *",#crontab
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["inflearn"]
) as dag:
    @task(task_id="python_task1")
    def print_content(some_input):
        print(some_input)
    python_task1 = print_content("task_decorator 실행")
