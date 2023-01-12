from google.oauth2 import service_account

from config import GOOGLE_CREDENTIAL_PATH, GCLOUD_REGION
from gcloud import dataproc

credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_CREDENTIAL_PATH)

jobClient = dataproc.JobControllerClient(credentials=credentials)
clusterClient = dataproc.ClusterControllerClient(credentials=credentials, client_options={
    'api_endpoint': f'{GCLOUD_REGION}-dataproc.googleapis.com:443'})
