Updated 2025-03-10
# NAT Gateway Metrics
You can monitor the health, capacity, and performance of your NAT gateways by using metrics, alarms, and notifications.
For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace `oci_nat_gateway`.
Resources: NAT gateways
## Overview of Metrics: oci_nat_gateway 🔗 
A NAT gateway is used to give an entire private network access to the internet without assigning each host a public IPv4 address. The hosts can initiate connections to the internet and receive responses, but not receive inbound connections initiated from the internet. 
The available metrics help you determine quickly if your NAT gateway is up, how much data is flowing through the gateway, and if packets are being dropped for unexpected errors. 
  * **Traffic to and from the NAT gateway:** Per-gateway traffic levels (packets and bytes), which can help you identify meaningful increases or decreases in traffic coming in and out of the gateway.
  * **Packets dropped:** Per-gateway drops (dropped packets), which can help you identify changes in traffic caused by issues such as NAT port exhaustion.


### Required IAM Policy
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_nat_gateway 🔗 
The metrics listed in the following table are automatically available for each NAT gateway that you create. You do not need to enable monitoring to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes one or more of the following dimensions:  

RESOURCEID
    The **OCID** of the NAT gateway.  

DROPTYPE
    The type of packet drop:     
  * `noPorts`: Packets dropped due to NAT port exhaustion.
  * `throttle`: Packets dropped due to throttling at NAT gateway.
  * `other`: Packets invalid for one of the following reasons: 
    * Packet TCP data indicates a TCP connection that is already closed 
    * Packet TCP data indicates the connection was not previously established
    * Packet size exceeds MTU
    * Packet destination is unreachable


Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`BytesToNATgw` |  **Bytes from OCI resources to NAT gateway** |  Bytes |  Number of bytes sent from Oracle Cloud Infrastructure (OCI) resources to NAT gateway. | `resourceId`  
`BytesFromNATgw` |  **Bytes from NAT gateway to OCI resources** |  Bytes |  Number of bytes sent from NAT gateway to OCI resources.  
`PacketsToNATgw` |  **Packets from OCI resources to NAT gateway** |  Packets |  Number of packets sent from OCI resources to NAT gateway.  
`PacketsFromNATgw` |  **Packets from NAT gateway to OCI resources** |  Packets | Number of packets sent from NAT gateway to OCI resources.  
`DropsToNATgw ` |  **Packet Drops from OCI resource to NAT gateway** |  Packets | Number of packets from OCI resources to NAT Gateway that were dropped by NAT Gateway. |  `resourceId` `dropType`  
ConnectionsEstablished | **Connections established via NAT gateway** | Number | Number of connections established via NAT gateway  
ConnectionsClosed | **Connections via NAT gateway that were closed by far ends** | Number | Number of connections via NAT gateway that were closed by the internet host  
ConnectionsTimedOut | **Connections closed by NAT gateway due to idle time out** | Number | Number of connections closed by NAT gateway due to idle time out  
## Using the Console 🔗 
[To view default metric charts for all NAT gateways in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/nat-gateway-metrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In Compartment, select the compartment you're interested in. 
  3. For Metric **Namespace** , select **oci_nat_gateway**. 
  4. The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace. 


By default, the charts show a separate line for each resource in the compartment. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

