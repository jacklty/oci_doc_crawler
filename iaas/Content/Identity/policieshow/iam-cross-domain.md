Updated 2024-09-26
# Cross-Tenancy Access Policies
Use cross-tenancy policy statements to create IAM policies that work across tenancies.
You can create cross-tenancy policy statements, in addition to the required user and service policy statements, to share resources with another organization that has its own tenancy. That organization might be another business unit in your company, a company customer, a company that provides services to you, and so on.
To access and share resources, the administrators of both tenancies need to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words _Define_ , _Endorse_ , and _Admit_.
## Endorse, Admit, and Define Statements 🔗 
Use the following special start words in cross-tenancy statements:
  * **Endorse** : States the general set of abilities that a group _in your own tenancy_ can perform in other tenancies. The _Endorse_ statement always belongs in the tenancy that contains the group of users crossing the boundaries to work with another tenancy's resources. In the examples, this tenancy is called the _source tenancy_.
  * **Admit** : States the kind of ability _in your own tenancy_ that you want to grant a group from the other tenancy. The _Admit_ statement belongs in the tenancy that is granting "admittance" to the tenancy. The _Admit_ statement identifies the group of users that requires resource access from the source tenancy and is identified with a corresponding _Endorse_ statement. In the examples, this tenancy is called the _destination tenancy_.
  * **Define** : Assigns an alias to a tenancy OCID for _Endorse_ and _Admit_ policy statements. The _Define_ statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for _Admit_ statements.
Include a _Define_ statement in the same policy statement as the _Endorse_ or _Admit_ policy statement.


The _Endorse_ and _Admit_ statements work together. An _Endorse_ statement resides in the source tenancy and an _Admit_ statement resides in the destination tenancy. Without a corresponding statement that specifies access, a particular _Endorse_ or _Admit_ statement grants no access. _Both tenancies must agree on access._
**Important** In addition to policy statements, target and source tenancies must subscribe to the same regions to share resources.
## Cross-Tenancy Examples
  * The following policy lets the group `StorageAdmins` manage resources in the destination tenancy Object Storage resources:
```
Endorse group StorageAdmins to manage object-family in any-tenancy 
```

The following policy statements endorse the IAM group `StorageAdmins` in the source tenancy to do anything with all Object Storage resources in your destination tenancy:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1.exampleuniqueID
Define group StorageAdmins as ocid1.group.oc1.exampleuniqueID
Admit group StorageAdmins of tenancy SourceTenancy to manage object-family in tenancy 
```

  * To write a policy that reduces the scope of tenancy access, the source administrator must reference the destination tenancy OCID provided by the destination administrator. The following policy statements endorse the IAM group `StorageAdmins` group to manage Object Storage resources in `DestinationTenancy` only:
Copy
```
Define tenancy DestinationTenancy as ocid1.tenancy.oc1..<unique_ID>
Endorse group StorageAdmins to manage object-family in tenancy DestinationTenancy
```

These example policy statements endorse the IAM group `StorageAdmins` in the source tenancy to manage Object Storage resources only the `SharedBuckets` compartment:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..exampleuniqueID
Define group StorageAdmins as ocid1.group.oc1..exampleuniqueID
Admit group StorageAdmins of tenancy SourceTenancy to manage object-family in compartment SharedBuckets 
```



Was this article helpful?
YesNo

