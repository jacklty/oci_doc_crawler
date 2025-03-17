Updated 2024-03-22
# Moving a Block Volume to a Different Compartment
Move a block volume in the Block Volume service to a different compartment.
When you move a block volume to a new compartment, associated Block Volume resources, such as volume backups, volume clones, and volume replicas are not moved. After you move the block volume to the new compartment, inherent policies apply immediately and affect access to the block volume through the Console. For more information, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
**Important** When you move a block volume between compartments, ensure that users have sufficient access permissions on the compartment the block volume is being moved to.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List scope** , select the compartment that contains the block volume. 
    3. In the **Block Volumes** list, click the name of the block volume that you want to move.
    4. Click **Move resource**.
    5. Choose the destination compartment from the list. 
    6. Click **Move resource**.
  * Use the [oci bv volume change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/change-compartment.html) command and required parameters to move a block volume between compartments:
Command
CopyTry It
```
oci bv volume change-compartment --compartment-id compartment-ocid --volume-id volume-ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ChangeVolumeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ChangeVolumeCompartment) operation move a block volume between compartments.


Was this article helpful?
YesNo

