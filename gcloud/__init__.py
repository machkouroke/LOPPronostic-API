import os
from config import GOOGLE_CREDENTIAL, GOOGLE_CREDENTIAL_PATH
if not (os.path.exists(GOOGLE_CREDENTIAL_PATH)):
    print(GOOGLE_CREDENTIAL, file=open(GOOGLE_CREDENTIAL_PATH, mode="w"))

from google.cloud import dataproc_v1
dataproc = dataproc_v1