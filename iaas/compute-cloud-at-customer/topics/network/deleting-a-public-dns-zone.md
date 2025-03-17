Updated 2024-01-18
# Deleting a Public DNS Zone
On Compute Cloud@Customer, you can delete a public DNS zone.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-dns-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-dns-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-dns-zone.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Zones**. 
    2. At the top of the page, select the compartment that contains the public DNS zone you want to delete.
    3. Click the zone name that you want to remove from the drop-down list of zones.
    4. Click **Delete**.
The DNS zone is removed from the list.
The DNS zone is deleted.
  * Use the [oci dns zone delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/delete.html) command and required parameters to delete the specified DNS zone.
Copy
```
oci dns zone delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/DeleteZone) operation to delete the specified DNS zone.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

