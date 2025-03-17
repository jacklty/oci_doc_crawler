Updated 2025-01-15
# Tagging a VCN Route Table
Manage tags for a Virtual Cloud Network (VCN) route table. 
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tagging-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tagging-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tagging-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
    4. Click a route table's name to view its details. 
    5. Find the route table in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Add Tags**.
  * Use the [network route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/create.html) command and required parameters to add tags when you create a VCN route table:
Command
CopyTry It
```
oci network route-table create --compartment-id ocid --route-rules rules --vcn-id ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

Use the [network route-table update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/update.html) command and required parameters to add tags to the specified route table:
Command
CopyTry It
```
oci network route-table update --rt-id ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable) operation to add tags when you create a subnet, and use the definedTags attribute.
Run the [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) operation to add tags when you update a subnet, and use the definedTags or freeformTags attributes.


Was this article helpful?
YesNo

