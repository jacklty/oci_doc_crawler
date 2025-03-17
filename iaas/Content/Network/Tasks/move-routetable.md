Updated 2025-01-15
# Moving a VCN Route Table to a Different Compartment
Move a Virtual Cloud Network (VCN) route table to a different compartment. 
For an overview of routing in your VCN and subnets, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Route Tables**. 
    4. Find the route table in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right side of it, and then select **Move resource**.
    5. Select the destination compartment from the list. 
    6. Click **Move Resource**.
  * Use the [network route-table change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/change-compartment.html) command and required parameters to move a VCN route table to a different compartment:
Command
CopyTry It
```
oci network route-table change-compartment --compartment-id destination-ocid --rt-id routetable-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeRouteTableCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ChangeRouteTableCompartment) operation to move a VCN route table to a different compartment.


Was this article helpful?
YesNo

