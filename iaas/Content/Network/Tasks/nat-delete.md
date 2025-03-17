Updated 2025-01-17
# Deleting a NAT Gateway
Delete a NAT gateway from a Virtual Cloud Network (VCN) in Networking.
**Prerequisite:** Before you delete a NAT gateway, delete all route rules in the VCN that specify the gateway as the target. Deleting those rules stops the routing in the VCN to the gateway. If a route rule refers to the gateway, it can't be deleted until the reference is removed.
See [Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#list-routetable "List VCN route tables in a given VCN and compartment.") and [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") for more about finding and updating route rules that refer to a gateway.
This operation is asynchronous. The NAT gateway's _lifecycleState_ state changes to TERMINATING temporarily until the NAT gateway is removed.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
    4. For the NAT gateway that you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Terminate**.
    5. To confirm, select **Terminate**. 
  * Use the [network nat-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/delete.htm) command and required parameters to delete a NAT gateway:
Command
CopyTry It
```
oci network nat-gateway delete --nat-gateway-id nat-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/DeleteNatGateway) operation to delete a NAT gateway.


Was this article helpful?
YesNo

