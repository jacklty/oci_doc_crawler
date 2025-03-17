Updated 2025-03-10
# Service Gateway Metrics
You can monitor the health, capacity, and performance of your service gateways by using metrics, alarms, and notifications. 
For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace ` oci_service_gateway`.
Resources: Service gateways
## Overview of Metrics: oci_service_gateway 🔗 
A service gateway is used to enable on-premises hosts or VCN hosts to privately access Oracle services (such as Object Storage and Autonomous Database) without exposing the resources to the public internet. 
The available metrics help you determine quickly if your service gateway is up, how much data is flowing through the gateway, and if packets are being dropped for unexpected errors. 
  * **Traffic to and from the service gateway:** Per-gateway traffic levels (packets and bytes), which can help you identify meaningful increases or decreases in traffic coming in and out of the gateway. 
  * **Packets dropped:** Per-gateway drops (dropped packets), which can help you identify changes in traffic caused by issues such as gateway misconfiguration or unrecognized packet protocol. 


### Required IAM Policy
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
## Available Metrics: oci_service_gateway 🔗 
The metrics listed in the following table are automatically available for each service gateway that you create. You do not need to enable monitoring to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes one or more of the following dimensions:  

RESOURCEID
    The **OCID** of the service gateway.  

DROPTYPE
    The type of packet drop:     
  * `sgwDisabledDrops`: Packets dropped because the service gateway is disabled.
  * `sgwMtuExceededDrops`: Packets dropped because the [Maximum Transmission Unit (MTU) has been exceeded. ](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Overview)
  * `sgwServiceDestUnknown`: Packets dropped because of an unknown or incorrect service destination. 
  * `sgwTtlExpiryDrops`: Packets dropped because the [TTL (Time To Live)](https://en.wikipedia.org/wiki/Time_to_live) value in the IPv4 header of the packet has expired. 
  * `sgwMisconfigurationDrops`: Packets dropped because the gateway service moniker is misconfigured. For example, the gateway's associated route table points to a different CIDR service than the one specified in the gateway configuration. 
  * `sgwUnknownProtocolDrops`: Packets dropped because the protocol in the IPv4 header of the packet is not recognized. 


Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`packetsToService` |  **Packets to Service** |  Packets |  The number of packets successfully sent from the service gateway toward Oracle services.  | `resourceId`  
`packetsFromService` |  **Packets from Service** |  Packets |  The number of packets successfully sent from the service gateway toward customer instances.   
`bytesToService` |  **Bytes to Service** |  Bytes |  The number of bytes successfully sent from the service gateway toward Oracle services.   
`bytesFromService` |  **Bytes from Service** |  Bytes |  The number of bytes successfully sent from the service gateway toward customer instances.   
`sgwDropsFromService` |  **Packet Drops from Service** |  Packets |  The number of packets dropped while sending packets from the service gateway toward customer instances.  
`sgwDropsToService ` |  **Packet Drops to Service** |  Packets |  The number of packets dropped while sending packets from the service gateway toward Oracle services.  |  `resourceId` `dropType`  
## Using the Console 🔗 
[To view default metric charts for all service gateways in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/SGWmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In Compartment, select the compartment you're interested in. 
  3. For Metric **Namespace** , select **oci_service_gateway**. 
  4. The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace. 


By default, the charts show a separate line for each resource in the compartment. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

