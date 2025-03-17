Updated 2025-01-07
# Creating a **Bitbucket Cloud** Configuration Source Provider
Create a configuration source provider in Resource Manager from **Bitbucket Cloud**.
## Before You Begin 🔗 
To connect Oracle Cloud Infrastructure Resource Manager to a **Bitbucket Cloud** repository, you must have Read permissions to the repository. For more information, see [Grant repository access to users and groups](https://support.atlassian.com/bitbucket-cloud/docs/grant-repository-access-to-users-and-groups/) and [Configure project permissions for users and groups](https://support.atlassian.com/bitbucket-cloud/docs/configure-project-permissions-for-users-and-groups/).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm)


  * After completing all the prerequisites, follow these steps in the Console to create a configuration source provider from **Bitbucket Cloud**.
    1. On the **Configuration source providers** list page, select **Create configuration source provider**. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. In the **Create configuration source provider** panel, enter a name and optional description for the configuration source provider. Avoid entering confidential information.
    3. Select the compartment that you want to store the configuration source provider in.
    4. (Optional) To use a [private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#top "Create, edit, and delete private endpoints in Resource Manager."), follow these steps:
      1. Select **Private endpoint**.
      2. Select or create a private endpoint. To select a private endpoint or certificate in a different compartment, select **Change Compartment**.
      3. Select an SSL certificate.
For more information about private endpoints for private servers, see [Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.").
    5. For **Type** , select **Bitbucket Cloud**.
    6. Enter the following values:
       * **Server URL** : The **Bitbucket Cloud** service endpoint. Example: <https://bitbucket.org/>
       * **Vault** : [Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm) where the secret is stored.
       * **Secret** : [Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm) for authorization.
    7. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    8. Select **Create**.
    9. To confirm that Resource Manager can access the server URL using the provided authentication information, select the configuration source provider to open its details page, and then select **Validate connection**.
  * Use the `oci resource-manager configuration-source-provider create-bitbucket-cloud-username-app-password-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create-bitbucket-cloud-username-app-password-provider.html)` command and required parameters to create a configuration source provider from **Bitbucket Cloud**.
Copy
```
oci resource-manager configuration-source-provider create-bitbucket-cloud-username-app-password-provider --api-endpoint <Bitbucket_Cloud_service_endpoint> --secret-id <secret_OCID> -username <username>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider) operation to create a configuration source provider from **Bitbucket Cloud**.
For an example of the `configSourceProviderType` part of the request, see [CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails).


## What's Next 🔗 
[Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm#top "Confirm that Resource Manager can access a configuration source provider's server URL with the provided authentication information. You can validate a connection by using the Console only.")
Was this article helpful?
YesNo

