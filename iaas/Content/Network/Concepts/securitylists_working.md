Updated 2025-02-12
# Working with Security Lists
Learn general information about managing security lists. 
## General Process for Working with Security Lists
  1. Create a security list.
  2. Add security rules to the security list.
  3. Associate the security list with one or more subnets.
  4. Create resources in the subnet (for example, create compute instances in the subnet). The security rules apply to all the VNICs in that subnet. See [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).


## Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network) covers management of all Networking components, including security lists.
If you have security admins who need to manage security lists but not other components in Networking, you could write a more restrictive policy: 
```
Allow group SecListAdmins to manage security-lists in tenancy
Allow group SecListAdmins to manage vcns in tenancy
```

Both statements are needed because the creation of a security list affects the VCN the security list is in. The scope of the second statement _also_ allows the SecListAdmins group to create VCNs. However, the group can't create subnets or manage any other components related to any of those VCNs (except for the security lists), because other permissions would be required for those resources. The group also can't delete any existing VCNs that already have subnets in them, because that action would require permissions related to subnets.
For more information, see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
Was this article helpful?
YesNo

