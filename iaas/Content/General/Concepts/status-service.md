Updated 2024-07-19
# System Status
The Oracle Cloud Infrastructure Status service allows you to see the status of OCI services in a region on a dashboard, and query service status programmatically.
**Note** The Oracle Cloud Infrastructure Status dashboard shows service outages at the service or region level. Outages specific to a customer are communicated to the customer with [Console Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Console_Announcements).
## Service Highlights 🔗 
  * View a dashboard that shows the health of services in a region.
  * See event information, and a history of events.
  * Programmatically query the status of services.
  * You can access the status dashboard from a provided URL.


## Status Dashboard 🔗 
The Status Dashboard shows the health of each individual service in a realm. The Status Dashboard page is auto-refreshed every 5 minutes. To view the status for a region group, click on the corresponding tab at the top of the dashboard panel.
![This image shows a screenshot of the dashboard.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/status-1.jpg)
### Status Icons
Services displayed in the dashboard can show the following types of status indicator icons:
  * **Normal Performance**![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/NormalPerformance.png)**:** The service is available and operating within normal parameters. This status won't have an associated event report.
  * **Informational**![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/Informational.png)**:** Useful information regarding service performance is available.
  * **Service Disruption**![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ServiceDisruption.png)**:** The service is reporting a high number of request failures, resulting in the service being unavailable some of the time. This status has an associated event report.
  * **Service Down**![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ServiceDown.png)**:** The service is not available. This status has an associated event report.
  * **Dash (-):** Service not available in the region.


**Tip** Click on a ![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/Informational.png), ![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ServiceDisruption.png), or ![](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ServiceDown.png) icon to view the associated event report. Learn more about [event reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_Incidents).
### To view the Status dashboard:
  1. For commercial regions, open a browser and navigate to <https://ocistatus.oraclecloud.com/>.
For government regions, open a browser and navigate to <https://gov.ocistatus.com/>.
**Tip** Bookmark the URL for future reference.


## Service Events 🔗 
The **History** provides detailed event reports for each service that experiences degraded, partial, or complete outage conditions. Filter events by **Services** and **Regions**. You can obtain information for both current events and those that occurred in the past up to today's date. Use the **Date Range** selector to view past events.
You can access the **History** from the Status Dashboard, and you can also subscribe to **RSS** notifications about events and updates.
### Event Details
The following information is available for each event. Some types of information won't be immediately available but are added as the event is investigated, addressed, and closed:
  * **Title:** A short description of the location, affected services, and reference number for the event.
  * **Event Status:** The current mitigation status of the event. Options are **Investigating** , **Identified** , **Monitoring** , and **Resolved**.
  * **Message:** Informative messages from the Oracle Cloud Infrastructure team about the event and action being taken to resolve the event. 
  * **Customer Impact:** Details about the effects that customers might see in their services as a result of the event.
  * **Reference Number:** A unique reference number identifying the event.
  * **Start Time:** (Included if known) The date and time that the event first occurred, shown in UTC format. For example: January 17, 2021, 17:35 UTC
  * **End Time:** (Included if known) The date and time that the event was resolved, shown in UTC format. For example: January 18, 2021, 05:29 UTC
  * **Next Update:** The estimated time that you can expect an event update, shown in UTC format. For example: January 18, 2021, 10:30 UTC
  * **Preliminary Root Cause:** (When determined) A summary of the preliminary root cause of the event.


[To view service events](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm)
  1. Open a browser and navigate to <https://ocistatus.oraclecloud.com/> for commercial regions, or <https://gov.ocistatus.com/> for government regions.
  2. Click on **History** in the upper-right corner of the menu bar.
  3. Use the **Services** and **Regions** filters to find an event for a specifc service, or within a specified region.
  4. Click on the directional arrows to **Select a Date Range** you want to view.
  5. Click the **View More** link to see Event Details related to the event.


[To subscribe to RSS notifications about status updates](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm)
**Note**
  * When you subscribe, you receive _all notifications_ for all services and regions.


  1. Open a browser and navigate to <https://ocistatus.oci.oc.scloud>.
  2. Click on **RSS** in the upper-right corner of the menu bar.
  3. Copy the RSS feed URL link. Open your RSS reader and follow the instructions to load the Status feed URL.


## Programmatically Accessible Status Reports 🔗 
The status service provides JSON file reports that you can download:
  * **Summary Report:** Shows the current status of every service and region. 
Download this report: <https://ocistatus.oraclecloud.com/api/v2/components.json>
  * **Status Report:** Shows a high-level status for all systems. 
Download this report: <https://ocistatus.oraclecloud.com/api/v2/status.json>


