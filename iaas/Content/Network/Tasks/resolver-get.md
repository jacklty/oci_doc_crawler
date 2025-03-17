Updated 2023-05-30
# Getting a Resolver's Details
View details about a private resolver in a VCN.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-get.htm)


  * From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
The Details page contains information about the resolver, both general information and links to its resources. Some items in the page are read-only, while other items allow you to edit and update the resolver configuration. See [Adding a Private View to a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm#top "You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN.") and [Editing a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm#top "You can update information like the resolver name.").
  * Use the [resolver get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/get.html) command and required parameters to view details about a resolver:
Command
CopyTry It
```
oci dns resolver get --resolver-id resolver_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/GetResolver) operation to view details about a resolver.


Was this article helpful?
YesNo

