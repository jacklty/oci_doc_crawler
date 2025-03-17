Updated 2024-03-22
# Downloading an Object Version for Roving Edge Infrastructure
Describes how to download a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.
Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for downloading.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/download-object-versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/download-object-versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/download-object-versions.htm)


  *     1. Open the navigation menu and select **Object Storage > Object Storage**. The **Buckets** page appears. All buckets are listed in tabular form.
    2. Click the bucket that contains the object whose version you want to download. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. (optional) Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted.
    4. Click the Down arrow at the right side of the object's entry to display the versions.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) of the version you want to download and click **Download**.
The **Download Object** dialog box appears displaying the progress of the object being downloaded. You can also cancel the download by clicking **Cancel Download**.
  * Run the `oci os object get` command to download an object from a bucket using the CLI as described in [Downloading an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#top "Learn how to download an Object Storage object from a Roving Edge Infrastructure device to your computer."). Include the `--version-id` parameter in the command to specify the version being downloaded. For example:
Command
CopyTry It
```
oci os object get ... --version-id version-id ...
```

  * Run the `GetObject` operation to delete the version of an object in the Roving Edge Infrastructure device's object storage bucket as described in [Downloading an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#top "Learn how to download an Object Storage object from a Roving Edge Infrastructure device to your computer."). Include the `versionId` attribute to specify the object version being delete.


Was this article helpful?
YesNo

