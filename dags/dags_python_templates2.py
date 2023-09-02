"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림. 

with DAG(
    dag_id="dags_python_templates2",
    schedule="0 0 * * *",#crontab
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "inflearn"]
) as dag:

    @task(task_id='pyton_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:'+kwargs['ds'])
        print('ds:'+kwargs['ts'])

        print('data_interval_start:'+str(kwargs['data_interval_start']))
        print('data_interval_end:'+str(kwargs['data_interval_end']))
        print('task_instance:'+str(kwargs['ti']))
        return ''

    @task()
    def python_function3(name:str):
        print(f"hello {name}")
        return

    python_function2()  >> python_function3('test')
