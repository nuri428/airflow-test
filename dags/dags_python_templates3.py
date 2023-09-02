"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림.

with DAG(
    dag_id="dags_python_templates3",
    schedule="0 0 * * *",#crontab
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "inflearn"]
) as dag:

    @task(task_id='pyton_t1')
    def python_function1():
        import sqlalchemy
        print(sqlalchemy.__version__)
        return ''

    task1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        )

    task1
