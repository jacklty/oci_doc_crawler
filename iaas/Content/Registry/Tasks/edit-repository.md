Updated 2025-02-05
# Editing a Repository
_Find out how to edit a repository in Container Registry._
Having created a repository in Container Registry, you can edit its properties. For example, you might want to change access to a repository from private access to public access.
Your permissions control the repositories in Container Registry that you can edit (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can edit repositories you've created, and repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can edit any repository in the tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm)


  *     1. On the **Container Registry** list page, select the repository that you want to work with from the **Repositories and images** list. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry.").
The repository's details section opens.
    2. Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").
For example, you can make the following edits:
       * Select **Change to Public** or **Change to Private** to change access to the repository.
       * Select **Add scanner** or **Remove scanner** to enable image scanning by adding an image scanner to the repository, or to disable image scanning (see [Scanning Images for Vulnerabilities](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm#Retaining_and_Deleting_Images_Using_Retention_Policies "Find out how to scan images in a repository for security vulnerabilities with Container Registry.")).
       * Select **Move compartment** to move the repository from one compartment to another (see [Moving a Repository Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm#top "Find out how to move a repository in Container Registry from one compartment to another.")).
       * On the **Tags** tab, select **Add tags** to apply additional free-form tags and defined tags to the repository, or select the **Edit** button beside an existing tag to modify or remove that tag. To apply a defined tag, you must have permissions to use the tag namespace. For more information, see [Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm#registrytaggingimageswithfreeformdefinedtags "Find out how to add free-form tags and defined tags to repositories, images, and image signatures with Container Registry.").
  * Use the [oci artifacts container repository update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/update.html) command and required parameters to edit repository properties:
Command
CopyTry It
```
oci artifacts container repository update --repository-id <repository-ocid> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci artifacts container repository update --repository-id ocid1.containerrepo.oc1.us-phoenix-1.0.ansh81vru1zp.aaaaaaaaswec83o... --is-public yes
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [UpdateContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/UpdateContainerRepository) operation to edit a repository.


Was this article helpful?
YesNo

