Updated 2024-08-28
# Private Access
This topic gives an overview of the options for enabling private access to services within Oracle Cloud Infrastructure. _Private access_ means that traffic does not go over the internet. Access can be from hosts within your virtual cloud network (VCN) or your on-premises network.
**Tip** This topic does not discuss access to services through an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway). However, remember that traffic through an internet gateway between a VCN and a public IP address _that is part of Oracle Cloud Infrastructure_ is routed without being sent over the internet.
## Highlights 🔗 
  * You can enable private access to certain services within Oracle Cloud Infrastructure from your VCN or on-premises network by using either a _private endpoint_ or a _service gateway_. See the sections that follow.
  * For each private access option, these services or resource types are available:
    * **With a private endpoint:**
      * [Anomaly Detection](https://docs.oracle.com/iaas/Content/anomaly/using/overview.htm)
      * [Autonomous Database Serverless](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/private-endpoints-autonomous.html#GUID-60FE6BFD-B05C-4C97-8B4A-83285F31D575)
      * [Bastion](https://docs.oracle.com/en/solutions/use-bastion-service/index.html#GUID-1B455658-0988-42C4-A52F-4757A3201232)
      * [Data Catalog](https://docs.oracle.com/iaas/releasenotes/changes/7e3d5557-784d-4c9e-9ccd-b9512dd37c1d/)
      * [Data Flow](https://docs.oracle.com/iaas/data-flow/using/dfs_data_flow.htm)
      * [Data Safe](https://docs.oracle.com/en/cloud/paas/data-safe/admds/connectivity-options-target-databases.html)
      * [Data Science](https://docs.oracle.com/iaas/data-science/using/overview.htm)
      * [Database Management](https://docs.oracle.com/iaas/database-management/doc/create-database-management-private-endpoint.html)
      * [Database Tools](https://docs.oracle.com/iaas/database-tools/index.html)
      * [DevOps](https://docs.oracle.com/iaas/Content/devops/using/create_oke_environment.htm)
      * [Language](https://docs.oracle.com/iaas/language/using/overview.htm)
      * [Oracle Analytics Cloud](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoci/manage-service-access-and-security.html#GUID-0987CA3C-B435-41EC-B4EB-49B11C346897)
      * [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)
      * [Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)
      * [Streaming](https://docs.oracle.com/iaas/Content/Security/Reference/streaming_security.htm#securing_service_name)
      * [Oracle Digital Assistant](https://docs.oracle.com/en/cloud/paas/digital-assistant/use-chatbot/service-administration1.html#GUID-5042E5CE-6105-4C00-B4C6-BDFC632942E7)
    * **With a service gateway:** [Available services](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/)
  * With either private access option, the traffic stays within the Oracle Cloud Infrastructure network and does not traverse the internet. However, if you use a service gateway, requests to the service use a public endpoint for the service.
  * If you do not want to access a given Oracle service through a public endpoint, Oracle recommends using a private endpoint in your VCN (assuming the service supports private endpoints). A private endpoint is represented as a private IP address within a subnet in your VCN.


## About Private Endpoints 🔗 
A private endpoint is a private IP address within your VCN that you can use to access a given service within Oracle Cloud Infrastructure. The service sets up the private endpoint in a subnet of your choice within the VCN. You can think of the private endpoint as just another **VNIC** in your VCN. You can control access to it like you would for any other VNIC: by using [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). However, the service sets up this VNIC and maintains its availability on your behalf. You only need to maintain the subnet and the security rules.
The following diagram illustrates the concept.
[![This diagram shows a VCN with a private endpoint for a resource.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_private_access_pe.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_private_access_pe.svg)
The private endpoint gives hosts within your VCN and your on-premises network access to a _single resource_ within the Oracle service of interest (for example, one database in Autonomous Database Serverless). Compare that private access model with a service gateway (see the next section): If you created five Autonomous Databases for a given VCN, all five would be accessible through a single service gateway by sending requests to a public endpoint for the service. However, with the private endpoint model, there would be five separate private endpoints: one for each Autonomous Database, and each with its own private IP address.
**Note** The service that sets up the private endpoint in your VCN might provide you a DNS name (fully qualified domain name, or FQDN) for the private endpoint, and not the private IP address itself. If you've configured your network setup for DNS, your hosts can access the private endpoint by using the FQDN. If the service supports the use of [network security groups (NSGs)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) with its resources, you can request that the service set up the private endpoint in an NSG of your choice within your VCN. NSGs let you write [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control access to the private endpoint without knowing the private IP address assigned to the private endpoint.
If you have a private endpoint for a resource, hosts within the VCN can use the private endpoint's FQDN or private IP address to access the resource. You set up [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control access between hosts in the VCN and the private endpoint. For an example of how to do this with Autonomous Database for Analytics and Data Warehousing, see [Configuring Network Access with Private Endpoints](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/private-endpoints-autonomous.html#GUID-60FE6BFD-B05C-4C97-8B4A-83285F31D575).
You can also set up [transit routing with your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) so that hosts in the on-premises network can use the private endpoint. To enable on-premises hosts to use the private endpoint's FQDN instead of its private IP address, you have two options:
  * Set up an instance in the VCN to be a custom DNS server. For an example of an implementation of this scenario with the Oracle Terraform provider, see [Hybrid DNS Configuration](https://github.com/oracle/terraform-provider-oci/blob/255817f83956f1f9a3ab903e11465e8b4dde1957/docs/examples/networking/hybrid_dns/Hybrid-DNS-configuration-using-DNS-VM-in-VCN.md).
  * Manage hostname resolution yourself manually.


You might have multiple VCNs with hosts that need access to the specific resource of interest. You can [peer the VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) so that hosts in the other VCNs can also use the private endpoint (the preceding diagram does not show any peered VCNs).
## About Service Gateways 🔗 
A [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway) gives resources in your VCN and on-premises network private access to _multiple_ services within Oracle Cloud Infrastructure, without the traffic going over the internet.
The following diagram illustrates the concept. The diagram refers to the _Oracle Services Network_ , which is a conceptual network in Oracle Cloud Infrastructure that is reserved for Oracle services.
[![This diagram shows a VCN with a service gateway for access to the Oracle Services Network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_private_access_service_gateway.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_private_access_service_gateway.svg)
To use a service gateway from a particular subnet within your VCN, you set up a route rule in the subnet's [route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2), and specify the service gateway as the target of the rule. You also set up [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control access between hosts in the VCN and the services available through the service gateway. 
If you have more than one VCN in your tenancy, you can configure each with its own service gateway. 
See [Gateway Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#gateway_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for more limits-related information.
You can also set up [transit routing for the Oracle Services Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services) so that hosts in your on-premises network can use a VCN's service gateway.
Was this article helpful?
YesNo

