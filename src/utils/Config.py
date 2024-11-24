import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("doc-url")
    KEY = os.getenv("key")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("storage-connect-string")
    CONTAINER_NAME = os.getenv("container-name")