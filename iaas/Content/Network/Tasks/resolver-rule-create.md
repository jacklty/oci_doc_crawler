Updated 2024-02-20
# Creating a Resolver Rule
You can create a resolver rule that's used to answer queries that aren't answered by a resolver's views.
**Note** Endpoints are used in the rule, and they must exist before you create a resolver rule. 
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") and [Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm#dns_topic_resolver_endpoints "Resolver endpoints are attached to a VCN or a subnet.") for more information about resolvers and endpoints in your VCN. 
## Using the Console 🔗 
  1. From the **Private Resolver Details** screen, click **Rules** in the Resources column. Click **Manage Rules**. The **Manage Rules** screen appears. 
  2. You can have up to 50 rules per resolver. For each rule, select: 
     * **Rule condition:** Determines whether routing decisions are made based on the query's originating CIDR Block or Domain (up to 10 hostnames), or neither (Select None to match any CIDR Block or Domain).
     * **Client CIDR blocks or Domains:** Up to 10 CIDR blocks or domains. 
     * **Rule action:** This field is read-only. Forward is the only option.
     * **Source endpoint:** The private endpoint used to forward queries when the rule condition is met.
     * **Destination IP address:** The address to forward the query to if the rule condition is met.
  3. Click **+Additional Rule** to create another rule if necessary. 
  4. Click **Save Changes** when finished.


Was this article helpful?
YesNo

