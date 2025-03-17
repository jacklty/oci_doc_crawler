Updated 2024-12-16
# Cloning a Block Volume
On Compute Cloud@Customer, you can create a clone from a volume using the Block Volume service. Cloning enables you to make a copy of an existing block volume without needing to go through the backup and restore process.
A cloned volume is a point-in-time direct disk-to-disk deep copy of the source volume. All the data that's in the source volume is copied to the clone volume. Any subsequent changes to the data on the source volume aren't copied to the clone. 
By default, the clone is the same size as the source volume unless you specify a larger volume size when you create the clone.
The volume data is being copied in the background, and can take up to thirty minutes depending on the size of the volume. You can attach and use the cloned volume as a regular volume when the state changes to Available.
For more information about cloning volumes, see [Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__volume-backups-clones).
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click ****Block Storage**** , then click **Block Volumes**.
    2. At the top of the page, select the compartment that contains the block volume you want to clone.
    3. For the volume you want to clone, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Create Clone**.
    4. In the dialog box, enter the following information:
       * **Name:** A name or description for the volume. Avoid entering confidential information.
       * **Compartment:** Select the compartment in which to clone the block volume.
       * **Size (in GBs):** You can keep the size the same, or increase the size in 1 GB increments up to 32768 (32 TB). You can't decrease the size.
       * **High-Performance Volume:**(Optional) By default, the clone has the same performance setting as the source volume. Use this button to change the performance setting for this clone.
       * **Backup Policy:**(Optional) Select a backup policy from the drop-down list. You might need to change the compartment.
Oracle defined policies are listed, and any user defined policies. For information about Oracle defined policies (`bronze`, `silver`, and `gold`) see [Oracle Provided Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies__oracle-backup-policies).
Backup policies can be assigned or changed after the volume is cloned, or you can back up this volume manually. A volume can only have only one volume backup policy assigned at a time. For information about creating, editing, and assigning backup policies, see [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy."). You can also back up this volume manually as described in [Creating a Manual Boot or Block Volume Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm#creating-a-manual-volume-backup "On Compute Cloud@Customer, you can create a block or boot volume backup manually using the Compute Cloud@Customer Console, CLI, and API.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Clone**.
  * Use the [oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html) command and required parameters to clone a volume.
Command
CopyTry It
```
oci bv volume create --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> --source-volume-id <source_volume_OCID> --display-name <display_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation to clone a volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

