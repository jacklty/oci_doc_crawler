Updated 2024-09-16
# Listing VCNs for a Roving Edge Infrastructure Device
Describes how to list the VCNs on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list_vcn.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
  * Use the [oci network vcn list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/list.html) command and required parameters how to list the VCNs on your Roving Edge Infrastructure devices:
Copy
```
oci network vcn list --compartment-id compartment_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns) operation how to list the VCNs on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

