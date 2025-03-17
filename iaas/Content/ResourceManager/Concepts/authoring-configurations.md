Updated 2024-08-14
# Authoring Configurations
Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format (HCL).
Using Terraform, you can describe infrastructure resources using the HashiCorp Configuration Language format (HCL) in Terraform configuration files (see [Configuration Syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration)). Terraform configuration files can use either of two formats: Terraform domain-specific language (HashiCorp Configuration Language format [HCL]), which is the recommended approach, or JSON format if the files need to be machine-readable. Configuration files that use the HCL format end with the `.tf` file extension; those using JSON format end with the `.tf.json` file extension. The Terraform format is human-readable, while the JSON format is machine readable.
Use Terraform configurations to define Oracle Cloud Infrastructure (OCI) resources, variable definitions, data sources, and a great deal more. Terraform, then, converts the OCI configurations into a set of API calls against OCI API endpoints. The key to writing Terraform configuration is understanding how to abstract the wanted infrastructure conceptually into [Configuration Syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration).
**Important** While the Oracle Cloud Infrastructure API uses camelCase extensively, Terraform doesn't support camelCase in configuration files. For this reason, in the configurations you see underscores rather than capitalization as separators. For example, where the API uses `availabilityDomain`, the Terraform configuration uses `availability_domain`.
## Configuration File Requirements 🔗 
Terraform configuration (`.tf`) files have specific requirements, depending on the components that are defined in the file. For example, you might have Terraform provider defined in one file (`provider.tf`), variables defined in another (`variables.tf`), and data sources defined in yet another.
**Note** For example configuration files, see [Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples).
### Provider Definitions 🔗 
**Note** For third-party providers in Terraform configurations used with Resource Manager, see [Third-party Provider Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers "Reference third-party Terraform providers in Terraform configurations used with Resource Manager.").
The following example using Terraform syntax illustrates the requirements for an OCI Terraform provider definition, and also shows associated variable definitions. The provider definition relies on variables so that the configuration file itself doesn't contain sensitive data. Including sensitive data creates a security risk when exchanging or sharing configuration files.
```
variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "region" {}
provider "oci" {
  tenancy_ocid = "${var.tenancy_ocid}"
  user_ocid = "${var.user_ocid}"
  fingerprint = "${var.fingerprint}"
  private_key_path = "${var.private_key_path}"
  region = "${var.region}"
}
```

The `region` attribute specifies the geographical region in which your provider resources are created. To target multiple regions in a single configuration, you simply create a provider definition for each region and then differentiate by using a provider alias, as shown in the following example. Notice that only one provider, named `oci` is defined, and yet the `oci` provider definition is entered twice, once for the `us-phoenix-1` region (with the alias `phx`), and once for the region `us-ashburn-1` (with the alias "iad").
```
variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "compartment_ocid" {}
provider "oci" {
  region = "us-phoenix-1"
  alias = "phx"
  tenancy_ocid = "${var.tenancy_ocid}"
  user_ocid = "${var.user_ocid}"
  fingerprint = "${var.fingerprint}"
  private_key_path = "${var.private_key_path}"
}
provider "oci" {
  region = "us-ashburn-1"
  alias = "iad"
  tenancy_ocid = "${var.tenancy_ocid}"
  user_ocid = "${var.user_ocid}"
  fingerprint = "${var.fingerprint}"
  private_key_path = "${var.private_key_path}"
}
```

