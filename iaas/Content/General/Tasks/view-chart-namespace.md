Updated 2025-01-15
# Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)
Go to the **Service Metrics** page in the Console to view metric charts that use predefined service queries for a selected metric namespace. The charts show metric data for all resources in the selected metric namespace, compartment, and region.
For prerequisite information, see [Before You Begin](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm#prerequisites).
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see [Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions) and [Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
  3. On the **Service Metrics** page, select the compartment that contains the resources for which you want metric data.
The **Metric namespace** list is populated with metric namespaces for the selected region and compartment. For example, if the current compartment contains load balancers, then the list includes **oci_lbaas**.
  4. Select the metric namespace for the resource type of interest.
For example, select **oci_lbaas** to see metrics for load balancers.
  5. (Optional) To change the time range:
    1. Select a period of time from **Quick Selects**.
For example, **Last hour**.
    2. To specify the start or end of a period time, enter a value in **Start time** or **End time** and then type a value.


The **Service Metrics** page displays default charts for all resources in the selected region and compartment that emit metric data to the selected metric namespace.
You can update the query by [adding or editing dimensions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-dimensions.htm), by [aggregating metric streams](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-aggregate-metric-streams.htm), or by [opening the chart in the **Metrics Explorer** page](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-explore.htm) for advanced query updates. You can also [create an alarm based on the query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-create-alarm.htm).
For query troubleshooting, see [Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).
Was this article helpful?
YesNo

