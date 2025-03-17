Updated 2025-01-15
# Changing Which VCN Route Table a Subnet Uses
Change which virtial cloud network (VCN) route table a subnet uses. 
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Click **Subnets**.
    4. Click the name of the subnet you're interested in.
    5. Click **Edit**.
    6. In the **Route Table** section, select the new route table you want the subnet to use.
    7. Click **Save changes**.
The changes takes effect within a few seconds.
  * Use the [network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and described parameters to change which route table a subnet uses:
Command
CopyTry It
```
oci network subnet update --subnet-id ocid --route-table-id routetable-ocid ... [OPTIONS]
```

The route-table-id is the OCID of the route table the subnet will use. 
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) operation to change which VCN route table a subnet uses.


Was this article helpful?
YesNo

