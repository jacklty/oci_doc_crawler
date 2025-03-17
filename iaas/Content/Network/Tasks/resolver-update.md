Updated 2023-05-30
# Editing a Resolver
You can update information like the resolver name.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm)


  * When using the console, you can only edit the resolver name.
    1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. Click **Edit**.
    3. Update the resolver **Name**.
    4. Click **Save changes**.
  * Use the [resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html) command and required parameters to edit a resolver:
Command
CopyTry It
```
oci dns resolver update --resolver-id resolver_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver) operation to edit a resolver.


Was this article helpful?
YesNo

