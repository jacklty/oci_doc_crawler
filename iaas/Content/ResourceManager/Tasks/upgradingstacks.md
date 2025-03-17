Updated 2025-01-31
# Upgrading a Stack to a Later Terraform Version
Upgrade a stack in Resource Manager to a later Terraform version.
**Note** These instructions don't apply to Resource Manager stacks created through Marketplace.
These steps are completed in the command line and the Console.
For information about Terraform versions supported by Resource Manager, see [Supported Terraform Versions](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/terraformversions.htm#top "Review the Terraform versions supported by the Resource Manager service.").
## Before You Begin 🔗 
To successfully upgrade your stack, you must have the following:
  * A MacOS, Linux, or Windows computer for running command line tools.
  * Software to create and unpack `.zip` archives, such as 7-ZIP.
  * [IAM policies to manage stacks and jobs.](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__stacks-jobs)


## Upgrade Paths 🔗 
Following are supported upgrade paths by initial version.
Initial Terraform Version | Upgrade Path  
---|---  
0.12 | In sequence, upgrade to each supported version: 0.13 > 0.14 > 1.0 (recommended) > 1.1 > 1.2 > 1.5.  
0.13 | In sequence, upgrade to each supported version: 0.14 > 1.0 (recommended) > 1.1 > 1.2 > 1.5.  
0.14 | In sequence, upgrade to each supported version: 1.0 (recommended) > 1.1 > 1.2 > 1.5.  
1.0 | In sequence, upgrade to each supported version: 1.1 > 1.2 > 1.5.  
1.1 | In sequence, upgrade to each supported version: 1.2 > 1.5.  
1.2 | Upgrade to 1.5.  
## Task 1: Confirm Up-to-Date Infrastructure 🔗 
This task uses the Console. For CLI and API instructions for a step, see the associated link.
  1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
  2. Confirm that the details page for the stack shows the expected version (**Terraform version**).
For CLI and API instructions to get a stack's details, see [Getting a Stack's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
  3. Check for pending changes to infrastructure:
    1. Select **Plan**.
When the action finishes, the details page for the related job opens.
For CLI and API instructions, see [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.").
    2. To review the log for the completed plan action, select **Logs**.
The log contents indicate whether the stack is up-to-date or has pending changes.
For CLI and API instructions, see [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").
Example for a stack that's up-to-date (no pending changes):
`No changes. Infrastructure is up-to-date.`
  4. If the log contents indicate pending changes, then apply pending changes:
    1. Select **Stack details** to go back to the details page for the stack.
    2. Select **Apply**.
For CLI and API instructions, see [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.").
When the action finishes, the details page for the related job opens. 
    3. Confirm that the apply action was successful: Select **Logs** to review the log for the completed plan action.
For CLI and API instructions, see [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").

When the stack infrastructure is up-to-date, you can proceed to the next task for downloading Terraform configuration and state files.
## Task 2: Download the Configuration and State 🔗 
**Note**
If the stack's Terraform configuration is stored in a source code control system, such as GitLab, then check out and download the Terraform configuration from there.
If the stack's Terraform configuration is stored in a bucket, then download the Terraform configuration from there.
This task uses the Console. For CLI and API instructions for a step, see the associated link.
  1. On a computer that can run command line tools, create a folder to store the downloaded Terraform configuration and state.
Example folder name: `c:\StackUpgrade`
  2. In the Console: On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
  3. Next to **Terraform configuration** , select **Download**.
For CLI and API instructions, see [Getting a Stack's Terraform Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#top "Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job.").
  4. Download the Terraform state file:
    1. On the stack's details page, select **View state**.
    2. To download the stack's state file, go to **More actions** and select **Download Terraform state**.
For CLI and API instructions, see [Getting a Stack's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm#top "Download the Terraform state file used by a stack in Resource Manager. The Terraform state file for a stack is the one associated with the most recent successful job.").

When the Terraform configuration and state are downloaded, you can proceed to the next task for upgrading the Terraform configuration.
## Task 3: Upgrade the Configuration 🔗 
This task provides customized steps for upgrading a Terraform configuration used with Resource Manager.
  1. On the same computer that you used to [store the downloaded Terraform configuration and state files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#download), download the `.zip` files needed to upgrade your Terraform configuration:
     * From <https://releases.hashicorp.com/terraform>, download the `.zip` file for your target Terraform version and operating system.
For example, for Terraform 0.13 on Mac, download the Darwin version: <https://releases.hashicorp.com/terraform/0.13.7/terraform_0.13.7_darwin_amd64.zip>.
  2. Extract the contents of each `.zip` file.
  3. Update the provider configuration to add arguments such as `user_ocid`, `fingerprint` and `private_key_path`. You might have commented out these arguments before.
Example of commented-out arguments:```
provider "oci" {
          tenancy_ocid = var.tenancy_ocid
          /*
          user_ocid = var.user_ocid
          fingerprint = var.fingerprint
          private_key_path = var.private_key_path
          */
          region = var.region
          }
```

  4. To follow code examples in the rest of this procedure, rename the extracted file as `terraform_<major-version>`.
Example: `terraform_13`
  5. To make the command (extracted file) accessible, store it in a directory that's present in your PATH directory.
  6. Open a command prompt.
  7. Change directory to the folder where you stored the downloaded stack information.
Example:
Copy
```
cd c:\StackUpgrade
```

  8. To initialize Terraform, run the following command:
Copy
```
terraform_<major-version> init
```

Example:
Copy
```
terraform_13 init
```

  9. To upgrade the syntax of your Terraform configuration, run the command for the target Terraform version:
Target Terraform Version | Command  
---|---  
0.13 | `terraform_13 13upgrade`  
0.14 | `terraform_14 14upgrade`  
1.0 and later | None needed. If preceding upgrades were successfully applied during the process, then no special changes are needed for upgrading the configuration.  
The output indicates whether the upgrade was successful.
If successful, continue with the next step.
If not successful, then make manual changes to your Terraform configuration files as directed.
  10. Create a `.zip` archive of your Terraform configuration files.
Example `.zip` archive: `c:\StackUpgrade\MyConfigUpgraded.zip`
Ensure that the archive omits the Terraform state file (`terraform.tfstate`) and the `.terraform` directory to satisfy the [required file structure for Terraform configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.").
  11. If a source code control system (such as GitHub) is used for the stack's Terraform configuration, then commit the upgraded Terraform configuration there.
The most recent commit is used when you run jobs on the stack.
  12. If an Object Storage bucket is used for the stack's Terraform configuration, then change the contents of that bucket to correspond with the upgraded Terraform configuration.
**Note** Back up the current bucket before changing it to correspond to the upgraded Terraform configuration. Limit the bucket to files that are intended for use with Terraform.
The most recent contents of the bucket are used when you run jobs on the stack.

When the Terraform configuration is successfully upgraded to the target Terraform version, then you can proceed to the next task for upgrading the stack.
## Task 4: Upgrade the Stack 🔗 
This task uses the Console. For CLI and API instructions for updating a stack, see [Updating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack.htm#top "Update a stack in Resource Manager.").
  1. In the Console, reopen the details page for the stack that you're upgrading: On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
  2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
  3. Upload the [upgraded Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#config) to the stack.
You can either drag the file onto the dialog's control or select **Browse** and navigate to the location of the file or folder.
Example file path: `c:\StackUpgrade\MyConfigUpgraded.zip`
The dialog box is populated with information contained in the Terraform configuration.
**Note** Skip this uploading step if the stack's Terraform configuration is stored in a source code control system (such as GitHub) or in an Object Storage bucket, then the stack was configured to use the upgraded Terraform configuration in [Task 3: Upgrade the Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#config) when you committed the change to source code or uploaded the file to the bucket.)
  4. Specify the target Terraform version: Change the **Terraform version**.
  5. Select **Next** twice, then select **Save changes**.

The stack is now synchronized with the upgraded Terraform configuration and specified Terraform version. You can now proceed to the next task for importing the state file.
## Task 5: Import the State 🔗 
This task uses the Console. For CLI and API instructions, see [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.").
  1. In the Console, reopen the details page for the stack that you're upgrading: On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
  2. Go to **More actions** and select **Import state**.
  3. In the **Import** panel, add the downloaded Terraform state file.
You can either drag the file onto the dialog's control or select **Browse** and navigate to the location of the file or folder.
Example file path: `c:\StackUpgrade\terraform.tfstate`
  4. Select **Import**.
The import job is created. The new job is listed under **Jobs**.
When the job finishes, the **Job details** page opens.
  5. Confirm successful import: Select **Logs**.
For CLI and API instructions, see [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").

After a successful import of the state file, proceed to the next task for checking for issues.
## Task 6: Check for Issues 🔗 
This task uses the Console. For CLI and API instructions for a step, see the associated link.
  1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
  2. Check for pending changes to infrastructure:
    1. Select **Plan**.
When the action finishes, the details page for the related job opens.
For CLI and API instructions, see [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.").
    2. To review the log for the completed plan action, select **Logs**.
For CLI and API instructions, see [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").
    3. In the log contents, check for issues described at [Troubleshooting Logs During an Upgrade](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#troubleshooting).
  3. Resolve any listed issues by manually updating the Terraform configuration, as described at [Troubleshooting Logs During an Upgrade](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#troubleshooting).
  4. On the details page for the stack, select **Edit** , then upload the newly updated Terraform configuration to the stack.
You can either drag the file onto the dialog's control or select **Browse** and navigate to the location of the file or folder.
Example file path: `c:\StackUpgrade\MyConfigUpgraded.zip`
The dialog box is populated with information contained in the Terraform configuration.
**Note** Skip this uploading step if the stack's Terraform configuration is stored in a source code control system (such as GitHub) or in an Object Storage bucket, then the stack was configured to use the upgraded Terraform configuration in [Task 3: Upgrade the Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#config) when you committed the change to source code or uploaded the file to the bucket.)
  5. Select **Next** twice, then select **Save changes**.
  6. Run the plan action again to confirm that the issues are no longer listed in the associated log contents.
    1. Select **Plan**.
When the action finishes, the details page for the related job opens.
For CLI and API instructions, see [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.").
    2. To review the log for the completed plan action, select **Logs**.
For CLI and API instructions, see [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").


### Troubleshooting Logs During an Upgrade 🔗 
Following are some issues you might see in logs while upgrading a stack to a new Terraform version. This list is limited to a few issues that the Resource Manager service team knows about.
#### Error: Failed to install providers 🔗 
The log shows an error message similar to the following.
```
Error: Failed to install providers
Could not find required providers, but found possible alternatives:
hashicorp/gitlab -> gitlabhq/gitlab
If these suggestions look correct, upgrade your configuration with the following command:
terraform 0.13upgrade .
```

The configuration doesn't meet requirements for the specified Terraform version. Version 0.13.x and later don't use this syntax for providers. Example configuration causing this error:
```
provider "gitlab" {
 token = "glpat-_abcd"
} 
# Add a project owned by the user
resource "gitlab_project" "sample_project" {
 name = "example"
}
```

Add a `required_providers` block and explicitly mention the source information for the provider. For more information, see [Requiring Providers](https://developer.hashicorp.com/terraform/language/v1.1.x/providers/requirements#requiring-providers). Example update:
```
terraform {
 required_providers {
  oci = {
   source = "oracle/oci"
   version = "5.46"
  }
  gitlab = {
   source = "gitlabhq/gitlab"
   version = "17.8.0"
  }
 }
}
```

#### Error: Invalid quoted type constraints 🔗 
The log shows an error message similar to the following.
```
Error: Invalid quoted type constraints on variables.tf line 18, in variable "vcn_dns_label"
 18:    type = "string"
Terraform 0.11 and earlier required type constraints to be given in quotes, 
but that form is now deprecated and will be removed in a future version of
Terraform. Remove the quotes around "string".
```

The configuration doesn't meet requirements for the specified Terraform version. Version 1.0.x and later don't use quotes for type declarations of variables. Example configuration causing this error:
```
variable "vcn_dns_label" {
 type = "string"
 default = "vcn"
}
```

Remove the quotes from type declarations of variables. Example update:
```
variable "vcn_dns_label" {
 type = string
 default = "vcn"
}
```

#### Error: Error in function call (map) 🔗 
The log shows an error message similar to the following.
```
Error: Error in function call
on main.tf line 44, in resource "oci_core_subnet" "this":
44:    display_name    = lookup(map("a", "b", "c", "d"), "a", "default")
────────────────
while calling map(vals...)
Call to function "map" failed: the "map" function was deprecated in Terraform v0.12 and 
is no longer available; use tomap({ ... }) syntax to write a literal map.
```

The configuration doesn't meet requirements for the specified Terraform version. Version 1.0.x and later don't use this syntax for maps. Example configuration causing this error:
```
resource "oci_core_subnet" "this" {
  ...
  ...
  vcn_id = lookup(map("a", 1, "b", 2), "a", "default")
  ...
  ...
}
```

Correct the syntax for the map to use `tomap()`. Example update:
```
resource "oci_core_subnet" "this" {
  ...
  ...
  vcn_id = lookup(tomap({"a" = 1, "b" = 2}), "a", "default")
  ...
  ...
}
```

#### Error: Error in function call (list) 🔗 
The log shows an error message similar to the following.
```
Error: Error in function call
on main.tf line 35, in resource "oci_core_subnet" "this"
 35:    count        = length(list("phx-ad-1"", ""phx-ad-2"))
Call to function "list"" failed: the ""list" function was deprecated in
Terraform v0.12 and is no longer available; use tolist([ ... ]) syntax to
write a literal list.
```

The configuration doesn't meet requirements for the specified Terraform version. Version 1.0.x and later don't use this syntax for lists. Example configuration causing this error:
```
resource "oci_core_subnet" "this" {
  count = length(list("phx-ad-1", "phx-ad-2"))
  ...
  ...
}
```

Correct the syntax for the list to use `tolist()`. Example update:
```
resource "oci_core_subnet" "this" {
  count = length(tolist(["phx-ad-1", "phx-ad-2"]))
  ...
  ...
}
```

#### Error: The ["*"] form of ignore_changes wildcard is deprecated 🔗 
The log shows an error message similar to the following.
```
Getting providers from registry and/or custom terraform providers
resource "oci_core_subnet" "this"
 44:     ignore_changes = ["*"]
The ["*"] form of ignore_changes wildcard is was deprecated and is now
invalid. Use "ignore_changes = all" to ignore changes to all attributes.
```

The configuration doesn't meet requirements for the specified Terraform version. Version 1.0.x and later don't use this syntax for `ignore_changes` wildcards. Example configuration causing this error:
```
resource "oci_core_subnet" "this" {
  ...
  ...
  lifecycle {
   ignore_changes = ["*"]
  }
}
```

Use `ignore_changes = all` instead. Example update:
```
resource "oci_core_subnet" "this" {
  ...
  ...
  lifecycle {
   ignore_changes = all
  }
}
```

#### Issue: Deprecated HCL Syntax 🔗 
The log indicates existence of deprecated HCL syntax.
The configuration doesn't meet requirements for the specified Terraform version.
Update the configuration to omit deprecated HCL syntax.
Was this article helpful?
YesNo

