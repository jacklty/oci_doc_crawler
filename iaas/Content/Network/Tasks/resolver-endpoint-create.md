Updated 2023-05-30
# Creating a Resolver Endpoint
Create a resolver endpoint that can used for forwarding and listening to DNS queries to or from another private DNS system such as a peered VCN or an on-premises network.
[When you create a VCN and select the Use DNS hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About__How), this choice creates a [dedicated private DNS resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and a default private view with system-managed zones. 
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN.
See [Managing Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm) for more information about managing private zones and views.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm)


  *     1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. From the **Private Resolver Details** screen, click **Endpoints** in the left-hand navigation.
    3. Click **Create Endpoint**. The **Create Endpoint** screen appears. 
    4. Make choices for the following settings: 
       * Select a name for the endpoint. The name can use any combination of letters and numbers, but the only supported special character is an underscore.
       * Select a subnet for the endpoint from the pull-down list.
       * Select the endpoint type, which can be either **Listening** or **Forwarding**. When you make this choice, you provide an IP address, or allow Oracle to assign one for the endpoint. This IP address is used by the resolver to forward DNS queries, or to listen for DNS queries from other systems. The IP address must be in the same CIDR block used by the VCN or subnet associated with the resolver.
       * _Optional:_ Use a [Network Security Group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) to control traffic. To use this feature, select an NSG to use with the endpoint. You can also add an NSG after the endpoint is created.
Next Steps: 
    * Optionally, [create a resolver rule.](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm#dns_topic_resolver_rules "Rules are used to answer queries that aren't answered by a resolver's views. They're checked in order, and each can optionally have conditions that limit which queries they apply to.")
  * Use the [resolver-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/create.html) command and required parameters to create a resolver endpoint:
Command
CopyTry It
```
oci dns resolver-endpoint create --is-forwarding [boolean] --is-listening [boolean] 
--name endpoint_name --resolver-id resolver_OCID --subnet-id subnet_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/CreateResolverEndpoint) operation to create a resolver endpoint.


Was this article helpful?
YesNo

