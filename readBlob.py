import pandas as pd
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
# Import the client object from the SDK library
from azure.storage.blob import BlobClient
# Uploaded ActivityLog-01.csv 
# to https://pythonazurestorage57510.blob.core.windows.net/blob-container-01/sample-blob-bee98.txt
# first set the environment to development so we can load the 
# service principal authentication variables from .env file
# PS > $env:ENVIRONMENT="development"
if ( os.environ['ENVIRONMENT'] == 'development'):
    print("Loading environment variables from .env file")
    load_dotenv(".env")
#print("AZURE_CLIENT_ID: " + os.environ["AZURE_CLIENT_ID"])
#print("AZURE_CLIENT_SECRET: " + os.environ["AZURE_CLIENT_SECRET"])
#print("AZURE_TENANT_ID: " +  os.environ["AZURE_TENANT_ID"])
credential = DefaultAzureCredential()

# Retrieve the storage blob service URL, which is of the form
# https://<your-storage-account-name>.blob.core.windows.net/
#storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]
#from AZURE_VARIABLES import environ
#storage_url = environ["AZURE_STORAGE_BLOB_URL"]
#
## Create the client object using the storage URL and the credential
#blob_client = BlobClient(
#    storage_url,
#    container_name="blob-container-01",
#    blob_name="sample-blob-bee98.txt",
#    credential=credential,
#)
blob_url = 'https://pythonazurestorage57510.blob.core.windows.net/blob-container-01/sample-blob-bee98.txt'
blob_client = BlobClient.from_blob_url(blob_url=blob_url,credential=credential)
stream = blob_client.download_blob()
response = pd.read_csv(stream)
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
rows,columns = response.shape
print ("rows : {:d}, columns : {:d}".format(rows,columns))