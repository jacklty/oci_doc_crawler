Updated 2023-05-30
# Private DNS resolvers
A private DNS resolver answers DNS queries for a VCN per a configuration you create.
When you create a VCN and select the [**Use DNS hostnames in this VCN**](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network) option, this choice creates a dedicated private DNS resolver and a default private view with system-managed zones. A private DNS resolver also handles internal DNS queries for your VCN based on private views and the private zones that you have created and the [rules you create for the resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm#dns_topic_resolver_rules "Rules are used to answer queries that aren't answered by a resolver's views. They're checked in order, and each can optionally have conditions that limit which queries they apply to."). A private DNS zone has capabilities similar to an internet DNS zone, but only provides responses for clients that can reach it through a VCN. The default view is only used if the resolver does not get a match from the other attached private views, if there are any. A private resolver can be configured to use views and zones as well as conditional forwarding rules to define how to respond to DNS queries. To better understand views and zones, refer to [Private DNS](https://docs.oracle.com/iaas/Content/DNS/Tasks/privatedns.htm). 
You can create your own custom domains to use in addition to the system-generated names based on VCNs and subnets, and you can do VCN to VCN and VCN to on-premises resolution.
## Private Resolver Tasks 🔗 
  * [Adding a Private View to a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm#top "You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN.")
  * [Removing a Private View From a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm#top "You can remove a non-default private view from a resolver.")
  * [Listing Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-list.htm#top "View a list of resolvers in a compartment.")
  * [Getting a Resolver's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-get.htm#top "View details about a private resolver in a VCN.")
  * [Editing a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm#top "You can update information like the resolver name.")
  * [Moving a Resolver Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm#top "You can move a resolver from one compartment to another.")


### To manage DNS zones and views
See [Managing Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm) for more information.
Was this article helpful?
YesNo

