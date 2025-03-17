Updated 2024-09-26
# Details for API Gateway
This topic covers details for writing policies to control access to API Gateway.
## Resource-Types 🔗 
### Aggregate Resource-Type
`api-gateway-family`
### Individual Resource-Types
  * `api-gateways`
  * `api-deployments`
  * `api-definitions`
  * `api-workrequests`
  * `api-certificates`
  * `api-sdks`
  * `api-subscribers`
  * `api-usage-plans`


### Comments
A policy that uses `<verb> api-gateway-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm#apigatewayverbresourcetypecombination) for details of the API operations covered by each verb, for each individual resource-type included in `api-gateway-family`.
## Supported Variables 🔗 
API Gateway supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `api-gateways` resource-type includes the same permissions and API operations as the `inspect` verb, plus the API_GATEWAY_READ permission and a number of API operations (e.g., `GetGateway`, etc.). The `use` verb covers additional permissions and API operations compared to `read`. Lastly, `manage` covers more permissions and operations compared to `use`.
[api-gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_GATEWAY_LIST | `ListGateways` | none  
read | INSPECT + API_GATEWAY_READ | INSPECT + `GetGateway` | `GetDeployment` (also needs `read api-deployments`)   
use | READ + API_GATEWAY_ADD_DEPLOYMENT API_GATEWAY_REMOVE_DEPLOYMENT | no extra | `CreateDeployment` and `DeleteDeployment` (both also need `manage api-deployments`) `UpdateDeployment` (also needs `use api-deployments`)  
manage | USE + API_GATEWAY_CREATE API_GATEWAY_DELETE API_GATEWAY_UPDATE API_GATEWAY_MOVE | USE + `DeleteGateway` `UpdateGateway` `ChangeGatewayCompartment` | `CreateGateway` (also needs `use                   api-certificates`)  
[api-deployments](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_DEPLOYMENT_LIST | `ListDeployments` | none  
read | INSPECT + API_DEPLOYMENT_READ | no extra | `GetDeployment` (also needs `read api-gateways`)   
use | READ + API_DEPLOYMENT_UPDATE | no extra | `UpdateDeployment` (also needs `use api-gateways`)   
manage | USE + API_DEPLOYMENT_CREATE API_DEPLOYMENT_DELETE API_DEPLOYMENT_MOVE | USE + `ChangeDeploymentCompartment` | `CreateDeployment` and `DeleteDeployment` (both also need `use api-gateways`)   
[api-definitions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_DEFINITION_LIST | `ListApis` | none  
read | INSPECT + API_DEFINITION_READ | INSPECT + `GetApi` `GetApiContent` `GetApiDeploymentSpecification` `GetApiValidations` |  none  
use | READ + API_DEFINITION_UPDATE | READ + `UpdateApi` |  none  
manage | USE + API_DEFINITION_CREATE API_DEFINITION_DELETE API_DEPLOYMENT_MOVE | USE + `CreateApi` `DeleteApi` `ChangeApiCompartment` |  none  
[api-workrequests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_WORK_REQUEST_LIST | `ListWorkRequests` | none  
read | INSPECT + API_WORK_REQUEST_READ | INSPECT + `GetWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` | none  
use | READ + API_WORK_REQUEST_CANCEL | READ + `CancelWorkRequest` | none  
manage | no extra | no extra | none  
[api-certificates](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_CERTIFICATE_LIST | `ListCertificates` | none  
read | INSPECT + API_CERTIFICATE_READ | INSPECT + `GetCertificate` | none  
use | READ + API_CERTIFICATE_APPLY_TO_GATEWAY | no extra | `CreateGateway` (also needs `manage                   api-gateways`)  
manage | USE + API_CERTIFICATE_CREATE API_CERTIFICATE_DELETE API_CERTIFICATE_UPDATE API_CERTIFICATE_MOVE | USE + CreateCertificate DeleteCertificate UpdateCertificate ChangeCertificateCompartment | none  
[api-sdks](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_SDK_LIST | `ListSdks` | none  
read | INSPECT + API_SDK_READ | INSPECT + `GetSdk` | none  
use | READ + API_SDK_UPDATE |  READ +`UpdateSdk` | none  
manage | USE + API_SDK_CREATE API_SDK_DELETE | USE + `CreateSdk` `DeleteSdk` `ListSdkLanguageTypes` | none  
[api-subscribers](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_SUBSCRIBER_LIST | `ListSubscribers` | none  
read | INSPECT + API_SUBSCRIBER_READ | INSPECT + `GetSubscriber` | none  
use | READ + API_SUBSCRIBER_UPDATE |  no extra | `UpdateSubscriber` (also needs `read api-usage-plans` to update subscribed usage plans during subscriber update)  
manage | USE + API_SUBSCRIBER_CREATE API_SUBSCRIBER_DELETE API_SUBSCRIBER_MOVE |  USE + `DeleteSubscriber` `ChangeSubscriberCompartment` | `CreateSubscriber` (also needs `read api-usage-plans` to add subscribed usage plans during subscriber creation)  
[api-usage-plans](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/apigatewaypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | API_USAGE_PLAN_LIST | `ListUsagePlans` | none  
read | INSPECT + API_USAGE_PLAN_READ | INSPECT + `GetUsagePlan` | none  
use | READ + API_USAGE_PLAN_UPDATE |  no extra | `UpdateUsagePlan` (also needs `read api-deployments` to update target API deployments in entitlements during usage plan update)  
manage | USE + API_USAGE_PLAN_CREATE API_USAGE_PLAN_DELETE API_USAGE_PLAN_MOVE |  USE + `DeleteUsagePlan` `ChangeUsagePlanCompartment` | `CreateUsagePlan` (also needs`read api-deployments` to add target API deployments to entitlements during usage plan creation)  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type. 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListGateways` | API_GATEWAY_LIST  
`CreateGateway` | API_GATEWAY_CREATE and API_CERTIFICATE_APPLY_TO_GATEWAY  
`GetGateway` | API_GATEWAY_READ  
`UpdateGateway` | API_GATEWAY_UPDATE  
`DeleteGateway` | API_GATEWAY_DELETE  
`ChangeGatewayCompartment` | API_GATEWAY_READ and API_GATEWAY_UPDATE and API_GATEWAY_MOVE  
`ListDeployments` | API_DEPLOYMENT_LIST  
`CreateDeployment` |  API_DEPLOYMENT_CREATE and API_GATEWAY_READ and API_GATEWAY_ADD_DEPLOYMENT  
`GetDeployment` | API_DEPLOYMENT_READ and API_GATEWAY_READ  
`UpdateDeployment` | API_DEPLOYMENT_UPDATE and API_GATEWAY_READ and API_GATEWAY_ADD_DEPLOYMENT  
`DeleteDeployment` | API_DEPLOYMENT_DELETE and API_GATEWAY_READ and API_GATEWAY_REMOVE_DEPLOYMENT  
`ChangeDeploymentCompartment` | API_DEPLOYMENT_READ and API_DEPLOYMENT_UPDATE and API_DEPLOYMENT_MOVE  
`ListApis` | API_DEFINITION_LIST  
`CreateApi` | API_DEFINITION_CREATE  
`GetApi` | API_DEFINITION_READ  
`GetApiContent` | API_DEFINITION_READ  
`GetApiDeploymentSpecification` | API_DEFINITION_READ  
`GetApiValidations` | API_DEFINITION_READ  
`UpdateApi` | API_DEFINITION_UPDATE   
`DeleteApi` | API_DEFINITION_DELETE  
`ChangeApiCompartment` | API_DEFINITION_MOVE  
`ListWorkRequests` |  API_WORK_REQUEST_LIST  
`GetWorkRequest` |  API_WORK_REQUEST_READ  
`CancelWorkRequest` |  API_WORK_REQUEST_CANCEL  
`ListWorkRequestErrors` |  API_WORK_REQUEST_READ  
`ListWorkRequestLogs` |  API_WORK_REQUEST_READ  
`ListCertificates` | API_CERTIFICATE_LIST  
`CreateCertificate` | API_CERTIFICATE_CREATE  
`GetCertificate` | API_CERTIFICATE_READ  
`UpdateCertificate` | API_CERTIFICATE_UPDATE  
`DeleteCertificate` | API_CERTIFICATE_DELETE  
`ChangeCertificateCompartment` | API_CERTIFICATE_MOVE  
`ListSdks` | API_SDK_LIST  
`GetSdk` | API_SDK_READ  
`UpdateSdk` | API_SDK_UPDATE  
`CreateSdk` | API_SDK_CREATE  
`ListSdkLanguageTypes` | API_SDK_CREATE  
`DeleteSdk` | API_SDK_DELETE  
`ListSubscribers` | API_SUBSCRIBER_LIST  
`GetSubscriber` | API_SUBSCRIBER_READ  
`UpdateSubscriber` | API_SUBSCRIBER_UPDATEAPI_USAGE_PLAN_READ is necessary to update subscribed usage plans during subscriber update.  
`CreateSubscriber` | API_SUBSCRIBER_CREATEAPI_USAGE_PLAN_READ is necessary to add subscribed usage plans during subscriber creation.  
`DeleteSubscriber` | API_SUBSCRIBER_DELETE  
`ChangeSubscriberCompartment` | API_SUBSCRIBER_MOVE  
`ListUsagePlans` | API_USAGE_PLAN_LIST  
`GetUsagePlan` | API_USAGE_PLAN_READ  
`UpdateUsagePlan` | API_USAGE_PLAN_UPDATEAPI_DEPLOYMENT_READ is necessary to update target API deployments in entitlements during usage plan update.  
`CreateUsagePlan` | API_USAGE_PLAN_CREATEAPI_DEPLOYMENT_READ is necessary to add target API deployments to entitlements during usage plan creation.  
`DeleteUsagePlan` | API_USAGE_PLAN_DELETE  
`ChangeUsagePlanCompartment` | API_USAGE_PLAN_MOVE  
Was this article helpful?
YesNo

