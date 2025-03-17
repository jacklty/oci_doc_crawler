Updated 2025-03-10
# DRG Metrics
You can monitor the health, capacity, and performance of upgraded dynamic routing gateways (DRGs) by using metrics, alarms, and notifications.
For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
**Note** This feature is only available for upgraded DRGs and not for legacy DRGs.
This topic describes the metrics emitted by the metric namespace `oci_dynamic_routing_gateway`.
Resources: Dynamic routing gateways
## Overview of Metrics: oci_dynamic_routing_gateway 🔗 
A DRG acts as a virtual router, providing a path for traffic between your on-premises networks and VCNs. It can also route traffic between VCNs. Using different types of attachments, you can construct custom network topologies using components in different regions and tenancies. Each DRG attachment has an associated route table to route packets entering the DRG to their next hop. In addition to static routes, optional import route distributions can dynamically import routes from attached networks into the DRG route tables. Refer to [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) for more details.
### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). Refer also to [Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#Authenti).
## Available Metrics: oci_dynamic_routing_gateway 🔗 
Each metric includes one or more of the following dimensions: 
  * `resourceId`: The DRG attachment OCID.
  * `drgOcid`: OCID of the DRG to which the DRG attachment belongs.
  * `drgRouteTableId`: Route table OCID of the DRG attachment.
  * `attachmentType`: DRG attachment type, one of the following:
    * VCN
    * VIRTUAL_CIRCUIT
    * IPSEC_TUNNEL
    * REMOTE_PEERING_CONNECTION
  * `peerRegion`: The peered region for remote peering connection attachments. 
  * `dropType`: One of the following:
    * `throughput`: Count of packet drops from "throughput" exceeding the allocated bandwidth.
    * `noRoute`: Count of packets dropped because a route to the destination could not be found.
    * `others`: Count of packets declared invalid for one of the following reasons: 
    *       * Packet size exceeds MTU
      * Packet TTL expired in transit
      * Packet attempts to traverse OCI from on-premises to on-premises, which is not allowed


Metric Names |  Display Name |  Unit |  Description |  Dimensions  
---|---|---|---|---  
`BytesToDrgAttachment` |  **Bytes sent from DRG** |  Bytes |  The number of bytes sent from the DRG through the DRG attachment. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * peerRegion

  
`BytesFromDrgAttachment` |  **Bytes sent to DRG** |  Bytes |  The number of bytes sent to the DRG from the DRG attachment. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * peerRegion

  
`PacketsToDrgAttachment` |  **Packets sent from DRG** |  Packets |  Number of packets sent from the DRG through the DRG attachment. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * peerRegion

  
`PacketsFromDrgAttachment` |  **Packets sent to DRG** |  Packets |  Number of packets sent from the DRG attachment to the DRG. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * peerRegion

  
`PacketDropsToDrgAttachment` |  **Dropped packets bound for the DRG attachment** |  Packets |  The number of dropped packets bound for the DRG attachment. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * `peerRegion`
  * `dropType`

  
`PacketDropsFromDrgAttachment` |  **Packets from the DRG attachment sent to the DRG then dropped** |  Packets |  The number of packets sent from the DRG attachment and dropped by the DRG. | 
  * `resourceId`
  * `drgOcid`
  * `drgRouteTableId`
  * `attachmentType`
  * `peerRegion`
  * `dropType`

  
## Using the Console 🔗 
[To view default metric charts for all DRGs in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/drgmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In Compartment, select the compartment you're interested in. 
  3. For Metric **Namespace** , select **oci_dynamic_routing_gateway**. 
  4. The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace. 


By default, the charts show a separate line for each resource in the compartment. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

