"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime
import random 
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림.

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *",#crontab
    start_date=pendulum.datetime(2021, 9, 8, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "inflearn"]
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCARD']
        rand_int = random.randint(0,len(fruit)-1)
        print(fruit[rand_int])
        
    py_t1 = PythonOperator(task_id='dags_python_operator',
                           python_callable=select_fruit
                           )
    
    py_t1
