import time

import requests

from airflow_dag.github_action.Exception.RequestException import RequestException
from airflow_dag.github_action.Exception.WorkflowException import WorkflowException
from airflow_dag.github_action.utilities import authenticate_to_github
import json


def track_runs(runs: list[dict]) -> bool:
    last_runs: dict = runs[-1]
    if last_runs["status"] == "error":
        raise WorkflowException("Erreur lors de l'execution du Run")
    return last_runs['status'] == "completed"


@authenticate_to_github
def get_all_runs() -> list[dict]:
    self = get_all_runs
    workflow_file = "buildJar.yml"
    url = f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/actions/workflows/{workflow_file}/runs"
    response = requests.get(url, headers=self.headers)
    if response.status_code != 200:
        raise RequestException("Une erreur est survenu lors de la requêtes")
    return sorted(json.loads(response.content)['workflow_runs'], key=lambda x: int(x["id"]))


@authenticate_to_github
def run_workflow(workflow_file: str):
    self = run_workflow
    data = {
        "ref": "main"
    }
    url = f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/actions/workflows/{workflow_file}/dispatches"

    response = requests.post(url, headers=self.headers, json=data)
    time.sleep(5)
    print("En cours execution...")
    while not track_runs(runs := get_all_runs()):
        pass
    print("Workflow executé")
