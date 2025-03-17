Updated 2025-02-28
# Oracle Cloud Agent
Oracle Cloud Agent is a lightweight process that manages plugins running on compute instances. Plugins collect performance metrics, install OS updates, and perform other instance management tasks.
To use plugins on an instance, the Oracle Cloud Agent software must be installed on the instance, the plugins must be enabled, and the plugins must be running. You might need to perform additional configuration tasks before you can use certain plugins.
## Supported Images 🔗 
**Oracle Cloud Agent:** Oracle Cloud Agent is supported on current [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images) and on [custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI) that are based on current platform images. Oracle Cloud Agent is installed by default on current platform images.
If you use an older platform image, you must manually install the Oracle Cloud Agent software. Select an image dated after November 15, 2018 (except Ubuntu, which must be dated after February 28, 2019).
You might have success manually installing Oracle Cloud Agent on other images, though it has not been tested on other operating systems and there is no guarantee that it will work.
**Plugins:** Plugins are installed as part of Oracle Cloud Agent. The plugins that are supported for an instance depend on the [version of Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#Oracle_Cloud_Agent_software_versions) and on the image that you use to create the instance. To determine which plugins are supported for a particular image, use the Console to create an instance. Or, use the [ListInstanceagentAvailablePlugins](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/Plugin/ListInstanceagentAvailablePlugins) API operation, providing the OS name and OS version of the image.
**Note** On Arm-based OCI Ampere A1 Compute shapes, the Custom Logs Monitoring plugin is not supported.
## Available Plugins 🔗 
Each Oracle Cloud Agent plugin provides functionality related to compute instances. This functionality can enable features that are part of the Compute service, and features that are part of other services.
The following Oracle Cloud Agent plugins are available.
Plugin Name | Description | Steps to Configure and Use  
---|---|---  
`Bastion` | Allows secure shell (SSH) connections to an instance without public IP addresses using the Bastion service. | See [Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm).  
`Block Volume Management` | Configures Block Volume sessions for the instance. | See [Enabling the Block Volume Management Plugin](https://docs.oracle.com/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm) and [Attaching Ultra High Performance Volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm#multipath).  
`Compute Instance Monitoring` | Emits metrics about the instance's health, capacity, and performance. These metrics are consumed by the Monitoring service. | See [Enabling Monitoring for Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) and [Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics).  
`Compute Instance Run Command` | Runs scripts within the instance to remotely configure, manage, and troubleshoot the instance. | See [Running Commands on an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm#runningcommands).  
`Cloud Guard Workload Protection` | Allows you to manually manage updates to the Instance Security agent if you are running a custom image which doesn't have Oracle Cloud Agent (OCA) enabled. | See [Manually Updating the Instance Security Agent](https://docs.oracle.com/iaas/cloud-guard/using/cgis-update-agent.htm).  
`Custom Logs Monitoring` | Ingests custom logs into the Logging service. | See [Custom Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs.htm).  
`High Performance Computing` | Performs complex calculations and processes data faster than traditional Compute. | See [High Performance Computing](https://docs.oracle.com/en-us/iaas/Content/Compute/References/high-performance-compute.htm#high-performance-compute "High Performance Computing \(HPC\) performs complex calculations and processes data faster than traditional Compute. HPC uses bare metal servers, ultralow latency cluster networking, high-performance storage options, and parallel file systems. This infrastructure enables parallel processing for compute-intensive workloads such as artificial intelligence, deep learning, data analysis, scientific simulations, and any other highly intensive workload.").  
`Management Agent` | Collects data from resources such as OSs, applications, and infrastructure resources for Oracle Cloud Infrastructure services that are integrated with Management Agent. Data can include observability, log, configuration, capacity, and health data. | See [Deploy Management Agents on Compute Instances](https://docs.oracle.com/iaas/management-agents/doc/management-agents-oracle-cloud-agent.html).  
`Oracle Autonomous Linux` | Manages autonomous updates and collects data associated with events, including logs and stack traces, for instances managed by the Autonomous Linux service.  | See [Oracle Autonomous Linux](https://docs.oracle.com/iaas/os-management/osms/alx-index.htm).  
`Oracle Java Management Service` | Monitors Java deployments on instances managed by the Java Management service. | See [Java Management](https://docs.oracle.com/iaas/jms/index.html).  
`OS Management Hub Agent` | Manage and monitor updates and patches for the operating system environment on the instance. | See [Registering an Instance with OS Management](https://docs.oracle.com/iaas/osmh/doc/register-oci-instance.htm).  
`OS Management Service Agent` | Manage and monitor updates and patches for the operating system environment on the instance. | See [OS Management](https://docs.oracle.com/iaas/os-management/home.htm).  
`Vulnerability Scanning` | Scans the instance for potential security vulnerabilities like OS packages that require updates. | See [Scanning Overview](https://docs.oracle.com/iaas/scanning/using/overview.htm).  
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to enable and disable individual plugins, as well as start and stop all plugins on an instance. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only `manage instance-family`, and remove the statements involving `volume-family` and `virtual-network-family`. In addition, you must use the following policy to allow users to access the available plugins:
Copy
```
Allow group PluginUsers to read instance-agent-plugins in compartment ABC
```

If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
## Installing the Oracle Cloud Agent Software 🔗 
**Note** If you create an instance using a current platform image or a custom image that is based on a current platform image, then Oracle Cloud Agent is installed by default. No action is needed.
To manually install the Oracle Cloud Agent software on an instance that uses another supported image, use one of the following procedures appropriate to the operating system.
[To manually install Oracle Cloud Agent on a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.").
  2. To download the Oracle Cloud Agent software, do one of the following things.
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
    1. To determine whether the Oracle Cloud Agent software is installed, run one of the following commands. On Oracle Linux:
Copy
```
sudo yum info oracle-cloud-agent
```

On Oracle Linux Cloud Developer:
Copy
```
rpm -qa | grep oracle-cloud-agent
```

The command returns the Oracle Cloud Agent version that is currently installed.
    2. If Oracle Cloud Agent isn't installed, or if the installed version is not the [latest version](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#Oracle_Cloud_Agent_software_versions), install the latest version by running the following command:
Copy
```
sudo yum install -y oracle-cloud-agent
```

**Note**
If you don't have access to the yum repository that has Oracle Cloud Agent, obtain the Oracle Cloud Agent installation file by [contacting support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
[CentOS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
To obtain the Oracle Cloud Agent installation file, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). Save the Oracle Cloud Agent installation file to the instance.
[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
**Note**
To install Oracle Cloud Agent on instances that use Ubuntu images, [Snapcraft](https://snapcraft.io/) must be installed on the instance. Install Snapcraft by running the following commands, in sequence:
Copy
```
sudo apt update
```

Copy
```
sudo apt install snapd
```

Copy
```
sudo snap install oracle-cloud-agent --classic
```

This command installs and runs the Oracle Cloud Agent software.
  3. To run the Oracle Cloud Agent software on the instance, enter one of the following commands.
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
sudo yum install -y <instance-agent-filename>
```

[CentOS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
sudo yum install -y <instance-agent-filename>
```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
No further action is needed. The command in the previous step installs and runs the software.


[To manually install Oracle Cloud Agent on a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. To obtain the Oracle Cloud Agent installation file, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  2. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.").
  3. Save the Oracle Cloud Agent installation file to the instance.
  4. As a user with administrative privileges, enter the following command to run the Oracle Cloud Agent software on the instance.
Copy
```
msiexec /qb /i <instance-agent-filename>
```



[To install Oracle Cloud Agent using cloud-init when creating an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
If you want to install Oracle Cloud Agent on an instance that uses an older image as part of the instance launch, you can provide a cloud-init script (cloudbase-init on Windows instances) when you create the instance.
  1. Obtain the Oracle Cloud Agent installation file. Do one of the following things, depending on the image:
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
If you have access to the yum repository that has Oracle Cloud Agent, proceed to the following step. If you don't have access to the yum repository, obtain the Oracle Cloud Agent installation file by [contacting support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
[CentOS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Obtain the Oracle Cloud Agent installation file by [contacting support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Proceed to the following step.
[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Obtain the Oracle Cloud Agent installation file by [contacting support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  2. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the advanced options.
  3. Click **Show advanced options**.
  4. On the **Management** tab, in the **Initialization script** section, select **Paste cloud-init script**. Then, copy and paste one of the following scripts, depending on the image.
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
sudo yum install -y oracle-cloud-agent
```

**Note**
If you don't have access to the yum repository that has Oracle Cloud Agent, paste the following script.
[Cloud-init script for Oracle Linux instances without access to yum repository](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
#!/bin/sh
curl -O <URL/to/installation_file.rpm> -v
yum install -y ~/<installation_file.rpm> -v
```

<URL/to/installation_file.rpm> is the URL of the Oracle Cloud Agent installation file provided by Oracle support.
<installation_file.rpm> is the filename of the installation file.
[CentOS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
#!/bin/sh
curl -O <URL/to/installation_file.rpm> -v
yum install -y ~/<installation_file.rpm> -v
```

<URL/to/installation_file.rpm> is the URL of the Oracle Cloud Agent installation file provided by Oracle support.
<installation_file.rpm> is the filename of the installation file.
[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
**Note**
To install Oracle Cloud Agent on instances that use Ubuntu images, [Snapcraft](https://snapcraft.io/) must be installed on the instance. Install Snapcraft by running the following commands, in sequence:
Copy
```
sudo apt update
```

Copy
```
sudo apt install snapd
```

Copy
```
sudo snap install oracle-cloud-agent --classic
```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Copy
```
#ps1_sysnative
md c:\temp
cd \temp
Invoke-WebRequest -Uri "<URL/to/installation_file.msi>" -OutFile "c:\temp\OracleCloudAgentSetup.msi"
msiexec /i "c:\temp\OracleCloudAgentSetup.msi" /quiet /L*V "c:\temp\OracleCloudAgentSetup.log"
```

<URL/to/installation_file.msi> is the URL of the Oracle Cloud Agent installation file provided by Oracle support.
**Note** For legacy versions of Windows images, ensure that cloudbase-init is supported. See [WinRM and cloudbase-init on Windows images](https://docs.oracle.com/iaas/releasenotes/changes/595afbb7-de0c-4934-8074-5b1ed6be1b56/).
  5. Click **Create**.


## Managing Plugins Using the Console 🔗 
[To see which plugins are enabled for an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Oracle Cloud Agent** tab.
The list of plugins is displayed. Enabled plugins can have the following statuses:
     * `RUNNING`: The plugin is running.
     * `STOPPED`: The plugin is stopped.
     * `NOT_SUPPORTED`: The plugin is not supported on this platform.
     * `INVALID`: The plugin status is not recognizable by the service.


[To enable or disable a plugin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Oracle Cloud Agent** tab.
  4. Toggle the **Enabled** or **Disabled** switch for the plugin.
**Caution** Functionality that depends on the plugin, such as monitoring, autoscaling, or OS management, will not work when the plugin is disabled.
It takes up to 10 minutes for the change to take effect.
  5. If you enabled a plugin, if necessary, perform any configuration tasks that are required before you can use the plugin. For information about how to configure each plugin, see the documentation for each plugin in [Available Plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#available-plugins).


[To stop all plugins on an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
You can stop all of the plugins that are running on an instance. Any individual plugins that are enabled on the instance remain enabled, but the plugin processes stop running. The plugin processes will only start running again after you restart all plugins.
For example, if you want to troubleshoot plugins, you can stop all plugins and then disable the plugins that you think might have an error. Reenable the plugins one-by-one, restarting the plugins after you enable each plugin, to determine which plugin has an issue. For more information about troubleshooting plugins, see [Troubleshooting Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#troubleshoot).
To stop all plugins on an instance:
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Oracle Cloud Agent** tab.
  4. Click **Stop plugins**.
**Caution** Functionality that depends on plugins, such as monitoring, autoscaling, and OS management, will not work when all plugins are stopped.
  5. Click **Stop plugins**.
It might take several minutes for all plugins to stop. Oracle Cloud Agent continues to run when plugins are stopped.


[To start all plugins on an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Oracle Cloud Agent** tab.
  4. Click **Start plugins**.
It takes up to 10 minutes for the plugins to restart.


## Managing Plugins Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage Oracle Cloud Agent plugins:
  * In the Core Services API:
    * [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) - enables or disables plugins, or stops all plugins, when you create an instance.
    * [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance) and [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) - gets information about which plugins are enabled on an instance (or a list of instances).
    * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) - enables or disables individual plugins, and stops or starts all plugins, for an existing instance.
  * In the Oracle Cloud Agent API:
    * [ListInstanceagentAvailablePlugins](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/Plugin/ListInstanceagentAvailablePlugins) - lists the plugins that are available for all instances. You can filter the results based on the image that you plan to use to launch an instance.
    * [ListInstanceAgentPlugins](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/Plugin/ListInstanceAgentPlugins) - gets information about the plugins that are available on an existing compute instance.
    * [GetInstanceAgentPlugin](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/Plugin/GetInstanceAgentPlugin) - gets information about a specific plugin on an existing compute instance.


## Updating the Oracle Cloud Agent Software 🔗 
We recommend always running the latest version of the Oracle Cloud Agent software.
If the instance can access the internet, then no action is needed. Oracle Cloud Agent periodically checks for newer versions and installs the latest version when an update is available.
If the instance does not have access to the internet, then you must manually update the Oracle Cloud Agent software. For example, a compute instance cannot access the internet if it does not have a public IP address, internet gateway, or service gateway. In this situation, Oracle Cloud Agent cannot complete its checks for newer versions.
[To see which version of Oracle Cloud Agent is installed ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
[Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and then do one of the following things:
  * For Oracle Linux and CentOS, run the following command:
Copy
```
sudo yum info oracle-cloud-agent
```

  * For Oracle Linux Cloud Developer, run the following command:
Copy
```
rpm -qa | grep oracle-cloud-agent
```

  * For Ubuntu, run the following command:
Copy
```
snap info oracle-cloud-agent
```

  * For Windows, do one of the following things: 
    * In Control Panel, select **Programs and Features** and then find the version number provided for "Oracle Cloud Agent."
    * In PowerShell, run the following command:
Copy
```
Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -eq "Oracle Cloud Agent" }
```

Example output:
```
IdentifyingNumber : {exampleuniqueidentifer}
Name       : Oracle Cloud Agent
Vendor      : Oracle Corporation
Version      : 0.0.10.0
Caption      : Oracle Cloud Agent
```



[To manually update Oracle Cloud Agent on a compute instance ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Do one of the following things:
  * Temporarily allow the instance to access the internet so that Oracle Cloud Agent can update itself.
  * Redo [the installation steps](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), using the latest version.


### Oracle Cloud Agent Release Notes 🔗 
[Linux versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Version | Date | Changes  
---|---|---  
1.49.0 | February 13, 2025 |  Block Volume Management:
  * Resolves a bug that overrode iscsid.conf noop parameters, this fix reduces the chance of iscsid to stop responding

High Performance Computing:
  * Adds support to monitor and recover RDMA interfaces from bad states and track reconfigure events
  * Enables HPC plug-ins for Oracle Linux 9 and Rocky Linux 9
  * Adds fix to recover if client.p12 is zero length or corrupted
  * Adds fix to prevent panic on IPV6 node that don't have rdma_features json file
  * Updates shapes.json to latest version: 20250130-0.5.8

OS Management Service Agent
  * Supports Boostrapper image downloads in ONSR
  * Adds automatic upgrade for osmh-agent 

Cloud Guard Workload Protection:
  * Adds a rollback when a new version of the wlpagent installation fails
  * Adds a wlpagent reboot on Oracle Linux if the kernel-uek-devel package is installed or updated

WebLogic Management Service:
  * Adds a rollback when a new version of the wlpagent installation fails
  * Adds support for the admin server patch readiness check WebLogic 14.1.2 multi-node, with secured production mode enabled
  * Adds support for WebLogic 14.1.2 single node domain with secured production mode disabled
  * Adds fix to handle special characters when you use the WebLogic Scripting Tool

Oracle Java Management Service:
  * Adds feature to send status to JMS if it can't communicate with other OCI services
  * Adds support to detect EJBs in WebLogic
  * Fixes the data type for PID values `int -> long`

Oracle Management Agent:
  * Adds the detection of root owned files in `oci-managementagent` state directory to prevent upgrade failures
  * Sets a default FIPS on/off setting for new OCI realms

  
1.48.0 | January 8, 2025 |  Block Volume Management:
  * Improvements to more efficiently handle 32 UHP volume attachments

High Performance Computing:
  * Improves the reliability of the detection and delivery of RDMA Link Flap faults
  * Fixes issue that caused false positive RDMA link flap faults delivered from the OCI HPC Monitoring plugin
  * Fixes issue that impacted RDMA network connectivity during the OCA upgrade process
  * Improves the deserialization logic of GPUIDs in shapes.json

WebLogic Management Service:
  * Code hardening of functional aspects
  * Fixes the issue to use additional metadata for a scan after an action
  * Truncates job result message size sent to the service data plane if the size exceeds 4KB
  * Fixes for failed patching with Opatch error when the .patch_storage was missing patch information

Custom Logs Monitoring:
  * Adds enable-disable service check

OS Management Service Agent:
  * Supports Object Storage Private Endpoint
  * Bug fixes for when the binary failed to recover after a new install

Oracle Cloud Agent Updater:
  * Adds an "overrides" directory for setting overrides for the updater.yml to disable auto-updates

  
1.47.0 | November 6, 2024 | Monthly patches and bug fixes. OS Management Service Agent:
  * Improvements to error logging
  * Moving the plugin process out of cgroup/oca.slice for stability in first boot scenarios

High Performance Computing:
  * Adds H100 Fault Xid 62 for HPC plugin
  * Adds publishing of GPU faults as metrics to OCI Monitoring
  * Adds PCI device presence diagnostics per GPU
  * Updates logic to detect SRAM ECC fault code
  * Mellanox Device Name and PCIe address mapping now takes into account overrides to shapes.json

Runcommand:
  * Bug fixes to error logging

Oracle Java Management Service:
  * Bug fixes and enhancements

Weblogic Management Service:
  * Limited release of the WebLogic Management Service plugin v1.1

Cloud Guard Workload Protection:
  * Improves to "server unreachable" detection
  * Adds support for the WLP plugin to run load test mode

  
1.46.0 | October 10, 2024 |  Monthly patches and bug fixes. Runcommand:
  * Object storage incremental log upload for Full Stack Disaster Relief

OS Management Service Agent:
  * Bug fixes and enhancements

WebLogic Management Service:
  * Limited release support

Oracle Java Management Service:
  * Bug fixes and enhancements

Block Volume Management:
  * Autoconfig flushes only mpath of interest instead of all mpaths

High Performance Computing:
  * Bug fixes and enhancements

  
1.45.0 | September 13, 2024 |  Monthly patches and bug fixes. OS Management Service Agent:
  * Restores yum repository files upon failure

  
1.44.0 | August 8, 2024 | Oracle Java Management Service:
  * Bug fixes and enhancements for Oracle Java Management Service
  * Releases version JMS 9.0

Cloud Guard Workload Protection:
  * Fixes plugin for fatal logs

Compute RDMA GPU Monitoring:
  * Enables GPU fault metrics for MI300X
  * Adds the ability to set GPU clocks within the OCA plugin by adding a new GPU Configuration module within the HPC Configure plugin

Compute Instance Run Command:
  * Run command reverts to main endpoint fix

  
1.43.0 | July 11, 2024 | Monthly patches and bug fixes.Compute RDMA GPU Monitoring:
  * Updates shapes.json with mappings for H100T and L40S supporting NIC bifurcation

  
1.42.0 | June 10,2024 | Oracle Java Management Service:
  * Adds Oracle Java Management Service improvements and features for JMS 9.0

High Performance Computing:
  * Adds IPv6 Single Stack Compatibility Support

Compute RDMA GPU Monitoring:
  * Adds RDMA ID and Mellanox ID to the OCI RDMA metrics
  * Enables GPU metrics for MI300X
  * Updates shapes.json to allow ORAP support for MI300X, L40S and H100T

OS Management Hub Agent:
  * Cloud customers can now enable OS Management Hub Agent YUM/DNF plugin on every check in

  
1.41.0 | May 9, 2024 |  Compute RDMA GPU Monitoring:
  * Adds support for RDMA fault metrics
  * Enables GPU health and fault monitoring metric for Ubuntu

OS Management Hub Agent:
  * OS Management Hub Agent is now available for cloud customers

Oracle Cloud Agent:
  * Updates diagnostic tool path to /usr/libexec/oracle-cloud-agent/ocatools on OL/Ubuntu

  
1.40.0 | March 8, 2024 | Monthly patches and bug fixes.  
1.39.0 | February 12, 2024 | Monthly patches and bug fixes.  
1.38.0 | January 5, 2024 |  High Performance Computing:
  * Compute HPC RDMA Authentication fix to recover from failed reconfigure event.

Block Volume Management:
  * Sets fast_io_fail_tmo to off in multipath.conf.oca.

Management Agent:
  * Management Agent now supports ARM.

  
1.37.2 | October 3, 2023 |  Oracle Cloud Agent:
  * Organizes oracle-cloud-agent systemd service units into root level oca.slice.

Block Volume Management:
  * Applies plugin fix for UHP attachments.

Oracle Java Management Service:
  * Oracle Java Management Service 8.0 now available to all regions.

Management Agent:
  * Management Agent disables plugin bugfix and allows import of custom root CA.

  
1.36.0 | August 11, 2023 |  Oracle Java Management Service:
  * Updates Oracle Java Management Service install script.

Block Volume Management:
  * Applies tuning steps on BM.Standard.A1.160 shape for multipath attachments.

Compute Instance Monitoring
  * Added a new dimension, `dedicatedVmHostId`, to emitted metrics stream. 

  
1.35.0 | July 12, 2023 |  Management Agent:
  * Management Agent support for Oracle Linux 9.

Block Volume Management:
  * Block Volume Management support for Ubuntu.
  * Fixes formatting bug in logging. 

Oracle Java Management Service:
  * Configures custom log manager for Oracle Java Management Service. 

  
1.34.0 | June 14, 2023 |  Oracle Java Management Service:
  * Oracle Java Management Service 7.0 available to all regions.
  * Oracle Java Management Service plugin launcher script update.

  
1.33.0 | May 9, 2023 |  Block Volume Management:
  * Fixes auto-attach related bugs.
  * Updates polling sequence in Block Volume Management plugin. 

Oracle Java Management Service:
  * Upgrades Oracle Java Management Service to 7.0.

  
1.32.2 | April 6, 2023 |  Vulnerability Scanning:
  * Disables collection of filesystem metadata in Vulnerability Scanning when the app scan is not enabled.

Oracle Java Management Service:
  * Checks version of Java for Oracle Java Management Service plugin for non-headless/headful.
  * Updates the Oracle Java Management Service launcher to allow agent app to use jcmd and attach modules for Java Management Service plugin.

  
1.31.0 | March 14, 2023 | Monthly patches and bug fixes.  
1.30.0 | February 7, 2023 |  Compute Instance Run Command:
  * Mitigates limitation of supporting 128 MiB of command output for output that is uploaded to a pre-authenticated request URL.

Management Agent:
  * Prevents startup attempts when Management Agent gets into a known bad state.

Oracle Java Management Service:
  * Fixes the Oracle Java Management Service launcher script for Oracle Linux 6.
  * Adds fixes for JDK Flight Recorder (JFR) feature of Java Management Service.

  
1.29.0 | December 28, 2022 |  Custom Logs Monitoring:
  * Adds support for instances with Arm-based processors.

Oracle Autonomous Linux:
  * Sets the default Unbreakable Enterprise Kernel (UEK) channel to UEK Release 7 on Oracle Autonomous Linux 8.

Oracle Java Management Service:
  * Upgrades Oracle Java Management Service to version 6.0.

OS Management Service Agent:
  * Adds support for FIPS mode on Oracle Linux 8 for instances with Arm-based processors.

  
1.28.0 | November 10, 2022 |  Compute Instance Run Command:
  * Addresses multiform uploads using pre-authenticated requests.

OS Management Service Agent:
  * Disables DNF syslog.

  
1.27.0 | September 8, 2022 |  Adds fixes for the Oracle Cloud Agent diagnostic tool. Custom Logs Monitoring:
  * Verify the Unified Monitoring Agent is stopped before issuing a `systemctl` start.

Oracle Java Management Service:
  * Adds JDK repository check.

OS Management Service Agent:
  * Adds support for FIPS mode on Oracle Linux 8 for instances with x86_64 processors (AMD and Intel).
  * Fixes managed instance display name.

Vulnerability Scanning:
  * Qualys agent stop fix.
  * Fixes the disk fillup issue by Vulnerability Scanning app scan.

  
1.26.0 | August 3, 2022 |  Block Volume Management:
  * Adds support for Oracle Linux 9.

Oracle Java Management Service:
  * Plugin release version 5.0.122.
  * Adds support for Oracle Linux 9.

OS Management Service Agent:
  * Bug fixes.

Vulnerability Scanning:
  * Adds vendor settings with Object Storage and vendor stop fixes.

Ubuntu instances only:
  * Adds support for the diagnostic tool.

  
1.25.0 | July 7, 2022 |  Bastion:
  * Make Bastion plugin handle `%h` and `%u` in sshd_config file.

Oracle Autonomous Linux:
  * Updates to avoid deadlock.

OS Management Service Agent:
  * Updates to avoid deadlock.

Vulnerability Scanning:
  * Appscan fixes.

  
1.24.0 | June 8, 2022 |  Compute Instance Run Command:
  * Fix runcommand npe when poll response is null.
  * Added support for "shell" at the deployment spec and individual step levels in code deploy.

Vulnerability Scanning:
  * Qualys agent update, installation and enabling workflow and use vss-tools for appscan.

  
1.23.0 | May 5, 2022 |  Bastion:
  * Change to created authorized key file to the owner of the homedir.

Block Volume Management:
  * Supports auto attach of single path volumes.

Oracle Autonomous Linux:
  * Increases the oops zip size limit.

OS Management Service Agent:
  * Fixes osms-work-request endpoint in the SDK for Go.

Vulnerability Scanning:
  * Adds qualys installer and changes to switch between Vulnerability Scanning and Qualys agents.
  * Adds syft scan tool for Vulnerability Scanning and adds skeleton of Vulnerability Scanning tools binary.
  * Restricts Vulnerability Scanning jarscan copied file permission to `oca` user read-only.

  
1.22.0 |  March 31, 2022 |  Oracle Autonomous Linux:
  * Enhancements for migration and notification.

Oracle Java Management Service:
  * Initial release.

Vulnerability Scanning:
  * Emits more jarscan time metrics.

  
1.21.0 | March 2, 2022 |  Management Agent:
  * Fix for converting package type.

Oracle Autonomous Linux:
  * Bug fixes and enhancements for resilience to outage.

Vulnerability Scanning:
  * Provide fast jar scan using shell script to reduce resource overhead and time.
  * Removed disk metadata from hot path of scanning and collecting it in parallel execution.

  
1.20.0 | February 2, 2022 |  Oracle Autonomous Linux:
  * Fixes a race condition.

Vulnerability Scanning:
  * Adds plugin slower mode for reading whole disk using sudo.

Ubuntu instances only:
  * Bug fixes.

  
1.19.0 | January 6, 2022 |  Custom Logs Monitoring:
  * Removes read of redundant versionInfo.yml and upgrades only when agent version is higher.

Oracle Autonomous Linux:
  * Updates for Autonomous Linux migration, channel handling, and OOPS processing.

OS Management Service Agent:
  * Fixes Python 3 subprocess output decoding.

Vulnerability Scanning:
  * Updates ScanJavaPkgs to mitigate Log4j vulnerability.

  
1.18.0 | December 6, 2021 |  Bastion:
  * Bug fix for similar usernames.

Oracle Autonomous Linux:
  * Updates for yum update retry and oops upload retry.
  * Enabled in United Kingdom Government Cloud.

Ubuntu instances only:
  * Bug fixes.

  
1.17.0 | November 19, 2021 |  The Oracle Cloud Agent version now adheres to the Semantic Versioning Specification (semver). When the monitoring client fails to construct during start, the gomon command-line utility is now able to recover. Oracle Autonomous Linux:
  * Adds fixes to ignore false alarms.
  * Reduces startup time.
  * Adds a health check.

  
1.16.0 | October 20, 2021 |  OS Management Service Agent:
  * Adds support for Oracle Linux 8.x.
  * Adds support for cleaning up data storage for inactive native agents.

Oracle Autonomous Linux:
  * Adds support for custom configurations.
  * Removes `soscleaner` and Oracle Ksplice sudo access to master.

Compute Instance Run Command:
  * Fixes an environment variable bug.

Changes the ownership of the `agent.yml` configuration file to support upgrades.  
1.15.0 | September 21, 2021 | Adds support for the OS Management Service Agent plugin with Arm-based shapes running Oracle Linux.  
1.14.2 | September 2, 2021 | Adds support for the Oracle Autonomous Linux plugin.  
1.14.0 | August 20, 2021 |  The [diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic) is now included in the release package. OS Management Service Agent:
  * Adds support for automatically enabling the resource discovery and monitoring feature with a new policy.

  
1.13.0 | July 1, 2021 |  Adds support for Arm-based shapes running Oracle Linux for the following plugins:
  * Bastion
  * Block Volume Management
  * Compute Instance Run Command
  * Vulnerability Scanning

Delays the update check on startup by one hour. Moves the instance agent service endpoint from `iaas` to `instance-agent`. OS Management Service Agent:
  * Adds support for custom CA certificates.

Vulnerability Scanning:
  * Updates the way RPM packages are queried.

  
1.12.0 | June 2, 2021 |  Bastion:
  * Fix to only create the control plane and data plane clients once and not on each iteration of the bastion workflow.

Block Volume Management:
  * Updated the plugin status to be running or stopped when it is running or stopped respectively.
  * Removed the default `/etc/multipath.conf` to avoid conflicts.
  * Improved the error message to report no volume attachments were found by the plugin.
  * Fixed a race condition by restarting the `multipathd` service.

Ubuntu instances only:
  * Miscellaneous updates.

  
1.11.4 | May 20, 2021 | Fixes an issue with the 1.11.0 and 1.11.1 updater not updating the Oracle Cloud Agent software.  
1.11.3 | May 14, 2021 | Miscellaneous updates.  
1.11.1 | May 3, 2021 |  Replaces the Python updater with a Golang updater. Initial release of the Bastion plugin.  
1.10.0 | April 7, 2021 |  Custom Logs Monitoring:
  * Added support for Ubuntu 16.04, 18.04, and 20.04.

OS Management Service Agent:
  * Added osmsx_ctl to manage a flag file in future Autonomous Linux releases.
  * Added FIPS Object Model to the OS Management Service Agent build.

Ubuntu instances only:
  * Added support for Custom Logs Monitoring.

  
1.9.0 | March 3, 2021 |  OS Management Service Agent:
  * OS Management process binds to port in ephemeral range.
  * Custom error handler for empty yum transactions.

  
1.8.3 | January 13, 2021 |  Ubuntu instances only:
  * Adds support to enable or disable individual plugins.
  * Adds two new metrics for monitoring.
  * Fix for updater start in new images.
  * Updater fix for signature verification on packages.
  * Adds support for reattachable plugins so that Oracle Cloud Agent can be upgraded without stopping plugins.

  
1.8.2 | January 13, 2021 |  Compute Instance Monitoring:
  * Improve filtering of UNIX disk devices.

  
1.8.1 | January 13, 2021 |  OS Management Service Agent:
  * Disabled by default.

  
1.8.0 | January 13, 2021 |  Adds support to enable or disable individual plugins. Adds two new metrics for monitoring. OS Management Service Agent:
  * Enabled by default.

  
1.7.1 | December 17, 2020 |  Fix for updater start in new images. OS Management Service Agent disabled in US Government Cloud.  
1.7.0 | December 7, 2020 |  Updater fix for signature verification on packages. Custom Logs Monitoring:
  * Bug fix for signature verification.
  * Add default bucket namespace for non-commercial realms.

  
1.6.0 | November 6, 2020 |  Adds support for reattachable plugins so that Oracle Cloud Agent can be upgraded without stopping plugins. Compute Instance Run Command:
  * Includes support for the run command feature in all regions in the Oracle Cloud Infrastructure commercial realm.

Custom Logs Monitoring:
  * Enables package signature verification in CentOS.

OS Management Service Agent:
  * Fixes the plugin to stop its process when it is requested to stop rather than staying up idle.
  * Fixes an upgrade kill cycle bug where OS Management upgrades Oracle Cloud Agent using yum, which then stops Oracle Cloud Agent, which stops the plugin.

  
1.5.1 | October 27, 2020 | Includes support for the run command feature.  
1.4.1 | October 21, 2020 | Hotfix for agent termination of orphaned processes.  
1.4.0 | October 2, 2020 |  Fixes in updater daemon and plugins to make them more resilient.  
1.3.2 | September 9, 2020 |  Fix auto update download directory permissions. Minor enhancements to the Compute Instance Monitoring plugin. Enable additional plugins. Create grpc sockets in /var/lib/oracle-cloud-agent/tmp.  
1.2.0 | August 3, 2020 | Upgrade the agent to support plugins  
0.0.19 | May 28, 2020 |  Fix updater failing to run on images that mount a filesystem with noexec flag set, to /tmp. Use instance metadata to generate client side URLs. Includes support for the instance metadata service (IMDS) v2.  
0.0.18 | May 11, 2020 | Miscellaneous updates.  
0.0.15 | January 15, 2020 | Migrate from Python 2.7.15 to Python 3.6.9.  
0.0.13 | November 4, 2019 | Fix a bug in handling monitoring service internal server errors.  
0.0.11 | September 13, 2019 | Fix retry strategy for sending metrics and refresh security tokens.  
0.0.10 | July 15, 2019 | Fix for correct handling of forced termination of the oracle-cloud-agent-updater.  
[Windows versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
Version | Date | Changes  
---|---|---  
1.49.0 | February 13, 2025 |  Block Volume Management:
  * Resolves a bug that overrode iscsid.conf noop parameters, this fix reduces the chance of iscsid to stop responding

OS Management Service Agent
  * Supports Boostrapper image downloads in ONSR
  * Adds automatic upgrade for osmh-agent 

Cloud Guard Workload Protection:
  * Adds a rollback when a new version of the wlpagent installation fails

  
1.48.0 | January 8, 2025 | OS Management Service Agent
  * Fixes issue where the binary failed to recover after a new install

Custom Logs Monitoring:
  * Fixes for handling multiple versions

  
1.47.0 | November 6, 2024 | Monthly patches and bug fixes.  
1.46.0 | October 10, 2024 | Monthly patches and bug fixes.  
1.45.0 | September 13, 2024 | Monthly patches and bug fixes.  
1.44.0 | August 8, 2024 | Cloud Guard Workload Protection:
  * Fixes for fatal logs
  * Windows machines will no longer register failure events in cases of IMDS being unreachable

Compute Instance Run Command:
  * Run command reverts to main endpoint fix

Custom Logs Monitoring:
  * Fixes for preventing auth config deletion

  
1.43.0 | July 11, 2024 | Monthly patches and bug fixes.Custom Logs Monitoring:
  * Resolves Unified Monitoring Agent uninstall issues

  
1.42.0 | June 10, 2024 | OS Management Service Agent
  * Resolves an issue on Windows last boot

  
1.41.0 | May 9, 2024 | Monthly patches and bug fixes.  
1.40.0 | March 8, 2024 | Monthly patches and bug fixes.  
1.39.0 | February 12, 2024 | Monthly patches and bug fixes.  
1.38.0 | January 5, 2024 | Monthly patches and bug fixes.  
1.37.2 | October 3, 2023 | Monthly patches and bug fixes.  
1.36.0 | August 11, 2023 |  Compute Instance Monitoring
  * Added a new dimension, `dedicatedVmHostId`, to emitted metrics stream 

  
1.35.0 | July 12, 2023 |  Block Volume Management:
  * Fixes formatting bug in logging. 

  
1.34.0 | June 14, 2023 | Monthly patches and bug fixes.  
1.33.0 | May 9, 2023 |  Block Volume Management:
  * Fixes auto-attach related bugs. 
  * Updates polling sequence in Block Volume Management plugin. 

  
1.32.2 | April 6, 2023 | Monthly patches and bug fixes.  
1.31.0 | March 14, 2023 | Monthly patches and bug fixes.  
1.30.0 | February 7, 2023 |  Compute Instance Run Command:
  * Mitigates limitation of supporting 128 MiB of command output for output that is uploaded to a pre-authenticated request URL.

  
1.29.0 | December 28, 2022 | Patches and bug fixes.  
1.28.0 | November 10, 2022 | Bug fixes.  
1.27.0 | September 8, 2022 |  Adds fixes for the Oracle Cloud Agent diagnostic tool. Vulnerability Scanning:
  * Qualys agent stop fix.

  
1.26.0 | August 3, 2022 |  Vulnerability Scanning:
  * Adds vendor settings with Object Storage and vendor stop fixes.

  
1.25.0 | July 7, 2022 |  Adds Qualys agent for Windows. Appscan fixes.  
1.24.0 | June 8, 2022 |  Block Volume Management:
  * Supports auto attach for block volumes.

Compute Instance Run Command:
  * Fix runcommand npe when poll response is null.

  
1.23.0 | May 5, 2022 | Bug fixes.  
1.22.0 | March 31, 2022 | Bug fixes.  
1.21.0 | March 2, 2022 | Bug fixes.  
1.20.0 | February 1, 2022 | Bug fixes.  
1.19.0 | January 6, 2022 |  Removes installer packages from diagnostic tool results. Custom Logs Monitoring:
  * Removes read of redundant versionInfo.yml and upgrades only when agent version is higher.

  
1.18.0 | December 6, 2021 | Bug fixes.  
1.17.2 | November 19, 2021 |  Fixes an OS Management Service Agent time-out bug.  
1.17.0 | November 19, 2021 |  The Oracle Cloud Agent version now adheres to the Semantic Versioning Specification (semver). When the monitoring client fails to construct during start, the gomon command-line utility is now able to recover.  
1.16.0 | October 20, 2021 |  Adds all Windows Server 2019 users to the [diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic). Fixes to the [diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic).  
1.15.0 | September 21, 2021 | Bug fixes.  
1.14.0 | August 20, 2021 |  The [diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic) is now included in the release package. Added support for the OS Management Service Agent self-test.  
1.13.0 | July 1, 2021 |  Delays the update check on startup by one hour. Moves the instance agent service endpoint from `iaas` to `instance-agent`. OS Management Service Agent:
  * Adds support for custom CA certificates.

  
1.12.0 | June 2, 2021 |  Block Volume Management:
  * Bug fixes.

Custom Logs Monitoring:
  * Use OS version fall back for Windows OS.

Vulnerability Scanning:
  * Bug fixes.

  
1.11.1 | May 20, 2021 | Fixes an issue with the 1.11.0 updater not updating the Oracle Cloud Agent software.  
1.11.0 | May 3, 2021 | Replaces the Python updater with a Golang updater.  
1.10.0 | April 7, 2021 |  Closes open handle for allocstall metric. OS Management Service Agent:
  * Additional logging on Windows.
  * Adds osmsx_ctl.

  
1.9.0 | March 3, 2021 | Bug fixes.  
1.8.0 | January 13, 2021 |  Adds support to enable or disable individual plugins. Adds two new metrics for monitoring. OS Management Service Agent:
  * Enabled by default.

  
1.7.1 | December 17, 2020 | All plugins disabled in US Government Cloud.  
1.7.0 | December 7, 2020 |  Updater fix for signature verification on packages. Compute Instance Run Command:
  * Enabled for Windows.

Custom Logs Monitoring:
  * Add default bucket namespace for non-commercial realms.

OS Management Service Agent:
  * Clean up leftover OS Management temporary directories due to OS Management being terminated on system reboot.

  
1.5.0.0 | November 6, 2020 |  Adds support for reattachable plugins so that Oracle Cloud Agent can be upgraded without stopping plugins. Custom Logs Monitoring plugin enabled in US Government Cloud realms.  
1.4.1.0 | October 2, 2020 |  Fixes in updater daemon and plugins to make them more resilient.  
1.3.0.0 | August 7, 2020 | Minor enhancements to the Compute Instance Monitoring plugin.  
1.2.0.0 | June 26, 2020 | Miscellaneous updates.  
1.0.0.0 | April 28, 2020 |  Includes all Microsoft patches as of April 24, 2020.  Includes a new version of the Oracle Cloud Agent with a plugin for Windows for the [OS Management service](https://docs.oracle.com/iaas/os-management/home.htm). Includes support for the instance metadata service (IMDS) v2.  
0.0.13.0 | January 15, 2020 | Fixed: Migrate from Python 2.7.15 to Python 3.6.9.  
0.0.11.0 | November 5, 2019 | Fixed: Fix a bug in handling monitoring service internal server errors.  
0.0.10.0 | September 13, 2019 |  Fixed: 
  * Fix retry strategy for sending metrics and refresh security tokens 
  * Fix for correct handling of forced termination of the oracle-cloud-agent-update 

  
0.0.9.0 | June 6, 2019 | Fixed: Bug fix where agent restarts when telemetry or auth service returns 5xx.  
## Troubleshooting 🔗 
For troubleshooting steps, see [Troubleshooting Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#troubleshoot).
## Uninstalling the Oracle Cloud Agent Software 🔗 
You can uninstall the Oracle Cloud Agent software from an instance. After you uninstall Oracle Cloud Agent, features that depend on Oracle Cloud Agent plugins are not available for the instance.
[To uninstall Oracle Cloud Agent from an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.").
  2. Run one of the following commands:
     * Oracle Linux and CentOS:
Copy
```
sudo yum remove oracle-cloud-agent
```

     * Ubuntu:
Copy
```
sudo apt-get remove oracle-cloud-agent
```

     * Windows:
Copy
```
$app = Get-WmiObject -Class Win32_Product -Filter "Name = 'Oracle Cloud Agent'"
>> $app.Uninstall(){}
```



Was this article helpful?
YesNo

