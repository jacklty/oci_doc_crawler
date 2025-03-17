Updated 2025-01-07
# Creating a Stack from **Bitbucket Cloud**
Create a stack in Resource Manager from a Terraform configuration stored in **Bitbucket Cloud**. Select a configuration source provider that specifies the **Bitbucket Cloud** information needed to access the configurations.
Ensure that the Terraform configuration is valid. See [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
For information about configuration source providers, see [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **Source code control system**.
    3. Under **Stack configuration** , for **Source code management type** , select **Bitbucket Cloud**.
    4. Select the **Bitbucket Cloud** configuration source provider that you want.
If you need to create a configuration source provider, select **Create configuration source provider** and enter values. For information about the fields, see [Creating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#top "Create a configuration source provider in Resource Manager from Bitbucket Cloud.").
    5. Select the **Bitbucket Cloud** workspace, repository, and branch. The list of branches is limited to 100.
For information about **Bitbucket Cloud** workspaces, see <https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/>.
    6. (Optional) To use a directory other than the root directory for running Terraform, specify the working directory. This field is visible when the selected branch has directories. Examples:
       * One level: Directory
       * Two levels: Directory/Subdirectory
    7. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    8. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    9. Select the compartment that you want to store the stack in.
    10. For **Terraform version** , select the version used by the Terraform configuration.
    11. To add a defined tag, select the namespace and key, then enter a value.
    12. To add a free-form tag, enter a key and value.
    13. Select **Next**.
    14. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    15. Select **Next**.
    16. In the **Review** panel, verify the stack configuration.
    17. (Optional) **Run apply**
    18. Select **Create**.
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

