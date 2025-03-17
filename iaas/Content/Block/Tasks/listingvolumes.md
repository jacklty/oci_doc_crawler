Updated 2023-07-12
# Listing Volumes
View a list of the block volumes in your tenancy.
You can list all block volumes in a specific compartment. To view detailed information for a single volume, see [Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#top "View a block volume's details.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm)


  * Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. A detailed list of volumes in your current compartment is displayed.
    * To view the volumes in a different compartment, change the compartment in the **Compartment** drop-down menu.
  * Use the [oci bv volume list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/list.html) command and required parameters to list the block volumes in your tenancy:
Command
CopyTry It
```
oci bv volume list [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ListVolumes) operation to list the block volumes in your tenancy.


Was this article helpful?
YesNo

