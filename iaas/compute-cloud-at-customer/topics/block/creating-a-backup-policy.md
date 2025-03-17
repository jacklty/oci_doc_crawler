Updated 2024-08-06
# Creating a Backup Policy
On Compute Cloud@Customer, you can use an Oracle defined backup policy, or you can follow the procedures described in this section to create your own backup policy.
For details about Oracle defined backup policies, see [Viewing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-backup-policies.htm#viewing-backup-policies "On Compute Cloud@Customer, after creating a backup policy, you can use the Compute Cloud@Customer Console, CLI, or API to view the policy.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm)


  * When you create a backup policy by using the Console, creating the backup policy schedule is a separate step. A policy can't be assigned to a resource until the policy schedule is defined.
    1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Backup Policies**.
    2. Click **Create Backup Policy**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the policy.
       * **Create in Compartment:** Select the compartment for the policy.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Backup Policy**.
A policy can't be assigned to a resource until at least one schedule is defined.
    5. Click the name of the new backup policy to go to the details page for the policy.
    6. On the policy details page, under Resources, click **Add Schedule**.
    7. Enter the following schedule parameters:
       * **Schedule Type:** Select **Daily** , **Weekly** , or **Monthly** , and then specify the time for the backup to run and the length of time to retain the backup.
         * **Hourly:** Select the Retention Time In Hours (1 - 24).
         * **Daily:** Select the Hour of the Day (0 - 23) and the Retention Time In Days (1 - 365).
         * **Weekly:** Select the Day of the Week and the Hour of the Day, and select the Retention Time In Weeks (1 - 52).
         * **Monthly:** Select the Day of the Month (1 - 31) and the Hour of the Day, and select the Retention Time In Months (1 - 144).
       * **Time Zone:** Select either UTC or your Regional Time.
    8. Click **Add Schedule**.
The policy can now be assigned to one or more resources. See [Assigning a Backup Policy to a Volume or Volume Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm#assinging-a-backup-policy-to-a-volume-or-volume-group "On Compute Cloud@Customer, after creating a backup policy, you assign the policy to one or more volumes or volume groups.").
A policy can have more than one schedule. To add another schedule to this policy, click **Add Schedule** again. See the schedule notes in [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.").
  * Use the [oci bv volume-backup-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/create.html) command and required parameters to create a new user defined backup policy.
Command
CopyTry It
```
oci bv volume-backup-policy create --compartment-id  _<compartment_OCID>_ --display-name <discriptive_name> --schedule <json_string> or file://<path_to_JSON_file> [OPTIONS]
```

Once the policy is created, it can be applied to one or more volumes and volume groups. See [Assigning a Backup Policy to a Volume or Volume Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm#assinging-a-backup-policy-to-a-volume-or-volume-group "On Compute Cloud@Customer, after creating a backup policy, you assign the policy to one or more volumes or volume groups."). 
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy) operation to create a new user defined backup policy.
Once the policy is created, it can be applied to one or more volumes and volume groups. See [Assigning a Backup Policy to a Volume or Volume Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/assinging-a-backup-policy-to-a-volume-or-volume-group.htm#assinging-a-backup-policy-to-a-volume-or-volume-group "On Compute Cloud@Customer, after creating a backup policy, you assign the policy to one or more volumes or volume groups.").
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

