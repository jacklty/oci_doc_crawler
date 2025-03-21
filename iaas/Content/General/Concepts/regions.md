Updated 2025-03-11
# Regions and Availability Domains
This topic describes the physical and logical organization of Oracle Cloud Infrastructure resources.
## About Regions and Availability Domains 🔗 
Oracle Cloud Infrastructure is hosted in regions and availability domains. A region is a localized geographic area, and an availability domain is one or more data centers located within a region. A region is composed of one or more availability domains. Most Oracle Cloud Infrastructure resources are either region-specific, such as a virtual cloud network, or availability domain-specific, such as a compute instance. Traffic between availability domains and between regions is encrypted. Availability domains are isolated from each other, fault tolerant, and very unlikely to fail simultaneously. Because availability domains do not share infrastructure such as power or cooling, or the internal availability domain network, a failure at one availability domain within a region is unlikely to impact the availability of the others within the same region. 
The availability domains within the same region are connected to each other by a low latency, high bandwidth network, which makes it possible for you to provide high-availability connectivity to the internet and on-premises, and to build replicated systems in multiple availability domains for both high-availability and disaster recovery.
Oracle is adding multiple cloud regions around the world to provide local access to cloud resources for our customers. To accomplish this quickly, we have chosen to launch regions in new geographies with one availability domain.
As regions require expansion, we have the option to add capacity to existing availability domains, to add additional availability domains to an existing region, or to build a new region. The expansion approach in a particular scenario is based on customer requirements as well as considerations of regional demand patterns and resource availability.
Regions are independent of other regions and can be separated by vast distances—across countries or even continents. Generally, you would deploy an application in the region where it is most heavily used, because using nearby resources is faster than using distant resources. However, you can also deploy applications in different regions for these reasons:
  * To mitigate the risk of region-wide events such as large weather systems or earthquakes.
  * To meet varying requirements for legal jurisdictions, tax domains, and other business or social criteria.


