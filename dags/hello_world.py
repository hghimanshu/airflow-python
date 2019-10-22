from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dummy_task import dummyVal


def print_hello():
    return 'Hello world!'


dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='*/3 * * * *',
          start_date=datetime(2019, 10, 22), catchup=False)

dummy_operator = PythonOperator(task_id='task-is-dummy', python_callable=dummyVal, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
