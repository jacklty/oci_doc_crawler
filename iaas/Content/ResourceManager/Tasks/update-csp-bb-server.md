Updated 2024-10-08
# Updating a **Bitbucket Server** Configuration Source Provider
Update a **Bitbucket Server** configuration source provider in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-server.htm)


  *     1. On the **Configuration source providers** list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. On the configuration source provider's details page, select **Edit**.
    3. To change the connection details, in the **Edit configuration source provider** panel, edit one or more of the following values:
       * To use a different [private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises."), select the endpoint and then select an SSL certificate. This option is available when the configuration source provider was created with a private endpoint.
       * **Server URL** : The **Bitbucket Server** service endpoint. Example: `my-private-bitbucket-server.example.com`
       * **Vault** : [Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm) where the secret is stored.
       * **Secret** : [Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm) for authorization.
    4. Optionally change the compartment, name, or description.
    5. Select **Save changes**.
  * Use the `oci resource-manager configuration-source-provider update-bitbucket-server-access-token-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/update-bitbucket-server-access-token-provider.html)` command and required parameters to update a configuration source provider from **Bitbucket Server**.
Copy
```
oci resource-manager configuration-source-provider update-bitbucket-server-access-token-provider --configuration-source-provider-id <configuration_source_provider_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [UpdateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/UpdateConfigurationSourceProvider) operation to update a configuration source provider that uses **Bitbucket Server**.
For an example of the `configSourceProviderType` part of the request, see [UpdateBitbucketServerAccessTokenConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateBitbucketServerAccessTokenConfigurationSourceProviderDetails).


Was this article helpful?
YesNo

