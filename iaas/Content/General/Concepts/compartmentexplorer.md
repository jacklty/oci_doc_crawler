Updated 2025-01-13
# Viewing All Resources in a Compartment
This topic describes how you can use the tenancy explorer to get a cross-region view of all resources in a compartment.
## Tenancy Explorer Highlights 🔗 
  * The tenancy explorer lets you view all your resources in a compartment, across all regions in your tenancy. 
  * You can choose to view just the resources that reside in the selected compartment, or you can choose to view all the resources in all the subcompartments as well, to get a full view of the compartment tree.
  * You can take actions on resources from the tenancy explorer. You can delete or move a single or multiple resources at a time. The tenancy explorer is a convenient option when you need to perform bulk delete or move actions on multiple resources.


The following image highlights these features:
[![Features of the tenancy explorer](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentexplorer.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentexplorer.png)
When using the tenancy explorer, be aware of the following:
  * If you recently created a resource, it might not show up in the tenancy explorer immediately. Similarly, if you recently updated a resource, your changes might not immediately appear.
  * You must be in the same region as the resource to navigate to its details page. The tenancy explorer displays the resource's region. Use the region selector at the top of the Console to change to the same region as the resource to enable these actions.
  * When taking bulk actions, you can monitor progress on the Work Requests page.


## Work Requests 🔗 
Tenancy explorer is one of the Oracle Cloud Infrastructure features that is integrated with the Work Requests API. For general information on using work requests in Oracle Cloud Infrastructure, see [Work Requests](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") in the user guide, and the [Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/).
## Resources Supported by the Tenancy Explorer 🔗 
The tenancy explorer is powered by the Search service and supports the same resource types. Most resources are supported.
[Supported resources](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm)
Service | Resource Type | Attributes  
---|---|---  
Application Performance Monitoring | `apmdomain` | See [ApmDomain Reference](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/ApmDomain).  
Analytics Cloud  | `analyticsinstance` | See [AnalyticsInstance Reference](https://docs.oracle.com/iaas/api/#/en/analytics/latest/AnalyticsInstance/).  
API Gateway  | `apideployment` | See [Deployment Reference](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/).  
API Gateway  | `apigateway` | See [Gateway Reference](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/).  
API Gateway  | `apigatewayapi` | See [Api Reference](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Api).  
API Gateway  | `apigatewaycertificate` | See [Certificate Reference](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/).  
Application Dependency Management | `admknowledgebase` | See [KnowledgeBase Reference](https://docs.oracle.com/iaas/api/#/en/adm/latest/KnowledgeBase/)  
Application Dependency Management | `admvulnerabilityaudit` | See [VulnerabilityAudit Reference](https://docs.oracle.com/iaas/api/#/en/adm/latest/VulnerabilityAudit/)  
Autonomous Recovery Service | `ProtectedDatabase` | See [ProtectedDatabase Reference](https://docs.oracle.com/iaas/api/#/en/recovery-service/latest/ProtectedDatabase/)  
Autonomous Recovery Service | `ProtectionPolicy` | See [ProtectionPolicy Reference](https://docs.oracle.com/iaas/api/#/en/recovery-service/latest/ProtectionPolicy/)  
Autonomous Recovery Service | `RecoveryServiceSubnet` | See [RecoveryServiceSubnet Reference](https://docs.oracle.com/iaas/api/#/en/recovery-service/latest/RecoveryServiceSubnet/)  
Bastion | `bastion` | See [Bastion Reference](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Bastion/).  
Big Data Service  | `bigdataservice` | See [Big Data Service: Search](https://docs.oracle.com/iaas/Content/bigdata/overview.htm#integration) for a list of supported fields.  
Big Data Service | `bigdataserviceapikey` | See [Big Data Service: Search](https://docs.oracle.com/iaas/Content/bigdata/overview.htm#integration) for a list of supported fields.  
Big Data Service | `bigdataservicemetastoreconfig` | See [Big Data Service: Search](https://docs.oracle.com/iaas/Content/bigdata/overview.htm#integration) for a list of supported fields.  
Big Data Service | `bigdataservicelakehouseconfig` | See [Big Data Service: Search](https://docs.oracle.com/iaas/Content/bigdata/overview.htm#integration) for a list of supported fields.  
Block Volume  | `bootvolume` | See [BootVolume Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume).  
Block Volume  | `bootvolumebackup` | See [BootVolumeBackup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup).  
Block Volume  | `bootvolumereplica` | See [BootVolumeReplica Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeReplica/).  
Block Volume  | `volume` | See [Volume Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/).  
Block Volume  | `volumebackup` | See [VolumeBackup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/).**Note:** Queries for the `sourceType` attribute are not supported.   
Block Volume  | `volumebackuppolicy` | See [VolumeBackupPolicy Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/).  
Block Volume  | `volumegroup` | See [VolumeGroup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/).  
Block Volume  | `volumegroupbackup` | See [VolumeGroupBackup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/).  
Block Volume  | `volumereplica` | See [VolumeReplica Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BlockVolumeReplica/).  
Blockchain Platform  | `blockchainplatforms` | See [BlockchainPlatform Reference](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/).  
Budgets | `budget` |  See [Budget Reference](https://docs.oracle.com/iaas/api/#/en/budgets/latest/Budget/).  
Certificates | `cabundle` | See [CaBundle Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/CaBundle/).  
Certificates | `cabundleassociation` | See [Association Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/Association/).  
Certificates | `certificate` | See [Certificate Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/Certificate/).  
Certificates | `certificateassociation` | See [Association Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/Association/).  
Certificates | `certificateauthority` | See [CertificateAuthority Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/CertificateAuthority/).  
Certificates | `certificateauthorityassociation` | See [Association Reference](https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/latest/Association/).  
Cloud Guard | `cloudguarddetectorrecipe` |  See [DetectorRecipe Reference](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/DetectorRecipe).  
Cloud Guard | `cloudguardmanagedlist` |  See [ManagedList Reference](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/ManagedList).  
Cloud Guard | `cloudguardresponderrecipe` |  See [ResponderRecipe Reference](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/ResponderRecipe).  
Cloud Guard | `cloudguardtarget` |  See [Target Reference](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/Target).  
Cluster Placement Groups | `clusterplacementgroup` | See [ClusterPlacementGroup Reference](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/ClusterPlacementGroup/). **Note:** Queries for the `capabilities` attribute aren't supported.  
Compute  | `autoscalingconfiguration` |  See [AutoScalingConfiguration Reference](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/). **Note:** Queries for the `policies` attribute are not supported.   
Compute  | `clusternetwork` |  See [ClusterNetwork Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/). **Note:** Queries for the `primarySubnetId`, `secondaryVnicSubnets`, and `timeUpdated` attributes are not supported.  
Compute | `computecapacityreservation` | See [ComputeCapacityReservation Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/)  
Compute  | `consolehistory` | See [ConsoleHistory Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/).  
Compute  | `dedicatedvmhost` |  See [DedicatedVmHost Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/).  
Compute  | `image` | See [Image Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/).  
Compute  | `instance` |  See [Instance Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/). **Note:** Queries for the `privateIp` or `publicIp` attribute of a `vnic` will include the related `instance`, if one exists, and is running, in the query results.  
Compute  | `instanceconfiguration` | See [InstanceConfiguration Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/).  
Compute  | `instancepool` |  See [InstancePool Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/). **Note:** Queries for the `primarySubnetId`, `faultDomains`, `secondaryVnicSubnets`, and `loadBalancers` attributes are not supported.  
Compute Cloud@Customer | `ccc-infrastructure` | See [CccInfrastructure Reference](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/)  
Compute Cloud@Customer | `ccc-upgrade-schedule` | See [CccUpgradeSchedule Reference](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccUpgradeSchedule/)  
Connector Hub | `serviceconnector` | See [ServiceConnector Reference](https://docs.oracle.com/iaas/api/#/en/serviceconnectors/latest/ServiceConnector).  
Container Instances | `container` | See [Container Reference](https://docs.oracle.com/iaas/api/#/en/container-instances/latest/Container/).  
Container Instances | `containerinstance` | See [ContainerInstance Reference](https://docs.oracle.com/iaas/api/#/en/container-instances/latest/ContainerInstance/).  
Content Management | `oceinstance` | See [OceInstance Reference](https://docs.oracle.com/iaas/api/#/en/oce/latest/OceInstance).  
Console Dashboards | `ConsoleDashboard` | See [Dashboard Reference](https://docs.oracle.com/iaas/api/#/en/dashboard/latest/Dashboard/)  
Console Dashboards | `ConsoleDashboardGroup` | See [Dashboard Group Reference](https://docs.oracle.com/iaas/api/#/en/dashboard/latest/DashboardGroup/)  
Data Catalog  | `datacatalog` | See [Catalog Reference](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/Catalog/).  
Data Catalog  | `datacatalogprivateendpoint` | See [CatalogPrivateEndpoint Reference](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/CatalogPrivateEndpoint/).  
Data Catalog | `datacatalogmetastore` | See [Metastore Reference](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/Metastore/).  
Data Flow  | `application` | See [Application Reference](https://docs.oracle.com/iaas/api/#/en/data-flow/latest/Application).  
Data Flow  | `run` | See [Run Reference](https://docs.oracle.com/iaas/api/#/en/data-flow/latest/Run).  
Data Integration  | `disworkspace` | See [Workspace Reference](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace).  
Data Labeling | `datalabelingdataset` | See [ Dataset](https://docs.oracle.com/iaas/api/#/en/datalabeling/latest/Dataset/).  
Data Safe  | `datasafeprivateendpoint` | See [DataSafePrivateEndpoint Reference](https://docs.oracle.com/iaas/api/#/en/data-safe/latest/DataSafePrivateEndpoint/).  
Data Science  | `datasciencejob` | See [Job Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/Job/).  
Data Science  | `datasciencejobrun` | See [JobRun Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/JobRun/).  
Data Science  | `datasciencemodel` | See [Model Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/Model/).  
Data Science  | `datasciencemodeldeployment` | See [ModelDeployment Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/ModelDeployment/).  
Data Science  | `datasciencenotebooksession` | See [NotebookSession Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/NotebookSession/).  
Data Science  | `datascienceproject` | See [Project Reference](https://docs.oracle.com/iaas/api/#/en/data-science/latest/Project/).  
Database  | `autonomouscontainerdatabase` | See [AutonomousContainerDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/AutonomousContainerDatabase/).  
Database  | `autonomousdatabase` | See [AutonomousDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/AutonomousDatabase/).  
Database  | `autonomousvmcluster` | See [AutonomousVmCluster Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/AutonomousVmCluster/).  
Database  | `backupdestination` | See [BackupDestination Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/BackupDestination/).  
Database | `cloudautonomousvmcluster` | See [CloudAutonomousVmCluster Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/CloudAutonomousVmCluster/).  
Database  | `cloudexadatainfrastructure` | See [CloudExadataInfrastructure Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/CloudExadataInfrastructure/).  
Database  | `cloudvmcluster` | See [CloudVmCluster Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/).  
Database  | `database` | See [Database Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/Database/).  
Database | `databasesoftwareimage` | See [DatabaseSoftwareImage Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/DatabaseSoftwareImage).  
Database  | `dbhome` | See [DbHome Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/DbHome/).  
Database | `dbkeystore` | See [KeyStore Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/KeyStore).  
Database | `dbnode` | See [DbNode Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/DbNode).  
Database | `dbserver` | See [DbServer Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/DbServer).  
Database  | `dbsystem` | See [DbSystem Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/DbSystem/).  
Database  | `exadatainfrastructure` | See [ExadataInfrastructure Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/ExadataInfrastructure/).  
Database  | `externalcontainerdatabase` | See [ExternalContainerDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/ExternalContainerDatabase).  
Database  | `externaldatabaseconnector` | See [ExternalDatabaseConnector Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/ExternalDatabaseConnector).  
Database  | `externalnoncontainerdatabase` | See [ExternalNonContainerDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/ExternalNonContainerDatabase).  
Database  | `externalpluggabledatabase` | See [ExternalPluggableDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/ExternalPluggableDatabase).  
Database | `pluggabledatabase` | See [PluggableDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/PluggableDatabase).  
Database  | `vmcluster` | See [VmCluster Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/VmCluster/).  
Database  | `vmclusternetwork` | See [VmClusterNetwork Reference](https://docs.oracle.com/iaas/api/#/en/database/latest/VmClusterNetwork/).  
Database Management | `dbmgmtexternalasm` | See [ExternalAsm Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalAsm/).  
Database Management | `dbmgmtexternalasminstance` | See [ExternalAsmInstance Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalAsmInstance/).  
Database Management | `dbmgmtexternalcluster` | See [ExternalCluster Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalCluster/).  
Database Management | `dbmgmtexternalclusterinstance` | See [ExternalClusterInstance Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalClusterInstance/).  
Database Management | `dbmgmtexternaldbhome` | See [ExternalDbHome Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalDbHome/).  
Database Management | `dbmgmtexternaldbnode` | See [ExternalDbNode Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalDbNode/).  
Database Management | `dbmgmtexternaldbsystem` | See [ExternalDbSystem Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalDbSystem/).  
Database Management | `dbmgmtexternaldbsystemconnector` | See [ExternalDbSystemConnector Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalDbSystemConnector/).  
Database Management | `dbmgmtexternalexadatainfrastructure` | See [ExternalExadataInfrastructure Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalExadataInfrastructure/).  
Database Management | `dbmgmtexternalexadatastorageconnector` | See [ExternalExadataStorageConnector Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalExadataStorageConnector/).  
Database Management | `dbmgmtexternalexadatastoragegrid` | See [ExternalExadataStorageGrid Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalExadataStorageGrid/).  
Database Management | `dbmgmtexternalexadatastorageserver` | See [ExternalExadataStorageServer Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalExadataStorageServer/).  
Database Management | `dbmgmtexternallistener` | See [ExternalListener Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ExternalListener/).  
Database Management | `dbmgmtjob` | See [Job Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/Job/).  
Database Management | `dbmgmtmanageddatabase` | See [ManagedDatabase Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ManagedDatabase/).  
Database Management | `dbmgmtmanageddatabasegroup` | See [ManagedDatabaseGroup Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/ManagedDatabaseGroup/).  
Database Management | `dbmgmtnamedcredential` | See [NamedCredential Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/NamedCredential/).  
Database Management | `dbmgmtprivateendpoint` | See [DbManagementPrivateEndpoint Reference](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/).  
Database Migration | `agent` | See [Agent Reference](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Agent/).  
Database Migration | `connection` | See [Connection Reference](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Connection/).  
Database Migration | `job` | See [Job Reference](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Job/).  
Database Migration | `migration` | See [Migration Reference](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Migration/).  
Database Tools | `databasetoolsconnection` | See [Database Tools Connection Reference](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/DatabaseToolsConnection).  
Database Tools | `databasetoolsprivateendpoint` | See [Database Tools Private Endpoint Reference](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/DatabaseToolsPrivateEndpoint)  
DevOps | `devopsdeployartifact` | See [Artifact Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/DeployArtifact/).  
DevOps | `devopsdeployenvironment` | See [Environment Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/DeployEnvironment/).  
DevOps | `devopsdeployment` | See [Deployment Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/Deployment/).  
DevOps | `devopsdeploypipeline` | See [Deployment Pipeline Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/DeployPipeline/).  
DevOps | `devopsbuildpipeline` | See [Build Pipeline Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/BuildPipeline/).  
DevOps | `devopsbuildpipelinestage` | See [Build Pipeline Stage Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/BuildPipeline/).  
DevOps | `devopsdeploystage` | See [Deployment Stage Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/DeployStage/).  
DevOps | `devopsrepository` | See [Repository Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/Repository/).  
DevOps | `devopsconnection` | See [Connection Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/Connection/).  
DevOps | `devopstrigger` | See [Trigger Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/Trigger/).  
DevOps | `devopsproject` | See [DevOps Project Reference](https://docs.oracle.com/iaas/api/#/en/devops/latest/Project/).  
Digital Assistant  | `odainstance` | See [OdaInstance Reference](https://docs.oracle.com/iaas/api/#/en/digital-assistant/latest/OdaInstance/).  
Email Delivery  | `emailsender` |  See [Sender Reference](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Sender/). See [EmailDomain Reference](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/). See [Dkim Reference](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/).  
Email Delivery  | `emaildomain`  
Email Delivery  | `dkim`  
Events  | `eventrule` | See [Rule Reference](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/).  
File Storage  | `filesystem` | See [FileSystem Reference](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/).  
File Storage | `mounttarget` | See [MountTarget Reference](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/).  
Fleet Application Management | `famsfleet` | See [Fleet Reference](https://docs.oracle.com/iaas/api/#/en/fleet-management/latest/Fleet).  
Fleet Application Management | `famsmaintenancewindow` | See [Maintenance Window Reference](https://docs.oracle.com/iaas/api/#/en/fleet-management/latest/MaintenanceWindow).  
Fleet Application Management | `famsschedulerdefinition` | See [Scheduler Definition Reference](https://docs.oracle.com/iaas/api/#/en/fleet-management/latest/SchedulerDefinition).  
Full Stack Disaster Recovery | `drprotectiongroup` | See [DrProtectionGroup Reference](https://docs.oracle.com/iaas/api/#/en/disaster-recovery/latest/DrProtectionGroup/).  
Full Stack Disaster Recovery | `drplan` | See [DrPlan Reference](https://docs.oracle.com/iaas/api/#/en/disaster-recovery/latest/DrPlan/).  
Full Stack Disaster Recovery | `drplanexeuction` | See [DrPlanExecution Reference](https://docs.oracle.com/iaas/api/#/en/disaster-recovery/latest/DrPlanExecution/).  
Functions  | `functionsapplication` | See [Application Reference](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/).  
Functions  | `functionsfunction` | See [Function Reference](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/).  
Globally Distributed Autonomous Database  | `OsdShardedDatabase` | See [ShardedDatabase Reference](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/).  
Globally Distributed Autonomous Database  | `OsdPrivateEndpoint` | See [PrivateEndpoint Reference](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/).  
GoldenGate | `goldengatedeployment` | See [Deployment Reference](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/).  
GoldenGate | `goldengateconnection` | See [Connection Reference](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Connection).  
IAM  | `compartment` | See [Compartment Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/).  
IAM  | `group` | See [Group Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/).  
IAM  | `identityprovider` | See [IdentityProvider Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/).  
IAM  | `policy` | See [Policy Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/Policy/).  
IAM  | `tagdefault` | See [TagDefault Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagDefault/).  
IAM  | `tagnamespace` | See [TagNamespace Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/).  
IAM  | `user` | See [User Reference](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/).  
Integration  | `integrationinstance` | See [IntegrationInstance Reference](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/).  
Java Management | `jmsfleet` | See [FleetSummary Reference](https://docs.oracle.com/iaas/api/#/en/jms/latest/datatypes/FleetSummary).  
Java Management | `jmsplugin` | See [JmsPluginSummary Reference](https://docs.oracle.com/iaas/api/#/en/jms/20210610/datatypes/JmsPluginSummary).  
Kubernetes Engine | `clusterscluster` | See [Cluster Reference](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/).  
Kubernetes Engine | `clustersvirtualnodepool` | See [VirtualNodePool Reference](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/).  
Kubernetes Engine | `clustersvirtualnode` | See [VirtualNode Reference](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/datatypes/VirtualNode).  
Load Balancer  | `loadbalancer` | See [LoadBalancer Reference](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/).  
Logging | `log` | See [Log Reference](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log).  
Logging | `loggroup` | See [LogGroup Reference](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroup).  
Logging | `logsavedsearch` | See [LogSavedSearch Reference](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch).  
Logging | `unifiedagentconfiguration` | See [UnifiedAgentConfiguration Reference](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration).  
Management Agent | `managementagent` | See [ManagementAgent Reference](https://docs.oracle.com/iaas/api/#/en/management-agent/latest/ManagementAgent).  
Management Agent | `managementagentinstallkey` | See [ManagementAgentInstallKey Reference](https://docs.oracle.com/iaas/api/#/en/management-agent/latest/ManagementAgentInstallKey).  
Media Services (Media Flow) | `mediaworkflow ` | See [MediaWorkflow Reference](https://docs.oracle.com/iaas/api/#/en/dms/latest/MediaWorkflow/).  
Media Services (Media Streams) | `streamdistributionchannel` | See [StreamDistributionChannel Reference](https://docs.oracle.com/iaas/api/#/en/dms/latest/StreamDistributionChannel/).  
Media Services (Media Streams) | `streampackagingconfig` | See [StreamPackagingConfig Reference](https://docs.oracle.com/iaas/api/#/en/dms/latest/StreamPackagingConfig/).  
Media Services (Media Streams) | `streamcdnconfig` | See [StreamCdnConfig Reference](https://docs.oracle.com/iaas/api/#/en/dms/latest/StreamCdnConfig/).  
Monitoring  | `alarm` | See [Alarms Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms).  
Networking  | `byoiprange` | See [ByoipRange Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange).  
Networking  | `cpe` | See [Cpe Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/).  
Networking  | `crossconnect` | See [CrossConnect Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CrossConnect/).  
Networking  | `crossconnectgroup` | See [CrossConnectGroup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CrossConnectGroup/).  
Networking | `dhcpoptions` | See [DhcpOptions Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions).  
Networking  | `drg` | See [Drg Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/).  
Networking | `internetgateway` | See [InternetGateway Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway).  
Networking  | `ipsecconnection` | See [IPSecConnection Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/).  
Networking  | `ipv6` | See [IPv6 Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/).  
Networking | `localpeeringgateway` | See [LocalPeeringGateway Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/).  
Networking  | `natgateway` | See [NatGateway Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/).  
Networking  | `networksecuritygroup` | See [NetworkSecurityGroup Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup).  
Networking  | `publicip` | See [PublicIp Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp).  
Networking  | `publicippool` | See [PublicIpPool Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool).  
Networking  | `privateip` | See [PrivateIp Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp).  
Networking  | `remotepeeringconnection` | See [RemotePeeringConnection Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/).  
Networking  | `routetable` | See [RouteTable Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/).  
Networking  | `securitylist` | See [SecurityList Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/).  
Networking  | `servicegateway` | See [ServiceGateway Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/).  
Networking  | `subnet` | See [Subnet Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/).  
Networking  | `vcn` | See [Vcn Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/).  
Networking  | `virtualcircuit` | See [VirtualCircuit Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VirtualCircuit/).  
Networking | `vlan` | See [Vlan Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/).  
Networking  | `vnic` |  See [Vnic Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/). **Note:** Queries for the `privateIp` or `publicIp` attribute of a `vnic` will include the related `instance`, if one exists and is running, in the query results.  
Network Firewall | `networkfirewall` | See [Network Firewall Reference](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewall/)  
Network Firewall | `networkfirewallpolicy` | See [Network Firewall Policy Reference](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewallPolicy/)  
NoSQL Database Cloud  | `nosqltable` | See [Table Reference](https://docs.oracle.com/iaas/api/#/en/nosql-database/latest/Table/).  
Notifications  | `onssubscription` |  See [Subscription Reference](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription).  **Note:** Queries for the `endpoint` attribute are not supported.   
Notifications  | `onstopic` | See [NotificationTopic Reference](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/).   
Object Storage  | `bucket` | See [Bucket Reference](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/).  
OCI Database with PostgreSQL | `postgresqlbackup` | See [Backup Reference](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Backup/).  
OCI Database with PostgreSQL | `postgresqlconfiguration` | See [Configuration Reference](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Configuration/).  
OCI Database with PostgreSQL | `postgresqldbsystem` | See [DbSystem Reference](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/DbSystem/).  
Oracle Cloud Bridge | `OcbInventory` | See [Inventory Reference](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Inventory/).  
Oracle Cloud Bridge | `OcbVmAsset` | See [Asset Reference](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Asset/).  
Oracle Cloud Bridge | `OcbVmwareVmAsset` | See [AssetSource Reference](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AssetSource/).  
OS Management  | `osmsmanagedinstancegroup` | See [ManagedInstanceGroup Reference](https://docs.oracle.com/iaas/api/#/en/os-management/latest/ManagedInstanceGroup/).  
OS Management  | `osmsscheduledjob` | See [ScheduledJob Reference](https://docs.oracle.com/iaas/api/#/en/os-management/latest/ScheduledJob/).  
OS Management  | `osmssoftwaresource` | See [SoftwareSource Reference](https://docs.oracle.com/iaas/api/#/en/os-management/latest/SoftwareSource/).  
OS Management Hub | `osmhlifecycleenvironment` | See [LifecycleEnvironment Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/LifecycleEnvironment/).  
OS Management Hub | `osmhmanagedinstancegroup` | See [ManagedInstanceGroup Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/).  
OS Management Hub | `osmhmanagementstation` | See [ManagementStation Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagementStation/).  
OS Management Hub | `osmhprofile` | See [Profile Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/Profile/) .  
OS Management Hub | `osmhscheduledjob` | See [ScheduledJob Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ScheduledJob/).  
OS Management Hub | `osmhsoftwaresource` | See [ SoftwareSource Reference](https://docs.oracle.com/iaas/api/#/en/osmh/latest/SoftwareSource/) .  
Process Automation  | `OpaInstance` | See [OpaInstance Reference](https://docs.oracle.com/iaas/api/#/en/opa/latest/OpaInstance/).   
Queue | `queue` | See [Queue Reference](https://docs.oracle.com/iaas/api/#/en/queue/).  
Container Registry  | `containerimage` | See [ContainerImage Reference](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage).  
Container Registry  | `containerrepo` | See [ContainerRepository Reference](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository).  
Resource Manager  | `ormconfigsourceprovider` | See [ConfigurationSourceProvider Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider).  
Resource Manager  | `ormjob` | See [Job Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/).  
Resource Manager | `ormprivateendpoint` | See [PrivateEndpoint Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/).  
Resource Manager  | `ormstack` | See [Stack Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/).  
Resource Manager | `ormtemplate` | See [Template Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template).  
Search | `consoleresourcecollections`  
Security Zones | `securityzonessecurityzone` | See [SecurityZone](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/SecurityZone)  
Security Zones | `securityzonessecurityrecipe` | See [SecurityRecipe](https://docs.oracle.com/iaas/api/#/en/cloud-guard/latest/SecurityRecipe)  
Service Limits | `quota` | See [Quota Reference](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/).  
Service Mesh | `mesh` | See [Mesh Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/Mesh/).  
Service Mesh | `meshaccesspolicy` | See [Access Policy Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/AccessPolicy/).  
Service Mesh | `meshingressgateway` | See [Ingress Gateway Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGateway/).  
Service Mesh | `meshingressgatewayroutetable` | See [Ingress Gateway Route Table Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGatewayRouteTable/).  
Service Mesh | `meshvirtualdeployment` | See [Virtual Deployment Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualDeployment/).  
Service Mesh | `meshvirtualservice` | See [Virtual Service Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualService/).  
Service Mesh | `meshvirtualserviceroutetable` | See [Virtual Service Route Table Reference](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualServiceRouteTable/).  
Streaming  | `connectharness` | See [ConnectHarness Reference](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarness/).  
Streaming  | `stream` | See [Stream Reference](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Stream/).  
Vault  | `key` | See [Key Reference](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/).  
Vault  | `vault` | See [Vault Reference](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/).  
Vault  | `vaultsecret` | See [Secret Reference](https://docs.oracle.com/iaas/api/#/en/secretmgmt/latest/Secret/).  
Visual Builder | `visualbuilderinstance` | See [VbInstance Reference](https://docs.oracle.com/iaas/api/#/en/visual-builder/latest/VbInstance).  
Visual Builder Studio | `vbsinstance` | See [VbsInstance Reference](https://docs.oracle.com/iaas/api/#/en/visual-builder-studio/latest/VbsInstance)  
VMware solution | `vmwareesxihost` | See [EsxiHost Reference](https://docs.oracle.com/iaas/api/#/en/vmware/latest/EsxiHost).  
VMware solution | `vmwaresddc` | See [Sddc Reference](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc).  
Vulnerability Scanning | `vsshostscanrecipe` | See [HostScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/).  
Vulnerability Scanning | `vsshostscantarget` | See [HostScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/).  
Vulnerability Scanning | `vsscontainerscanrecipe` | See [ContainerScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/ContainerScanRecipe/).  
Vulnerability Scanning | `vsscontainerscantarget` | See [ContainerScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/ContainerScanTarget/).  
WAF  | `httpredirect` | See [HttpRedirect Reference](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/).  
WAF  | `waasaddresslist` | See [AddressList Reference](https://docs.oracle.com/iaas/api/#/en/waas/latest/AddressList/).  
WAF  | `waascertificate` | See [Certificate Reference](https://docs.oracle.com/iaas/api/#/en/waas/latest/Certificate/).  
WAF  | `waascustomprotectionrule` | See [CustomProtectionRule Reference](https://docs.oracle.com/iaas/api/#/en/waas/latest/CustomProtectionRule/).  
WAF  | `waaspolicy` | See [WaasPolicy Reference](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/).  
Zero Trust Packet Routing | `securityattributenamespace` | See [SecurityAttributeNamespace Reference](https://docs.oracle.com/iaas/api/#/en/security-attribute/latest/SecurityAttributeNamespace)  
Zero Trust Packet Routing | `zprpolicy` | See [ZprPolicy Reference](https://docs.oracle.com/iaas/api/#/en/zero-trust-packet-routing/latest/ZprPolicy)  
## Required IAM Policy to Work with Resources in the Tenancy Explorer 🔗 
The resources that you see in the tenancy explorer depend on the permissions you have in place for the resource type. 
You do not necessarily see results for everything in the compartment. For example, if your user account is not associated with a policy that grants you the ability to, at a minimum, `inspect` the `instance` resource type, then you can't view instances in the tenancy explorer. For more information about policies, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies."). For information about the permissions required for the list API operation for a specific resource type, see the policy reference for the appropriate service.
**Required Permissions to View Work Requests**
Work requests inherit the permissions of the operation that spawns the work request. So if you have the permissions to move or delete a resource, you also have permission to see the work requests associated with this action.
To enable users to list all work requests in a tenancy, use a policy like the following:
Copy
```
Allow group <My_Group> to inspect work-requests in tenancy
```

## Navigating to the Tenancy Explorer and Viewing Resources 🔗 
Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**. 
The tenancy explorer opens with a view of the root compartment. Select the compartment you want to explore from the compartment picker on the left side of the Console. After you select a compartment, the resources that you have permission to view are displayed. The **Name** and **Description** of the compartment you are viewing are displayed at the top of the page.To also list all resources in the subcompartments of the selected compartment, select **Show resources in subcompartments**. When viewing resources in all subcompartments, it is helpful to use the **Compartment** column in the results list to see the compartment hierarchy where the resource resides. 
## Filtering Displayed Resources 🔗 
To view only specific resource types, select the resource types you are interested in from the **Filter by resource type** menu. You can select multiple resources to include in the filtered list. You can also [filter the list by tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags).
## Opening the Resource Details Page 🔗 
Detail page navigation is not supported for all resource types. If detail page navigation is not supported, the resource name does not display as a link and the option is grayed out on the Actions menu.
To open the details page for a resource:
  1. Locate the resource in the list.
  2. Verify that you are in the same region as the resource. The resource's region is listed in the tenancy explorer results. If it is not the same as the region you are currently in (shown at the top of the Console), then select the appropriate region from the **Regions** menu.
  3. To open the details page, you can either:
     * Click the name.
     * Click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **View Details**.


## Moving Resources to a Different Compartment 🔗 
Not all resource-types can be moved to a different compartment. If the resource cannot be moved, the option is not selectable on the Actions menu. You must have the appropriate permissions for the resources you want to move in both the original and destination compartments. 
**Important** Ensure that you understand the impact of moving a resource before you perform this action. See the resource's service documentation for details.
[To move a single resource to a different compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm)
  1. Locate the resource in the list.
  2. Click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Move Resource**.
  3. In the dialog, choose the destination compartment from the list.
  4. Click **Move Resource**.


[To move multiple resources to a different compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm)
To move multiple resources, the resources must be in the same compartment.
  1. Locate and select the resources in the list. 
  2. Click **Move Selected**.
  3. In the dialog, choose the destination compartment from the list.
  4. Click **Move Resource**.


The Work Request page launches to show you the status of the work request to move the resources. 
## Deleting Resources 🔗 
Not all resource-types can be deleted using the tenancy explorer. If delete is not supported, the option is not selectable on the Actions menu. 
Also, if a resource is in use by another resource, you can't delete it. For example, to delete a VCN, it must first be empty and have no related resources or attached gateways.
[To delete a single resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm)
  1. Locate the resource in the list.
  2. Click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Delete**.
  3. In the confirmation dialog, click **Delete**.
  4. You are taken to the details page for the deleted resource.


[To delete multiple resources](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm)
To delete multiple resources, the resources must be in the same compartment.
  1. Locate and select the resources in the list.
  2. Click **Delete Selected**.
  3. In the confirmation dialog, click **Delete**.


The Work Request page launches to show you the status of the work request to move the resources. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to move or delete multiple resources at once:
  * [ListBulkActionResourceTypes](https://docs.oracle.com/iaas/api/#/en/identity/latest/BulkActionResourceTypeCollection) - use this API to help you provide the correct resource-type information to the BulkDeleteResources and BulkMoveResources operations. The returned list of resource-types provides the appropriate resource-type name to use as input and the required identifying information for each resource-type. Most resource-types only require the OCID to identity a specific resource, but some resources, such as buckets, require you to provide other identifying information. 
  * [BulkDeleteResources](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/BulkDeleteResources)
  * [BulkMoveResources](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/BulkMoveResources)


Was this article helpful?
YesNo

