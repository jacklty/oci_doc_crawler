Updated 2024-09-16
# Creating a Subnet for a Roving Edge Infrastructure Device
Describes how to create a subnet under the VCN on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
    2. Click the VCN. The VCN's **Details** page appears.
    3. Click **Create Subnet**. The **Create Subnet** dialog box appears.
    4. Specify the resources to associate with the subnet. By default, the subnet is created in the root compartment, where you can also choose your resources. 
Enter the following:
       * **Name** : A friendly name for the subnet. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **CIDR Block** : A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Ensure that the CIDR block is within the cloud network's CIDR block and does not overlap with any other subnets. You cannot change this value later.
       * **Use DNS Hostnames in this SUBNET** : This option is available only if you provided a DNS label for the VCN during creation. The option is required for assignment of DNS hostnames to hosts in the subnet. Enabling this option is required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). 
If the check box is selected, you can specify a DNS label for the subnet, otherwise the Device Console generates one for you. The dialog box automatically displays the corresponding **DNS Label** for the subnet (`<subnet_DNS_label>.<VCN_DNS_label>.oraclevcn.com`).
       * **DHCP Options** : The set of DHCP options to associate with the subnet.
    5. Click **Create Subnet**. The subnet is then created and displayed on the **Subnets** page in the root compartment.
  * Use the [oci network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html) command and required parameters to create a subnet under a VCN on your Roving Edge Infrastructure devices:
Copy
```
oci network subnet create --compartment-id compartment_ocid --vcn-id vcn_ocid --cidr-block cidr_block [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet) operation to create a subnet under a VCN on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

