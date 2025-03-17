Updated 2025-02-06
# Creating a VCN Route Table
Create a Virtual Cloud Network (VCN) route table in a specific VCN and compartment. 
For an overview of routing in VCNs and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
    4. Click **Create Route Table**. 
    5. Enter the following information:
       * **Name:** A friendly name for the route table. The name doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** The compartment where you want to create the route table, if different from the compartment you're currently working in. 
    6. Optionally, click **+Additional Route Rule** to add one or more route rules, each with the following information. You can create a route table with no rules and then add them later. 
       * **Target Type:** See the list of target types in [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN). If the target type is a DRG, the VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. If the target is a private IP object, before you specify the target you must first disable the source/destination check on the VNIC that uses that private IP object. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). 
       * **Destination CIDR Block** : Available only if the target isn't a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the destination CIDR block for the traffic. You can provide a specific destination CIDR block, or use 0.0.0.0/0 if all traffic leaving the subnet needs to be routed to the target specified in this rule.
       * **Destination Service:** Available only if the target is a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.
       * **Compartment:** The compartment containing the target.
       * **Target:** The target. If the target is a private IP object, enter its OCID. Or you can enter the private IP address itself, in which case the Console finds the corresponding OCID and uses it as the target for the route rule.
       * **Description:** An optional description of the rule.
    7. Optionally, click **Show Tagging Options** and assign tags to the route table. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    8. Click **Create**.
The route table is created and then displayed on the **Route Tables** page in the compartment you chose. You can now specify this route table when creating or updating a subnet. 
  * Use the [network route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/create.html) command and required parameters to create a VCN route table:
Command
CopyTry It
```
oci network route-table create --compartment-id compartment-ocid --route-rules rules --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable) operation to create a route table.


Was this article helpful?
YesNo

