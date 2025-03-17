Updated 2024-10-08
# Retrieving the Latest Providers
Within the version constraints of the Terraform configuration, retrieve the latest versions available from the configured source of Terraform providers when running a job. You can retrieve the latest providers when running the following types of jobs: plan, apply, destroy, import state, and run drift detection.
When retrieving latest versions of providers for a job, Resource Manager automatically manages [dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock) for the stack.
This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack. Providers are updated within the version constraints of the Terraform configuration.
## Before You Begin 🔗 
Review prerequisites for retrieving the latest providers.
  * The stack must use Terraform version 0.14 or later
  * If the stack is older, then it must be upgraded to use Terraform Registry. See [Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-lock-file.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-lock-file.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-lock-file.htm)


  * These steps show how to retrieve the latest providers for a job in a stack. You can also retrieve the latest providers for a job [in a compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Select the option for running the [type of job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.") that you want.
    3. In the panel for the job type that you selected, select **Show advanced options** and select **Upgrade provider versions**.
    4. Run the [job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.").
  * Use the command and required parameters for the type of job you want to run, and set `--job-operation-details-is-provider-upgrade-required` to `true`.
For example, to retrieve the latest providers when running a plan job, use the `oci resource-manager job create-plan-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)` command to run a plan job, with `--job-operation-details-is-provider-upgrade-required` set to `true`.
Copy
```
oci resource-manager job create-plan-job --stack-id <stack_ocid> --job-operation-details-is-provider-upgrade-required true
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to retrieve the latest providers when running a job.
When defining [CreateJobDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateJobDetails), specify `jobOperationDetails` ([CreateJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateJobOperationDetails)), setting `isProviderUpgradeRequired` to `true`.


Was this article helpful?
YesNo

