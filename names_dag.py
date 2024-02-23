# This script defines an Airflow DAG (Directed Acyclic Graph) for orchestrating
# an ETL (Extract, Transform, Load) process from Google Cloud Storage (GCS)
# to BigQuery (BQ).

import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.operators.python import PythonOperator
#from twitter_etl.py
from names_etl import extract_transform_load  # Import custom Python function for ETL

# Custom Python logic for deriving data value
yesterday = datetime.combine(datetime.today() - timedelta(1), datetime.min.time())

# Default arguments for Airflow DAG
default_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
with DAG(dag_id='GCS_ETL_BQ_FINAL_V18.0',
         catchup=False,
         schedule_interval=timedelta(days=1),
         default_args=default_args
         ) as dag:
    
    # Define dummy start task
    start = DummyOperator(
        task_id="Start",
        dag=dag   
    )
    
    # Define dummy end task
    end = DummyOperator(
        task_id="end",
        dag=dag   
    )
    
    # Define PythonOperator for ETL process
    transform = PythonOperator(
        task_id="extract_transform_load",
        python_callable=extract_transform_load,
        dag=dag
    )
    
    # Define GoogleCloudStorageToBigQueryOperator for loading data from GCS to BQ
    gcs_to_bq_load = GoogleCloudStorageToBigQueryOperator(
                task_id='gcs_to_bq_load',
                bucket='etl-with-composerflow',
                source_objects=['data_files/new_data.csv'],
                source_format='CSV',
                destination_project_dataset_table='gcs_to_bq_dataset.gcs_to_bq_table',
                schema_fields=[
                                {'name': 'Name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                {'name': 'Gender', 'type': 'STRING', 'mode': 'NULLABLE'},
                                {'name': 'Count', 'type': 'STRING', 'mode': 'NULLABLE'}
                              ],
                skip_leading_rows=1,
                create_disposition='CREATE_IF_NEEDED',
                write_disposition='WRITE_TRUNCATE', 
                autodetect=True,
                dag=dag)

# Define task dependencies
start >> transform >> gcs_to_bq_load >> end
