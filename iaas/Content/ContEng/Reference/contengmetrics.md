Updated 2025-01-15
# Kubernetes Engine (OKE) Metrics
_Find out about the metrics emitted by Kubernetes Engine (OKE)._
You can monitor the health, capacity, and performance of Kubernetes clusters managed by Kubernetes Engine using **metrics** , **alarms** , and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by Kubernetes Engine in the `oci_oke` metric namespace.
Resources: clusters, worker nodes
## Overview of the Kubernetes Engine (OKE) Service Metrics 🔗 
Kubernetes Engine metrics help you monitor Kubernetes clusters, along with node pools and individual worker nodes. You can use metrics data to diagnose and troubleshoot cluster and node pool issues.
While frequency varies by metric, default service metrics typically have a frequency of 60 seconds (that is, at least one data point posted per minute).
To view a default set of metrics charts in the Console, navigate to the cluster you're interested in, and then click **Metrics**. You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
## Prerequisites 🔗 
IAM policies: To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
For example, to observe the condition of nodes in a Kubernetes cluster, you must have been granted access using a policy statement similar to the following:
Copy
```
Allow group <group-name> to read metrics in <location>
```

## Available Metrics: oci_oke 🔗 
The metrics listed in the following tables are automatically available for any Kubernetes clusters you create. You do not need to enable monitoring on the resource to get these metrics.
Kubernetes Engine metrics include the following dimensions: 

RESOURCEID
    The **OCID** of the resource to which the metric applies. 

RESOURCEDISPLAYNAME
    The name of the resource to which the metric applies. 

RESPONSECODE
     The response code sent from the Kubernetes API server. 

RESPONSEGROUP
    The response code group, based on the response code's first digit (for example, 2xx, 3xx, 4xx, 5xx). 

CLUSTERID
    The **OCID** of the cluster to which the metric applies. 

NODEPOOLID
    The **OCID** of the node pool to which the metric applies. 

NODESTATE
    The state of the compute instance hosting the worker node. For example, ACTIVE, CREATING, DELETING, DELETED, FAILED, UPDATING, INACTIVE. 

NODECONDITION
    The condition of the worker node, as indicated by the Kubernetes API server. For example, Ready, MemoryPressure, PIDPressure, DiskPressure, NetworkUnavailable. 

AVAILABILITYDOMAIN
    The availability domain where the compute instance resides. 

FAULTDOMAIN
    The fault domain where the compute instance resides.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`APIServerRequestCount` | **API Server Requests** | count | Number of requests received by the Kubernetes API Server. |  `resourceId` `resourceDisplayName`  
`APIServerResponseCount` | **API Server Response Count** | count | Number of different non-200 responses (that is, error responses) sent from the Kubernetes API server. | `resourceId` `resourceDisplayName` `responseCode` `responseGroup`  
`UnschedulablePods` | **Unschedulable Pods** | count | Number of pods that the Kubernetes scheduler is unable to schedule. Not available in clusters running versions of Kubernetes prior to version 1.15.x. | `resourceId` `resourceDisplayName`  
`NodeState` | **Node State** | count | Number of compute nodes in different states.  | `resourceId` `clusterId` `nodepoolId` `resourceDisplayName` `nodeState` `nodeCondition``availabilityDomain``faultDomain`  
`KubernetesNodeCondition` | **Kubernetes Node Condition** | count |  Number of worker nodes in different conditions, as indicated by the Kubernetes API server. | `resourceId` `clusterId` `nodepoolId` `resourceDisplayName` `nodeCondition`  
## Using the Console 🔗 
[To view default metric charts for a single cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm)
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Select the region you are using with Kubernetes Engine.
  3. Select the compartment containing the cluster for which you want to view metrics. 
The **Clusters** page shows all the clusters in the compartment you selected.
  4. Click the name of the cluster for which you want to view metrics.
  5. Under **Resources** , click **Metrics**. 
The **Metrics** tab displays a chart for each metric for the cluster that is emitted by the Kubernetes Engine metric namespace. To see metrics for a node pool in the cluster, display the **Node Pools** tab, click the name of the node pool, and display the **Metrics** tab. To see metrics for a worker node in the node pool, display the**Nodes** tab and click the **View Metrics** link beside the name of the worker node. For more information about the emitted metrics, see [Available Metrics: oci_oke](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#availablemetrics).
For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).


[Not seeing the cluster metrics data you expect?](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm)
If you don't see the metrics data for a cluster that you expect, see the following possible causes and resolutions. 
Problem | Possible Cause | How to check | Resolution  
---|---|---|---  
I know the Kubernetes API server returned some error responses but the **API Server Response Count** chart doesn't show them. | The responses might have been returned outside the time period covered by the **API Server Response Count** chart. | Confirm the **Start Time** and **End Time** cover the period when the responses were returned. | Adjust the **Start Time** and **End Time** as necessary.  
I know the Kubernetes API server returned some error responses but the **API Server Response Count** chart doesn't show them, even though the responses were returned between the **Start Time** and **End Time**. | Although the responses were returned between the **Start Time** and **End Time** , the **x-axis (window of data display)** might be excluding the responses. | Confirm the **x-axis (window of data display)** covers the period when the responses were returned. | Adjust the **x-axis (window of data display)** as necessary.  
I want to see data in the charts as a continuous line over time, but the line has gaps in it.  | This is expected behavior. If there is no metrics data to show in the selected interval, the data line is discontinuous.  | Increase the **Interval** (for example, from 1 minute to 5 minutes, or from 1 minute to 1 hour). | Adjust the **Interval** as necessary.  
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

