Updated 2024-01-18
# Moving a Volume to a Different Compartment
On Compute Cloud@Customer, you can move Block Volume resources such as block volumes, boot volumes, clones, volume backups, volume groups, and volume group backups from one compartment to another. 
When you move a resource to a new compartment, associated resources might not be moved. For example, when you move a block volume, any backups of that volume are not moved. 
**Important**
Any access policies that exist on the new compartment apply immediately. Before you move resources to a different compartment, ensure that the resource users have sufficient access permissions on the compartment the resource is being moved to.
  * You can't move a block volume or boot volume from a security zone to a standard compartment.
  * You can't move a volume from a standard compartment to a compartment that is in a security zone if the volume violates any security zone policies.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/moving-a-volume-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/moving-a-volume-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/moving-a-volume-to-a-different-compartment.htm)


  * This task isn't available in the Console.
  * Use the [oci bv boot-volume change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/change-compartment.html):
Command
CopyTry It
```
oci bv volume change-compartment --volume-id <volume_OCID> --compartment-id <destination_compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ChangeVolumeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ChangeVolumeCompartment) operation to move a volume to another compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

