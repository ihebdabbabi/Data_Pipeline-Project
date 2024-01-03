from airflow import DAG
from airflow.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def notify_completion(**kwargs):
    # This function can be customized to send a notification or log a message
    print("PySpark job completed successfully!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag_spark = DAG(
    'pyspark_processing',
    default_args=default_args,
    description='Processing NiFi Output with PySpark',
    schedule_interval='@daily',
)

# Task to submit PySpark job
submit_pyspark_job = SparkSubmitOperator(
    task_id='submit_pyspark_job',
    application='./../Data_Pipeline_Project/script.py',  
    conn_id='spark_default',  
    verbose=1,  # Set to 1 for verbose mode
    dag=dag_spark,
)

# Task to notify completion or log a message
notify_task = PythonOperator(
    task_id='notify_completion',
    python_callable=notify_completion,
    provide_context=True,
    dag=dag_spark,
)

# Define task dependencies
submit_pyspark_job >> notify_task

if __name__ == "__main__":
    dag_spark.cli()
