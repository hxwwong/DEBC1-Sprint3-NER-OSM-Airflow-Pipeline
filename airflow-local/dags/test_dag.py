from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    'coffee-lake-demo-v2',
    description="Demo of Fem/Hans's Data Pipeline",
    schedule_interval=timedelta(minutes=15),
    start_date=datetime(2022, 6, 17),
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

    t4 = BashOperator(
        task_id="curl",
        bash_command="curl -X POST -H 'Content-type: application/json' --data '{\"text\" : \"presentation time (fem/hans) test!\"}' \"https://discord.com/api/webhooks/986224448984195082/pQp4GNcVWh-J2XtmIycVnjxYuGRGVIYFeveDRS5EwvgmGozthyd_alj8wbeKhfVn9SSk/slack\"",
        dag=dag
    )


    t1 >> t2 >> t3 >> t4
