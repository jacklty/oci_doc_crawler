Updated 2024-01-18
# Recovering a Deleted Object Version
On Compute Cloud@Customer, recovering a deleted object version is as simple as deleting the delete marker that was created when you deleted the latest version of an object. The previous version of the object listed just below the delete marker is recovered and becomes the latest version of the object.
To perform this task, you need to know which object is marked for deletion. To obtain that information, list the objects in the bucket. See [Viewing Object Versions and Details](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-object-versions-and-details.htm#viewing-object-versions-and-details "On Compute Cloud@Customer, you can list object versions and details using the CLI and API."). In the output, locate the object version that has `"is-delete-marker": true`.
Use the version-id of that object with the delete command to delete the delete marker.
**Note**
If an object has a `version-id` of `null`, there is only one version of the object. To delete this object marker, omit the `--version-id` argument.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/recovering-a-deleted-object-version.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/recovering-a-deleted-object-version.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/recovering-a-deleted-object-version.htm)


  * This task isn't available in the Console.
  * Use the [oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html) command and required parameters to remove the delete marker from an object.
Syntax:
Copy
```
oci os object delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --object-name <object_name> --version-id <bucket_version_id> [OPTIONS]
```

Example:
```
oci os object delete
--namespace-name examplenamespace \ 
--bucket-name MyBucket
--object-name application.log
--version-id 6ce3eb93-8850-4732-8949-uniqueID
Are you sure you want to delete this resource? [y/N]: y
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to remove the delete marker from an object.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

