"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from common.common_func import regist2
# catchup : 누락된 작업 내용을 한꺼번에 돌림.

with DAG(
    dag_id="dags_python_decorator_opargs2",
    schedule="0 0 * * *",#crontab
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["inflearn"]
) as dag:

    regist_t1 = PythonOperator(
        task_id='regist_t1',
        python_callable=regist2,
        op_args=['name', 'gender', 'et1c', 'etc2'],
        op_kwargs={'country':'korea','city':'', 'email':'test@email'}
    )
    regist_t1
