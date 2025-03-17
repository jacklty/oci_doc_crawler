Updated 2023-08-14
# Enabling Object Versioning for Roving Edge Infrastructure
Describes how to enable versioning of objects when creating an object storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm)


  * Follow the steps for creating a bucket using the Device Console as described in [Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#top "Describes how to create a object storage bucket on your Roving Edge Infrastructure devices."). Select **Enable Object Versioning** to apply versioning to all objects that you upload.
  * Run the `oci os bucket create` command to create a bucket using the CLI as described in [Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#top "Describes how to create a object storage bucket on your Roving Edge Infrastructure devices."). Include the `--versioning enabled` parameter in the command. For example:
Copy
```
oci os bucket create ... --versioning enabled ...
```

  * Run the `CreateBucket` operation to create a bucket using the API as described in [Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#top "Describes how to create a object storage bucket on your Roving Edge Infrastructure devices."). Include the `versioning: enabled` attribute in the operation.


Was this article helpful?
YesNo

