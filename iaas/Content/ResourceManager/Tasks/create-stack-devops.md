Updated 2025-01-07
# Creating a Stack from DevOps
Create a stack in Resource Manager from a Terraform configuration stored in DevOps.
Ensure that your Terraform configuration is valid. See [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
For information about DevOps, see [DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **Source code control system**.
    3. Under **Stack configuration** , for **Source code management type** , select **DevOps**.
    4. Select the [DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm) project, repository, and branch that contains the Terraform configuration that you want. The list of branches is limited to 100.
    5. (Optional) To use a directory other than the root directory for running Terraform, specify the working directory. This field is visible when the selected branch has directories. Examples:
       * One level: Directory
       * Two levels: Directory/Subdirectory
    6. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    7. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    8. Select the compartment that you want to store the stack in.
    9. For **Terraform version** , select the version used by the Terraform configuration.
    10. To add a defined tag, select the namespace and key, then enter a value.
    11. To add a free-form tag, enter a key and value.
    12. Select **Next**.
    13. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    14. Select **Next**.
    15. In the **Review** panel, verify the stack configuration.
    16. (Optional) To automatically provision resources on creation of the stack, select **Run apply**.
    17. Select **Create**.
The stack is created and its details page opens.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.
  * Use the `oci resource-manager stack create-stack-create-dev-ops-config-source-details[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-stack-create-dev-ops-config-source-details.html)` command and required parameters to create a stack from DevOps.
Copy
```
oci resource-manager stack create-stack-create-dev-ops-config-source-details --compartment-id <compartment_OCID> --config-source-project-id <devops_project_OCID> --config-source-repository-id <devops_repository_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from DevOps.
For an example of the `configSource` part of the request, see [CreateDevOpsConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateDevOpsConfigSourceDetails).


Was this article helpful?
YesNo

