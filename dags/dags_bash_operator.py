"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# catchup : 누락된 작업 내용을 한꺼번에 돌림. 

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",#crontab 
    start_date=pendulum.datetime(2021, 8, 31, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), timeout 
    tags=["example", "example2"],
    params={"example_key": "example_value"}, # task에 공통적으로 넘길 파라메터 
) as dag:    

    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo $whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t3 = BashOperator(
        task_id="bash_t3",
        env={
            "START_DATE":"{{data_interval_start | ds}}",
            "END_DATE":"{{data_interval_end | ds}}"
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    # [END howto_operator_bash]
    bash_t1 >> bash_t2 >> bash_t3
