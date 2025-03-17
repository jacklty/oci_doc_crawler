Updated 2024-01-18
# Listing Buckets
On Oracle Compute Cloud@Customer, you can list buckets.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Object Storage** , then click **Object Storage**.
A list of the buckets in the compartment you're viewing is displayed.
    2. If you don’t see the bucket you're looking for, ensure that you’re viewing the correct compartment (select the compartment at the top of the page).
The page shows only the resources in that compartment.
  * Use the [oci os bucket list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/list.html) command and required parameters to get a list of all bucket summary items in a compartment. A bucket summary contains only summary fields for the bucket and does not contain fields like the user-defined metadata.
Copy
```
oci os bucket list --namespace-name<object_storage_namespace>--compartment-id<compartment_OCID>[OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListBuckets](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ListBuckets) operation to get a list of all bucket summary items in a compartment. A bucket summary contains only summary fields for the bucket and does not contain fields like the user-defined metadata.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

