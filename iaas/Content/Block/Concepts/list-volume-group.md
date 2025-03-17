Updated 2023-12-08
# Listing Volume Groups
List volume groups in the Block Volume service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm)


  * Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  * Use the [oci bv volume-group list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/list.html) command and required parameters to list volume groups:
Command
CopyTry It
```
oci bv volume-group list --compartment-id <compartment_ID>
```

For example:
Command
CopyTry It
```
oci bv volume-group list --compartment-id ocid1.compartment.oc1..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVolumeGroups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ListVolumeGroups) operation to list volume groups.


Was this article helpful?
YesNo

