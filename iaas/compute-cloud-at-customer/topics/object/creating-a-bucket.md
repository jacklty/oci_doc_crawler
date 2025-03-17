Updated 2024-08-06
# Creating a Bucket
On Compute Cloud@Customer, you can create Object Storage buckets.
When you create a bucket, the bucket doesn't provide public access. To make the bucket publicly available, see [Using Preauthenticated Requests](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/using-pre-authenticaed-requests.htm#using-pre-authenticaed-requests "On Compute Cloud@Customer, preauthenticated requests provide a way to let users access a bucket or an object without having their own credentials, as long as the request creator has permissions to access those objects.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Object Storage** , then click **Object Storage**.
    2. Click **Create Bucket**.
    3. Enter the following details:
       * **Name:** Enter a name for the bucket. 
Specify a name that's unique within your tenancy Object Storage namespace.
       * **Create in Compartment:** Select the compartment in which to create this bucket.
       * **Enable Object Versioning:** Optionally, you can enable object versioning.
For more information, see [Managing Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Bucket**. 
The bucket is created immediately and you can start uploading objects. See [Uploading an Object](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/uploading-an-object.htm#uploading-an-object "On Compute Cloud@Customer, you can upload an object using the CLI and API.").
  * Use the [oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html) command and required parameters to create a bucket in the particular namespace with a bucket name and optional user-defined metadata. 
Copy
```
oci os bucket create --namespace-name <object_storage_namespace> --compartment-id <compartment_OCID> --name <bucket_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
For information about how to configure your CLI environment to reach Compute Cloud@Customer infrastructure resources, see [Using the CLI to Manage Compute Cloud@Customer Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/accessing-cli.htm#accessing-cli "You can use the OCI CLI to manage resources \(compute, storage, and networking\) on Compute Cloud@Customer the same way you use the OCI CLI to manage your tenancy resources.").
  * Use the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation to create a bucket in the given namespace with a bucket name and optional user-defined metadata.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

