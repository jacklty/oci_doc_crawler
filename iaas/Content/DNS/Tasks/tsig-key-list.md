Updated 2025-03-10
# Listing TSIG Keys
View a list of all TSIG keys in a compartment
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **TSIG keys**.
    2. Under **List scope** , select the compartment that contains the key.
  * Use the [tsig list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/list.html) command and required parameters to list all TSIG keys in a compartment:
Command
CopyTry It
```
oci dns tsig-key list --compartment-id compartment_id ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListTsigKeys](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/ListTsigKeys) operation to see all TSIG keys in a compartment.


Was this article helpful?
YesNo

