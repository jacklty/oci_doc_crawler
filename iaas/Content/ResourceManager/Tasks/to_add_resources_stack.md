Updated 2025-01-23
# Adding Unmanaged Resources
Add existing resources to a stack in Resource Manager.
**Note** Some steps in these instructions use [Terraform CLI](https://developer.hashicorp.com/terraform/cli); most steps use the Oracle Cloud Infrastructure Console.
  1. Gather information about the unmanaged resources that you want to add: Note their [OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
Unmanaged resources are created outside Resource Manager.
**Tip** You can generate a Terraform configuration that lists all resources in a compartment. For instructions, see [Creating a Stack from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#top "Using resource discovery, create a stack in Resource Manager based on an existing compartment to generate a Terraform configuration that describes the compartment's resources.").
  2. [Gather stack information](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm)
    1. In the Console, access the details page for the stack that you want to add the resources to.
      1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
      2. Under **List Scope** , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
      3. Select the name of the stack to display its details page.
    2. Confirm that managed resources are up-to-date: Generate a drift detection report.
      1. Go to **More actions** and select **Run drift detection**.
      2. In the **Run drift detection** panel, select **All resources**.
      3. Select **Run drift detection**.
A work request is started. When the work request is complete, the drift status appears in the **Stack information** tab.
      4. Go to **More actions** and select **View drift detection report**.
A panel lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
      5. To view details of drift status for a resource, expand the resource.
Actual and expected properties are listed.
      6. If differences between actual and expected properties are reported, make your resources match the properties of your Terraform configuration: [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."). In the Stack Details page, select **Apply**.
You can alternatively address these differences when manually editing the Terraform configuration later.
    3. Download the stack's Terraform configuration file: In the **Stack information** tab, to the right of **Terraform configuration** , select **Download**.
    4. Download the stack's state file:
      1. Go to the details page for the most recent apply job: Select the job link under **Jobs**.
      2. On the job details page, select **Download Terraform state**.
  3. [Update the state file using Terraform CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm)
    1. Set up Terraform CLI on your local machine.
For instructions, see [Terraform CLI](https://developer.hashicorp.com/terraform/cli).
    2. On your local machine, go to Terraform CLI and navigate to the directory containing the downloaded Terraform configuration and state file.
    3. For each [unmanaged resource previously identified](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__unmanaged-resources), import the state file by running the `terraform import` command:
```
terraform import -state=<path_to_tfstate_file> -var-file="<path_to_credentials_file>" -var-file="<path_to_env_file>" <resource_name> <resource_ocid>
```

Example:
```
terraform import -state=example.tfstate -var-file="credentials.tfvars" -var-file="environments.tfvars" module.operations.oci_identity_compartment.move_compartment ocid1.compartment.oc1..exampleid
```

For more information about this command, see [Terraform Import CLI Command](https://developer.hashicorp.com/terraform/cli/commands/import).
    4. Refresh the state file by running the `terraform refresh` command:
**Note** To refresh for a specific resource, use the refresh target `-target=<resource>`.
For more information about this command, see [Terraform Refresh CLI Command](https://developer.hashicorp.com/terraform/cli/commands/refresh).
  4. Manually update the downloaded Terraform configuration to include the [unmanaged resource previously identified](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__unmanaged-resources).
If any unresolved drift remains in [the drift detection report](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__drift), address those differences in your manual update.
  5. [Update the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm)
    1. Access the stack's details page again.
      1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
      2. Under **List Scope** , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
      3. Select the name of the stack to display its details page.
    2. Import the refreshed state file to the stack.
      1. Go to **More actions** and select **Import state**.
      2. In the **Import state** dialog, add your Terraform state file, either by dragging and dropping it onto the dialog's control, or by selecting **Browse** and navigating to the file location.
      3. Select **Import**.
    3. Upload the [manually edited Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__config) to the stack.
      1. In the **Stack information** tab, next to **Terraform configuration** , select **Upload**.
      2. In the **Edit stack** dialog, under **Stack configuration** , select **.Zip file** and add your revised Terraform configuration.
You can either drag and drop your Terraform configuration .zip file onto the control or select **Browse** and navigate to the location of the .zip file.
      3. Select **Next** as needed and then select **Save changes**. 
  6. [Confirm that infrastructure is up-to-date](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm)
    1. Select **Plan**.
    2. In the **Plan** dialog, review the plan job **Name** and update it if needed.
    3. Select **Plan**. 
The new plan job is listed under **Jobs** , with an initial state of **Accepted**. Soon the status changes to **In progress**. When the job is complete, view the job log to confirm no changes. 
Example of a job log reporting no changes:
```
No changes. Infrastructure is up-to-date.
This means that Terraform did not detect any differences between your
configuration and real physical resources that exist. As a result, no
actions need to be performed. 
```

Congratulations! You have successfully added previously unmanaged resources to the stack. The added resources are now managed by Resource Manager.


Was this article helpful?
YesNo

