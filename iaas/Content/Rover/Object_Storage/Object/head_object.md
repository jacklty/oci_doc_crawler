Updated 2024-10-09
# Getting an Object's Details for Roving Edge Infrastructure
Describes how to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket whose details you want to get. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the object whose details you want to get and click **View Object Details**. The object's **Details** page appears. If object has versioning applied to it, the command is renamed View Object Versioning Details. The ObjecAll versions of the object are
  * Use the [oci os object head](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/head.html) command and required parameters to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os object head --bucket-name bucket_name --name name [OPTIONS]
```

For example:
```
oci os object head --bucket-name my_bucket --name file1.txt
{
 "content-length": "2211",
 "content-md5": "bj/FoJzx9JEpRv7l+CUamQ==",
 "content-type": "application/octet-stream",
 "date": "Fri, 02 Jun 2023 12:37:09 GMT",
 "etag": "6e3fc5a09cf1f4912946fee5f8251a99",
 "last-modified": "Fri Jun 02 12:36:39 GMT 2023",
 "opc-client-request-id": "exampleuniqueID",
 "opc-request-id": "exampleuniqueID"
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject) operation to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

