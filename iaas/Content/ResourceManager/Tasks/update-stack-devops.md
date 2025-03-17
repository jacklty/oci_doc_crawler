Updated 2024-10-08
# Updating the DevOps Location for a Stack
Update the DevOps repository or other location details used by a stack in Resource Manager. The updated location is used when you run jobs on the stack.
**Note** For information about configuration source providers, see [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** page, select a different [DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm) repository or branch.
    4. Change other values as needed.
For information about the fields, see [Creating a Stack from DevOps](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in DevOps.").
    5. Select **Next** twice.
    6. Select **Save changes**.
  * Use the `oci resource-manager stack update-stack-update-dev-ops-config-source-details[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update-stack-update-dev-ops-config-source-details.html)` command and required parameters to update the DevOps location used by a stack.
Copy
```
oci resource-manager stack update-from-devops --stack-id <stack_OCID> --config-source-project-id <DevOps_project_OCID> --config-source-repository-id <DevOps_repository_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the DevOps location used by a stack.
For an example of the `configSource` part of the request, see [UpdateDevOpsConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateDevOpsConfigSourceDetails).


Was this article helpful?
YesNo

