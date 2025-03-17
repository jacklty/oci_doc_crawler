Updated 2024-11-07
# Deleting a Block Volume
On Compute Cloud@Customer, you can delete a volume that is no longer needed.
**Caution**
You can't undo this operation. Any data on a volume is permanently deleted when the volume is deleted. 
**Caution**
All policy-based (scheduled) backups expire. A manual backup expires if a scheduled backup of the same volume is created after the manual backup was created. To keep a volume backup indefinitely, cancel all future scheduled backups and create a manual backup before you delete the source volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
The result of deleting a block volume differs depending on thee following conditions:
  * **The volume has no backups or clones:** The volume is immediately deleted and the volume capacity is returned to the system for reuse. The volume is marked TERMINATED and eventually is no longer listed.
  * **The volume has a backup or a clone:** The volume is marked TERMINATED, but the volume is not deleted and the capacity is not returned to the system until all of the backups and clones of the volume are deleted.
  * **The volume is part of a DR configuration and replicating:** The volume is marked TERMINATED, but the volume is not deleted and the capacity is not returned to the system until DR completes the replication.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-block-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-block-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-block-volume.htm)


  *     1. Perform administrative tasks to remove any dependencies that any instances have for the block volume.
For example, ensure that no applications are accessing the volume. Unmount the volume and remove it from the `/etc/fstab` file, and so on. 
    2. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    3. At the top of the page, select the compartment that contains the block volume that you plan to delete.
    4. For the volume you plan to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Terminate**.
    5. Confirm the termination.
The block volume enters the TERMINATED state, and remains in that state for about 24 hours until it's removed.
  * Use the [oci bv volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/delete.html) command and required parameters to delete a block volume.
Command
CopyTry It
```
oci bv volume delete --volume-id <volume_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DeleteVolume) operation to delete a volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

