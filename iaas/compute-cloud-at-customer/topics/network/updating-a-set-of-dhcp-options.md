Updated 2024-04-02
# Updating a Set of DHCP Options
On Compute Cloud@Customer, you can change DHCP options.
To update the DHCP options for the instances in a subnet, do one of the following:
  * Update the DHCP Options object that's assigned to that subnet as described in this section.
  * Update the subnet to assign a different DHCP Options object as described in [Editing a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-subnet.htm#editing-a-subnet "On Compute Cloud@Customer, you can edit subnets. You can change the subnet name, the route tables and security lists used by the subnet, and DHCP options.").


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-set-of-dhcp-options.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-set-of-dhcp-options.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-set-of-dhcp-options.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN.
    3. Click the name of the VCN for the DHCP options that you want to edit. 
    4. Under **Resources** , click **DHCP Options**.
The list of DHCP options sets is displayed.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the set of options you want to change, then click **Edit**.
    6. Change options.
    7. Click **Save Changes**.
  * Use the [oci network dhcp-options update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/dhcp-options/update.html) command and required parameters to update the specified set of DHCP options. You can update the display name or the options themselves.
**Important** The options object you provide replaces the entire existing set of options.
Copy
```
oci network dhcp-options update --dhcp-id <dhcp_OCID> <options_to_update> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateDhcpOptoins](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/UpdateDhcpOptions) operation to update the specified set of DHCP options. You can update the display name or the options themselves. Avoid entering confidential information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

