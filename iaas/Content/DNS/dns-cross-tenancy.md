Updated 2025-03-10
# Managing DNS Resources Across Tenancies
Create IAM policies that let a tenancy access DNS resources in other tenancies.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [DNS Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).
## Cross-Tenancy Policies 🔗 
An organization might want to share resources with another organization that has its own tenancy. It could be another business unit in a company, a company's customer, a company that provides services to another company, and so on. In these cases, you need cross-tenancy policies in addition to the required user and service policies already described. 
To access and share resources, the administrators of both tenancies need to create special IAM policy statements that explicitly state the resources that can be accessed and shared.
### Endorse, Admit, and Define Statements
Here's an overview of the special verbs used in cross-tenancy statements:
  * **Endorse** : States the general set of abilities that a group in one tenancy can perform in the other tenancies. The _Endorse_ statement always belongs in the tenancy with the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, this tenancy is called the source.
  * **Admit** : States the kind of ability in a tenancy that you want to grant to a group from another tenancy. The _Admit_ statement belongs in the tenancy who is granting "admittance" to the tenancy. The _Admit_ statement identifies the group of users that requires resource access from the source tenancy and identified with a corresponding _Endorse_ statement. In the examples, this tenancy is called the destination.
  * **Define** : Assigns an alias to a tenancy OCID for _Endorse_ and _Admit_ policy statements. A _Define_ statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for _Admit_ statements.
Define statements must be included in the same policy entity as the endorse or the admit statement.


The _Endorse_ and _Admit_ statements work together, but they reside in separate policies, one in each tenancy. Without a corresponding statement that specifies access, a particular _Endorse_ or _Admit_ statement grants no access. _Agreement is required from both tenancies._
**Important** In addition to policy statements, you must also be subscribed to a region to share resources across regions.
### Source tenancy policy statements
The administrator for source tenancy creates policy statements that endorse an IAM group allowed to manage resources in the destination tenancy.
Here is an example of a broad policy statement that endorses the IAM group DNSAdmins to do anything with all DNS resources in any tenancy:
Copy
```
Endorse group DNSAdmins to manage DNS in any-tenancy 
```

To write a policy that reduces the scope of tenancy access, the destination administrator must provide the destination tenancy OCID. Here is an example of policy statements that endorse the IAM group DNSAdmins group to manage DNS resources in the DestinationTenancy only:
Copy
```
Define tenancy DestinationTenancy as ocid1.tenancy.oc1..<unique_ID>
Endorse group DNSAdmins to manage dns in tenancy DestinationTenancy
```

### Destination tenancy policy statements
The destination administrator creates policy statements that:
  * Defines the source tenancy and IAM group that's allowed to access resources in another tenancy. The source administrator must provide this information.
  * Admits those defined sources to access DNS resources that you want to allow access to in the local tenancy.


Here is an example of policy statements that admit the IAM group DNSAdmins in the source tenancy to do anything with all DNS resources in the local tenancy:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group DNSAdmins as ocid1.group.oc1..<unique_ID>
Admit group DNSAdmins of tenancy SourceTenancy to manage dns in tenancy 
```

Here is an example of policy statements that endorse the IAM group DNSAdmins in the source tenancy to manage DNS resources only in the SharedZones compartment :
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group DNSAdmins as ocid1.group.oc1..<unique_ID>
Admit group DNSAdmins of tenancy SourceTenancy to manage dns in compartment SharedZones 
```

### Example: To create a child zone in a different tenancy from the parent zone
Here's an example of a commonly used scenario where the child zone resides in a different tenancy from the parent zone:
**Parent zone policies:**```
define tenancy ChildZoneTenancy as ocid1.tenancy.oc1..<child_zone_tenancy_unique_ID>
define group ChildZoneGroup as ocid1.group.oc1..<child_zone_group_unique_ID>
admit group ChildZoneGroup of tenancy ChildZoneTenancy to manage dns-records in tenancy where all {target.dns-zone.name = '<example.com>', target.dns-record.type = 'NS', target.dns-domain.name = '<child.example.com>'}
admit group ChildZoneGroup of tenancy ChildZoneTenancy to associate dns-records in tenancy with dns-zones in tenancy ChildZoneTenancy
```

**Child zone policies:**```
define tenancy ParentZoneTenancy as ocid1.tenancy.oc1..<parent_zone_tenancy_unique_ID>
endorse group ChildZoneGroup to manage dns-records in tenancy ParentZoneTenancy where target.dns-zone.name = '<example.com>'
endorse group ChildZoneGroup to associate dns-zones in tenancy with dns-records in tenancy ParentZoneTenancy
```

### Example: To create a parent zone in a different tenancy from an existing child zone
To create a parent zone (`example.com`) when one or more child zones (`child.example.com`) already exist in other tenancies, the user in the parent zone tenancy must have permission to delete any child zones that exist.
**Parent zone tenancy policies:**
```
define tenancy ChildZoneTenancy as ocid1.tenancy.oc1..<child_zone_tenancy_unique_ID> 
endorse group ParentTenancyGroup to manage dns-zones in tenancy ChildZoneTenancy where target.dns-zone.name = '<child.example.com>'
```

**Child zone tenancy policies:**
```
define tenancy ParentZoneTenancy as ocid1.tenancy.oc1..<parent_zone_tenancy_unique_ID>
define group ParentTenancyGroup as ocid1.group.oc1..<unique_ID> admit group ParentTenancyGroup to manage dns-zones in tenancy ChildZoneTenancy 
where target.dns-zone.name = '<child.example.com>'
```

If child zones exist in many tenancies, create a set of policies for each tenancy.
### DNS Operations that require policy statements to function across tenancies
The following table shows DNS operations that require admit and endorse policy statements to function across tenancies. For each use case, you need the minimum listed user or group permissions for the source and destination tenancy.
To | Source Tenancy Permission | Destination Tenancy Permission  
---|---|---  
Create a private zone where the view is in a different tenancy | DNS_ZONE_CREATE | DNS_VIEW_INSPECT  
Create a zone with a TSIG key in a different tenancy | DNS_ZONE_CREATE | DNS_TSIG_KEY_READ  
Create a child zone in a different tenancy than the parent zone.  | DNS_ZONE_CREATE | DNS_RECORD_UPDATE  
Create a child zone with TSIG key in a different tenancy than the parent zone. |  DNS_ZONE_CREATE DNS_TSIG_KEY_READ (if the TSIG key is in the source tenancy.) |  DNS_RECORD_UPDATE DNS_TSIG_KEY_READ (if the TSIG key is in the destination tenancy.)  
Update a zone with a TSIG key in a different tenancy | DNS_ZONE_UPDATE | DNS_TSIG_KEY_READ  
Create an attachment for a zone to a steering policy in a different tenancy | DNS_ZONE_UPDATE | DNS_STEERING_POLICY_READ  
Update an attachment for a zone to a steering policy in a different tenancy | DNS_ZONE_UPDATE | DNS_STEERING_POLICY_READ  
Delete an attachment from a zone to a steering policy in a different tenancy | DNS_ZONE_UPDATE | DNS_STEERING_POLICY_READ  
Update resolver information where the associated view is in a different tenancy | DNS_RESOLVER_UPDATE | DNS_VIEW_INSPECT  
Was this article helpful?
YesNo

