Updated 2023-05-30
# Listing Resolver Endpoints
You can view a list of resolver endpoints.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm)


  *     1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. From the **Private Resolver Details** screen, click **Endpoints** in the left-hand navigation.
Endpoints in the resolver are listed in tabular form.
  * Use the [resolver-endpoint list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/list.html) command and required parameters to list resolver endpoints:
Command
CopyTry It
```
oci dns resolver-endpoint list --resolver-id resolver_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListResolverEndpoints](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/ListResolverEndpoints) operation to list resolver endpoints.


Was this article helpful?
YesNo

