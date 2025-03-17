Updated 2025-03-10
# Access to Oracle Services: Service Gateway
This topic describes how to set up and manage a service gateway. A service gateway enables cloud resources without public IP addresses to privately access Oracle services.
## Access to Oracle Services 🔗 
The _Oracle Services Network_ is a conceptual network in Oracle Cloud Infrastructure that is reserved for Oracle services. These services have [public IP addresses](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm#osn-ranges) that you typically reach over the internet. However, you can access the Oracle Services Network _without the traffic going over the internet_. There are different ways, depending on which of your hosts need the access:
  * **Hosts in your on-premises network:**
    * [Private access through a VCN with FastConnect private peering or Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services): The on-premises hosts use private IP addresses and reach the Oracle Services Network by way of the VCN and the VCN's service gateway.
    * [Public access with FastConnect public peering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."): The on-premises hosts use public IP addresses.
  * **Hosts in your VCN:**
    * Private access through a service gateway: This is the scenario covered in this topic. The VCN's hosts use private IP addresses. 


## Highlights 🔗 
  * A service gateway lets your Virtual Cloud Network (VCN) privately access specific Oracle services without exposing the data to the public internet. No internet gateway or NAT gateway is required to reach those specific services. The resources in the VCN can be in a private subnet and use only private IP addresses. The traffic from the VCN to the Oracle service travels over the Oracle network fabric and never traverses the internet.
  * The service gateway is regional and enables access only to supported Oracle services _in the same region_ as the VCN. 
  * Only one service gateway is needed for each VCN. All subnets within a VCN have access to the service gateway if the security rules and route table rules allow that access.
  * The service gateway allows access to supported Oracle services within the region to protect your data from the internet. Your workloads may require access to public endpoints or services not supported by the service gateway (for example, to download updates or patches). Ensure you have a [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway) or other access to the internet if necessary.
  * The supported Oracle services are Oracle Cloud Infrastructure Object Storage and others in the Oracle Services Network. For a list, see [Service Gateway: Supported Cloud Services in Oracle Services Network](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/).
  * The service gateway uses the concept of a _service CIDR label_ , which is a string that represents all the regional public IP address ranges for the service or group of services of interest (for example, _OCI PHX Object Storage_ is the string for Object Storage in US West (Phoenix)). You use that service CIDR label when you configure the service gateway and related route rules to control traffic to the service. You can optionally use it when configuring [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). If the service's public IP addresses change in the future, you don't have to adjust those rules.
  * You can set up a VCN so that your on-premises network has _private access_ to Oracle services by way of the VCN and the VCN's service gateway. The hosts in your on-premises network communicate with their private IP addresses and the traffic does not go over the internet. For more information, see [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services)


## Overview of Service Gateways 🔗 
A service gateway lets resources in your VCN privately access specific Oracle services, without exposing the data to an internet gateway or NAT. The resources in the VCN can be in a private subnet and use only private IP addresses. The traffic from the VCN to the service of interest travels over the Oracle network fabric and never traverses the internet.
The following simple diagram illustrates a VCN that has both a **public subnet** and a **private subnet**. Resources in the private subnet have only private IP addresses. 
The VCN shown has three gateways:
  * **Internet gateway:** To provide the public subnet direct access to public endpoints on the internet. Connections can be initiated from the subnet or from the internet. The resources in the public subnet must have public IP addresses. For more information, see [Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway).
  * **Service gateway:** To provide the private subnet with private access to supported Oracle services within the region. Connections can be initiated only from the subnet.
  * **NAT gateway:** To provide the private subnet with private access to public endpoints on the internet. Connections can be initiated only from the subnet. For more information, see [NAT Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway).


You control routing in your VCN at the subnet level, so you can specify which subnets in your VCN use each gateway. In the diagram, the route table for the public subnet (Callout 1) sends non-local traffic through the internet gateway. The route table for the private subnet (Callout 2) sends traffic destined for the Oracle services through the service gateway. It sends all remaining traffic to the NAT gateway.
[![This image shows the basic layout of a VCN with a service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_service_gateway.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_service_gateway.svg)
Callout 1: Public subnet route table Destination CIDR | Route target  
---|---  
0.0.0.0/0 | Internet Gateway  
Callout 2: Private subnet route table Destination CIDR | Route target  
---|---  
OSN services in region | Service Gateway  
0.0.0.0/0 | NAT Gateway   
**Important** See this [known issue](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/known_issues_for_networking.htm#sgw-route-rule-conflict) for information about configuring route rules with _service gateway_ as the target on route tables associated with public subnets.
A service gateway can be used by resources in the gateway's own VCN. However, if the VCN is [peered with another](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering), resources in the other VCN cannot access the service gateway unless a service gateway is configured in both VCNs. You could configure traffic destined for Oracle Services Network that originates on a spoke to travel through a network virtual appliance (NVA) in the hub and then through the hub's service gateway. See [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route) and [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services) for more information. 
Resources in your on-premises network that is connected to the service gateway's VCN with [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") can also use the service gateway. For more information, see [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services). 
Notice that your on-premises network can _also_ use [FastConnect public peering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#uses) for private access to public Oracle services. That means that your on-premises network could have multiple paths to access Oracle services public IP address ranges. If that is the case, your edge device receives route advertisement of the Oracle services public IP address ranges over multiple paths. For important information about configuring your edge device correctly, see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network).
Only one service gateway is needed for each VCN. All subnets within a VCN have access to the service gateway if the security rules and route table rules allow that access.
For instructions on setting up a service gateway, see [Setting Up a Service Gateway in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#setting_up_sgw). 
### About Service CIDR Labels 🔗 
Each Oracle service has a regional public endpoint that uses public IP addresses for access. When you set up a service gateway with access to an Oracle service, you also set up Networking service [route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and optionally [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that control traffic with the service. That would normally mean you need to know the service's public IP addresses to set up those rules. To make it easier for you, the Networking service uses _service CIDR labels_ as an alias representing all the public CIDRs for a given Oracle service or a group of Oracle services. If a service's CIDRs change in the future, you don't have to adjust your route rules or security rules.
Examples:
  * **OCI PHX Object Storage** is a service CIDR label that represents all the Object Storage CIDRs in the US West (Phoenix) region. 
  * **All PHX Services in Oracle Services Network** is a service CIDR label that represents all the CIDRs for the supported services in the Oracle Services Network in the US West (Phoenix) region. For a list of the services, see [Service Gateway: Supported Cloud Services in Oracle Services Network](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/). 


As you can see, a service CIDR label can be associated with either a single Oracle service (example: Object Storage), or multiple Oracle services. Once you have assigned a service CIDR label to a service gateway, the Console will allow you to switch to the other label, but the service gateway must always have a service CIDR label. The API and CLI will allow you to remove the service CIDR label completely.
The term _service_ is often used in this topic in place of the more accurate term _service CIDR label_. The important thing to remember is that when you set up a service gateway (and related route rules), you specify the _service CIDR label_ you're interested in. In the Console, you're presented with the available service CIDR labels. If you use the REST API, the [ListServices](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Service/ListServices) operation returns the available `Service` objects. The `Service` object's `cidrBlock` attribute contains the service CIDR label (example: `all-phx-services-in-oracle-services-network`).
### Available Service CIDR Labels 🔗 
Here are the available service CIDR labels:
  * **OCI <region> Object Storage:** For information about the service, see [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)
  * **All <region> Services in Oracle Services Network:** For a list of supported services, see [Service Gateway: Supported Cloud Services in Oracle Services Network](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/). 


**Important** See this [known issue](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/known_issues_for_networking.htm#sgw-image-yum) for information about accessing Oracle YUM services through the service gateway.
### Enabling a Service CIDR Label for a Service Gateway
To give your VCN access to a given service CIDR label, you must _enable_ that service CIDR label for the VCN's service gateway. You can do that when you create the service gateway, or later after it's created. You can also disable a service CIDR label for the service gateway at any time.
**Important**
Because Object Storage is covered by both **OCI <region> Object Storage** and **All <region> Services in Oracle Services Network**, a service gateway can use **only one of those service CIDR labels**. Likewise, a route table can have a single rule for one of the service CIDR labels. It cannot have two separate rules, one for each label.
If the service gateway is configured to use **All <region> Services in Oracle Services Network**, the route rule can use either CIDR label. However, if the service gateway is configured to use **OCI <region> Object Storage** and the route rule uses **All <region> Services in Oracle Services Network**, traffic to services in the Oracle Services Network except Object Storage will be blackholed. The Console prohibits you from configuring the service gateway and corresponding route table in that manner.
If you want to switch the service gateway to use a different service CIDR label, see [When You Switch to a Different Service CIDR Label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/service-gateway_management.htm#switch_label).
### Blocking Traffic Through a Service Gateway
You create a service gateway in the context of a specific VCN. In other words, the service gateway is always attached to that one VCN. However, you can block or allow traffic through the service gateway at any time. By default, the gateway allows traffic flow upon creation. Blocking the service gateway traffic prevents all traffic from flowing, regardless of what service CIDR labels are enabled, or any existing route rules or security rules in your VCN. For instructions on how to block traffic, see [Controlling Traffic for a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#sgw-traffic "You can block or allow traffic for a service gateway in a virtual cloud network \(VCN\).").
### Route Rules and Security Rules for a Service Gateway
For traffic to be routed from a subnet in your VCN to a service gateway, you must add a rule accordingly to the subnet's route table. The rule must use the service gateway as the target. For the destination, you must use the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that is enabled for the service gateway. This means that you don't have to know the specific public CIDRs, which could change over time.
Any traffic leaving the subnet and destined for the service's public CIDRs is then routed to the service gateway. If the service gateway traffic is blocked, no traffic flows through it even if there's a route rule that matches the traffic. For instructions on setting up route rules for a service gateway, see [Task 2: Update routing for the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_routing). 
The VCN's security rules must also allow the desired traffic. If you like, you can use a service CIDR label instead of a CIDR for the source or destination of the desired traffic. Again, this means that you don't have to know the specific public CIDRs for the service. For convenience, you can use a service CIDR label in security rules even if your VCN doesn't have a service gateway, and the traffic to the services uses an internet gateway.
You can use [stateful or stateless security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful) that use a service CIDR label:
  * **For stateful rules:** Create an egress rule with the destination service = the service CIDR label of interest. As with any security rule, you can specify other items such as the IP protocol and source and destination ports. 
  * **For stateless rules:** You must have both egress and ingress rules. Create an egress rule with the destination service = the service CIDR label of interest. Also create an ingress rule with the source service = the service CIDR label of interest. As with any security rule, you can specify other items such as the IP protocol and source and destination ports. 


For instructions on setting up security rules that use a service CIDR label, see [Task 3: (Optional) Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_security_list).
### Object Storage: Allowing Bucket Access from Only a Particular VCN or CIDR Range
If you use a service gateway to access Object Storage, you can write an IAM policy that allows access to a particular Object Storage bucket only if these requirements are met:
  * The request goes through a service gateway.
  * The request originates from the particular VCN that is specified in the policy.


For examples of this particular type of IAM policy, and important caveats about its use, see [Task 4: (Optional) Update IAM Policies to Restrict Object Storage Bucket Access](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_iam_policy).
Alternatively, you can use IAM IP-based filtering to restrict access to an IP address or ranges of addresses. For more information, see [Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).
### Deleting a Service Gateway
To delete a service gateway, its traffic does not have to be blocked, but there must not be a route table that lists it as a target. See [Deleting a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm#delete-sgw "Delete a service gateway in a Virtual Cloud Network \(VCN\) to remove access to the Oracle Services Network \(OSN\).").
### Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Setting Up a Service Gateway in the Console 🔗 
See the instructions in [Creating a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#create-sgw "Create a service gateway in a Virtual Cloud Network \(VCN\) to allow access to the Oracle Services Network \(OSN\)."). 
[Task 1: Create the service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm)
See the instructions in [Creating a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#create-sgw "Create a service gateway in a Virtual Cloud Network \(VCN\) to allow access to the Oracle Services Network \(OSN\)."). 
[Task 2: Update routing for the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm)
When you configure a service gateway for a particular service CIDR label, you must also create a route rule that specifies that label as the destination and the target as the service gateway. You do this for each subnet that needs to access the gateway.
  1. Determine which subnets in your VCN need access to the service gateway. 
  2. For each of those subnets, [update the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") to include a new rule using the following values: 
     * **Target Type:** Service Gateway.
     * **Destination Service:** The [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that is enabled for the gateway.
     * **Compartment:** The compartment where the service gateway is located.
     * **Target:** The service gateway.
     * **Description:** An optional description of the rule.


Any subnet traffic with a destination that matches the rule is routed to the service gateway. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
Later, if you no longer need the service gateway and want to delete it, you must first delete all the route rules in your VCN that specify the service gateway as the target.
**Tip**
Without the required routing, traffic doesn't flow over the service gateway. If a situation occurs where you want to temporarily stop the traffic flow over the gateway to a particular service, you can simply remove the route rule that enables traffic. You can also disable that particular service CIDR label for the gateway. Or you can [block all traffic through the service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#sgw-traffic "You can block or allow traffic for a service gateway in a virtual cloud network \(VCN\).") entirely. You do not have to delete the gateway.
[Task 3: (Optional) Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm)
When you configure a service gateway to access a service CIDR label, you must also ensure that the security rules are configured to allow the desired traffic. Your security rules might already allow this traffic, which is why this task is optional. The following procedure assumes you are using security lists to implement your security rules. The procedure describes how to set up a rule that uses the service CIDR label. You do this for each subnet that needs to access the gateway. 
**Tip** Security lists are one way to control traffic in and out of the VCN's resources. You can also use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)
  1. Determine which subnets in your VCN need to connect to the services you're interested in.
  2. [Update the security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#update-securitylist "Update the rules used in a security list in a Virtual Cloud Network \(VCN\).") for each of those subnets to include rules to allow the desired egress or ingress traffic with the particular service. 
Let's say you want to add a stateful rule that enables egress HTTPS (TCP port 443) traffic from the subnet to both Object Storage and Oracle YUM repos. Here are the basic options to choose when adding a rule: 
    1. In the **Allow Rules for Egress** section, click **+Add Rule**.
    2. Leave the **Stateless** checkbox unselected.
    3. **Destination Type:** Service.
    4. **Destination Service:** The [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in. To access both Object Storage and Oracle YUM repos, choose **All <region> Services in Oracle Services Network**.
    5. **IP Protocol:** Leave as **TCP**. 
    6. **Source Port Range:** Leave as **All**.
    7. **Destination Port Range** : Enter 443.
    8. **Description:** An optional description of the rule.


For more information about setting up security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
[Task 4: (Optional) Update IAM Policies to Restrict Object Storage Bucket Access](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm)
This task is applicable only if you're using a service gateway to access Object Storage. You can optionally create a network source and write an IAM policy to allow only the resources in a specific VCN to write objects to a particular bucket. 
**Important**
If you use one of the following IAM policies to restrict access to a bucket, the bucket is _not accessible from the Console_. It's accessible only from within the specific VCN. 
Also, the IAM policies allow requests to Object Storage only if they go from the specified VCN _through the service gateway_. If they go through the internet gateway, the requests are denied. 
  * Create a network source to specify the allowed VCN. For information on creating network sources, see [Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).
  * Create the policy. The following example lets resources in the example ObjectBackup group write objects to an existing bucket called db-backup that resides in a compartment called ABC. 
Copy
```
Allow group ObjectBackup to read buckets in compartment ABC
Allow group ObjectBackup to manage objects in compartment ABC where
  all {target.bucket.name='db-backup', 
    request.networkSource.name='<VCN_NETWORK_SOURCE',
    any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}}
```



You can specify multiple VCNs by creating and specifying multiple network sources in the policy. The next example has network sources for two VCNs. You might do this if you've [set up your on-premises network with private access to Oracle services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services) through a VCN, and you've also set up one or more _other_ VCNs with their own service gateways. For more information, see [Overview of On-Premises Network Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#private-access-overview). 
Copy
```
Allow group ObjectBackup to read buckets in compartment ABC
Allow group ObjectBackup to manage objects in compartment ABC where
  all {target.bucket.name='db-backup', 
    any {request.networkSource.name='<NETWORK_SOURCE_FOR_VCN_1>', request.networkSource.name='<NETWORK_SOURCE_FOR_VCN_2'},
    any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}}
```

Was this article helpful?
YesNo