Regions are grouped into **realms**. Your tenancy exists in a single realm and can access all regions that belong to that realm. You cannot access regions that are not in your realm. Currently, Oracle Cloud Infrastructure has multiple realms, including commercial, [government](https://docs.oracle.com/en-us/iaas/Content/gov-cloud/govlanding.htm "Review government cloud services included in Oracle Cloud Infrastructure."), and [dedicated](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/dedicatedregions.htm#dedicatedregions "Dedicated regions are public regions assigned to a single organization. Region specific details, such as region ID and region key are not available in public documentation, check with your Oracle contact for this information for your dedicated region.") realms. 
The following table lists the regions in the Oracle Cloud Infrastructure commercial **realms** :
Region Name | Region Identifier | Region Location | Region Key | Realm Key | Availability Domains  
---|---|---|---|---|---  
Australia East (Sydney)  | ap-sydney-1  | Sydney, Australia | SYD  | OC1 | 1  
Australia Southeast (Melbourne)  | ap-melbourne-1  | Melbourne, Australia | MEL  | OC1 | 1  
Brazil East (Sao Paulo)  | sa-saopaulo-1  | Sao Paulo, Brazil | GRU  | OC1 | 1  
Brazil Southeast (Vinhedo)  | sa-vinhedo-1  | Vinhedo, Brazil | VCP  | OC1 | 1  
Canada Southeast (Montreal)  | ca-montreal-1  | Montreal, Canada | YUL  | OC1 | 1  
Canada Southeast (Toronto)  | ca-toronto-1  | Toronto, Canada | YYZ  | OC1 | 1  
Chile Central (Santiago)  | sa-santiago-1  | Santiago, Chile | SCL  | OC1 | 1  
Chile West (Valparaiso)  | sa-valparaiso-1  | Valparaiso, Chile | VAP  | OC1 | 1  
Colombia Central (Bogota)  | sa-bogota-1  | Bogota, Colombia | BOG  | OC1 | 1  
France Central (Paris)  | eu-paris-1  | Paris, France | CDG  | OC1 | 1  
France South (Marseille)  | eu-marseille-1  | Marseille, France | MRS  | OC1 | 1  
Germany Central (Frankfurt)  | eu-frankfurt-1  | Frankfurt, Germany | FRA  | OC1 | 3  
India South (Hyderabad)  | ap-hyderabad-1  | Hyderabad, India | HYD  | OC1  | 1  
India West (Mumbai)  | ap-mumbai-1  | Mumbai, India | BOM  | OC1  | 1  
Israel Central (Jerusalem) | il-jerusalem-1 | Jerusalem, Israel | MTZ | OC1 | 1  
Italy Northwest (Milan)  | eu-milan-1  | Milan, Italy | LIN  | OC1 | 1  
Japan Central (Osaka)  | ap-osaka-1  | Osaka, Japan | KIX  | OC1 | 1  
Japan East (Tokyo)  | ap-tokyo-1  | Tokyo, Japan | NRT  | OC1 | 1  
Mexico Central (Queretaro)  | mx-queretaro-1  | Queretaro, Mexico | QRO  | OC1 | 1  
Mexico Northeast (Monterrey)  | mx-monterrey-1  | Monterrey, Mexico | MTY  | OC1 | 1  
Netherlands Northwest (Amsterdam)  | eu-amsterdam-1  | Amsterdam, Netherlands | AMS  | OC1 | 1  
Saudi Arabia Central (Riyadh)  | me-riyadh-1  | Riyadh, Saudi Arabia | RUH | OC1 | 1  
Saudi Arabia West (Jeddah)  | me-jeddah-1  | Jeddah, Saudi Arabia | JED  | OC1 | 1  
Serbia Central (Jovanovac)  | eu-jovanovac-1  | Jovanovac,Serbia | BEG  | OC20 | 1  
Singapore (Singapore)  | ap-singapore-1  | Singapore,Singapore | SIN  | OC1 | 1  
Singapore West (Singapore)  | ap-singapore-2  | Singapore,Singapore | XSP  | OC1 | 1  
South Africa Central (Johannesburg)  | af-johannesburg-1  | Johannesburg, South Africa | JNB  | OC1 | 1  
South Korea Central (Seoul)  | ap-seoul-1  | Seoul, South Korea | ICN  | OC1 | 1  
South Korea North (Chuncheon)  | ap-chuncheon-1  | Chuncheon, South Korea | YNY  | OC1 | 1  
Spain Central (Madrid)  | eu-madrid-1  | Madrid, Spain | MAD  | OC1 | 1  
Sweden Central (Stockholm)  | eu-stockholm-1  | Stockholm, Sweden | ARN  | OC1 | 1  
Switzerland North (Zurich)  | eu-zurich-1  | Zurich, Switzerland | ZRH  | OC1 | 1  
UAE Central (Abu Dhabi)  | me-abudhabi-1  | Abu Dhabi, UAE | AUH  | OC1 | 1  
UAE East (Dubai)  | me-dubai-1  | Dubai, UAE | DXB  | OC1 | 1  
UK South (London)  | uk-london-1  | London, United Kingdom | LHR  | OC1 | 3  
UK West (Newport)  | uk-cardiff-1  | Newport, United Kingdom | CWL  | OC1 | 1  
US East (Ashburn)  | us-ashburn-1  | Ashburn, VA | IAD  | OC1 | 3  
US Midwest (Chicago)  | us-chicago-1  | Chicago, IL | ORD  | OC1 | 3  
US West (Phoenix)  | us-phoenix-1  | Phoenix, AZ  | PHX  | OC1 | 3  
US West (San Jose)  | us-sanjose-1  | San Jose, CA  | SJC  | OC1 | 1  
To subscribe to a region, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#Managing_Regions).
For a list of regions in the Oracle Government Cloud realms, see the following topics:
  * [Oracle US Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govfedramp.htm)
  * [Oracle US Defense Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govfeddod.htm)
  * [Oracle Cloud Infrastructure United Kingdom Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govuksouth.htm)
  * [Oracle Cloud Infrastructure for Australia Government and Defence](https://docs.oracle.com/iaas/Content/gov-cloud/ausgov.htm)


## Your Tenancy's Availability Domain Names 🔗 
To help balance capacity in data centers, Oracle Cloud Infrastructure randomizes availability domains by **tenancy**. For example, the availability domain labeled `PHX-AD-1` for tenancyA might be a different data center than the one labeled `PHX-AD-1` for tenancyB. 
To track which availability domain corresponds to which data center for each tenancy, Oracle Cloud Infrastructure uses tenancy-specific prefixes for availability domain names. An example prefix is `Uocm:`. With this prefix, availability domain names are `Uocm:PHX-AD-1`, `Uocm:PHX-AD-2`, and so on.
To get the specific names of your tenancy's availability domains, use the [ListAvailabilityDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/AvailabilityDomain/ListAvailabilityDomains) operation, which is available in the IAM API. You can also see the names when you use the Console to [create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) and choose which availability domain to create the instance in.
## Fault Domains 🔗 
A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains provide anti-affinity: they let you distribute your instances so that the instances are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance event that affects one fault domain does not affect instances in other fault domains. 
To control the placement of your compute instances, bare metal DB system instances, or virtual machine DB system instances, you can optionally specify the fault domain for a new instance or instance pool at launch time. If you don't specify the fault domain, the system selects one for you. Oracle Cloud Infrastructure makes a best-effort anti-affinity placement across different fault domains, while optimizing for available capacity in the availability domain. To change the fault domain for a compute instance, [edit the fault domain](https://docs.oracle.com/iaas/Content/Compute/Tasks/edit-fault-domain.htm). To change the fault domain for a bare metal or virtual machine DB system instance, terminate it and launch a new instance in the preferred fault domain.
Use fault domains to do the following things:
  * Protect against unexpected hardware failures.
  * Protect against planned outages because of Compute hardware maintenance.


For more information:
  * For recommendations about how to use fault domains when provisioning application and database servers, see [Fault Domains](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm#Fault) in [Best Practices for Your Compute Instances](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm).


## Subscribed Region Limits 🔗 
Trial, free tier, and pay-as-you-go tenancies are limited to one subscribed region. You can request an increase to the limit for pay-as-you-go tenancies, see [To request a subscribed region limit increase](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#To_request_a_subscribed_region_limit_increase) for more information.
Universal monthly credit tenancies can subscribe to all publicly released commercial regions. 
### Requesting a Limit Increase to the Subscribed Region Count 🔗 
You can submit a request to increase the subscribed region count for your tenancies from within the Console. If you try to subscribe to a region beyond the limit for your tenancy, you'll be prompted to submit a limit increase request. Additionally, you can launch the request from the service limits page or at any time by clicking the link under the **Help** menu (![Help menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/help-menu.png)). 
[To request a subscribed region limit increase](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)
  1. Open the **Help** menu (![Help menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/help-menu.png)), go to **Support** and click **Request service limit increase**.
  2. Enter the following:
     * **Primary Contact Details:** Enter the name and email address of the person making the request. Enter one email address only. A confirmation will be sent to this address. 
     * **Service Category:** Select **Regions**. 
     * **Resource:** Select **Subscribed region count**. 
     * **Tenancy Limit:** Specify the limit number. 
     * **Reason for Request:** Enter a reason for your request. If your request is urgent or unusual, please provide details here.
  3. Click **Submit Request**.


After you submit the request, it is processed. A response can take anywhere from a few minutes to a few days. If your request is granted, a confirmation email is sent to the address provided in the primary contact details. 
If we need additional information about your request, a follow-up email is sent to the address provided in the primary contact details. 
## Service Availability Across Regions 🔗 
OCI offers its cloud services in all of its public cloud regions and dedicated cloud regions. However, certain specialized or emerging services are available only in select regions. For more information, see [Service Availability](https://www.oracle.com/cloud/distributed-cloud/#service-availability).
## Resource Availability 🔗 
The following sections list the resource types based on their availability: across regions, within a single region, or within a single availability domain. 
**Tip** In general: IAM resources are cross-region. DB Systems, instances, and volumes are specific to an availability domain. Everything else is regional. Exception: Subnets were originally designed to be specific to an availability domain. Now, you can create [regional subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm), which are what Oracle recommends. 
### Cross-Region Resources 🔗 
  * API signing keys
  * compartments
  * detectors (Cloud Guard; regional to reporting region)
  * dynamic groups
  * federation resources
  * groups
  * managed lists (Cloud Guard)
  * network sources
  * policies (IAM and Zero Trust Packet Routing
  * responders (Cloud Guard; regional to reporting region)
  * security attributes (Zero Trust Packet Routing)
  * security attribute namespaces (Zero Trust Packet Routing)
  * tag namespaces
  * tag keys
  * targets (Cloud Guard; regional to reporting region)
  * users


### Regional Resources
  * access policies (Service Mesh)
  * agents (Database Migration)
  * alarms
  * apm-domains (Application Performance Monitoring)
  * applications (Data Flow service)
  * applications (Functions service)
  * artifact-repositories (Artifact Registry)
  * backups (OCI Database with PostgreSQL)
  * bastions
  * blockchain platforms (Blockchain Platform service)
  * buckets: Although buckets are regional resources, they can be accessed from any location if you use the correct region-specific Object Storage URL for the API calls.
  * infrastructures (Compute Cloud@Customer service)
  * upgrade schedules (Compute Cloud@Customer service)
  * clusters (Big Data Service service)
  * clusters (Kubernetes Engine service)
  * cluster placement groups (Cluster Placement Groups service)
  * cloudevents-rules
  * config work requests (Logging Analytics)
  * configurations (OCI Database with PostgreSQL)
  * configuration source providers (Resource Manager)
  * connections (Database Migration)
  * connectors (Connector Hub)
  * content and experience (Content Management)
  * customer-premises equipment (CPE)
  * dashboards (Console Dashboards)
  * dashboards (Management Dashboard)
  * dashboard-groups (Console Dashboards)
  * data catalogs
  * database insights (Ops Insights)
  * databases (OCI Database with PostgreSQL)
  * datasets (Data Labeling)
  * DB Systems (HeatWave service)
  * deployments (GoldenGate)
  * desktop pools (Secure Desktops)
  * devops projects (DevOps)
  * build pipelines (DevOps)
  * code repositories (DevOps)
  * deployment pipelines (DevOps)
  * DHCP options sets
  * discovery jobs (Stack Monitoring)
  * DrProtectionGroup (Full Stack Disaster Recovery)
  * DrPlan (Full Stack Disaster Recovery)
  * DrPlanExecution (Full Stack Disaster Recovery)
  * dynamic routing gateways (DRGs)
  * encryption keys
  * entities (Logging Analytics)
  * fleets (Java Management)
  * fleets (Fleet Application Management)
  * functions
  * generic-artifacts (Artifact Registry)
  * groups (OS Management Hub)
  * host scans
  * images
  * ingress gateways (Service Mesh)
  * ingress gateway route tables (Service Mesh)
  * instances (OS Management Hub)
  * lifecycle environments (OS Management Hub)
  * lifecycle stages (OS Management Hub)
  * internet gateways
  * jobs (Database Management)
  * jobs (Database Migration)
  * jobs (Resource Manager)
  * load balancers
  * local peering gateways (LPGs)
  * log groups (Logging Analytics)
  * maintenance windows (Fleet Application Management)
  * management agent install keys
  * management agents
  * managed database groups (Database Management)
  * managed databases (Database Management)
  * management stations (OS Management Hub)
  * meshes (Service Mesh)
  * metrics
  * Media workflow (Media Flow)
  * Media workflow configuration (Media Flow) 
  * Media workflow job (Media Flow) 
  * Media asset (Media Flow)
  * migrations (Database Migration)
  * models
  * monitors (Health Checks)
  * NAT gateways
  * network firewall policies
  * network security groups
  * node pools
  * notebook sessions
  * object collection rules (Logging Analytics)
  * OpenSearch clusters (Search with OpenSearch)
  * OpenSearch cluster backups (Search with OpenSearch)
  * port scans
  * private endpoints (Database Management)
  * private endpoints (Resource Manager)
  * private endpoint work requests (Database Management)
  * private templates (Resource Manager)
  * probes (Health Checks)
  * problems (Cloud Guard; regional to reporting region)
  * profiles (OS Management Hub)
  * projects
  * properties (Fleet Application Management)
  * queryjob work requests (Logging Analytics)
  * queues
  * registered databases (GoldenGate)
  * repositories
  * reserved public IPs
  * resources (Stack Monitoring)
  * route tables
  * runs
  * runbooks (Fleet Application Management)
  * saved searches (Management Dashboard)
  * scan recipes
  * schedules (Fleet Application Management)
  * scheduled tasks (Logging Analytics)
  * scheduled jobs (OS Management Hub)
  * secrets
  * security lists
  * security zones
  * security zone recipes
  * service gateways
  * sessions (Bastion)
  * sharded-database (Globally Distributed Autonomous Database)
  * sharded-database-work-request (Globally Distributed Autonomous Database)
  * sharded-database-private-endpoint (Globally Distributed Autonomous Database)
  * software sources (OS Management Hub)
  * stacks (Resource Manager)
  * StreamDistributionChannel (Media Streams)
  * StreamPackagingConfig (Media Streams)
  * StreamCdnConfig (Media Streams)
  * storage work requests (Logging Analytics)
  * subnets: When you create a subnet, you choose whether it's [regional or specific to an availability domain](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm). Oracle recommends using regional subnets.
  * subscriptions
  * tables
  * targets (Vulnerability Scanning)
  * threat indicators
  * threat types
  * topics
  * vaults
  * virtual cloud networks (VCNs)
  * virtual deployments (Service Mesh)
  * virtual services (Service Mesh)
  * virtual service route tables (Service Mesh)
  * volume backups: They can be restored as new volumes to any availability domain within the same region in which they are stored.
  * vulnerability reports
  * workspaces


### Availability Domain-Specific Resources
  * container instances
  * DB systems (Oracle Database service)
  * ephemeral public IPs
  * instances (Compute): They can be attached only to volumes in the same availability domain.
  * network firewalls
  * subnets: When you create a subnet, you choose whether it is [regional or specific to an availability domain](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm). Oracle recommends using regional subnets.
  * volumes: They can be attached only to an instance in the same availability domain.


Was this article helpful?
YesNo

