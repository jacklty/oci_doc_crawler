Updated 2025-02-12
# **Internet Gateway Metrics**
You can monitor the health, capacity, and performance of your internet gateways by using metrics, alarms, and notifications.
For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
This topic describes the metrics emitted by the metric namespace oci_internet_gateway.
Resources: [Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway)
## Overview of Metrics: oci_internet_gateway 🔗 
An internet gateway as an optional virtual router that connects the edge of the VCN with the internet. To use the gateway, the hosts on both ends of the connection must have public IP addresses for routing. Connections that originate in your VCN and are destined for a public IP address (either inside or outside the VCN) go through the internet gateway. Connections that originate outside the VCN and are destined for a public IP address inside the VCN go through the Internet gateway.
### Required IAM Policy
To monitor resources, you must be given the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you've been granted and which **compartment** you should work in. For more information on user authorizations for monitoring, see the Authentication and Authorization section for the related service: [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Authenti) or [Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#Authenti). 
## Available Metrics: internet_gateway 🔗 
The metrics listed in the following table are automatically available for each service gateway that you create. You don't need to enable monitoring to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm). 

RESOURCEID
    The **OCID** of the internet gateway.  

DROPTYPE
    The type of packet drop:     
  * `securityRule`: Count of packet drops because of a security rule configured in the VN component.
  * `noRoute`: Count of packet drops because of a non routable destination. 
  * `throughput`: Count of packet drops because of "throughput" exceeding the allocated bandwidth. 
  * `others`: Count of packets declared invalid for one of the following reasons:
    * Packet size exceeds MTU
    * Packet TTL expired in transit
    * Invalid IP checksum


Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`BytesToIgw` | **Bytes from VCN to Internet Gateway** | Bytes | Bytes sent from VCN (to which Internet Gateway is attached) to Internet Gateway | resourceId  
`**BytesFromIgw**`| **Bytes from Internet Gateway to VCN** | Bytes | Bytes sent from Internet Gateway to VCN (to which Internet Gateway is attached)  
`**PacketsToIgw**`| **Packets from VCN to Internet Gateway** | Packets | Packets sent from VCN (to which Internet Gateway is attached) to Internet Gateway  
`PacketsFromIgw` | **Packet from Internet Gateway to VCN** | Packets | Packets sent from Internet Gateway to VCN (to which Internet Gateway is attached)  
`PacketDropsToIgw` | **Packet drops from VCN to Internet Gateway** | Packets | Packets from VCN (to which Internet Gateway is attached) to Internet Gateway that were dropped by Internet Gateway |  resourceId dropType  
`PacketDropsFromIgw` | **Packet drops from Internet Gateway to VCN** | Packets | Packets from Internet Gateway to VCN (to which Internet Gateway is attached) that were dropped by Internet Gateway  
## Using the Console 🔗 
### To view default metric charts for all internet gateways in a compartment 🔗 
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In Compartment, select the compartment you're interested in. 
  3. For Metric **Namespace** , select **oci_internet_gateway**. 
  4. The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace. 
By default, the charts show a separate line for each resource in the compartment. 


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

