Updated 2024-08-06
# Viewing Public IP Addresses
On Compute Cloud@Customer, you can use the Compute Cloud@Customer Console, CLI, and API to view the IP addresses assigned to instances.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-public-ip-addresses.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-public-ip-addresses.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-public-ip-addresses.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to view the private IP address.
    3. Click the name of the instance.
The instance details page is displayed.
    4. View networking information or VNIC information:
       * Click the **Networking** tab. The primary private IP address and any attached public IP address are shown in the Instance Access column.
       * Under **Resources** , click **Attached VNICs**. Click the name of the VNIC for which you want to view IP addresses.
On the VNIC details page, under **Resources** , click **IP Addresses**. The primary private IP address and any secondary private IP addresses, and any attached public IP addresses, are shown in the table.
  * Use the [oci network public-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/list.html) command and required parameters to list the PublicIp objects in the specified compartment.
Copy
```
oci network public-ip list [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListPublicIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/ListPublicIps) operation to list the PublicIp objects in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

