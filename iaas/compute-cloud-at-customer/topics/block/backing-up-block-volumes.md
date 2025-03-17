Updated 2025-02-21
# Backing Up Block Volumes
On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.
On Compute Cloud@Customer, all backups are full backups.
There are two ways to initiate a backup:
  * **Manual Backups:** These are full backups that you can launch immediately. See [Creating a Manual Boot or Block Volume Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm#creating-a-manual-volume-backup "On Compute Cloud@Customer, you can create a block or boot volume backup manually using the Compute Cloud@Customer Console, CLI, and API.").
  * **Policy-Based Backups:** These are automated scheduled backups defined by the backup policy assigned to the volume. See [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.").


For information to help you decide whether to create a backup or a clone of a boot volume, see [Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__volume-backups-clones).
Was this article helpful?
YesNo

