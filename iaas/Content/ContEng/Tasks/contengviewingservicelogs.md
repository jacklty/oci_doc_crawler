Updated 2025-01-15
# Viewing Kubernetes Engine (OKE) Service Logs
_Find out how to view the logs of Kubernetes processes (such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver) running on the control plane of clusters you've created using Kubernetes Engine (OKE)._
Having created a cluster using Kubernetes Engine, you can use Oracle Cloud Infrastructure Logging to view and search the logs of Kubernetes processes running on the cluster's control plane. The Kubernetes control plane process logs are available in Oracle Cloud Infrastructure Logging as logs for the Kubernetes Engine service, where they are referred to as service logs.
The following Kubernetes control plane process logs are available for Kubernetes Engine as service logs:
  * The kube-scheduler log, containing errors and events within the kube-scheduler process (such as scheduler decisions).
  * The kube-controller-manager log, containing errors and events within the kube-controller-manager process (such as reconciling the deployment).
  * The cloud-controller-manager log, containing errors and events within the cloud-controller-manager process (such as provisioning the load balancer).
  * The kube-apiserver log, containing errors and events within the kube-apiserver process (for every request sent to the Kubernetes API server).


The service logs are configured at the default Kubernetes log level verbosity (`v=2`). At this level, the service logs contain useful steady state information about the service, and important log messages that might correlate to significant changes in the system.
You'll find the service logs useful when troubleshooting cluster issues such as:
  * Cluster control plane virtual machine(s) shutdowns.
  * Network partitioning issues within a cluster, or between the cluster and users.
  * Kubernetes software crashes.
  * Data loss or unavailability of persistent storage.
  * Operator errors, such as misconfigured Kubernetes or application software.


Having enabled and configured service logs, you can subsequently view the service logs. 
For more information about service logs, see [Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm).
Note that in addition to viewing the Kubernetes Engine service logs, you can also:
  * Monitor the overall status of the cluster itself, node pools, and nodes. See [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
  * View log events in the Oracle Cloud Infrastructure Audit. See [Viewing Kubernetes API Server Audit Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringoke.htm#Monitoring_Container_Engine_for_Kubernetes_and_the_Kubernetes_API_Server "Find out how to view operations of both Kubernetes Engine \(OKE\) and the Kubernetes API server as log events in the Oracle Cloud Infrastructure Audit.").
  * View application logs on managed node compute instances. See [Viewing Application Logs on Managed Nodes and Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm#Viewing_Worker_Node_Logs "Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).").
  * Monitor the health, capacity, and performance of clusters, node pools, and nodes at a more granular level using **metrics** , **alarms** , and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").


## Using the Console 🔗 
To create a new service log object to enable you to view and search the logs of Kubernetes processes running on a cluster's control plane:
  1. Open the **navigation menu** and select **Observability & Management**. Under **Logging** , select **Logs**.
  2. Choose a **Compartment** you have permission to work in.
  3. Click **Enable service log** to create a new service log.
  4. In the **Enable Resource Log** dialog:
    1. Identify the cluster, by specifying:
       * **Resource Compartment:** Select the compartment to which the cluster belongs.
       * **Service:** Select **Kubernetes Engine**.
       * **Resource:** Select the cluster for which you want to enable service logs.
    2. Configure the service log you want to view, by specifying:
       * **Log Category:** Select the Kubernetes process for which you want to view the service log (for example,**kube-controller-manager**), or select **All log sources**.
       * **Log Name:** A name of your choosing for the new service log. Avoid entering confidential information.
    3. Optionally, click **Show Advanced Options** and specify:
       * **Log Location:** The compartment in which to create the service log.
       * **Log Group:** The log group in which to place the service log. Optionally, click **Create New Group** to create a new log group (see [Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm)).
       * **Log Retention:** The length of time (in months) to retain the service log. Select one of the predefined options, or select **Custom time** and specify a number of months (up to a maximum of 60). 
       * **Tagging Options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    4. Click **Enable Log**.
A new service log is created, and the **Log Details** page is displayed.


To view and search the contents of a service log:
  1. Open the **navigation menu** and select **Observability & Management**. Under **Logging** , select **Logs**.
  2. Click the name of the service log that you want to view. You can sort log entries by age, and filter by time.
  3. (Optional) Click **Actions** and select **Explore with Log Search** to open the central logging **Search** page. You can apply filters, and explore and visualize the log data in different ways.


Was this article helpful?
YesNo

