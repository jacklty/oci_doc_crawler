Updated 2025-02-06
# Updating a VCN Route Table's Rules
Add, edit, or delete rules for a Virtual Cloud Network (VCN) route table. 
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
    4. Click the name of the route table you're interested in.
    5. If you want to create a route rule, click **Add Route Rule** , and enter the following information:
       * **Target Type:** See the list of target types in [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN). If the target type is a DRG, the VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. If the target is a private IP object, before you specify the target you must first disable the source/destination check on the VNIC that uses that private IP object. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). 
       * **Destination CIDR Block** : Available only if the target isn't a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the destination CIDR block for the traffic. You can provide a specific destination CIDR block, or use 0.0.0.0/0 if all traffic leaving the subnet needs to be routed to the target specified in this rule.
       * **Destination Service:** Available only if the target is a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.
       * **Compartment:** The compartment containing the target.
       * **Target:** The target. If the target is a private IP object, enter its OCID. Or you can enter the private IP address itself, in which case the Console finds the corresponding OCID and uses it as the target for the route rule.
       * **Description:** An optional description of the rule.
    6. If you want to delete an existing rule, select the checkbox next to the rule, and then click **Remove**.
    7. If you wanted to edit an existing rule, select the checkbox next to the rule, and then click **Edit**.
  * Use the [network route-table update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/update.html) command and required parameters to update the specified route table's display name or route rules:
Command
CopyTry It
```
oci network route-table update --rt-id ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) operation to update the specified route table's display name or route rules.


Was this article helpful?
YesNo

