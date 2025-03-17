Updated 2024-08-06
# Viewing Private IP Addresses
On Compute Cloud@Customer, you can see the private IP addresses for instances.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-private-ip-addresses.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-private-ip-addresses.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-private-ip-addresses.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to view IP address information.
    3. Click the name of the instance.
The instance details page is displayed.
    4. View networking information or VNIC information.
       * Click the **Networking** tab. The primary private IP address and any attached public IP address are shown in the Instance Access column.
       * Under **Resources** , click **Attached VNICs**. Click the name of the VNIC for which you want to view IP addresses.
On the VNIC details page, Under **Resources** , click **IP Addresses**. The primary private IP address and any secondary private IP addresses, and any attached public IP addresses, are shown in the table.
  * Use the [oci network private-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/list.html) command and required parameters to list private IP address objects.
Copy
```
oci network private-ip list [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListPrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) operation to list private IP address objects.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

