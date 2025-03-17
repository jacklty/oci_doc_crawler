Updated 2024-10-09
# Deleting an Object from Roving Edge Infrastructure
Describes how to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices.
To delete objects in bulk using the command line interface (CLI), see [Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top "Describes how to upload, download, and delete objects in bulk on your Roving Edge Infrastructure devices.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket containing the object you want to delete. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. Check each object that you want to delete.
    4. Click **Delete Objects**. To delete a single object, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for that object in the Buckets page and click **Delete**.
    5. Confirm the deletion when prompted.
  * Use the following command and required parameters to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os object delete --bucket-name bucket-name --name name [OPTIONS]
```

For example:```
oci os object delete --bucket-name my_bucket --name file_with_new_name.txt
Are you sure you want to delete this resource? [y/N]: y 
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

