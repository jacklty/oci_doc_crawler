Updated 2024-09-26
# Details for Logging Analytics
This topic covers details for writing policies to control access to the Logging Analytics service.
## Resource-Types 🔗 
### Individual Resource-Types 🔗 
`loganalytics-category`
`loganalytics-config-work-request`
`loganalytics-em-bridge`
`loganalytics-entity`
`loganalytics-entity-type`
`loganalytics-field`
`loganalytics-ingesttime-rule`
`loganalytics-label`
`loganalytics-lifecycle`
`loganalytics-log-group`
`loganalytics-lookup`
`loganalytics-object-collection-rule`
`loganalytics-ondemand-upload`
`loganalytics-parser`
`loganalytics-query`
`loganalytics-queryjob-work-request`
`loganalytics-scheduled-task`
`loganalytics-source`
`loganalytics-storage`
`loganalytics-storage-work-request`
### Aggregate Resource-Types 🔗 
The `loganalytics-features-family` aggregrate resource-type covers these individual resource-types (resource kinds that are not modeled as resources; that is, resource kinds that do not belong to a compartment):
`loganalytics-category`
`loganalytics-entity-type`
`loganalytics-field`
`loganalytics-label`
`loganalytics-lifecycle`
`loganalytics-lookup`
`loganalytics-ondemand-upload`
`loganalytics-parser`
`loganalytics-query`
`loganalytics-source`
`loganalytics-storage`
The `loganalytics-resources-family` aggregrate resource-type covers these individual resource-types (resource kinds that are modeled as resources; that is, resource kinds that belong to a compartment):
`loganalytics-config-work-request`
`loganalytics-em-bridge`
`loganalytics-entity`
`loganalytics-ingesttime-rule`
`loganalytics-log-group`
`loganalytics-object-collection-rule`
`loganalytics-queryjob-work-request`
`loganalytics-scheduled-task`
`loganalytics-storage-work-request`
### Comments 🔗 
A policy that uses `<verb> loganalytics-features-family` or `<verb> loganalytics-resources-family` is equivalent to writing one with a separate `<verb> <individual           resource-type>` statement for each of the individual resource-types in the family.
See the table in [Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm#permissions) for details of the API operations covered by each verb, for each individual resource-type.
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[loganalytics-category](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | LOG_ANALYTICS_CATEGORY_INSPECT |  `ListCategories` `ListResourceCategories` |  none  
read | INSPECT +LOG_ANALYTICS_CATEGORY_READ |  `GetCategory` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + LOG_ANALYTICS_CATEGORY_UPDATE LOG_ANALYTICS_CATEGORY_DELETE |  `UpdateResourceCategories` `DeleteResourceCategories` |  none  
[loganalytics-config-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_CONFIG_WORK_REQUEST_INSPECT | `ListConfigWorkRequests` |  none  
read |  INSPECT + LOG_ANALYTICS_CONFIG_WORK_REQUEST_READ | `GetConfigWorkRequest` |  none  
use |  READ + LOG_ANALYTICS_CONFIG_WORK_REQUEST_CREATE LOG_ANALYTICS_CONFIG_WORK_REQUEST_DELETE |  no extra |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-em-bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_EM_BRIDGE_INSPECT |  `ListLogAnalyticsEMBridges` `GetLogAnalyticsEMBridgeSummary` |  none  
read |  INSPECT + LOG_ANALYTICS_EM_BRIDGE_READ |  `GetLogAnalyticsEMBridge` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + LOG_ANALYTICS_EM_BRIDGE_CREATE LOG_ANALYTICS_EM_BRIDGE_UPDATE LOG_ANALYTICS_EM_BRIDGE_DELETE LOG_ANALYTICS_EM_BRIDGE_MOVE |  `CreateLogAnalyticsEMBridge` `UpdateLogAnalyticsEMBridge` `DeleteLogAnalyticsEMBridge` `ChangeLogAnalyticsEMBridgeCompartment` |  none  
[loganalytics-entity](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_ENTITY_INSPECT | `GetLogAnalyticsEntitiesSummary``ListEntityAssociations``ListLogAnalyticsEntities` |  none  
read |  INSPECT + LOG_ANALYTICS_ENTITY_READ | `GetLogAnalyticsEntity` |  none  
use |  READ + LOG_ANALYTICS_ENTITY_CREATE LOG_ANALYTICS_ENTITY_DELETE LOG_ANALYTICS_ENTITY_MOVE LOG_ANALYTICS_ENTITY_UPDATE LOG_ANALYTICS_ENTITY_UPLOAD_LOGS |  `AddEntityAssociation` `ChangeLogAnalyticsEntityCompartment` `CreateLogAnalyticsEntity` `DeleteLogAnalyticsEntity` `RemoveEntityAssociations` `UpdateLogAnalyticsEntity` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-entity-type](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_ENTITY_TYPE_INSPECT | `ListLogAnalyticsEntityTypes` |  none  
read |  INSPECT + LOG_ANALYTICS_ENTITY_TYPE_READ | `GetLogAnalyticsEntityType` |  none  
use |  READ + LOG_ANALYTICS_ENTITY_TYPE_CREATE LOG_ANALYTICS_ENTITY_TYPE_DELETE LOG_ANALYTICS_ENTITY_TYPE_UPDATE |  `CreateLogAnalyticsEntityType` `DeleteLogAnalyticsEntityType` `UpdateLogAnalyticsEntityType` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-field](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_FIELD_INSPECT |  `GetFieldsSummary` `ListFields` |  none  
read |  INSPECT + LOG_ANALYTICS_FIELD_READ | `GetField` |  none  
use |  READ + LOG_ANALYTICS_FIELD_CREATE LOG_ANALYTICS_FIELD_DELETE LOG_ANALYTICS_FIELD_UPDATE |  `DeleteField` `UpsertField` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-ingesttime-rule](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_INGESTTIME_RULE_INSPECT |  `ListIngestTimeRules` |  none  
read |  INSPECT + LOG_ANALYTICS_INGESTTIME_RULE_READ |  `GetIngestTimeRule` |  none  
use |  READ + LOG_ANALYTICS_INGESTTIME_RULE_CREATE LOG_ANALYTICS_INGESTTIME_RULE_UPDATE LOG_ANALYTICS_INGESTTIME_RULE_DELETE LOG_ANALYTICS_INGESTTIME_RULE_MOVE |  `CreateIngestTimeRule` `UpdateIngestTimeRule` `DeleteIngestTimeRule` `EnableIngestTimeRule` `DisableIngestTimeRule` `ChangeIngestTimeRuleCompartment` |  none  
manage |  USE + none |  no extra |  none  
[loganalytics-label](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_LABEL_INSPECT |  `GetLabelSummary` `ListLabelPriorities` `ListLabels` |  none  
read |  INSPECT + LOG_ANALYTICS_LABEL_READ |  `BatchGetBasicInfo` `GetLabel` `ListLabelSourceDetails` |  none  
use |  READ + LOG_ANALYTICS_LABEL_CREATE LOG_ANALYTICS_LABEL_DELETE LOG_ANALYTICS_LABEL_UPDATE |  `DeleteLabel` `UpsertLabel` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-lifecycle](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_LIFECYCLE_INSPECT | `ListNamespaces` |  none  
read |  INSPECT + LOG_ANALYTICS_LIFECYCLE_READ LOG_ANALYTICS_PREFERENCE_READ |  `GetNamespace` `GetTenantPreferences` |  none  
use |  READ + no extra |  no extra |  none  
manage |  USE + LOG_ANALYTICS_LIFECYCLE_HOMEPAGE_UPDATE LOG_ANALYTICS_PREFERENCE_UPDATE LOG_ANALYTICS_LIFECYCLE_OFFBOARD LOG_ANALYTICS_PREFERENCE_DELETE LOG_ANALYTICS_LIFECYCLE_ONBOARD |  `OffboardNamespace` `OnboardNamespace` `DeleteTenantPreferences` `UpdateTenantPreferences` |  none  
[loganalytics-log-group](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_LOG_GROUP_INSPECT |  `GetLogAnalyticsLogGroupsSummary` `ListLogAnalyticsLogGroups` |  none  
read |  INSPECT + LOG_ANALYTICS_LOG_GROUP_READ | `GetLogAnalyticsLogGroup` |  none  
use |  READ + LOG_ANALYTICS_LOG_GROUP_CREATE LOG_ANALYTICS_LOG_GROUP_UPDATE LOG_ANALYTICS_LOG_GROUP_UPLOAD_LOGS | `ChangeLogAnalyticsLogGroupCompartment``CreateLogAnalyticsLogGroup` `UpdateLogAnalyticsLogGroup` |  none  
manage |  USE + LOG_ANALYTICS_LOG_GROUP_DELETE_LOGS |  `DeleteLogAnalyticsLogGroup` |  none  
[loganalytics-lookup](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_LOOKUP_INSPECT |  none |  none  
read |  INSPECT + LOG_ANALYTICS_LOOKUP_READ |  none |  none  
use |  READ + LOG_ANALYTICS_LOOKUP_CREATE LOG_ANALYTICS_LOOKUP_DELETE LOG_ANALYTICS_LOOKUP_UPDATE |  `RegisterLookups` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-object-collection-rule](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_OBJECT_COLLECTION_RULE_INSPECT | `ListLogAnalyticsObjectCollectionRules` |  none  
read |  INSPECT + LOG_ANALYTICS_OBJECT_COLLECTION_RULE_READ |  no extra |  `GetLogAnalyticsObjectCollectionRule` (also needs `inspect loganalytics-entity`, `inspect                   loganalytics-log-group`, and `inspect                   loganalytics-source`)  
use |  READ + LOG_ANALYTICS_OBJECT_COLLECTION_RULE_CREATE LOG_ANALYTICS_OBJECT_COLLECTION_RULE_UPDATE LOG_ANALYTICS_OBJECT_COLLECTION_RULE_DELETE LOG_ANALYTICS_OBJECT_COLLECTION_RULE_MOVE |  `ChangeLogAnalyticsObjectCollectionRuleCompartment` `DeleteLogAnalyticsObjectCollectionRule` |  `CreateLogAnalyticsObjectCollectionRule`, `UpdateLogAnalyticsObjectCollectionRule` (both also need `use loganalytics-entity`, `use                   loganalytics-log-group`, and `read                   loganalytics-source`)  
manage |  USE + no extra |  no extra |  none  
[loganalytics-ondemand-upload](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_ONDEMAND_UPLOAD_INSPECT |  `ListSupportedCharEncodings` `ListSupportedTimezones` `ListUploads` |  none  
read |  INSPECT + LOG_ANALYTICS_ONDEMAND_UPLOAD_READ |  `GetUpload` `ListUploadWarnings` |  `ListUploadFiles` (also needs `read                   loganalytics-log-group`)  
use |  READ + LOG_ANALYTICS_ONDEMAND_UPLOAD_CREATE |  `ValidateFile` `ValidateSourceMapping` |  `UploadLogFile` (also needs `use                   loganalytics-entity`, `use                   loganalytics-log-group`, and `read                   loganalytics-source`)  
manage |  USE + LOG_ANALYTICS_ONDEMAND_UPLOAD_DELETE |  `DeleteUploadWarning` |  `DeleteUpload` (also needs `manage                   loganalytics-log-group`, `read                   loganalytics-query`, and `read                   compartments`) `DeleteUploadFile` (also needs `manage                   loganalytics-log-group`, `read                   loganalytics-query`, and `read                   compartments`  
[loganalytics-parser](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_PARSER_INSPECT |  `GetParserSummary` `ListParserMetaPlugins` `ListParsers` |  none  
read |  INSPECT + LOG_ANALYTICS_PARSER_READ |  `ExtractStructuredLogFieldPaths` `ExtractStructuredLogHeaderPaths` `GetParser` `ListParserFunctions` `TestParser` |  none  
use |  READ + LOG_ANALYTICS_PARSER_CREATE  LOG_ANALYTICS_PARSER_DELETE LOG_ANALYTICS_PARSER_UPDATE  |  `DeleteParser` `UpsertParser` |  none  
manage |  USE + no extra |  no extra |  none  
[loganalytics-query](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_QUERY_INSPECT |  none |  `Filter`, `ParseQuery` (both also need `read loganalytics-lifecycle`)  
read |  INSPECT + LOG_ANALYTICS_QUERY_VIEW |  none |  `Export` (also needs `read                   loganalytics-lifecycle`, `read                   loganalytics-log-group`, and `read                   compartments` `GetQueryResult` (also needs `read                   loganalytics-lifecycle` and `read                   loganalytics-queryjob-work-request`) `Suggest` (also needs `read                   loganalytics-lifecycle` and `read                   compartments` `Query` (also needs `read                   loganalytics-lifecycle`, `read                   loganalytics-log-group`, `read                   loganalytics-queryjob-work-request`, and `read                   compartments`)  
use |  READ + no extra |  none |  none  
manage |  USE + no extra |  none |  none  
[loganalytics-queryjob-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_INSPECT |  none | `ListQueryWorkRequests` (also needs `read                 loganalytics-lifecycle`)  
read |  INSPECT + LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_READ |  none |  `GetQueryResult` (also needs `read                   loganalytics-lifecycle` and `read                   loganalytics-query`) `GetQueryWorkRequest`, `PutQueryWorkRequestBackground` (both also need `read loganalytics-lifecycle`) `Query` (also needs `read                   loganalytics-lifecycle`, `read                   loganalytics-log-group`, `read                   loganalytics-query`, and `read                   compartments`)  
use |  READ + LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_DELETE |  none | `CancelQueryWorkRequest` (also needs `read                 loganalytics-lifecycle`)  
manage |  no extra |  no extra |  no extra  
[loganalytics-scheduled-task](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_ACCELERATIONTASK_INSPECT LOG_ANALYTICS_PURGETASK_INSPECT LOG_ANALYTICS_SAVEDSEARCHTASK_INSPECT | `ListScheduledTasks` |  none  
read |  INSPECT + LOG_ANALYTICS_ACCELERATIONTASK_READ LOG_ANALYTICS_PURGETASK_READ LOG_ANALYTICS_SAVEDSEARCHTASK_READ |  `Clean` `GetScheduledTask` `Run` |  none  
use |  READ + LOG_ANALYTICS_ACCELERATIONTASK_CREATE LOG_ANALYTICS_ACCELERATIONTASK_DELETE LOG_ANALYTICS_ACCELERATIONTASK_MOVE LOG_ANALYTICS_ACCELERATIONTASK_UPDATE LOG_ANALYTICS_SAVEDSEARCHTASK_CREATE LOG_ANALYTICS_SAVEDSEARCHTASK_DELETE LOG_ANALYTICS_SAVEDSEARCHTASK_MOVE LOG_ANALYTICS_SAVEDSEARCHTASK_UPDATE |  `ChangeScheduledTaskCompartment` for taskType ACCELERATION, ACCELERATION_MAINTENANCE, or SAVED_SEARCH `CreateScheduledTask` for taskType ACCELERATION, ACCELERATION_MAINTENANCE, or SAVED_SEARCH `DeleteScheduledTask` for taskType ACCELERATION, ACCELERATION_MAINTENANCE, or SAVED_SEARCH `UpdateScheduledTask` for taskType ACCELERATION, ACCELERATION_MAINTENANCE, or SAVED_SEARCH |  none  
manage |  USE + LOG_ANALYTICS_PURGETASK_CREATE LOG_ANALYTICS_PURGETASK_DELETE LOG_ANALYTICS_PURGETASK_MOVE LOG_ANALYTICS_PURGETASK_UPDATE |  `ChangeScheduledTaskCompartment` for taskType PURGE `CreateScheduledTask` for taskType PURGE `DeleteScheduledTask` for taskType PURGE `UpdateScheduledTask` for taskType PURGE |  none  
[loganalytics-source](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_SOURCE_INSPECT |  `GetAssociationSummary` `GetSourceSummary` `ListAssociatedEntities` `ListEntitySourceAssociations` `ListMetaSourceTypes` `ListSourceLabelOperators` `ListSourceMetaFunctions` `ListSources` |  none  
read |  INSPECT + LOG_ANALYTICS_SOURCE_READ |  `GetColumnNames` `GetSource` `ListSourceAssociations` `ListSourceExtendedFieldDefinitions` `ListSourcePatterns` `ValidateAssociationParameters` `ValidateSourceExtendedFieldDetails` |  `ExportCustomContent` (also needs `read                   loganalytics-field`, `read                   loganalytics-label`, and `read                   loganalytics-parser`)  
use |  READ + LOG_ANALYTICS_SOURCE_CREATE LOG_ANALYTICS_SOURCE_DELETE LOG_ANALYTICS_SOURCE_ENTITY_ASSOC LOG_ANALYTICS_SOURCE_ENTITY_DISASSOC LOG_ANALYTICS_SOURCE_UPDATE |  `DeleteAssociations` `DeleteSource` `UpsertAssociations` `UpsertSource` `ValidateSource` |  `ImportCustomContent` (also needs `use                   loganalytics-field`, `use                   loganalytics-label`, and `use                   loganalytics-parser`)  
manage |  USE + LOG_ANALYTICS_SOURCE_DISABLE_AUTOASSOC LOG_ANALYTICS_SOURCE_ENABLE_AUTOASSOC |  no extra |  none  
[loganalytics-storage](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_STORAGE_INSPECT |  none |  none  
read |  INSPECT + LOG_ANALYTICS_STORAGE_READ |  `GetStorage` `GetStorageUsage` |  `GetStorageWorkRequest`, `ListStorageWorkRequestErrors` (both also need `read loganalytics-storage-work-request`) `ListStorageWorkRequests` (also need `inspect                   loganalytics-storage-work-request`)  
use |  READ + LOG_ANALYTICS_STORAGE_ARCHIVE_RECALL LOG_ANALYTICS_STORAGE_ARCHIVE_RELEASE |  no extra |  `RecallArchivedData`, `ReleaseRecalledData` (both also need `manage loganalytics-storage-work-request`)  
manage |  USE + LOG_ANALYTICS_STORAGE_ARCHIVE_DISABLE LOG_ANALYTICS_STORAGE_ARCHIVE_ENABLE LOG_ANALYTICS_STORAGE_PURGE LOG_ANALYTICS_STORAGE_UPDATE |  `DisableArchiving` `EnableArchiving` `EstimatePurgeDataSize` `UpdateStorage` |  `PurgeStorageData` (also needs `manage                   loganalytics-storage-work-request`)  
[loganalytics-storage-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/loganalyticspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  LOG_ANALYTICS_STORAGE_WORK_REQUEST_INSPECT |  none |  `ListStorageWorkRequests` (also need `read                   loganalytics-storage`)  
read |  INSPECT + LOG_ANALYTICS_STORAGE_WORK_REQUEST_READ |  none |  `GetStorageWorkRequest`, `ListStorageWorkRequestErrors` (both also need `read loganalytics-storage`)  
use |  READ + no extra |  none |  none  
manage |  USE + LOG_ANALYTICS_STORAGE_WORK_REQUEST_CREATE LOG_ANALYTICS_STORAGE_WORK_REQUEST_DELETE |  none |  `PurgeStorageData` (also needs `manage                   loganalytics-storage`) `RecallArchivedData`, `ReleaseRecalledData` (both also need `use                   loganalytics-storage`)  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in alphabetical order.
For information about permissions, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
API Operation | Permissions Required to Use the Operation  
---|---  
`AddEntityAssociation` | LOG_ANALYTICS_ENTITY_UPDATE  
`BatchGetBasicInfo` | LOG_ANALYTICS_LABEL_READ  
`CancelQueryWorkRequest` |  LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_DELETE and LOG_ANALYTICS_LIFECYCLE_READ  
`ChangeIngestTimeRuleCompartment` | LOG_ANALYTICS_INGESTTIME_RULE_MOVE  
`ChangeLogAnalyticsEMBridgeCompartment` | LOG_ANALYTICS_EM_BRIDGE_MOVE  
`ChangeLogAnalyticsEntityCompartment` | LOG_ANALYTICS_ENTITY_MOVE  
`ChangeLogAnalyticsLogGroupCompartment` | LOG_ANALYTICS_LOG_GROUP_UPDATE  
`ChangeLogAnalyticsObjectCollectionRuleCompartment` |  LOG_ANALYTICS_OBJECT_COLLECTION_RULE_MOVE on both source (current) and target (new) compartments.  
`ChangeScheduledTaskCompartment` | LOG_ANALYTICS_SAVEDSEARCHTASK_MOVE or LOG_ANALYTICS_ACCELERATIONTASK_MOVE or LOG_ANALYTICS_PURGETASK_MOVE  
`Clean` | LOG_ANALYTICS_ACCELERATIONTASK_READ  
`CreateIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_CREATE  
`CreateLogAnalyticsEMBridge` | LOG_ANALYTICS_EM_BRIDGE_CREATE  
`CreateLogAnalyticsEntity` | LOG_ANALYTICS_ENTITY_CREATE  
`CreateLogAnalyticsEntityType` | LOG_ANALYTICS_ENTITY_TYPE_CREATE  
`CreateLogAnalyticsLogGroup` | LOG_ANALYTICS_LOG_GROUP_CREATE  
`CreateLogAnalyticsObjectCollectionRule` |  LOG_ANALYTICS_OBJECT_COLLECTION_RULE_CREATE and LOG_ANALYTICS_SOURCE_READ and LOG_ANALYTICS_LOG_GROUP_UPLOAD_LOGS and LOG_ANALYTICS_ENTITY_UPLOAD_LOGS  
`CreateScheduledTask` | LOG_ANALYTICS_SAVEDSEARCHTASK_CREATE or LOG_ANALYTICS_ACCELERATIONTASK_CREATE or LOG_ANALYTICS_PURGETASK_CREATE  
`DeleteAssociations` | LOG_ANALYTICS_SOURCE_ENTITY_DISASSOC  
`DeleteField` | LOG_ANALYTICS_FIELD_DELETE  
`DeleteLabel` | LOG_ANALYTICS_LABEL_DELETE  
`DeleteIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_DELETE  
`DeleteLogAnalyticsEMBridge` | LOG_ANALYTICS_EM_BRIDGE_DELETE  
`DeleteLogAnalyticsEntity` | LOG_ANALYTICS_ENTITY_DELETE  
`DeleteLogAnalyticsEntityType` | LOG_ANALYTICS_ENTITY_TYPE_DELETE  
`DeleteLogAnalyticsLogGroup` | LOG_ANALYTICS_LOG_GROUP_DELETE_LOGS  
`DeleteLogAnalyticsObjectCollectionRule` | LOG_ANALYTICS_OBJECT_COLLECTION_RULE_DELETE  
`DeleteParser` | LOG_ANALYTICS_PARSER_DELETE  
`DeleteResourceCategories` | LOG_ANALYTICS_CATEGORY_DELETE  
`DeleteScheduledTask` | LOG_ANALYTICS_SAVEDSEARCHTASK_DELETE or LOG_ANALYTICS_ACCELERATIONTASK_DELETE or LOG_ANALYTICS_PURGETASK_DELETE  
`DeleteSource` | LOG_ANALYTICS_SOURCE_DELETE  
`DeleteTenantPreferences` | LOG_ANALYTICS_PREFERENCE_DELETE  
`DeleteUpload` |  LOG_ANALYTICS_ONDEMAND_UPLOAD_DELETE and LOG_ANALYTICS_LOG_GROUP_DELETE_LOGS and LOG_ANALYTICS_QUERY_VIEW and Compartment Permissions (COMPARTMENT_READ)  
`DeleteUploadFile` |  LOG_ANALYTICS_ONDEMAND_UPLOAD_DELETE and LOG_ANALYTICS_LOG_GROUP_DELETE_LOGS and LOG_ANALYTICS_QUERY_VIEW and Compartment Permissions (COMPARTMENT_READ)  
`DeleteUploadWarning` | LOG_ANALYTICS_ONDEMAND_UPLOAD_DELETE  
`DisableArchiving` | LOG_ANALYTICS_STORAGE_ARCHIVE_DISABLE  
`DisableIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_UPDATE  
`EnableArchiving` | LOG_ANALYTICS_STORAGE_ARCHIVE_ENABLE  
`EnableIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_UPDATE  
`EstimatePurgeDataSize` | LOG_ANALYTICS_STORAGE_UPDATE  
`Export` |  LOG_ANALYTICS_QUERY_VIEW and READ_COMPARTMENTS and LOGANALYTICS_LOG_GROUP_READ_LOGS and LOG_ANALYTICS_LIFECYCLE_READ  
`ExportCustomContent` |  LOG_ANALYTICS_SOURCE_READ or LOG_ANALYTICS_PARSER_READ or LOG_ANALYTICS_FIELD_READ or LOG_ANALYTICS_LABEL_READ or LOG_ANALYTICS_METRIC_READ  
`ExtractStructuredLogFieldPaths` | LOG_ANALYTICS_PARSER_READ  
`ExtractStructuredLogHeaderPaths` | LOG_ANALYTICS_PARSER_READ  
`Filter` |  LOG_ANALYTICS_QUERY_INSPECT and LOG_ANALYTICS_LIFECYCLE_READ  
`GetAssociationSummary` | LOG_ANALYTICS_SOURCE_INSPECT  
`GetCategory` | LOG_ANALYTICS_CATEGORY_READ  
`GetColumnNames` | LOG_ANALYTICS_SOURCE_READ  
`GetConfigWorkRequest` | LOG_ANALYTICS_CONFIG_WORK_REQUEST_READ  
`GetField` | LOG_ANALYTICS_FIELD_READ  
`GetFieldsSummary` | LOG_ANALYTICS_FIELD_INSPECT  
`GetIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_READcreate  
`GetLabel` | LOG_ANALYTICS_LABEL_READ  
`GetLabelSummary` | LOG_ANALYTICS_LABEL_INSPECT  
`GetLogAnalyticsEMBridge` | LOG_ANALYTICS_EM_BRIDGE_READ  
`GetLogAnalyticsEMBridgeSummary` | LOG_ANALYTICS_EM_BRIDGE_INSPECT  
`GetLogAnalyticsEntitiesSummary` | LOG_ANALYTICS_ENTITY_INSPECT  
`GetLogAnalyticsEntity` | LOG_ANALYTICS_ENTITY_READ  
`GetLogAnalyticsEntityType` | LOG_ANALYTICS_ENTITY_TYPE_READ  
`GetLogAnalyticsLogGroup` | LOG_ANALYTICS_LOG_GROUP_READ  
`GetLogAnalyticsLogGroupsSummary` | LOG_ANALYTICS_LOG_GROUP_INSPECT  
`GetLogAnalyticsObjectCollectionRule` | LOG_ANALYTICS_OBJECT_COLLECTION_RULE_READ and LOG_ANALYTICS_LOG_GROUP_INSPECT and LOG_ANALYTICS_SOURCE_INSPECT and LOG_ANALYTICS_ENTITY_INSPECT   
`GetNamespace` | LOG_ANALYTICS_LIFECYCLE_READ  
`GetParser` | LOG_ANALYTICS_PARSER_READ  
`GetParserSummary` | LOG_ANALYTICS_PARSER_INSPECT  
`GetQueryResult` |  LOG_ANALYTICS_QUERY_VIEW and LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_READ and LOG_ANALYTICS_LIFECYCLE_READ  
`GetQueryWorkRequest` |  LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_READ and LOG_ANALYTICS_LIFECYCLE_READ  
`GetScheduledTask` | LOG_ANALYTICS_SAVEDSEARCHTASK_READ or LOG_ANALYTICS_ACCELERATIONTASK_READ or LOG_ANALYTICS_PURGETASK_READ  
`GetSource` | LOG_ANALYTICS_SOURCE_READ  
`GetSourceSummary` | LOG_ANALYTICS_SOURCE_INSPECT  
`GetStorage` | LOG_ANALYTICS_STORAGE_READ  
`GetStorageUsage` | LOG_ANALYTICS_STORAGE_READ  
`GetStorageWorkRequest` |  LOG_ANALYTICS_STORAGE_WORK_REQUEST_READ and LOG_ANALYTICS_STORAGE_READ  
`GetTenantPreferences` | LOG_ANALYTICS_PREFERENCE_READ   
`GetUpload` | LOG_ANALYTICS_ONDEMAND_UPLOAD_READ  
`ImportCustomContent` |  LOG_ANALYTICS_SOURCE_CREATE or LOG_ANALYTICS_PARSER_CREATE or LOG_ANALYTICS_FIELD_CREATE or LOG_ANALYTICS_LABEL_CREATE or LOG_ANALYTICS_METRIC_CREATE or LOG_ANALYTICS_SOURCE_UPDATE or LOG_ANALYTICS_PARSER_UPDATE or LOG_ANALYTICS_FIELD_UPDATE or LOG_ANALYTICS_LABEL_UPDATE or LOG_ANALYTICS_METRIC_UPDATE  
`ListAssociatedEntities` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListCategories` | LOG_ANALYTICS_CATEGORY_INSPECT  
`ListConfigWorkRequests` | LOG_ANALYTICS_CONFIG_WORK_REQUEST_INSPECT  
`ListEntityAssociations` | LOG_ANALYTICS_ENTITY_INSPECT  
`ListEntitySourceAssociations` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListFields` | LOG_ANALYTICS_FIELD_INSPECT  
`ListIngestTimeRules` | LOG_ANALYTICS_INGESTTIME_RULE_INSPECT  
`ListLabelPriorities` | LOG_ANALYTICS_LABEL_INSPECT  
`ListLabels` | LOG_ANALYTICS_LABEL_INSPECT  
`ListLabelSourceDetails` | LOG_ANALYTICS_LABEL_READ  
`ListLogAnalyticsEMBridges` | LOG_ANALYTICS_EM_BRIDGE_INSPECT  
`ListLogAnalyticsEntities` | LOG_ANALYTICS_ENTITY_INSPECT  
`ListLogAnalyticsEntityTypes` | LOG_ANALYTICS_ENTITY_TYPE_INSPECT  
`ListLogAnalyticsLogGroups` | LOG_ANALYTICS_LOG_GROUP_INSPECT  
`ListLogAnalyticsObjectCollectionRules` | LOG_ANALYTICS_OBJECT_COLLECTION_RULE_INSPECT  
`ListMetaSourceTypes` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListNamespaces` | LOG_ANALYTICS_LIFECYCLE_INSPECT  
`ListParserFunctions` | LOG_ANALYTICS_PARSER_READ  
`ListParserMetaPlugins` | LOG_ANALYTICS_PARSER_INSPECT  
`ListParsers` | LOG_ANALYTICS_PARSER_INSPECT  
`ListQueryWorkRequests` |  LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_INSPECT and LOG_ANALYTICS_LIFECYCLE_READ  
`ListResourceCategories` |  LOG_ANALYTICS_CATEGORY_INSPECT  
`ListScheduledTasks` | LOG_ANALYTICS_SAVEDSEARCHTASK_INSPECT or LOG_ANALYTICS_ACCELERATIONTASK_INSPECT or LOG_ANALYTICS_PURGETASK_INSPECT  
`ListSourceAssociations` | LOG_ANALYTICS_SOURCE_READ  
`ListSourceExtendedFieldDefinitions` | LOG_ANALYTICS_SOURCE_READ  
`ListSourceLabelOperators` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListSourceMetaFunctions` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListSourcePatterns` | LOG_ANALYTICS_SOURCE_READ  
`ListSources` | LOG_ANALYTICS_SOURCE_INSPECT  
`ListStorageWorkRequestErrors` |  LOG_ANALYTICS_STORAGE_WORK_REQUEST_READ and LOG_ANALYTICS_STORAGE_READ  
`ListStorageWorkRequests` |  LOG_ANALYTICS_STORAGE_WORK_REQUEST_INSPECT and LOG_ANALYTICS_STORAGE_READ  
`ListSupportedCharEncodings` | LOG_ANALYTICS_ONDEMAND_UPLOAD_INSPECT  
`ListSupportedTimezones` | LOG_ANALYTICS_ONDEMAND_UPLOAD_INSPECT  
`ListUploadFiles` |  LOG_ANALYTICS_ONDEMAND_UPLOAD_READ and LOG_ANALYTICS_LOG_GROUP_READ  
`ListUploads` | LOG_ANALYTICS_ONDEMAND_UPLOAD_INSPECT  
`ListUploadWarnings` | LOG_ANALYTICS_ONDEMAND_UPLOAD_READ  
`OffboardNamespace` | LOG_ANALYTICS_LIFECYCLE_OFFBOARD  
`OnboardNamespace` | LOG_ANALYTICS_LIFECYCLE_ONBOARD  
`ParseQuery` |  LOG_ANALYTICS_QUERY_INSPECT and LOG_ANALYTICS_LIFECYCLE_READ  
`PurgeStorageData` |  LOG_ANALYTICS_STORAGE_PURGE and LOG_ANALYTICS_STORAGE_WORK_REQUEST_CREATE  
`PutQueryWorkRequestBackground` |  LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_READ and LOG_ANALYTICS_LIFECYCLE_READ  
`Query` |  LOG_ANALYTICS_QUERY_VIEW and READ_COMPARTMENTS and LOGANALYTICS_LOG_GROUP_READ_LOGS and LOG_ANALYTICS_LIFECYCLE_READ and LOG_ANALYTICS_QUERYJOB_WORK_REQUEST_READ  
`RecallArchivedData` |  LOG_ANALYTICS_STORAGE_ARCHIVE_RECALL and LOG_ANALYTICS_STORAGE_WORK_REQUEST_CREATE  
`RegisterLookup` | LOG_ANALYTICS_LOOKUP_CREATE  
`ReleaseRecalledData` |  LOG_ANALYTICS_STORAGE_ARCHIVE_RELEASE and LOG_ANALYTICS_STORAGE_WORK_REQUEST_CREATE  
`RemoveEntityAssociations` | LOG_ANALYTICS_ENTITY_UPDATE  
`Run` | LOG_ANALYTICS_ACCELERATIONTASK_READ  
`Suggest` |  LOG_ANALYTICS_QUERY_VIEW and READ_COMPARTMENTS and LOG_ANALYTICS_LIFECYCLE_READ  
`TestParser` | LOG_ANALYTICS_PARSER_READ  
`UpdateIngestTimeRule` | LOG_ANALYTICS_INGESTTIME_RULE_UPDATE  
`UpdateLogAnalyticsEMBridge` | LOG_ANALYTICS_EM_BRIDGE_UPDATE  
`UpdateLogAnalyticsEntity` | LOG_ANALYTICS_ENTITY_UPDATE  
`UpdateLogAnalyticsEntityType` | LOG_ANALYTICS_ENTITY_TYPE_UPDATE  
`UpdateLogAnalyticsLogGroup` | LOG_ANALYTICS_LOG_GROUP_UPDATE  
`UpdateLogAnalyticsObjectCollectionRule` | LOG_ANALYTICS_OBJECT_COLLECTION_RULE_UPDATE and LOG_ANALYTICS_SOURCE_READ and LOG_ANALYTICS_LOG_GROUP_UPLOAD_LOGS and LOG_ANALYTICS_ENTITY_UPLOAD_LOGS  
`UpdateResourceCategories` | LOG_ANALYTICS_CATEGORY_UPDATE  
`UpdateScheduledTask` | LOG_ANALYTICS_SAVEDSEARCHTASK_UPDATE or LOG_ANALYTICS_ACCELERATIONTASK_UPDATE or LOG_ANALYTICS_PURGETASK_UPDATE  
`UpdateStorage` | LOG_ANALYTICS_STORAGE_UPDATE  
`UpdateTenantPreferences` | LOG_ANALYTICS_PREFERENCE_UPDATE   
`UploadLogFile` |  LOG_ANALYTICS_ONDEMAND_UPLOAD_CREATE and LOG_ANALYTICS_LOG_GROUP_UPLOAD_LOGS and LOG_ANALYTICS_SOURCE_READ and LOG_ANALYTICS_ENTITY_UPLOAD_LOGS  
`UpsertAssociations` | LOG_ANALYTICS_SOURCE_ENTITY_ASSOC  
`UpsertField` |  LOG_ANALYTICS_FIELD_CREATE or LOG_ANALYTICS_FIELD_UPDATE  
`UpsertLabel` |  LOG_ANALYTICS_LABEL_CREATE or LOG_ANALYTICS_LABEL_UPDATE  
`UpsertParser` |  LOG_ANALYTICS_PARSER_CREATE or LOG_ANALYTICS_PARSER_UPDATE  
`UpsertSource` |  LOG_ANALYTICS_SOURCE_CREATE or LOG_ANALYTICS_SOURCE_UPDATE  
`ValidateAssociationParameters` | LOG_ANALYTICS_SOURCE_READ  
`ValidateFile` | LOG_ANALYTICS_ONDEMAND_UPLOAD_CREATE  
`ValidateSource` |  LOG_ANALYTICS_SOURCE_CREATE or LOG_ANALYTICS_SOURCE_UPDATE  
`ValidateSourceExtendedFieldDetails` | LOG_ANALYTICS_SOURCE_READ  
`ValidateSourceMapping` | LOG_ANALYTICS_ONDEMAND_UPLOAD_CREATE  
Was this article helpful?
YesNo

