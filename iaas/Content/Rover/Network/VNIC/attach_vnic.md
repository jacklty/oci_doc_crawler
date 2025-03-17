Updated 2024-11-18
# Creating and Attaching a Secondary VNIC to a Roving Edge Infrastructure Device
Describes how to create and attach a secondary VNIC to your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to create and attach a secondary VNIC. The instance's **Details** page appears.
    4. Under **Resources** , click **Attached VNICs**. The primary VNIC and any secondary VNICs attached to the instance are displayed.
    5. Click **Create VNIC**. The **Create VNIC** dialog box appears.
    6. Enter the following information:
       * **Name** : Enter a name for the secondary VNIC.
       * **Virtual cloud network** : Select the VCN that contains the subnet of interest from the list.
       * **Subnet** : Select the subnet of interest from the list. The secondary VNIC must be in the same availability domain as the instance's primary VNIC, so the subnet list includes any regional subnets or AD-specific subnets in the primary VNIC availability domain.
       * **Private IP Address** : Enter an available private IP address of your choice from the subnet CIDR (otherwise the private IP address is automatically assigned).
       * **Assign a public IP address** : Specify whether to assign a public IP address to the VNIC primary private IP. Available only if the subnet is public. Select this option to specify an existing reserved public IP address by name, or to create a new reserved IP address by assigning a name and selecting a source IP pool for the address. If you don't select an IP pool, the default Oracle IP pool is used.
       * **Hostname** : Enter a hostname to be used for DNS within the cloud network. Available only if the VCN and subnet both have DNS labels.
    7. Click **Submit**. 
The secondary VNIC is created and then displayed on the **Attached VNICs** page for the instance. It can take several seconds before the secondary VNIC appears on the page.
    8. Make note of the secondary VNIC OCID. You might need it when you configure the instance OS.
    9. Configure the OS to use the VNIC.
See [Configuring the Instance OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance-multi-vnic.htm#configure-multiple-vnics "On Roving Edge Infrastructure, after you create a secondary VNIC, log in to the instance OS and configure the OS to use the new VNIC.").
  * Use the [oci compute instance attach-vnic](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/attach-vnic.html) command and required parameters to create and attach a secondary VNIC to your Roving Edge Infrastructure devices:
Copy
```
oci compute instance attach-vnic --instance-id instance_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [AttachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/AttachVnic) operation to create and attach a secondary VNIC to your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

