Updated 2023-05-30
# Adding a Network Security Group (NSG) to a Resolver Endpoint
Add a network security group (NSG) to a resolver endpoint.
Network security groups (NSGs) act as a virtual firewall for your DNS resolver endpoints. An NSG consists of a set of ingress and egress [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that apply only to the associated DNS resolver endpoints. 
Oracle recommends that you modify your security list or NSG security rules to allow traffic bound for UDP Port 53 (and optionally TCP Port 53) on your DNS listener endpoints.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN.
## Using the Console 🔗 
  1. From the **Private Resolver Details** screen, click the name of the endpoint you want to associate with a Network Security group. The **Endpoint Details** screen appears. 
  2. Click **Add Network Security Groups** , and select up to five security groups to associate with the endpoint. 
  3. When finished, click **Add Network Security Groups**. 


Was this article helpful?
YesNo

