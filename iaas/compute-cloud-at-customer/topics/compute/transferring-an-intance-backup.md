Updated 2024-10-07
# Transferring an Instance Backup
On Compute Cloud@Customer, you can transfer instance backups to and from another system in your data center.
## Transferring an Instance Backup to Another System 🔗 
You can use this procedure to transfer the instance backup to another system in your data center for safekeeping.
Instance backups are large files. Ensure that you have enough space on your system to store the backup. You can use the `oci os object list` command to display the size of the instance backup. See [Viewing Objects in a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-objects-in-a-bucket.htm#viewing-objects-in-a-bucket "On Compute Cloud@Customer, you can view objects in a bucket.").
**Using the CLI**
  1. Gather the information that you need to run the command.
     * Namespace name (see [Obtaining the Object Storage Namespace](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/obtaining-the-object-storage-namespace.htm#obtaining-the-object-storage-namespace "On Compute Cloud@Customer, an Object Storage namespace serves as the top-level container for all buckets and objects. Each tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments. The namespace name is a required argument for many Object Storage CLI commands."))
     * Bucket name (`oci os bucket list`), see [Listing Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm#listing-buckets "On Oracle Compute Cloud@Customer, you can list buckets.")
     * Object name (`oci os object list`), see [Viewing Objects in a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-objects-in-a-bucket.htm#viewing-objects-in-a-bucket "On Compute Cloud@Customer, you can view objects in a bucket.")
  2. Run the `object get` command.
Syntax (entered on a single line):
```
oci os object get 
--namespace-name <object_storage_namespace>
--bucket-name <bucket_name> 
--name <object_name> 
--file <file_location>
```

<file_location> is the destination path for the file being downloaded, such as `C:\workspace\backups\ocid1.instance.uniqueID` or `/home/downloads/backups/ocid1.instance.uniqueID`. 
Example:
```
oci os object get \
--namespace-name mytenant \
--bucket-name my-backup-bucket \
--name ocid1.instance.........uniqueID \
--file /home/downloads/backups/ocid1.instance.........uniqueID
Downloading object [########################------------]  68% 00:00:05
```



For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
## Transferring an Instance Backup from Another System to Compute Cloud@Customer 🔗 
**Using the CLI**
  1. Gather the information that you need to run the command.
     * Namespace name. See [Obtaining the Object Storage Namespace](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/obtaining-the-object-storage-namespace.htm#obtaining-the-object-storage-namespace "On Compute Cloud@Customer, an Object Storage namespace serves as the top-level container for all buckets and objects. Each tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments. The namespace name is a required argument for many Object Storage CLI commands.").
     * Bucket name (`oci os bucket list`). See [Listing Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm#listing-buckets "On Oracle Compute Cloud@Customer, you can list buckets.").
  2. Upload the instance backup to an Object Storage bucket in the target Compute Cloud@Customer.
Use the `oci os object put` command.
Syntax (entered on a single line):
```
oci os object put \
--namespace-name <namespace_name> \
--bucket-name <bucket_name> \
--file <instance_backup_pathname>
```

The value of <instance_backup_pathname> is the path name of the object being uploaded, such as `C:\workspace\backups\ocid1.instance.uniqueID` or `/home/downloads/backups/ocid1.instance.uniqueID`.
Example:
```
oci os object put \
--namespace-name mytenant \
--bucket-name target-bucket \
--file ./ocid1.instance.….….….uniqueID
Upload ID: f000bf64-9a96-4008-b1cc-f6b2595b04b1
Split file into 35 parts for upload.
Uploading object [####################################] 100%
{
 "etag": "ef7bdd67a72536e29da97f3414f4118e",
 "last-modified": "2022-07-06T17:50:00",
 "opc-multipart-md5": "htOEPyjWDFA4Bs2urJJPRQ==-35"

```



For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Was this article helpful?
YesNo

