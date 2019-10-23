from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from file_writing import filewriting


dag = DAG('hello_world', description='DAG for writing txt files',
          schedule_interval='*/5 * * * *',
          start_date=datetime(2019, 10, 23), catchup=False)

for i in range(20):
    dummy_operator = PythonOperator(task_id='writing files', python_callable=filewriting(i), dag=dag)
    file_operator = PythonOperator(task_id='writing files', python_callable=filewriting(i), dag=dag)
    dummy_operator >> file_operator
