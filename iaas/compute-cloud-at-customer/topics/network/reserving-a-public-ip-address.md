Updated 2024-01-18
# Reserving a Public IP Address
On Compute Cloud@Customer, you can reserve a public IP address that's available to assign to a private IP address object at a later time.
There are two types of public IPs:
  * **Ephemeral:** Think of it as temporary and existing for the lifetime of the instance.
  * **Reserved:** Think of it as persistent and existing beyond the lifetime of the instance it's assigned to. You can unassign it and then reassign it to another instance whenever you like.


For more information, see [Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/reserving-a-public-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/reserving-a-public-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/reserving-a-public-ip-address.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Reserved Public IPs**.
    2. Click **Reserve Public IP Address**.
    3. Enter the following information:
       * **Reserved Public IP Address Name:** (Required) Enter a name for the reserved address. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment in which to reserve the address.
       * **IP Address Source:** Select the source from which to reserve the address.
    4. Click **Reserve Public IP**.
The new reserved public IP is created and displayed on the page. You can assign it to an instance if you like. See [Assigning a Reserved Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-a-reserved-public-ip-address-to-an-instance.htm#assingning-a-reserved-public-ip-address-to-an-instance "On Compute Cloud@Customer, you can assign a public IP address to an instance, you assign the public IP address object to a private IP address object.").
  * Use the [oci network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html) command with the `--lifetime` option and required parameters to define how the public IP handled when it is deleted.
Copy
```
oci network public-ip create --lifetime EPHEMERAL|RESERVED [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp) operation to define how the public IP handled when it is deleted.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

