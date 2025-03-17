Updated 2024-12-16
# Tenancy Administrator Tasks
Learn about the set of tasks you perform in the OCI tenancy to enable the OKE service on Compute Cloud@Customer.
**Note**
At least three available public IP addresses are required to use OKE on Compute Cloud@Customer. See [Public IP Address Requirements](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/container-engine-for-kubernetes.htm#container-engine-for-kubernetes__public-ip-requirements).
## Tenancy Administrator Tasks 🔗 
Perform the following one-time administrative tasks to configure OKE for use on Compute Cloud@Customer. 
These administrative tasks involve configuring IAM groups, policies, and a tag namespace with key definitions in the OCI tenancy that's associated with Compute Cloud@Customer. If you don't have tenancy administration privileges, work with your tenancy administrator.
**Note** After you complete these tasks, it can take up to 15 minutes for the IAM changes to synchronize on the Compute Cloud@Customer infrastructure.
No. | Tasks  
---|---  
1. |  [Ensure Platform Images with OKE are Available](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/ensure-platform-images-with-oke-are-available.htm#ensure-platform-images-with-oke-are-available "Compute Cloud@Customer includes platform images that have OKE installed on them. Ensure that you have access to them.")  
2. |  [Create the OraclePCA-OKE.cluster_id Tag](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm#creating_the_oraclepca_oke_cluster_id_tag "The OraclePCA-OKE.cluster_id defined tag consists of an OraclePCA-OKE tag namespace with a cluster_id tag. This defined tag is required to create or update an OKE cluster or node pool. When you create a node pool, or update the node pool to add nodes, this tag is applied to every node to identify instances that need to be members of the dynamic group.")  
3. |  [Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.")  
4. |  [Create a User Group and Policies for OKE Users](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-user-group-and-policies-that-authorize-members-to-use-oke.htm#create-a-user-group-and-policies-that-authorize-members-to-use-oke "In your OCI tenancy that's associated with Compute Cloud@Customer, create a user group and policies that authorize users to use OKE.")  
5. |  Create a Dynamic Group and policies. Use one of the following procedures:
  * [Create a Dynamic Group and Policies (Using the Oracle Cloud Console)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group.htm#create-a-dynamic-group "In your OCI tenancy that's associated with Compute Cloud@Customer, create a dynamic group and policies to authorize member instances to manage OKE resources.")
  * [Example Terraform Scripts for Creating Dynamic Groups and Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group-using-terraform-scripts.htm#create-a-dynamic-group-using-terraform-scripts "You can use Terraform scripts to automate the creation of a dynamic group and policies to authorize member instances to manage OKE resources.")

  
6. |  Understand how [Certificate Authority Bundles](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-the-certificate-authority-bundle.htm#updating-the-certificate-authority-bundle "The Certificate Authority \(CA\) bundle for Compute Cloud@Customer is downloaded and made available to a cluster when the cluster is created. The CA bundle includes the certificate, private and public keys, and other authorization information.") are handled for OKE.  
Was this article helpful?
YesNo

