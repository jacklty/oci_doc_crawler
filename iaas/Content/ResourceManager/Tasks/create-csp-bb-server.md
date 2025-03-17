Updated 2025-01-07
# Creating a **Bitbucket Server** Configuration Source Provider
Create a configuration source provider in Resource Manager from **Bitbucket Server**.
## Before You Begin 🔗 
Following are the prerequisites to connect Oracle Cloud Infrastructure Resource Manager to **Bitbucket Server**. 

Private server
    
  * Private instance
  * Private IP address connected to a private domain name through a private DNS zone, using [a private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.")
  * Certificate. See [Creating a Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#create-cert "Create a server certificate, certificate chain, and private key for a private Bitbucket server.") and [Importing an Existing Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#import-cert "To access a private Bitbucket server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.")
  * Server must run over HTTPS on port 443 (certificate authority not required)
Port 443 is required for communication with Resource Manager. Port 8443 is the **Bitbucket Server** default. For more information on server setup, see **Bitbucket Server** documentation, such as the following page: <https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html>.



Public server
    
  * Public IP address
  * Server must run over HTTPS with a certificate authority; self-signed certificates aren't allowed
For more information on server setup, see **Bitbucket Server** documentation, such as the following page: <https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html>.



Access token
    
  * Permissions to clone the repository and read the server information
  * Stored as a [secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm) in a [vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm) that you can access (through [policies](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm#permissions)) when creating the configuration source provider


### Creating a Certificate 🔗 
Create a server certificate, certificate chain, and private key for a private Bitbucket server.
  1. Note the passphrase to use for creating the certificate.
  2. [Connect to your private compute instance.](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm)
  3. Create the server certificate.
For example, use the OpenSSL command line application.
     * For Linux, run: `sudo yum install openssl`
     * For MacOS, run: `brew install openssl`
     * For Windows, download the `openssl` binary from [Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) and configure the environment.
Example commands, using `vi` for file creation (you can alternatively use `touch`):
```
sudo openssl genrsa -des3 -out myCA.key 2048
sudo openssl req -x509 -new -nodes -key myCA.key -sha256 -days 1825 -out myCA.pem
sudo openssl genrsa -des3 -out <key-name>.key 2048 
sudo openssl req -new -key <key-name>.key -out <key-name>.csr
sudo vi ./<file-name> 
sudo openssl x509 -req -in <key-name>.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out rms<key-name>.crt -days 825 -sha256 -extfile <key-name>.ext
cat <key-name>.crt
cat myCA.pem
sudo touch cert_chain.crt
```

  4. Create the certificate chain (`cert_chain.crt`):
    1. Copy the contents of <key-name>.crt to the top of `cert_chain.crt`.
    2. Underneath, copy the contents of `myCA.pem`.
The root certificate (`.pem` contents) must follow the individual certificate (`.crt` contents).
    3. Save the file.
  5. Create the private key (`<key-name>.npass.key`) by running the following OpenSSL command:
```
sudo openssl rsa -in <key-name>.key -out <key-name>.npass.key
```



### Importing an Existing Certificate 🔗 
To access a private Bitbucket server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.
For more information about the Certificates service, see [Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm).
  1. Note the passphrase and the locations of the certificate chain, server certificate, and private key.
See [Creating a Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#create-cert "Create a server certificate, certificate chain, and private key for a private Bitbucket server.").
  2. Import the certificate.
See [Importing a Certificate](https://docs.oracle.com/iaas/Content/certificates/importing-certificate.htm).
After the certificate is in the Certificates service, you can select it along with a private endpoint when you [create the configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.").


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm)


  * After completing all the prerequisites, follow these steps in the Console to create a configuration source provider from **Bitbucket Server**.
    1. On the **Configuration source providers** list page, select **Create configuration source provider**. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. In the **Create configuration source provider** panel, enter a name and optional description for the configuration source provider. Avoid entering confidential information.
    3. Select the compartment that you want to store the configuration source provider in.
    4. (Optional) To use a [private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#top "Create, edit, and delete private endpoints in Resource Manager."), follow these steps:
      1. Select **Private endpoint**.
      2. Select or create a private endpoint. To select a private endpoint or certificate in a different compartment, select **Change Compartment**.
      3. Select an SSL certificate.
For more information about private endpoints for private servers, see [Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.").
    5. For **Type** , select **Bitbucket Server**.
    6. Enter the following values:
       * **Server URL** : The **Bitbucket Server** service endpoint. Example: `my-private-bitbucket-server.example.com`
       * **Vault** : [Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm) where the secret is stored.
       * **Secret** : [Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm) for authorization.
    7. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    8. Select **Create**.
    9. To confirm that Resource Manager can access the server URL using the provided authentication information, select the configuration source provider to open its details page, and then select **Validate connection**.
  * Use the `oci resource-manager configuration-source-provider create-bitbucket-server-access-token-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create-bitbucket-server-access-token-provider.html)` command and required parameters to create a configuration source provider from **Bitbucket Server**.
Copy
```
oci resource-manager configuration-source-provider create-bitbucket-server-access-token-provider --api-endpoint <Bitbucket_Server_service_endpoint> --secret-id <secret_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider) operation to create a configuration source provider from **Bitbucket Server**.
For an example of the `configSourceProviderType` part of the request, see [CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails).


## What's Next 🔗 
[Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm#top "Confirm that Resource Manager can access a configuration source provider's server URL with the provided authentication information. You can validate a connection by using the Console only.")
Was this article helpful?
YesNo

