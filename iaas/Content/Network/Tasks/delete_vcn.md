Updated 2025-01-15
# Deleting a VCN
Delete a Virtual Cloud Network (VCN) from OCI. 
The Console has an easy "Delete all" process that scans the chosen compartments then deletes a VCN and its related Networking resources (subnets, route tables, security lists, sets of DHCP options, internet gateway, and so on). If the VCN is attached to a Dynamic Routing Gateway (DRG), the process deletes the attachment, but the DRG remains. 
The "Delete All" process deletes one resource at a time. A VCN with many compartments and resources takes longer to delete than a VCN with only a few. A progress report is displayed to show the results of both the scan for resources and the deletion of those resources. 
**Note**
Before using the "Delete All" process, verify that no resources such as compute instances, [load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm), OCI database systems, or orphaned mount targets are present in any of the subnets. If any of these are present, the deletion process stalls when trying to delete the resource's subnet. Deleted VCN resources are irretrievable. For more information, see [Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion). 
If any subnet still contains resources, or if you don't have permission to delete a particular Networking resource, the "Delete All" process stops and returns an error message that includes the OCIDs of the blocking resources and subnets, which link to the details page for that resource. In some cases, you might need to contact your tenancy administrator to help you delete any remaining resources if you don't have the needed permissions. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to delete. You might need to change the compartment to find the VCN that you want.
    3. Click **Delete**.
In the **Delete Virtual Cloud Network** dialog box, select **Search compartments for resources associated with this VCN**. 
When you select this option, the process scans for active resources in the VCN. If the process finds any active resources (subnets and route tables, for example) it deletes them if possible, then deletes the VCN. If the process finds a VNIC on a compute instance, a load balancer, a database system, or a mount target, you must manually delete those resources and then restart the process. 
We recommend selecting this option unless you're certain the VCN and its subnets are already empty. If you select this option, you can also choose which compartments to search: 
       * **All (number) compartments** : This option searches all compartments in the same region as this VCN for resources associated with the VCN. 
       * **Specific compartments** : This option lets you choose specific compartments and searches only the chosen compartments for resources associated with the VCN.
Searching more compartments takes more time, but is more thorough and has a smaller chance of failure.
    4. Click **Scan**.
The scan begins. Progress is displayed in the completion bar when the process identifies associated resources. The scan lists associated VCN resource types like subnets, DRG attachments, internet or NAT gateways, and so on. 
    5. Click **Delete All** to delete associated resources in the order listed. 
If you don't have the needed permissions to delete an associated resource or an error occurs, the deletion process stops. Deleted VCN resources are irretrievable. Resolve the error and restart the process to delete the VCN. 
If a subnet still contains compute instances, load balancers, and so on, deleting the subnet fails. The resulting error message displays the OCID of the subnet and the blocking item in that subnet. Click on the OCID to go to the details page for that item and either delete it or move it to a subnet in a different VCN.
    6. Click **Close** when the deletion of the VCN and all associated resources finishes. 
If the VCN is empty, its state changes to TERMINATING and then TERMINATED temporarily until the VCN is completely removed. Once a deleted VCN is completely removed it no longer appears in the list of VCNs in that compartment.
  * Use the [network vcn delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/delete.html) command and required parameters to delete a VCN: 
Command
CopyTry It
```
oci network vcn delete --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/DeleteVcn) operation to delete a VCN.
Be aware this deletes only the VCN and not its related resources. If there are any resources in the VCN, the deletion attempt will not succeed. For more information, see [Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion). The Console offers a "Delete All" process that makes it easy to delete the VCN and its related resources. 


Was this article helpful?
YesNo

