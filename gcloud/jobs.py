from config import GCLOUD_PROJECT_ID, GCLOUD_REGION
from gcloud import clients, dataproc


def make_prediction(home_team: str, away_team: str):

    client = clients.jobClient

    # Initialize request argument(s)
    job = dataproc.Job()
    job.placement.cluster_name = "loprono"
    job.spark_job.main_class = "org.lop.Main"
    job.spark_job.jar_file_uris = [
        "gs://lopprono/jar/current.jar"
      ]
    job.spark_job.args = [
        "prediction",
        home_team,
        away_team
    ]

    request = dataproc.SubmitJobRequest(
        project_id=GCLOUD_PROJECT_ID,
        region=GCLOUD_REGION,
        job=job,
    )

    # Make the request
    response = client.submit_job(request=request)

    # Handle the response
    print(response)
