Updated 2024-09-16
# Deleting a VCN from a Roving Edge Infrastructure Device
Describes how to delete a VCN on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete_vcn.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
    2. Click the VCN. The VCN's **Details** page appears.
    3. Click **Terminate**.
    4. Confirm the deletion when prompted.
  * Use the [oci network vcn delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/delete.html) command and required parameters to delete a VCN on your Roving Edge Infrastructure devices:
Copy
```
oci network vcn delete --vcn-id vcn_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/DeleteVcn) operation to delete a VCN on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

