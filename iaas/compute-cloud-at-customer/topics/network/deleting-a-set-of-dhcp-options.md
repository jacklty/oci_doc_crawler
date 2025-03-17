Updated 2024-04-02
# Deleting a Set of DHCP Options
On Compute Cloud@Customer, you can delete a set of DHCP options as long as the DHCP options are not assigned to any subnet.
To unassign the DHCP options set from a subnet, update the subnet to assign a different set of DHCP options. See [Editing a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-subnet.htm#editing-a-subnet "On Compute Cloud@Customer, you can edit subnets. You can change the subnet name, the route tables and security lists used by the subnet, and DHCP options."). You can't delete a VCN default set of DHCP options.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-set-of-dhcp-options.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-set-of-dhcp-options.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-set-of-dhcp-options.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN.
    3. Click the name of the VCN for which you want to delete a DHCP Options set.
    4. Under **Resources** , click **DHCP Options**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the set you want to delete, then click **Delete**.
    6. Confirm the deletion.
  * Use the [oci network dhcp-options delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/dhcp-options/delete.html) command and required parameters to delete the specified set of DHCP options, but only if it’s not associated with a subnet.
Copy
```
oci network dhcp-options delete --dhcp-id ocid1.dhcpoptions.unique_ID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/DeleteDhcpOptions) operation to delete the specified set of DHCP options, but only if it’s not associated with a subnet.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

