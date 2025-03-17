Updated 2023-12-08
# Moving a Volume Group to a Different Compartment
Move a volume group in the Block Volume service to another compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Under **List scope** , select the compartment that contains the volume group.
    3. In the **Volume Groups** list, click the volume group you want to move.
    4. Click **Move resource**.
    5. In the **Move resource** dialog box, select the compartment that you want to move the volume group to.
    6. Click **Move resource**.
  * Use the [oci bv volume-group change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/change-compartment.html) command and required parameters to move a volume group to a different compartment:
Command
CopyTry It
```
oci bv volume-group change-compartment --volume-group-id <volume-group_ID> --compartment-id <compartment_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeVolumeGroupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ChangeVolumeGroupCompartment) operation to move a volume group to a different compartment.


Was this article helpful?
YesNo

