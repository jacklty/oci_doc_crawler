Updated 2025-01-22
# Accessing Object Storage Resources Across Tenancies
Learn about how to write policies that gives your tenancy access to Object Storage resources in other tenancies.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
## Cross-Tenancy Policies 🔗 
Your organization might also want to share resources with another organization that has its own tenancy. It could be another business unit in your company, a customer of your company, a company that provides services to your company, and so on. In cases like these, you need cross-tenancy policies in addition to the required user and service policies described previously. 
To access and share resources, the administrators of both tenancies need to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words _Define_ , _Endorse_ , and _Admit_.
### Endorse, Admit, and Define Statements 🔗 
Here's an overview of the special verbs used in cross-tenancy statements:
  * **Endorse** : States the general set of abilities that a group _in your own tenancy_ can perform in other tenancies. The _Endorse_ statement always belongs in the tenancy that contains the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, we refer to this tenancy as the source tenancy.
  * **Admit** : States the kind of ability in _your own tenancy_ that you want to grant a group from the other tenancy. The _Admit_ statement belongs in the tenancy who is granting "admittance" to the tenancy. The _Admit_ statement identifies the group of users that requires resource access from the source tenancy and is identified with a corresponding _Endorse_ statement. In the examples, we refer to this tenancy as the destination tenancy.
  * **Define** : Assigns an alias to a tenancy OCID for _Endorse_ and _Admit_ policy statements. A _Define_ statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for _Admit_ statements.
Include a _Define_ statement in the same policy entity as the _Endorse_ or _Admit_ statement.


The _Endorse_ and _Admit_ statements work together. An _Endorse_ statement resides in the source tenancy while an _Admit_ statement resides in the destination tenancy. Without a corresponding statement that specifies access, a particular _Endorse_ or _Admit_ statement grants no access. _Both tenancies must agree on access._
**Important** In addition to policy statements, you must also subscribe to a region to share resources across regions.
### Source Tenancy Policy Statements
The source and target tenancy administrators create policy statements that endorse a source IAM group allowed to manage resources in the destination tenancy.
Here's an example of a broad policy statement that endorses the IAM group `StorageAdmins` group to do anything with all Object Storage resources in any tenancy:
Copy
```
Endorse group StorageAdmins to manage object-family in any-tenancy 
```

To write a policy that reduces the scope of tenancy access, the source administrator must reference the destination tenancy OCID provided by the destination administrator. Here’s an example of policy statements that endorse the IAM group `StorageAdmins` group to manage Object Storage resources in `DestinationTenancy` only:
Copy
```
Define tenancy DestinationTenancy as ocid1.tenancy.oc1..<unique_ID>
Endorse group StorageAdmins to manage object-family in tenancy DestinationTenancy
```

### Destination Tenancy Policy Statements
The destination administrator creates policy statements that:
  * Defines the source tenancy and IAM group that's allowed to access resources in your tenancy. The source administrator must provide this information.
  * Admits those defined sources to access Object Storage resources that you want to allow access to in your tenancy.


Here's an example of policy statements that endorse the IAM group `StorageAdmins` in the source tenancy to do anything with all Object Storage resources in your tenancy:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group StorageAdmins as ocid1.group.oc1..<unique_ID>
Admit group StorageAdmins of tenancy SourceTenancy to manage object-family in tenancy 
```

Here's an example of policy statements that endorse the IAM group `StorageAdmins` in the source tenancy to manage Object Storage resources only the `SharedBuckets` compartment:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group StorageAdmins as ocid1.group.oc1..<unique_ID>
Admit group StorageAdmins of tenancy SourceTenancy to manage object-family in compartment SharedBuckets 
```

Was this article helpful?
YesNo

