Updated 2024-03-22
# Getting an Object Version's Details for Roving Edge Infrastructure
Describes how to get the details for a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.
Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for getting details.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm)


  *     1. Open the navigation menu and select **Object Storage > Object Storage**. The **Buckets** page appears. All buckets are listed in tabular form.
    2. Click the bucket whose containing the object whose version details you want to get. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. (optional) Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted.
    4. Click the Down arrow at the right side of the object's entry to display the versions.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) of the version whose details you want to get and click **View Object Details**.
The **Object Version Details** dialog box appears. It contains information on the object version including basic information on the version, response headers, and object contents.
  * Run the `oci os object head` command to get details of an object's version from a bucket using the CLI as described in [Getting an Object's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#HeadObject "Describes how to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices."). Include the `--version-id` parameter in the command to specify the version being deleted. For example:
Command
CopyTry It
```
oci os object head ... --version-id version-id ...
```

  * Run the `HeadObject` operation to get details of an object's version in the Roving Edge Infrastructure device's object storage bucket as described in [Getting an Object's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#HeadObject "Describes how to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices."). Include the `versionId` attribute to specify the object version being delete.


Was this article helpful?
YesNo

