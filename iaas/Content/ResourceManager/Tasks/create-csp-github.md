Updated 2025-01-07
# Creating a GitHub Configuration Source Provider
Create a configuration source provider in Resource Manager from GitHub.
## Before You Begin 🔗 
Following are the prerequisites to connect Oracle Cloud Infrastructure Resource Manager to GitHub.
  * **Private Git server** : Network information is required to set up a private endpoint for use with the configuration source provider, including an [SSL certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert "To access a private GitHub server, make its associated SSL certificate available in the OCI Certificates service."). For more information, see [Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.").
  * **Public Git server** : This server must be accessible over the internet using a [public IP address](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
  * **Resolvable URL** : Ensure that Resource Manager can resolve the server URL. Ensure that the server is deployed with a well-known root certificate, such as `DigiCert`, so that OCI can trust its endpoint.
  * **APIs** : Your GitHub server must use GitHub APIs. An example of a GitHub server that doesn't meet this prerequisite is an Azure native GitHub solution ([example](https://docs.microsoft.com/en-us/azure/devops/boards/github/connect-on-premises-to-github)).
  * **Network configuration for IP addresses** : Configure your network to allow access from OCI [IP address ranges](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm). Ensure that you include ranges for all relevant services, including the Oracle Services Network (tag: `OSN`).
  * **Ingress rules** : Enable network ingress rules on the VCN where the server is deployed to allow access from OCI IP addresses.
  * **Repository permissions** : You must have admin or owner permissions for the repository. 
  * **Personal access token (PAT)** : You must have a PAT to the server. To create a PAT, see the relevant guidance and documentation:
    * The scope `repo` (which includes `repo:status`, `repo_deployment`, and `public_repo`) is required for use with Resource Manager. See <https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token>
    * For GitHub Enterprise Cloud, single sign-on (SSO) must be enabled on the PAT. See [Authenticating with SAML single sign-on (GitHub site)](https://docs.github.com/en/authentication/authenticating-with-saml-single-sign-on).
**Note** Resource Manager reads the customer's repository content but doesn't push changes to the repository.


### Importing an Existing Certificate 🔗 
To access a private GitHub server, make its associated SSL certificate available in the OCI Certificates service.
For more information about the Certificates service, see [Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm).
After the certificate is in the Certificates service, you can select it along with a private endpoint when you [create the configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.").
  1. Get the certificate information for your private Git server.
    1. Install the OpenSSL command line application.
For Linux, run: `sudo yum install openssl`
For MacOS, run: `brew install openssl`
For Windows, download the `openssl` binary from [Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) and configure the environment.
    2. Get the certificate chain.
Run the following command, replacing $SERVERNAME with the server URL and $PORT with the server's TCP port:
Copy
```
openssl s_client -connect $SERVERNAME:$PORT -servername $SERVERNAME -showcerts 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certChain.pem
```

    3. Get the server certificate.
Run the following command, replacing $SERVERNAME with the server URL and $PORT with the server's TCP port:
Copy
```
echo -n | openssl s_client -connect $SERVERNAME:$PORT -servername $SERVERNAME | openssl x509 > $SERVERNAME.pem
```

    4. Get the private key.
Example source of private key from NGINX Gitlab Server (`/etc/gitlab/gitlab.rb`):
Copy
```
nginx['ssl_certificate_key'] = <Path_to_PRIVATE_KEY>
```

  2. Import the certificate.
See [Importing a Certificate](https://docs.oracle.com/iaas/Content/certificates/importing-certificate.htm).
After the certificate is in the Certificates service, you can select it along with a private endpoint when you [create the configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.").


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm)


  * After completing all the prerequisites, follow these steps in the Console to create a configuration source provider from GitHub.
    1. On the **Configuration source providers** list page, select **Create configuration source provider**. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. In the **Create configuration source provider** panel, enter a name and optional description for the configuration source provider. Avoid entering confidential information.
    3. Select the compartment that you want to store the configuration source provider in.
    4. (Optional) To use a [private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#top "Create, edit, and delete private endpoints in Resource Manager."), follow these steps:
      1. Select **Private endpoint**.
      2. Select or create a private endpoint. To select a private endpoint or certificate in a different compartment, select **Change Compartment**.
      3. Select an SSL certificate.
For more information about private endpoints for private servers, see [Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.").
    5. For **Type** , select **GitHub**.
    6. Enter the following values:
       * **Server URL** : The service endpoint.
Examples:
         * GitHub Enterprise Cloud: `https://github.com/org-name`
         * GitHub Enterprise Server: `https://hostname/api/v3`
         * GitHub Free for Organization: `https://github.com/org-name`
         * GitHub Free for User Accounts: `https://github.com`
         * GitHub team: `https://github.com/team-name`
       * **Personal access token** : Enter the personal access token (PAT).
    7. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    8. Select **Create**.
    9. To confirm that Resource Manager can access the server URL using the provided authentication information, select the configuration source provider to open its details page, and then select **Validate connection**.
  * Use the `oci resource-manager configuration-source-provider create-github-access-token-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create-github-access-token-provider.html)` command and required parameters to create a configuration source provider from GitHub.
Copy
```
oci resource-manager configuration-source-provider create-github-access-token-provider --access-token <personal_access_token> --api-endpoint <GitHub_service_endpoint>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider) operation to create a configuration source provider from GitHub.
For an example of the `configSourceProviderType` part of the request, see [CreateGithubAccessTokenConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateGithubAccessTokenConfigurationSourceProviderDetails).


## What's Next 🔗 
[Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm#top "Confirm that Resource Manager can access a configuration source provider's server URL with the provided authentication information. You can validate a connection by using the Console only.")
Was this article helpful?
YesNo

