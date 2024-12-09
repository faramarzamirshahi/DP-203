# Use blob storage from app code
# https://learn.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-storage-use?tabs=managed-identity%2Ccmd
# read use_blob_auth.md
import os
import uuid

from azure.identity import DefaultAzureCredential

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

credential = DefaultAzureCredential()

# Retrieve the storage blob service URL, which is of the form
# https://<your-storage-account-name>.blob.core.windows.net/
#storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]
from AZURE_VARIABLES import environ
storage_url = environ["AZURE_STORAGE_BLOB_URL"]

# Create the client object using the storage URL and the credential
blob_client = BlobClient(
    storage_url,
    container_name="blob-container-01",
    blob_name=f"sample-blob-{str(uuid.uuid4())[0:5]}.txt",
    credential=credential,
)

# Open a local file and upload its contents to Blob Storage
with open("./Section-02/Resources/ActivityLog-01.csv", "rb") as data:
    blob_client.upload_blob(data)
    print(f"Uploaded ActivityLog-01.csv to {blob_client.url}")

