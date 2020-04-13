import airflow

from airflow.models import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

def display_variable():
    my_var = Variable.get("my_var")
    print('variable: ' + my_var)
    return my_var

with DAG(dag_id='variable_dag', 
    default_args=default_args, 
    schedule_interval="@once") as dag:

    task = PythonOperator(
        task_id='display_variable',
        python_callable=display_variable
    )
