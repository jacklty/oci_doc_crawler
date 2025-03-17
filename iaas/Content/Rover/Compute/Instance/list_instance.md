Updated 2024-09-16
# Listing Instances for a Roving Edge Infrastructure Device
Describes how to list the compute instances on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list_instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list_instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list_instance.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
  * Use the [oci compute instance list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/list.html) command and required parameters to list the compute instances on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance list --compartment-id compartment_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation to display a list of instances.


Was this article helpful?
YesNo

