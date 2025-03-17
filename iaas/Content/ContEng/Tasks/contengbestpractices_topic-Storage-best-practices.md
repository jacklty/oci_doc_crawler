Updated 2024-08-23
# Storage Best Practices
_Find out about storage best practices for clusters you've created with Kubernetes Engine (OKE)._
This section contains best practices for storage and Kubernetes Engine.
## Best Practice: Choose appropriate storage type 🔗 
We recommend that you consider the type of workload that a cluster will run before choosing a storage type that is appropriate for that workload. 
If you require a durable, scalable, and distributed enterprise-grade network file system, we recommend you use the Oracle Cloud Infrastructure File Storage service. 
If you require persistent, durable, and high-performance block storage, we recommend you use the Oracle Cloud Infrastructure Block Volume service.
## Best Practice: Create and use storage classes to define application needs 🔗 
We recommend that you define the required type of storage using Kubernetes storage classes, and then reference the storage classes in pod and deployment specifications. Storage class definitions work together to create the appropriate storage and connect it to pods.
See [Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.").
## Best Practice: Create and use volumes for persistent storage 🔗 
We recommend that you create and use persistent volumes (PVs) to store data outside of containers and prevent data loss. 
Container storage via a container's root file system is ephemeral, and can disappear upon container deletion and creation. To provide a durable location to prevent data from being lost, create and use persistent volumes to store data outside of containers.
When creating a persistent volume, the Kubernetes documentation recommends:
  * Always including persistent volume claims (PVCs) in container configurations.
  * Always defining a default storage class for a cluster, otherwise PVCs that don't specify a specific class will fail.
  * Always giving storage classes meaningful names.


See [Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.").
## Best Practice: Dynamically provision volumes 🔗 
We recommend that you dynamically provision persistent volumes (PVs) backed by the Block Volume service, rather than statically creating and assigning volumes. Dynamically provisioning volumes reduces management overhead and enables scaling.
We also recommend that you include an appropriate reclaim policy in storage class definitions to minimize unneeded storage costs when pods are deleted. 
Note that dynamic provisioning is not available for PVs backed by the File Storage service.
See [Creating a PVC on a Block Volume Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Dynamic_PV_CSI).
## Best Practice: Use the CSI volume plugin rather than the FlexVolume volume plugin 🔗 
We recommend that you use the CSI volume plugin to provision persistent volume claims on the Block Volume service, rather than the FlexVolume volume plugin.
We recommend the CSI volume plugin because:
  * New functionality is only being added to the CSI volume plugin, not to the FlexVolume volume plugin (although Kubernetes developers will continue to maintain the FlexVolume volume plugin).
  * The CSI volume plugin does not require access to underlying operating system and root file system dependencies.


The StorageClass specified for a PVC controls which volume plugin to use to connect to Block Volume service volumes. Two storage classes are defined by default, `oci-bv` for the CSI volume plugin and `oci` for the FlexVolume plugin. If you don't explicitly specify a value for `storageClassName` in the yaml file that defines the PVC, the cluster's default storage class is used.
Kubernetes Engine initially sets a cluster's default storage class according to the Kubernetes version that was specified when the cluster was created. In clusters created by Kubernetes Engine to run Kubernetes version 1.24 (or later), the `oci-bv` storage class is initially set as the default. 
See [Creating a PVC on a Block Volume Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Dynamic_PV_CSI) (and [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) in the Kubernetes documentation).
## Best Practice: Limit storage resource consumption 🔗 
We recommend that you place limits on the use of storage by containers, to reflect the amount of storage actually available in the local data center, or the budget available for Oracle Cloud storage resources.
You can limit container storage consumption by using:
  * **Resource Quotas** to limit the amount of resources (including storage, CPU, and memory) that all the containers within a Kubernetes namespace can use.
  * **StorageClasses** to limit the amount of storage provisioned to containers in response to a persistent volume claim (PVC).


See [Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.") (and [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) in the Kubernetes documentation).
## Best Practice: Secure and back up data 🔗 
We recommend that you use appropriate tools to secure and back up data. 
  * **Best Practice: Use a tool like Velero for backups.**
We recommend that you back up data using a tool like [Velero](https://velero.io/) that is appropriate for the storage type. Having taken backups, we recommend that you verify the integrity and security of those backups.
See [Velero backup for Oracle Container Engine for Kubernetes](https://blogs.oracle.com/cloud-infrastructure/post/backing-up-your-oke-environment-with-velero)
  * **Best Practice: Use a tool like Longhorn to persist and replicate data.**
We recommend that you persist and replicate data using a tool like [Longhorn](https://longhorn.io/).
See [Cross-region file replication with Longhorn in Oracle Cloud and Kubernetes](https://medium.com/oracledevs/cross-region-file-replication-with-longhorn-in-oracle-cloud-and-kubernetes-de5a5b82e4b7).
  * **Best Practice: Use a tool like Rackware SWIFT to enable backup and disaster recovery.**
We recommend that you enable backup and disaster recovery between Kubernetes clusters across regions using a tool like [Rackware SWIFT](https://www.rackwareinc.com/swift).
See [Protect your OKE Workloads with DR-as-a-Service (DRaaS) for Oracle Cloud](https://blogs.oracle.com/developers/post/protect-your-oke-workloads-with-draas-for-oracle-cloud).


## Best Practice: Use a distributed file system for ReadWriteMany use cases 🔗 
We recommend that you use a distributed file system (such as NFS, or the Oracle Cloud Infrastructure [File Storage](https://docs.oracle.com/iaas/Content/File/home.htm) service) when provisioning PVCs for ReadWriteMany use cases.
Block volume storage with high performance capabilities (such as the Oracle Cloud Infrastructure [Block Volume](https://docs.oracle.com/iaas/Content/Block/home.htm) service) is more appropriate when provisioning PVCs for single read and write use cases.
See [Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.").
Was this article helpful?
YesNo

