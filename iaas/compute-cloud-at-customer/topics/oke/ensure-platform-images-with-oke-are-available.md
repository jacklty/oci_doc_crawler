Updated 2024-12-16
# Ensure Platform Images with OKE are Available
Compute Cloud@Customer includes platform images that have OKE installed on them. Ensure that you have access to them. 
See [Listing Images and Viewing Details](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm#listing-images-and-viewing-details "On Compute Cloud@Customer, in both the Compute Cloud@Customer Console and CLI, Oracle provided images are listed first, followed by custom images."). OKE enabled images have `OKE` in the image name. Examples:
  * `uln-pca-Oracle-Linux8-OKE-1.26.6-20240210.oci`
  * `uln-pca-Oracle-Linux8-OKE-1.27.7-20240209.oci`
  * `uln-pca-Oracle-Linux8-OKE-1.28.3-20240210.oci`


**What's Next:**
[Create the OraclePCA-OKE.cluster_id Tag](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm#creating_the_oraclepca_oke_cluster_id_tag "The OraclePCA-OKE.cluster_id defined tag consists of an OraclePCA-OKE tag namespace with a cluster_id tag. This defined tag is required to create or update an OKE cluster or node pool. When you create a node pool, or update the node pool to add nodes, this tag is applied to every node to identify instances that need to be members of the dynamic group.")
Was this article helpful?
YesNo

