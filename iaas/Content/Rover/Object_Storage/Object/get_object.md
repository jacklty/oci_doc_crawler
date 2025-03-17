Updated 2024-10-09
# Downloading an Object
Learn how to download an Object Storage object from a Roving Edge Infrastructure device to your computer.
To download objects in bulk using the command line interface (CLI), see [Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top "Describes how to upload, download, and delete objects in bulk on your Roving Edge Infrastructure devices.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket whose details you want to get. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the object whose details you want to get and click **View Object Details**. The **Object Details** dialog box appears.
    4. Click **Download**.
Alternately, you can select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the object in the Objects page and click **Download**.
The object is downloaded to your local computer in the default download location.
  * Use the [oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html) command and required parameters to download an object contained to a bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os object get --bucket-name bucket-name --file file --name name [OPTIONS]
```

For example:
```
oci os object get --bucket-name my)bucket --name file1.txt --file file_downloaded.txt
Downloading object [####################################] 100% 
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) operation to download an Object Storage object contained to a bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

