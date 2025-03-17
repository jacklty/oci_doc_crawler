Updated 2025-02-21
# Managing Backup Policies
On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.
The Block Volume service enables you to perform volume backups and volume group backups automatically according to a schedule that's defined in a backup policy. The backup policy also specifies how long to retain the backup.
You can use one of the backup policies defined by Oracle and available in every compartment, or you can create your own user-defined backup policy as described in [Creating a Backup Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm#creating-a-backup-policy "On Compute Cloud@Customer, you can use an Oracle defined backup policy, or you can follow the procedures described in this section to create your own backup policy."). You can't modify policies that are provided by Oracle. You can't use an Oracle defined backup policy to back up a volume group.
On Compute Cloud@Customer, all backups are full backups.
A particular resource can't be assigned more than one backup policy. A particular policy can have more than one backup schedule.
**Schedule Notes**
These notes apply to both user-defined and Oracle-defined backup policies.
  * Start time: A backup might not start at its scheduled start time. A backup can be delayed for hours if the system is very busy.
  * Conflicts: The Block Volume service will not run more than one scheduled backup of a particular resource in one day. If more than one backup is scheduled to run on the same day (for example, daily, weekly, and monthly backups are all scheduled to run this Sunday), the Block Volume service will run the backup that has the longest schedule period.


**Caution**
All policy-based (scheduled) backups expire. A manual backup expires if a scheduled backup of the same volume is created after the manual backup was created. To keep a volume backup indefinitely, cancel all future scheduled backups and create a manual backup as described in [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
## Oracle Provided Backup Policies 🔗 
Oracle defined backup policies can be used to back up individual block volumes and boot volumes. These policies can't be used to back up a volume group.
Oracle defined policies can't be changed. If you need a different backup time or retention time, for example, create a user defined backup policy as described in [Creating a Backup Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm#creating-a-backup-policy "On Compute Cloud@Customer, you can use an Oracle defined backup policy, or you can follow the procedures described in this section to create your own backup policy."). 
The following backup policies are provided by Oracle and available in every compartment. A resource can have only one backup policy assigned, but a backup policy can have multiple schedules. The Oracle Bronze policy has one schedule, the Silver policy has two schedules, and the Gold policy has three schedules. All schedule times are your regional data center time. All backup types are full backups.  

Bronze
    
  1. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.



Silver
    
  1. Weekly backups that run at 00:00 every Monday and are retained for four weeks.
  2. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.



Gold
    
  1. Daily backups that run at 00:00 and are retained for seven days.
  2. Weekly backups that run at 00:00 every Monday and are retained for four weeks.
  3. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.


The Block Volume service will not run more than one scheduled backup of a particular resource in one day. When schedules conflict, for example, daily, weekly, and monthly backups are scheduled to run at the same time, the backup with the longest period runs.
Was this article helpful?
YesNo

