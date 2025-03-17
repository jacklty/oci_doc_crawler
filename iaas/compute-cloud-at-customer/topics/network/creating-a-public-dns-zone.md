Updated 2024-08-06
# Creating a Public DNS Zone
On Compute Cloud@Customer, DNS zones are created in a compartment to associate IP addresses with portions of the DNS namespace. Zones are created in a compartment using the DNS service.
After a public DNS zone is created, you can add resource tags. You can also edit the `externalMasters` field of a `SECONDARY` zone.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-public-dns-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-public-dns-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-public-dns-zone.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Zones**. 
    2. Click **Create Zone**.
    3. Enter the required zone information:
       * **Zone Name:** Provide a name or description for the DNS zone.
       * **Compartment:** Select the compartment in which to create the DNS zone.
       * **Zone Type:** Choose the type of DNS zone you are creating.
         * **Primary** : A primary DNS zone is the original authoritative DNS zone of a portion of the DNS namespace. When a DNS server hosts a primary zone, that DNS server is the Authoritative DNS Server and is considered the primary source of information in that zone.
         * **Secondary** : A secondary DNS zone is a read-only copy of a primary DNS zone or another secondary DNS zone. A secondary DNS zone is kept on a Secondary DNS Server and reduces the load on the primary DNS zone and eliminated a single point of failure risk to name resolution inside the zone.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Zone**.
The zone is now ready for the addition of zone records or for the configuration of TSIG Keys or Steering Policies. See [Zone Records](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm#working-with-zone-records "On Compute Cloud@Customer,"), [Transaction Signature (TSIG) Keys](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm#working-with-transaction-signature-keys "On Compute Cloud@Customer, you can create, add, and delete TSIG keys."), and [Managing Traffic with Steering Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-traffic-with-steering-policies.htm#managing-traffic-with-steering-policies "On Compute Cloud@Customer, offers two types of traffic steering policies based on load balancing and some value of the IP address prefix.").
  * Use the [oci dns zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a DNS zone.
Copy
```
oci dns zone create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a DNS zone.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

