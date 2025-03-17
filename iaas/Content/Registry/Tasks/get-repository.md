Updated 2025-02-05
# Getting a Repository's Details
_Find out how to get details of a specific repository in Container Registry._
You can get detailed information about the repositories in Container Registry. 
Your permissions control which repositories you can get information about (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can get information about repositories that you've created, and repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can get information about any repository in the tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm)


  * On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens. It contains information about the repository, both general information and commands to run other tasks.
  * Use the [oci artifacts container repository get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/get.html) command and required parameters to get details of a repository:
Command
CopyTry It
```
oci artifacts container repository get --repository-id <repository-ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository get --repository-id ocid1.containerrepo.oc1.us-phoenix-1.0.ansh81vru1zp.aaaaaaaaswec83o...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/GetContainerRepository) operation to get details of a repository.


Was this article helpful?
YesNo

