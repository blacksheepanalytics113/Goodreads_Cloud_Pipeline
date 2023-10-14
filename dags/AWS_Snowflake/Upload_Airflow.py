from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from AWS_Snowflake.upload_rawdata import upload_file



with DAG("Upload_Airflow", start_date=datetime(2023, 10, 11),
schedule_interval='@daily', max_active_runs=1, catchup=False) as dag:

    Goodreads_script_A = PythonOperator(
        task_id="Upload_raw_data",
        python_callable=upload_file
    )

    Goodreads_script_A
    