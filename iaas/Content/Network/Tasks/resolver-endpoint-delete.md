Updated 2023-05-30
# Deleting a Resolver Endpoint
Delete an enpoint from a resolver.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-delete.htm)


  *     1. From the **Private Resolver Details** screen, click the **Action** button to the right of the endpoint you want to delete, and then click **Delete**. 
    2. Confirm the deletion by clicking **Delete**. 
  * Use the [resolver-endpoint delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/delete.html) command and required parameters to delete a resolver endpoint:
Command
CopyTry It
```
oci dns resolver-endpoint delete --resolver-endpoint-id resolver-endpoint_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/DeleteResolverEndpoint) operation to delete a resolver endpoint.


Was this article helpful?
YesNo

