Updated 2024-08-06
# Creating a Network Security Group
On Compute Cloud@Customer, you can create Network Security Groups (NSGs).
**General Process for Working with NSGs**
  1. Create an NSG as described in this section.
  2. Add security rules to the NSG. See [Managing Network Security Group Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-network-security-group-rules.htm#managing-security-group-rules "On Compute Cloud@Customer, you can add, update, and remove NSG rules.").
  3. Add parent resources (or more specifically, VNICs) to the NSG.
You can do this when you create the parent resource, or you can update the parent resource and add it to one or more NSGs. 
When you create a Compute instance and add it to an NSG, the instance's primary VNIC is added to the NSG. Separately, you can create secondary VNICs and optionally add them to NSGs.


Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-network-security-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-network-security-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-network-security-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to create an NSG. 
The VCN details page is displayed.
    4. Under **Resources** , click **Network Security Groups**.
    5. Click **Create Network Security Group**. 
    6. In the **Create Network Security Group** dialog box, enter the following information:
       * **Name:** Enter a descriptive name for the NSG. The name doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment where you want to create the NSG.
    7. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    8. Click **Create Network Security Group**.
The details page for the new NSG is displayed. You can create security rules and select VNICs to add to the group now, or you can do these tasks later. See [Configuring VCN Rules and Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vcn-rules-and-options.htm#configuring-vcn-rules-and-options "On Compute Cloud@Customer, VCNs and their subnets have various rules and options associated with them. The main categories are the use of DHCP, route tables, and security. If you do not configure these rules and options explicitly, the system uses default values.") and [Configuring VNICs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vnics.htm#configuring-vnics-and-ip-adresses "On Compute Cloud@Customer, the compute nodes have physical network interface cards \(NICs\). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network.").
  * Use the [oci network nsg create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/create.html) command and required parameters to create a new network security group for the specified VCN.
Copy
```
oci network nsg create --compartment-id <compartment_OCID> --vcn-id <vcn_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/CreateNetworkSecurityGroup) operation to create a new network security group for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

