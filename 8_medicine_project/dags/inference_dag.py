from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.decorators import task
from datetime import datetime
repo = "/home/alex_kondrashov7/Экзамен Инжиниринг"
etl  = f"{repo}/etl"
with DAG (dag_id='breast_cancer_inference', schedule_interval= '* * * * *',start_date=datetime(2025, 6, 15), catchup=False) as dag:
    prepare = BashOperator(task_id='prepare',
                           bash_command=(
                               f"python {etl}/01_prepare.py " f"--input {repo}/data.csv " f"--ids_out {repo}/ids.csv "f"--feat_out {repo}/feats.parquet"))

    
    predict = BashOperator(task_id='predict',
            bash_command=(f"python {etl}/02_predict.py "f"--feat {repo}/feats.parquet "f"--selector {repo}/selector_model.pkl "f"--model {repo}/voting_model.pkl "f"--proba_out {repo}/proba.csv")
    )

    submit = BashOperator(task_id='make_csv',
            bash_command=(f"python {etl}/03_make_csv.py " f"--ids {repo}/ids.csv " f"--proba {repo}/proba.csv " f"--dst_dir {repo}/results")
    )

    prepare >> predict >> submit
