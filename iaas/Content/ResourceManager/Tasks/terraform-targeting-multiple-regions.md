Updated 2024-04-29
# Targeting Multiple Regions
Use a single Terraform configuration to create Oracle Cloud Infrastructure (OCI) resources in multiple regions.
## Create a Provider for Each Region 🔗 
A Terraform configuration may have only a single OCI Terraform provider block, but to apply configurations to multiple regions, you need to create multiple provider blocks.
A typical OCI Terraform provider block might look like the following:
Copy
```
provider "oci" {
 region      = var.region
 tenancy_ocid   = var.tenancy_ocid
 user_ocid    = var.user_ocid
 fingerprint   = var.fingerprint
 private_key_path = var.private_key_path
}
```

**Tip** All parameters should be set using variables.
If you want to use more than one region within a single Terraform config, multiple providers are required. Each provider must be given an alias. For example:
Copy
```
provider "oci" {
 **alias      = "home"**
 region      = var.region
 tenancy_ocid   = var.tenancy_ocid
 user_ocid    = var.user_ocid
 fingerprint   = var.fingerprint
 private_key_path = var.private_key_path
}
provider "oci" {
 **alias      = "region2"**
 region      = var.region2
 tenancy_ocid   = var.tenancy_ocid
 user_ocid    = var.user_ocid
 fingerprint   = var.fingerprint
 private_key_path = var.private_key_path
}
```

When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one region, which is your _home region_. The home region has special properties. For example, IAM resources can only be created in your home region. For that reason, you should designate that region with an appropriate alias, like `home`. Use simple aliases for other regions so that users can easily map configurations to the regions that they want (for example, `region2`).
**Note** Specific regions (us-phoenix-1, us-ashburn-1, and so on) are not hardcoded into either the `region` or `alias` fields.
## Provision a Resource 🔗 
To provision a resource in a region, specify the aliased provider name in the resource.
For example:
```
resource "oci_core_instance" "test_instance" {
 provider = oci.home
 ...
}
```

## Modules and Multiple Regions 🔗 
Typically, a module should use only a single region. If more regions are needed, you should use separate modules.
If the config contains multiple providers, the module should specify the provider to use by using the following format:
```
module "compartments" {
 source    = "./compartments"
 providers = {
  oci = "oci.home"
 }
}
```

Was this article helpful?
YesNo

