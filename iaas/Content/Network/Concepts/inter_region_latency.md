Updated 2025-02-18
# Inter-Region Latency
View the Inter-Region Latency dashboard in the Console. The dashboard provides the average network round-trip latency (round-trip time or RTT) for all pairs of **regions** in an Oracle Cloud Infrastructure **realm**. In realms with only one region, the Inter-Region Latency dashboard isn't available. 
The dashboard shows a current snapshot view and lets you view historic snapshots including up to a 30-day history. The latency information provided isn't specific to a **tenancy's** workloads. Rather, these global statistics provide visibility into latency among all regions to help you plan scenarios such as backup and data transfers. This dashboard isn't intended for use in troubleshooting.
The Inter-Region Latency dashboard shows the following charts:
  * **Current Inter-Region Round-Trip Time** provides a current snapshot expressed in milliseconds. This snapshot is an average of values over the last five minutes. This view updates every minute.
  * **Inter-Region Round-Trip Time (ms) for the last 30 days** provides a historical view of the last 30 days.


## **Viewing the Latency Dashboard** 🔗 
Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Inter-region latency**.
The **Current Inter-Region Round-Trip Time** chart is at the top of the page. With this chart, you can perform the following actions:
  * Select two regions (one is the "from" region and one is the "to" region ) and then select **Show**. The relevant cell is highlighted and displays the RTT in milliseconds for the origin-destination pair. 
  * Hover over the three-letter code in the heading row or column to see the region name associated with the code. 
  * Select a cell in the table that corresponds to a pair of regions to highlight the cell. The cell displays the RTT in milliseconds for the origin-destination pair.


The **Inter-Region Round-Trip Time (ms) for the last 30 days** chart is at the bottom of the page. With this chart, you can perform the following actions: 
  * Select two regions (one is the "from" region and one is the "to" region ) and then select **Show**. The relevant graph of latency times between the origin-destination pair is displayed. The graph covers the last 30 days by default
  * Using the date bar under the chart, slide the beginning and end of the bar to change the time period covered by the chart.
  * Hover over a point on the graph to get the values in milliseconds for that point in time.


Was this article helpful?
YesNo

