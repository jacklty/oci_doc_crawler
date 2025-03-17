Updated 2025-01-15
# Listing Security Lists
List the security lists in the specified VCN and compartment. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/listing-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/listing-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/listing-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. The security lists in this VCN are listed in a table below the VCN details.
  * Use the [network security-list list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/list.html) command and parameters to list the security lists in the specified VCN and compartment:
Command
CopyTry It
```
oci network security-list list --compartment-id compartment-ocid --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListSecurityLists](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/ListSecurityLists) operation to Lists the security lists in a specified VCN and compartment.


Was this article helpful?
YesNo

