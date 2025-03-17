Updated 2025-02-05
# Moving a Repository Between Compartments
_Find out how to move a repository in Container Registry from one compartment to another._
When you create a new repository in Container Registry, you specify the compartment in which to create it. Having created the repository in one compartment, you can subsequently move it to a different compartment. For example, to change the users who are authorized to use the repository, or to change how billing for a repository is charged. 
Only users with appropriate permissions can access the repository in the compartment that you move it to.
Your permissions control which repositories you can move, and the compartments that you can move them to (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can move repositories that you've created (and repositories that the groups to which you belong have been granted access by IAM policies) to any compartment to which you have access. If you belong to the Administrators group, you can move any repository in the tenancy to any compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select **Move compartment**.
    3. Select the compartment to which you want to move the repository.
    4. Select **Submit** to move the repository.
The repository is moved to the compartment you selected. Only users with appropriate permissions can now access the repository in the compartment that you've moved it to.
  * Use the [oci artifacts container repository change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/change-compartment.html) command and required parameters to move repositories between compartments:
Command
CopyTry It
```
oci artifacts container repository change-compartment --compartment-id <compartment_ocid_new> --repository-id <repository_ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository change-compartment --compartment-id ocid1.compartment.oc1..aaaaaaaaswegb83o... --repository-id ocid1.containerrepo.oc1.us-phoenix-1.0.ansh81vru1zp.aaaaaaaatxfd94p...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ChangeContainerRepositoryCompartment](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/ChangeContainerRepositoryCompartment) operation to move a repository to a different compartment.


Was this article helpful?
YesNo

