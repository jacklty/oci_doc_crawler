Updated 2025-01-07
# Getting a Job's State File
Download the Terraform state file (`.json`) from a completed apply, apply rollback, or import job in Resource Manager.
**Note** To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a `409` error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm)


  * These steps show how to get the state for a job in a compartment. You can also get the state for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, find the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. For the job that you want, select **View state**
The job's details page opens with **View state** selected.
Don't see **View state**? Check that the job has finished running, and that it's an [apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."), [apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager."), or [import job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack."). No state files are available for [canceled](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#top "Cancel a running job in Resource Manager.") jobs.
    3. (Optional) Select **Show changes in this version**.
    4. (Optional) Select **Download Terraform state**.
  * Use the `oci resource-manager job get-job-tf-state[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-state.html)` command and required parameters to get a job's state.
Command
CopyTry It
```
oci resource-manager job get-job-tf-state [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetJobTfState](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobTfState) operation to get a job's state.
[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm)
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



## Example State File 🔗 
The following example state file is from a successful apply job for the Document [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.").
[Expand to see example](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm)
```
{
 "version": 4,
 "terraform_version": "0.14.11",
 "serial": 3,
 "lineage": "example-guid",
 "outputs": {},
 "resources": [
  {
   "mode": "managed",
   "type": "oci_identity_group",
   "name": "document-group",
   "provider": "provider[\"registry.terraform.io/hashicorp/oci\"]",
   "instances": [
    {
     "schema_version": 0,
     "attributes": {
      "compartment_id": "ocid1.tenancy.oc1..example-guid",
      "defined_tags": {},
      "description": "Document Group",
      "freeform_tags": {},
      "id": "ocid1.group.oc1..example-guid",
      "inactive_state": null,
      "name": "DocumentGroup",
      "state": "ACTIVE",
      "time_created": "2023-06-21 14:48:21.832 +0000 UTC",
      "timeouts": null
     },
     "sensitive_attributes": [],
     "private": "example-guid"
    }
   ]
  },
  {
   "mode": "managed",
   "type": "oci_identity_policy",
   "name": "document-root-policy",
   "provider": "provider[\"registry.terraform.io/hashicorp/oci\"]",
   "instances": [
    {
     "schema_version": 0,
     "attributes": {
      "ETag": "example-guid",
      "compartment_id": "ocid1.tenancy.oc1..example-guid",
      "defined_tags": {},
      "description": "Document Root Policies",
      "freeform_tags": {},
      "id": "ocid1.policy.oc1..example-guid",
      "inactive_state": null,
      "lastUpdateETag": "example-guid",
      "name": "DocumentRootPolicies",
      "policyHash": "example-guid",
      "state": "ACTIVE",
      "statements": [
       "Allow group DocumentGroup to manage ai-service-document-family in tenancy",
       "Allow group DocumentGroup to use object-family in tenancy"
      ],
      "time_created": "2023-06-21 14:48:24.068 +0000 UTC",
      "timeouts": null,
      "version_date": null
     },
     "sensitive_attributes": [],
     "private": "example-guid",
     "dependencies": [
      "oci_identity_group.document-group"
     ]
    }
   ]
  }
 ]
}
```

Was this article helpful?
YesNo

