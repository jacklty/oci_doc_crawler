Updated 2024-10-09
# Listing an Object's Versions for Roving Edge Infrastructure
Describes how to list the versions of an object in an object storage bucket on your Roving Edge Infrastructure device.
Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for listing.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list-object-versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list-object-versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list-object-versions.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket whose details you want to get. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. (optional) Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted.
    4. Click the Down arrow at the right side of the object's entry to display the versions.
Each version of the object is displayed as a separate entry that you can perform various tasks on using the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)).
  * Use the [oci os object list-object-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list-object-versions.html) command and required parameters to list the versions of an object in the Roving Edge Infrastructure device's object storage bucket:
```
oci os object list-object-versions --bucket-name bucket_name [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListObjectVersions](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjectVersions) operation to list the versions of an object in the Roving Edge Infrastructure device's object storage bucket.


Was this article helpful?
YesNo

