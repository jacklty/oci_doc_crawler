Updated 2024-12-16
# Creating a File System
On Compute Cloud@Customer, you can create a shared file system using the File Storage service.
(Optional) To create a file system with specific values for the following attributes, first configure the attributes as described in [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes."). Then use the following information when you create the file system.
  * **Quota**
The default value of `quota` is 0, which means no quota is set. A quota that you set includes the data in the file system and all snapshots created under the file system. You can specify a quota value in gigabytes from 0 to 8000000 (8 petabytes). Any fractional portion of the gigabyte value is rounded to the next larger megabyte. The file system quota can be changed with the file system `update` command.
To apply a quota, during file system creation, assign this defined tag:
    * **Tag namespace:** `OraclePCA`
    * **Tag name:** `quota`
    * **Value:** <quota value in gigabytes>
  * **Database record size**
The default database record size is `131072` bytes. You can specify one of the following values (in bytes): `512`, `1024`, `2048`, `4096`, `8192`, `16384`, `32768`, `65536`, `131072`, `262144`, `524288`, `1048576`. The record size can be set only when the file system is created. You can't set or change this property value later.
  * To use a nondefault value, during file system creation, assign this defined tag:
    * **Tag namespace:** `OraclePCA`
    * **Tag name:** `databaseRecordSize`
    * **Value** (select one): `512`, `1024`, `2048`, `4096`, `8192`, `16384`, `32768`, `65536`, `131072`, `262144`, `524288`, `1048576`
  * **Backing store pool**
By default, the backing store of a file system is the default pool of the attached ZFS Storage Appliance, specified as **PCA_POOL**. You can specify `PCA_POOL_HIGH` to indicate that you want to use a high performance pool for the backing store. Before you specify `PCA_POOL_HIGH`, verify that a high performance pool is available. This property can be set only when the file system is created. You can't set or change this property value later.
To use a nondefault value, during file system creation, assign this defined tag:
    * **Tag namespace:** `OraclePCA`
    * **Tag name:** `databaseRecordSize`
    * **Value** (select one): `PCA_POOL` (default) or `PCA_POOL_HIGH`


Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. Ensure that the correct compartment is selected in the compartment drop-down menu above the file systems list. The file system and mount target must be in the same compartment and the same backing store pool when you create an export.
    3. Click **Create File System**.
    4. In the **Create File System** dialog box, enter the following information:
       * **Name:** It doesn't have to be unique. An Oracle Cloud Identifier (OCID) uniquely identifies the file system. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment where the file system is created.
       * **Tagging:** (Optional) Add tags to this resource.
You can optionally set the **Tag Namespace** to **None (add a free-form tag)** , then set your own tag key and value. Or you can set free-form tags later.
If the OraclePCA tag namespace and OraclePCA tag key definitions for file systems are configured in your OCI tenancy (see [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes.")), you can specify the **OraclePCA** Tag Namespace, select a key and a value. Your file system is created with the applicable attribute. The OraclePCA tag namespace can't be added later. 
    5. Click **Create File System**. 
The file system is created. 
Next, create an export for the file system. See [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").
  * Use the [oci fs file-system create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create.html) command and required parameters to create a new file system in the specified compartment and availability domain.
Copy
```
oci fs file-system create --availability-domain <availability_domain_name> --compartment-id <compartment_id> --display-name <fs_display_name>  [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Gather the information that you need to run the command:
       * Availability Domain Name (`oci iam availability-domain                     list`)
       * Compartment OCID (`oci iam compartment list`)
       * File System Name: The display name you want assigned to this file system
    2. To use nondefault values for the quota, database record size, or backend store pool, specify the appropriate tags to set the values for these attributes. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
See the following step for an example of setting these values.
    3. Run the create file system command.
Example:
```
oci fs file-system create --availability-domain AD-1 --compartment-id ocid1.compartment.unique_ID --display-name MyFileSystem
{
 "data": {
  "availability-domain": "AD-1",
  "compartment-id": "ocid1.compartment._unique_ID_",
  "defined-tags": {
   "Oracle-Tags": {
    "CreatedBy": "pca_user",
    "CreatedOn": "2024-07-05T13:15:11.19Z"
   }
  },
  "display-name": "MyFileSystem",
  "freeform-tags": {},
  "id": "ocid1.filesystem._unique_ID_",
  "is-clone-parent": false,
  "is-hydrated": true,
  "is-targetable": null,
  "kms-key-id": "",
  "lifecycle-details": "",
  "lifecycle-state": "CREATING",
  "metered-bytes": 0,
  "source-details": {
   "parent-file-system-id": "",
   "source-snapshot-id": ""
  },
  "time-created": "2024-07-05T13:15:11.234434+00:00"
 },
 "etag": "58dec47e-4732-4730-9e18-6b5db1ac30d6"
}
```

Example using defined tags to set additional properties:
To set a quota for the file system, change the default database record size, or specify a high performance pool for the file system backing store, use `OraclePCA` defined tags as shown in the following example.
```
oci fs file-system create --availability-domain AD-1 --compartment-id ocid1.compartment.unique_ID --display-name myfilesystem --defined-tags '{"OraclePCA":{"quota":100000,"databaseRecordSize":8192,"poolName":"PCA_POOL_HIGH"}}'
```

Alternatively, you can specify these properties in a JSON file.
```
{
 "OraclePCA": {
  "quota": 100000,
  "databaseRecordSize": 8192,
  "poolName": "PCA_POOL_HIGH"
 }
}
```

Then specify the file as the argument of the `--defined-tags` option.
```
--defined-tags file://./fs_options.json
```

    4. Next, create an export for the file system. See [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").
  * Use the [CreateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateFileSystem) operation to create a new file system in the specified compartment and availability domain.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

