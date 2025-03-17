Updated 2024-04-02
# Viewing Network Security Groups
On Compute Cloud@Customer, NSGs are available for you to create and use.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-network-security-groups.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-network-security-groups.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-network-security-groups.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to view Network Security Groups. 
The VCN details page is displayed.
    4. Under **Resources** , click **Network Security Groups**. 
The list of NSGs is displayed.
    5. Click the name of the NSG to view its details, including security rules and attached VNICs.
  * Use the [oci network nsg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/list.html) command and required parameters to list either the network security groups in the specified compartment, or those associated with the specified VLAN. 
**Note** You must specify either a `vlanId` or a `compartmentId`, but not both. If you specify a `vlanId`, all other parameters are ignored.
Copy
```
oci network nsg list --compartment-id <compartment_OCID> | --VLAN-id <vlan_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListNetworkSecurityGroups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/ListNetworkSecurityGroups) operation to list either the network security groups in the specified compartment, or those associated with the specified VLAN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

