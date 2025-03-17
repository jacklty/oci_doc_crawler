Updated 2024-12-16
# Example Terraform Scripts for Network Resources
On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.
You can use the following Terraform scripts in your Terraform environment to automate the creation of the network resources that are required by OKE. For detailed information about Terraform, see [Terraform](https://www.terraform.io/). (Alternatively, you can create the network resources individually. See [Configuring OKE Network Resources Individually](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/configuring-network-resources-individually.htm#configuring-network-resources-individually "On Compute Cloud@Customer, you can create the required OKE network resources individually using the Compute Cloud@Customer Console, CLI, or API."))
Most of the values shown in these scripts, such as resource display names and CIDRs, are examples. Some ports must be specified as shown (see [Workload Cluster Network Ports](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-network-ports.htm#oke-network-ports "Learn about the required ports for OKE on Compute Cloud@Customer.")), and the OKE control plane subnet must be named `control-plane`. See [Workload Cluster Network CIDR Ranges](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/workload-cluster-network-cidr-ranges.htm#workload-cluster-network-cidr-ranges "Review the example CIDR ranges used for OKE network resources on Compute Cloud@Customer.") for comments about CIDR values.
**Terraform Script Examples**
  * [variables.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__variables-tf)
  * [terraform.tfvars](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__tf_vars_sample)
  * [provider.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__provider-tf)
  * [main.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__tf_main)
  * [oke_vcn.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__oke_vcn-tf)
  * [oke_worker_seclist.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__oke_worker_seclist-tf)
  * [oke_worker_subnet.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__oke_worker_subnet-tf)
  * [oke_kmi_seclist.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__oke_kmi_seclist-tf)
  * [oke_kmi_subnet.tf](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources__oke_kmi_subnet-tf)


## variables.tf 🔗 
This file creates several variables that are used to configure OKE network resources. Many of these variables aren't assigned values in this file. One port and five CIDRs are assigned values. The `kubernetes_api_port`, port 6443, is the port used to access the Kubernetes API. See also [Workload Cluster Network Ports](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-network-ports.htm#oke-network-ports "Learn about the required ports for OKE on Compute Cloud@Customer."). The five CIDRs that are defined in this file are for the OKE VCN, worker subnet, worker load balancer subnet, control plane subnet, and control plane load balancer subnet.
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
variable "compartment_id" {
 description = "compartment OCID"
 type    = string
 nullable  = false
}
variable "vcn_name" {
 description = "VCN name"
 nullable  = false
}
variable "kube_client_cidr" {
 description = "CIDR of Kubernetes API clients"
 type    = string
 nullable  = false
}
variable "kubernetes_api_port" {
 description = "port used for kubernetes API"
 type    = string
 default   = "6443"
}
variable "worker_lb_ingress_rules" {
 description = "traffic allowed to worker load balancer"
 type = list(object({
  source  = string
  port_min = string
  port_max = string
 }))
 nullable = false
}
variable "worker_ingress_rules" {
 description = "traffic allowed directly to workers"
 type = list(object({
  source  = string
  port_min = string
  port_max = string
 }))
 nullable = true
}
#
# IP network addressing
#
variable "vcn_cidr" {
 default = "172.31.252.0/23"
}
# Subnet for KMIs where kube-apiserver and other control
# plane applications run
variable "kmi_cidr" {
 description = "K8s control plane subnet CIDR"
 default   = "172.31.252.224/28"
}
# Subnet for KMI load balancer 
variable "kmilb_cidr" {
 description = "K8s control plane LB subnet CIDR"
 default   = "172.31.252.240/28"
}
# Subnet for worker nodes, max 128 nodes
variable "worker_cidr" {
 description = "K8s worker subnet CIDR"
 default   = "172.31.253.0/24"
}
# Subnet for worker load balancer (for use by CCM)
variable "workerlb_cidr" {
 description = "K8s worker LB subnet CIDR"
 default   = "172.31.252.0/25"
}
```

## terraform.tfvars 🔗 
This file assigns values to some of the variables that were created in `variables.tf`. It also defines security list rules for accessing the worker nodes and the worker load balancer.
Copy
```
# Name of the profile to use from $HOME/.oci/config
oci_config_file_profile = "DEFAULT"
# Tenancy OCID from the oci_config_file_profile profile.
tenancy_ocid = "ocid1.tenancy.unique_ID"
# Compartment in which to build the OKE cluster.
compartment_id = "ocid1.compartment.unique_ID"
# Display name for the OKE VCN.
vcn_name = "oketest"
# CIDR of clients that are allowed to contact Kubernetes API server.
kube_client_cidr = "10.0.0.0/8"
# Security list rules for who is allowed to contact the worker load balancer.
# Adjust these values for your applications.
worker_lb_ingress_rules = [
 {
  source  = "10.0.0.0/8"
  port_min = 80
  port_max = 80
 },
 {
  source  = "10.0.0.0/8"
  port_min = 443
  port_max = 443
 },
]
# Security list rules for who is allowed to contact worker nodes directly.
# This example allows 10.0.0.0/8 to contact the default nodeport range.
worker_ingress_rules = [
 {
  source  = "10.0.0.0/8"
  port_min = 30000
  port_max = 32767
 },
]
```

## provider.tf 🔗 
This file is required to use the OCI provider. The file initializes the OCI module using the OCI profile configuration file.
Copy
```
provider "oci" {
 config_file_profile = var.oci_config_file_profile
 tenancy_ocid    = var.tenancy_ocid
}
```

## main.tf 🔗 
This file specifies the provider to use (`oracle/oci`), defines several security list rules, and initializes required local variables.
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
locals {
 kube_internal_cidr = "253.255.0.0/16"
 worker_lb_ingress_rules = var.worker_lb_ingress_rules
 worker_ingress_rules = flatten([var.worker_ingress_rules, [
  {
   source  = var.vcn_cidr
   port_min = 22
   port_max = 22
  },
  {
   source  = var.kube_client_cidr
   port_min = 30000
   port_max = 32767
  },
  {
   source  = var.workerlb_cidr
   port_min = 30000
   port_max = 32767
  },
  {
   source  = var.workerlb_cidr
   port_min = 10256
   port_max = 10256
  },
  {
   source  = var.kmi_cidr
   port_min = 22
   port_max = 65535
  },
 ]])
 worker_ingress_udp_rules = [
  {
   source  = var.worker_cidr
   port_min = 8285
   port_max = 8472
  },
  {
   source  = var.kmi_cidr
   port_min = 8285
   port_max = 8472
  },
 ]
 kmi_lb_ingress_rules = [
  {
   source  = local.kube_internal_cidr
   port_min = var.kubernetes_api_port
   port_max = var.kubernetes_api_port
  },
  {
   source  = var.kube_client_cidr
   port_min = var.kubernetes_api_port
   port_max = var.kubernetes_api_port
  },
  {
   source  = var.vcn_cidr
   port_min = var.kubernetes_api_port
   port_max = var.kubernetes_api_port
  },
 ]
 kmi_ingress_rules = [
  {
   source  = var.kube_client_cidr
   port_min = var.kubernetes_api_port
   port_max = var.kubernetes_api_port
  },
  {
   source  = var.kmilb_cidr
   port_min = var.kubernetes_api_port
   port_max = var.kubernetes_api_port
  },
  {
   source  = var.worker_cidr
   port_min = 1024
   port_max = 65535
  },
  {
   source  = var.kmi_cidr
   port_min = 1024
   port_max = 65535
  },
 ]
 kmi_ingress_udp_rules = [
  {
   source  = var.worker_cidr
   port_min = 8285
   port_max = 8472
  },
  {
   source  = var.kmi_cidr
   port_min = 8285
   port_max = 8472
  },
 ]
}
```

## oke_vcn.tf 🔗 
This file defines a VCN, NAT gateway, internet gateway, private route table, and public route table. The private route table is the default route table for the VCN. 
Copy
```
resource "oci_core_vcn" "oke_vcn" {
 cidr_block   = var.vcn_cidr
 dns_label   = var.vcn_name
 compartment_id = var.compartment_id
 display_name  = "${var.vcn_name}-vcn"
}
resource "oci_core_nat_gateway" "vcn_ngs" {
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name = "VCN nat g6s"
}
resource "oci_core_internet_gateway" "vcn_igs" {
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name = "VCN i6t g6s"
 enabled   = true
}
resource "oci_core_default_route_table" "private" {
 manage_default_resource_id = oci_core_vcn.oke_vcn.default_route_table_id
 display_name        = "Default - private"
 route_rules {
  destination    = "0.0.0.0/0"
  destination_type = "CIDR_BLOCK"
  network_entity_id = oci_core_nat_gateway.vcn_ngs.id
 }
}
resource "oci_core_route_table" "public" {
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name = "public"
 route_rules {
  destination    = "0.0.0.0/0"
  destination_type = "CIDR_BLOCK"
  network_entity_id = oci_core_internet_gateway.vcn_igs.id
 }
}
```

## oke_worker_seclist.tf 🔗 
This file defines the security lists for both the worker subnet and the worker load balancer subnet. The rules for these security lists were defined in other Terraform files in this set.
Copy
```
resource "oci_core_security_list" "workerlb" {
 display_name  = "${var.vcn_name}-workerlb"
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.worker_lb_ingress_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "6"
   tcp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
}
resource "oci_core_security_list" "worker" {
 display_name  = "${var.vcn_name}-worker"
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.worker_ingress_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "6"
   tcp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.worker_ingress_udp_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "17"
   udp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
}
```

## oke_worker_subnet.tf 🔗 
This file defines the worker and worker load balancer subnets. The worker load balancer subnet is named `service-lb`.
Copy
```
resource "oci_core_subnet" "worker" {
 cidr_block   = var.worker_cidr
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name        = "worker"
 dns_label         = "worker"
 prohibit_public_ip_on_vnic = true
 security_list_ids = [
  oci_core_default_security_list.oke_vcn.id,
  oci_core_security_list.worker.id
 ]
}
resource "oci_core_subnet" "worker_lb" {
 cidr_block   = var.workerlb_cidr
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name        = "service-lb"
 dns_label         = "servicelb"
 prohibit_public_ip_on_vnic = false
 route_table_id       = oci_core_route_table.public.id
 security_list_ids = [
  oci_core_default_security_list.oke_vcn.id,
  oci_core_security_list.workerlb.id
 ]
}
```

## oke_kmi_seclist.tf 🔗 
This file defines the security lists for the control plane and control plane load balancer subnets. This file also defines updates to make to the default security list for the VCN.
Copy
```
resource "oci_core_default_security_list" "oke_vcn" {
 manage_default_resource_id = oci_core_vcn.oke_vcn.default_security_list_id
 egress_security_rules {
  destination   = "0.0.0.0/0"
  destination_type = "CIDR_BLOCK"
  protocol     = "all"
 }
 dynamic "ingress_security_rules" {
  iterator = icmp_type
  for_each = [3, 8, 11]
  content {
   # ping from VCN; unreachable/TTL from anywhere
   source   = (icmp_type.value == "8" ? var.vcn_cidr : "0.0.0.0/0")
   source_type = "CIDR_BLOCK"
   protocol  = "1"
   icmp_options {
    type = icmp_type.value
   }
  }
 }
}
resource "oci_core_security_list" "kmilb" {
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name = "${var.vcn_name}-kmilb"
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.kmi_lb_ingress_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "6"
   tcp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
}
resource "oci_core_security_list" "kmi" {
 compartment_id = var.compartment_id
 vcn_id     = oci_core_vcn.oke_vcn.id
 display_name = "${var.vcn_name}-kmi"
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.kmi_ingress_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "6"
   tcp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
 dynamic "ingress_security_rules" {
  iterator = port
  for_each = local.kmi_ingress_udp_rules
  content {
   source   = port.value.source
   source_type = "CIDR_BLOCK"
   protocol  = "17"
   udp_options {
    min = port.value.port_min
    max = port.value.port_max
   }
  }
 }
}
```

## oke_kmi_subnet.tf 🔗 
This file defines the control plane and control plane load balancer subnets.
**Important**
The name of the `kmi` subnet must be exactly `control-plane`.
Copy
```
resource "oci_core_subnet" "kmi" {
 cidr_block         = var.kmi_cidr
 compartment_id       = var.compartment_id
 display_name        = "control-plane"
 dns_label         = "kmi"
 vcn_id           = oci_core_vcn.oke_vcn.id
 prohibit_public_ip_on_vnic = true
 security_list_ids = [
  oci_core_default_security_list.oke_vcn.id,
  oci_core_security_list.kmi.id
 ]
}
resource "oci_core_subnet" "kmi_lb" {
 cidr_block         = var.kmilb_cidr
 compartment_id       = var.compartment_id
 dns_label         = "kmilb"
 vcn_id           = oci_core_vcn.oke_vcn.id
 display_name        = "control-plane-endpoint"
 prohibit_public_ip_on_vnic = false
 route_table_id       = oci_core_route_table.public.id
 security_list_ids = [
  oci_core_default_security_list.oke_vcn.id,
  oci_core_security_list.kmilb.id
 ]
}
```

Was this article helpful?
YesNo

