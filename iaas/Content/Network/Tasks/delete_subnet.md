Updated 2025-01-15
# Deleting a Subnet
Delete a subnet from a Virtual Cloud Network (VCN).
Before you can delete a subnet, it must have no instances, [load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)s, OCI database systems, or orphaned mount targets in it. For more information, see [Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion). 
If the subnet is empty, its state changes to TERMINATING briefly and then TERMINATED. If the subnet is not empty, you get an error indicating that there are still instances or other resources in it that you must delete first.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Click **Subnets**.
    4. Click the subnet that you're interested in.
    5. On the subnet details page, click **Terminate**.
    6. When prompted, confirm the deletion. 
  * Use the [network subnet delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/delete.html) command and required parameters to delete a subnet:
Command
CopyTry It
```
oci network subnet delete --subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/DeleteSubnet) operation to delete a subnet.


Was this article helpful?
YesNo

