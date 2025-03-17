Updated 2025-01-22
# Managing Folders in an Object Storage Bucket
Create and delete folders and subfolders in an Object Storage bucket to organize objects.
Use the Console to create folders and subfolders in which you can upload and store your objects according to your organizational needs.
## Using the Console 🔗 
  1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
  2. On the details page, select **Objects**.
  3. Perform one of the following tasks:
     * To add a new folder: Select **Create New Folder** from the **More Actions** menu.
     * To add a folder or subfolder to an existing folder: Select the existing folder to open it. Select **Create New Folder** from the **More Actions** menu.
  4. Enter a name for the folder or subfolder. Avoid entering confidential information.
  5. Select **Create**.


The folder or subfolder is created and displayed in the **Objects** table, either at the root level of the **Objects** list or under an existing folder depending on where you created it.
### Deleting a Folder 🔗 
When you delete a folder in the **Objects** list, all the objects contained in the folder are deleted. If object versioning is enabled on the bucket, you can restore those objects. See [Restoring a Deleted Object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm#top "Recover a deleted object to an Object Storage bucket.") for more information.
  1. Find the root or parent folder of the folder you want to delete in the **Objects** list.
  2. From the **Actions** menu for folder, select **Delete Folder**.
  3. When prompted, confirm the deletion.


Was this article helpful?
YesNo

