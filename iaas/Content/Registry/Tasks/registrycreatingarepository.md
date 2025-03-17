Updated 2025-02-05
# Creating a Repository
_Find out how to create a repository in Container Registry._
After you create a repository, you can push an image to it using the Docker CLI (see [Pushing Images Using the Docker CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm#Pushing_Images_Using_the_Docker_CLI "Find out how to push images to Container Registry using the Docker CLI.")). Any images that you subsequently push to the registry that include the same repository name are grouped into that repository.
Creating a repository _before_ pushing an image is the usual workflow, but it's not always necessary. If you're not authorized to manage repositories in the tenancy's root compartment, you must always push an image to an existing repository. However, if you are authorized to push images to the tenancy's root compartment and you intend to do so, an existing repository is not necessary. 
When you push an image, you normally use a command in the format `docker push <registry-domain>/<tenancy-namespace>/<repo-name>:<version>`. However, if you select the **Create repository on first push in root compartment** option and push an image with a command that includes the name of a repository that doesn't already exist, a new private repository is created automatically in the root compartment. 
For example, if you enter the command `docker push ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project02/acme-web-app:7.5.2` and the `project02/acme-web-app` repository doesn't exist, a private repository called `project02/acme-web-app` is created automatically in the root compartment.
You must belong to the tenancy's Administrators group or have been granted the REPOSITORY_MANAGE permission on the tenancy to automatically create the private repository in the tenancy's root compartment. See [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)


  *     1. On the **Container Registry** list page, select **Create repository**. If you need help finding the list page, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
    2. Enter the following information:
       * **Create in compartment** : The compartment in which to create the repository. You can select any compartment that you have permission to work in.
       * **Access** : Whether the repository is a public repository or a private repository. You can only make the repository public if you belong to the tenancy's Administrators group or have been granted the REPOSITORY_MANAGE permission. Note these points:
         * If you make the repository public, any user with internet access and knowledge of the appropriate URL can pull images from the repository.
         * If you make the repository private, you (along with users belonging to the tenancy's Administrators group) can perform any operation on the repository.
       * **Repository name** : A name of your choice for the repository. The name you enter must be unique across all compartments in the tenancy. Avoid entering confidential information.
       * **Tags** : Optionally, one or more free-form tags or defined tags to apply to the repository. To apply a defined tag, you must have permissions to use the tag namespace. If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator. For more information, see [Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm#registrytaggingimageswithfreeformdefinedtags "Find out how to add free-form tags and defined tags to repositories, images, and image signatures with Container Registry.").
    3. Select **Create**.
    4. (Optional) To automatically create new private repositories in the tenancy's root compartment when `docker push` commands don't include the name of an existing repository, follow these steps:
      1. Select **Settings**.
      2. Select **Create repository on first push in root compartment**.
  * Use the [oci artifacts container repository create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/create.html) command and required parameters to create a repository:
Command
CopyTry It
```
oci artifacts container repository create --display-name  _<repo-name>_ --compartment-id _<compartment_ocid>_ [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository create --display-name project01/acme-web-app --compartment-id ocid1.compartment.oc1..aaaaaaaarvdfa72n...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/CreateContainerRepository) operation to create a repository.


Was this article helpful?
YesNo

