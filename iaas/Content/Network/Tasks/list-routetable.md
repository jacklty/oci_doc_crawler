Updated 2025-01-15
# Listing VCN Route Tables
List VCN route tables in a given VCN and compartment.
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
The default VCN route table is displayed in the list of route tables.
  * Use the [network route-table list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/list.html) command and required parameters to list the route tables in the specified VCN and compartment.:
Command
CopyTry It
```
oci network route-table list --compartment-id compartment-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListRouteTables](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ListRouteTables) operation to list the route tables in the specified VCN and compartment.


Was this article helpful?
YesNo

