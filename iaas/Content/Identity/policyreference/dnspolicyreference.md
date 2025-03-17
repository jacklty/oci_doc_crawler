Updated 2024-06-06
# Details for the DNS Service
This topic covers details for writing policies to control access to the DNS service.
## Aggregate Resource-Type 🔗 
`dns`
## Individual Resource-Types 🔗 
`dns-zones`
`dns-records`
`dns-steering-policies`
`dns-steering-policy-attachments`
`dns-tsig-keys`
`dns-views`
`dns-resolvers`
### Comments
A policy that uses `<verb> dns` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm#Details) for details of the API operations covered by each verb, for each individual resource-type included in `dns`.
## Supported Variables 🔗 
The DNS service supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus the ones listed here.
The `dns-zones` resource type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.dns-zone.id` | Entity (OCID) | Use this variable to control access to specific DNS zones by OCID.  
`target.dns-zone.name` | String | Use this variable to control access to specific DNS zones by name.  
`target.dns-zone.apex-label` | String | The most significant DNS label for the target zone. Example: If the target zone's name is "service.example.com", the value of this variable would be "service."  
`target.dns-zone.parent-domain` | String | The domain name of the target zone's parent zone.  
`target.dns.scope` | String | Valid values are "public" and "private".  
The `dns-records` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-zone.id` | Entity (OCID) | Use this variable to control access to specific DNS zones by OCID.  
`target.dns-zone.name` | String | Use this variable to control access to specific DNS zones by name.  
`target.dns-record.type` | List (String) | Use this variable to control access to specific DNS records by type. Valid values in the list can be any supported DNS resource type. For example, "A", "AAAA", "TXT", and so on. See [Supported Resource Records](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).  
`target.dns-domain.name` | List (String) |  Use this variable to control access to specific domain names. Applicable to the following API operations:
  * `GetDomainRecords`
  * `PatchDomainRecords`
  * `UpdateDomainRecords`
  * `DeleteRRSet`
  * `GetRRSet`
  * `PatchRRSet`
  * `UpdateRRSet`

  
