Updated 2023-01-04
# Creating a Job
Create a job in Resource Manager, such as plan, apply, or destroy.
**Note** A job might fail because of a downstream service issue. For example, an apply job for creating a compute instance might fail because of a temporary connectivity issue in the Compute service. When a job fails because of downstream service issue, the job retries according to the Go SDK default retry policy. See [Go SDK for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/tools/go/latest/).
You can perform the following job creation tasks:
  * [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.")
  * [Creating a Plan Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm#top "Create a plan rollback job in Resource Manager.")
  * [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.")
  * [Creating an Apply Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager.")
  * [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.")
  * [Creating a Destroy Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.")
  * [Bulk Destroying Resources and Deleting Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/bulk-destroy-delete2.htm#bulk-destroy-delete2 "For the specified compartment, use the following script to delete all the stacks in Resource Manager and destroy all the resources associated with the corresponding stacks.")


Was this article helpful?
YesNo

