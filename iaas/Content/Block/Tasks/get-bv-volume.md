Updated 2023-07-12
# Getting a Block Volume's Details
View a block volume's details.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List Scope** , in the **Compartment** list, click the name of the compartment where the block volume was created.
    3. In the **Block Volumes** list, click the name of the volume.
The **Details** page for the block volume appears. The **Details** page contains information about the volume, both general information and links to its resources. Some items in the page are read-only, while other items allow you to edit and update the block volume's configuration. 
  * Use the [oci bv volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/get.html) command and required parameters to get the details of a block volume:
Command
CopyTry It
```
oci bv volume get --volume-id volume_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/GetVolume) operation to get the details for a block volume.


Was this article helpful?
YesNo

