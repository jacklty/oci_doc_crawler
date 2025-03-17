Updated 2024-12-16
# Example Terraform Scripts for Creating Dynamic Groups and Policies
You can use Terraform scripts to automate the creation of a dynamic group and policies to authorize member instances to manage OKE resources. 
This section provides examples of Terraform scripts you can use to create the group and policies. Or, you can create the group and policies [using the Oracle Cloud Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group.htm#create-a-dynamic-group "In your OCI tenancy that's associated with Compute Cloud@Customer, create a dynamic group and policies to authorize member instances to manage OKE resources."). 
**variables.tf**
Copy
```
variable "oci_config_file_profile" {
 type  = string
 default = "DEFAULT"
}
variable "tenancy_ocid" {
  description = "tenancy OCID"
  type    = string
  nullable  = false
}
variable "oke_dyn_grp" {
  description = "Dynamic group that needs to be created for instance principal"
  default = "oke-dyn-ip-grp"
}
variable "oke_policy_name" {
  description = "Policy set name for dynamic group"
  default = "oke-instance-principal-policy"
}
```

**terraform.tfvars**
Copy
```
# Name of the profile to use from $HOME/.oci/config
oci_config_file_profile = "DEFAULT"
# Tenancy OCID from the oci_config_file_profile profile.
tenancy_ocid = "ocid1.tenancy.UNIQUE_ID"
# Dynamic Group Name
oke_dyn_grp = "oke-dyn-ip-group"
# OKE Dynamic Group Policy Name
oke_policy_name = "oke-dyn-grp-policy"
```

**provider.tf**
Copy
```
provider "oci" {
 config_file_profile = var.oci_config_file_profile
 tenancy_ocid    = var.tenancy_ocid
}
```

**main.tf**
Copy
```
terraform {
 required_providers {
  oci = {
   source = "oracle/oci"
   version = ">= 4.50.0"
   # If necessary, you can pin a specific version here
   #version = "4.71.0"
  }
 }
 required_version = ">= 1.1"
}
```

**oke-dyn-grp.tf**
Copy
```
resource "oci_identity_dynamic_group" "oke-dynamic-grp" {
  compartment_id = "${var.tenancy_ocid}"
  description  = "PCA OKE worker dynamic group for instance principal"
  matching_rule = "tag.${oci_identity_tag_namespace.oracle-pca.name}.${oci_identity_tag.cluster-id.name}.value"
  name      = "${var.oke_dyn_grp}"
  depends_on = [oci_identity_tag.cluster-id]
}
```

**oke-policy.tf**
Copy
```
resource "oci_identity_policy" "oke-dyn-grp-policy" {
  compartment_id = "${var.tenancy_ocid}"
  description  = "Dynamic group policies for OKE Resources"
  name      = "${var.oke_policy_name}"
  statements   = [
    "allow dynamic-group ${oci_identity_dynamic_group.oke-dynamic-grp.name} to use instance-family in tenancy",
    "allow dynamic-group ${oci_identity_dynamic_group.oke-dynamic-grp.name} to use virtual-network-family in tenancy"
    "allow dynamic-group ${oci_identity_dynamic_group.oke-dynamic-grp.name} to manage load-balancers in tenancy",
    "allow dynamic-group ${oci_identity_dynamic_group.oke-dynamic-grp.name} to manage volume-family in tenancy",
    "allow dynamic-group ${oci_identity_dynamic_group.oke-dynamic-grp.name} to manage file-family in tenancy",
  ]
  depends_on = [oci_identity_dynamic_group.oke-dynamic-grp]
}
```

**oke-tag-ns.tf**
This script creates the `OraclePCA-OKE.cluster_id` tag, which is also described in [Create the OraclePCA-OKE.cluster_id Tag](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm#creating_the_oraclepca_oke_cluster_id_tag "The OraclePCA-OKE.cluster_id defined tag consists of an OraclePCA-OKE tag namespace with a cluster_id tag. This defined tag is required to create or update an OKE cluster or node pool. When you create a node pool, or update the node pool to add nodes, this tag is applied to every node to identify instances that need to be members of the dynamic group.").
Copy
```
resource "oci_identity_tag" "cluster-id" {
  description   = "Default tag key definition"
  name       = "cluster_id"
  tag_namespace_id = "${oci_identity_tag_namespace.oracle-pca.id}"
  depends_on = [oci_identity_tag_namespace.oracle-pca]
}
resource "oci_identity_tag_namespace" "oracle-pca" {
  compartment_id = "${var.tenancy_ocid}"
  description  = "Default Tag namespace for Oracle PCA OKE"
  name      = "OraclePCA-OKE"
}
```

The OKE service is now ready for OKE users to manage OKE resources. To get started, see [Cluster Administrator Tasks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/user-tasks.htm#user-tasks "Perform a set of tasks to create OKE clusters on Compute Cloud@Customer.").
To learn how certificate authority bundles are handled, see [Certificate Authority Bundles](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-the-certificate-authority-bundle.htm#updating-the-certificate-authority-bundle "The Certificate Authority \(CA\) bundle for Compute Cloud@Customer is downloaded and made available to a cluster when the cluster is created. The CA bundle includes the certificate, private and public keys, and other authorization information.").
Was this article helpful?
YesNo

