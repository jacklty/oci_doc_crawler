Updated 2024-03-22
# Enabling the Block Volume Management Plugin
Enable the Block Volume Management plugin on a Compute instance.
The Block Volume Management plugin is required for the following volume attachment scenarios:
  * iSCSI attached volumes configured for the **Ultra High Performance** level. These volume attachements need to be multipath-enabled to achieve the optimized performance available with the **Ultra High Performance** level. 
  * iSCSI attached volumes configured for other performance levels and configured to automatically connect. These volumes were attached with the **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** option selected, and is supported for attachments to Linux and Windows-based instances. The following table lists the available version of the Oracle Cloud Agent software for the different operating systems:
Operating systems and corresponding Oracle Cloud Agent versions OS | Oracle Cloud Agent version  
---|---  
Oracle Linux or a custom image based on an Oracle Linux image | 1.23.0 or newer  
Windows or a custom image based on a Windows image | 1.24.0 or newer  
Ubuntu or a custom image based on an Ubuntu image | 1.35.0 or newer  


The Block Volume Management plugin is managed by the Oracle Cloud Agent software and performs the following actions:
  1. Checks the instance's metadata for multipath-enabled attachments to **Ultra High Performance** volumes or attachments configured to automatically connect to volumes configured for other performance levels, with a polling interval of one minute.
  2. Installs `device-mapper-multipath rpm` and adds `"/etc/multipath.conf"` only if there are multipath-enabled attachments.
  3. If there are multipath-enabled attachments or attachments configured to automatically connect in the instance's metadata, then the plugin performs batch iSCSI `login` commands for the volume attachments.


## Prerequisites 🔗 
The Block Volume Management plugin is supported on Oracle Autonomous Linux and Oracle Linux images, and on custom images that are based on those images.
The following steps are required for the Block Volume Management plugin.
  * **Service gateways or public IP addresses** : The compute instance must have either a public IP address or a service gateway to be able to connect to Oracle services.
If the instance does not have a public IP address, set up a service gateway on the virtual cloud network (VCN). The service gateway lets your instance privately access Oracle services without exposing the data to the public internet. Here are special notes for setting up the service gateway for the Block Volume Management plugin: 
    * When creating the service gateway, enable the service label called **All <region> Services in Oracle Services Network**.
    * When setting up routing for the subnet that contains the instance, set up a route rule with **Target Type** set to **Service Gateway** , and the **Destination Service** set to **All <region> Services in Oracle Services Network**.
