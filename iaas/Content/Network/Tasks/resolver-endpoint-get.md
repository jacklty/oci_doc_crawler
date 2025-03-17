Updated 2023-05-30
# Getting a Resolver Endpoint's Details
View details about a resolver endpoint.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-get.htm)


  *     1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. From the **Private Resolver Details** screen, click **Endpoints** in the left-hand navigation.
All resolver endpoints are listed in tabular form.
    3. Click the name of the endpoint you want to see details for.
The Details page contains information about the resolver endpoint, both general information and links to its resources. Some items in the page are read-only, while other items allow you to edit and update the endpoint configuration. See [Adding a Network Security Group (NSG) to a Resolver Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-add-nsg.htm#top "Add a network security group \(NSG\) to a resolver endpoint.").
  * Use the [resolver-endpoint get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/get.html) command and required parameters to get details about a resolver endpoint:
Command
CopyTry It
```
oci dns resolver-endpoint get --resolver-endpoint-id resolver-endpoint_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/GetResolverEndpoint) operation to view details about a resolver endpoint.


Was this article helpful?
YesNo

