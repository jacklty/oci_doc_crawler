Updated 2025-02-05
# Unversioning an Image
_Find out how to unversion an image in Container Registry._
When you want to clean up the list of images in a repository without actually deleting images, you can remove the version identifier from images in Oracle Cloud Infrastructure Registry (also known as Container Registry). Removing version identifiers is referred to as 'unversioning'.
Your permissions control the images in Container Registry that you can unversion (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can unversion images in repositories you've created, and images in repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can unversion images in any repository in the tenancy.
**Tip**
To view images with no version identifiers in a repository, select **Include unversioned images**.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select the repository in the **Repositories and images** list a second time.
The images in the repository, including their version identifiers, are listed under the repository in the **Repositories and images** list.
    3. Select the image you want.
The image's details section opens.
    4. Select the **Versions** tab and then select **Remove version**.
    5. When prompted, confirm the removal of the version identifier.
  * Use the [oci artifacts container image remove-version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/remove-version.html) command and required parameters to unversion an image:
Command
CopyTry It
```
oci artifacts container image remove-version --image-id  _<image-ocid>_ --image-version _<version>_ [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci artifacts container image remove-version --image-id ocid1.containerimage.oc1.phx.0.ansh81vru1zp.aaaaaaaalqzjyks... --image-version 1.0
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [RemoveContainerVersion](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/RemoveContainerVersion) operation to unversion an image.


Was this article helpful?
YesNo

