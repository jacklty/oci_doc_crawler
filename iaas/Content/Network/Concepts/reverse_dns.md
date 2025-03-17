Updated 2024-07-08
# Reverse DNS (PTR)
A reverse DNS record, also known as a pointer record (PTR), resolves an IP address back to a fully qualified domain name (FQDN).
Reverse DNS records function in the opposite way of an A (IPv4) or AAAA (IPv6) forward record. For example: `192.0.2.5 → myhost.mydomain.com`.
You can request that a PTR record be established for your cloud IP addresses:
  1. Create an **A** (IPv4) or **AAAA**(IPv6) forward record that points the fully qualified domain name to the IP prior to opening the request. You can create the record using the [Oracle Cloud Infrastructure DNS service](https://docs.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm), or a third-party DNS provider.
  2. [Open a service request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) and include the following information:
    1. The IP address and fully qualified domain name (FQDN) you want in the PTR.
    2. The FQDN of the forward record that you created in step 1.

After the service request is received, the forward (A or AAAA) record information is validated to be sure it can be successfully resolved, and Oracle creates the PTR record on your behalf.
## Using the API 🔗 
Use the following operations to manage resolvers and resolver endpoints:
  * [ListResolvers](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ListResolvers)
  * [GetResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/GetResolver)
  * [UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver)
  * [ChangeResolverCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ChangeResolverCompartment)
  * [ListResolverEndpoints](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/ListResolverEndpoints)
  * [CreateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/CreateResolverEndpoint)
  * [GetResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/GetResolverEndpoint)
  * [UpdateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/UpdateResolverEndpoint)
  * [DeleteResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/DeleteResolverEndpoint)


Was this article helpful?
YesNo

