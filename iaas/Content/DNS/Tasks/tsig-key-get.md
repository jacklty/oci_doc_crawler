Updated 2025-03-10
# Getting a TSIG Key's Details
View details for a specific TSIG key.
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **TSIG keys**.
    2. Under **List scope** , select the compartment that contains the key.
    3. Select the name of the TSIG key to open its details page.
The details page contains information about the TSIG key, both general information and links to its resources. Some items in the page are read-only, and other items are editable. See [Editing a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm#top "Update the information for a TSIG key.").
  * Use the [tsig get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/get.html) command and required parameters to see details for a TSIG key:
Command
CopyTry It
```
oci dns tsig-key get --tsig-key-id tsig_key_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/GetTsigKey) operation to see details about a TSIG key.


Was this article helpful?
YesNo

