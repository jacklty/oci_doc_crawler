Updated 2025-01-15
# Viewing Application Logs on Managed Nodes and Self-Managed Nodes
_Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine (OKE)._
Having created a cluster using Kubernetes Engine, you can use Oracle Cloud Infrastructure Logging to view and search the logs of applications running on compute instances hosting managed nodes and self-managed nodes in the cluster.
Before you can collect and parse the application logs using Oracle Cloud Infrastructure Logging:
  * You must have already:
    * Enabled monitoring for compute instances hosting managed nodes and self-managed nodes (see [Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm)).
    * Installed the Oracle Cloud Agent software on compute instances hosting managed nodes and self-managed nodes. The agent enables you to specify which logs to collect and how to parse them. The agent is installed by default on managed node compute instances. To confirm that the agent is already installed, see [Verify Agent Installation](https://docs.oracle.com/iaas/Content/Logging/Task/verify_agent_installation.htm).
  * You must have already:
    * Created a dynamic group with a rule that includes the compute instances hosting managed nodes and self-managed nodes as target hosts (see [About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About) and [Selecting Target Hosts with Dynamic Groups](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs_multihost.htm)). For example:
Copy
```
instance.compartment.id = 'ocid1.tenancy.oc1..<unique-id>'
```

    * Created a policy for the dynamic group with a policy statement to allow the target hosts in the dynamic group to push logs to Oracle Cloud Infrastructure Logging (see [Selecting Target Hosts with Dynamic Groups](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs_multihost.htm)). For example:
Copy
```
allow dynamic-group <dynamic-group-name> to use log-content in tenancy
```

Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format `dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format `dynamic-group id <dynamic-group-ocid>`.


Having completed the above prerequisites, you can then define custom logs and associated agent configurations to view application logs on compute instances hosting managed nodes and self-managed nodes. Note that application logs must be output to the file path that you specify when you create an agent configuration (typically, but not necessarily, `/var/logs/containers`). For more information about custom logs and agent configurations, see [Custom Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs.htm).
Note that in addition to viewing application logs on compute instances hosting managed nodes and self-managed nodes, you can also:
  * Monitor the overall status of the cluster itself, node pools, and nodes. See [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
  * View and search the logs of Kubernetes processes (such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver running in the cluster's control plane. See [Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm#contengviewingservicelogs "Find out how to view the logs of Kubernetes processes \(such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver\) running on the control plane of clusters you've created using Kubernetes Engine \(OKE\).").
  * Monitor the health, capacity, and performance of clusters, node pools, and nodes at a more granular level using **metrics** , **alarms** , and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").


## Using the Console 🔗 
To define a new custom log object and an associated agent configuration to enable you to view and search the logs of applications running on compute instances hosting managed nodes and self-managed nodes in a cluster:
  1. Open the **navigation menu** and select **Observability & Management**. Under **Logging** , select **Logs**.
  2. Choose a **Compartment** you have permission to work in.
  3. Click **Create custom log** to create a new custom log.
  4. On the **Create custom log** page, specify:
     * **Custom Log Name:** A name of your choosing for the new custom log. Avoid entering confidential information.
     * **Compartment:** The compartment in which to create the new custom log.
     * **Log Group:** The log group in which to place the custom log. Optionally, click **Create New Group** to create a new log group (see [Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm)).
  5. Optionally, click **Show additional options** and specify:
     * **Log Retention:** The length of time (in months) to retain the custom log. Select one of the predefined options, or select **Custom time** and specify a number of months of your choosing (up to 60). 
     * **Tagging Options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  6. Click **Create custom log**. 
A new custom log is created, and the **Create agent configuration** page is displayed.
For convenience, these instructions now describe how to create a new agent configuration associated with the new custom log (although you can create a new agent configuration later if you prefer). 
  7. On the **Create agent configuration** page, select **Create new configuration** and specify:
     * **Configuration Name:** A name of your choosing for the new agent configuration. Avoid entering confidential information.
     * **Description:** A description for the new agent configuration.
     * **Compartment:** The compartment in which to create the new agent configuration.
  8. In the **Host Groups** panel on the **Create agent configuration** page, specify:
     * **Group type:** Select **Dynamic group**.
     * **Group:** An existing dynamic group that includes managed nodes in the cluster's managed node pools as target hosts. The dynamic group you select must have permission to access the compartment you specified for the agent configuration, and must also allow target hosts to push logs to Oracle Cloud Infrastructure Logging.
  9. In the **Agent configuration** panel on the **Create agent configuration** page, specify:
     * **Configure log inputs:** One or more locations from which to obtain application logs as inputs to the custom log, as follows:
       * **Input type:** Select **Log path**.
       * **Input name:** A name of your choosing for the new log input.
       * **File paths:** The path to application logs on the compute instances hosting managed nodes and self-managed nodes. For example, typically (but not necessarily) `/var/logs/containers/*`
     * **Select log destination:** The options are pre-populated with the custom log details you specified previously.
  10. Optionally, click **Show additional options** and specify:
     * **Tagging Options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  11. Click **Create agent config** to create the agent configuration associated with the custom log.


To view and search the contents of a custom log created for an application running on compute instances hosting managed nodes and self-managed nodes in a cluster:
  1. Open the **navigation menu** and select **Observability & Management**. Under **Logging** , select **Logs**.
  2. Click the name of the custom log that you want to view. You can sort log entries by age, and filter by time.
  3. (Optional) Click **Actions** and select **Explore with Log Search** to open the central logging **Search** page. You can apply filters, and explore and visualize the log data in different ways (see [Viewing Custom Logs in a Compute Instance](https://docs.oracle.com/iaas/Content/Logging/Concepts/viewing_custom_logs_in_a_compute_instance.htm)).


Was this article helpful?
YesNo

