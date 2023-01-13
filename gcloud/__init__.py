import os
from config import GCLOUD_SERVICE_KEY_JSON, GCLOUD_CREDENTIAL_PATH

if not (os.path.exists(GCLOUD_CREDENTIAL_PATH)):
    print(GCLOUD_SERVICE_KEY_JSON, file=open(GCLOUD_CREDENTIAL_PATH, mode="w"))

from google.cloud import dataproc_v1

dataproc = dataproc_v1
