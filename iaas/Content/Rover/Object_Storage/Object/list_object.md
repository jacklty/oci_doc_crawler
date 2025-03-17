Updated 2024-10-09
# Listing Objects for Roving Edge Infrastructure
Describes how to list the objects contained within an Object Storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket whose details you want to get. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted. If an object listed has versioning applied to it, you can click the Down arrow at the right side of the object's entry to display the versions.
  * Use the [oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html) command and required parameters how to list the objects contained within an Object Storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os object list --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os object list --bucket-name os_test
{
 "data": [
  {
   "archival-state": null,
   "etag": "6e3fc5a09cf1f4912946fee5f8251a99",
   "md5": "bj/FoJzx9JEpRv7l+CUamQ==",
   "name": "file1.txt",
   "size": 2211,
   "storage-tier": null,
   "time-created": "2023-06-02T12:38:25.243000+00:00",
   "time-modified": "2023-06-02T12:38:25.243000+00:00"
  },
  {
   "archival-state": null,
   "etag": "6e3fc5a09cf1f4912946fee5f8251a99",
   "md5": "bj/FoJzx9JEpRv7l+CUamQ==",
   "name": "file_with_new_name.txt",
   "size": 2211,
   "storage-tier": null,
   "time-created": "2023-06-02T12:36:39.721000+00:00",
   "time-modified": "2023-06-02T12:36:39.721000+00:00"
  }
 ],
 "prefixes": []
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects) operation to list the objects contained within an Object Storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

