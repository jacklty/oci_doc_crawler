Updated 2024-09-17
# Resolver Endpoints
Resolver endpoints are attached to a VCN or a subnet. 
A DNS forwarding resolver endpoint is required before you can create a resolver rule. No listening endpoint is required for compute instances sending queries to 169.254.169.254. Two types of endpoint are used: 
  * **Listening:** A listening endpoint receives queries from these sources: within the VCN, other VCN Resolvers, or your on-premises network's DNS. Once created, no further configuration is needed for a listening endpoint.
  * **Forwarding:** A forwarding endpoint forwards DNS queries to the Listening endpoint for resolvers in other peered VCNs or your on-premises network's DNS. Decisions about where to forward queries are based on [resolver rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm#dns_topic_resolver_rules "Rules are used to answer queries that aren't answered by a resolver's views. They're checked in order, and each can optionally have conditions that limit which queries they apply to.") that you define. 


Resolver endpoints are highly available and backed by availability domains and fault domains of virtual networking.
**Note** IPv6 isn't supported for listening or forwarding endpoints. 
An endpoint can only be configured to either forward or listen.
**Note** Network security groups (NSGs) act as a virtual firewall for your DNS resolver endpoints. An NSG consists of a set of ingress and egress [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that apply only to the associated DNS resolver endpoints. 
We recommend that you change the security list or NSG security rules to allow traffic bound for UDP Port 53 (and optionally TCP Port 53) on your DNS listener endpoints.
## Resolver Endpoint Tasks 🔗 
  * [Creating a Resolver Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm#top "Create a resolver endpoint that can used for forwarding and listening to DNS queries to or from another private DNS system such as a peered VCN or an on-premises network.")
  * [Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm#top "You can view a list of resolver endpoints.")
  * [Getting a Resolver Endpoint's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-get.htm#top "View details about a resolver endpoint.")
  * [Adding a Network Security Group (NSG) to a Resolver Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-add-nsg.htm#top "Add a network security group \(NSG\) to a resolver endpoint.")
  * [Removing a Network Security Group (NSG) from a Resolver Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-remove-nsg.htm#top "You can remove network security groups \(NSGs\) from your resolver endpoint. The NSG no longer acts as a virtual firewall for the endpoint.")
  * [Deleting a Resolver Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-delete.htm#top "Delete an enpoint from a resolver.")


Was this article helpful?
YesNo

