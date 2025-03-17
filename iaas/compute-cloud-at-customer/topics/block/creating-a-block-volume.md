Updated 2024-12-16
# Creating a Block Volume
On Compute Cloud@Customer, block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance. 
During the block volume creation, you can optionally use free-form tags to change the following block volume parameter: 

Volume Block size
    The default value is 8192 bytes. To change the value, specify a value in bytes for the `PCA_blocksize` free-form tag. Supported values are a power of 2 between 512 bytes and 1 megabyte, specified as a string and fully expanded. We recommend setting the value to at least 8192 bytes.     The block size can't be changed after the volume has been created.     See [Using Free-Form Tags for Extended Functionality](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/freeform-tags-used-for-extended-functionality.htm#freeform-tags-used-for-extended-functionality "On Compute Cloud@Customer, you can use free-form tags to extend the functionality of some services.").
(Optional) To create a block volume with nondefault values for the following attributes, first configure the required tags as described in [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes."). Then use the following information when you create the block volume.
  * **Synchronous Write Bias**
You can configure the write cache flash devices for a share or LUN ("Logzilla"). The value can be changed later by updating the block volume.
To use a nondefault value, during block volume creation, assign this defined tag:
    * **Tag namespace:** OraclePCA
    * **Tag name:** logBias
    * **Value** (select one): LATENCY (default) or THROUGHPUT
  * **Secondary Cache**
You can configure the use of the read cache flash devices for a share or LUN ("Readzilla"). The value can be changed later by updating the block volume.
To use a nondefault value, during block volume creation, assign this defined tag:
    * **Tag namespace:** OraclePCA
    * **Tag name:** secondaryCache
    * **Value** (select one): ALL (default), METADATA, or NONE


Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    2. Click **Create Block Volume**.
    3. Provide the following volume information:
       * **Name:** Provide a name or description for the volume. Avoid entering confidential information.
       * **Compartment:** Select the compartment in which to create the block volume.
       * **Size (in GBs):** The default size of 1024 GB is shown. To change the size, enter a value from 50 to 32768 (50 GB to 32 TB).
       * **High Performance Volume:** (Optional) By default, the volume uses balanced performance. To create a block volume that uses the high performance feature, click the Enable High Performance button. You can only select high performance volumes if such volumes are available. For more information, see [Block Volume Performance Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__block-volume-performance-options).
This selection can't be changed after the volume is created.
       * **Backup Policy:** (Optional) Select a backup policy from the drop-down list. You might need to change the compartment.
Oracle defined policies are listed, and any user defined policies. For information about Oracle defined policies (`bronze`, `silver`, and `gold`) see [Oracle Provided Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies__oracle-backup-policies).
Backup policies can be assigned or changed after the volume is created. A volume can only have only one volume backup policy assigned at a time. For information about creating, editing, and assigning backup policies, see [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy."). You can also back up this volume manually as described in [Creating a Manual Boot or Block Volume Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm#creating-a-manual-volume-backup "On Compute Cloud@Customer, you can create a block or boot volume backup manually using the Compute Cloud@Customer Console, CLI, and API.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
To use nondefault values for the block size, write bias, or secondary cache, specify the appropriate tags to set the values for these attributes. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
    4. Click **Create Block Volume**.
The volume is ready to attach to an instance after its icon lists the volume in the Available state. See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").
  * Use the [oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html) command and required parameters to create a volume.
Copy
```
oci bv volume create --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
To use nondefault values for the block size, write bias, or secondary cache, specify the appropriate tags to set the values for these attributes. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
**Procedure**
    1. Gather the information that you need to run the command:
       * Availability domain name (`oci iam availability-domain                     list`)
       * Compartment OCID (`oci iam compartment list`)
    2. Run the volume create command.
This procedure doesn't show all available parameters for this command. For information about additional parameters, run the command with the `--help` option.
Example:
This example specifies VPUs, log bias, secondary cache, and volume block size.
**VPUs per Gigabyte Option**
The value of the `--vpus-per-gb` option is the number of volume performance units (VPUs) that will be applied to this volume per GB. The default value for `vpus-per-gb` is 10, for balanced volume performance. For higher performance, you can specify 20 VPUs/GB. You can only select high performance volumes if such volumes are available. For more information, see [Block Volume Performance Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__block-volume-performance-options).
VPUs per GB can't be changed after the volume is created.
You can't auto-tune volumes.
Example:
```
$ oci bv volume create --availability-domain AD-1 --compartment-id compartment_OCID --display-name myblockvolume --size-in-gbs 50 --vpus-per-gb 20 --defined-tags '{"OraclePCA":{"logBias":"THROUGHPUT","secondaryCache":"METADATA"}}' 
--freeform-tags '{"PCA_blocksize": "65536"}'
{
 "data": {
  "auto-tuned-vpus-per-gb": null,
  "autotune-policies": null,
  "availability-domain": "AD-1",
  "block-volume-replicas": null,
  "compartment-id": "ocid1.compartment.**
            _unique_ID_
           **",
  "defined-tags": {
   "OraclePCA": {
    "logBias": "THROUGHPUT",
    "secondaryCache": "METADATA"
   }
  },
  "display-name": "myblockvolume",
  "freeform-tags": {},
     "PCA_blocksize": "65536"
  },
  "id": "ocid1.volume.**
            _unique_ID_
           **",
  "is-auto-tune-enabled": null,
  "is-hydrated": null,
  "kms-key-id": null,
  "lifecycle-state": "PROVISIONING",
  "size-in-gbs": 50,
  "size-in-mbs": 51200,
  "source-details": null,
  "system-tags": null,
  "time-created": "2022-12-08T21:05:36.647925+00:00",
  "volume-group-id": null,
  "vpus-per-gb": 20
 },
 "etag": "08d0abc9-60c6-4fc7-b6fe-85d0af1c0308",
 "opc-work-request-id": "ocid1.workrequest.**
            _unique_ID_
           **"
}
```

A `vpus-per-gb` value of 10 indicates that this is a balanced performance volume. A `vpus-per-gb` value of 20 indicates that this is a high performance volume.
When the volume is in the AVAILABLE state, you can attach the volume to an instance. See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").
  * Use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation to create a block volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

