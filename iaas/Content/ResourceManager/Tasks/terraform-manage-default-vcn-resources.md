Updated 2024-04-29
# Managing Default VCN Resources
Use Resource Manager and Terraform configurations to manage default VCN resources.
When you create an `oci_core_vcn` resource, it will also create the following associated resources by default:
  * `oci_core_security_list`
  * `oci_core_dhcp_options`
  * `oci_core_route_table`


These default resources will be implicitly created even if they are not specified in the Terraform configuration. Their OCIDs are returned by the following attributes under the `oci_core_vcn` resource:
  * `default_security_list_id`
  * `default_dhcp_options_id`
  * `default_route_table_id`


Default resources must be configured in Terraform using a separate resource type. Here are the mappings between the resource and the new resource type to use for configuring default resources:
  * `oci_core_security_list` => `oci_core_default_security_list`
  * `oci_core_dhcp_options` => `oci_core_default_dhcp_options`
  * `oci_core_route_table` => `oci_core_default_route_table`


Default resources types are configured in the same way as their non-default counterparts. The only difference is specifying the ID of the default resource using the `manage_default_resource_id` argument.
Consequently, the `vcn_id` is no longer necessary for default resources.
The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at [docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/) and [Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs).
Data sources and resources are grouped by service within the reference.
The following example modifies a VCN's default route table and DHCP options:
```
resource "oci_core_vcn" "vcn1" {
 cidr_block = "10.0.0.0/16"
 dns_label = "vcn1"
 compartment_id = var.compartment_id
 display_name = "vcn1"
}
# Gateway
## Internet Gateway
resource "oci_core_internet_gateway" "inetGw" {
  compartment_id = var.compartment_id
  display_name  = "inetGw"
  vcn_id     = oci_core_vcn.vcn1.id
}
resource "oci_core_default_dhcp_options" "default-dhcp-options" {
 manage_default_resource_id = oci_core_vcn.vcn1.default_dhcp_options_id
 #Required
 options {
  type = "DomainNameServer"
  server_type = "VcnLocalPlusInternet"
 }
}
 #Optional
 options {
  type = "SearchDomain"
  search_domain_names = [ "abc.com" ]
 }
}
resource "oci_core_default_route_table" "default-route-table" {
 manage_default_resource_id = oci_core_vcn.vcn1.default_route_table_id
  #Required
  compartment_id = var.compartment_id
  #Optional
  display_name = "default_route_table"
  route_rules {
    #Required
    network_entity_id = oci_core_internet_gateway.inetGw.id
    #Optional
    destination = "0.0.0.0/0"
    destination_type = "CIDR_BLOCK"
  }
}
```

## Limitations 🔗 
Default resources can only be removed when the associated `oci_core_vcn` resource is removed. When attempting a targeted removal of a default resource, the resource will be removed from the Terraform state file but the resource may still exist in OCI with empty settings.
Examples of targeted removal include:
  * Removing a default resource from a Terraform configuration that was previously applied
  * Running a `terraform destroy -target=<default resource>` command
  * Changing the `manage_default_resource_id` for a default resource that was previously applied


Was this article helpful?
YesNo

