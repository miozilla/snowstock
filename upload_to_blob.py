from azure.storage.blob import BlobServiceClient

connect_str = "Your_Azure_Connection_String"
container_name = "your-container-name"
file_path = "stock_data_output.csv"
blob_name = "stock_data_output.csv"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("File uploaded to Azure Blob Storage.")
