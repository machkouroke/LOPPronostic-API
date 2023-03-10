import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))
X_Auth_Token = os.environ.get("X_AUTH_TOKEN")
GCLOUD_SERVICE_KEY_JSON = os.environ.get("GCLOUD_SERVICE_KEY_JSON").replace("'", '"')
GCLOUD_CREDENTIAL_PATH = os.environ.get("GCLOUD_CREDENTIAL_PATH")
GCLOUD_PROJECT_ID = os.environ.get("GCLOUD_PROJECT_ID")
GCLOUD_REGION = os.environ.get("GCLOUD_REGION")
