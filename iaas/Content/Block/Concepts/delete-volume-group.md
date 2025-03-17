Updated 2023-12-08
# Deleting a Volume Group
Delete a volume group in the Block Volume service.
**Note** When you delete a volume group the individual volumes in the group are not deleted, only the volume group is deleted. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Under **List scope** , select the compartment that contains the volume group.
    3. In the **Volume Groups** list, click the volume group you want to delete.
    4. On the **Volume Group Details** page, click **Terminate**.
    5. On the **Terminate volume group** dialog, click **Terminate**.
  * Use the [oci bv volume-group delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/delete.html) command and required parameters to delete a volume group:
Command
CopyTry It
```
oci bv volume-group delete --volume-group-id <volume-group_ID>
```

For example:
```
oci bv volume-group delete --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/DeleteVolumeGroup) operation to delete a volume group.


Was this article helpful?
YesNo

