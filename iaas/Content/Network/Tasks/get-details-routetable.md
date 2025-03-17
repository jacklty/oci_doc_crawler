Updated 2025-01-15
# Getting a VCN Route Table's Details
Get details for a Virtual Cloud Network (VCN) route table. 
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
The default route table and any other route tables that have been created are displayed in the list of tables.
    4. Click a route table's name to view its details. 
  * Use the [network route-table get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/get.html) command and required parameters to get details for a VCN route table:
Command
CopyTry It
```
oci network route-table get --rt-id ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/GetRouteTable) operation to get details for a VCN route table.


Was this article helpful?
YesNo

