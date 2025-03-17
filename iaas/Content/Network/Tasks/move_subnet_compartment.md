Updated 2025-01-15
# Moving a Subnet to a Different Compartment
Move a subnet in a Virtual Cloud Network (VCN) to a different compartment.
For more information, see [Working with Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#Working). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Find the subnet in the **Subnets** list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for it, and then select **Move resource**.
    4. Select the destination compartment from the list. 
    5. Click **Move resource**.
  * Use the [network subnet change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/change-compartment.html) command and required parameters to move a subnet from one compartment to another:
Command
CopyTry It
```
oci network subnet change-compartment --compartment-id destination-compartment-ocid--subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeSubnetCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ChangeSubnetCompartment) operation to move a subnet from one compartment to another.


Was this article helpful?
YesNo

