Updated 2025-01-31
# Introduction to Network Sources
A network source is a set of defined IP addresses.
The IP addresses can be public IP addresses or IP addresses from VCNs within your tenancy. After you create the network source, you can reference it in policy or in your tenancy's authentication settings to control access based on the originating IP address.
Network sources can only be created in the tenancy (or root compartment) and, like other IAM resources, reside in the [home region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Home). For information about the number of network sources you can have, see [IAM With Identity Domains Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iam-service-limits). 
You can use network sources to help secure your tenancy in the following ways:
  * Specify the network source in IAM policy to restrict access to resources.
When specified in a policy, IAM validates that requests to access a resource originate from an allowed IP address. 
For example, you can restrict access to Object Storage buckets in your tenancy to only users that are signed in to Oracle Cloud Infrastructure through your corporate network. Or, you can allow only resources belonging to specific subnets of a specific VCN to make requests over a [service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
  * An identity domain's Sign In policies manage access to sign into in the identity domain. For more information, see [Managing Sign-On Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#Managing_signonpolicies).


Was this article helpful?
YesNo

