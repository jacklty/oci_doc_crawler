Updated 2025-03-10
# Deleting a TSIG Key
Delete a TSIG key.
**Note**
A TSIG key attached to a zone must be removed from the zone using DNS Zone Management. See [Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm#managing-zones "The Oracle Cloud Infrastructure DNS service lets you manage zones using the Console, CLI, or API.") for more information.
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **TSIG keys**.
    2. Under **List scope** , select the compartment that contains the key.
    3. Find the TSIG key in the list, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Delete**. 
    4. In the confirmation dialog box, select **Delete**.
  * Use the [tsig delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/delete.html) command and required parameters to delete a TSIG key:
Command
CopyTry It
```
oci dns tsig-key delete --tsig-key-id tsig_key_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/DeleteTsigKey) operation to delete a TSIG key.


Was this article helpful?
YesNo

