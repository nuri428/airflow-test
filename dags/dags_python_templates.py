"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
# catchup : 누락된 작업 내용을 한꺼번에 돌림. 

with DAG(
    dag_id="dags_python_templates",
    schedule="0 0 * * *",#crontab 
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "inflearn"]    
) as dag:        
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
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

    python_t1 = PythonOperator(
        task_id="python_t1",
        python_callable=python_function1,
        op_kwargs={'start_date':"{{data_interval_start | ds}}", "end_date":"{{data_interval_end | ds}}"}
    )

    # python_function1 >> python_function3('jhknag')    # python_function1 
    # python_function3('jhknag') >>   python_t1  # python_function1 
    # python_t1 >> python_function3('jhknag') >> python_function2() 
    python_t1 >> python_function2() 
