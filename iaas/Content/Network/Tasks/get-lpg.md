Updated 2025-01-17
# Getting Details for an LPG
Get configuration details for a specific LPG in a virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-lpg.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN with the LPG you want to see details for. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Select the name of the VCN with the LPG you want to see details for.
    4. Under **Resources** , select **Local Peering Gateways**. 
    5. Select the name of the LPG you're interested in.
  * Use the [network local-peering-gateway get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/get.html) command and required parameters to get configuration details for a specific LPG:
Command
CopyTry It
```
oci network local-peering-gateway get --local-peering-gateway-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/GetLocalPeeringGateway) operation to get configuration details for a specific LPG.


Was this article helpful?
YesNo

