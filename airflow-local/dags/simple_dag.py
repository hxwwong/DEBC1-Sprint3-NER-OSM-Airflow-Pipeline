from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    'bash_operator_example',
    description='Example of using bash scripts',
    schedule_interval=timedelta(minutes=15),
    start_date=datetime(2022, 6, 15),
    catchup=False,
    tags=['examples'],
) as dag:

    # The start of the data interval as YYYY-MM-DD
    date = "{{ ds }}"

    t1 = BashOperator(
        task_id="test_env",
        bash_command="echo $DATA_INTERVAL_START",
        dag=dag,
        env={"DATA_INTERVAL_START": date},
    )

    t2 = BashOperator(
        task_id="sleep",
        bash_command="sleep 5",
        dag=dag
    )

    t3 = BashOperator(
        task_id="echo",
        bash_command="echo 'Finished!'",
        dag=dag
    )

    t1 >> t2 >> t3
