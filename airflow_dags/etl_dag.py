from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

default_args = {
    'owner': 'zenith',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('apparel_etl_dag', default_args=default_args, schedule_interval='@daily') as dag:
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        op_kwargs={'file_path': 'data/sales_data.xlsx'}
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        op_kwargs={'output_path': 'data/transformed_sales.csv'}
    )

    extract_task >> transform_task >> load_task