### JSON File Contents and Syntax
Expand to view an example of each report JSON file, and a table of syntax definitions:
[Example of the Summary Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm)
**Note** This example shows a shortened sample of the report contents. To see the full report, download it from the provided URL.
```
{
 "realm": "OC1",
 "regionHealthReports": [{
   "regionId": "<unique_id>",
   "regionName": "US East (Ashburn)",
   "regionCanonicalName": "us-ashburn-1"
   "geographicAreaName": "North America",
   "serviceHealthReports": [ {
    "serviceId" : "<unique_id>",
    "serviceName" : "Account Management and Billing",
    "serviceCanonicalName" : "account-management-and-billing",
    "serviceCategoryId" : "<unique_id>",
    "serviceCategoryName" : "Cloud Services",
    "serviceStatus" : "NormalPerformance",
    "incidents" : [ {
     "incidentId" : "ocid1.oraclecloudincident.<unique_id>",
     "severity" : "Informational"
   } ]
  }, {
    "serviceId" : "<unique_id>",
    "serviceName" : "Console",
    "serviceCanonicalName" : "console",
    "serviceCategoryId" : "<unique_id>",
    "serviceCategoryName" : "Cloud Services",
    "serviceStatus" : "NormalPerformance",
    "incidents" : [ ]
  }, {
    "serviceId" : "<unique_id>",
    "serviceName" : "Developer Tools",
    "serviceCanonicalName" : "developer-tools",
    "serviceCategoryId" : "<unique_id>",
    "serviceCategoryName" : "Cloud Services",
    "serviceStatus" : "NormalPerformance",
    "incidents" : [ ]
    }
   ]
  },
	  {
    "regionId" : "<unique_id>",
    "regionName" : "US West (Phoenix)",
    "regionCanonicalName" : "us-phoenix-1",
    "geographicAreaName" : "North America",
    "serviceHealthReports" : [ {
     "serviceId" : "<unique_id>",
     "serviceName" : "Account Management and Billing",
     "serviceCanonicalName" : "account-management-and-billing",
     "serviceCategoryId" : "e<unique_id>",
     "serviceCategoryName" : "Cloud Services",
     "serviceStatus" : "NormalPerformance",
     "incidents" : [ ]   
    } ]
 } ]
}
```

TBD Field Name | Definition | Type | Examples  
---|---|---|---  
`realm` | The Oracle Cloud Infrastructure realm | string |  `"OC1", "OC2"` A realm is a logical collection of regions. Realms are isolated from each other and do not share any data.  
`regionHealthReports` | Heath reports grouped by region. | array | See preceding [Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).  
`regionId` | Unique identifier for a region | string | Numeric, dash-separated value  
`regionName` | The region name | string | US East (Ashburn) See [About Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#About) for more information.  
`regionCanonicalName` | The canonical name of the region, used for search consistency | string | `account-management-and-billing`  
`geographicAreaName` | The geographic group the region is in | string | `"Americas", "Europe"`  
`serviceHealthReports` | Heath reports grouped by service | array | See preceding [Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).  
`serviceId` | Unique identifier for a service | string | Numeric, dash-separated value  
`serviceName` | The name of a specific service | string | `"Autonomous Data Warehouse", "File Storage", "Virtual Cloud          Networks"`  
`serviceCanonicalName` | The canonical name of the service, used for search consistency | string | `account-management-and-billing`  
`serviceCategoryId` | Unique identifier for a service category | string | Numeric, dash-separated value  
`serviceCategoryName` | The category the service belongs to. Each service is grouped in the same service category as in Console home page.  | string | `"Compute", "Storage", "Analytics", "Database",         "Networking"`  
`serviceStatus` | The current status of the service | string | `Normal Performance, Informational, Service Disruption, Service          Down`  
`incidents` | Events reported by the service | array | See preceding [Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).  
`incidentId` | Unique identifier for an event | string | OCID (Oracle Cloud Identifier)  
`severity` | The event severity | string | `Normal Performance, Informational, Service Disruption, Service          Down`  
[Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm)
```
{
"page": {
"name": "OCI",
"updated_at": "2021-08-27T20:43:33.591Z"
},
"status": {
"indicator": "minor",
"description": "Minor Service Outage"
}
}
```

TBD Field Name | Definition | Type | Examples  
---|---|---|---  
`page` | The status report page. | array | See preceeding [Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__status_json).  
name | The status report name. | string | "OCI"   
`updated_at` |  Report creation time in ISO 8601 format.  Expressed as `<date>T<time>` | string |  `"updated_at": "2021-09-18` `T19:55:47.204985"`  
`status` | The high-level status of all systems. | array | See preceeding [Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__status_json).  
`indicator` | The current status of all systems. | string |  `critical` `major` `minor` `none`  
`description` | A description of the current status of all systems. | string |  Critical Service Outage Major Service Outage Minor Service Outage No Service Outage  
Was this article helpful?
YesNo

