Updated 2024-05-22
# Updating the Bucket for a Stack
Update the Object Storage bucket used by a stack in Resource Manager. The updated bucket is used when you run jobs on the stack.
Limit the bucket to files that are intended for use with Terraform.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-bucket.htm)


  * This task can't be performed using the Console.
  * Use the `oci resource-manager stack update-from-object-storage[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update-from-object-storage.html)` command and required parameters to update a stack's bucket.
Copy
```
oci resource-manager stack update-from-object-storage --stack-id <stack_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the bucket used by a stack.
For an example of the `configSource` part of the request, see [UpdateObjectStorageConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateObjectStorageConfigSourceDetails).


Was this article helpful?
YesNo

