Updated 2024-08-06
# Assigning a Secondary Private IP Address
On Compute Cloud@Customer, when you create an instance, the instance automatically gets a VNIC, and the VNIC automatically gets a primary private IP address. You can add secondary private IP addresses to a VNIC. A VNIC can have up to 33 private IP addresses: one primary private IP address, and up to 32 secondary private IP addresses.
Creating a VNIC in the same subnet as another VNIC for the same instance can introduce asymmetric routing as described in [Configuring VNICs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vnics.htm#configuring-vnics-and-ip-adresses "On Compute Cloud@Customer, the compute nodes have physical network interface cards \(NICs\). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network."). Instead, you can create a secondary private IP address for the existing VNIC that's in the subnet that you want.
See information about secondary private IP addresses, including use cases, in [Managing Private IP Addresses](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-private-ip-addresses.htm#managing-private-ip-addresses "On Compute Cloud@Customer, a private IP address enables communication with resources on the VCN.").
After you perform the following procedure to assign a secondary private IP address, log onto the instance to configure the instance OS to use the new IP address. See [Configuring the Instance OS for a Secondary IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-ip-address.htm#configuring-the-instance-os-for-a-secondary-ip-address "On Compute Cloud@Customer, after you create a secondary private IP address on a VNIC, sign in to the instance to configure the instance OS to use the new IP address.").
Avoid entering confidential information in names and tags.
## Moving a Secondary IP Address 🔗 
In addition to adding a secondary private IP address, you can use this procedure to reassign (move) a currently assigned secondary private IP address to a different VNIC. Because the VNIC must be in the same subnet as the VNIC where the secondary private IP address is currently assigned, the new VNIC probably is attached to a different instance; as previously mentioned, having two VNICs in the same subnet in the same instance can introduce asymmetric routing.
To move a secondary private IP address, see the Unassign if assigned or `--unassign-if-already-assigned` options in the following procedures.
You can't move a VNIC primary private IP address.
If a public IP address object is assigned to a secondary private IP address object, and you move that secondary private IP address object to another VNIC, the public IP address object moves with it.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assigning-a-secondary-private-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assigning-a-secondary-private-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assigning-a-secondary-private-ip-address.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to add a secondary private IP address.
    3. Click the name of the instance to which you want to add a secondary private IP address.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
    5. Click the name of the attached VNIC to which you want to add a secondary private IP address.
    6. On the VNIC details page, under **Resources** , click **IP Addresses**.
    7. Click **Assign Secondary Private IP Address**.
    8. In the **Attach Private IP** dialog box, all input fields are optional.
       * **IP Address:** If you don't enter an address, an IP address from the subnet CIDR is automatically assigned.
If you enter an address, the IP address must be within the CIDR block for the subnet. You can enter a secondary private IP address that's already assigned to another VNIC in the subnet. You can't enter a primary private IP address.
If you enter an IP address that's already assigned, see the following option.
       * **Unassign if assigned:** In the previous option, if you entered a secondary private IP address that's already assigned, select this item to _move_ that private IP address. The address will be unassigned from the VNIC where it's currently assigned and reassigned to this VNIC.
If you entered an IP address that's already assigned and you don't select this item, this secondary private IP assignment operation fails.
       * **Hostname:** Enter the hostname to be used for DNS within the cloud network. This option is available only if the VCN and subnet both have DNS labels.
    9. Click **Attach IP Address**.
The new secondary private IP address is shown in the table.
    10. Configure the new secondary private IP address in the instance. See [Configuring the Instance OS for a Secondary IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-ip-address.htm#configuring-the-instance-os-for-a-secondary-ip-address "On Compute Cloud@Customer, after you create a secondary private IP address on a VNIC, sign in to the instance to configure the instance OS to use the new IP address.").
  * Use the [network vnic assign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/assign-private-ip.html) command and required parameters to assign a secondary private IP address to the specified VNIC. The secondary private IP must be in the same subnet as the VNIC. 
Copy
```
oci network vnic assign-private-ip --vnic-id <vnic_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [PrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp) operation to assign a secondary private IP address to the specified VNIC. The secondary private IP must be in the same subnet as the VNIC.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

