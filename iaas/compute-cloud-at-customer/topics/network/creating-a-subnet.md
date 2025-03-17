Updated 2024-08-06
# Creating a Subnet
On Compute Cloud@Customer, a subnet is a subdivision of a VCN. For each VCN, you create one or more subnets.
VCNs can be divided into subnets. Although it's possible to have an enormous VCN with a thousand IP addresses, it often makes sense from a performance and fault isolation standpoint to create multiple subnets within a VCN. The subnets can still communicate if configured properly.
IP subnet calculation can be a difficult task, especially when figuring out which IP addresses in the range are reserved. The wide range of allowable CIDR block addresses complicates the issue. Free subnet calculation tools available online can help, such as <https://www.calculator.net/ip-subnet-calculator.html>.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN in which you want to create a new subnet. 
The VCN details page is displayed.
    4. In the **Resources** section, click **Subnets**.
    5. Click **Create Subnet**.
    6. Enter the following information:
       * **Name:** Enter a descriptive name for the subnet.
       * **Create in Compartment:** Select the compartment where you want to create this subnet.
       * **CIDR Block:** Specify which CIDR range can be used within the subnet. 
**Important** The CIDR block range is an important subnet parameter. The range must be within the VCN CIDR block and must not overlap with other subnet CIDR block ranges. These IP addresses can't be shared.
       * **Route Table (Optional):** Select the route table to associate with this subnet. You might need to change the compartment selection. If you do not select a route table, the VCN default route table is used.
       * **Private or Public Subnet:** If you select Private Subnet, instances in this subnet are not allowed to obtain a public IP address.
       * **DNS Hostnames (Optional):** Check this box to assign a DNS hostname when you launch an instance in this subnet. If you check the box, enter a DNS label that's unique across the system. 
       * **DHCP Options (Optional):** Select the set of DHCP options to associate with the subnet. You might need to change the compartment selection. If you do not select a set of options, the VCN default set is used.
       * **Security Lists (Optional):** If you want a security list for this subnet, click +Add Security List. Select a security list to associate with the subnet. You might need to change the compartment selection. If you want another security list, click +Add Security List and select another security list. If you don't select a security list, the VCN default security list is used.
    7. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    8. Click **Create Subnet**. 
The details page of the new subnet is displayed.
  * Use the [oci network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html) command and required parameters to create a subnet in a specified VCN.
Copy
```
oci network subnet create --compartment-id compartment_OCID --vcn-id vcn_OCID --cidr-block cidr_block --dns-label dns_label --display-name display_name [OPTIONS]
```

**Important** The CIDR block range is an important subnet parameter. The range must be within the VCN CIDR block and must not overlap with other subnet CIDR block ranges. These IP addresses can't be shared.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet) operation to create a subnet in a specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

