Updated 2025-02-05
# Retaining and Deleting Images Using Retention Policies
_Find out how to set up and use image retention policies with Container Registry._
You can set up image retention policies to automatically delete images that meet particular selection criteria, namely:
  * Images that haven't been pulled for a certain number of days.
  * Images that haven't been versioned for a certain number of days.
  * Images that haven't been given particular version identifiers specified as exempt from automatic deletion.


An hourly process checks images against the selection criteria, and any that meet the selection criteria are automatically deleted. 
You'll often find image retention policies are a more convenient way to manage the images in a repository than manually deleting individual images (see [Deleting an Image](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm#top "Find out how to delete an image from Container Registry.")).
In each region in a tenancy, there's a global image retention policy. The global image retention policy's default selection criteria retain all images, so that no images are automatically deleted. However, you can change the global image retention policy so that images are deleted if they meet the criteria you specify. A region's global image retention policy applies to all repositories in the region, unless it is explicitly overridden by one or more custom image retention policies. 
You can set up custom image retention policies to override the global image retention policy with different criteria for specific repositories in a region. Having created a custom image retention policy, you apply the custom retention policy to a repository by adding the repository to the policy. The global image retention policy no longer applies to repositories that you add to a custom retention policy.
If you have `manage` permission on the tenancy, you can perform the following tasks:
  * Modify each region's own global image retention policy.
  * Create new custom image retention policies.
  * Modify the criteria of existing custom image retention policies.
  * Delete custom image retention policies.


If you have `manage` permission on a repository, you can:
  * Add the repository to a custom image retention policy.
  * Remove the repository from a custom image retention policy.


Note the following:
  * Only one custom image retention policy at a time can apply to a repository. If a repository has already been added to a custom retention policy and you want to add the repository to a different custom retention policy, you have to remove the repository from the first retention policy before adding it to the second.
  * When you create or update an image retention policy, the hourly process that checks images for deletion will ignore the new or updated policy for several hours. This cooling-off period enables you to refine the policy criteria to select only the images you want to delete, and thus reduces the chance of images being deleted unexpectedly. After this period, the policy is included in the hourly process and images are checked and deleted accordingly.
  * The global image retention policy (and any custom image retention policies you create) are specific to a particular region. To delete images consistently in different regions in your tenancy, set up image retention policies in each region with identical selection criteria.
  * When you delete an image, it can take up to 48 hours for the deletion to take effect and for storage to be released. If you're deleting images to release storage, you can also [contact us](https://support.oracle.com/) to obtain more storage.


## Using the Console to Edit the Global Image Retention Policy 🔗 
Provided you have `manage` permission on the tenancy, you can edit the region's global image retention policy that applies to all repositories in a region (except for repositories that have been explicitly added to a custom image retention policy).
  1. On the **Container Registry** list page, select **Settings**. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry."). 
You see the current selection criteria of the region's global image retention policy, along with any custom image retention policies that override the global image retention policy for specific repositories.
  2. Select **Edit global policy**.
  3. In the **Global image retention policy** panel, specify new criteria for the global retention policy:
     * **Delete any images that haven't been pulled in the specified number of days** : Select this option to delete images that haven't been pulled for the number of days you specify.
     * **Delete any images that haven't been versioned in the specified number of days** : Select this option to delete images that haven't been versioned for the number of days you specify.
     * **Exempt versions** : To prevent images from being deleted based on version identifiers they've been given, specify those version identifiers as exempt in a comma-separated list. An image that has been given one of the exempt version identifiers won't be deleted, even if the image meets the other criteria. You can include the asterisk (*) as a wildcard to represent none, one, or more characters. For example, you might specify `latest,prod-*,*-tail,*.100.*`.
  4. Select **Save changes**.


Going forward, the criteria you entered for the region's global image retention policy will apply to all repositories in the region, except for repositories that have been explicitly added to a custom image retention policy. Images in repositories that haven't been added to a custom image retention policy will be deleted from Container Registry if they meet the criteria you specified in the global image retention policy.
When you create or update an image retention policy, the hourly process that checks images for deletion will ignore the new or updated policy for several hours. This cooling-off period enables you to refine the policy criteria to select only the images you want to delete, and thus reduces the chance of images being deleted unexpectedly. After this period, the policy is included in the hourly process and images are checked and deleted accordingly.
## Using the Console to Create a New Custom Image Retention Policy to Override the Global Policy 🔗 
Provided you have `manage` permission on the tenancy, you can create a new custom image retention policy to override the region's global image retention policy for the repositories you specify. A custom image retention policy is specific to the region in which you create it.
  1. On the **Container Registry** list page, select **Settings**. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry."). 
