Updated 2025-02-13
# Verbs
The verb element of a policy statement specifies the type of access. For example, use `inspect` to let third-party auditors list the specified resources.
Verbs for creating IAM policies are defined by Oracle.
From least to most access, following are possible verbs:
  * inspect
  * read
  * use
  * manage


**General Access Covered by Each Verb**
Following are general types of access and target users for each possible verb, which are ordered from least to most access. Some resources support exceptions. See 
Verb | Target User | Types of Access Covered  
---|---|---  
`inspect` | Third-party auditors | Ability to list resources, without access to any confidential information or user-specified metadata that might be part of that resource. **Important:** The operation to list policies includes the contents of the policies themselves. The list operations for the Networking resource-types return all the information (for example, the contents of security lists and route tables).   
`read` | Internal auditors | Includes `inspect` plus the ability to get user-specified metadata and the actual resource itself.   
`use` | Day-to-day end users of resources | Includes `read` plus the ability to work with existing resources (the actions vary by resource type). Includes the ability to update the resource, except for resource-types where the "update" operation has the same effective impact as the "create" operation (for example, `UpdatePolicy`, `UpdateSecurityList`, and more), in which case the "update" ability is available only with the `manage` verb. In general, this verb doesn't include the ability to create or delete that type of resource.  
`manage` | Administrators | Includes all permissions for the resource.  
The verb gives a certain general type of access (e.g., `inspect` lets you list and get resources). When you then join that type of access with a particular resource-type in a policy (e.g., `Allow group XYZ to inspect compartments in the tenancy`), then you give that group access to a specific set of permissions and API operations (e.g., `ListCompartments`, `GetCompartment`). For more examples, see [Details for Verbs + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm#Identity). The [Detailed Service Policy Reference](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference.htm "Get an overview of IAM policy reference topics, including verbs, resources types, and general variables.") includes a similar table for each service, giving you a list of exactly which API operations are covered for each combination of verb and resource-type. 
There are some special exceptions or nuances for certain resource-types. 
**Users:** Access to both `manage users` and `manage         groups` lets you do anything with users and groups, including creating and deleting users and groups, and adding/removing users from groups. To add/remove users from groups without access to creating and deleting users and groups, only both `use users` and `use groups` are required. See [Policy Builder Policy Templates](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#top). 
**Policies:** The ability to update a policy is available only with `manage policies`, not `use policies`, because updating a policy is similar in effect to creating a new policy (you can overwrite the existing policy statements). In addition, `inspect policies `lets you get the full contents of the policies. 
**Object Storage objects:** `inspect objects` lets you list all the objects in a bucket and do a HEAD operation for a particular object. In comparison, `read objects` lets you download the object itself.
**Load Balancer resources:** Be aware that `inspect load-balancers` lets you get _all_ information about your load balancers and related components (backend sets, etc.). 
**Networking resources:**
Be aware that the `inspect` verb not only returns general information about the cloud network's components (for example, the name and OCID of a security list, or of a route table). It also includes the contents of the component (for example, the actual rules in the security list, the routes in the route table, and so on). 
Also, the following types of abilities are available only with the `manage` verb, not the `use` verb:
  * Update (enable/disable) `internet-gateways`
  * Update `security-lists`
  * Update `route-tables`
  * Update `dhcp-options`
  * Attach a Dynamic Routing Gateway (DRG) to a Virtual Cloud Network (VCN)
  * Create an IPSec connection between a DRG and customer-premises equipment (CPE)
  * Peer VCNs


**Important** Each VCN has various components that directly affect the behavior of the network (route tables, security lists, DHCP options, Internet Gateway, and so on). When you create one of these components, you establish a relationship between that component and the VCN, which means you must be allowed in a policy to both create the component and manage the VCN itself. However, the ability to _update_ that component (to change the route rules, security list rules, and so on) **doesn't** require permission to manage the VCN itself, even though changing that component can directly affect the behavior of the network. This discrepancy is designed to give you flexibility in granting least privilege to users, and not require you to grant excessive access to the VCN so the user can manage other components of the network. Be aware that by giving someone the ability to update a particular type of component, you're implicitly trusting them with controlling the network's behavior.
Was this article helpful?
YesNo

