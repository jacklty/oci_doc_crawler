Updated 2024-04-12
# Removing a Private View From a Resolver
You can remove a non-default private view from a resolver.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm)


  *     1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. From the **Private Resolver Details** screen, select the checkbox next to the private view you want to remove from the resolver. **Remove** turns red, and can now be clicked. You can select other private views if necessary. 
    3. Click **Remove**.
**Note** You can also remove a private view from the **Manage Private Views** screen by clicking the red button labeled **-** and then clicking **Save Changes**.
  * Use the [resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html) command and required parameters to remove a private view from a resolver. In the `attached-views` parameter, _do not include_ the view **OCID** value for the view you want to remove.
Command
CopyTry It
```
oci dns resolver update --resolver-id resolver_OCID --attached-views '[{"view-id":""}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver) operation to remove a private view from a resolver.


Was this article helpful?
YesNo

