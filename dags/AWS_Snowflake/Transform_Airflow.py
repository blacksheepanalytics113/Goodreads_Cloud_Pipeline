import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from ReadTransform import html_transform

with DAG("Transform_Airflow", start_date=datetime(2023, 10, 11),
schedule_interval='@daily', max_active_runs=1, catchup=False) as dag:

    Goodreads_script_B = PythonOperator(
        task_id="Transform_raw_data",
        python_callable=html_transform
    )

    Goodreads_script_B
    
    
    