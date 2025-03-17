Updated 2024-02-20
# Resolver Rules
Rules are used to answer queries that aren't answered by a resolver's views. They're checked in order, and each can optionally have conditions that limit which queries they apply to.
When a rule condition is matched, it results in the forwarding action and no later rule is evaluated.
**Important** Forwarding redundancy isn't achieved using duplicate forwarding rules, because only the first matching rule is used. Instead, consider creating a network load balancer (NLB) with redundant backends, and use the NLB IP address with a single forwarding rule. 
Queries not matched by any view or rule are resolved from internet DNS. You can have up to 50 rules per resolver.
**Note** Endpoints are used in the rule, and they must exist before you create a resolver rule. 
## Use case 🔗 
The most common application is to have one or more rules that follow this general form: 
If <query domain> is <example.com>, forward using <forwarding-endpoint> to IP address X.X.X.X.
Followed by a final rule that follows this form: 
If <anything else> , forward using <forwarding-endpoint> to IP address Y.Y.Y.Y.
So if the query is looking for example.com, the resolver internally forwards it to X.X.X.X through the specified forwarding endpoint and responds with the answer it receives. For any other query, it forwards to Y.Y.Y.Y through the same forwarding endpoint and responds with that answer it gets from Y.Y.Y.Y.
## Resolver Rule Tasks 🔗 
  * [Creating a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-rule-create.htm#resolver-rule-create "You can create a resolver rule that's used to answer queries that aren't answered by a resolver's views.")
  * [Editing a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-rule-edit.htm#resolver-rule-edit "Change the information for a resolver rule.")
  * [Removing a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-rule-remove.htm#resolver-rule-remove "Remove rules from the resolver.")


Was this article helpful?
YesNo

