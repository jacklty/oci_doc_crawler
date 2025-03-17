Updated 2024-08-06
# Assigning an Ephemeral Public IP Address to an Instance
On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.
An ephemeral public IP address is created and assigned in the same step.
An ephemeral public IP address can only be assigned to a primary private IP address: The value of the `is-primary` property of the private IP address object must be `true`. Every VNIC has one primary private IP address.
For secondary private IP addresses (the value of the `is-primary` property of the private IP address object is `false`), assign reserved public IP addresses.
An ephemeral public IP address can't be unassigned and can't be moved to a different private IP address.
An ephemeral public IP address object is deleted in the following cases:
  * Its private IP address object is deleted.
  * Its VNIC is detached or deleted.
  * Its instance is deleted.


Avoid entering confidential information in names.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to assign a public IP address.
    3. Click the name of the instance.
The instance detail page is displayed.
    4. Under **Resources** , click **Attached VNICs**. 
    5. Click the name of the VNIC for which you want to assign a public IP address.
    6. On the VNIC details page, under **Resources** , click **IP Addresses**. The primary private IP address and any secondary private IP addresses, and as any attached public IP addresses, are shown in the table.
    7. If the primary private IP address doesn't already have a public IP address assigned, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the primary private IP address, and then click **Edit Public IP**.
    8. In the dialog box, click **Ephemeral Public IP**.
    9. (Optional) Give the ephemeral public IP address a name.
    10. Click **Reserve Public IP**.
You might need to refresh the page to see the new public IP address. 
The new public IP address is displayed in the **IP Addresses** table in **Resources** , in the **Primary IP Information** column for the VNIC, and in the **Instance Access** column of the **Networking** tab of the instance.
  * Use the [oci network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html) command and required parameters to create a public IP. Use the _lifetime_ property to specify whether it’s an ephemeral or reserved public IP.
Copy
```
oci network public-ip create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp) operation to create a public IP.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

