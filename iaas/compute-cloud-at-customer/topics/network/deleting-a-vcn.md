Updated 2024-01-18
# Deleting a VCN
On Compute Cloud@Customer, a VCN can only be deleted if it's empty. Before deleted a VCN, ensure that all subnets, route tables, gateways, and other resources have been deleted. 
For more information about deleting VCNs and Subnets, see [Subnet or VCN Deletion](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion)
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-vcn.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN.
    3. Click the name of the VCN that you want to delete. 
The VCN details page is displayed. 
    4. Under **Resources** , ensure that the VCN doesn't have any resources.
If all the resources such as Subnets, Route Tables, and so on include a zero in parenthesis, then the VCN doesn't have any resources.
If a resource exists, you must delete the resource before you can delete the VCN.
    5. Click **Delete**. 
    6. Confirm the deletion.
  * Use the [oci network vcn delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/delete.html) command and required parameters to delete a VCN.
Copy
```
oci network vcn delete --vcn-id vcn_OCID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteVCN](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/DeleteVcn) operation to delete a VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

