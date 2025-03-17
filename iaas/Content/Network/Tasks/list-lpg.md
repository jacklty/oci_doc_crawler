Updated 2025-01-17
# Listing the LPGs
List the local peering gateways (LPGs) in a virtual cloud network (VCN).
A VCN can have several LPGs, and each one can be used to connect to one and only one other VCN. See [Gateway Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#gateway_limits) for more details on current LPG limits.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN whose LPGs you want to list. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Select the name of the VCN whose LPGs you want to list.
    4. Under **Resources** , select **Local Peering Gateways**. 
  * Use the [network local-peering-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/list.html) command and required parameters to list LPGs in a compartment:
Command
CopyTry It
```
oci network local-peering-gateway list --compartment-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListLocalPeeringGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ListLocalPeeringGateways) operation to list the LPGs in the specified compartment.


Was this article helpful?
YesNo

