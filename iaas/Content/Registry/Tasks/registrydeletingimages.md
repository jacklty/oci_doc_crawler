Updated 2025-02-05
# Deleting an Image
_Find out how to delete an image from Container Registry._
When you no longer need an image or you want to clean up the list of image versions in a repository, you can delete images from Container Registry.
Your permissions control which images you can delete (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can delete images from repositories that you've created, and from repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can delete images from any repository in the tenancy.
In addition to deleting individual images as described in this topic, you can set up image retention policies to delete images automatically based on selection criteria that you specify. See [Retaining and Deleting Images Using Retention Policies](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymanagingimageretention.htm#Retaining_and_Deleting_Images_Using_Retention_Policies "Find out how to set up and use image retention policies with Container Registry.").
When you delete an image, it can take up to 48 hours for the deletion to take effect and for storage to be released. If you're deleting images to release storage, you can also [contact us](https://support.oracle.com/) to obtain more storage.
You can undelete an image that you've previously deleted, for up to 48 hours after you deleted it (see [Undeleting (Restoring) an Image](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm#undelete-image "Find out how to undelete \(restore\) an image from Container Registry.")). After that time, the image is permanently removed from Container Registry.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select the repository in the **Repositories and images** list a second time.
The images in the repository, including their version identifiers, are listed under the repository in the **Repositories and images** list.
    3. Select the image you want.
The image's details section opens.
    4. Select **Delete image**.
    5. When prompted, confirm the deletion.
The image you deleted no longer appears under the associated repository in the **Repositories and images** list.
  * Use the [oci artifacts container image delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/delete.html) command and required parameters to delete an image:
Command
CopyTry It
```
oci artifacts container image delete --image-id  _<image-ocid>_ [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container image delete --image-id ocid1.containerimage.oc1.phx.0.ansh81vru1zp.aaaaaaaalqzjyks...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DeleteContainerImage](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/DeleteContainerImage) operation to delete an image.


Was this article helpful?
YesNo

