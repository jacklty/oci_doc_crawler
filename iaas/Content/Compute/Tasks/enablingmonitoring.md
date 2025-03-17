Updated 2025-02-13
# Enabling Monitoring for Compute Instances
This topic describes how to enable monitoring, specifically for the [compute instance metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics), on compute instances.
The compute instance metrics provide data about the activity level and throughput of the instance. These metrics are required to use features such as autoscaling, metrics, alarms, and notifications with compute instances. A compute instance emits these metrics only when the Compute Instance Monitoring plugin is enabled and running on the instance.
The Compute Instance Monitoring plugin is [managed by the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
**Note** To monitor certain metrics without the use of Oracle Cloud Agent, use [Agentless Compute Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics-topic-available-metrics-oci-vmi-resource-utilization.htm#agentless-compute-metrics "This topic describes the metrics emitted by the private agentless metric namespace oci_vmi_resource_utilization.").
## Supported Images 🔗 
Compute instance metrics are supported on current [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images) and on [custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI) that are based on current platform images.
If you use an older platform image, you must [manually install the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent) before you can use the Compute Instance Monitoring plugin. Select an image dated after November 15, 2018 (except Ubuntu, which must be dated after February 28, 2019).
You might have success enabling compute instance metrics on other [images that support the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#supported-images), though the Compute Instance Monitoring plugin has not been tested on other operating systems and there is no guarantee that it will work.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For more information about the IAM policies that are needed to create and update a compute instance, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
## Before You Begin 🔗 
  * **Service gateways or public IP addresses:** The compute instance must have either a public IP address or a service gateway to be able to send compute instance metrics to the Monitoring service.
If the instance does not have a public IP address, set up a service gateway on the virtual cloud network (VCN). The service gateway lets the instance send compute instance metrics to the Monitoring service without the traffic going over the internet. Here are special notes for setting up the service gateway to access the Monitoring service: 
    * When creating the service gateway, enable the service label called **All <region> Services in Oracle Services Network**. It includes the Monitoring service.
    * When setting up routing for the subnet that contains the instance, set up a route rule with **Target Type** set to **Service Gateway** , and the **Destination Service** set to **All <region> Services in Oracle Services Network**.
For detailed instructions, see [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
  * **Oracle Cloud Agent:** The Oracle Cloud Agent software must be installed on the instance. Oracle Cloud Agent is installed by default on current platform images. For steps to manually install Oracle Cloud Agent on older images, see [Installing the Oracle Cloud Agent Software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent).
  * **Compute Instance Monitoring plugin:** For the instance to emit the compute instance metrics, the Compute Instance Monitoring plugin must be enabled on the instance and plugins must be running. For more information about how to enable and run plugins, see [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).


## Enabling Monitoring for a New Compute Instance 🔗 
To configure a new compute instance to emit the compute instance metrics, use the following steps.
### Creating a Monitoring-Enabled Instance Using the Console 🔗 
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the advanced options. Ensure that the instance has either a public IP address or a service gateway, as described in the [prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).
  2. Click **Show Advanced Options**.
  3. On the **Oracle Cloud Agent** tab, select **Compute Instance Monitoring**.
**Note** If you're using an older platform image or a custom image that is not based on a recent platform image, you must manually install the Oracle Cloud Agent software. You can do this by providing a cloud-init script. For more information, see [Installing the Oracle Cloud Agent Software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent). Compare the date of the image to the date listed in [Supported Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).
  4. Click **Create**.
The newly created, monitoring-enabled instance emits compute instance metrics to the Monitoring service.


### Creating a Monitoring-Enabled Instance Using the API 🔗 
Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation. Include the following parameters:
Copy
```
{
 "agentConfig": {
  "isMonitoringDisabled": false,
  "areAllPluginsDisabled": false,
  "pluginsConfig": [
   {
    "name": "Compute Instance Monitoring",
    "desiredState": "ENABLED"
   }
  ]
 }
}
```

Ensure that the instance has either a public IP address or a service gateway, as described in the [prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).
**Note** If you're using an older platform image or a custom image that is not based on a recent platform image, you must manually install the Oracle Cloud Agent software. You can do this by providing a cloud-init script. For more information, see [Installing the Oracle Cloud Agent Software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent). Compare the date of the image to the date listed in [Supported Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).
## Enabling Monitoring for an Existing Compute Instance 🔗 
To configure an existing compute instance to emit the compute instance metrics, use the following steps.
[To enable monitoring on an existing compute instance using the Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), if it is not already installed.
  2. [Enable the Compute Instance Monitoring plugin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#disable-one-plugin).
  3. [Confirm that plugins are running on the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#turn-on-all-plugins).
  4. Ensure that the instance has either a public IP address or a service gateway, as described in the [prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).
  5. To confirm that monitoring is enabled:
    1. Go to the Metrics page for the instance: 
      1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
      2. Click the instance that you're interested in.
      3. Under **Resources** , click **Metrics**.
      4. In the **Metric namespace** list, select **oci_computeagent**.
    2. If you see metric charts with data, then the Monitoring service is receiving compute instance metrics from this instance. For more information about these metrics, see [Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics).
If monitoring is not enabled (and the instance uses a supported image), then a button is available to enable monitoring. Click **Enable monitoring**.


[To enable monitoring on an existing compute instance using the API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), if it is not already installed.
  2. Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation. Include the following parameters:
Copy
```
{
 "agentConfig": {
  "isMonitoringDisabled": false,
  "areAllPluginsDisabled": false,
  "pluginsConfig": [
   {
    "name": "Compute Instance Monitoring",
    "desiredState": "ENABLED"
   }
  ]
 }
}
```

  3. Ensure that the instance has either a public IP address or a service gateway, as described in the [prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).


## Managing the Compute Instance Monitoring Plugin 🔗 
For an instance to emit the compute instance metrics, the Compute Instance Monitoring plugin must be enabled on the instance and plugins must be running.
If you want to temporarily prevent the instance from emitting compute instance metrics, you can disable the Compute Instance Monitoring plugin. You can also stop all of the plugins that run on the instance, including the Compute Instance Monitoring plugin.
**Caution** Functionality that depends on the plugin, such as monitoring and autoscaling, does not work when the plugin is disabled or stopped.
For more information about how to enable and run plugins, see [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
## Troubleshooting: Finding Out if Monitoring Has Your Metrics 🔗 
To determine whether Monitoring is receiving the compute instance metrics, you can either query the instance metrics, or view the instance properties to confirm that the Compute Instance Monitoring plugin is enabled and running.
[Using the Console: To find out whether Monitoring is receiving metrics by querying instance metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in. 
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_computeagent**.
If you see metric charts with data, then the Monitoring service is receiving metrics from this instance. For more information about these metrics, see [Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics).
If you see a message that monitoring is not enabled, or that the Oracle Cloud Agent software needs to be installed, then complete those tasks.


[Using the Console: To find out whether the Compute Instance Monitoring plugin is enabled and running](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Oracle Cloud Agent** tab.
  4. Confirm that the Compute Instance Monitoring plugin is enabled, and all plugins are running.


[Using the API: To find out whether Monitoring is receiving metrics by querying instance metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
Use the [SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData) API operation. If metrics are returned, it indicates that the Monitoring service is receiving metrics from the instance.
[Using the API: To find out whether the Compute Instance Monitoring plugin is enabled and running](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
Use the [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance) operation (or [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation, for multiple instances).
In the response, if the `agentConfig` object returns the following values, it indicates that the Compute Instance Monitoring plugin is enabled and all plugins are running.```
{
 "agentConfig": {
  "isMonitoringDisabled": false,
  "areAllPluginsDisabled": false,
  "pluginsConfig": [
   {
    "name": "Compute Instance Monitoring",
    "desiredState": "ENABLED"
   }
  ]
 }
}
```

[Not seeing metrics for your instance?](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
If you don't see any metric charts, the instance might not be emitting metrics. See the following possible causes and resolutions.
Possible cause | How to check | Resolution  
---|---|---  
The Compute Instance Monitoring plugin is disabled on the instance or plugins are stopped. | Review the instance properties. | [Enable the Compute Instance Monitoring plugin and start all plugins](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).  
The instance can't access the Monitoring service because its VCN doesn't use the internet. | Review the instance's IP address. If it's not public, then a service gateway is needed.  | [Set up a service gateway](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).  
The instance doesn't use a supported image. | Review the [supported images](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).  | Create an instance with a [supported image](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).  
Older images and custom images: No Oracle Cloud Agent software exists on the instance.  | Connect to the instance and look for the software. | [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent).  
Something else is wrong with the Oracle Cloud Agent software. | (not applicable) | [Follow the troubleshooting steps for Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm).  
Was this article helpful?
YesNo

