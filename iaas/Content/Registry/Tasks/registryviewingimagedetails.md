Updated 2025-02-05
# Getting an Image's Details
_Find out how to get details of an image in a repository in Container Registry._
To make sure you pull the correct image or to identify images that you no longer need, you can get detailed information about the images in Container Registry. 
Your permissions control which images you can get information about (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can get information about images in repositories that you've created, and in repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can get information about images in any repository in the tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Select the repository in the **Repositories and images** list a second time.
The images in the repository, including their version identifiers, are listed under the repository in the **Repositories and images** list.
    3. Select the image you want.
The image's details section opens.
    4. Perform the following tasks to see the image's details:
       * Select the **Image information** tab to see the size of the image, when it was pushed and by which user, and the number of times the image has been pulled.
       * Select the **Layers** tab to see the SHA message digest of each layer in the selected image.
       * Select the **Versions** tab to see the full path for the image with the version identifier you select. Note that if you select a different version identifier, the summary details change accordingly.
       * Select the **Tags** tab to see the free-form tags and defined tags applied to the image. For more information, see [Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm#registrytaggingimageswithfreeformdefinedtags "Find out how to add free-form tags and defined tags to repositories, images, and image signatures with Container Registry.").
       * Select the **Signatures** tab to see details of signatures created if the image was signed. For more information, see [Signing Images for Security](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm#Deleting_a_Repository "Find out how to sign images stored in Container Registry.").
       * Select the **Scan Results** tab to see a summary of each scan of the image for the last 13 months. For more information, see [Scanning Images for Vulnerabilities](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm#Retaining_and_Deleting_Images_Using_Retention_Policies "Find out how to scan images in a repository for security vulnerabilities with Container Registry.").
    5. (Optional) To pull an image, select **Copy pull command**. The command you copy includes the fully qualified path to the image's location in Container Registry, in the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`.
For example, `docker pull ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test`. See [Pulling Images Using the Docker CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm#Pulling_Images_Using_the_Docker_CLI "Find out how to pull images from Container Registry using the Docker CLI.").
  * Use the [oci artifacts container image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/get.html) command and required parameters to get details of an image:
Command
CopyTry It
```
oci artifacts container image get --image-id  _<image-ocid>_ [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container image get --image-id ocid1.containerimage.oc1.phx.0.ansh81vru1zp.aaaaaaaalqzjyks...
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetContainerImage](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/GetContainerImage) operation to get image details.


Was this article helpful?
YesNo

