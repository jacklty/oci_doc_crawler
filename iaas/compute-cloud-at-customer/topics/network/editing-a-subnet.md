Updated 2024-08-06
# Editing a Subnet
On Compute Cloud@Customer, you can edit subnets. You can change the subnet name, the route tables and security lists used by the subnet, and DHCP options.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-subnet.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN and subnet.
    3. Click the name of the VCN that contains the subnet you want to edit. 
The VCN details page is displayed.
    4. Under **Resources** , click **Subnets**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Make the changes to the subnet. The following items can be changed:
       * **Name:** Change the name of the subnet.
       * **Route Table:** Select a different route table for this subnet. You might need to change the compartment selection.
       * **DHCP Options:** Select a different set of DHCP options for this subnet. You might need to change the compartment selection.
       * **Security Lists:** Select different or additional security lists for this subnet. You might need to change the compartment selection.
    7. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    8. Click **Save Changes**. 
The subnet properties are updated.
  * Use the [oci network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and required parameters to update a subnet.
Copy
```
oci network subnet update --subnet-id ocid1.subnet.unique_ID --dhcp-options-id ocid1.dhcpoptions.unique_ID --route-table-id ocid1.routetable.unique_ID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet) operation to update a subnet.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

