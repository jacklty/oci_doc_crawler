Updated 2024-06-06
# Details for Resource Manager
Review details for writing policies to control access to the Resource Manager service.
## Aggregate Resource-Type 🔗 
`orm-family`
## Individual Resource-Types 🔗 
`orm-config-source-providers`
`orm-jobs`
`orm-private-endpoints`
`orm-stacks`
`orm-template`
`orm-work-requests`
## Supported Variables 🔗 
Resource Manager supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)), plus the ones listed here.
The `orm-jobs` resource type can use the following variables. 
Variable | Variable Type | Comments  
---|---|---  
`target.job.operation` |  String |  Use this variable to control access for running specified job types. For example, to limit access to PLAN and APPLY jobs, use the following phrase: `where any {target.job.operation = 'PLAN', target.job.operation = 'APPLY'}`  
`target.stack.id` |  String | Use this variable to limit access to specified stacks. For example, use the following phrase: `where any {target.stack.id = ocid1.ormstack.uniqueid1, target.stack.id = ocid1.ormstack.uniqueid2}`  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access..
[orm-config-source-providers](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  `ORM_CONFIG_SOURCE_PROVIDER_INSPECT` | `ListConfigurationSourceProviders` |  none  
read |  `INSPECT +` `ORM_CONFIG_SOURCE_PROVIDER_READ` | `GetConfigurationSourceProvider` | `CreateStack`: When creating stacks that use configuration source providers (`configSourceType` value `GIT_CONFIG_SOURCE`), also need `manage orm-stacks`  
use |  `READ +` no extra |  no extra |  none  
manage |  `USE +` `ORM_CONFIG_SOURCE_PROVIDER_CREATE` `ORM_CONFIG_SOURCE_PROVIDER_UPDATE` `ORM_CONFIG_SOURCE_PROVIDER_MOVE` `ORM_CONFIG_SOURCE_PROVIDER_DELETE` |  `CreateConfigurationSourceProvider` `UpdateConfigurationSourceProvider` `ChangeConfigurationSourceProviderCompartment` `DeleteConfigurationSourceProvider` |  none  
[orm-jobs](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  `ORM_JOB_INSPECT` | `ListJobs` |  none  
read |  `INSPECT +` `ORM_JOB_READ` |  `GetJob` `GetJobTfState` `GetJobTfConfig` `GetJobTfPlan` `GetJobLogs` `GetJobLogsContent` `ListJobAssociatedResources` `ListJobOutputs` |  none  
use |  `READ +` no extra |  no extra |  none  
manage |  `USE +` `ORM_JOB_MANAGE` |  `UpdateJob` `CancelJob` | `CreateJob` (also need `use orm-stacks`)   
[orm-private-endpoints](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | `ORM_PRIVATE_ENDPOINT_INSPECT` | `ListPrivateEndpoints` |  none  
read |  `INSPECT +` `ORM_PRIVATE_ENDPOINT_READ` |  `GetPrivateEndpoint` `GetReachableIp` |  none  
use |  `READ +` `ORM_PRIVATE_ENDPOINT_UPDATE` |  `UpdatePrivateEndpoint` |  none  
manage |  `USE +` `ORM_PRIVATE_ENDPOINT_CREATE` `ORM_PRIVATE_ENDPOINT_DELETE` `ORM_PRIVATE_ENDPOINT_MOVE` |  `ChangePrivateEndpointCompartment` `CreatePrivateEndpoint` `DeletePrivateEndpoint` |  none  
[orm-stacks](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  `ORM_STACK_INSPECT` |  `ListResourceDiscoveryServices` `ListStacks` `ListTerraformVersions` |  none  
read |  `INSPECT +` `ORM_STACK_READ` |  `GetStack` `GetStackTfConfig` `GetStackTfState` `ListStackAssociatedResources` `ListStackResourceDriftDetails` |  none  
use |  `READ +` `ORM_STACK_USE` |  no extra | `CreateJob` (also need `manage orm-jobs`)   
manage |  `USE +` `ORM_STACK_CREATE` `ORM_STACK_UPDATE` `ORM_STACK_MOVE` `ORM_STACK_DELETE` |  `CreateStack` (unless using configuration source providers) `UpdateStack` `ChangeStackCompartment` `DeleteStack` `DetectStateDrift` `ListTerraformVersions` | `CreateStack`: When creating stacks that use configuration source providers (`configSourceType` value `GIT_CONFIG_SOURCE`), also need `read orm-config-source-providers`  
[orm-template](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | `ORM_TEMPLATE_INSPECT` | `ListTemplates` |  none  
read |  `INSPECT +` `ORM_TEMPLATE_READ` |  ``GetTemplate`` ``GetTemplateLogo`` ``GetTemplateTfConfig`` |  none  
use |  `READ +` `ORM_TEMPLATE_UPDATE` |  `UpdateTemplate` |  none  
manage |  `USE +` `ORM_TEMPLATE_CREATE` `ORM_TEMPLATE_DELETE` `ORM_TEMPLATE_MOVE` |  `ChangeTemplateCompartment` `CreateTemplate` `DeleteTemplate` |  none  
[orm-work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  `ORM_WORK_REQUEST_INSPECT` | `ListWorkRequests` |  none  
read |  `INSPECT +` `ORM_WORK_REQUEST_READ` |  `ListWorkRequestErrors` `ListWorkRequestLogs` `GetWorkRequest` |  none  
use |  `READ +` no extra |  no extra |  none  
manage |  `USE +` no extra |  no extra |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`CancelJob` |  `ORM_JOB_MANAGE`  
`ChangeConfigurationSourceProviderCompartment` |  `ORM_CONFIG_SOURCE_PROVIDER_MOVE`  
`ChangePrivateEndpointCompartment` | `ORM_PRIVATE_ENDPOINT_MOVE`  
`ChangeStackCompartment` |  `ORM_STACK_MOVE`  
`ChangeTemplateCompartment` | `ORM_TEMPLATE_MOVE`  
`CreateConfigurationSourceProvider` | `ORM_CONFIG_SOURCE_PROVIDER_CREATE`  
`CreateJob` | `ORM_JOB_MANAGE and ORM_STACK_USE`  
`CreatePrivateEndpoint` | `ORM_PRIVATE_ENDPOINT_CREATE`  
`CreateStack` |  `ORM_STACK_CREATE` if not using configuration source providers.  If using configuration source providers (`configSourceType` value `GIT_CONFIG_SOURCE`), also need `ORM_CONFIG_SOURCE_PROVIDER_READ`  
`p` |  `ORM_TEMPLATE_CREATE`  
`DeleteConfigurationSourceProvider` |  `ORM_CONFIG_SOURCE_PROVIDER_DELETE`  
`DeletePrivateEndpoint` |  `ORM_PRIVATE_ENDPOINT_DELETE`  
`DeleteStack` |  `ORM_STACK_DELETE`  
`DeleteTemplate` |  `ORM_TEMPLATE_DELETE`  
`DetectStateDrift` |  `ORM_STACK_UPDATE`  
`GetConfigurationSourceProvider` |  `ORM_CONFIG_SOURCE_PROVIDER_READ`  
`GetJob` |  `ORM_JOB_READ`  
`GetJobLogs` |  `ORM_JOB_READ`  
`GetJobLogsContent` |  `ORM_JOB_READ`  
`GetJobTfConfig` |  `ORM_JOB_READ`  
`GetJobTfPlan` |  `ORM_JOB_READ`  
`GetJobTfState` |  `ORM_JOB_READ`  
`GetPrivateEndpoint` |  `ORM_PRIVATE_ENDPOINT_READ`  
`GetReachableIp` |  `ORM_PRIVATE_ENDPOINT_READ`  
`GetStack` |  `ORM_STACK_READ`  
`GetStackTfConfig` |  `ORM_STACK_READ`  
`GetStackTfState` |  `ORM_STACK_READ`  
`GetTemplate` |  `ORM_TEMPLATE_READ`  
`GetTemplateLogo` |  `ORM_TEMPLATE_READ`  
`GetTemplateTfConfig` |  `ORM_TEMPLATE_READ`  
`GetWorkRequest` |  `ORM_WORK_REQUEST_READ`  
`ListConfigurationSourceProviders` |  `ORM_CONFIG_SOURCE_PROVIDER_INSPECT`  
`ListJobAssociatedResources` |  `ORM_JOB_READ`  
`ListJobOutputs` |  `ORM_JOB_READ`  
`ListJobs` |  `ORM_JOB_INSPECT`  
`ListPrivateEndpoints` |  `ORM_PRIVATE_ENDPOINT_INSPECT`  
`ListResourceDiscoveryServices` |  `ORM_STACK_INSPECT`  
`ListStackAssociatedResources` |  `ORM_STACK_READ`  
`ListStackResourceDriftDetails` |  `ORM_STACK_READ`  
`ListStacks` |  `ORM_STACK_INSPECT`  
`ListTemplateCategories` | None  
`ListTemplates` |  `ORM_TEMPLATE_INSPECT`  
`ListTerraformVersions` |  `ORM_STACK_INSPECT`  
`ListWorkRequestErrors` |  `ORM_WORK_REQUEST_READ`  
`ListWorkRequestLogs` |  `ORM_WORK_REQUEST_READ`  
`ListWorkRequests` |  `ORM_WORK_REQUEST_INSPECT`  
`UpdateConfigurationSourceProvider` |  `ORM_CONFIG_SOURCE_PROVIDER_UPDATE`  
`UpdateJob` |  `ORM_JOB_MANAGE`  
`UpdatePrivateEndpoint` |  `ORM_PRIVATE_ENDPOINT_UPDATE`  
`UpdateStack` |  `ORM_STACK_UPDATE`  
`UpdateTemplate` |  `ORM_TEMPLATE_UPDATE`  
Was this article helpful?
YesNo

