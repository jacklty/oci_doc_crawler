Updated 2025-01-13
# Viewing Default Metric Charts for a Single Resource
Go to a resource's details page in the Console to view metric charts that use predefined service queries for that resource. The charts show metric data for the selected resource.
**Note**
To access resource-specific metric charts from other pages in the Console (including the **Service Metrics** page), select a resource-specific dimension. See [Selecting Dimensions on the Service Metrics Page](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-dimensions.htm).
For information about directly editing MQL expressions and changing queries by using the CLI or API in this context, see [Selecting a Resource for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-resource.htm).
On the page for the resource of interest, under **Resources** , select **Metrics**. 
For example, to view metric data for a Compute instance: 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Select the name of the instance that you want to see metrics for.
  3. On the instance details page, under **Resources** , select **Metrics**.
The page displays a chart for each metric. For a list of metrics related to Compute instances, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).


The Console displays the last hour of metric data for the selected resource. The page shows a chart (graph) for each metric emitted by the selected resource.
For example, default charts for a Compute instance include **CPU Utilization** and **Memory Utilization**.
For a list of metrics emitted by the resource, see [Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).
For query troubleshooting, see [Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).
Was this article helpful?
YesNo

