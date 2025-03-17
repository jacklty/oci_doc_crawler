Updated 2024-08-06
# Creating a Query with Metrics Explorer
On Compute Cloud@Customer, you can create your own metric queries using Metrics Explorer.
Use the information in this section to create a metric query that's specifically for Compute Cloud@Customer infrastructure resources using the metric oci_ccc namespace. For general information about metric queries, see [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
  1. Open the Oracle Cloud Console navigation menu, and click **Observability & Management**. Under **Monitoring** , click **Metrics Explorer**. 
The **Metrics Explorer** page displays an empty chart with fields to build a query.
  2. From the Console header, select the region that contains the metric data that you want. 
For more information about regions, see [Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions). 
  3. **(Optional)** The default query period is set to **Last hour**. To change it, go to the top panel, and set the query period by selecting a **Start time** and **End time** , or select a period from the **Quick selects** menu. 
  4. In the **Query** area under the chart, select values for the following items: 
     * **Compartment:** Select the compartment where the Compute Cloud@Customer infrastructure was created.
     * **Metric namespace:** Select **oci_ccc** (the Compute Cloud@Customer namespace).
     * **Metric name:** From the drop-down menu, select one of the Compute Cloud@Customer metrics. For descriptions of each metric, see [Compute Cloud@Customer Metrics Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/metrics-reference.htm#metrics-reference "See a list of metrics emitted by Compute Cloud@Customer using the oci_ccc metric namespace.").
     * **Interval:** Change the default interval to a value greater than collection frequency. For queries using the oci_ccc namespace, choose an interval of 15 minutes or longer. 
     * **Statistic:** Select a statistic. For queries using the oci_ccc namespace, Max works well.
  5. **(Optional)** In the **Metric dimensions** area, to further refine the query, select values for the following items:
     * **Dimension name:** From the drop-down menu, select a dimension value. For example, to see metrics for a particular fault domain, select **faultDomain**.
     * **Dimension value:** From the drop-down menu, select a dimension value. For example, you might select a specific fault domain for this query.
  6. Click **Update Chart**.
The chart shows data points for the custom metric in a graph view. 
To change the metric chart, update the query values, then click **Update Chart** again.
The query is a one-time query. If you want a persistent query, you can take advantage of the following services:
     * Configure a query in a **Console Dashboard**. The Console Dashboard service enables you to create custom dashboards to monitor resources, diagnostics, and key metrics for your tenancy. See [Console Dashboards](https://docs.oracle.com/iaas/Content/Dashboards/home.htm).
     * View the default metric charts. See [Viewing Compute Cloud@Customer Default Metric Charts](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/viewing-default-metrics.htm#viewing-default-metrics "You can view the default metric charts for the Compute Cloud@Customer infrastructure. The charts show metrics for total and available OCPUs, memory, and storage resources in the infrastructure.").


Was this article helpful?
YesNo

