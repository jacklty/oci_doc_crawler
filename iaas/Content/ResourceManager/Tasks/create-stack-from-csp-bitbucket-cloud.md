Updated 2025-01-07
# Creating a Stack from **Bitbucket Cloud**
Create a stack in Resource Manager from a Terraform configuration stored in **Bitbucket Cloud**. Select a configuration source provider that specifies the **Bitbucket Cloud** information needed to access the configurations.
Ensure that the Terraform configuration is valid. See [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
For information about configuration source providers, see [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-bitbucket-cloud.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-bitbucket-cloud.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-bitbucket-cloud.htm)


  *     1. On the **Configuration source providers** list page, find the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the configuration source provider, select **Create stack from configuration source provider**.
The **Create stack** page opens with the **Bitbucket Cloud** configuration source provider already selected.
    3. Select the **Bitbucket Cloud** workspace, repository, and branch. The list of branches is limited to 100.
For information about **Bitbucket Cloud** workspaces, see <https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/>.
    4. (Optional) To use a directory other than the root directory for running Terraform, specify the working directory. This field is visible when the selected branch has directories. Examples:
       * One level: Directory
       * Two levels: Directory/Subdirectory
    5. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    6. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    7. Select the compartment that you want to store the stack in.
    8. For **Terraform version** , select the version used by the Terraform configuration.
    9. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    10. Select **Next**.
    11. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    12. Select **Next**.
    13. In the **Review** panel, verify the stack configuration.
    14. (Optional) To automatically provision resources on creation of the stack, select **Run apply**.
    15. Select **Create**.
The stack is created and its details page opens.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.
  * Use the `oci resource-manager stack create-from-bitbucket-cloud[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-bitbucket-cloud.html)` command and required parameters to create a stack from **Bitbucket Cloud**.
Copy
```
oci resource-manager stack create-from-bitbucket-cloud --compartment-id <compartment_OCID> --config-source-configuration-source-provider-id <Bitbucket_Cloud_configuration_source_provider_OCID> --config-source-repository-url <Bitbucket_Cloud_repository> --config-source-workspace-id <workspace_ID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from **Bitbucket Cloud**.
For an example of the `configSource` part of the request, see [CreateBitbucketCloudConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketCloudConfigSourceDetails).


Was this article helpful?
YesNo

