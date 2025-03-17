Updated 2024-01-18
# Moving a Compute Cloud@Customer Upgrade Schedule Between Compartments
Move an existing Compute Cloud@Customer upgrade schedule to a different compartment within the same tenancy.
You must have the required permissions in both compartments. See [Preparing Your Tenancy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#preparing-your-tenancy "Before the Compute Cloud@Customer infrastructure is connected to Oracle Cloud Infrastructure, the tenancy administrator must set up compartments, create policies, and configure a virtual cloud network. This setup is used to connect the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.") for details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/move-upgrade-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/move-upgrade-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/move-upgrade-schedule.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Upgrade Schedules**.
    3. Click the name of the upgrade schedule that you want to move to a different compartment. If you don't see the upgrade schedule that you want, you might need to change compartments.
    4. Click **Move resource**. 
    5. Choose the compartment to move the upgrade schedule to, and then click **Move resource**.
  * Use the [ccc upgrade-schedule change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/upgrade-schedule/change-compartment.html) command and required parameters to move an upgrade schedule to a different compartment:
Command
CopyTry It
```
oci ccc upgrade-schedule change-compartment --compartment-id <compartment ocid of the new compartment> --upgrade-schedule-id <OCID of the upgrade schedule to be moved> ... [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ChangeCccUpgradeScheduleCompartment](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/ChangeCccUpgradeScheduleCompartment) operation to move a Compute Cloud@Customer upgrade schedule to a different compartment in the tenancy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

