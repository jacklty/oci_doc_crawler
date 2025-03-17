Updated 2024-01-18
# Getting Bucket Details
On Compute Cloud@Customer, you can view bucket details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/getting-bucket-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/getting-bucket-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/getting-bucket-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Object Storage** , then click **Object Storage**.
    2. At the top of the page, select the compartment that contains the bucket.
    3. Click the bucket name to display the details.
    4. Click **View** or **Copy**.
  * Use the [oci os bucket get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/get.html) command and required parameters to get the current representation of the given bucket in the given Object Storage namespace.
Copy
```
oci os bucket get --namespace-name <object_storage_namespace> --bucket-name <bucket_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket) operation to get the current representation of the given bucket in the given Object Storage namespace.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

