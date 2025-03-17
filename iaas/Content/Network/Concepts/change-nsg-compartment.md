Updated 2025-01-15
# Moving an NSG to a Different Compartment
Move a network security group (NSG) in a Virtual Cloud Network (VCN) between compartments. 
When you move an NSG to a new compartment, inherent policies apply immediately. 
For more information about using compartments and policies to control access to resources in your cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
    4. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right side of the NSG, and then select **Move resource**.
    5. Select the destination compartment from the list. 
    6. Click **Move resource**.
  * Use the [network nsg change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/change-compartment.html) command and required parameters to move an NSG from one compartment to another:
Command
CopyTry It
```
oci network nsg change-compartment --compartment-id destination-compartment-ocid --nsg-id nsg-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeNetworkSecurityGroupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/ChangeNetworkSecurityGroupCompartment) operation to move an NSG from one compartment to another.


Was this article helpful?
YesNo

