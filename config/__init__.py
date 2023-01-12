import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))
X_Auth_Token = os.environ.get("X_Auth_Token")
GOOGLE_CREDENTIAL = os.environ.get("GCLOUD_CREDENTIAL").replace("'", '"')
GOOGLE_CREDENTIAL_PATH = os.environ.get("GCLOUD_CREDENTIAL_PATH")
GCLOUD_PROJECT_ID = os.environ.get("GCLOUD_PROJECT_ID")
GCLOUD_REGION = os.environ.get("GCLOUD_REGION")
