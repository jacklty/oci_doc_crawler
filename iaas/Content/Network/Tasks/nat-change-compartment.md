Updated 2025-01-17
# Moving a NAT Gateway to a Different Compartment 
Move a NAT gateway into a different compartment within the same tenancy.
You can move a NAT gateway from one compartment to another. When you move a NAT gateway to a new compartment, inherent policies apply immediately. 
For more information about using compartments and policies to control access to a cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
    4. For the NAT gateway you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move resource**.
    5. Select the destination compartment from the list. 
    6. Select **Move resource**.
  * Use the [network nat-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/change-compartment.htm) command and required parameters to move a NAT gateway:
Command
CopyTry It
```
oci network nat-gateway change-compartment --compartment-id new-compartment-ocid --nat-gateway-id nat-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeNatGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/ChangeNatGatewayCompartment) operation to move a NAT gateway.


Was this article helpful?
YesNo

