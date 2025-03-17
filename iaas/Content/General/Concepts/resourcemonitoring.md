Updated 2024-02-13
# Resource Monitoring
You can monitor the health, capacity, and performance of your Oracle Cloud Infrastructure resources when needed using **queries** or on a passive basis using **alarms**. Queries and alarms rely on **metrics** emitted by your resource to the Monitoring service. 
## Prerequisites 🔗 
  * IAM policies: To monitor resources, you must have the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you have and which **compartment** you should work in. For more information about user authorizations for monitoring, see [IAM Policies (Monitoring)](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
  * Metrics exist in Monitoring: The resources that you want to monitor must emit metrics to the Monitoring service. 
  * Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see [Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm). 


## Working with Resource Monitoring 🔗 
Not all resources support monitoring. See [Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices) for the list of resources that support the Monitoring service, which is required for queries and alarms used in monitoring. 
The following pages describe basic resource monitoring tasks:
  * [Viewing Default Metric Charts for a Single Resource](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/view-chart-resource.htm#top "Go to a resource's details page in the Console to view metric charts that use predefined service queries for that resource. The charts show metric data for the selected resource.")
  * [Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/view-chart-namespace.htm#top "Go to the Service Metrics page in the Console to view metric charts that use predefined service queries for a selected metric namespace. The charts show metric data for all resources in the selected metric namespace, compartment, and region.")
  * [Creating a Query](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/query-metric.htm#top "Define a query to retrieve data from Monitoring.")
  * [Creating an Alarm from a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/view-chart-create-alarm.htm#top "Create an alarm based on the predefined service query used to generate a default metric chart. Default metric charts are available on the Service Metrics page and under Metrics on resource details pages in the Console.")


Was this article helpful?
YesNo

