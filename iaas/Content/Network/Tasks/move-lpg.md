Updated 2025-01-17
# Moving a local peering gateway to a different compartment
You can move a local peering gateway (LPG) from one compartment to another. When you move a local peering gateway to a new compartment, IAM policies for the new compartment apply immediately. 
For more information about using compartments and policies to control access to a cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the VCN you're interested in.
    3. Under **Resources** , select **Local Peering Gateways**.
    4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the local peering gateway, and then select **Move Resource**. 
    5. Select the destination compartment from the list. 
    6. Select **Move Resource**.
  * Use the [network local-peering-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/change-compartment.html) command and required parameters to get configuration details for a specific LPG:
Command
CopyTry It
```
oci network local-peering-gateway change-compartment --local-peering-gateway-id ocid --compartment-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeLocalPeeringGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ChangeLocalPeeringGatewayCompartment) operation to move a local peering gateway (LPG) from one compartment to another.


Was this article helpful?
YesNo