You see the current selection criteria of the region's global image retention policy, along with any custom image retention policies that override the global image retention policy for specific repositories.
  2. Select **Another override policy**.
  3. In the **Create image retention override policy** dialog, specify criteria for the new retention policy:
     * **Policy name** : A name of your choice for the policy. Avoid entering confidential information.
     * **Delete any images that haven't been pulled in the specified number of days** : Select this option to delete images that haven't been pulled for the number of days you specify.
     * **Delete any images that haven't been versioned in the specified number of days** : Select this option to delete images that haven't been versioned for the number of days you specify.
     * **Exempt versions** : To prevent images from being deleted based on version identifiers they've been given, specify those version identifiers as exempt in a comma-separated list. An image that has been given one of the exempt version identifiers won't be deleted, even if the image meets the other criteria. You can include the asterisk (*) as a wildcard to represent none, one, or more characters. For example, you might specify `latest,prod-*,*-tail,*.100.*`.
  4. Select **Save changes**.


You can now add repositories to the new custom retention policy. 
## Using the Console to Remove a Repository from a Custom Image Retention Policy 🔗 
Provided you have `manage` permission on a repository, you can remove a repository from a custom image retention policy to which it was previously added.
You might want to remove the repository from a custom image retention policy:
  * If you want the region's global image retention policy to apply to the repository.
  * If you want a different custom image retention policy to apply to the repository (only one custom image retention policy at a time can apply to a repository).


  1. On the **Container Registry** list page, select **Settings**. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry."). 
You see the current selection criteria of the region's global image retention policy, along with any custom image retention policies that override the global image retention policy for specific repositories.
  2. Select **Edit override policy** beside the custom image retention policy to which the repository has been added.
  3. Select the delete icon beside the repository name to remove it from the custom image retention policy.
  4. Select **Save changes**.


Going forward, the region's global image retention policy will apply to the repository (unless you add the repository to a different custom image retention policy). The images in the repository will be deleted from Container Registry if they meet the criteria specified in the global image retention policy. 
When you create or update an image retention policy, the hourly process that checks images for deletion will ignore the new or updated policy for several hours. This cooling-off period enables you to refine the policy criteria to select only the images you want to delete, and thus reduces the chance of images being deleted unexpectedly. After this period, the policy is included in the hourly process and images are checked and deleted accordingly.
## Using the Console to Add a Repository to a Custom Image Retention Policy 🔗 
Provided you have `manage` permission on a repository, you can add a repository to an existing custom image retention policy.
Note that if a custom image retention policy already applies to the repository, you'll have to remove the repository from the current policy before adding it to a different policy. Note also that a custom image retention policy is specific to the region in which it was created.
  1. On the **Container Registry** list page, select **Settings**. If you need help finding the list page or the repository, see [Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#list-repository "Find out how to list the repositories in Container Registry."). 
You see the current selection criteria of the region's global image retention policy, along with any custom image retention policies that override the global image retention policy for specific repositories.
  2. Select **Edit override policy** beside the custom image retention policy to which you want to add the repository.
  3. Select **Another repository** and select from the list the repository you want to add to the custom image retention policy.
Note that the repository list includes all repositories in the region, regardless of whether you have permission to add them to a retention policy. You can only add a repository to a retention policy if you have `manage` permission on that repository.
If a repository in the list has a policy name beside it, the repository has already been added to a policy. Before you can add the repository to a different policy, you'll have to remove it from the first policy.
  4. Select **Save changes**.


Going forward, the custom retention policy to which you added the repository will override the region's global image retention policy. The images in the repository will be deleted from Container Registry if they meet the criteria specified in the custom retention policy. 
When you create or update an image retention policy, the hourly process that checks images for deletion will ignore the new or updated policy for several hours. This cooling-off period enables you to refine the policy criteria to select only the images you want to delete, and thus reduces the chance of images being deleted unexpectedly. After this period, the policy is included in the hourly process and images are checked and deleted accordingly.
Was this article helpful?
YesNo

