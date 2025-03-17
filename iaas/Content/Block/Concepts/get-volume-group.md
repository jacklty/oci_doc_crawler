Updated 2023-12-08
# Getting a Volume Group's Details
Get details for a volume group in the Block Volume service, including a list of the block volumes and boot volumes in the volume group.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Under **List Scope** , in the **Compartment** list, click the name of the compartment where the volume group was created.
    3. In the **Volume Groups** list, click the volume group you want to view the volumes for.
    4. To view the block volumes for the volume group, in **Resources** , click **Block volumes**.
    5. To view the boot volumes for the volume group, in **Resources** , click **Boot volumes**.
  * Use the [oci bv volume-group get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/get.html) command and required parameters to get details for a volume group:
Command
CopyTry It
```
oci bv volume-group get --volume-group-id <volume-group-ID>
```

For example:
Command
CopyTry It
```
oci bv volume-group get --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/GetVolumeGroup) operation to get details for a volume group.


Was this article helpful?
YesNo

