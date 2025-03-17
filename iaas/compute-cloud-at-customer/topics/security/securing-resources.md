Updated 2023-08-15
# Securing Compute Cloud@Customer Resources
Compute Cloud@Customer resources are the virtual cloud networking, compute instances, and storage for which your workloads reside. Securing these resources secures your workloads.
You secure Compute Cloud@Customer resources the same way you secure resources in Oracle Cloud Infrastructure, with a slight, but important difference:
  * **IAM resources** : When you create users, groups, compartments, and policies to secure resources, you configure the IAM resources in your tenancy in Oracle Cloud Infrastructure.
The IAM resources are automatically synchronized to Compute Cloud@Customer, but IAM can't be changed in Compute Cloud@Customer.
For information about managing IAM, see [IAM with Identity Domains](https://docs.oracle.com/iaas/Content/Identity/home.htm).
  * **Resource security features** : When you use security features that are part of the resource, for example, network security groups for securing networking resources, you configure the resource feature on Compute Cloud@Customer. 
The following table lists the resources that have security features that you can use to secure the resource.
Resources with Security Features | For More Information  
---|---  
Networking: VCNs and DNS | [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/iaas/Content/Security/Reference/networking_security.htm)  
Load balancers | [LBaaS Security](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/lbaas-security-overview.htm#lbaas-security-overview "On Compute Cloud@Customer, you can configure and secure the Load Balancer as a Service \(LBaaS\).")  
Compute instances | [Securing Compute](https://docs.oracle.com/iaas/Content/Security/Reference/compute_security.htm)  
Block volumes | [Securing Block Volume](https://docs.oracle.com/iaas/Content/Security/Reference/blockstorage_security.htm)  
File storage | [Securing File Storage](https://docs.oracle.com/iaas/Content/Security/Reference/filestorage_security.htm)  
Object storage | [Object Storage Security Guidelines](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/object-storage-service-security-features.htm#object-storage-service-security-features "On Compute Cloud@Customer, the Object Storage service stores and provides access to large amounts of unstructured data of any content type. Content stored in object storage can be accessed by compute instances and from the data center through the Compute Cloud@Customer domain name.")  


Was this article helpful?
YesNo

