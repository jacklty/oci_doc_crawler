Updated 2025-02-05
# Listing Repositories
_Find out how to list the repositories in Container Registry._
Your permissions control which repositories you can list (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can list repositories that you've created, and repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can list any repository in the tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Container Registry**.
The **Container Registry** list page opens.
    2. Select the region that contains the registry.
    3. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
    4. Select the **Repositories and images** box to display the list.
The **Repositories and images** list displays the repositories in the selected region and compartment to which you have access.
  * Use the [oci artifacts container repository list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/list.html) command and required parameters to list repositories:
Command
CopyTry It
```
oci artifacts container repository list --compartment-id <compartment-ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository list --compartment-id ocid1.compartment.oc1..aaaaaaaaswegb83o...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListContainerRepositories](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/ListContainerRepositories) operation to list repositories.


Was this article helpful?
YesNo

