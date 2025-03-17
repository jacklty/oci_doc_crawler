Updated 2024-11-14
# Services Reference
This section describes how to find Oracle Cloud Infrastructure Resource Manager reference information and lists supported services.
This topic provides a reference of the Oracle Cloud Infrastructure (OCI) services that Resource Manager supports.
## Full Reference Documentation 🔗 
The full reference of the resources and data sources supported by Resource Manager contains usage, argument, and attribute details. The full reference is available at [docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/) and [Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs).
Data sources and resources are grouped by service within the reference.
The [Deprecated Resources](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/deprecated-resources.htm#top "Review the list of deprecated Oracle Cloud Infrastructure Terraform provider resources.") reference lists the resources and data sources marked for deprecation by the Oracle Cloud Infrastructure (OCI) Terraform provider.
## Supported Services 🔗 
The following table lists the services supported by the OCI Terraform provider and the services supported by the [resource discovery](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resource-discovery.htm) feature. This list also includes the values accepted by resource discovery's `services` parameter.
**Note** Resource discovery may not be available for all services that Resource Manager supports.
Supported OCI service | Resource discovery support | Resource discovery services parameter  
---|---|---  
Account Management (Billing and Subscriptions) | No | N/A  
Analytics Cloud | Yes | `analytics`  
Announcements | Yes | `announcements_service`  
Anomaly Detection | Yes | `ai_anomaly_detection`  
API Gateway | Yes | `apigateway`  
Application Dependency Management | Yes | `adm`  
Application Performance Monitoring | Yes | `apm`  
Application Performance Monitoring (Synthetic Monitoring) | Yes | `apm_synthetics`  
Application Performance Monitoring (Configuration) | Yes | `apm_config`  
Artifact Registry (Generic Artifacts Content API) | Yes | `artifacts`  
Audit | No | N/A  
Autonomous Recovery Service | Yes | `recovery`  
Autoscaling (Compute) | Yes | `auto_scaling`  
Bastion | Yes | `bastion`  
Big Data Service | Yes | `bds`  
Blockchain Platform | Yes | `blockchain`  
Budgets | Yes | `budget`  
OCI Cache | Yes | `redis`  
Certificates | Yes | `certificates_management`  
Oracle Cloud Bridge | Yes | `cloud_bridge`  
Cloud Guard | Yes | `cloud_guard`  
Oracle Cloud Migrations | Yes | `cloud_migrations`  
Compute Cloud@Customer | Yes | `compute_cloud_at_customer`  
Connector Hub | Yes | `sch`  
Kubernetes Engine | Yes | `containerengine`  
Content Management | Yes | `oce`  
Core Services (Networking, Compute, Block Volume) | Yes | `core`  
Cost Analysis (Usage API, Usage Proxy API) | Yes | `metering_computation`, `usage_proxy`  
Data Catalog | Yes | `datacatalog`  
Data Flow | Yes | `dataflow`  
Data Integration | Yes | `dataintegration`  
Data Labeling | Yes | `data_labeling_service`  
Data Safe | Yes | `data_safe`  
Data Science | Yes | `datascience`  
Database | Yes | `database`  
Database Management | Yes | `database_management`  
Database Migration | Yes | `database_migration`  
Database Tools | Yes | `database_tools`  
Delegate Access Control | Yes | `delegate_access_control`  
DevOps | Yes | `devops`  
Digital Assistant | Yes | `oda`  
DNS Service | Yes | `dns`  
Document Understanding | Yes | `ai_document`  
Email Delivery | Yes | `email`, `email_tenancy`  
Events | Yes | `events`  
FastConnect | No | N/A  
File Storage | Yes | `file_storage`  
[Exadata Fleet Update](https://docs.oracle.com/iaas/edsfu/index.html) | Yes | `fleet_software_update`  
[Fleet Application Management](https://docs.oracle.com/iaas/Content/fleet-management/home.htm) | Yes | `fleet_apps_management`  
Full Stack Disaster Recovery | Yes | `disaster_recovery`  
Functions | Yes | `functions`  
Fusion Applications Environment Management | Yes | `fusion_apps`  
Generative AI | Yes | `generative_ai`  
Generative AI Agents | Yes | `generative_ai_agent`  
Globally Distributed Database | Yes | `globally_distributed_database`  
GoldenGate | Yes | `golden_gate`  
Health Checks | Yes | `health_checks`  
IAM | Yes | `identity`, `identity_data_plane`, `availability_domain`  
Identity Domains | Yes | `identity_domains`  
Integration Cloud | Yes | `integration`  
Java Management | Yes | `jms`  
Key Management (for the Vault service) | Yes | `kms`  
Language | Yes | `ai_language`  
License Manager | Yes | `license_manager`  
Limits | Yes | `limits`  
Load Balancer | Yes | `load_balancer`  
Logging | Yes | `logging`  
Logging Analytics | Yes | `log_analytics`  
Management Agent | Yes | `management_agent`  
Management Dashboard  | No | N/A  
Marketplace | Yes | `marketplace`  
Media Services | Yes | `media_services`  
Monitoring | Yes | `monitoring`  
HeatWave | Yes | `mysql`  
Network Firewall | Yes | `network_firewall`  
Network Load Balancer | Yes | `network_load_balancer`  
NoSQL Database Cloud | Yes | `nosql`  
Notifications | Yes | `ona`  
Object Storage | Yes | `object_storage`  
OCI Control Center | Yes | `capacity_management`  
OCI Control Center - Demand Signal | Yes | `demand_signal`  
Ops Insights | Yes | `opsi`  
Operator Access Control (Database) | Yes | `operator_access_control`  
Optimizer | Yes | `optimizer`  
OS Management (including Resource Monitoring Management Agent Plugin) | Yes | `osmanagement`  
OS Management Hub | Yes | `os_management_hub`  
OCI Database with PostgreSQL | Yes | `psql`  
Process Automation | Yes | `opa`  
Queue | Yes | `queue`  
Registry (Artifacts and Container Images API) | Yes | `artifacts`  
Resource Manager | Yes | `resourcemanager`  
Resource Scheduler | Yes | `resource_scheduler`  
Search with OpenSearch | Yes | `opensearch`  
Secrets (for the Vault service) | No | N/A  
Secure Desktops | Yes | `desktops`  
Security Attributes (Zero Trust Packet Routing) | Yes | `security_attribute`  
Service Manager Proxy (Applications Console) | No | N/A  
Service Mesh | Yes | `service_mesh`  
Streaming | Yes | `streaming`  
Tagging | Yes | `tagging`  
Vision | Yes | `ai_vision`  
Visual Builder | Yes | `visual_builder`  
Visual Builder Studio | Yes | `vbs_inst`  
Oracle Cloud VMware Solution | Yes | `ocvp`  
Vault | Yes | `vault`  
Vulnerability Scanning | Yes | `vulnerability_scanning`  
Web Application Acceleration | Yes | `waa`  
Web Application Firewall (WAF) | Yes | `waas`, `waf`  
Zero Trust Packet Routing | Yes | `zpr`  
Was this article helpful?
YesNo

