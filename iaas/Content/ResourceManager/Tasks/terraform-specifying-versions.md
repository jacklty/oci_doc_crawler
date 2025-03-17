Updated 2024-10-04
# Specifying Versions
Specify and pin versions of the OCI Terraform provider and modules for use with Resource Manager.
Terraform, the Oracle Cloud Infrastructure (OCI) Terraform provider, and Terraform modules you call in your configuration files all introduce changes or add new functionality periodically. As these changes are made, new versions are released.
To ensure that your configurations are applied consistently to OCI resources, you can explicitly set the version of these components in Terraform configuration files.
## Provider Version 🔗 
You can control the version of the OCI Terraform provider that Terraform uses when interacting with OCI resources. This ability is especially helpful when your configuration relies on features introduced with a particular version of the provider or it has only been tested with a particular version of the provider.
You can use the `>=` or `=` operators to specify the version, depending on your use case.
For more information, see [Specifying Provider Requirements](https://developer.hashicorp.com/terraform/language/settings#specifying-provider-requirements).
### Using Terraform v0.12 or earlier
Terraform v0.12 or earlier allowed you to specify `version` within the `provider` block. For example:
```
provider "oci" {
  version     = ">= 3.27.0"
  region      = "${var.region}"
  …
}
```

### Using Terraform v0.13
Terraform v0.13 deprecated `version` within `provider` blocks. Instead, versions should be specified within a `required_providers` block. For example:
```
terraform {
  required_providers {
    oci = {
      source = "hashicorp/oci"
      version = ">= 4.0.0"
    }
  }
  ...
}
```

## Module Version 🔗 
In addition to specifying the version of the Terraform CLI and the OCI Terraform provider, you can also specify the version of Terraform modules.
If a module has been upgraded to use a newer version of Terraform core, but you still use an earlier version of Terraform, you can specify a compatible version of the module. If your configurations have only been tested with a specific version of the module, you can specify that version to ensure compatibility.
Modules accept the `version` argument. For example:
```
module "oke" {
  source = "oracle-terraform-modules/oke/oci"
  version = "1.0.0"
  # insert required variables here
}
```

For more information, see [Module Blocks](https://developer.hashicorp.com/terraform/language/modules/syntax).
Was this article helpful?
YesNo

