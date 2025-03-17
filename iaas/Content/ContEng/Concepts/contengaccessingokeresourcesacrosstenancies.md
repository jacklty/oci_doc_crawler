Updated 2025-01-10
# Accessing Cluster-Related Resources Across Tenancies
_Find out about the IAM policies required to enable one tenancy to access cluster-related resources in other tenancies._
When you want one tenancy to access resources in other tenancies, you have to create cross-tenancy policies.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and refer to:
  * [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#Policy_Configuration_for_Cluster_Creation_and_Deployment "Find out about the IAM policies to create before using Kubernetes Engine \(OKE\).")
  * [Details for Kubernetes Engine](https://docs.oracle.com/iaas/Content/Identity/policyreference/contengpolicyreference.htm)


## Cross-Tenancy Policies 🔗 
Your organization might want to share cluster-related resources with another organization that has its own tenancy. It could be another business unit in your company, a customer of your company, a company that provides services to your company, and so on. In cases like these, you need cross-tenancy policies in addition to the required user and service policies described in [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#Policy_Configuration_for_Cluster_Creation_and_Deployment "Find out about the IAM policies to create before using Kubernetes Engine \(OKE\).").
### Endorse, Admit, and Define statements 🔗 
To access and share resources between two tenancies, the administrators of both tenancies have to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words _Define_ , _Endorse_ , and _Admit_. 
Here's an overview of the special verbs used in cross-tenancy statements:
  * **Endorse** : States the general set of abilities that a group _in your own tenancy_ can perform in other tenancies. The _Endorse_ statement always belongs in the tenancy with the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, this tenancy is referred to as the source tenancy.
  * **Admit** : States the kind of ability in _your own tenancy_ that you want to grant a group from another tenancy. The _Admit_ statement belongs in the tenancy who is granting "admittance" to the tenancy. The _Admit_ statement identifies the group of users that requires resource access from the source tenancy and identified with a corresponding _Endorse_ statement. In the examples, this tenancy is referred to as the destination tenancy.
  * **Define** : Assigns an alias to a tenancy OCID for _Endorse_ and _Admit_ policy statements. A _Define_ statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for _Admit_ statements.
_Define_ statements must be included in the same policy entity as the _Endorse_ or the _Admit_ statement.


The _Endorse_ and _Admit_ statements work together, but they reside in separate policies, one in each tenancy. Without a corresponding statement that specifies access, a particular _Endorse_ or _Admit_ statement grants no access. _Agreement is required from both tenancies._
### Source policies 🔗 
The source administrator creates policy statements that endorse a source IAM group to manage resources in a destination tenancy.
Here is an example of a broad policy statement that endorses the IAM group OKE-Admins to do anything with all cluster-related resources in any tenancy:
Copy
```
Endorse group OKE-Admins to manage cluster-family in any-tenancy
```

To enable the source IAM group to create clusters in the destination tenancy, the source administrator must also create policy statements to endorse the group to manage virtual networks and inspect compartments. For example:
Copy
```
Endorse group OKE-Admins to manage virtual-network-family in any-tenancy
Endorse group OKE-Admins to inspect compartments in any-tenancy
```

To write a policy that reduces the scope of tenancy access to just the destination tenancy, the source administrator must obtain the destination tenancy's OCID from the destination administrator, and include that OCID in a policy statement. Here is an example of policy statements that endorse the IAM group OKE-Admins to manage cluster-related resources in the DestinationTenancy only:
Copy
```
Define tenancy DestinationTenancy as ocid1.tenancy.oc1..<unique_ID>
Endorse group OKE-Admins to manage cluster-family in tenancy DestinationTenancy
```

### Destination policies 🔗 
The destination administrator creates policy statements that:
  * Define the source tenancy and the IAM group that is allowed to access resources in the destination tenancy. The source administrator must provide the OCIDs of the source tenancy and the source IAM group.
  * Admit the source IAM group to access cluster-related resources in the destination tenancy.


Here is an example of policy statements that admit the IAM group OKE-Admins from the source tenancy to do anything with all cluster-related resources in the destination tenancy:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group OKE-Admins as ocid1.group.oc1..<unique_ID>
Admit group OKE-Admins of tenancy SourceTenancy to manage cluster-family in tenancy
```

To enable the source IAM group to create clusters in the destination tenancy, the destination administrator must also create policy statements to admit the group to manage virtual networks and inspect compartments in the destination tenancy. For example:
Copy
```
Admit group OKE-Admins of tenancy SourceTenancy to manage virtual-network-family in tenancy
Admit group OKE-Admins of tenancy SourceTenancy to inspect compartments in tenancy
```

Here is an example of policy statements that endorse the IAM group OKE-Admins in the source tenancy to manage cluster-related resources only in the SharedOKEClusters compartment:
Copy
```
Define tenancy SourceTenancy as ocid1.tenancy.oc1..<unique_ID>
Define group OKE-Admins as ocid1.group.oc1..<unique_ID>
Admit group OKE-Admins of tenancy SourceTenancy to manage cluster-family in compartment SharedOKEClusters
```

## Accessing Custom Images in other Tenancies When Creating or Updating Managed Node Pools 🔗 
When using the CLI or API to create or update a managed node pool, you specify the OCID of the image that Kubernetes Engine uses to provision managed nodes in the node pool. If you specify the OCID of a custom image, the custom image can be in the same tenancy as the cluster, or in a different tenancy. If the custom image is in a different tenancy, policies must exist to enable access to the other tenancy to read the image.
In the tenancy (the source tenancy) containing the cluster with the managed node pool that you want Kubernetes Engine to provision using a custom image, the source administrator must create policy statements to endorse access to the custom image in the destination tenancy. For example:
Copy
```
Define tenancy image-tenancy as ocid1.tenancy.oc1...<unique_ID>
Endorse any-user to {INSTANCE_IMAGE_INSPECT, INSTANCE_IMAGE_READ} in tenancy image-tenancy where request.principal.type = 'nodepool'
```

In the tenancy containing the custom image (the destination tenancy), the destination administrator must create policy statements to admit access from the source tenancy to the custom image. For example:
Copy
```
Define tenancy nodepool-tenancy as ocid1.tenancy.oc1...<unique_ID>
Admit any-user of tenancy nodepool-tenancy to {INSTANCE_IMAGE_INSPECT, INSTANCE_IMAGE_READ} where request.principal.type = 'nodepool'
```

Was this article helpful?
YesNo

