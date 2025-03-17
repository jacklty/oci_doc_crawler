Updated 2024-01-18
# Deleting a Subnet
On Compute Cloud@Customer, to delete a subnet, it must contain no resources (instances, VNICs).
For more information about deleting VCNs and Subnets, see [Subnet or VCN Deletion](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion)
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-subnet.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN and subnet.
    3. Click the name of the VCN that contains the subnet you want to delete.
    4. Under **Resources** , click **Subnets**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), click **Delete**.
    6. Confirm the deletion.
  * Use the [oci network subnet delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/delete.html) command and required parameters to delete a subnet.
Copy
```
oci network subnet delete --subnet-id subnet_OCID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/DeleteSubnet) operation to delete a subnet.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

