Updated 2025-01-23
# Getting Started
This sample provides an end-to-end walkthrough of the tasks required to create and deploy an Oracle Cloud Infrastructure compute instance using Resource Manager.
This page helps you get started with Resource Manager. Use this end-to-end walkthrough of tasks to create and deploy an Oracle Cloud Infrastructure compute instance using either a prebuilt Terraform configuration or your own Terraform configuration. For a brief introduction to Resource Manager, see [Overview of Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#top "Automate deployment and operations for Oracle Cloud Infrastructure resources using Resource Manager. With supported Infrastructure as Code \(IaC\) tools, DevOps engineers can develop and deploy their infrastructure anywhere."). 
## Highlights 🔗 
In addition to providing a prebuilt Terraform configuration for creating a Compute instance, this walkthrough provides samples that demonstrate how to write a Terraform configuration. Whichever configuration you use (prebuilt or your own), Resource Manager uses Terraform to provision the defined resources . The resources are organized into stacks, which you create and provision using jobs.
The walkthrough covers the following tasks:
  * Select or create a Terraform configuration.
  * Provision the infrastructure: 
    * Create a stack in which to provision your infrastructure.
    * Run a plan job against your stack, which parses your configuration and creates an execution plan.
    * Review the generated execution plan. 
    * Run an apply job against your stack, which provisions your resources. The apply job follows the execution plan, which is based on your Terraform configuration.
    * Review the resulting infrastructure. 
  * Optionally provision the infrastructure in more environments, using the same Terraform configuration.


## Before You Begin 🔗 
Ensure that you have installed, obtained, or created the prerequisites:
  * An Oracle Cloud Infrastructure tenancy for each environment where you want to provision resources. For example, you might provision the resources defined in a Terraform configuration to development, staging, and production environments.
**Note** It is a best practice to locate each environment in its own tenancy.
  * The **OCID** for the compartment where you wish to create your stack.
  * A user account that includes the following: 
    * An API signing key. For guidance, see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
    * Required IAM permissions. For more information, see [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm) and [Details for Resource Manager](https://docs.oracle.com/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm).
  * If you want to use the Oracle Cloud Infrastructure CLI, install and configure the CLI first. See [Quickstart](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm) and [Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm)


## Task 1a: Select a prebuilt Terraform Configuration 🔗 
You can select the compute instance [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") with its prebuilt Terraform configuration instead of writing your own configuration. These steps guide you through the stack creation process.
  1. Select the following link to launch the **Create stack** page with the compute instance template already selected.
[Launch stack with Compute Instance template](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=computeinstance)
  2. In the **Create stack** page, enter a **Name** for the new stack (or accept the default name provided). Avoid entering confidential information.
  3. From the **Create in compartment** drop-down, select the compartment where you want to create the stack. 
A compartment from the list scope is set by default.
  4. Select **Next**. 
The **Configure variables** panel displays variables from the Terraform configuration.
  5. Review the variables and make changes as necessary.
**Important** Do not add your private key or other confidential information to configuration variables. 
  6. Select **Next**. 
  7. In the **Review** panel, verify your stack configuration. 
For purposes of this walkthrough, leave **Run apply** blank. (Use this option to automatically provision the infrastructure when the stack is created.)
  8. Select **Create** to create your stack.
The stack details page for the new stack appears. 
Congratulations! You have created a stack with the prebuilt Terraform configuration from the compute instance template. The next step is to [provision the infrastructure](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build).


## Task 1b: Create Your Own Terraform Configuration 🔗 
If you didn't select a prebuilt Terraform configuration, then follow these steps to write your own. 
A Terraform configuration is a file that codifies your infrastructure. The configuration defines your Terraform provider, the resources you intend to provision, variables, and specific instructions for provisioning the resources.
This page guides you through selecting the compute Instance [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") with its prebuilt Terraform configuration or alternatively writing your own configuration using several .tf files within a .zip file.
For more information about writing configurations for use with Resource Manager, see [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Terraform Language Documentation](https://developer.hashicorp.com/terraform/language).
**Caution** Do not provide user credentials or other confidential information in your Terraform configuration. 
[Create an Oracle Cloud Infrastructure Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following code sample creates a basic Oracle Cloud Infrastructure Terraform provider. You can provide values as variables that are defined either in a variables file or in the provider definition (.tf) file. For more information, see [Provider Configuration](https://developer.hashicorp.com/terraform/language/providers/configuration).
Copy
```
provider "oci" {
 region = "${var.region}"
}
```

[Define Variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Define the variables you want to use when provisioning your resources. A best practice is to create a "variables" file in the configuration package that you upload. Following is an example from a configuration file that we've named `variables.tf`. For more information about using variables, see [Define input variables](https://developer.hashicorp.com/terraform/tutorials/oci-get-started/oci-variables). See also [Input Variables](https://developer.hashicorp.com/terraform/language/values/variables).
Copy
```

variable "compartment_ocid" {
	default = "ocid1.compartment.oc1..uniqueid"
}
variable "region" {
	default = "us-phoenix-1"
}
variable "InstanceImageOCID" {
 type = "map"
 
 default = {
  // See https://docs.cloud.oracle.com/images/
  // Platform image "Oracle-Linux-7.5-2018.10.16-0"
  "eu-frankfurt-1" = "ocid1.image.oc1.eu-frankfurt-1.aaaaaaaaitzn6tdyjer7jl34h2ujz74jwy5nkbukbh55ekp6oyzwrtfa4zma"
  "uk-london-1" = "ocid1.image.oc1.uk-london-1.aaaaaaaa32voyikkkzfxyo4xbdmadc2dmvorfxxgdhpnk6dw64fa3l4jh7wa"
  "us-ashburn-1" = "ocid1.image.oc1.iad.aaaaaaaageeenzyuxgia726xur4ztaoxbxyjlxogdhreu3ngfj2gji3bayda"
  "us-phoenix-1" = "ocid1.image.oc1.phx.aaaaaaaaoqj42sokaoh42l76wsyhn3k2beuntrh5maj3gmgmzeyr55zzrwwa"
 }
}

variable "ssh_public_key" {
	default = "ssh-rsa <public_key_value>"
}
# Defines the number of instances to deploy
variable "NumInstances" {
  default = "1"
}
variable "InstanceShape" {
  default = "VM.Standard2.1"
}
# Specifies the Availability Domain
variable "localAD" {
  default = "<AD_name>"
}
```

For more information about variables declared in the preceding examples, see the following:
  * `InstanceImageOCID`: [Platform Images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)
  * `InstanceShape`: [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)
  * `region` and `localAD`: [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)


[Define a Schema Document (Optional)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
With a [schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#top "Review requirements, supported types, and examples for schema documents used with Terraform configurations in Resource Manager."), you can reuse one, unedited Terraform configuration in development, staging, and production environments. Resource Manager prompts you for variable values when you create a stack with a Terraform configuration that includes a schema document.
Schema documents are recommended for Terraform configurations when using Resource Manager. Including a schema document allows you to extend pages in the Oracle Cloud Infrastructure Console. Facilitate variable entry in the **Create stack** page by surfacing SSH key controls and by naming, grouping, dynamically prepopulating values, and more. Define text in the **Application Information** tab of the **Stack details** page that opens for a created stack.
Following are contents of an example schema document (`schema.yaml`) that covers the basic details in this scenario.
**Note** To easily reuse this schema document, [specify default values](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__default) for each variable.
Copy
```
locale: "en"
variableGroups:
 - title: "Destination"
  variables:
   - compartment_ocid
   - ${region}
   - ${localAD}
 - title: "Instance Details"
  variables:
   - ${numInstances}
   - ${instanceImageOCID}
   - ${instanceShape}
 - title: "SSH Public Key"
  variables:
   - ${ssh_public_key}
variables:
 compartment_ocid:
  type: oci:identity:compartment:id
  required: true
  title: Compartment OCID
 region:
  type: oci:identity:region:name
  required: true
  title: Region
 localAD:
  type: oci:identity:availabilitydomain:name
  required: true
  title: Availability Domain
  dependsOn:
   compartmentId: compartment_ocid
 numInstances:
  type: integer
  required: true
  title: Number of Instances
  minimum: 1
  maximum: 10
  multipleOf: 1
 instanceImageOCID:
  type: oci:core:image:id
  required: true
  title: Instance Image OCID
  dependsOn:
   compartmentId: compartment_ocid
 instanceShape:
  type: oci:core:instanceshape:name
  required: true
  title: Instance Shape
  default: "VM.Standard.E2.1.Micro"
  dependsOn:
   compartmentId: compartment_ocid
 ssh_public_key:
  type: oci:core:ssh:publickey
  required: true
  title: SSH Public Key
```

[Create a Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following code sample creates an Oracle Cloud Infrastructure virtual cloud network (VCN) named "ExampleVCN."
Copy
```
resource "oci_core_virtual_network" "ExampleVCN" {
 cidr_block = "10.1.0.0/16"
 compartment_id = "${var.compartment_ocid}"
 display_name = "TFExampleVCN"
 dns_label = "tfexamplevcn"
}
```

[Create a Subnet in Your VCN](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following code sample creates a subnet named "ExampleSubnet" in the VCN defined in the previous code sample.
Copy
```
resource "oci_core_subnet" "ExampleSubnet" {
 availability_domain = "${var.localAD}"
 cidr_block = "10.1.20.0/24"
 display_name = "TFExampleSubnet"
 dns_label = "tfexamplesubnet"
 security_list_ids = ["${oci_core_virtual_network.ExampleVCN.default_security_list_id}"]
 compartment_id = "${var.compartment_ocid}"
 vcn_id = "${oci_core_virtual_network.ExampleVCN.id}"
 route_table_id = "${oci_core_route_table.ExampleRT.id}"
 dhcp_options_id = "${oci_core_virtual_network.ExampleVCN.default_dhcp_options_id}"
}
```

[Create an Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following code sample creates an internet gateway named "ExampleIG" in the VCN that we created.
Copy
```
resource "oci_core_internet_gateway" "ExampleIG" {
 compartment_id = "${var.compartment_ocid}"
 display_name = "TFExampleIG"
 vcn_id = "${oci_core_virtual_network.ExampleVCN.id}"
}
```

[Create a Core Route Table](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following code sample creates a Oracle Cloud Infrastructure core route table in the VCN and then applies two route rules.
Copy
```
resource "oci_core_route_table" "ExampleRT" {
 compartment_id = "${var.compartment_ocid}"
 vcn_id = "${oci_core_virtual_network.ExampleVCN.id}"
 display_name = "TFExampleRouteTable"
 route_rules {
  cidr_block = "0.0.0.0/0"
  network_entity_id = "${oci_core_internet_gateway.ExampleIG.id}"
 }
}
```

[Create a Compute Instance](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The following extended code example creates an Oracle Cloud Infrastructure compute instance. The code also references the image on which the compute instance is created, sets boot volume size, adds essential metadata, and applies both free-form and defined tags.
Copy
```
resource "oci_core_instance" "TFInstance" {
 count = "${var.NumInstances}"
 availability_domain = "${var.localAD}"
 compartment_id = "${var.compartment_ocid}"
 display_name = "TFInstance${count.index}"
 shape = "${var.InstanceShape}"
 
 create_vnic_details {
  subnet_id = "${oci_core_subnet.ExampleSubnet.id}"
  display_name = "primaryvnic"
  assign_public_ip = true
  hostname_label = "tfexampleinstance${count.index}"
 }
 
 source_details {
  source_type = "image"
  source_id = "${var.InstanceImageOCID[var.region]}"
 
  # Apply this to set the size of the boot volume that's created for this instance.
  # Otherwise, the default boot volume size of the image is used.
  # This should only be specified when source_type is set to "image".
  #boot_volume_size_in_gbs = "60"
 }

  # Apply the following flag only if you wish to preserve the attached boot volume upon destroying this instance
 # Setting this and destroying the instance will result in a boot volume that should be managed outside of this config.
 # When changing this value, make sure to run 'terraform apply' so that it takes effect before the resource is destroyed.
 #preserve_boot_volume = true
 
 metadata = {
  ssh_authorized_keys = "${var.ssh_public_key}"
 
 }
 timeouts {
  create = "60m"
 }
}

```

[Finalize the Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Ensure that all of the configuration files are in a single directory. You can store your Terraform configuration file locally or in a source code control system. For more information on storing your file in a source code control system, see [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager."). Wherever your file is stored, you can select it when creating a stack using the CLI or Console.
**Important** Make sure your Terraform configuration file is valid. See [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).") and [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model."). 
## Task 2: Provision the Infrastructure 🔗 
Use your Terraform configuration to build and deploy your infrastructure by taking the following actions:
  1. If you created your own Terraform configuration, follow these steps to create a stack in a tenancy compartment of your choosing. (If you selected a prebuilt configuration, skip this step.)
For Terraform configuration sources supported with Resource Manager, see [Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).
A stack is a collection of resources that you can act on as a group. All of the resources that you specify in your configuration are provisioned in the stack that you create.
You can create a stack from a remote, versioned file in a source code control system (such as [Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.")), an [Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in an Object Storage bucket."), or a locally accessed .zip file that you upload. Following are instructions for a local file.
[To create a stack from your .zip file (Console) ](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.
    3. Select **Create stack**. 
The **Create stack** page opens, with the **Stack information** tab selected.
    4. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **My configuration**.
    5. Under **Stack configuration** , select **.Zip file** and add the Terraform configuration.
You can either drag and drop your Terraform configuration .zip file onto the control or select **Browse** and navigate to the location of the .zip file.
You can also store your configuration remotely. For example, store the configuration in [Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.") or an [Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in an Object Storage bucket.").
The page is populated with information contained in the Terraform configuration.
    6. Enter values for the remaining fields.
Name | Description  
---|---  
**Use custom providers** | Select this option to use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), and then select the bucket that contains the custom providers.  
**Name** | Stack name. You can accept the default name provided. Avoid entering confidential information.  
**Description** | Stack description (optional).  
**Create in compartment** | Compartment where you want to create the stack. A compartment from the list scope is set by default.  
**Terraform version** | Version that you want for the Terraform configuration.  
**Tags** | Optionally apply [tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm) to the stack.  
    7. Select **Next**. 
The **Configure variables** panel lists variables from the Terraform configuration.
    8. Review the variables and change as needed.
Don't add your private key or other confidential information to configuration variables. 
    9. Select **Next**.
    10. In the **Review** panel, verify the stack configuration.
    11. To automatically provision resources on creation of the stack, select **Run apply**.
    12. Select **Create** to create the stack.
The stack is created and its details page opens.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.
[To create a stack from your .zip file (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the command related to your file location. 
[To create a stack from a remote, versioned file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager stack create-from-git-provider[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-git-provider.html)` command and required parameters to create a stack from Git.
Command
CopyTry It
```
oci resource-manager stack create-from-git-provider [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Command
CopyTry It
```
oci resource-manager stack create-from-git-provider --compartment-id ocid1.tenancy.oc1..uniqueid --config-source-configuration-source-provider-id ocid.ormconfigsourceprovider.oc1..uniqueid --config-source-repository-url https://github.com/user/repo.git --config-source-branch-name mybranch --display-name "My Stack from Git" --description "My Test" --variables file://variables.json --working-directory ""
```

[To create a stack from your .zip file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
**Note** On Windows, be sure the zip file and variables.json files are in the same directory from which you're running the CLI. The CLI currently has a limitation on Windows that prevents correct handling of the files if either one is in a subdirectory.
Use the `oci resource-manager stack create[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create.html)` command and required parameters to create a stack from a local zip file.
Command
CopyTry It
```
oci resource-manager stack create [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Command
CopyTry It
```
oci resource-manager stack create --compartment-id ocid1.tenancy.oc1..uniqueid --config-source vcn.zip --variables file://variables.json --display-name "My Example Stack" --description "My Tutorial to Create a VCN" --working-directory ""
```

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
```
{
 "data": {
  config-source": 
  {
   "working-directory": null,
   "config-source-type": "ZIP_UPLOAD"
  },
  "defined-tags": {},
  "description": "My Tutorial to Create a VCN",
  "display-name": "My Example Stack",
  "freeform-tags": {},
  "id": "ocid1.ormstack.oc1..uniqueid",
  "lifecycle-state": "ACTIVE",
  "time-created": "2019-04-03T18:26:56.299000+00:00",
  "variables": 
  {
   "compartment_ocid": "ocid1.compartment.oc1..uniqueid", 
   "region": "us-phoenix-1"
  }
 }
}
```

  2. Generate an execution plan. 
The plan job parses your configuration to create an "execution plan," which is a step-by-step representation of the planned deployment in job log entries. Once the plan job has completed, you can evaluate the execution plan by viewing the job's log entries to confirm that it performs the expected operations, and in the intended sequence.
**Note** You can skip this step if you selected **Run apply** when you [created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.
[To run a plan job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.
    3. Select the name of the stack that you want.
The **Stack details** page opens.
    4. Select **Plan**.
    5. In the **Plan** panel, review the **Name** and optionally change it.
    6. Select **Plan**.
The plan job is created. The new job is listed under **Jobs**.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
[To run a plan job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job create-plan-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)` command and required parameters to run a plan job.
Copy
```
oci resource-manager job create-plan-job [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
  3. Review the execution plan to confirm that it represents your intentions. 
The execution plan is represented in the log for the plan job you ran previously. 
**Note** You can skip this step if you selected **Run apply** when you [created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.
[To review an execution plan (the log for the plan job) (Console) ](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Jobs**.
You can also access jobs from a stack detail page. Select **Stacks** and then select the name of the stack you want.
    2. Under **List Scope** , select a compartment that you have permission to work in.
    3. Select the name of the plan job that you ran.
The **Job details** page opens. Logs are visible (in the **Logs** section under **Resources**).
For plan jobs, the log file is the execution plan. View the log file for the plan job and note the "message" fields in the sequence of log entries of the log file. These values represent the sequence of operations specified in your configuration.
    4. (Optional) Select **Download logs** (in the **Logs** section under **Resources**).
If changes are needed, [update your stack to use a revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#top "Update the zip file or folder Terraform configuration used by a stack in Resource Manager. The updated configuration is used when you run jobs on the stack. A folder-based update is available using the Console only.") and then [run another plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.") to obtain an updated execution plan.
[To review an execution plan (the log for the plan job) (CLI) ](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job get-job-logs[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)` command and required parameters to get logs for a job as a paged list of entries.
Command
CopyTry It
```
oci resource-manager job get-job-logs [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The command returns JSON objects that describe log entries. Each object has a message member with a property that displays one line of the execution plan. In this example, the plan job creates a single virtual cloud network (VCN); the remaining members show details about the VCN.
```
...
        {
        "level": "INFO",
        "message": "Terraform will perform the following actions:",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "+ oci_core_virtual_network.vcn1",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "id: <computed>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "cidr_block: \"10.0.0.0/16\",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "compartment_id: \"ocid1.tenancy.oc1..exampleaqnpcpfqfmrf6dw5gcew7yqpirvarueirj2mv4jzn5goejsxma\",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "default_dhcp_options_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "   default_route_table_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "   default_security_list_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        ...
       
```

If changes are needed, [update your stack to use a revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#top "Update the zip file or folder Terraform configuration used by a stack in Resource Manager. The updated configuration is used when you run jobs on the stack. A folder-based update is available using the Console only.") and then [run another plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.") to obtain an updated execution plan.
  4. Provision your resources by running an apply job against the execution plan. 
When satisfied with the execution plan, you're ready to do the work of provisioning the stack with the resources that you've defined. The apply job takes the execution plan and "applies" it to the stack. The result is a fully provisioned stack.
**Note** You can skip this step if you selected **Run apply** when you [created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.
[To run an apply job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.
    3. Select the name of the stack that you created.
The **Stack details** page opens.
    4. Select **Apply**.
    5. (Optional) In the **Apply** panel, review the apply job **Name** and [other settings](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#console) and update if needed.
    6. Select **Apply**.
The apply job is created. The new job is listed under **Jobs**.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
To confirm existence of newly provisioned resources, [inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm#top "Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned \(by running an apply job\) or absence of a resource that you released \(by running a destroy job\)."). 
[To run an apply job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job create-apply-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-apply-job.html)` command and required parameters to run an apply job.
Copy
```
oci resource-manager job create-apply-job [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Examples](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Example 1: Reference a plan job.
Copy
```
oci resource-manager job create-apply-job --execution-plan-strategy <plan_job_ocid> --stack-id <stack_ocid>
```

Example 2: Automatically approve (don't reference a plan job).
Copy
```
oci resource-manager job create-apply-job --execution-plan-strategy AUTO_APPROVED --stack-id <stack_ocid>
```

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
To confirm existence of newly provisioned resources, [inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm#top "Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned \(by running an apply job\) or absence of a resource that you released \(by running a destroy job\)."). 
  5. Review the log entries and state file for the apply job you just ran. 
     * See the entries in the job log for more details about the job. 
[To view the job log (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
       1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Jobs**.
You can also access jobs from a stack detail page. Select **Stacks** and then select the name of the stack you want.
       2. Under **List Scope** , select a compartment that you have permission to work in.
       3. Select the name of the apply job that you ran.
The **Job details** page opens. Logs are visible (in the **Logs** section under **Resources**).
       4. (Optional) Select **Download logs** (in the **Logs** section under **Resources**).
[To view the job log (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
View the log file and note the "message" fields in the sequence of log entries of the log file. You can view the log file for the specified job as either a paged list of entries or in its raw form. 
[To view a paged list of entries](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job get-job-logs[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)` command and required parameters to get logs for a job as a paged list of entries.
Command
CopyTry It
```
oci resource-manager job get-job-logs [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
The command returns JSON objects that describe log entries. Each object has a message member with a property that displays one line of the execution plan. In this example, the plan job creates a single virtual cloud network (VCN); the remaining members show details about the VCN.
```
...
        {
        "level": "INFO",
        "message": "Terraform will perform the following actions:",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "+ oci_core_virtual_network.vcn1",
        "timestamp": "2018-05-24T00:57:14.170000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "id: <computed>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "cidr_block: \"10.0.0.0/16\",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "compartment_id: \"ocid1.tenancy.oc1..exampleaqnpcpfqfmrf6dw5gcew7yqpirvarueirj2mv4jzn5goejsxma\",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "default_dhcp_options_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "   default_route_table_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        {
        "level": "INFO",
        "message": "   default_security_list_id: <computed_value>",
        "timestamp": "2018-05-24T00:57:14.172000+00:00",
        "type": "TERRAFORM_CONSOLE"
        },
        ...
       
```

[To view logs in raw form](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job get-job-logs-content[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs-content.html)` command and required parameters to get logs content for a job.
Command
CopyTry It
```
oci resource-manager job get-job-logs-content [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
     * The job state file represents the job's output in JSON format. 
The state file maps your stack's resources to your configuration and also maintains essential configuration metadata, such as resource dependencies. Resource Manager generates and updates state files automatically when you run jobs.
The Resource Manager supports state locking by allowing only one job at a time to run on a given stack. For more information about state files, see [State](https://developer.hashicorp.com/terraform/language/state).
[To view the state of the job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
       1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Jobs**.
You can also access jobs from a stack detail page. Select **Stacks** and then select the name of the stack you want.
       2. Under **List Scope** , select a compartment that you have permission to work in.
       3. Select the name of the job.
The **Job details** page opens.
       4. Select **Download Terraform configuration**.
[To view the state of the job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job get-job-tf-state[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-state.html)` command and required parameters to get a job's state.
Command
CopyTry It
```
oci resource-manager job get-job-tf-state [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
Example response:
Copy
```
{
 "data": 
 {
  "lineage": "57ef4f0c-c8cd-8a32-d45f-d2c40be7b915",
  "modules": 
  [
   {
    "depends_on": [],
    "outputs": {},
    "path": 
    [
     "root"
    ],
    "resources": 
    {
     "oci_core_virtual_network.vcn1": {
     "depends_on": [],
     "deposed": [],
     "primary": 
     {
      "attributes": {
      "cidr_block": "10.0.0.0/16",
      "compartment_id": "ocid1.tenancy.oc1..uniqueid",
      "default_dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.uniqueid",
      "default_route_table_id": "ocid1.routetable.oc1.phx.uniqueid",
      "default_security_list_id": "ocid1.securitylist.oc1.phx.uniqueid",
      "display_name": "My VCN display name",
      "dns_label": "myvcntest",
      "id": "ocid1.vcn.oc1.phx.uniqueid",
      "state": "AVAILABLE",
      "time_created": "2018-05-24 01:13:05.855 +0000 UTC",
      "vcn_domain_name": "myvcntest.oraclevcn.com"
     },
     "id": "ocid1.vcn.oc1.phx.uniqueid",
     "meta": 
     {
      "e2bfb730-ecaa-11e6-8f88-34363bc7c4c0": {
      "create": 300000000000,
      "delete": 300000000000,
      "update": 300000000000
     }
    },
    "tainted": false
   },
   "provider": "provider.oci",
   "type": "oci_core_virtual_network"
     }
    }
   }
  ],
 "serial": 4,
 "terraform_version": "0.11.7",
 "version": 3
}
}
```

**Note** You can also [import state files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.") for resources already managed by Terraform. 
  6. When you need to release the resources that you provisioned, run a destroy job on the stack. 
A destroy job tears down the stack that you created and then cleans up associated resources without deleting them. For example, the destroy job terminates Compute instances associated with the stack.
**Note**
We recommend running a destroy job before deleting a stack to release associated resources first. When you delete a stack, its associated state file is also deleted; therefore, you lose track of the state of its associated resources. Cleaning up resources associated with a deleted stack can be difficult without the state file, especially when those resources are spread across multiple compartments. To avoid difficult cleanup later, we recommend that you release associated resources first by running a destroy job.
Data cannot be recovered from destroyed resources.
[To run a destroy job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.
    3. Select the name of the stack that you want.
The **Stack details** page opens.
    4. Select **Destroy**.
    5. (Optional) In the **Destroy** panel, review the apply job **Name** and [other settings](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#console) and update if needed.
    6. Select **Destroy**.
The destroy job is created. The new job is listed under **Jobs**.
After running a destroy job, get the job to check its status. You can optionally view the Terraform state file, view the logs, and confirm deletion of the resources. You can also re-create destroyed resources.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the **Job details** page, then select **View state** under **Resources**. Optionally select **Show changes in this version**.
To view the logs for the job, select the job to open its details page, then select **Logs** under **Resources**.
To confirm deletion of the resources, [inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm#top "Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned \(by running an apply job\) or absence of a resource that you released \(by running a destroy job\)."). 
To re-create a stack's resources after the resources are destroyed, [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."). The new resources differ from previously destroyed resources by their unique [OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) and other metadata. 
[To run a destroy job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm)
Use the `oci resource-manager job create-destroy-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-destroy-job.html)` command and required parameters to run a destroy job.
Copy
```
oci resource-manager job create-destroy-job [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
After running a destroy job, get the job to check its status.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
You can optionally [view the Terraform state file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#top "Download the Terraform state file \(.json\) from a completed apply, apply rollback, or import job in Resource Manager."), [view the logs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager."), and confirm deletion of the resources. You can also re-create destroyed resources.
To confirm deletion of the resources, [inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm#top "Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned \(by running an apply job\) or absence of a resource that you released \(by running a destroy job\)."). 
To re-create a stack's resources after the resources are destroyed, [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."). The new resources differ from previously destroyed resources by their unique [OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) and other metadata. 


## Task 3: Repeat in More Environments 🔗 
This section describes how to build and deploy infrastructure in multiple environments.
In this scenario, you use the same [Terraform configuration .zip file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#config) to provision a Compute instance in your development, staging, and production environments.
**Note** This scenario assumes that the Terraform configuration includes [a schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#schema), which allows you to change variable values when creating a stack in the Console.
  1. Access the tenancy for the new environment where you want to provision the infrastructure defined in your Terraform configuration.
For example, access the tenancy for your staging or production environment.
  2. Open the **Create stack** page:
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Under **List Scope** , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. Select **Create stack**. 
  3. Using the same Terraform configuration as for the first environment, complete the **Stack information** tab:
    1. On the **Create stack** page, select **My configuration**.
    2. Under **Stack configuration** , select **.Zip file** and add the Terraform configuration.
You can either drag and drop your Terraform configuration .zip file onto the control or select **Browse** and navigate to the location of the .zip file.
    3. Enter a **Name** for the new stack (or accept the default name provided). Avoid entering confidential information.
    4. Optionally enter a **Description**. 
    5. From the **Create in compartment** drop-down, select the compartment where you want to create the stack. 
    6. Select **Next**. 
The **Configure variables** panel displays variables from the selected Terraform configuration file. 
  4. Specify the variable values for this environment:
    1. In the **Configure variables** panel, review the variables and make changes as necessary.
[Default values](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__default) are provided when specified in the [schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#schema).
**Important** Do not add your private key or other confidential information to configuration variables.
    2. Select **Next**. 
  5. In the **Review** panel, verify your stack configuration. 
  6. To automatically provision resources on creation of the stack, select **Run apply**.
  7. Select **Create** to create your stack.
The stack details page for the new stack appears.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.


Congratulations, you have reused your Terraform configuration to create a stack in a new environment. If you selected **Run apply** , then you also provisioned resources in the new environment.
You can now generate and review an execution plan (and provision resources, if **Run apply** wasn't selected). To complete these items, repeat the steps from [Task 2: Provision the Infrastructure](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build) in the new environment.
Was this article helpful?
YesNo

