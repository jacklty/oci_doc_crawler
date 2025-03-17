Updated 2025-01-08
# Details for Search
The Search service does not require permissions for its API operations. You do not need to write policies specifically to control access to Search. However, what you can see in search or query results depends on the permissions you have. If a policy exists to give you access to the `inspect` verb for a particular resource type, you have access to the permissions needed to view that resource type and its associated metadata in search results. If a service does not recognize the `inspect` verb or if the resource type's `inspect` verb does not fully cover list operations, permissions to view the service's supported resource types are granted by the `read` verb instead.
For more information about permissions, see the Permissions section of [Advanced Policy Features.](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi)
## Permissions Required to View Each Resource Type 🔗 
The following table lists the resource types grouped by service, which are listed in alphabetical order. The Search API operations that can access the metadata for these resource types with these permissions are `GetResourceType`, `ListResourceTypes`, and `SearchResources`.
Service | Resource Type |  Permissions Required to View in Search Results  
---|---|---  
Application Performance Monitoring | `apm-domains` | APM_DOMAIN_LIST  
Analytics Cloud | `analytics-instance` | ANALYTICS_INSTANCE_INSPECT  
API Gateway | `api-deployments` | API_DEPLOYMENT_LIST  
API Gateway | `api-gateways` | API_GATEWAY_LIST  
API Gateway | `api-definitions` | API_DEFINITION_LIST  
API Gateway | `api-certificates` | API_CERTIFICATE_LIST  
Application Dependency Management | `adm-knowledge-bases` | ADM_KNOWLEDGE_BASE_INSPECT  
Application Dependency Management | `adm-vulnerability-audits` | ADM_VULNERABILITY_AUDIT_INSPECT  
Autonomous Recovery Service | `recovery-service-protected-database` | RECOVERY_SERVICE_PROTECTED_DATABASE_INSPECT  
Autonomous Recovery Service | `recovery-service-policy` | RECOVERY_SERVICE_POLICY_INSPECT  
Autonomous Recovery Service | `recovery-service-subnet` | RECOVERY_SERVICE_SUBNET_INSPECT  
Bastion | `bastion` | BASTION_INSPECT  
Block Volume  | `volumes` | VOLUME_INSPECT  
Block Volume  | `volume-backups` | VOLUME_BACKUP_INSPECT  
Block Volume | `backup-policies` | BACKUP_POLICY_INSPECT  
Block Volume | `volume-groups` | VOLUME_GROUP_INSPECT  
Block Volume | `volume-group-backups` | VOLUME_GROUP_BACKUP_INSPECT  
Block Volume | `volume-replicas` | VOLUME_REPLICA_INSPECT  
Blockchain Platform | `blockchain-platforms` | BLOCKCHAIN_PLATFORM_INSPECT  
Budgets | `usage-budgets` | USAGE_BUDGET_INSPECT  
Certificates | `cabundles` | CABUNDLE_INSPECT  
Certificates | `cabundle-associations` | CABUNDLE_ASSOCIATION_INSPECT  
Certificates | `leaf-certificates` | CERTIFICATE_INSPECT  
Certificates | `certificate-associations` | CERTIFICATE_ASSOCIATION_INSPECT  
Certificates | `certificate-authorities` | CERTIFICATE_AUTHORITY_INSPECT  
Certificates | `certificate-authority-associations` | CERTIFICATE_AUTHORITY_ASSOCIATION_INSPECT  
Cloud Guard | `cloud-guard-detector-recipes` | CG_DETECTOR_RECIPE_INSPECT  
Cloud Guard | `cloud-guard-managed-lists` | CG_MANAGED_LIST_INSPECT  
Cloud Guard | `cloud-guard-responder-recipes` | CG_RESPONDER_RECIPE_INSPECT  
Cloud Guard | `cloud-guard-targets` | CG_TARGET_INSPECT  
Cluster Placement Groups | `cluster-placement-group` | CLUSTER_PLACEMENT_GROUP_INSPECT  
Compute | `auto-scaling-configurations` | AUTO_SCALING_CONFIGURATION_INSPECT  
Compute | `cluster-networks` | CLUSTER_NETWORK_INSPECT  
Compute | `compute-capacity-reservations` | CAPACITY_RESERVATION_INSPECT  
Compute  | `console-histories` | CONSOLE_HISTORY_INSPECT  
Compute | `dedicated-vm-hosts` | DEDICATED_VM_HOST_INSPECT  
Compute | `instances` | INSTANCE_READ  
Compute  | `instance-images` | INSTANCE_IMAGE_READ  
Compute | `instance-configurations` | INSTANCE_CONFIGURATION_INSPECT  
Compute | `instance-pools` | INSTANCE_POOL_INSPECT  
Compute Cloud@Customer | `ccc-infrastructure` | CCC_INFRASTRUCTURE_INSPECT  
Compute Cloud@Customer | `ccc-upgrade-schedule` | CCC_UPGRADE_SCHEDULE_INSPECT  
Connector Hub | `serviceconnectors` | SERVICE_CONNECTOR_INSPECT  
Container Instances | `compute-containers` | COMPUTE_CONTAINER_INSPECT  
Container Instances | `compute-container-instances` | COMPUTE_CONTAINER_INSTANCE_INSPECT  
Container Registry | `repos` | REPOSITORY_INSPECT  
Content Management | `oce-instances` | OCE_INSTANCE_INSPECT  
Console Dashboards | `dashboards` | DASHBOARD_INSPECT  
Console Dashboards | `dashboard-groups` | DASHBOARD_GROUP_INSPECT  
Data Catalog | `data-catalogs` | CATALOG_INSPECT  
Data Catalog | `data-catalog-private-endpoints` | CATALOG_PRIVATE_ENDPOINT_INSPECT  
Data Catalog | `data-catalog-metastores` | CATALOG_METASTORE_INSPECT  
Data Flow | `dataflow-application` | DATAFLOW_APPLICATION_INSPECT  
Data Flow | `dataflow-run` | DATAFLOW_RUN_INSPECT  
Data Integration | `dis-workspaces` | DIS_WORKSPACE_INSPECT  
Data Labeling | `data-labeling-datasets` | DATA_LABELING_DATASET_INSPECT  
Data Safe | `data-safe-private-endpoints` | DATA_SAFE_PRIVATE_ENDPOINT_INSPECT  
Data Science | `data-science-jobs` | DATA_SCIENCE_JOB_INSPECT  
Data Science | `data-science-job-runs` | DATA_SCIENCE_JOB_RUN_INSPECT  
Data Science | `data-science-models` | DATA_SCIENCE_MODEL_INSPECT  
Data Science | `data-science-model-deployments` | DATA_SCIENCE_MODEL_DEPLOYMENT_INSPECT  
Data Science | `data-science-notebook-sessions` | DATA_SCIENCE_NOTEBOOK_SESSION_INSPECT  
Data Science | `data-science-projects` | DATA_SCIENCE_PROJECT_INSPECT  
Database | `autonomous-container-databases` | AUTONOMOUS_CONTAINER_DATABASE_INSPECT  
Database | `autonomous-databases` | AUTONOMOUS_DATABASE_INSPECT  
Database | `autonomous-vmclusters` | AUTONOMOUS_VM_CLUSTER_INSPECT  
Database | `backup-destinations` | BACKUP_DESTINATION_INSPECT  
Database | `cloud-autonomous-vmclusters` | CLOUD_AUTONOMOUS_VM_CLUSTER_INSPECT  
Database | `cloud-exadata-infrastructures` | CLOUD_EXADATA_INFRASTRUCTURE_INSPECT  
Database | `cloud-vmclusters` | CLOUD_VM_CLUSTER_INSPECT  
Database  | `databases` | DATABASE_INSPECT  
Database | `database-software-images` | DB_SOFTWARE_IMG_INSPECT  
Database  | `db-homes` | DB_HOME_INSPECT (if you want to filter results using `db-homes` attributes)  
Database | `key-stores` | KEY_STORE_INSPECT  
Database | `db-nodes` | DB_NODE_INSPECT, DB_NODE_QUERY  
Database | `dbservers` | EXADATA_INFRASTRUCTURE_INSPECT  
Database  | `db-systems` | DB_SYSTEM_INSPECT  
Database | `exadata-infrastructures` | EXADATA_INFRASTRUCTURE_INSPECT  
Database | `external-container-databases` | EXTERNAL_CONTAINER_DATABASE_INSPECT  
Database | `external-database-connectors` | EXTERNAL_DATABASE_CONNECTOR_INSPECT  
Database | `external-non-container-databases` | EXTERNAL_NON_CONTAINER_DATABASE_INSPECT  
Database | `external-pluggable-databases` | EXTERNAL_PLUGGABLE_DATABASE_INSPECT  
Database | `pluggable-databases` | PLUGGABLE_DATABASE_INSPECT  
Database | `vmclusters` | VM_CLUSTER_INSPECT  
Database | `vmcluster-networks` | EXADATA_INFRASTRUCTURE_INSPECT  
Database Management | `dbmgmt-external-asms` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-asm-instance` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-cluster` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-cluster-instance` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-dbhome` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-dbnode` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-dbsystem` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-db-system-connector` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-external-exadata-infrastructure` | DBMGMT_EXTERNAL_EXADATA_INSPECT  
Database Management | `dbmgmt-external-exadata-storage-connector` | DBMGMT_EXTERNAL_EXADATA_INSPECT  
Database Management | `dbmgmt-external-exadata-storage-grid` | DBMGMT_EXTERNAL_EXADATA_READ  
Database Management | `dbmgmt-external-exadata-storage-server` | DBMGMT_EXTERNAL_EXADATA_INSPECT  
Database Management | `dbmgmt-external-listener` | DBMGMT_EXTERNAL_DBSYSTEM_INSPECT  
Database Management | `dbmgmt-jobs` | DBMGMT_JOB_INSPECT  
Database Management | `dbmgmt-managed-databases` | DBMGMT_MANAGED_DB_INSPECT  
Database Management | `dbmgmt-managed-database-groups` | DBMGMT_MANAGED_DB_GROUP_INSPECT  
Database Management | `dbmgmt-named-credentials` | DBMGMT_NAMED_CREDENTIAL_INSPECT  
Database Management | `dbmgmt-private-endpoints` | DBMGMT_PRIVATE_ENDPOINT_INSPECT  
Database Migration | `odms-agent` | ODMS_AGENT_INSPECT  
Database Migration | `odms-connection` | ODMS_CONNECTION_INSPECT  
Database Migration | `odms-job` | ODMS_JOB_INSPECT  
Database Migration | `odms-migration` | ODMS_MIGRATION_INSPECT  
Database Tools | `database-tools-connections` | DATABASE_TOOLS_CONNECTION_INSPECT  
Database Tools | `database-tools-private-endpoints` | DATABASE_TOOLS_PRIVATE_ENDPOINT_INSPECT  
DevOps | `devops-deploy-artifact` | DEVOPS_DEPLOY_ARTIFACT_INSPECT  
DevOps | `devops-deploy-environment` | DEVOPS_DEPLOY_ENVIRONMENT_INSPECT  
DevOps | `devops-deployment` | DEVOPS_DEPLOYMENT_INSPECT  
DevOps | `devops-deploy-pipeline` | DEVOPS_DEPLOY_PIPELINE_INSPECT  
DevOps | `devops-build-pipeline` | DEVOPS_BUILD_PIPELINE_INSPECT  
DevOps | `devops-build-pipeline-stage` | DEVOPS_BUILD_PIPELINE_STAGE_INSPECT  
DevOps | `devops-deploy-stage` | DEVOPS_DEPLOY_STAGE_INSPECT  
DevOps | `devops-repository` | DEVOPS_REPOSITORY_INSPECT  
DevOps | `devops-connection` | DEVOPS_CONNECTION_INSPECT  
DevOps | `devops-trigger` | DEVOPS_TRIGGER_INSPECT  
DevOps | `devops-project` | DEVOPS_PROJECT_INSPECT  
Digital Assistant | `oda-instances` | ODA_INSTANCES_LIST  
Email Delivery | `approved-senders` | APPROVED_SENDER_INSPECT  
Email Delivery | `email-domains` | EMAIL_DOMAIN_INSPECT  
Email Delivery | `dkim` | DKIM_INSPECT  
Events | `cloudevents-rules` | EVENTRULE_LIST  
File Storage | `file-systems` | FILE_SYSTEM_INSPECT  
File Storage | `mount-target` | MOUNT_TARGET_INSPECT  
Fleet Application Management | `fams-fleets` | FAMS_FLEET_INSPECT  
Fleet Application Management | `fams-maintenance-windows` | FAMS_MAINTENANCE_WINDOW_INSPECT  
Fleet Application Management | `fams-schedules` | FAMS_SCHEDULE_INSPECT  
Full Stack Disaster Recovery | `disaster-recovery-protection-groups` | DISASTER_RECOVERY_PROTECTION_GROUP_INSPECT  
Full Stack Disaster Recovery | `disaster-recovery-plans` | DISASTER_RECOVERY_PLAN_INSPECT  
Full Stack Disaster Recovery | `disaster-recovery-plan-executions` | DISASTER_RECOVERY_PLAN_EXECUTION_INSPECT  
Functions | `fn-app` | FN_APP_LIST  
Functions | `fn-function` | FN_FUNCTION_LIST  
Globally Distributed Autonomous Database | `sharded-database` | SDB_INSPECT  
Globally Distributed Autonomous Database | `osdprivateendpoint` |  VCN_READ SUBNET_READ VNIC_READ  
GoldenGate | `goldengate-deployments` | GOLDENGATE_DEPLOYMENT_INSPECT  
GoldenGate | `goldengate-connections` | GOLDENGATE_CONNECTION_INSPECT  
IAM  | `compartments` | COMPARTMENT_INSPECT  
IAM  | `groups` | GROUP_INSPECT  
IAM  | `identity-providers` | IDENTITY_PROVIDER_INSPECT  
IAM | `policies` | POLICY_READ  
IAM | `tag-defaults` |  TAG_DEFAULT_INSPECT TAG_NAMESPACE_READ  
IAM | `tag-namespaces` | TAG_NAMESPACE_INSPECT  
IAM  | `users` | USER_INSPECT  
Integration | `integration-instance` | INTEGRATION_INSTANCE_INSPECT  
Java Management | `fleets` | FLEET_INSPECT  
Kubernetes Engine | `clusters` | CLUSTER_INSPECT  
Kubernetes Engine | `cluster-virtualnode-pools` | CLUSTER_VIRTUAL_NODE_POOL_INSPECT  
Kubernetes Engine | `clustersvirtualnode` | CLUSTER_VIRTUAL_NODE_POOL_READ  
Load Balancer | `load-balancers` | LOAD_BALANCER_INSPECT  
Logging | `logs` | LOG_GROUP_INSPECT  
Logging | `log-groups` | LOG_GROUP_INSPECT  
Logging | `unified-configuration` | UNIFIED_AGENT_CONFIG_INSPECT  
Management Agent | `management-agents` | MGMT_AGENT_INSPECT  
Management Agent | `management-agent-install-keys` | MGMT_AGENT_INSTALL_KEY_INSPECT  
Media Services (Media Flow) | `media-workflow` | MEDIA_WORKFLOW_INSPECT  
Media Services (Media Streams) | `media-stream-distribution-channel` | MEDIA_STREAM_DISTRIBUTION_CHANNEL_INSPECT  
Media Services (Media Streams) | `media-stream-packaging-config` | MEDIA_STREAM_PACKAGING_CONFIG_INSPECT  
Media Services (Media Streams) | `media-stream-cdn-config` | MEDIA_STREAM_CDN_CONFIG_INSPECT  
Monitoring | `alarms` | ALARM_INSPECT  
Network Firewall | `network-firewall-policy` | NETWORK_FIREWALL_POLICY_INSPECT  
Networking | `byoiprange` | BYOIP_RANGE_INSPECT  
Networking | `cpes` | CPE_READ  
Networking | `cross-connects` | CROSS_CONNECT_READ  
Networking | `cross-connect-groups` | CROSS_CONNECT_GROUP_READ  
Networking | `dhcp-options` | DHCP_READ  
Networking | `drgs` | DRG_READ  
Networking | `internet-gateways` | INTERNET_GATEWAY_READ  
Networking | `ipsec` | IPSEC_CONNECTION_READ  
Networking | `ipv6s` |  IPV6_READ VNIC_INSPECT SUBNET_INSPECT  
Networking | `local-peering-gateways` | LOCAL_PEERING_GATEWAY_READ  
Networking | `nat-gateways` | NAT_GATEWAY_READ  
Networking | `network-security-groups` | NETWORK_SECURITY_GROUP_INSPECT  
Networking | `public-ips` | PUBLIC_IP_READ  
Networking | `publicippool` | PUBLIC_IP_POOL_INSPECT  
Networking | `private-ips` | PRIVATE_IP_READ  
Networking | `remote-peering-connections` | REMOTE_PEERING_CONNECTION_READ  
Networking  | `route-tables` | ROUTE_TABLE_READ  
Networking  | `security-lists` | SECURITY_LIST_READ  
Networking | `service-gateways` | SERVICE_GATEWAY_READ  
Networking  | `subnets` | SUBNET_READ  
Networking  | `vcns` | VCN_READ  
Networking | `virtualcircuit` | VIRTUAL_CIRCUIT_READ  
Networking | `vlan` | VLAN_READ  
Networking | `vnic` | VNIC_READ  
NoSQL Database Cloud | `nosql-tables` | NOSQL_TABLE_INSPECT  
Notifications | `ons-subscriptions` | ONS_SUBSCRIPTION_INSPECT  
Notifications | `ons-topics` | ONS_TOPIC_INSPECT  
Object Storage  | `buckets` | BUCKET_INSPECT  
OCI Database with PostgreSQL | `postgres-backups` | POSTGRES_BACKUP_INSPECT  
OCI Database with PostgreSQL | `postgres-configurations` | POSTGRES_CONFIGURATION_INSPECT  
OCI Database with PostgreSQL | `postgres-db-systems` | POSTGRES_DB_SYSTEM_INSPECT  
OS Management | `osms-managed-instance-groups` | OSMS_MANAGED_INSTANCE_GROUP_INSPECT  
OS Management | `osms-scheduled-jobs` | OSMS_SCHEDULED_JOB_INSPECT  
OS Management | `osms-software-sources` | OSMS_SOFTWARE_SOURCE_INSPECT  
OS Management Hub | `osmh-lifecycle-environments` | OSMH_LIFECYCLE_ENVIRONMENT_INSPECT  
OS Management Hub | `osmh-managed-instance-groups` | OSMH_MANAGED_INSTANCE_GROUP_INSPECT  
OS Management Hub | `osmh-management-stations` | OSMH_MANAGEMENT_STATION_INSPECT  
OS Management Hub | `osmh-profiles` | OSMH_PROFILE_INSPECT  
OS Management Hub | `osmh-scheduled-jobs` | OSMH_SCHEDULED_JOB_INSPECT  
OS Management Hub | `osmh-software-sources` | OSMH_SOFTWARE_SOURCE_INSPECT  
Process Automation | `process-automation-instance` | PROCESS_AUTOMATION_INSTANCE_INSPECT  
Queue | `queue` | QUEUE_INSPECT  
Resource Explorer | `resource-collections` | RESOURCE_COLLECTION_INSPECT  
Resource Manager | `orm-config-source-providers` | ORM_CONFIG_SOURCE_PROVIDER_INSPECT  
Resource Manager | `orm-jobs` | ORM_JOB_INSPECT  
Resource Manager | `orm-private-endpoints` | ORM_PRIVATE_ENDPOINT_INSPECT  
Resource Manager | `orm-stacks` | ORM_STACK_INSPECT  
Resource Manager | `orm-templates` | ORM_TEMPLATE_INSPECT  
Security Zones | `security-zone` | SECURITY_ZONE_INSPECT  
Security Zones | `security-recipe` | SECURITY_RECIPE_INSPECT  
Service Limits | `quotas` | QUOTA_INSPECT  
Service Mesh | `service-meshes` | SERVICE_MESH_LIST  
Service Mesh | `mesh-access-policies` | MESH_ACCESS_POLICY_LIST  
Service Mesh | `mesh-ingress-gateways` | MESH_INGRESS_GATEWAY_LIST  
Service Mesh | `mesh-ingress-gateway-routetables` | MESH_INGRESS_GATEWAY_ROUTE_TABLE_LIST  
Service Mesh | `mesh-virtual-deployments` | MESH_VIRTUAL_DEPLOYMENT_LIST  
Service Mesh | `mesh-virtual-services` | MESH_VIRTUAL_SERVICE_LIST  
Service Mesh | `mesh-virtual-service-route-tables` | MESH_VIRTUAL_SERVICE_ROUTE_TABLE_LIST  
Streaming | `connect-harnesses` | CONNECT_HARNESS_INSPECT  
Streaming | `streams` | STREAM_INSPECT  
Vault | `keys` | KEY_INSPECT  
Vault | `vaults` | VAULT_INSPECT  
Vault | `secrets` | SECRET_INSPECT  
Visual Builder | `visualbuilder-instance` | VISUALBUILDER_INSTANCE_INSPECT  
Visual Builder Studio | `vbstudio-instances` | VBS_INSTANCE_INSPECT  
VMware Solution | `vmwareesxihost` | SDDC_INSPECT  
VMware Solution | `vmwaresddc` | SDDC_INSPECT  
Vulnerability Scanning | `host-scan-recipes` | VSS_HOSTSCANRECIPE_INSPECT  
Vulnerability Scanning | `host-scan-targets` | VSS_HOSTSCANTARGET_INSPECT  
Vulnerability Scanning | `container-scan-recipes` | VSS_CONTAINERSCAN_INSPECT  
Vulnerability Scanning | `container-scan-targets` | VSS_CONTAINERSCANTARGET_INSPECT  
WAF | `http-redirects` | HTTPREDIRECT_INSPECT  
WAF | `waas-address-list` | WAAS_ADDRESS_LIST_INSPECT  
WAF | `waas-certificate` | WAAS_CERTIFICATE_INSPECT  
WAF | `waas-custom-protection-rule` | WAAS_CUSTOM_PROTECTION_RULE_INSPECT  
WAF | `waas-policy` | WAAS_POLICY_INSPECT  
Zero Trust Packet Routing | `security-attribute-namespace` | ZPR_POLICY_INSPECT  
Zero Trust Packet Routing | `zpr-policy` | SECURITY_ATTRIBUTE_NAMESPACE_INSPECT  
Was this article helpful?
YesNo

