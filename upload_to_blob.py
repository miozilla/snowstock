from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Azure Storage connection string (from Access Keys in Azure Portal)
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# The container created in Azure
container_name = "stockdata"

# Local CSV file path
file_path = "stock_data_output.csv"

# Name to save the file as in blob storage
blob_name = "stock_data_output.csv"

# Connect to Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload the file
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("File uploaded to Azure Blob Storage.")
