Updated 2024-09-26
# Details for Ops Insights
This topic covers details for writing policies to control access to the Ops Insights service.
## Resource-Types 🔗 
### Individual Resource-Types 🔗 
`opsi-database-insights`
`opsi-enterprise-manager-bridges`
`opsi-host-insights`
`opsi-work-requests`
`opsi-exadata-insights`
`opsi-warehouses`
`opsi-warehouse-users`
`opsi-awr-hubs`
`opsi-private-endpoint`
`opsi-data-objects`
`opsi-em-warehouses`
### Aggregate Resource-Types 🔗 
`opsi-family`
`opsi-em-warehouse-family`
### Comments 🔗 
See the table in [Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm#permissions) for details of the API operations covered by each verb, for each individual resource-type.
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[opsi-database-insights](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_DATABASE_INSIGHT_INSPECT OPSI_DATABASE_CONFIGURATION_INSPECT |  `ListDatabaseInsights` `ListDatabaseConfigurations` |  none  
read |  INSPECT + OPSI_DATABASE_INSIGHT_READ OPSI_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND_READ OPSI_DATABASE_INSIGHT_RESOURCE_USAGE_TREND_READ OPSI_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND_READ OPSI_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND_READ OPSI_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ OPSI_DATABASE_INSIGHT_RESOURCE_USAGE_READ OPSI_DATABASE_INSIGHT_RESOURCE_STATISTICS_READ OPSI_DATABASE_INSIGHT_SQL_INSIGHTS_READ OPSI_DATABASE_INSIGHT_SQL_PLAN_INSIGHTS_READ OPSI_DATABASE_INSIGHT_SQL_STATISTICS_READ OPSI_DATABASE_INSIGHT_SQL_RESPONSE_TIME_DISTRIBUTIONS_READ OPSI_DATABASE_INSIGHT_SQL_STATISTICS_TIME_SERIES_READ OPSI_DATABASE_INSIGHT_SQL_STATISTICS_TIME_SERIES_BY_PLAN_READ OPSI_DATABASE_INSIGHT_SQL_SEARCH_READ OPSI_DATABASE_INSIGHT_SQL_PLAN_INSIGHTS_READ OPSI_DATABASE_INSIGHT_SQL_PLANS_READ OPSI_DATABASE_INSIGHT_SQL_TEXTS_READ OPSI_DATABASE_INSIGHT_DATA_OBJECT_DATA_QUERY |  `GetDatabaseInsight` `SummarizeDatabaseInsightTablespaceUsageTrend` `SummarizeDatabaseInsightResourceUsageTrend` `SummarizeDatabaseInsightResourceCapacityTrend` `SummarizeDatabaseInsightResourceForecastTrend` `SummarizeDatabaseInsightResourceUtilizationInsight` `SummarizeDatabaseInsightResourceUsage` `SummarizeDatabaseInsightResourceStatistics` `SummarizeSqlInsights` `SummarizeSqlPlanInsights` `SummarizeSqlStatistics` `SummarizeSqlResponseTimeDistributions` `SummarizeSqlStatisticsTimeSeries` `SummarizeSqlStatisticsTimeSeriesByPlan` `SummarizeSqlPlanInsights` `ListSqlPlans` `ListSqlTexts` `ListSqlSearches` `QueryOpsiDataObjectData` |  none  
use |  READ + OPSI_DATABASE_INSIGHT_SQL_BUCKET_INGEST OPSI_DATABASE_INSIGHT_SQL_TEXT_INGEST OPSI_DATABASE_INSIGHT_SQL_PLAN_LINES_INGEST OPSI_DATABASE_INSIGHT_METRICS_INGEST OPSI_DATABASE_INSIGHT_SQL_STATS_INGEST OPSI_DATABASE_INSIGHT_UPDATE |  `IngestSqlBucket` `IngestSqlText` `IngestSqlPlanLines` `IngestDatabaseMetrics` `IngestSqlStats` `UpdateDatabaseInsight` |  none  
manage |  USE + OPSI_DATABASE_INSIGHT_CREATE OPSI_DATABASE_INSIGHT_ENABLE OPSI_DATABASE_INSIGHT_DISABLE OPSI_DATABASE_INSIGHT_DELETE OPSI_DATABASE_INSIGHT_MOVE |  `CreateDatabaseInsight` `EnableDatabaseInsight` `DisableDatabaseInsight` `DeleteDatabaseInsight` `ChangeDatabaseInsightCompartment` |  none  
[opsi-enterprise-manager-bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_ENTERPRISE_MANAGER_BRIDGE_INSPECT |  `ListEnterpriseManagerBridge` |  none  
read |  INSPECT + OPSI_ENTERPRISE_MANAGER_BRIDGE_READ OPSI_ENTERPRISE_MANAGER_BRIDGE_IMPORTABLE_ENTITIES_READ |  `GetEnterpriseManagerBridge` `ListImportableEnterpriseManagerEntities` |  none  
use |  READ + OPSI_ENTERPRISE_MANAGER_BRIDGE_UPDATE |  `UpdateEnterpriseManagerBridge` |  none  
manage |  USE + OPSI_ENTERPRISE_MANAGER_BRIDGE_CREATE OPSI_ENTERPRISE_MANAGER_BRIDGE_DELETE OPSI_ENTERPRISE_MANAGER_BRIDGE_MOVE |  `CreateEnterpriseManagerBridge` `DeleteEnterpriseManagerBridge` `ChangeEnterpriseManagerBridgeCompartment` |  none  
[opsi-host-insights](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_HOST_INSIGHT_INSPECT |  `ListHostInsights` |  none  
read |  INSPECT + OPSI_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ OPSI_HOST_INSIGHT_RESOURCE_USAGE_TREND_READ OPSI_HOST_INSIGHT_RESOURCE_CAPACITY_TREND_READ OPSI_HOST_INSIGHT_RESOURCE_FORECAST_TREND_READ OPSI_HOST_INSIGHT_RESOURCE_USAGE_SUMMARY_READ OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_READ OPSI_HOST_INSIGHT_HOSTED_ENTITIES_READ OPSI_HOST_INSIGHT_TOP_PROCESS_USAGE_TREND_READ OPSI_HOST_INSIGHT_DATA_OBJECT_DATA_QUERY |  `SummarizeHostInsightResourceUtilizationInsight` `SummarizeHostInsightResourceUsageTrend` `SummarizeHostInsightResourceCapacityTrend` `SummarizeHostInsightResourceForecastTrend` `SummarizeHostInsightResourceUsage` `SummarizeHostInsightResourceStatistics` `SummarizeHostedEntityResourceUtilizationTrends` `SummarizeHostInsightTopProcessesUsageTrend` `QueryOpsiDataObjectData` |  none  
use |  READ + OPSI_HOST_INSIGHT_METRICS_INGEST OPSI_HOST_INSIGHT_CONFIGURATION_METRICS_INGEST OPSI_HOST_INSIGHT_UPDATE |  `IngestHostMetrics` `IngestHostConfiguration` `UpdateHostInsight` |  none  
manage |  USE + OPSI_HOST_INSIGHT_CREATE OPSI_HOST_INSIGHT_ENABLE OPSI_HOST_INSIGHT_DISABLE OPSI_HOST_INSIGHT_DELETE OPSI_HOST_INSIGHT_MOVE |  `CreateHostInsight` `EnableHostInsight` `DisableHostInsight` `DeleteHostInsight` `ChangeHostInsightCompartment` |  none  
[opsi-work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_WORK_REQUEST_INSPECT |  `ListDatabaseInsights` |  none  
read |  INSPECT + OPSI_WORK_REQUEST_READ |  `GetWorkRequest` |  none  
use |  READ + no extra |  no extra |  none  
manage |  USE + no extra |  no extra |  none  
[opsi-exadata-insights](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_EXADATA_INSIGHT_INSPECT OPSI_EXADATA_CONFIGURATION_INSPECT |  `ListExadataInsights` `ListExadataConfigurations` |  none  
read |  INSPECT + OPSI_EXADATA_INSIGHT_READ OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATED_READ OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_READ OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATED_READ OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_READ OPSI_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ OPSI_EXADATA_INSIGHT_RESOURCE_USAGE_SUMMARY_AGGREGATED_READ OPSI_EXADATA_INSIGHT_RESOURCE_USAGE_SUMMARY_READ OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_READ OPSI_EXADATA_INSIGHT_MEMBERS_READ |  `GetExadataInsight` `SummarizeExadataInsightResourceCapacityTrendAggregated` `SummarizeExadataInsightResourceCapacityTrend` `SummarizeExadataInsightResourceForecastTrendAggregated` `SummarizeExadataInsightResourceForecastTrend` `SummarizeExadataInsightResourceUtilizationInsight` `SummarizeExadataInsightResourceUsageAggregated` `SummarizeExadataInsightResourceUsage` `SummarizeExadataInsightResourceStatistics` `SummarizeExadataMembers` |  none  
use |  READ + OPSI_EXADATA_INSIGHT_UPDATE |  `UpdateExadataInsight` |  none  
manage |  USE + OPSI_EXADATA_INSIGHT_CREATE OPSI_EXADATA_INSIGHT_DELETE OPSI_EXADATA_INSIGHT_ENABLE OPSI_EXADATA_INSIGHT_ENABLE OPSI_EXADATA_INSIGHT_DISABLE OPSI_EXADATA_INSIGHT_MOVE OPSI_EXADATA_INSIGHT_ADD_MEMBERS |  `CreateExadataInsight` `DeleteExadataInsight` `EnableExadataInsight` `DisableExadataInsight` `ChangeExadataInsightCompartment` `AddExadataInsightMembers` |  none  
[opsi-warehouses](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_WAREHOUSE_INSPECT |  `ListOperationsInsightsWarehouses` |  none  
read |  INSPECT + OPSI_WAREHOUSE_READ |  `GetOperationsInsightsWarehouse` `SummarizeOperationsInsightsWarehouseResourceUsage` |  none  
use |  READ + OPSI_WAREHOUSE_UPDATE |  `UpdateOperationsInsightsWarehouse` |  none  
manage |  USE + OPSI_WAREHOUSE_CREATE OPSI_WAREHOUSE_DELETE OPSI_WAREHOUSE_MOVE OPSI_WAREHOUSE_DOWNLOAD_WALLET OPSI_WAREHOUSE_ROTATE_WALLET |  `CreateOperationsInsightsWarehouse` `DeleteOperationsInsightsWarehouse` `ChangeOperationsInsightsWarehouseCompartment` `DownloadOperationsInsightsWarehouseWallet` `RotateOperationsInsightsWarehouseWallet` |  none  
[opsi-warehouse-users](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_WAREHOUSE_USER_INSPECT |  `ListOperationsInsightsWarehouseUsers` |  none  
read |  INSPECT + OPSI_WAREHOUSE_USER_READ |  `GetOperationsInsightsWarehouseUser` |  none  
use |  READ + OPSI_WAREHOUSE_USER_UPDATE |  `UpdateOperationsInsightsWarehouseUser` |  none  
manage |  USE + OPSI_WAREHOUSE_USER_CREATE OPSI_WAREHOUSE_USER_DELETE OPSI_WAREHOUSE_USER_MOVE |  `CreateOperationsInsightsWarehouseUser` `DeleteOperationsInsightsWarehouseUser` `ChangeOperationsInsightsWarehouseUserCompartment` |  none  
[opsi-awr-hubs](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_AWRHUB_INSPECT |  `ListOperationsInsightsWarehouseUsers` |  none  
read |  INSPECT + OPSI_AWRHUB_READ |  `GetOperationsInsightsWarehouseUser` |  none  
use |  READ + OPSI_AWRHUB_UPDATE |  `UpdateOperationsInsightsWarehouseUser` |  none  
manage |  USE + OPSI_AWRHUB_CREATE OPSI_AWRHUB_DELETE OPSI_AWRHUB_MOVE |  `CreateAwrHub` `DeleteAwrHub` `ChangeAwrHubCompartment` |  none  
[opsi-private-endpoint](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_PRIVATE_ENDPOINT_INSPECT |  `ListOperationsInsightsPrivateEndpoints` |  none  
read |  INSPECT + OPSI_PRIVATE_ENDPOINT_READ |  `GetOperationsInsightsPrivateEndpoint` |  none  
use |  READ + OPSI_PRIVATE_ENDPOINT_UPDATE |  `UpdateOperationsInsightsPrivateEndpoint` |  none  
manage |  USE + OPSI_PRIVATE_ENDPOINT_CREATE OPSI_PRIVATE_ENDPOINT_DELETE OPSI_PRIVATE_ENDPOINT_MOVE |  `CreateOperationsInsightsPrivateEndpoint` `DeleteOperationsInsightsPrivateEndpoint` `ChangeOperationsInsightsPrivateEndpointCompartment` |  none  
[opsi-data-objects](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_DATA_OBJECT_INSPECT |  `ListOperationsInsightsPrivateEndpoints` |  none  
read |  INSPECT + OPSI_DATA_OBJECT_READ OPSI_DATABASE_INSIGHT_DATA_OBJECT_DATA_QUERY  OPSI_HOST_INSIGHT_DATA_OBJECT_DATA_QUERY OPSI_EXADATA_INSIGHT_DATA_OBJECT_DATA_QUERY |  `GetOperationsInsightsPrivateEndpoint` |  none  
[opsi-em-warehouses](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/operationsinsightspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OPSI_EM_WAREHOUSE_INSPECT |  `ListEmWarehouses` |  none  
read |  INSPECT + OPSI_EM_WAREHOUSE_READ |  `GetEmWarehouseResourceUsage` `GetEmWarehouse` `GetEtlRun` |  none  
use |  READ + OPSI_EM_WAREHOUSE_UPDATE |  `UpdateEmWarehouse` `ChangeEmWarehouseCompartment` | none  
manage |  USE + OPSI_EM_WAREHOUSE_CREATE OPSI_EM_WAREHOUSE_DELETE |  `CreateEmWarehouse` `DeleteEmWarehouse` | none  
## Permissions Required for Each API Operation 🔗 
The following tables list the API operations in alphabetical order.
For information about permissions, see services permission page.
### Database (Data Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`IngestDatabaseMetrics` | OPSI_DATABASE_INSIGHT_METRICS_INGEST  
`IngestSqlBucket` | OPSI_DATABASE_INSIGHT_SQL_BUCKET_INGEST  
`IngestSqlPlanLines` | OPSI_DATABASE_INSIGHT_SQL_PLAN_LINES_INGEST  
`IngestSqlStats` | OPSI_DATABASE_INSIGHT_SQL_STATS_INGEST  
`IngestSqlText` | OPSI_DATABASE_INSIGHT_SQL_TEXT_INGEST  
`ListDatabaseConfigurations` | OPSI_DATABASE_CONFIGURATION_INSPECT  
`ListDatabaseInsights` | OPSI_DATABASE_INSIGHT_INSPECT  
`ListSqlPlans` | OPSI_DATABASE_INSIGHT_SQL_PLANS_READ  
`ListSqlSearches` | OPSI_DATABASE_INSIGHT_SQL_SEARCH_READ  
`ListSqlTexts` | OPSI_DATABASE_INSIGHT_SQL_TEXTS_READ  
`SummarizeDatabaseInsightResourceCapacityTrend` | OPSI_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND_READ  
`SummarizeDatabaseInsightResourceForecastTrend` | OPSI_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND_READ  
`SummarizeDatabaseInsightResourceStatistics` | OPSI_DATABASE_INSIGHT_RESOURCE_STATISTICS_READ  
`SummarizeDatabaseInsightResourceUsage` | OPSI_DATABASE_INSIGHT_RESOURCE_USAGE_READ  
`SummarizeDatabaseInsightResourceUsageTrend` | OPSI_DATABASE_INSIGHT_RESOURCE_USAGE_TREND_READ  
`SummarizeDatabaseInsightResourceUtilizationInsight` | OPSI_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ  
`SummarizeDatabaseInsightTablespaceUsageTrend` | OPSI_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND_READ  
`SummarizeSqlInsights` | OPSI_DATABASE_INSIGHT_SQL_INSIGHTS_READ  
`SummarizeSqlPlanInsights` | OPSI_DATABASE_INSIGHT_SQL_PLAN_INSIGHTS_READ  
`SummarizeSqlResponseTimeDistributions` | OPSI_DATABASE_INSIGHT_SQL_RESPONSE_TIME_DISTRIBUTIONS_READ  
`SummarizeSqlStatistics` | OPSI_DATABASE_INSIGHT_SQL_STATISTICS_READ  
`SummarizeSqlStatisticsTimeSeries` | OPSI_DATABASE_INSIGHT_SQL_STATISTICS_TIME_SERIES_READ  
`SummarizeSqlStatisticsTimeSeriesByPlan` | OPSI_DATABASE_INSIGHT_SQL_STATISTICS_TIME_SERIES_BY_PLAN_READ  
### Host (Data Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`IngestHostConfiguration` | OPSI_HOST_INSIGHT_CONFIGURATION_METRICS_INGEST  
`IngestHostMetrics` | OPSI_HOST_INSIGHT_METRICS_INGEST  
`SummarizeHostedEntityResourceUtilizationTrends` | OPSI_HOST_INSIGHT_HOSTED_ENTITIES_READ  
`SummarizeHostInsightResourceCapacityTrend` | OPSI_HOST_INSIGHT_RESOURCE_CAPACITY_TREND_READ  
`SummarizeHostInsightResourceForecastTrend` | OPSI_HOST_INSIGHT_RESOURCE_FORECAST_TREND_READ  
`SummarizeHostInsightResourceStatistics` | OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_READ  
`SummarizeHostInsightResourceUsage` | OPSI_HOST_INSIGHT_RESOURCE_USAGE_SUMMARY_READ  
`SummarizeHostInsightResourceUsageTrend` | OPSI_HOST_INSIGHT_RESOURCE_USAGE_TREND_READ  
`SummarizeHostInsightResourceUtilizationInsight` | OPSI_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ  
SummarizeHostInsightTopProcessesUsageTrend | OPSI_HOST_INSIGHT_TOP_PROCESS_USAGE_TREND_READ  
### Exadata (Data Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`IngestHostConfiguration` | OPSI_EXADATA_CONFIGURATION_INSPECT  
`SummarizeExadataInsightResourceCapacityTrendAggregated` | OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATED_READ  
`SummarizeExadataInsightResourceCapacityTrend` | OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_READ  
`SummarizeExadataInsightResourceForecastTrendAggregated` | OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATED_READ  
`SummarizeExadataInsightResourceForecastTrend` | OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_READ  
`SummarizeExadataInsightResourceUtilizationInsight` | OPSI_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_READ  
`SummarizeExadataInsightResourceUsageAggregated` | OPSI_EXADATA_INSIGHT_RESOURCE_USAGE_SUMMARY_AGGREGATED_READ  
`SummarizeExadataInsightResourceUsage` | OPSI_EXADATA_INSIGHT_RESOURCE_USAGE_SUMMARY_READ  
`SummarizeExadataInsightResourceStatistics` | OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_READ  
`SummarizeExadataMembers` | OPSI_EXADATA_INSIGHT_MEMBERS_READ  
### Database (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ChangeDatabaseInsightCompartment` | OPSI_DATABASE_INSIGHT_MOVE  
`ChangeEnterpriseManagerBridgeCompartment` | OPSI_ENTERPRISE_MANAGER_BRIDGE_MOVE  
`CreateEnterpriseManagerBridge` | OPSI_ENTERPRISE_MANAGER_BRIDGE_CREATE  
`DeleteDatabaseInsight` | OPSI_DATABASE_INSIGHT_DELETE  
`DeleteEnterpriseManagerBridge` | OPSI_ENTERPRISE_MANAGER_BRIDGE_DELETE  
`DisableDatabaseInsight` | OPSI_DATABASE_INSIGHT_DISABLE  
`EnableDatabaseInsight` | OPSI_DATABASE_INSIGHT_ENABLE  
`GetDatabaseInsight` | OPSI_DATABASE_INSIGHT_READ  
`GetEnterpriseManagerBridge` | OPSI_ENTERPRISE_MANAGER_BRIDGE_READ  
`ListDatabaseInsights` | OPSI_DATABASE_INSIGHT_INSPECT  
`ListEnterpriseManagerBridge` | OPSI_ENTERPRISE_MANAGER_BRIDGE_INSPECT  
`ListImportableEnterpriseManagerEntities` | OPSI_ENTERPRISE_MANAGER_BRIDGE_IMPORTABLE_ENTITIES_READ  
`UpdateDatabaseInsight` | OPSI_DATABASE_INSIGHT_UPDATE  
`UpdateEnterpriseManagerBridge` | OPSI_ENTERPRISE_MANAGER_BRIDGE_UPDATE  
### Host (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ChangeHostInsightCompartment` | OPSI_HOST_INSIGHT_MOVE  
`CreateHostInsight` | OPSI_HOST_INSIGHT_CREATE  
`DeleteHostInsight` | OPSI_HOST_INSIGHT_DELETE  
`DisableHostInsight` | OPSI_HOST_INSIGHT_DISABLE  
`EnableHostInsight` | OPSI_HOST_INSIGHT_ENABLE  
`ListHostInsights` | OPSI_HOST_INSIGHT_INSPECT  
`UpdateHostInsight` | OPSI_HOST_INSIGHT_UPDATE  
### Exadata (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListExadataInsights` | OPSI_EXADATA_INSIGHT_INSPECT  
`CreateExadataInsight` | OPSI_EXADATA_INSIGHT_CREATE  
`GetExadataInsight` | OPSI_EXADATA_INSIGHT_READ  
`UpdateExadataInsight` | OPSI_EXADATA_INSIGHT_UPDATE  
`DeleteExadataInsight` | OPSI_EXADATA_INSIGHT_DELETE  
`EnableExadataInsight` | OPSI_EXADATA_INSIGHT_ENABLE  
`DisableExadataInsight` | OPSI_EXADATA_INSIGHT_DISABLE  
`ChangeExadataInsightCompartment` | OPSI_EXADATA_INSIGHT_MOVE  
### Work Requests (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`GetWorkRequest` | OPSI_WORK_REQUEST_READ  
`ListWorkRequestErrors` | OPSI_WORK_REQUEST_INSPECT  
`ListWorkRequestLogs` | OPSI_WORK_REQUEST_INSPECT  
`ListWorkRequests` | OPSI_WORK_REQUEST_INSPECT  
### Warehouse (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListOperationsInsightsWarehouses` | OPSI_WAREHOUSE_INSPECT   
`GetOperationsInsightsWarehouse` | OPSI_WAREHOUSE_READ  
`SummarizeOperationsInsightsWarehouseResourceUsage` | OPSI_WAREHOUSE_READ  
`CreateOperationsInsightsWarehouse` | OPSI_WAREHOUSE_CREATE  
`UpdateOperationsInsightsWarehouse` | OPSI_WAREHOUSE_UPDATE  
`DeleteOperationsInsightsWarehouse` | OPSI_WAREHOUSE_DELETE  
`ChangeOperationsInsightsWarehouseCompartment` | OPSI_WAREHOUSE_MOVE  
`DownloadOperationsInsightsWarehouseWallet` | OPSI_WAREHOUSE_DOWNLOAD_WALLET  
`RotateOperationsInsightsWarehouseWallet` | OPSI_WAREHOUSE_ROTATE_WALLET  
### Warehouse User (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListOperationsInsightsWarehouseUsers` | OPSI_WAREHOUSE_USER_INSPECT  
`GetOperationsInsightsWarehouseUser` | OPSI_WAREHOUSE_USER_READ  
`CreateOperationsInsightsWarehouseUser` | OPSI_WAREHOUSE_USER_CREATE  
`UpdateOperationsInsightsWarehouseUser` | OPSI_WAREHOUSE_USER_UPDATE  
`DeleteOperationsInsightsWarehouseUser` | OPSI_WAREHOUSE_USER_DELETE  
`ChangeOperationsInsightsWarehouseUserCompartment` | OPSI_WAREHOUSE_USER_MOVE  
### AWR Hub (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListAwrHubs` | OPSI_AWRHUB_INSPECT  
`GetAwrHub` | OPSI_AWRHUB_READ  
`CreateAwrHub` | OPSI_AWRHUB_CREATE  
`UpdateAwrHub` | OPSI_AWRHUB_UPDATE  
`DeleteAwrHub` | OPSI_AWRHUB_DELETE  
`ChangeAwrHubCompartment` | OPSI_AWRHUB_MOVE  
`SummarizeAwrSourcesSummaries` | OPSI_AWRHUB_READ  
`ListAwrSnapshots` | OPSI_AWRHUB_READ  
### Private Endpoints (Control Plane) 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListOperationsInsightsPrivateEndpoints` | OPSI_PRIVATE_ENDPOINT_INSPECT  
`CreateOperationsInsightsPrivateEndpoint` | OPSI_PRIVATE_ENDPOINT_CREATE  
`GetOperationsInsightsPrivateEndpoint` | OPSI_PRIVATE_ENDPOINT_READ  
`UpdateOperationsInsightsPrivateEndpoint` | OPSI_PRIVATE_ENDPOINT_UPDATE  
`DeleteOperationsInsightsPrivateEndpoint` | OPSI_PRIVATE_ENDPOINT_DELETE  
`ChangeOperationsInsightsPrivateEndpointCompartment` | OPSI_PRIVATE_ENDPOINT_MOVE  
### Data Objects (Control Plane)
API Operation | Permissions Required to Use the Operation  
---|---  
`ListOpsiDataObjects` | OPSI_DATA_OBJECT_INSPECT  
`GetOpsiDataObject` | OPSI_DATA_OBJECT_READ  
`QueryOpsiDataObjectData` | OPSI_DATA_OBJECT_READ and(OPSI_DATABASE_INSIGHT_DATA_OBJECT_DATA_QUERY |OPSI_HOST_INSIGHT_DATA_OBJECT_DATA_QUERY |OPSI_EXADATA_INSIGHT_DATA_OBJECT_DATA_QUERY)  
### EM Warehouse (Control Plane)
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateEmWarehouse` | OPSI_EM_WAREHOUSE_CREATE  
`ListEmWarehouses` | OPSI_EM_WAREHOUSE_INSPECT  
`GetEmWarehouse` | OPSI_EM_WAREHOUSE_READ  
`DeleteEmWarehouse` | OPSI_EM_WAREHOUSE_DELETE  
`GetEmWarehouseResourceUsage` | OPSI_EM_WAREHOUSE_READ  
`UpdateEmWarehouse` | OPSI_EM_WAREHOUSE_UPDATE  
`ChangeEmWarehouseCompartment` | OPSI_EM_WAREHOUSE_UPDATE  
`GetEtlRun` | OPSI_EM_WAREHOUSE_READ  
Was this article helpful?
YesNo

