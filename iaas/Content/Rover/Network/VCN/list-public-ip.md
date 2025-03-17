Updated 2024-09-16
# Listing Reserved Public IP Addresses for a Roving Edge Infrastructure Device
Describes how to list the reserved public IP addresses for your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list-public-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list-public-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list-public-ip.htm)


  *     1. Open the navigation menu and select **Networking > IP Management**. The **IP Management** page appears.
    2. Click **Reserved Public IPs**.
The **Reserved Public IP Addresses** page appears. The reserved public IP addresses are listed in tabular form.
  * Use the [oci network public-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/list.html) and required parameters to list the reserved public IP addresses for your Roving Edge Infrastructure device:
Command
CopyTry It
```
oci network public-ip list --compartment-id compartment_ocid --scope [AVAILABILITY_DOMAIN|REGION] [OPTIONS]
```

where the possible values for `scope` are:
    * REGION: The public IP exists within a region and is assigned to a regional entity (such as a NatGateway), or can be assigned to a private IP in any availability domain in the region. Reserved public IPs have _scope_ = _REGION_ , as do ephemeral public IPs assigned to a regional entity.
    * AVAILABILITY_DOMAIN: The public IP exists within the availability domain of the entity it's assigned to, which is specified by the _availabilityDomain_ property of the public IP object. Ephemeral public IPs that are assigned to private IPs have _scope_ = _AVAILABILITY_DOMAIN_.
To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListPublicIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/ListPublicIps) operation to list the reserved public IP addresses for your Roving Edge Infrastructure device.


Was this article helpful?
YesNo