`target.dns-zone.source-compartment.id` | Entity (OCID) |  Use this variable to control access to the current compartment of the DNS zone by OCID.  
`target.dns-zone.destination-compartment.id` | Entity (OCID) |  Use this variable to control access to the destination compartment of the DNS zone by OCID.  
**Note** Use the `target.dns-record.type` and `target.dns-domain.name` variables in your authorization policy to restrict users when modifying records of a specific type in a specific subdomain. A policy like this would allow a specific group of users to modify "A" records in the "example.com" domain: `Allow group <GroupName> to use dns in compartment <CompartmentName> where all {target.dns-record.type='A', target.dns-domain.name = 'example.com'}` Users will only be authorized to use RRSet API operations with this type of authorization policy. 
The `dns-steering-policies` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-steering-policy.id` | Entity (OCID) | Use this variable to control access to specific steering policies by OCID.  
`target.dns-steering-policy.display-name` | String | Use this variable to control access to specific steering policies by name.  
`target.dns-steering-policy.source-compartment.id` | Entity (OCID) |  Use this variable to control access to the current compartment of the steering policy by OCID.  
`target.dns-steering-policy.destination-compartment.id` | Entity (OCID) |  Use this variable to control access to the destination compartment of the steering policy by OCID.  
The `dns-tsig-keys` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-tsig-key.id` | Entity (OCID) | Use this variable to control access to specific TSIG keys by OCID.  
`target.dns-tsig-key.name` | String | Use this variable to control access to specific TSIG keys by name.  
`target.dns-tsig-key.source-compartment.id` | Entity (OCID) | Use this variable to control access to the current compartment of a specific TSIG key by OCID.  
`target.dns-tsig-key.destination-compartment.id` | Entity (OCID) | Use this variable to control access to the destination compartment of the specific TSIG key by OCID.  
The `dns-view` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-view.id` | Entity (OCID) | Use this variable to control access to specific view by OCID.  
`target.dns-view.display-name` | String | Use this variable to control access to specific view by name.  
`target.dns-view.source-compartment.id` | Entity (OCID) | Use this variable to control access to the current compartment of a specific view by OCID.  
`target.dns-view.destination-compartment.id` | Entity (OCID) | Use this variable to control access to the destination compartment of the specific view by OCID.  
The `dns-resolver` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-resolver.id` | Entity (OCID) | Use this variable to control access to specific resolver by OCID.  
`target.dns-resolver.display-name` | String | Use this variable to control access to specific resolver by name.  
`target.dns-resolver.source-compartment.id` | Entity (OCID) | Use this variable to control access to the current compartment of a specific resolver by OCID.  
`target.dns-resolver.destination-compartment.id` | Entity (OCID) | Use this variable to control access to the destination compartment of the specific resolver by OCID.  
The `dns-resolver-endpoint` resource type can use the following variables:
Variable  | Variable Type | Comments  
---|---|---  
`target.dns-resolver-endpoint.name` | String | Use this variable to control access to specific resolver endpoints by name.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `manage` verb for the `dns-records` resource-type covers no extra permissions or API operations compared to the `use` verb.
[dns-zones](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_ZONE_INSPECT | `ListZones` | none  
read | INSPECT + DNS_ZONE_READ | `GetZone` | `GetZoneRecords`  
use | READ + DNS_ZONE_UPDATE | `UpdateZone` | `UpdateZoneRecords` `PatchZoneRecords` `CreateSteeringPolicyAttachment` `DeleteSteeringPolicyAttachment`  
manage | UPDATE + DNS_ZONE_CREATE DNS_ZONE_DELETE DNS_ZONE_MOVE | `CreateZone` `DeleteZone` `ChangeZoneCompartment` | none  
[dns-records](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_RECORD_INSPECT | none | none  
read | INSPECT + DNS_RECORD_READ | `GetDomainRecords` `GetRRSet` | `GetZoneRecords`  
use | READ + DNS_RECORD_UPDATE | `PatchDomainRecords` `UpdateDomainRecords` `DeleteRRSet` `PatchRRSet` `UpdateRRSet` | `UpdateZoneRecords` `PatchZoneRecords` `UpdateSteeringPolicyAttachment`  
manage | UPDATE + DNS_RECORD_CREATE DNS_RECORD_DELETE | no extra | none  
[dns-steering-policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_STEERING_POLICY_INSPECT | `ListSteeringPolicies` | none  
read | INSPECT + DNS_STEERING_POLICY_READ | `GetSteeringPolicy` | `UpdateSteeringPolicyAttachment` `DeleteSteeringPolicyAttachment`  
use | READ +  DNS_POLICY_STEERING_UPDATE | `UpdateSteeringPolicy` | none  
manage | UPDATE + DNS_STEERING_POLICY_CREATE DNS_STEERING_POLICY_DELETE DNS_STEERING_POLICY_MOVE | `CreateSteeringPolicy` `DeleteSteeringPolicy` `ChangeSteeringPolicyCompartment` | none  
[dns-steering-policy-attachments](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_STEERING_ATTACHMENT_INSPECT | `ListSteeringPolicyAttachments` | none  
read | INSPECT + DNS_STEERING_ATTACHMENT_READ | `GetSteeringPolicyAttachment` | none  
[dns-tsig-keys](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_TSIG_KEY_INSPECT | `ListTsigKeys` | none  
read | INSPECT + DNS_TSIG_KEY_READ | `GetTsigKey` | none  
use | READ + DNS_TSIG_KEY_UPDATE | `UpdateTsigKey` | none  
manage | USE + DNS_TSIG_KEY_CREATE DNS_TSIG_KEY_DELETE DNS_TSIG_KEY_MOVE | `CreateTsigKey` `DeleteTsigKey` `ChangeTsigKeyCompartment` | none  
[dns-views](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_VIEW_INSPECT | `ListViews` | none  
read | INSPECT + DNS_VIEW_READ | `GetView` | none  
use | READ + DNS_VIEW_UPDATE | `UpdateView` | none  
manage | USE + DNS_VIEW_CREATE DNS_VIEW_DELETE DNS_VIEW_MOVE | `CreateView` `DeleteView` `ChangeViewCompartment` | none  
[dns-resolvers](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_RESOLVER_INSPECT | `ListResolvers` | none  
read | INSPECT + DNS_RESOLVER_READ | `GetResolver` | none  
use | READ + DNS_RESOLVER_UPDATE | `UpdateResolver` | none  
manage | USE + DNS_RESOLVER_CREATE DNS_RESOLVER_DELETE DNS_RESOLVER_MOVE | `CreateResolver` `DeleteResolver` `ChangeResolverCompartment` | none  
[dns-resolver-endpoint](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DNS_RESOLVER_ENDPOINT_INSPECT | `ListResolverEndpoints` | none  
read | INSPECT + DNS_RESOLVER_ENDPOINT_READ | `GetResolverEndpoint` | none  
use | READ + DNS_RESOLVER_ENDPOINT_UPDATE | `UpdateResolverEndpoint` | none  
manage | USE + DNS_RESOLVER_ENDPOINT_CREATE DNS_RESOLVER_ENDPOINT_DELETE | `CreateResolverEndpoint``DeleteResolverEndpoint` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`ListZones` | DNS_ZONE_INSPECT  
`CreateZone` | DNS_ZONE_CREATE  
`CreateChildZone` | DNS_ZONE_CREATE and DNS_RECORD_UPDATE  
`DeleteZone` | DNS_ZONE_DELETE  
`GetZone` | DNS_ZONE_READ  
`UpdateZone` | DNS_ZONE_UPDATE  
`ChangeZoneCompartment` | DNS_ZONE_MOVE  
`GetZoneRecords` | DNS_ZONE_READ and DNS_RECORD_READ  
`PatchZoneRecords` | DNS_ZONE_UPDATE and DNS_RECORD_UPDATE  
`UpdateZoneRecords` | DNS_ZONE_UPDATE and DNS_RECORD_UPDATE  
`GetDomainRecords` |  DNS_RECORD_READ  
`PatchDomainRecords` | DNS_RECORD_UPDATE  
`UpdateDomainRecords` | DNS_RECORD_UPDATE  
`DeleteRRSet` | DNS_RECORD_UPDATE  
`GetRRSet` | DNS_RECORD_READ  
`PatchRRSet` | DNS_RECORD_UPDATE  
`UpdateRRSet` | DNS_RECORD_UPDATE  
`ListSteeringPolicies` | DNS_STEERING_POLICY_INSPECT  
`CreateSteeringPolicy` | DNS_STEERING_POLICY_CREATE  
`GetSteeringPolicy` | DNS_STEERING_POLICY_READ  
`UpdateSteeringPolicy` | DNS_STEERING_POLICY_UPDATE  
`DeleteSteeringPolicy` | DNS_STEERING_POLICY_DELETE  
`ChangeSteeringPolicyCompartment` | DNS_STEERING_POLICY_MOVE  
`ListSteeringPolicyAttachments` | DNS_STEERING_ATTACHMENT_INSPECT  
`CreateSteeringPolicyAttachment` | DNS_ZONE_UPDATE and DNS_STEERING_POLICY_READ  
`GetSteeringPolicyAttachment` | DNS_STEERING_ATTACHMENT_READ  
`UpdateSteeringPolicyAttachment` | DNS_ZONE_UPDATE and DNS_STEERING_POLICY_READ  
`DeleteSteeringPolicyAttachment` | DNS_ZONE_UPDATE and DNS_STEERING_POLICY_READ  
`ListTsigKeys` | DNS_TSIG_KEY_INSPECT  
`CreateTsigKey` | DNS_TSIG_KEY_CREATE  
`GetTsigKey` | DNS_TSIG_KEY_READ  
`UpdateTsigKey` | DNS_TSIG_KEY_UPDATE  
`DeleteTsigKey` | DNS_TSIG_KEY_DELETE  
`ChangeTsigKeyCompartment` | DNS_TSIG_KEY_MOVE  
`ListViews` | DNS_VIEW_INSPECT  
`CreateView` | DNS_VIEW_CREATE  
`GetView` | DNS_VIEW_READ  
`UpdateView` | DNS_VIEW_UPDATE  
`DeleteView` | DNS_VIEW_DELETE  
`ChangeViewCompartment` | DNS_VIEW_MOVE  
`ListResolvers` | DNS_RESOLVER_INSPECT  
`GetResolver` | DNS_RESOLVER_READ  
`UpdateResolver` | DNS_RESOLVER_UPDATE  
`ChangeResolverCompartment` | DNS_RESOLVER_MOVE  
`ListResolverEndpoints` | DNS_RESOLVER_ENDPOINT_INSPECT and DNS_RESOLVER_READ  
`CreateResolverEndpoint` | DNS_RESOLVER_UPDATE and DNS_RESOLVER_ENDPOINT_CREATE  
`GetResolverEndpoint` | DNS_RESOLVER_ENDPOINT_READ  
`UpdateResolverEndpoint` | DNS_RESOLVER_UPDATE and DNS_RESOLVER_ENDPOINT_UPDATE  
`DeleteResolverEndpoint` | DNS_RESOLVER_UPDATE and DNS_RESOLVER_ENDPOINT_DELETE  
Was this article helpful?
YesNo

