Updated 2024-02-13
# Viewing Carbon Emissions Reports
View carbon emissions reports using the Console or the API.
## Using the Console 🔗 
To view Carbon Emissions Analysis reports in the Console:
  1. Open the navigation menu and click **Governance & Administration**. Under **Emissions Management** , click **Carbon Emissions Analysis**.
  2. From **Reports** , select a report to view. You can view either the default **System Reports** , or create and save your own reports, which appear under the **Saved Reports** section of the **Reports** menu. By default, the **Customer Carbon Footprint by Service** report is selected.
The following default **System Reports** are available:
     * **Customer Carbon Footprint by Service** (shown by default when the Carbon Emissions Analysis page opens)
     * **Customer Carbon Footprint by Service and Description**
     * **Customer Carbon Footprint by Service and SKU (Part Number)**
     * **Customer Carbon Footprint by Region**
     * **Monthly Customer Carbon Footprint**
  3. From **Time range** , select the time range you want to view reports from.
     * 2 Months to Date (the default)
     * 3 Months to Date
     * 6 Months to Date
     * 1 Year to Date
     * Custom: Select the starting and ending year and month (YYYY-MM format) from the **Start month** and **End month** fields. The minimum allowed date range is 6 months, which is filled by default, and the maximum is 12.
  4. From **Filters** , you can filter on or more of the following. You can add multiple filters if preferred. Added filters appear next to the **Filters** field. Click the **X** icon to remove individual filters, or **Clear all filters** to remove all.
     * **Availability Domains**
     * **Compartment**
**Note** Filtering by compartment displays carbon usage attributed to all resources in the selected compartments.
       * **By name**
       * **By OCID**
       * **By Path** (for example, root/compartmentname/compartmentname)
     * **Platform** : **Gen_1** are services which aren't OCI native. **Gen_2** includes all OCI native services.
     * **Tag**
       * **Tag Namespace**
       * **Tag Key** + **Match any value** or **Match any of the following**
     * **Region**
     * **Service**
     * **Subscription ID**
     * **Resource OCID**
     * **Product description** (the human-readable corresponding name) 
     * **SKU (Part Number)** (for example, B91444)
     * **Tenant**
     * **Unit**
You can also edit any applied filter by clicking its name, make changes, and then click **Select**.
Filters are ORed within each specific filter, and ANDed between filters. For example, a filter for Service = Compute, Block Storage, Object Storage, Database, and Tag = Tag Key "MyKey" displays data that's for (Compute OR Block Storage OR Object Storage OR Database) AND Tag Key "MyKey".
The **Tag** filter, however, is a unique case. You can add multiple **Tag** filters, which function as a joined OR.
**Note** In the **Tag** dialog, only ten **Tag Key** values are retrieved and shown in the **Tag Key** list when you try to select a possible **Tag Key** value. Or, you can manually type in the **Tag Key** value you want to filter on when **None (free-form-tag)** is selected.
  5. From **Grouping dimensions** , select an option to visualize the data in terms of the particular grouping. A grouping dimension by **Service** is displayed by default. Grouping dimensions change the way data is aggregated, but don't change the sum. If a resource doesn't have a value for a particular field, a "no value" column is displayed, which reflects the sum of those resources. Products which are GEN_1 often don't have an Availability domain, compartment, or resource ID. You can view only one grouping dimension at a time.
     * **Availability Domain**
     * **Compartment**. When you group by compartment, you can pick the display name value, and a compartment depth. The compartment depth corresponds to the lowest level you want the compartments to be grouped by. All levels above that grouping level return what is directly in those compartments. The grouping level returns values for all resources in those compartments, plus all resources in compartments below it. 
       * **Display as**
         * **Compartment Name**
         * **Compartment OCID**
**Note** If **Compartment OCID** is selected, you can't view **Compartment Level**.
         * **Compartment Path**
       * **Compartment Level**
         * All (the default): Every compartment is displayed. Values would display usage associated only with the resources in that specific compartment. 
         * Level 1 (root only): Only 1 column is returned (root), and values for resources contained in root and every child compartment are displayed. 
         * Level 2 (root/<value>): Displays root, with values for root equaling only those resources in root. All compartments that are direct children of root are also returned. The values for each of those compartments is the sum of all resources therein, or within any children of those compartments. 
         * Level 3 (root/<value>/<value>): Returns root, with values for root equaling only those resources in root. All Level 2 compartments are also returned, but with values only equal to the resources contained in each of those specific compartments. The first child level of the level 2 compartments are also returned. The values for the third level of compartment (root/child1/child2) would be equal to the resources in those compartments, plus all the resources in all the children of those compartments. 
         * Level 4 (root/<value>/<value>/<value>) 
         * Level 5 (root/<value>/<value>/<value>/<value>)
     * **Platform** : GEN_1 are services which aren't Oracle Cloud Infrastructure native, while GEN_2 includes all native Oracle Cloud Infrastructure services.
     * **Region**
     * **Resource OCID**
     * **Service**
     * **Service and Product Description**
     * **Service and SKU (Part Number)**
     * **SKU (Part Number)**
     * **SKU (Product Description)**
     * **Subscription ID**
     * **Tag**
       * **Tag Namespace**
       * **Tag Key**
     * **Tenant ID**
     * **Tenant Name**
  6. Click **Apply** to reload the chart with the selected report type, time range, filters and grouping dimensions.
