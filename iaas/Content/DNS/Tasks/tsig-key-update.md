Updated 2025-01-10
# Editing a TSIG Key
Update the information for a TSIG key.
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm)


  * This task isn't available in the Console.
  * Use the [tsig update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/update.html) command and required parameters to edit details for a TSIG key:
Command
CopyTry It
```
oci dns tsig-key update --tsig-key-id tsig_key_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/UpdateTsigKey) operation to update details about a TSIG key.


Was this article helpful?
YesNo

