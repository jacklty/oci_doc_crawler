Updated 2024-10-08
# Updating the Git Configuration Source Provider for a Stack
Update the Git configuration source provider used by a stack in Resource Manager. The updated configuration source provider is used when you run jobs on the stack.
For more information about configuration source providers, see [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** page, select a different Git configuration source provider.
If you need to create a Git configuration source provider, select **Create configuration source provider** and enter values. For information about these fields, see [Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#top "Create a configuration source provider in Resource Manager from GitHub.") and [Creating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#top "Create a configuration source provider in Resource Manager from GitLab.").
    4. Select the Git repository and branch.
    5. Change other values as needed.
For information about the fields, see [Creating a Stack from Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.").
    6. Select **Next** twice.
    7. Select **Save changes**.
  * Use the `oci resource-manager stack update-from-git-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update-from-git-provider.html)` command and required parameters to update a stack's configuration source provider.
Copy
```
oci resource-manager stack update-from-git-provider --stack-id <stack_OCID> --config-source-configuration-source-provider-id <Git_configuration_source_provider_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the Git configuration source provider used by a stack.
For an example of the `configSource` part of the request, see [UpdateGitConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateGitConfigSourceDetails).


Was this article helpful?
YesNo

