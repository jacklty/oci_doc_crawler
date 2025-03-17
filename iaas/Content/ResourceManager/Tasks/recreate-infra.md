Updated 2024-10-08
# Recreating Infrastructure from an Existing Compartment
Using resource discovery in Resource Manager, re-create existing infrastructure from an existing compartment.
For more information about resource discovery, see [Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager.").
The following high-level instructions show how to re-create infrastructure from an existing compartment. To access detailed steps, select the provided links.
  1. [Create a stack from the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#top "Using resource discovery, create a stack in Resource Manager based on an existing compartment to generate a Terraform configuration that describes the compartment's resources.") that contains the resources you want to re-create.
  2. [Download](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#top "Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job.") the generated Terraform configuration file.
  3. Edit the `vars.tf` file (variables in the downloaded Terraform configuration file) to specify the destination `compartment_ocid` and `region`.
Example: 
Copy
```
variable "compartment_ocid" {
 default = "ocid1.compartment.oc1..uniqueid"
}
variable "region" {
 default = "us-phoenix-1"
}
```

  4. If the destination region has more or fewer availability domains than the source region, then edit the `vars.tf` file to specify the correct number of [availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).
For example, if you cloned from a region that has 3 availability domains and you want to re-create the infrastructure in a region that has only 1 availability domain, then remove the references to the second and third availability domains.
Example showing 3 availability domains:
```
data oci_identity_availability_domain export_NzDH-EU-FRANKFURT-1-AD-1 {
 compartment_id = var.compartment_ocid
 ad_number   = "1"
}
data oci_identity_availability_domain export_NzDH-EU-FRANKFURT-1-AD-2 {
 compartment_id = var.compartment_ocid
 ad_number   = "2"
}
data oci_identity_availability_domain export_NzDH-EU-FRANKFURT-1-AD-3 {
 compartment_id = var.compartment_ocid
 ad_number   = "3"
}
```

Example showing 1 availability domain:
```
data oci_identity_availability_domain export_NzDH-EU-FRANKFURT-1-AD-1 {
 compartment_id = var.compartment_ocid
 ad_number   = "1"
}
```

  5. Store the edited configuration file in the location that you want to reference when creating the second stack.
You can store a configuration file in a zip file, folder, Git repository, or other location supported by Resource Manager for creating stacks. See [Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).
  6. [Create](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.") a second stack using the edited configuration file.
  7. (Optional) Run a [plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.") on the new stack.
  8. Run an [apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") on the new stack.

The resources are cloned in the specified compartment and region.
Was this article helpful?
YesNo

