Updated 2025-01-17
# Blocking or Allowing Traffic for a NAT Gateway
Block or allow traffic for a NAT gateway.
You create a NAT gateway in the context of a specific VCN. The NAT gateway is automatically always attached to only one VCN. However, you can block or allow traffic through the NAT gateway at any time. By default, the gateway allows traffic upon creation. Blocking the NAT gateway prevents all traffic from flowing, regardless of any existing route rules or security rules in the VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
    4. For the NAT gateway you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Block Traffic** (or **Allow Traffic** if you previously blocked traffic).
    5. Select **Block Traffic** (or **Allow Traffic** if you previously blocked traffic) to confirm.
When the traffic is blocked, the NAT gateway's icon turns gray, and the label changes to BLOCKED. When the traffic is allowed, the NAT gateway's icon turns green, and the label changes to AVAILABLE. 
  * Use the [network nat-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/update.htm) command and required parameters to block (true) or allow (false) traffic for a NAT gateway:
Command
CopyTry It
```
oci network nat-gateway update --nat-gateway-id nat-ocid --block-traffic [true | false] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/UpdateNatGateway) operation to block or allow traffic for a NAT gateway.


Was this article helpful?
YesNo