Under **Carbon emissions details (MTCO2e)** , the **Carbon emissions by date** chart displays the selected data. The chart is organized in terms of the date (UTC) on the X-axis, and the Carbon Emission MTCO2e (Metric Tons Carbon dioxide equivalent) amount on the Y-axis. When viewing a chart, you can hover the mouse over a data point in the chart to see more details. The tooltip shows the data point details for the particular Y-axis item at a particular time, whether you're viewing the chart as either a **Bars** (the default), **Lines** , or **Stacked Lines** chart.
Select the **Cumulative** option to change the values so that they're cumulative for the selected time period. For example, consider if you were looking at 10 months of data, cumulatively, and the values for each month are 5. In such a case, selecting **Cumulative** displays values of 5, 10, 15, 20, 25, 30, 35, 40, 45, and 50 across the 10 months. In a non-cumulative chart, the values display as 5, 5, 5, 5, 5, 5, 5, 5, 5, 5.
To the right of the chart, the **Legend** box shows all the data by default, and each item is color-coded. You can click any of the **Legend** items to switch the chart data on or off for that item. For example, when viewing a chart with various services and their emissions, the **Legend** box includes all the impacted services related to the query. Toggling one or more of the services shows or hides them dynamically from the chart output. Toggling the **Legend** data, however, doesn't change the data shown in the table below the chart, or what you can download from the **Download** menu.
A tabular version of the chart is also provided, which is also updated as you apply different time range, filtering, and grouping dimension options. When viewing the table data, you can click any of the column headers to sort in ascending or descending order.
  7. (Optional) You can download your carbon emissions data from the **Download** menu.
     * **Download table as CSV** : Download a CSV file of the data. In the **Export Confirmation** that opens, click **Confirm**. You can then download a CSV file with the current date included in the file name.
     * **Download as PDF** : Export the chart and table data to PDF. In the **Export Confirmation** that opens, click **Confirm**. You can then save a PDF file with the **Carbon emissions by date** chart, and which includes the current timestamp in the PDF file name. The PDF version of the chart includes the legend items, and reflects the selected time range, applied filters, and grouping dimensions.
     * **Download chart** : Download a PNG image of the chart, with the current timestamp included in the file name. The chart image includes the legend items, and reflects the selected time range, applied filters, and grouping dimensions.
  8. After viewing any of the predefined **System Reports** in the **Reports** menu, and then applying custom date range, filters, and grouping dimensions, you can save your reports for later viewing. See [Saving Reports](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#carbon-analysis-savingreports "Use the Report actions menu in Carbon Emissions Analysis to create a saved report.") for more information.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following [Usage API](https://docs.oracle.com/iaas/api/#/en/usage/) operations to manage Carbon Emissions Analysis:
  * [RequestAverageCarbonEmission](https://docs.oracle.com/iaas/api/#/en/usage/latest/AverageCarbonEmission/RequestAverageCarbonEmission)
  * [RequestCleanEnergyUsage](https://docs.oracle.com/iaas/api/#/en/usage/latest/CleanEnergyUsage/RequestCleanEnergyUsage)
  * [RequestUsageCarbonEmissionConfig](https://docs.oracle.com/iaas/api/#/en/usage/latest/Configuration/RequestUsageCarbonEmissionConfig)
  * [CreateUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/CreateUsageCarbonEmissionsQuery)
  * [DeleteUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/DeleteUsageCarbonEmissionsQuery)
  * [GetUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/GetUsageCarbonEmissionsQuery)
  * [ListUsageCarbonEmissionsQueries](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/ListUsageCarbonEmissionsQueries)
  * [UpdateUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/UpdateUsageCarbonEmissionsQuery)
  * [RequestUsageCarbonEmissions](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionSummary/RequestUsageCarbonEmissions)


Was this article helpful?
YesNo

