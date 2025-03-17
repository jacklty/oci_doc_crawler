Updated 2025-02-19
# Details for the Java Management Service
This topic covers details for writing policies to control access to the Java Management service.
## Resource-Types 🔗 
`fleets`
`jms-plugins`
`java-download-tokens`
`java-download-reports`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[fleets](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/javamanagementreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  FLEET_INSPECT |  `ListFleets` `ListWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` `ListBlocklists` `ListWorkItems` `ListDrsFiles ` |  none  
read |  INSPECT + FLEET_READ FLEET_QUERY_RESOURCES |  `GetFleet` `GetWorkRequest` `SummarizeJres` `RequestSummarizedJres` `SummarizeApplications` `RequestSummarizedApplications` `SummarizeInstallations` `RequestSummarizedInstallations` `SummarizeManagedInstances` `RequestSummarizedManagedInstances` `GetFleetAdvancedFeatureConfiguration` `ListJreUsage` `SummarizeJreUsage` `SummarizeApplicationUsage` `SummarizeDeployedApplicationUsage` `SummarizeManagedInstanceUsage` `SummarizeInstallationUsage` `GetFleetAgentConfiguration` `ListInstallationSites` `ListFleetDiagnoses` `SummarizeApplicationInstallationUsage` `SummarizeDeployedApplicationInstallationUsage` `SummarizeJavaServerUsage` `SummarizeJavaServerInstanceUsage` `SummarizeLibraryUsage` `SummarizeResourceInventory` `GetCryptoAnalysisResult` `ListCryptoAnalysisResults` `GetPerformanceTuningAnalysisResult` `ListPerformanceTuningAnalysisResults` `GetJavaMigrationAnalysisResult` `ListJavaMigrationAnalysisResults` `GetDrsFile` `GetExportSetting` `GetExportStatus` `GenerateLoadPipelineScript` `GenerateAgentInstallerConfiguration` `ListAgentInstallers` `GetAgentInstallerContent` `ListFleetErrors` `ListPluginErrors` `SummarizeFleetErrors` `SummarizePluginErrors` |  none  
use |  READ + FLEET_UPDATE | `UpdateFleet``UpdateFleetAgentConfiguration``CreateBlocklist``DeleteBlocklist``CancelWorkRequest``RemoveFleetInstallationSites``GenerateAgentDeployScript``ScanJavaServerUsage``ScanLibraryUsage``RequestJfrRecordings``RequestCryptoAnalyses``DeleteCryptoAnalysisResult``RequestJavaMigrationAnalyses``RequestPerformanceTuningAnalyses``DeletePerformanceTuningAnalysisResult``DeleteJavaMigrationAnalysisResult``RequestDeployedApplicationMigrationAnalyses``EnableDrs``DisableDrs``UpdateExportSetting` |  none  
manage |  USE + FLEET_CREATE FLEET_DELETE FLEET_MOVE FLEET_ADVANCED_FEATURES_UPDATE  |  `CreateFleet` `DeleteFleet` `ChangeFleetCompartment` `UpdateFleetAdvancedFeatureConfiguration` `RequestUploadDrsFile` `RequestUpdateDrsFile` `DeleteDrsFile` `CreateDrsFile` `UpdateDrsFile` |  none  
[jms-plugins](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/javamanagementreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | JMS_PLUGIN_INSPECT | `ListJmsPlugins` |  none  
read |  INSPECT +  JMS_PLUGIN_READ | `GetJmsPlugin` |  none  
use |  READ +  JMS_PLUGIN_UPDATE | `UpdateJmsPlugin` |  none  
manage |  USE + JMS_PLUGIN_CREATE+JMS_PLUGIN_DELETE |  `CreateJmsPlugin` `DeleteJmsPlugin` |  none  
[java-download-tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/javamanagementreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  JAVA_DOWNLOAD_TOKEN_INSPECT |  `ListJavaDownloadTokens` `ListWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` |  none  
read |  INSPECT + JAVA_DOWNLOAD_TOKEN_READ |  `GetJavaDownloadToken` `GetWorkRequest` |  none  
use |  READ  | none |  none  
manage |  USE + JAVA_DOWNLOAD_TOKEN_CREATE JAVA_DOWNLOAD_TOKEN_UPDATE JAVA_DOWNLOAD_TOKEN_DELETE |  `CreateJavaDownloadToken` `UpdateJavaDownloadToken` `DeleteJavaDownloadToken` `CancelWorkRequest` |  none  
[java-download-reports](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/javamanagementreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  JAVA_DOWNLOAD_REPORT_INSPECT |  `ListJavaDownloadReports` |  none  
read |  INSPECT + JAVA_DOWNLOAD_REPORT_READ |  `GetJavaDownloadReport` `GetJavaDownloadReportContent` `RequestSummarizedJavaDownloadCounts` `ListJavaDownloadRecords` |  none  
use |  READ  | none |  none  
manage |  USE + JAVA_DOWNLOAD_REPORT_CREATE JAVA_DOWNLOAD_REPORT_DELETE |  `CreateJavaDownloadReport` `DeleteJavaDownloadReport` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the Java Management Service Fleets API operations:
API Operation | Permissions Required to Use the Operation  
---|---  
`ListFleets` | FLEET_INSPECT  
`GetFleet` | FLEET_READ  
`UpdateFleet` |  FLEET_UPDATE  
`ChangeFleetCompartment` | FLEET_MOVE  
`CreateFleet` | FLEET_CREATE  
`DeleteFleet` |  FLEET_DELETE  
`SummarizeJres` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedJres` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeApplications` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedApplications` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeInstallations` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedInstallations` |  FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeManagedInstances` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedManagedInstances` | FLEET_READ and FLEET_QUERY_RESOURCES  
`ListWorkRequest` | FLEET_INSPECT  
`GetWorkRequest` | FLEET_READ  
`ListWorkRequestErrors` | FLEET_INSPECT  
`ListWorkRequestLogs` | FLEET_INSPECT  
`GetFleetAdvancedFeatureConfiguration` | FLEET_READ  
`UpdateFleetAdvancedFeatureConfiguration` | FLEET_ADVANCED_FEATURES_UPDATE   
`ListJreUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeJreUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedJreUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeApplicationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedApplicationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeInstallationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedInstallationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeManagedInstanceUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedManagedInstanceUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`ListBlocklists` | FLEET_INSPECT  
`CreateBlocklist` | FLEET_UPDATE  
`DeleteBlocklist` | FLEET_UPDATE  
`CancelWorkRequest` | FLEET_UPDATE  
`ListWorkItems` | FLEET_INSPECT  
`ListInstallationSites` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestDeleteInstallationSites` | FLEET_UPDATE  
`AddFleetInstallationSites` | FLEET_UPDATE  
`RemoveFleetInstallationSites` | FLEET_UPDATE  
`GenerateAgentDeployScript` | FLEET_UPDATE  
`ListJavaFamilies`  
`GetJavaFamily`  
`ListJavaReleases`  
`GetJavaRelease`  
`ListAnnouncements`  
`GetFleetAdvancedFeatureConfiguration` | FLEET_READ  
`UpdateFleetAdvancedFeatureConfiguration` | FLEET_ADVANCED_FEATURES_UPDATE  
`ListFleetDiagnoses` | FLEET_READ  
`SummarizeApplicationInstallationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeDeployedApplicationInstallationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeDeployedApplicationUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeJavaServerInstanceUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`ScanJavaServerUsage` | FLEET_UPDATE  
`SummarizeJavaServerUsage` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestJfrRecordings` | FLEET_UPDATE  
`RequestCryptoAnalyses` | FLEET_UPDATE  
`ListCryptoAnalysisResults` | FLEET_QUERY_RESOURCES  
`GetCryptoAnalysisResult` | FLEET_READ  
`DeleteCryptoAnalysisResult` | FLEET_UPDATE  
`RequestJavaMigrationAnalyses` | FLEET_UPDATE  
`RequestPerformanceTuningAnalyses` | FLEET_UPDATE  
`DeletePerformanceTuningAnalysisResult` | FLEET_UPDATE  
`GetPerformanceTuningAnalysisResult` | FLEET_READ  
`ListPerformanceTuningAnalysisResults` | FLEET_QUERY_RESOURCES  
`SummarizeResourceInventory` | FLEET_READ and FLEET_QUERY_RESOURCES  
`DeleteJavaMigrationAnalysisResult` | FLEET_UPDATE  
`GetJavaMigrationAnalysisResult` | FLEET_READ  
`RequestDeployedApplicationMigrationAnalyses` | FLEET_UPDATE  
`ListJavaMigrationAnalysisResults` | FLEET_QUERY_RESOURCES  
`RequestUploadDrsFile` | FLEET_ADVANCED_FEATURES_UPDATE  
`RequestUpdateDrsFile` | FLEET_ADVANCED_FEATURES_UPDATE  
`DeleteDrsFile` | FLEET_ADVANCED_FEATURES_UPDATE  
`ListDrsFiles` | FLEET_INSPECT  
`GetDrsFile` | FLEET_READ  
`EnableDrs` | FLEET_UPDATE  
`DisableDrs` | FLEET_UPDATE  
`CreateDrsFile` | FLEET_ADVANCED_FEATURES_UPDATE  
`UpdateDrsFile` | FLEET_ADVANCED_FEATURES_UPDATE  
`GetExportSetting` | FLEET_READ  
`UpdateExportSetting` | FLEET_UPDATE  
`GetExportStatus` | FLEET_READ  
`GenerateLoadPipelineScript` | FLEET_READ  
`GenerateAgentInstallerConfiguration` | FLEET_READ  
`ListAgentInstallers` | FLEET_READ  
`GetAgentInstallerContent` | FLEET_READ  
`ListFleetErrors` | FLEET_READ and FLEET_QUERY_RESOURCES  
`ListPluginErrors` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeFleetErrors` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizePluginErrors` | FLEET_READ and FLEET_QUERY_RESOURCES  
The following table lists the Java Management Service `JmsPlugin` API operations in alphabetical order: 
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateJmsPlugin` | JMS_PLUGIN_CREATE  
`DeleteJmsPlugin` | JMS_PLUGIN_DELETE  
`GetJmsPlugin` | JMS_PLUGIN_READ  
`ListJmsPlugins` | JMS_PLUGIN_INSPECT  
`UpdateJmsPlugin` | JMS_PLUGIN_UPDATE  
The following table lists the Java Management Service Java Download API operations in alphabetical order:
API Operation | Permissions Required to Use the Operation  
---|---  
`CancelWorkRequest` | JAVA_DOWNLOAD_TOKEN_DELETE  
`CreateJavaDownloadReport` | JAVA_DOWNLOAD_REPORT_CREATE  
`CreateJavaDownloadToken` | JAVA_DOWNLOAD_TOKEN_CREATE  
`DeleteJavaDownloadReport` |  JAVA_DOWNLOAD_REPORT_DELETE  
`DeleteJavaDownloadToken` | JAVA_DOWNLOAD_TOKEN_DELETE  
`GetJavaDownloadReport` | JAVA_DOWNLOAD_REPORT_READ  
`GetJavaDownloadReportContent` | JAVA_DOWNLOAD_REPORT_READ  
`GetJavaDownloadToken` | JAVA_DOWNLOAD_TOKEN_READ  
`GetWorkRequest` | JAVA_DOWNLOAD_TOKEN_READ  
`ListJavaDownloadRecords` | JAVA_DOWNLOAD_REPORT_READ  
`ListJavaDownloadReports` |  JAVA_DOWNLOAD_REPORT_INSPECT  
`ListJavaDownloadTokens` | JAVA_DOWNLOAD_TOKEN_INSPECT  
`ListWorkRequest` | JAVA_DOWNLOAD_TOKEN_INSPECT  
`ListWorkRequestErrors` | JAVA_DOWNLOAD_TOKEN_INSPECT  
`ListWorkRequestLogs` | JAVA_DOWNLOAD_TOKEN_INSPECT  
`RequestSummarizedJavaDownloadCounts` | JAVA_DOWNLOAD_REPORT_READ  
`UpdateJavaDownloadToken` |  JAVA_DOWNLOAD_TOKEN_UPDATE  
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
Was this article helpful?
YesNo

