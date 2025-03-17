Updated 2024-04-17
# Updating Instance Metadata
You can add and update custom metadata for a compute instance using the [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm) or [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).
When you create an instance using the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation, you can specify custom metadata for the instance in the [LaunchInstanceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails) datatype's `metadata` or `extendedMetadata` attributes.
To update an instance's metadata, use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation, specifying the custom metadata in the [UpdateInstanceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateInstanceDetails) datatype's `metadata` or `extendedMetadata` attributes.
The `metadata` attribute supports key/value string pairs. The `extendedMetadata` attribute supports nested JSON objects. The combined size of these two attributes can be a maximum of 32,000 bytes.
It might take up to a minute for the changes to be reflected in the instance metadata service.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Using the API 🔗 
When you use the `UpdateInstance` operation, the instance's metadata will be the combination of the values specified in the [UpdateInstanceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateInstanceDetails) datatype's `metadata` or `extendedMetadata` attributes. Any set of key/value pairs specified for these attributes in the `UpdateInstance       `operation will replace the existing values for these attributes, so you need to include all the metadata values for the instance in each call, not just the ones you want to add. If you leave the attribute empty when calling `UpdateInstance`, the existing metadata values in that attribute will be used. You cannot specify a value for the same metadata key twice, as this will cause the `UpdateInstance `operation to fail due to there being duplicate keys.
To understand this, consider the example scenario where you created an instance using the `LaunchInstance` operation and specified the following key/value pair for the `metadata `attribute:
```
"myCustomMetadataKey" : "myCustomMetadataValue"
```

If you then call the `UpdateInstance `operation, and add new metadata by specifying additional key/value pairs in the `extendedMetadata` attribute, but you leave the `metadata `attribute empty, do not include the `myCustomMetadataKey `key/value in the `extendedMetadata` attribute, as this will cause the operation to fail since that key already exists. If you do specify values for the metadata attribute, you need to include the `myCustomMetadataKey` key/value to maintain it in the instance's metadata. In this case, you can specify it in either of the attributes.
There are two reserved keys, `user_data` and `ssh_authorized_keys`, that can only be set for an instance at launch time, they cannot be updated later. If you use the metadata attribute to add or update metadata for an instance, you need to ensure that you include the values specified at launch time for both these keys, otherwise the `UpdateInstance `operation will fail. 
## Best Practices for Updating an Instance's Metadata 🔗 
When using the `UpdateInstance` operation, we recommend the following:
  * Use the [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance) operation to retrieve the existing custom metadata for the instance to ensure that you include the values you want to maintain in the appropriate attributes when you call `UpdateInstance`. The metadata values are returned in the `metadata` and `extendedMetadata` attributes for the [Instance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/) . For a code example demonstrating this, see the [UpdateInstanceExample](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/UpdateInstanceExample.java) in the [SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java).
  * Unless you are updating custom metadata that was added using the `metadata` attribute, use the `extendedMetadata` attribute to add custom metadata. Otherwise you need to include the launch time values for the `user_data` and `ssh_authorized_keys` reserved keys. If you use the `metadata` attribute to add values and you leave out the values for these reserved keys or specify different values for them, the `UpdateInstance` call will fail.


Was this article helpful?
YesNo

