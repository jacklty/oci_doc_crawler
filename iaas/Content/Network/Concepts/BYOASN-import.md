Updated 2025-02-21
# Importing ASN
Import your ASN to OCI and use your existing ASN within the OCI environment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm)


  *     1. Confirm you're viewing the region and compartment you're interested in.
    2. Open the navigation menu and click **Networking**. Under **IP management** , click **BYOASN**.
    3. Click **Import your ASN**.
    4. On the **Import your ASN** page, enter a name for the ASN, select the compartment, and enter the ASN you intend to bring to your tenancy. Avoid entering confidential information.
    5. Click **Import your ASN**. The details page for that ASN import request appears.
    6. In the **Next Steps** section, make a copy of the validation token.
    7. Create a Route Origin Authorization (ROA) object that authorizes Oracle to advertise the BYOIP CIDR block. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the US Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). Set an expiry date at least 6 months in the future. Follow the instructions appropriate for your RIR:
       * **ARIN:**[ROA Requests](https://www.arin.net/resources/manage/rpki/roa_request/)
       * **RIPE NCC:** [Managing ROAs](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/resource-certification-roa-management)
       * **APNIC:** [Route/ROA management](https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf)
**Note**
If you don't create an ROA, Oracle can't advertise the BYOIP IPv4 CIDR block or IPv6 prefix. Without being able to advertise the routes, there may be little point in importing them.
**Note**
The BYOASN workflow takes up to 10 business days to complete, during which Oracle validates your ASN and IP Prefix combinations with service providers. To speed up the process, ensure to let your Oracle Account team know which IP prefix you plan to link to the ASN.
    8. Add the validation token to the RIR account information associated with your address range. Each RIR uses a slightly different method:
       * **ARIN:** Add the token string in the "Public Comments" section associated with your address range.
       * **RIPE NCC:** Add the token string as a new "descr" field associated with your address range.
       * **APNIC:** Add the token string to the "remarks" field for your address range by emailing it to helpdesk@apnic.net. The email must be sent from the APNIC authorized contact account for the IP address range.
**Note**
The validation token must be associated with the address range information. Don't add it to the information for the organization that owns the address range.
    9. Wait until the token registration is complete before you click the **Finish import** button.
    10. Return to the details page for the BYOASN request and click **Finish import**. A confirmation screen appears.
    11. Click **Finish import** , confirming that you would like to validate the BYOASN request. View the work requests to see the status.
  * Use the `network byoasn create` command and required parameters to import an ASN within the OCI environment:
Command
CopyTry It
```
oci network byoasn create --asn ASN --compartment-id Compartment ID OCID --display-name ASN Display name
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/CreateByoasn) operation to import an ASN.
Run the [ValidateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/ValidateByoasn) operation to validate the imported ASN.


Was this article helpful?
YesNo

