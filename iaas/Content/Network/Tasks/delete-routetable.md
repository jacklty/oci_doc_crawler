Updated 2025-01-15
# Deleting a VCN Route Table
Delete a Virtual Cloud Network (VCN) route table.
**Prerequisite:** To delete a route table, it must not be associated with a subnet or gateway. If you associate a route table with a gateway, afterwards the gateway must always have a route table associated with it. You can modify the rules in the current route table or replace it with another route table.
You can't delete the default route table in a VCN.
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
    4. Click the route table you're interested in.
    5. Click **Terminate**. 
    6. Confirm when prompted.
  * Use the [network route-table delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/delete.html) command and required parameters to delete a VCN route table:
Command
CopyTry It
```
oci network route-table delete --rt-id routetable-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/DeleteRouteTable) operation to delete a VCN route table.


Was this article helpful?
YesNo

