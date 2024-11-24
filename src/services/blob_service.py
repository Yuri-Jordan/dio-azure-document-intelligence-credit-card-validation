from azure.storage.blob import BlobServiceClient
from utils.Config import Config

def upload_blob(file, file_name):
    service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
    client = service_client.get_blob_client(container=Config.CONTAINER_NAME, blob= file_name)
    client.upload_blob(file, overwrite=True)
    return client.url
