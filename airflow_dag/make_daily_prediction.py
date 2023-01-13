from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow_dag.github_action.Workflow import run_workflow

default_args = {
    'owner': 'me',
    'start_date': datetime(2023, 1, 13),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'build_jar',
    default_args=default_args,
    schedule='0 0 * * *',  # runs every day at 00:00
)


def launch_jar_build():
    run_workflow("buildJar.yml")
    return True


task = PythonOperator(
    task_id='get_jar',
    python_callable=launch_jar_build,
    dag=dag,
)
