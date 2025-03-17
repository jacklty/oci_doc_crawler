Updated 2025-01-17
# Deleting an LPG
Delete a local peering gateway (LPG) from a Virtual Cloud Network (VCN) in Networking.
**Prerequisite:** Before you delete an LPG, delete all route rules in the VCN that specify the LPG as the target. Deleting those rules stops the routing in the VCN to the LPG. If a route rule refers to the LPG, it can't be deleted until the reference is removed.
See [Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#list-routetable "List VCN route tables in a given VCN and compartment.") and [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") for more about finding and updating route rules that refer to a gateway.
After deletion, the LPG's state could still be PEERED if the other LPG still exists. Whenever an LPG is deleted, the LPG at the other side of the peering changes to the REVOKED state. 
**Note**
After deleting an LPG, ensure that the other LPG in the peering (in the other VCN) is removed. That LPG can't be peered again. See [Repurposing an LPG fails](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#lpg-delete) for more detail.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the VCN that contains the LPG to delete. 
    3. Under Resources, select **Local Peering Gateways**. 
    4. For the LPG that you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Terminate**.
    5. Confirm when prompted.
  * Use the [network local-peering-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/delete.html) command and required parameters to delete an LPG:
Command
CopyTry It
```
oci network local-peering-gateway delete --local-peering-gateway-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/DeleteLocalPeeringGateway) operation to delete an LPG.


Was this article helpful?
YesNo

