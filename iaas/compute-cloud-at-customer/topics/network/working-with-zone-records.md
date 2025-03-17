Updated 2024-10-07
# Zone Records
On Compute Cloud@Customer, 
Creating a DNS zone is only the beginning of working with DNS. The zone is essentially empty when created, except for a basic Start of Authority (SOA) and Name Server (NS) record The SOA record provides a kind of history of this DNS zone and holds information such as when it was last updated and things like that. The NS record contains the fully-qualified name of the DNS server for the zone. The NS record is very important and therefore has a high TTL, usually 24 hours (86400 seconds).
To make the name server truly useful, the zone must be rounded out and filled with the DNS records that form the basis of responses to the kinds of queries that clients make. These queries include IP addresses for parts of the domain namespace, email server details, and so on.
## Creating a Zone Record 🔗 
On Compute Cloud@Customer, you can create a DNS zone record.
The RDATA field is where the content of the zone record is entered. The format of the information varies according to the type of record you are creating. However, the data must be in one of the formats that DNS understands. For example, an A-type zone record RDATA is an IP address, and an MX record contains information on how to route email. Because of the authoritative nature of the zone records within a zone, RDATA is not editable. If DNS information in a zone changes, then the old record must be deleted and a new record created. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Zones**. 
A list of previously configured zones in compartments is displayed.
    2. At the top of the page, select the compartment that contains the designated DNS zone.
    3. Click the name of the zone. 
The information screen contains general zone information such as type and compartment, OCID (which you can show in full or copy to the clipboard), and the date and time that the zone was created. The zone records that exist are also displayed, and initially only SOA and NS records.
    4. Enter the required zone record information:
       * **Zone Record:** Select the type of zone record you're creating from the drop-down list. 
         * **A - IPv4 Address** : A host record, which is used to point a hostname to an IPv4 address. This is the most basic DNS record type.
         * You can add many other types of zone records: any types in the drop down list. 
       * **Domain (Optional)** : Type the name of the zone subdomain if used (this value is already filled in based on the zone itself: the initial dot (".") is used for adding the zone subdomain).
       * **TTL** : Check this box to set your own value for the TTL of that particular record type. If you don't check this box, the default TTL value for that record type is used (for example, 300 for SOA, 86400 for NS). The valid range is from 1 to 129540 seconds (from 1 second to about a day and a half). 
       * **Edit RDATA** : Check this box if you want to edit the RDATA information, such as the IP address or Target established by the zone record type. This box is only displayed for some zone record types.
       * **(RDATA)** : This unlabeled field varies based on the type of zone record created. For example, you enter the 32-bit IP address that corresponds to the A-type DNS record, or Flags for a DNSKEY zone record, if that's what you are creating. 
         * **A - IPv4 Address** : If you're creating an A type zone record, then the data is a formatted IPv4 address. This is the most basic DNS record, but there are many others.
         * The RDATA field reflects the correct information for the type of zone record selected.
    5. Click **Create Record**.
The zone record is now added to the zone. If you click the optional box to **Add another record** , then the screen stays at the **Create DNS Zone Record** state to make record entry more efficient.
  * Use the [oci dns record zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/zone/update.html) command and required parameters to replace records in the specified zone with the records specified in the request body.
Copy
```
oci dns record zone update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateZoneRecords](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/UpdateZoneRecords) operation to replace records in the specified zone with the records specified in the request body.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


## Editing a Zone Record 🔗 
On Compute Cloud@Customer, you can update a DNS zone record.
There is no "`edit record`" command. You can update a group of records, and if one of the records in the list is the same except for the `rdata` for example, in effect you have updated the record. 
## Deleting a Zone Record 🔗 
On Compute Cloud@Customer, you can delete many, but not all DNS zone records. The initial SOA and NS records created by default when the zone is created can't be deleted.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-zone-records.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Zones**. 
A list of previously configured zones in compartments appears. 
    2. At the top of the page, select the compartment that contains the DNS zone with the record you want to delete.
    3. Click the name of the zone. 
The information screen contains general zone information such as type and compartment, OCID (which you can show in full or copy to the clipboard), and the date and time that the zone was created. The zone records that exist are also displayed.
    4. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the zone record that you're deleting. 
    5. Click **Delete**. 
  * Use the [oci dns record rrset delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/delete.html) command and required parameters to delete all records in the specified RRSet.
Copy
```
oci dns record rrset delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteRRSet](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/DeleteRRSet) command and required parameters to delete all records in the specified RRSet.
Copy
```
SYNTX [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).


Was this article helpful?
YesNo

