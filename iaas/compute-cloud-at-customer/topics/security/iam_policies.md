Updated 2024-08-06
# IAM Policies
Oracle Cloud Infrastructure Identity and Access Management (IAM) provides authentication of users, and authorization to access resources on Compute Cloud@Customer.
**Attention**
For Compute Cloud@Customer, IAM resources are managed in OCI within your tenancy, and synchronized to Compute Cloud@Customer every ten minutes or so. IAM resources can't be managed on the Compute Cloud@Customer infrastructure.
For detailed recommendations for securing IAM resources, See [Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm).
For IAM policies that are unique to Compute Cloud@Customer, see [Compute Cloud@Customer Policy Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/policy-reference.htm#policy-reference "Use policies to control access to Compute Cloud@Customer infrastructure and upgrade schedule operations.").
## Limit Access to Compute Cloud@Customer by Assigning it to its own Compartment  🔗 
Consider assigning each Compute Cloud@Customer infrastructure to its own compartment. Limit compartment access to only the users who are supposed to have access to the Compute Cloud@Customer infrastructure.
Was this article helpful?
YesNo

