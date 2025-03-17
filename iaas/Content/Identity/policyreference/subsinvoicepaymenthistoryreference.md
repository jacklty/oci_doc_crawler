Updated 2024-06-06
# Details for Subscriptions, Invoices, and Payment History
This topic covers details for writing policies to control access to the **Subscriptions** , **Invoices** , and **Payment History** pages in Billing and Cost Management.
## Resource-Types 🔗 
  * `billing-schedules`
  * `computed-usages`
  * `invoices`
  * `invoice-preferences`
  * `subscription`
  * `subscribed-services`
  * `rate-cards`


## Supported Variables 🔗 
Subscriptions, Invoices, and Payment History support all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus additional ones listed here:
**Required variables** (supplied by service for every request):
Variable | Variable Type | Comments  
---|---|---  
`target.resource.kind` | String | The resource kind name of the primary resource for the request.  
**Automatic Variables** (supplied by the SDK for every request):
Variable | Variable Type | Comments  
---|---|---  
`target.tenant.id` | Entity (OCID) | The OCID of the target tenant ID.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
### billing-schedules 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | BILLING_SCHEDULE_INSPECT | `ListBillingSchedules` | none  
READ | _INSPECT_ + BILLING_SCHEDULE_READ | _INSPECT_ + `ListBillingSchedules` | none  
USE | - | - | none  
MANAGE | - | none  
### computed-usages 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | COMPUTED_USAGE_INSPECT | `ListComputedUsages` `ListSubscribedServiceUsageAggregations` | none  
READ | _INSPECT_ + COMPUTED_USAGE_READ | _INSPECT_ + `GetComputedUsage` | none  
USE | - | - | none  
MANAGE | - | - | none  
### invoices 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | INVOICE_INSPECTINVOICE_COMPUTED_USAGE_INSPECT | `ListInvoices` `ListInvoicedComputedUsages` | none  
READ | _INSPECT_ + INVOICE_READ | _INSPECT_ + `GetBillingScheduleById` | none  
USE | - | - | none  
MANAGE | _READ_ + INVOICE_MANAGE | _READ_ + `PayInvoice` | none  
### invoice-preferences 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | - | -  | none  
READ | INVOICE_PREFERENCE_READ | `GetInvoicePreferences` | none  
USE | -  | - | none  
MANAGE | -  | - | none  
### subscription 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | - | -  | none  
READ | SUBSCRIPTION_INFO_READ | `GetSubscription``ListSubscriptions` | none  
USE | -  | - | none  
MANAGE | -  | - | none  
### subscribed-services 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | SUBSCRIBED_SERVICE_INSPECT | `ListSubscribedServices``ListCommitments` | none  
READ | _INSPECT_ + SUBSCRIBED_SERVICE_READ | _INSPECT_ + `GetCommitment``GetSubscribedService` | none  
USE | - | - | -  
MANAGE | - | - | none  
### rate-cards 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | RATE_CARD_INSPECT | `ListRateCards` | none  
READ | _INSPECT_ + RATE_CARD_READ | _INSPECT_ + `GetRateCard` | none  
USE | - | - | none  
MANAGE | - | - | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
**ListBillingSchedules** | BILLING_SCHEDULE_INSPECT, BILLING_SCHEDULE_READ  
**ListBillingScheduleSummary** | INVOICE_INSPECT  
**ListBillingScheduleAggregations** | INVOICE_INSPECT  
**GetBillingScheduleById** | INVOICE_INSPECT, INVOICE_READ  
**GetInvoicePreferences** | INVOICE_PREFERENCE_READ  
**ListInvoices** | INVOICE_INSPECT  
**PayInvoice** | INVOICE_MANAGE  
**ListInvoicedComputedUsages** | INVOICE_COMPUTED_USAGE_INSPECT  
**ListSalesOrderHeaders** | SALES_ORDER_INSPECT  
**GetSalesOrderHeader** | SALES_ORDER_INSPECT, SALES_ORDER_READ  
**ListSalesOrderLines** | SALES_ORDER_INSPECT  
**ListSubscriptions** | SUBSCRIPTION_INFO_READ  
**GetSubscription** | SUBSCRIPTION_INFO_READ  
**ListSubscribedServices** | SUBSCRIBED_SERVICE_INSPECT  
**GetSubscribedService** | SUBSCRIBED_SERVICE_INSPECT, SUBSCRIBED_SERVICE_READ  
**ListCommitments** | SUBSCRIBED_SERVICE_INSPECT  
**GetCommitment** | SUBSCRIBED_SERVICE_INSPECT, SUBSCRIBED_SERVICE_READ  
**GetRateCard** | RATE_CARD_INSPECT, RATE_CARD_READ  
**ListRateCards** | RATE_CARD_INSPECT  
**ListComputedUsages** | COMPUTED_USAGE_INSPECT  
**GetComputedUsage** | COMPUTED_USAGE_INSPECT, COMPUTED_USAGE_READ  
**ListSubscribedServiceUsageAggregations** | COMPUTED_USAGE_INSPECT  
Was this article helpful?
YesNo

