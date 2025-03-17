Updated 2025-01-06
# Oracle-Provided Templates
Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.
You can access templates from the Console when you [create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm#top "Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario."). To browse templates of a given type, select the tab for that type. For example, to browse service templates, select the **Service** tab. After creating the stack with a template, [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") on the stack to provision those resources.
**Note**
Create your own [private templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm#top "Reuse Terraform configurations using private templates in Resource Manager.") to share with others in the tenancy.
Common uses of templates: 
  * Test-drive the idea of infrastructure as code.
  * Apply proven best practices to your production workflow configuration. 


## Quickstarts Templates 🔗 
Use Quickstarts to quickly launch and try real solutions for deployment scenarios while learning about OCI services and capabilities. [Create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm#top "Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") with this template for consistent and repeatable deployments.
To automatically provision resources, access Quickstarts templates from the Console home page. For more information, see [Widgets](https://docs.oracle.com/iaas/Content/GSG/Concepts/console-home.htm#widgets).
Template | Description  
---|---  
**Apache Tomcat on Arm** | Deploy a simple to-do application with Apache Tomcat  
**APEX with ADB** | Deploy a fully managed APEX instance  
**ASP.NET quickstart** | Deploy a sample ASP .NET application in a highly available configuration, with two Windows instances and a load balancer.  
**Baseline landing zone sandbox** | Landing zone sandbox developed by OCI  
**Deploy a WordPress instance on OCI** | Deploy a WordPress instance on OCI  
**Deploy Elasticsearch and Kibana in OCI** | Deploy Elasticsearch and Kibana in OCI  
**Deploy self-hosted productivity platform Nextcloud** | Deploy self-hosted productivity platform Nextcloud  
**Highly available web application with autoscaling** | Deploy a highly available three-tier web application with autoscaling in Oracle Cloud Infrastructure.  
**Jenkins quickstart** | Deploy a containerized Jenkins instance on OCI  
**MuShop Basic quickstart** | Three-tier web application using Always Free resources  
**OCI Kubernetes Monitoring Solution** | Monitor, manage, and generate insights into your Kubernetes deployed in OCI, third party public clouds, private clouds, or on-premises including managed Kubernetes deployments. The solution utilizes the following OCI services: Logging Analytics, Monitoring, and Management Agent.  
**ORACLE RED BULL RACING – Predict the result of the next race** | Predict the result of the next race with our Oracle Red Bull Racing machine learning hands-on-lab  
**RStudio** | Deploy the RStudio integrated development environment (IDE) for R on OCI  
**Strava data on Autonomous Database** | Visualize and analyze Strava data on Autonomous Database  
## Architecture Templates 🔗 
Use an **Architecture** template to [create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm#top "Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") that uses multiple cloud services.
Template (select to launch stack) | Description  
---|---  
[**AWX deployment using OKE**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=$%7BMessages.solutionsHub.solutions.ociAnsibleAWX.solutionName\(\)%7D) | Provision AWX v19.3 on the OKE cluster  
[**Departmental Data Warehousing**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=departmental-data-warehousing) | Provision Autonomous Data Warehouse and Oracle Analytics Cloud to ingest data from multiple flat-file sources and analyze it.  
**Enterprise scale baseline landing zone** | Enterprise scale baseline landing zone developed by OCI  
**ESBLZ workload expansion** | The workload expansion for Enterprise Scale Baseline Landing Zone  
[**Hub-and-Spoke network topology**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=hubandspoke) | Provision a hub-and-spoke network topology in Oracle Cloud Infrastructure  
[**Oracle Cloud development kit**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=oci-dev-tools) For detailed instructions, see [Preinstalling the Oracle Cloud Development Kit](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#top "Provision a compute instance with the Oracle Cloud Development Kit preinstalled and ready to use."). | Provision a Compute instance with Oracle Cloud Infrastructure developer tools already installed  
**Oracle Enterprise Landing Zone V2.0** | Oracle Enterprise Landing Zone V2.0  
[**Sample e-commerce application (MuShop Basic)**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=mushop-basic-stack) | Deploy a sample e-commerce application using Always Free Oracle Cloud resources  
## Service Templates 🔗 
Use a **Service** template to [create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm#top "Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") specific to a single cloud service.
Template (select to launch stack) | Description  
---|---  
**Application Performance Monitoring synthetic dedicated vantage point** | Provision the infrastructure and prerequisites for a synthetic dedicated vantage point in Application Performance Monitoring.  
[**Autonomous Data Warehouse database**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=$%7BMessages.solutionsHub.solutions.autonomousDatawarehouse.solutionName\(\)%7D) | Provision an Autonomous Data Warehouse database  
[**Autonomous Transaction Processing Database**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=atpdb) | Provision an Autonomous Transaction Processing database  
[**Block volume**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=blockvolume) | Provision a block volume in Oracle Cloud Infrastructure  
[**Compute instance**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=computeinstance) | Provision a compute instance in Oracle Cloud Infrastructure  
[**Data Science**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=datascience) | Provision Data Science and its prerequisites  
[**Default VCN**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=defaultvcn) | Provision a VCN that includes a default route table, DHCP options, and subnets  
[**Document**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=$%7BMessages.solutionsHub.solutions.aidocument.solutionName\(\)%7D) | Provision Document and its prerequisites  
[**Resource Manager create private endpoint**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=%24%7BMessages.solutionsHub.solutions.resourcemanagerCreatePrivateEndpoint.solutionName%28%29%7D) | Provision a private endpoint from Resource Manager and use Terraform's remote-exec functionality with a private compute instance. This template prompts you for the compute instance's VCN and private subnet.  
[**Resource Manager get private endpoint**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=%24%7BMessages.solutionsHub.solutions.resourcemanagerGetPrivateEndpoint.solutionName%28%29%7D) | Retrieve an existing private endpoint from Resource Manager and use Terraform's remote-exec functionality with a private compute instance. This template prompts you for the compute instance's availability domain, VCN, and subnet.  
[**Subnets**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=subnets) | Provision subnets in Oracle Cloud Infrastructure  
[**Vision**](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=$%7BMessages.solutionsHub.solutions.aivision.solutionName\(\)%7D) | Provision Vision and its prerequisites  
Was this article helpful?
YesNo

