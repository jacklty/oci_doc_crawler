Updated 2025-03-10
# Site-to-Site VPN Metrics
You can monitor the health, capacity, and performance of your [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace `oci_vpn`.
Resources: IPSec connections.
## Overview of Metrics: oci_vpn 🔗 
The available metrics help you determine quickly if your [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") is up, how much data is flowing over the connection, and if packets are being dropped for unexpected errors.
Site-to-Site VPN includes these resources:
  * An IPSec connection, which you can think of as the _parent resource_ (identified by `parentResourceId` in the following discussion).
  * One or more individual tunnels associated with that IPSec connection (each identified by the tunnel's `publicIp` in the following discussion).


### Required IAM Policy
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_vpn 🔗 
The metrics listed in the following table are automatically available for any Site-to-Site VPN that you create. You do not need to enable monitoring on the resource to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following dimensions:  

PARENTRESOURCEID
    The **OCID** of the IPSec connection (the parent resource). The connection has multiple individual tunnels. 

PUBLICIP
    Although each tunnel has its own **OCID** , it can be easier to use the `publicIp` dimension to identify a specific IPSec tunnel in the connection. The value is the public IP address of the Oracle end of the tunnel (also known as the _Oracle VPN headend_). 
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`TunnelState` |  **IPSec Tunnel State** |  Binary (1 or 0) |  Whether the tunnel is up (1) or down (0). |  `parentResourceId ` `publicIp`  
`PacketsReceived` |  **Packets Received** |  Packets |  Number of packets received at the Oracle end of the connection.  
`BytesReceived` |  **Bytes Received** |  Bytes |  Number of bytes received at the Oracle end of the connection.  
`PacketsSent` |  **Packets Sent** |  Packets |  Number of packets sent from the Oracle end of the connection.  
`BytesSent` |  **Bytes Sent** |  Bytes |  Number of bytes sent from the Oracle end of the connection.  
`PacketsError` |  **Packets with Errors** |  Packets |  Number of packets dropped at the Oracle end of the connection. Dropped packets indicate a misconfiguration in some part of the overall system. Check if there's been a change to the configuration of your VCN, Site-to-Site VPN, or your CPE.   
## Using the Console 🔗 
[To view default metrics charts for an individual tunnel in an IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click the IPSec connection to view its details.
  3. Click the tunnel you're interested in to view its details and default metrics charts.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view default metric charts for all IPSec connections in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. For **Compartment** , select the compartment that contains the IPSec connection you're interested in. 
  3. For **Metric namespace** , select **oci_vpn**.
The **Service Metrics** page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace. 


Each IPSec tunnel is a single line in a given chart. The tunnel is identified in the chart by the public IP address of the Oracle end of the tunnel.
For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

