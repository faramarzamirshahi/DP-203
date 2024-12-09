### Setup service principal
If you run the use_blob_auth.py the command fails
azure.core.exceptions.HttpResponseError: This request is not authorized to perform this operation using this permission.

We need to create a service principal
```
Group
    az ad sp : Manage Azure Active Directory service principals for automation authentication.

Subgroups:
    credential      : Manage a service principal's password or certificate credentials.
    owner           : Manage service principal owners.

Commands:
    create          : Create a service principal.
    create-for-rbac : Create a service principal and configure its access to Azure resources.
    delete          : Delete a service principal.
    list            : List service principals.
    show            : Get the details of a service principal.
    update          : Update a service principal.
```

`PS > $env:AZURE_STORAGE_BLOB_URL="https://pythonazurestorage57510.blob.core.windows.net"`

`PS > E:\Sync\PROJECTS\DP-203> az ad sp create-for-rbac --name "storage account service"`

### RESPONSE
```
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "440eebef-6ad7-4db8-97b7-8f2c0b82b741",
  "displayName": "storage account service",
  "password": "Ivq8Q~vW8yal3czYU.bP-tarmlsKJwp21RUEycRO",
  "tenant": "baee6a44-bf1c-4770-852b-c4c1711e2e8e"
}
```
Now set the environment variables<br>
```
PS > $env:AZURE_CLIENT_ID="440****-6ad7-4db8-97b7-******82b741"
PS > $env:AZURE_TENANT_ID="bae*****-bf1c-4770-852b-******1e2e8e"
PS > $env:AZURE_CLIENT_SECRET="Ivq*****8yal3czYU.bP-tarmlsK******UEycRO"
PS > $env:AZURE_SUBSCRIPTION_ID="40fd581f-fb8a-4fee-b60c-7d3808f3379c"
```
And assign role<br>

<b>`PS > az role assignment create --assignee $env:AZURE_CLIENT_ID --role "Storage Blob Data Contributor" --scope "/subscriptions/$env:AZURE_SUBSCRIPTION_ID/resourceGroups/PythonAzureExample-rg/providers/Microsoft.Storage/storageAccounts/pythonazurestorage57510/blobServices/default/containers/blob-container-01"`</b>

### response
```
{
  "condition": null,
  "conditionVersion": null,
  "createdBy": "6b213707-d0df-4b66-9608-cde83aa90f3e",
  "createdOn": "2024-12-06T21:51:36.975624+00:00",
  "delegatedManagedIdentityResourceId": null,
  "description": null,
  "id": "/subscriptions/40fd581f-fb8a-4fee-b60c-7d3808f3379c/resourceGroups/PythonAzureExample-rg/providers/Microsoft.Storage/storageAccounts/pythonazurestorage57510/blobServices/default/containers/blob-container-01/providers/Microsoft.Authorization/roleAssignments/d6bb4042-0cc3-4447-abb8-8a757eb45382",
  "name": "d6bb4042-0cc3-4447-abb8-8a757eb45382",
  "principalId": "7f4a3f55-aff4-49cd-8d0c-cd7283e6a46f",
  "principalName": "440eebef-6ad7-4db8-97b7-8f2c0b82b741",
  "principalType": "ServicePrincipal",
  "resourceGroup": "PythonAzureExample-rg",
  "roleDefinitionId": "/subscriptions/40fd581f-fb8a-4fee-b60c-7d3808f3379c/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe",
  "roleDefinitionName": "Storage Blob Data Contributor",
  "scope": "/subscriptions/40fd581f-fb8a-4fee-b60c-7d3808f3379c/resourceGroups/PythonAzureExample-rg/providers/Microsoft.Storage/storageAccounts/pythonazurestorage57510/blobServices/default/containers/blob-container-01",
  "type": "Microsoft.Authorization/roleAssignments",
  "updatedBy": "6b213707-d0df-4b66-9608-cde83aa90f3e",
  "updatedOn": "2024-12-06T21:51:36.975624+00:00"
}
```
### Now you can run the script to upload the file onto blob
```
 & E:/Sync/PROJECTS/DP-203/.venv/Scripts/python.exe e:/Sync/PROJECTS/DP-203/use_blob_auth.py
```

### Response                                                                
```
Uploaded ActivityLog-01.csv to https://pythonazurestorage57510.blob.core.windows.net/blob-container-01/sample-blob-bee98.txt
```

## Delete the service application principal
`az ad app delete --id <AZURE_CLIENT_ID>`