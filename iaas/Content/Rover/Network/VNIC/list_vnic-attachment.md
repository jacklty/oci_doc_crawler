Updated 2024-09-16
# Listing VNIC Attachments for Roving Edge Infrastructure
Describes how to list the VNIC attachments on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to list VNIC attachments. The instance's **Details** page appears.
    4. Click **Attached VNICs** under **Resources**. The primary VNIC is listed. If the instance has two active physical NICs, the VNICs are grouped by NIC 0 and NIC 1.
  * #### Listing the VNIC attachments for a compartment 🔗 
Use the [oci compute vnic-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/vnic-attachment/list.html) command and required parameters to list the VNIC attachments on your Roving Edge Infrastructure devices:
Copy
```
oci compute vnic-attachment list --compartment-id compartment_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
#### Listing VNIC attachments for an instance 🔗 
Use the [oci compute instance list-vnics](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/list-vnics.html) command and required parameters to list the VNIC attachments on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance list-vnics [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Use the [ListVnicAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments) operation to list the VNIC attachments on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

