Updated 2024-01-18
# Viewing Objects in a Bucket
On Compute Cloud@Customer, you can view objects in a bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-objects-in-a-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-objects-in-a-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-objects-in-a-bucket.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Object Storage** , then click **Object Storage**.
    2. At the top of the page, select the compartment that contains the bucket that contains your object.
A list of buckets is displayed.
    3. Click the bucket name that contains your object. 
    4. Under **Resources** , click **Objects**.
The objects are displayed.
  * Use the [oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html) command and required parameters to list objects in a bucket.
Copy
```
oci os object list --namespace-name <object_storage_namespace> --bucket-name <bucket_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects) operation to list objects in a bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

