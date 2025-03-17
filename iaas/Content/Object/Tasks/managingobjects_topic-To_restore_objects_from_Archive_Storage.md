Updated 2025-01-22
# Restoring an Object Storage Object from Archive Storage
Restore an object from Archive Storage to Object Storage.
Depending on the size of the object, it can take at most an hour to restore an object from Archive Storage. You can't download an item object until the item is fully restored.
To restore objects from Archive Storage, you need OBJECT_RESTORE permissions.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_restore_objects_from_Archive_Storage.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_restore_objects_from_Archive_Storage.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_restore_objects_from_Archive_Storage.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Restore**.
To restore several objects, select the check boxes next to the object names and select **Restore** from the **More Actions** menu.
    4. (Optional) Specify the **Time Available for Download in Hours**.
By default, you have 24 hours to download an object after restoration. However, you can also specify a download time of from 1 to 240 hours. You can find out how much download time is remaining by looking at **Available for Download** in object **Details** or by looking at the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the **Download**. Refresh the browser to obtain up-to-date remaining download time information.
After the allotted download time expires, the object returns to Archive Storage.
    5. Select **Restore Objects**.
Error messages are generated if there's a problem with restoring the selected objects. You can optionally select **Retry failed restore option**.
    6. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the object you want to check the restoration or download status of, then select **Details**.
    7. Check the **Status**.
       * **Archived**
       * **Restoring**
       * **Restored**
  * Use the [oci os object restore-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/restore-status.html) command and required parameters to get that status of an object being restored from Archive Storage to Object Storage in a bucket:
Command
CopyTry It
```
oci os object restore-status --bucket-name archive_bucket_name --name archived_object_name [OPTIONS]
```

By default, you have 24 hours to download an object after restoration. However, you can include the optional `hours` parameter with an integer value of download time of from 1 to 240 hours. For example:
Command
CopyTry It
```
oci os object restore --bucket-name MyArchiveBucket --name MyArchivedObject --hours 12
```

You need `OBJECT_RESTORE` permissions to restore Archive Storage objects.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RestoreObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/RestoreObjects) operation to restore an object from Archive Storage to Object Storage.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API: 
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings.


Was this article helpful?
YesNo

