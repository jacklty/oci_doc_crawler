Updated 2023-05-30
# Listing Resolvers
View a list of resolvers in a compartment.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-list.htm)


  * This task is not available in the Console.
  * Use the [resolver list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/list.html) command and required parameters to see all resolvers in a compartment:
Command
CopyTry It
```
oci dns resolver list --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListResolvers](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ListResolvers) operation to view all resolvers in a compartment.


Was this article helpful?
YesNo

