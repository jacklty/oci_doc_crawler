Updated 2024-08-06
# Updating a Secondary Private IP Address
On Compute Cloud@Customer, you can update the hostname and change the IP address of a secondary private IP address object. You can't update a VNIC primary private IP address.
To change the hostname, use the Compute Cloud@Customer Console, CLI, or API as described in this section.
To change the IP address, delete the secondary IP address. Then create a new secondary IP address. See:
  * [Deleting a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-private-ip-address.htm#deleting-a-secondary-private-ip-address "On Compute Cloud@Customer, you can delete a secondary IP address. You can't delete a VNIC primary private IP address.")
  * [Assigning a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assigning-a-secondary-private-ip-address.htm#assigning-a-secondary-private-ip-address "On Compute Cloud@Customer, when you create an instance, the instance automatically gets a VNIC, and the VNIC automatically gets a primary private IP address. You can add secondary private IP addresses to a VNIC. A VNIC can have up to 33 private IP addresses: one primary private IP address, and up to 32 secondary private IP addresses.")


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-secondary-private-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-secondary-private-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-secondary-private-ip-address.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance that has the secondary private IP address object that you want to update.
    3. Click the name of the instance.
The instance details page is displayed.
    4. On the instance details page, under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
    5. Click the name of the attached VNIC that has the secondary private IP address object that you want to update.
    6. On the VNIC details page, under **Resources** , click **IP Addresses**.
    7. For the secondary private IP address object that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    8. In the **Attach Private IP** dialog box, update the host name.
    9. Click **Attach IP Address**.
  * Use the [oci network private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html) command and required parameters to change the display name or the hostname for a secondary private IP.
Copy
```
oci network private-ip update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp) operation to change the display name or the hostname for a secondary private IP.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

