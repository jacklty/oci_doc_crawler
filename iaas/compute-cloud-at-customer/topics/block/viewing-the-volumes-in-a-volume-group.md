Updated 2024-01-18
# Viewing the Volumes in a Volume Group
On Compute Cloud@Customer, you can view volume groups using the Compute Cloud@Customer Console, CLI, and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-the-volumes-in-a-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-the-volumes-in-a-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-the-volumes-in-a-volume-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume group you want to see.
    3. In the **Volume Groups** list, click the volume group you want to see.
    4. To view the block volumes in the volume group, under **Resources** , click **Volumes**.
  * Use the [oci bv volume-group list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/list.html) command and required parameters to list volume groups.
Command
CopyTry It
```
oci bv volume-group list --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListVolumeGroups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ListVolumeGroups) operation to list volume groups.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

