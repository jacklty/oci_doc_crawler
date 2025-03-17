Updated 2024-10-08
# Getting Logs for a Job
View console logs for a job in Resource Manager.
**Note**
For plan jobs, the log file is the same as the execution plan. Review the execution plan to ensure that it lists the resources you intend to provision. View the log file and note the "message" fields in the sequence of log entries. These values represent the sequence of operations specified in the configuration.
If you see problems or errors and want to make changes, then update the appropriate [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") (`.tf` file), [update the stack to use the revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#top "Update the zip file or folder Terraform configuration used by a stack in Resource Manager. The updated configuration is used when you run jobs on the stack. A folder-based update is available using the Console only."), [run a plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager."), and then [review the new execution plan (output of the plan job)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#top "Download the output of a plan job in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm)


  * These steps show how to get logs for a job in a compartment. You can also get logs for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. On the job's details page, select **Logs**.
  * Use the `oci resource-manager job get-job-logs[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)` command and required parameters to get logs for a job as a paged list of entries.
Command
CopyTry It
```
oci resource-manager job get-job-logs [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm)
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

  * Use the [GetJobLogs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobLogs) operation to get logs for a job.


Was this article helpful?
YesNo

