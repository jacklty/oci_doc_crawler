Updated 2025-01-17
# Associating a Route Table with an Existing LPG
To use transit routing, you must associate a route table to an LPG after you create the LPG.
**Prerequisite:** The route table must exist and belong to the VCN that the LPG belongs to.
This task is related to an advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). Associating a route table to an LPG influences the behavior of traffic entering the VCN through the LPG.
An LPG can exist without having an associated route table. After you associate a route table with an LPG there must always be a route table associated with it, but you can associate a _different_ route table. You can also edit the table's rules, or delete some or all rules. 
**Note** The route rules in a route table associated with an LPG can point to a DRG or a private IP address in the same VCN as the LPG.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the VCN you're interested in. 
    3. Under **Resources** , select **Local Peering Gateways**.
    4. For the LPG you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select either: 
       * **Associate With Route Table:** If the LPG has no route table associated with it yet.
       * **Replace Route Table Association:** If you're changing which route table is associated with the LPG.
    5. Select the compartment where the route table resides, and select the route table itself.
    6. Select **Associate**.
  * Use the [network local-peering-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/update.html) command and required parameters to change the name and associated route table of a local peering gateway (LPG):
Command
CopyTry It
```
oci network local-peering-gateway update --local-peering-gateway-id ocid --route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/UpdateLocalPeeringGateway) operation to set the `routeTableId` to associate a route table to an LPG.


Was this article helpful?
YesNo

