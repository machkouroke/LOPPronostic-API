from config import GCLOUD_PROJECT_ID, GCLOUD_REGION
from gcloud import clients, dataproc


def sample_submit_job():

    client = clients.jobClient

    # Initialize request argument(s)
    job = dataproc.Job()
    job.placement.cluster_name = "loprono"
    job.spark_job.main_class = "org.lop.Main"
    job.spark_job.jar_file_uris = [
        "gs://lopprono/start4.0.jar"
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