For detailed instructions, see [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
  * **Oracle Cloud Agent** : The Oracle Cloud Agent software must be installed on the instance. Oracle Cloud Agent is installed by default on current platform images. For steps to manually install Oracle Cloud Agent on older images, see [Installing the Oracle Cloud Agent Software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent). To update, see [Updating the Oracle Cloud Agent Software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#update-agent). 
**Important** If you're enabling the Block Volume Management plugin to support the automatically connect to a volume scenario, the instance must be running version 1.23.0 or newer of the Oracle Cloud Agent software.
  * **Configure Permissions** : These permissions authorize the instance to make API calls to Oracle Cloud Infrastructure services, allowing the Block Volume Management plugin to report the iSCSI setup results for multipath-enabled iSCSI attachments.
To configure permissions:
    1. **Create Dynamic Group** : Create a dynamic group with the matching rules in the following code sample, to include all instances in the specified compartments:
Copy
```
ANY {instance.compartment.id = 'ocid1.tenancy.oc1..<tenancy_ID>', instance.compartment.id = 'ocid1.compartment.oc1..<compartment_OCID>'}
```

    2. **Configure Policy for Dynamic Group** : Configure a policy granting permissions to the dynamic group created in the previous step to enable the instance agent access to call the Block Volume service to retrieve the attachment configuration.:
Copy
```
Allow dynamic-group InstantAgent to use instances in tenancy
Allow dynamic-group InstantAgent to use volume-attachments in tenancy
```



## Enabling Block Volume Management on New Instances 🔗 
To enable Block Volume Management on a new compute instance, use the following steps.
[To enable Block Volume Management on a new compute instance using the Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
  1. Follow the steps in [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm), until the advanced options. Ensure that the instance has either a public IP address or a service gateway, as described in the [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq).
  2. Click **Show Advanced Options**.
  3. On the **Oracle Cloud Agent** tab, select the **Block Volume Management** check box.
  4. Click **Create**.


[To enable Block Volume Management on a new compute instance using the API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), if it is not already installed.
  2. Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation. Include the following parameters:
Copy
```
#oci compute instance update --instance-id <New_Instance> --agent-config file:///agentUpdate.json
agentUpdate.json
{
  "is-agent-disabled": false,
  "plugins-config": [
    {"name": "Block Volume Management", "desiredState": "ENABLED" }
  ]
}
```

  3. Ensure that the instance has either a public IP address or a service gateway, as described in the [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq).


## Enabling Block Volume Management on Existing Instances 🔗 
To enable Block Volume Management on an existing compute instance, use the following steps.
[To enable Block Volume Management on an existing compute instance using the Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), if it is not already installed. The Oracle Cloud Agent should already be installed all current and most recent platform images. Run the following command to check if it's already installed:
```
systemctl status oracle-cloud-agent
```

If the result is not found, you need to install the softare, otherwise proceed to the next step.
  2. [Enable the Block Volume Management plugin](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#disable-one-plugin).
  3. [Confirm that plugins are running on the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#turn-on-all-plugins).
  4. Ensure that the instance has either a public IP address or a service gateway, as described in [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq).


[To enable Block Volume Management on an existing compute instance using the API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent), if it is not already installed.
  2. Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation. Include the following parameters:
Copy
```
#oci compute instance update --instance-id <New_Instance> --agent-config file:///agentUpdate.json
agentUpdate.json
{
  "is-agent-disabled": false,
  "plugins-config": [
    {"name": "Block Volume Management", "desiredState": "ENABLED" }
  ]
}
```

  3. Ensure that the instance has either a public IP address or a service gateway, as described in [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq).


## Manually Enabling Block Volume Management on an Instance 🔗 
You can manually enable Block Volume Management on a compute instance using the CLI.
This procedure is only required for custom images that have been updated to support the **Ultra High Performance** level, but the Block Volume Management plugin has not been enabled in the `/etc/oracle-cloud-agent/agent.yml` file.
Prior to performing this procedure, you need to complete the steps described in [Enabling Block Volume Management on New Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-newinstances) or [Enabling Block Volume Management on Existing Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-existinginstances).
[To manually enable the Block Volume Management plugin on an instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
  1. [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent) on the instance, if it is not already installed.
  2. Log into the instance, see [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
  3. Run the following `sed` script to enable Block Volume Management:
Copy
```
sed -i.saved -e '/^ oci-blockautoconfig:/,/^ [a-z]*:/{s/\(.*disabled:.*\)true/\1false/}' /etc/oracle-cloud-agent/agent.yml
```

This script updates the `disabled` parameter for the `oci-blockautoconfig` configuration in `/etc/oracle-cloud-agent/agent.yml` from `true` to `false`.
  4. Run the following command to restart the Oracle Cloud Agent service:```
systemctl restart oracle-cloud-agent.service
```



## Troubleshooting the Block Volume Management Plugin 🔗 
If the Block Volume Management plugin is not configured correctly for an instance, you may encounter an error when attaching a volume with an iSCSI attachement type. See the troubleshooting suggestions in this section for these issues.
[Block Volume Management Plugin Log Error: Volume Attachment Not Authorized or Not Found Error](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
If you have not configured permissions correctly for the Block Volume Management plugin, the volume will fail to attach to the instance.
#### Details
The volume will not show up as attached in the Console and you will see a `NotAuthorizedOrNotFound` error message in the Block Volume Management plugin log.
The Block Volume Management plugin log is located in:
```
"/var/log/oracle-cloud-agent/plugins/oci-blockautoconfig/oci-blockautoconfig.log
```

The following is an sample error log entry for this issue:
```
2021/08/13 09:14:25.864932 compute_client_command.go:255: Updating volume attachment to the state LOGIN_SUCCEEDED ...
2021/08/13 09:14:26.155473 compute_client_command.go:260: Service error:NotAuthorizedOrNotFound.
volume attachment ocid1.volumeattachment.oc1.iad.<volume-attachment_ID> not found.
http status code: 404. Opc request id: <request_ID>
```

#### Cause
The Block Volume Management plugin does not have sufficent permissions to send the iSCSI login status notification to the service.
#### Resolution
To configure permissions for the Block Volume Management plugin:
  1. **Create Dynamic Group** : Create a dynamic group with the matching rules in the following code sample, to include all instances in the specified compartments:
```
ANY {instance.compartment.id = 'ocid1.tenancy.oc1..<tenancy_ID>', instance.compartment.id = 'ocid1.compartment.oc1..<compartment_OCID>'
```

  2. **Configure Policy for Dynamic Group** : Configure a policy granting permissions to the dynamic group created in the previous step to enable the instance agent access to call the Block Volume service to retrieve the attachment configuration.:
```
Allow dynamic-group InstantAgent to use instances in tenancy
Allow dynamic-group InstantAgent to use volume-attachments in tenancy
```



[Block Volume Management Plugin Log Error: User Agent Can Not Be Blank](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)
The compute instance must have either a public IP address or a service gateway to be able to connect to Oracle services or the volume will fail to attach.
#### Details
The volume will not show up as attached in the Console and you will see a `user agent can not be blank` error message in the Block Volume Management plugin log.
The Block Volume Management plugin log is located in:
```
"/var/log/oracle-cloud-agent/plugins/oci-blockautoconfig/oci-blockautoconfig.log
```

The following is an sample error log entry for this issue:
```
2021/10/15 22:16:07.881953 compute_client_command.go:255: Updating volume attachment to the state LOGIN_SUCCEEDED ...
2021/10/15 22:16:07.882185 compute_client_command.go:260: user agent can not be blank
2021/10/15 22:16:07.882204 iscsi_commands_helper.go:302: user agent can not be blank
2021/10/15 22:16:07.882212 iscsi_commands_helper.go:310: user agent can not be blank
```

#### Cause
The Block Volume Management plugin cannot send the iSCSI login status notification to the service due to the network configuration.
#### Resolution
If the instance does not have a public IP address, set up a service gateway on the virtual cloud network (VCN). The service gateway lets your instance privately access Oracle services without exposing the data to the public internet. Here are special notes for setting up the service gateway for the Block Volume Management plugin: 
  * When creating the service gateway, enable the service label called **All <region> Services in Oracle Services Network**.
  * When setting up routing for the subnet that contains the instance, set up a route rule with **Target Type** set to **Service Gateway** , and the **Destination Service** set to **All <region> Services in Oracle Services Network**.


For detailed instructions, see [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
Was this article helpful?
YesNo

