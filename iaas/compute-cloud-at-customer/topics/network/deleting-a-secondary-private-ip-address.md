Updated 2024-08-06
# Deleting a Secondary Private IP Address
On Compute Cloud@Customer, you can delete a secondary IP address. You can't delete a VNIC primary private IP address.
On successful delete, the private IP address is returned to the pool of available addresses in the subnet. Any attached public IP address become available for assignment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-private-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-private-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-private-ip-address.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to delete a secondary private IP address. 
    3. Click the name of the instance.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
    5. Click the name of the attached VNIC for which you want to delete a secondary private IP address.
    6. On the VNIC details page, under **Resources** , click **IP Addresses**.
    7. For the secondary private IP address that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) and click **Delete**.
Confirm the deletion.
    8. Log onto the instance and delete the configuration for the IP address from the instance OS.
Undo the configuration you did when you added the IP address. See [Configuring the Instance OS for a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-vnic.htm#configuring-the-instance-os-for-a-secondary-vnic "On Compute Cloud@Customer, after you create a secondary VNIC, log in to the instance OS and configure the OS to use the new VNIC.").
  * Use the [network vnic unassign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/unassign-private-ip.html) command and required parameters to unassign a secondary private IP address from a VNIC.
Copy
```
oci network vnic unassign-private-ip [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Refer to the [PrivateIp Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp) for information about unassigning a secondary private IP address from a VNIC.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