For more information, see [Provider Configuration](https://developer.hashicorp.com/terraform/language/providers/configuration).
### Variable Definitions 🔗 
**Note**
In Resource Manager, variables are subject to the following [limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Resource_Manager_Limits).
Variables per stack: 250
Size per variable: 8192 bytes
Variables in Terraform represent parameters for Terraform modules. In variable definitions, each block configures a single input variable, and each definition can take any or all of the following optional arguments: 
  * `type` (optional): Defines the variable type as one of three allowed values: `string`, `list`, and `map`. If this argument isn't used, the variable type is inferred based on `default`. If no `default` is provided, the type is assumed to be `string`.
  * `default` (optional): Sets the default value for the variable. If no default value is provided, the caller must provide a value or Terraform throws an error.
  * `description` (optional): A human-readable description of the variable.


Following are examples of several variable definitions. Some definitions include optional parameters.
```
variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "region" {}
variable "AD" {
  default   = "1"
  description = "Availability Domain"
}
variable "CPUCoreCount" {
  default = "2"
  type  = string
}
```

For more information, see [Input Variables](https://developer.hashicorp.com/terraform/language/values/variables).
### Output Configuration 🔗 
Output variables provide a means to support Terraform end-user queries. Use output variables to extract meaningful data from among the potentially massive amount of data associated with a complex infrastructure. For example, you might be interested only in a handful of key values at any particular time and defining output variables lets you extract exactly the information that you need.
Following is a simple example in which only a few output variables (instance IP addresses and boot volume IDs) are defined:
```
# Output the private and public IPs of the instance
output "InstancePrivateIPs" {
value = ["${oci_core_instance.TFInstance.*.private_ip}"]
}
output "InstancePublicIPs" {
value = ["${oci_core_instance.TFInstance.*.public_ip}"]
}
# Output the boot volume IDs of the instance
output "BootVolumeIDs" {
 value = ["${oci_core_instance.TFInstance.*.boot_volume_id}"]
}
```

For more information, see [Output data from Terraform](https://developer.hashicorp.com/terraform/tutorials/configuration-language/outputs). See also [Output Values](https://developer.hashicorp.com/terraform/language/values/outputs).
### Resources 🔗 
Resources are components of Oracle Cloud Infrastructure. These resources include everything from low-level components such as physical and virtual servers, to higher-level components such as email and database providers, your DNS record.
The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at [docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/) and [Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs).
Data sources and resources are grouped by service within the reference.
**Caution** Terraform state files contain all resource attributes that are specified as part of configuration files. If you manage any sensitive data with Terraform, such as database or user passwords or instance private keys, we recommend that you treat the state file itself as sensitive data. See [Sensitive Data in State](https://developer.hashicorp.com/terraform/language/state/sensitive-data) for more information.
#### Declaring Resources
Following is a simple example of a resource definition that illustrates their basic structure.
```
resource "oci_core_virtual_network" "vcn1" {
  cidr_block = "10.0.0.0/16"
  dns_label = "vcn1"
  compartment_id = "${var.compartment_ocid}"
  display_name = "vcn1"
}
```

The resource declaration on the first line of the example uses the keyword "resource" and takes two parameters, resource `type` and resource `name` ("oci_core_virtual_network" and "vcn1" in the example). Inside the code block, then, is the resource configuration. 
For more information, see [Resources](https://developer.hashicorp.com/terraform/language/resources).
#### Resource Dependencies 🔗 
When a resource references another resource within its resource block, Terraform automatically infers the primary resource's dependency on the referenced resource. A resource might also depend on resources that aren't explicitly referenced within its block. For example, you might need to create policies for a resource before creating the resource itself.
To define hidden dependencies that Terraform can't automatically infer, you can use the [The depends_on Meta-Argument](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on) in the resource block.
The following example creates an `oci_datascience_notebook_session` resource and an `oci_identity_policy` resource for related policies. Adding the `depends_on` meta-argument to the `oci_datascience_notebook_session` resource ensures that the policies are created first:
Copy
```
resource "oci_datascience_notebook_session" "ods-notebook-session" {
 count = var.enable_ods ? var.ods_number_of_notebooks : 0
 
 #Required
 compartment_id = var.compartment_ocid
 notebook_session_configuration_details {
  #Required
  shape = var.ods_compute_shape
  subnet_id = local.private_subnet_id
 
 #Optional
 block_storage_size_in_gbs = var.ods_storage_size
 }
 project_id = oci_datascience_project.ods-project[0].id
 
 display_name = "${var.ods_notebook_name}-${count.index}"
 **depends_on = ["oci_identity_policy.ods-policy"]**
 }
resource "oci_identity_policy" "ods-policy" {
 provider = oci.home
 compartment_id = var.compartment_ocid
 description = "Data Science Policies"
 name = var.ods_policy_name
 statements = var.enable_vault ? concat(local.ods_policies , local.vault_policies) : local.ods_policies
 }
```

#### Referencing Resources in Another Stack (By Exporting Stack Output Values) 🔗 
You can reference resources that exist in other stacks. The Terraform `remote_state` data source lets you read output variables from state files. 
For example, when writing a Terraform configuration for a new web application, you can make the web application use the subnet created from the network stack, as long as the required subnet values were output in the network stack state file. In the Terraform configuration for your new web application, do the following: 
  * Pull the state file of the existing network stack into the context of the current Terraform configuration.
Pulling the state file effectively exports stack output values. For instructions on pulling the state file in Resource Manager, see [Getting a Stack's State File](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm).
  * Load the pulled state file to a data source for remote state files.
  * Populate the subnet data source in your current configuration with values from the relevant output variables of the referenced state file.
  * Optionally print the identifying information for the populated data source to confirm expected values.


**Note** In addition to permissions required for Resource Manager operations, you'll need appropriate permissions for resource types you're referencing, in the compartment that you're referencing them. In this example, you need read permissions for network resources in the compartment where they're located. 
The following Terraform configuration excerpt references a subnet in another stack:
```
# The following example assumes that the source stack (defined by `stack_id`) has output a value named `subnet_id`
# Terraform v0.12 is assumed
variable "stack_id" {}
# Pull the state file of the existing Resource Manager stack (the network stack) into this context
data "oci_resourcemanager_stack_tf_state" "stack1_tf_state" {
 stack_id  = "${var.stack_id}"
 local_path = "stack1.tfstate"
}
# Load the pulled state file into a remote state data source
data "terraform_remote_state" "external_stack_remote_state" {
 backend = "local"
 config = {
  path = "${data.oci_resourcemanager_stack_tf_state.stack1_tf_state.local_path}"
 }
}
# Populate a data source in this configuration using a value from the remote state data source
data "oci_core_subnet" "subnet1" {
 subnet_id = "${data.terraform_remote_state.external_stack_remote_state.outputs.subnet_id}"
}
# Print the values of the populated data source
output "print-subnet1" {
 value = "${data.oci_core_subnet.subnet1}"
}
```

### Data Sources 🔗 
Data sources represent read-only views of existing infrastructure intended for semantic use in Terraform configurations. Following is a simple example of a data source configuration to illustrate its basic structure:
```
# Gets a list of Availability Domains
data "oci_identity_availability_domains" "ADs" {
 compartment_id = "${var.tenancy_ocid}"
}
# Get DB node list
data "oci_database_db_nodes" "DBNodeList" {
 compartment_id = "${var.compartment_ocid}"
 db_system_id = "${oci_database_db_system.TFDBNode.id}"
}
# Get DB node details
data "oci_database_db_node" "DBNodeDetails" {
 db_node_id = "${lookup(data.oci_database_db_nodes.DBNodeList.db_nodes[0], "id")}"
}
# Gets the OCID of the first (default) vNIC
data "oci_core_vnic" "DBNodeVnic" {
 vnic_id = "${data.oci_database_db_node.DBNodeDetails.vnic_id}"
}
```

For more information, see [Data Sources](https://developer.hashicorp.com/terraform/language/data-sources).
#### Filtering Data Sources 🔗 
Data sources that return lists of resources support filtering semantics. To use a filter, include this block in your data source definition:
```
filter {
  name = ""
  values = [""]
}
```

The `name` value corresponds to the qualified property name to filter with and the `values` lists can contain one or more values filter with. 
Nested properties and map elements can be addressed by qualifying the property name with parent property name. Example `r1` gives all the instances that have `source_type` image. Example `r2` gives all the instances that contain a defined tag with value "42" for key `CostCenter` in the namespace `Operations`.
```
data "oci_core_instances" "r1" {
 ...
 filter {
  name = "source_details.source_type"
  values = ["image"]
 }
}
data "oci_core_instances" "r2" {
 ...
 filter {
  name = "defined_tags.Operations.CostCenter"
  values = ["42"]
 }
}
```

Multiple `values` work as an **OR** type filter. In the following shape example, the resulting data source would contain both VM shapes _Standard 1.1_ and _Standard 1.2_ :
```
data "oci_core_shape" "t" {
 ...
 filter {
  name = "name"
  values = ["VM.Standard1.1", "VM.Standard1.2"]
 }
}
```

Multiple filters blocks can be composed to form **AND** type comparisons. The following example returns a data source containing _running instances_ in the _first AD_ of a region:
```
data "oci_core_instances" "s" {
  ...
 filter {
  name = "availability_domain"
  values = ["\\w*-AD-1"]
  regex = true
 }
 filter {
  name = "state"
  values = ["RUNNING"]
 }
}
```

As the previous examples show, filters can also employ regular expressions. Setting `regex = true` treats each item in the `values` list as a regular expression. Backslashes in strings for regular expression special characters need to be escaped with another slash, shown in the previous examples as the first `\` before `\w` in `"\\w*-AD-1"`.
**Note** Drilling into lists of structured objects isn't supported. If these properties are targeted, no results are returned from the datasource.
## Functions 🔗 
Terraform offers several built-in functions that you can use in your configuration files. These functions let you change strings, perform calculations against numeric values, manage collections, and much more.
For more information, see [Built-in Functions](https://developer.hashicorp.com/terraform/language/functions).
## For More Information 🔗 
  * [Creating Modules](https://developer.hashicorp.com/terraform/language/modules/develop)
  * [Terraform Language Documentation](https://developer.hashicorp.com/terraform/language)
  * [Configuration Syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration)


Was this article helpful?
YesNo

