# How to Get Azure Client ID
The Client ID in Azure is a unique identifier for an application registered in Azure Active Directory (Azure AD).<br>
It is essential for authenticating and authorizing applications to access Azure resources. <br>
Here are the steps to find the Client ID in the Azure portal:<br>

# Examples
Code samples for this package can be found at:

* [Search Security Center Management](https://learn.microsoft.com/en-us/samples/browse/?languages=python&term=Getting%20started%20-%20Managing&terms=Getting%20started%20-%20Managing) on docs.microsoft.com
* [Azure Python Mgmt SDK Samples Repo](https://aka.ms/azsdk/python/mgmt/samples)

# Authenticate with DefaultAzureCredential
The DefaultAzureCredential object will look for the service principal information in a set of environment variables at runtime. Since most developers work on multiple applications, it's recommended to use a package like [python-dotenv](https://pypi.org/project/python-dotenv/) to access environment from a .env file stored in the application's directory during development. 

### [Python format print](https://pyformat.info/)