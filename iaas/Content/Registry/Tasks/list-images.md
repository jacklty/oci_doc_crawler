Updated 2025-02-05
# Listing Images
_Find out how to list the images in repositories in Container Registry._
Using the Console, you can list all the images in a repository. Using the CLI and the API, you have more options to filter the list of images.
Your permissions control which images you can list (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can list images in repositories that you've created, and in repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can list images in any repository in the tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select the repository in the **Repositories and images** list a second time.
The images in the repository, including their version identifiers, are listed under the repository in the **Repositories and images** list.
  * Use the [oci artifacts container image list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/list.html) command and required parameters to list images:
Command
CopyTry It
```
oci artifacts container image list --compartment-id <compartment-ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container image list --compartment-id ocid1.compartment.oc1..aaaaaaaaswegb83o...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListContainerImages](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImageSummary/ListContainerImages) operation to list images.


Was this article helpful?
YesNo

