Updated 2025-01-22
# Updating ASN
Associate your BYOIP CIDRs (IPv4/IPv6) with your own ASN instead of the OCI ASN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm)


  *     1. Open the navigation menu and click **Networking**. Under **IP management** , click **BYOIP**.
    2. On the **BYOIP** page, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right of the BYOIP IPv4 CIDR block or IPv6 prefix that you want to associate your ASN with and click **Update origin ASN**. 
    3. On the **Update origin ASN** page, click **Select your ASN**.
    4. Select the compartment where your ASN is imported to.
    5. Select your ASN from the list.
    6. Click **Update origin ASN**. 
View the work request to see the status.
  * Use the `network byoip-range set-origin-asn` command and required parameters to associate your BYOIP CIDRs (IPv4/IPv6) with your own ASN instead of the OCI ASN:
Command
CopyTry It
```
oci network byoasn set-origin-asn
```

Use the `network byoip-range set-origin-asn-to-oracle` command and required parameters to associate your BYOIP CIDRs (IPv4/IPv6) with the OCI ASN:
Command
CopyTry It
```
oci network byoasn set-origin-asn-to-oracle ASN --compartment-id Compartment ID OCID --display-name ASN Display name
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/UpdateByoasn) operation to associate your BYOIP CIDRs (IPv4/IPv6) with your own ASN instead of the OCI ASN.
Run the [ChangeByoasnCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/ChangeByoasnCompartment) operation to change the compartment of your ASN.


Was this article helpful?
YesNo

