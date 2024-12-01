from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


default_dag_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'catchup' : False
}

dag = DAG(
        'show_test_dir',
         default_args=default_dag_args)

t1 = BashOperator(
	task_id='Remove_directory', bash_command='rmdir /opt/airflow/dags/test_dir', dag=dag)

t2 = BashOperator(
	task_id='Make_directory', bash_command='mkdir /opt/airflow/dags/test_dir', dag=dag)


t3 = BashOperator(
	task_id='Show_directory', bash_command='ls /opt/airflow/dags/test_dir ', dag=dag)

t1 >> t2 >> t3   # This is how we set dependency among two tasks
