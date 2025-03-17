Updated 2024-01-18
# Assigning a Backup Policy to a Volume or Volume Group
On Compute Cloud@Customer, after creating a backup policy, you assign the policy to one or more volumes or volume groups.
You can assign a backup policy to a volume or volume group at resource creation or later:
  * During volume or volume group creation. Select from the Backup Policy list in the Console or specify the ``--backup-policy-id`` option in the CLI.
  * After the volume or volume group is created. Follow the procedures described in this section to add a backup policy if no backup policy is assigned, or to change the backup policy that is assigned to a volume or volume group.


A volume or volume group can have only one backup policy assigned. If a backup policy is already assigned to this volume or volume group when you assign a new policy, the existing assignment is replaced with the new assignment.
A volume group cannot be assigned a backup policy if any of the volumes in the group already is assigned a backup policy. To remove a backup policy assignment from a volume, see [Removing a Backup Policy Assignment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/removing-a-backup-policy-assignment.htm#removing-a-backup-policy-assignment "On Compute Cloud@Customer, you can remove a backup policy assignment from a volume or volume group. A volume group cannot be assigned a backup policy if any of the volumes in the group already is assigned a backup policy.").
**Note**
Oracle defined backup policies cannot be used for volume group backups. Only user defined backup policies can be assigned to a volume group.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes** , **Boot Volumes** , or **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume or volume group to which you want to assign a backup policy.
    3. For the volume or volume group to which you want to assign a backup policy, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Assign Backup Policy**.
    4. In the **Assign Backup Policy dialog** , select a backup policy from the drop-down list.
You can't assign an Oracle defined policy to a volume group.
    5. Click **Assign Backup Policy**.
  * Use the [oci bv volume-backup-policy-assignment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy-assignment/create.html) command and required parameters to assign a volume backup policy to the specified volume. 
Command
CopyTry It
```
oci bv volume-backup-policy-assignment create --asset-id <volume_OCID> --policy-id <backup-policyABC> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy) operation to assign a volume backup policy to the specified volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

