Updated 2024-01-18
# Deleting the Previous Version of an Object
On Compute Cloud@Customer, when versioning is enabled, deleting an object without targeting a specific version creates a delete marker and a previous version of the object that object can be recovered. However, deleting a previous version of an object is a permanent deletion.
No object is physically deleted from a bucket that has versioning enabled until you take explicit action to do so.
When you delete an object without targeting a specific version, the latest object version becomes a previous object version and a special delete marker is created that marks the deletion point. A delete marker contains only minimal metadata. If you delete a folder, a delete marker is created for each object in the folder. You can simply delete the delete marker to make that deleted version become the latest object version.
When you upload an object with the same name as the delete marker, the uploaded object becomes the latest version of the object. The delete marker remains. There can be multiple delete markers for an object and you can recover any of the previous object versions.
Object version deletion is different. When you delete an object version, the version is permanently deleted. Permanent deletion also happens if you explicitly delete the latest version by version ID. All delete operations that target a specific object version ID permanently deletes the data.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-the-previous-version-of-an-object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-the-previous-version-of-an-object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-the-previous-version-of-an-object.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html) command and required parameters to delete the previous version of an object.
If an object has a `version-id` of `null`, there is only one version of the object. To delete this object, omit the `--version-id` argument.
Copy
```
oci os object delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --version-id <bucket_version_id> --object-name <object_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to delete the previous version of an object.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

