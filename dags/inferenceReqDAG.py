from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from file_writing import filewriting

def checkCond(*args):
    if int(*args) %2 == 0:
        return 'writing_files'


dag = DAG('hello_world', description='DAG for writing txt files',
          schedule_interval='*/5 * * * *',
          start_date=datetime(2019, 10, 23), catchup=False)

for i in range(20):
    branch_op = BranchPythonOperator(task_id='branch_task', provide_context=True, python_callable=checkCond, 
                                        op_args=i, dag=dag)
    file_operator = PythonOperator(task_id='writing_files', python_callable=filewriting, 
                                        op_args=i, dag=dag)
    branch_op >> file_operator
