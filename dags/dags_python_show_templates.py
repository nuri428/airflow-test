"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림. 

with DAG(
    dag_id="dags_python_show_templates",
    schedule="0 0 * * *",#crontab 
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=True,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "example2"],
    params={"example_key": "example_value"}, # task에 공통적으로 넘길 파라메터 
) as dag:    
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()