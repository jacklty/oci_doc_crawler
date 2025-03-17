Updated 2024-04-02
# Viewing VCN DHCP Option Sets
On Compute Cloud@Customer, every VCN has a default set of DHCP options. If you create more sets, then you can choose which set to assign to a subnet.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-vcn-s-dhcp-option-sets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-vcn-s-dhcp-option-sets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-vcn-s-dhcp-option-sets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN.
    3. Click the name of the VCN for which you want to list DHCP Options sets.
    4. Under **Resources** , click **DHCP Options**. 
The list of DHCP options sets is displayed.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the a particular DHCP set, and click **Edit**. 
The options are displayed.
  * Use the [oci network dhcp-options list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/dhcp-options/list.html) command and required parameters to list DHCP option sets.
Copy
```
oci network dhcp-options list --compartment-id ocid1.compartment.unique_ID --vcn-id ocid1.vcn.unique_ID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/ListDhcpOptions) operation to list DHCP option sets.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

