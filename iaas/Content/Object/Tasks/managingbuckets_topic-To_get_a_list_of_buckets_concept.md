Updated 2025-01-22
# Listing Object Storage Buckets
View a list of the Object Storage buckets in a compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm)


  *     1. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Buckets**.
The **Buckets** list page opens. All existing Object Storage bucket resources in the selected compartment are displayed in a list table.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
  * Use the [oci os bucket list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/list.html) command and required parameters to list the buckets in a compartment:
```
oci os bucket list --compartment-id compartment_ocid [OPTIONS]
```

For example:
```
oci os bucket list --compartment-id ocid.compartment.oc1..exampleuniqueID --namespace MyNamespace					
{
 "data": [
  {
   "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
   "created-by": "ocid1.user.oc1..exampleuniqueID",
   "defined-tags": null,
   "etag": "c8889cd1-8414-41fb-84b7-3738c39e62c5",
   "freeform-tags": null,
   "name": "MyStandardBucket",
   "namespace": "MyNamespace",
   "time-created": "2020-05-22T19:22:25.032000+00:00"
  },
  {
   "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
   "created-by": "ocid1.user.oc1..exampleuniqueID",
   "defined-tags": null,
   "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e",
   "freeform-tags": null,
   "name": "MyArchiveBucket",
   "namespace": "MyNamespace",
   "time-created": "2020-06-22T13:04:05.879000+00:00"
  }
 ]
}				
```

By default, getting a list of buckets returns up to the first 1,000 buckets in the compartment.
#### Using Field Tags 🔗 
By default when listing buckets, `null` is returned as the value for both free-form and defined tags. To include [resource tag](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) data, include the `--fields tags` parameter: 
Command
CopyTry It
```
oci os bucket list --compartment-id compartment_ocid --fields tags [OPTIONS]
```

For example:
```
oci os bucket list --compartment-id ocid.compartment.oc1..exampleuniqueID --fields tags
{
 "data": [
	{
	 "compartment-id": "ocid1.compartment.oc1..exampleuniqueID",
	 "created-by": "ocid1.user.oc1..exampleuniqueID",
	 "defined-tags": {
		"example_tag_namespace_Financials": {
		 "production": "Unit 5"
		},
		"example_tag_namespace_Operations": {
		 "costcenter": "85"
		}		
	 },
	 "etag": "48af18cf-1edd-4b05-9f36-a629d5032260",
	 "freeform-tags": {
	  "Project": "prototype 3"
	 },
	 "name": "MyStandardBucket",
	 "namespace": "MyNamespace",
	 "time-created": "2020-05-27T18:52:16.951000+00:00"
	}
 ]
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListBuckets](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ListBuckets) operation to list the buckets in a compartment.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

