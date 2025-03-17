Updated 2025-02-05
# Deleting a Repository
_Find out how to delete a repository from Container Registry._
There is a limit to the number of repositories that you can have in any given region in a tenancy. So when you no longer need a repository, delete it from Container Registry. Any images in a repository are deleted when you delete the repository.
Your permissions control which repositories you can delete (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can delete repositories that you've created, and repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can delete any repository in the tenancy.
When you delete a repository, it can take up to 48 hours for the deletion to take effect and for storage to be released. If you're deleting repositories to release storage, you can also [contact us](https://support.oracle.com/) to obtain more storage.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingrepos.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingrepos.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingrepos.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select **Delete repository**.
    3. When prompted, confirm the deletion.
The repository you deleted is permanently removed from Container Registry. It no longer appears in the **Repositories and images** list
  * Use the [oci artifacts container repository delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/delete.html) command and required parameters to delete a repository:
Command
CopyTry It
```
oci artifacts container repository delete --repository-id <repository-ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository delete --repository-id ocid1.containerrepo.oc1.us-phoenix-1.0.ansh81vru1zp.aaaaaaaaswec83o...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DeleteContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/DeleteContainerRepository) operation to delete a repository.


Was this article helpful?
YesNo

