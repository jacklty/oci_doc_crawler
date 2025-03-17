Updated 2025-01-13
# Getting Instance Metadata
The instance metadata service (IMDS) provides information about a running instance, including a variety of details about the instance, its attached virtual network interface cards (VNICs), its attached multipath-enabled volume attachments, and any custom metadata that you define. IMDS also provides information to cloud-init that you can use for various system initialization tasks.
You can find some of this information in the Console on the **Instance Details** page, or you can get all of it by logging in to the instance and using the metadata service. The service runs on every instance and is an HTTP endpoint listening on 169.254.169.254. If an instance has multiple VNICs, you must send the request using the primary VNIC.
**Important** To increase the security of metadata requests, we strongly recommend that you update all applications to use the IMDS version 2 endpoint, if supported by the image. Then, disable requests to IMDS version 1.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Upgrading to the Instance Metadata Service v2 🔗 
The instance metadata service is available in two versions, version 1 and version 2. IMDSv2 offers increased security compared to v1.
When you disable IMDSv1 and allow requests only to IMDSv2, the following things change:
  * All requests must be made to the v2 endpoints (`/opc/v2`). Requests to the v1 endpoints (`/opc/v1` and `/openstack`) are rejected with a 404 not found error.
  * All requests to the v2 endpoints must include an authorization header. Requests that do not include the authorization header are rejected.
  * Requests that are forwarded using the HTTP headers `Forwarded`, `X-Forwarded-For`, or `X-Forwarded-Host` are rejected.


To upgrade the instance metadata service on a compute instance, use the following high-level steps:
  1. [Verify that the instance uses an image that supports IMDSv2](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2__supported-images).
  2. [Identify requests to the legacy v1 endpoints](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2__identify-requests).
  3. Migrate all applications to support the v2 endpoints.
  4. [Disable all requests to the legacy v1 endpoints](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2__disable-legacy).


### Supported Images for IMDSv2 🔗 
IMDSv2 is supported on the following [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images):
  * Oracle Autonomous Linux 8.x images
  * Oracle Autonomous Linux 7.x images released in June 2020 or later
  * Oracle Linux 8.x and Oracle Linux 7.x images released in July 2020 or later


Other platform images, most [custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image."), and most [Marketplace images](https://docs.oracle.com/iaas/Content/Marketplace/overview-marketplace.htm) do not support IMDSv2. Custom Linux images might support IMDSv2 if cloud-init is updated to version 20.3 or later and Oracle Cloud Agent is updated to version 0.0.19 or later. Custom Windows images might support IMDSv2 if Oracle Cloud Agent is updated to version 1.0.0.0 or later; cloudbase-init does not support IMDSv2.
### Identifying Requests to the Legacy IMDSv1 Endpoints 🔗 
To identify the specific IMDS endpoints that requests are being made to, and the agents that are making the requests, use the [InstanceMetadataRequests metric](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-management-metrics.htm#compute-management-metrics).
To identify which versions of IMDS are enabled for an instance, do either of the following things:
  * **Using the Console:**
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. In the **Instance Details** section, next to **Instance metadata service** , note the version numbers.
  * **Using the API:** Use the [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance) operation or the [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation. In the response, the `areLegacyImdsEndpointsDisabled` attribute in the `InstanceOptions` object returns `false` if both IMDSv1 and IMDSv2 are enabled for the instance. It returns `true` if IMDSv1 is disabled.


### Disabling Requests to the Legacy IMDSv1 Endpoints 🔗 
After you migrate all applications so that they make requests only to the IMDSv2 endpoints, you should disable all requests to the legacy IMDSv1 endpoints.
**Important** Verify that the instance does not use the IMDSv1 endpoints before you disable requests to IMDSv1. If the instance still relies on IMDSv1 when you disable requests to it, you might lose some functionality.
Do either of the following things:
  * **Using the Console:**
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. In the **Instance Details** section, next to **Instance metadata service** , click **Edit**.
    4. For **Allowed IMDS version** , select the **Version 2 only** option.
    5. Click **Save changes**.
  * **Using the API:** Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation. In the request body, in the `InstanceOptions` object, pass the value `true` for the `areLegacyImdsEndpointsDisabled` attribute.


**Note** If you disable IMDSv1 on an instance that does not support IMDSv2, you might not be able to connect to the instance when you launch it. To reenable IMDSv1: using the Console, on the Instance Details page, next to **Instance Metadata Service** , click **Edit**. Select the **Version 1 and version 2** option, save your changes, and then [restart the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions."). Using the API, use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation.
## Request Throttling 🔗 
Oracle Cloud Infrastructure applies throttling to instance metadata service requests to prevent accidental or abusive use of resources. To avoid throttling, instead of querying security credentials for every transaction, cache the credentials until they are near expiration.
If you make too many requests too quickly, you might see some succeed and others fail. If you are experiencing throttling, Oracle recommends that you retry using an exponential back-off.
## Getting Instance Metadata on Platform Images 🔗 
You can get instance metadata for platform images by using cURL on Linux instances. On Windows instances, you can use cURL (if supported by the Windows version) or an internet browser.
All requests to the instance metadata service v2 must include the following header:
Copy
```
Authorization: Bearer Oracle
```

Instance metadata accessed using IMDSv2 is available at the following root URLs:
  * All of the instance information:
Copy
```
http://169.254.169.254/opc/v2/instance/
```

  * Information about the VNICs that are attached to the instance:
Copy
```
http://169.254.169.254/opc/v2/vnics/
```

  * Information about a volume attached to the instance with multipath-enabled attachment:
Copy
```
http://169.254.169.254/opc/v2/volumeAttachments/
```



Instance metadata accessed using IMDSv1 is available at the following root URLs. No header is necessary.
  * All of the instance information:
Copy
```
http://169.254.169.254/opc/v1/instance/
```

  * Information about the VNICs that are attached to the instance:
Copy
```
http://169.254.169.254/opc/v1/vnics/
```

  * Information about a volume attached to the instance with multipath-enabled attachment:
Copy
```
http://169.254.169.254/opc/v1/volumeAttachments/
```



The values for [specific metadata keys](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#metadata-keys) are available as subpaths below the root URL.
### To get instance metadata for Linux instances 🔗 
  1. [Connect to a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") using SSH.
  2. Use cURL to issue a GET request to the instance metadata URL that you're interested in. For example:
Copy
```
curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/
```



### To get instance metadata for Windows instances 🔗 
The steps to get metadata on a Windows instance depend on which version of the instance metadata service you're requesting metadata from.
To get Windows instance metadata using IMDSv2:
  1. [Connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection.
  2. Depending on whether your Windows version includes cURL, do either of the following:
     * If your Windows version includes cURL, use cURL to issue a GET request to the instance metadata URL that you're interested in. For example:
Copy
```
curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/
```

     * If your Windows version does not include cURL, you can get instance metadata in your internet browser. Navigate to the instance metadata URL that you're interested in, and pass a request that includes the authorization header. See the instructions for your browser for more information about including headers in a request. You might need to install a third-party browser extension that lets you include request headers.


To get Windows instance metadata using IMDSv1:
  1. [Connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection.
  2. Open an internet browser and then navigate to the instance metadata URL that you're interested in.


### Retries for Instance Metadata 🔗 
The instance metadata service periodically experiences short periods of downtime for maintenance. Therefore, when you try to access IMDS endpoints, they might be unavailable. As a best practice, implement retry logic when accessing IMDS endpoints. The following strategy is recommended: retry up to three times with a 30 second timeout if you receive a `404`, `429`, or `5xx` response. For more information and examples, see the [SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconcepts.htm) documentation.
## Metadata Keys 🔗 
The instance metadata includes default metadata keys that are defined by Compute and cannot be edited, as well as custom metadata keys that you create.
Some metadata entries are directories that contain additional metadata keys. In the following tables, entries with a trailing slash indicate a directory. For example, `regionInfo/` is a directory that contains other metadata keys.
### Metadata Keys for an Instance 🔗 
The following metadata is available about an instance. The paths are relative to `http://169.254.169.254/opc/v2/instance/`.
Metadata Entry | Description  
---|---  
`availabilityDomain` |  The [availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) the instance is running in. This name includes the tenancy-specific prefix for the availability domain name. Example: `Uocm:PHX-AD-1`  
`faultDomain` |  The name of the [fault domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault) the instance is running in. Example: `FAULT-DOMAIN-1`  
`compartmentId` |  The **OCID** of the compartment that contains the instance.  
`displayName` | The user-friendly name of the instance.  
`hostname` | The host name of the instance.  
`id` | The OCID of the instance.  
`image` | The OCID of the image used to boot the instance.  
`metadata/` |  A directory containing any custom metadata that you provide for the instance. To query the metadata for a specific custom metadata key, use `metadata/<key-name>`, where <key-name> is the name of the key that you defined when creating the instance.  
`metadata/ssh_authorized_keys` | For Linux instances, the public SSH key that was provided when creating the instance.  
`metadata/user_data` | User data to be used by cloud-init or cloudbase-init to run custom scripts or provide custom configuration.  
`region` |  The [region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) that contains the availability domain the instance is running in. For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively. For all other regions, the full region identifier is returned. Examples: `phx`, `eu-frankfurt-1`  
`canonicalRegionName` |  The region identifier for the [region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) that contains the availability domain the instance is running in. Example: `us-phoenix-1`  
`ociAdName` |  The [availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) the instance is running in. This name is used internally and corresponds to the data center label. Example: `phx-ad-1`  
`regionInfo/` | A directory containing information about the [region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) that contains the availability domain the instance is running in.  
`regionInfo/realmKey` |  The key for the **realm** that the region is in. Example: `oc1`  
`regionInfo/realmDomainComponent` |  The domain for the realm. Example: `oraclecloud.com`  
`regionInfo/regionKey` |  The 3-letter key for the [region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example: `PHX`  
`regionInfo/regionIdentifier` |  The region identifier. Example: `us-phoenix-1`  
`shape` | The [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling the [ListShapes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Shape/ListShapes) operation.  
`state` |  The current lifecycle state of the instance. For a list of allowed values, see [Instance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/). Example: `Running`  
`timeCreated` | The date and time the instance was created, in the UNIX timestamp format in milliseconds since Epoch.  
`agentConfig/` | A directory containing information about the [Oracle Cloud Agent software and plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins) running on the instance.  
`agentConfig/monitoringDisabled` |  A Boolean value indicating whether the Oracle Cloud Agent software can gather performance metrics and monitor the instance using the monitoring plugins. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.  
`agentConfig/managementDisabled` |  A Boolean value indicating whether the Oracle Cloud Agent software can run all the available management plugins. The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.  
`agentConfig/allPluginsDisabled` | A Boolean value indicating whether Oracle Cloud Agent can run all of the available plugins. This includes the management and monitoring plugins.  
`agentConfig/pluginsConfig/` | A directory containing information about the [plugins that Oracle Cloud Agent manages](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins) on the instance.  
`agentConfig/pluginsConfig/name` | The plugin name.  
`agentConfig/pluginsConfig/desiredState` |  Whether the plugin should be enabled or disabled. To enable the monitoring and management plugins, the `monitoringDisabled` and `managementDisabled` attributes must also be set to false.  
`freeformTags/` | A directory containing any [free-form tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm) that are added to the instance.  
`definedTags/` | A directory containing any [defined tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm) that are added to the instance.  
Here's an example response that shows of all the information for an instance:
Copy
```
{
 "availabilityDomain" : "EMIr:PHX-AD-1",
 "faultDomain" : "FAULT-DOMAIN-3",
 "compartmentId" : "ocid1.tenancy.oc1..exampleuniqueID",
 "displayName" : "my-example-instance",
 "hostname" : "my-hostname",
 "id" : "ocid1.instance.oc1.phx.exampleuniqueID",
 "image" : "ocid1.image.oc1.phx.exampleuniqueID",
 "metadata" : {
  "ssh_authorized_keys" : "example-ssh-key"
 },
 "region" : "phx",
 "canonicalRegionName" : "us-phoenix-1",
 "ociAdName" : "phx-ad-1",
 "regionInfo" : {
  "realmKey" : "oc1",
  "realmDomainComponent" : "oraclecloud.com",
  "regionKey" : "PHX",
  "regionIdentifier" : "us-phoenix-1"
 },
 "shape" : "VM.Standard.E3.Flex",
 "state" : "Running",
 "timeCreated" : 1600381928581,
 "agentConfig" : {
  "monitoringDisabled" : false,
  "managementDisabled" : false,
  "allPluginsDisabled" : false,
  "pluginsConfig" : [ {
   "name" : "OS Management Service Agent",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Custom Logs Monitoring",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Compute Instance Run Command",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Compute Instance Monitoring",
   "desiredState" : "ENABLED"
  } ]
 },
 "freeformTags": {
  "Department": "Finance"
 },
 "definedTags": {
  "Operations": {
   "CostCenter": "42"
  }
 }
}

```

### Metadata Keys for Attached VNICs 🔗 
The following metadata is available about the [VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) that are attached to the instance. The paths are relative to `http://169.254.169.254/opc/v2/vnics/`.
Metadata Entry | Description  
---|---  
`vnicId` | The OCID of the VNIC.  
`privateIp` | The private IP address of the primary `privateIp` object on the VNIC. The address is within the CIDR of the VNIC's subnet.  
`vlanTag` |  The Oracle-assigned VLAN tag of the attached VNIC. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution, the `vlanTag` value is instead the value of the `vlanTag` attribute for the VLAN. See [Vlan](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/).  
`macAddr` |  The MAC address of the VNIC. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution, the MAC address is learned. If the VNIC belongs to a subnet, the MAC address is a static, Oracle-provided value.  
`virtualRouterIp` | The IP address of the virtual router.  
`subnetCidrBlock` | The subnet's CIDR block.  
`nicIndex` | Which physical network interface card (NIC) the VNIC uses. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).  
Here's an example response that shows the VNICs that are attached to an instance:
Copy
```
[ {
  "vnicId" : "ocid1.vnic.oc1.phx.exampleuniqueID",
  "privateIp" : "10.0.3.6",
  "vlanTag" : 11,
  "macAddr" : "00:00:00:00:00:01",
  "virtualRouterIp" : "10.0.3.1",
  "subnetCidrBlock" : "10.0.3.0/24",
  "nicIndex" : 0
}, {
  "vnicId" : "ocid1.vnic.oc1.phx.exampleuniqueID",
  "privateIp" : "10.0.4.3",
  "vlanTag" : 12,
  "macAddr" : "00:00:00:00:00:02",
  "virtualRouterIp" : "10.0.4.1",
  "subnetCidrBlock" : "10.0.4.0/24",
  "nicIndex" : 0
} ]
```

### Metadata Keys for Volumes Attached with Multipath-Enabled Attachments 🔗 
The following metadata is available about the [multipath-enabled volume attachments](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm#multipath) that are attached to the instance. The paths are relative to `http://169.254.169.254/opc/v2/volumeAttachments/`.
Metadata Entry | Description  
---|---  
`id` | The OCID of the volume attachment.  
`instanceId` | The OCID of the instance.  
`volumeId` | The OCID of the volume.  
`ipv4` | The IPv4 address of the iSCSI target.  
`iqn` | The IQN of the iSCSI target.  
`port` | The port of the iSCSI target.  
`multipathDevices` | A list of secondary multipath devices with the properties `ipv4`, `iqn`, and `port`.  
Here's an example response that shows the multipath-enabled volume attachments for an instance:
Copy
```
[
 {
  "id": "ocid1.volumeattachment.oc1.phx.exampleuniqueID",
  "instanceId": "ocid1.instance.oc1.phx.exampleuniqueID",
  "volumeId": "ocid1.volume.oc1.phx.exampleuniqueID",
  "ipv4": "169.254.2.2",
  "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
  "port": 3260,
  "multipathDevices":
  [
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   },
   {
    "ipv4": "exampleIP",
    "iqn": "iqn.2015-12.com.oracleiaas:exampleuniqueID",
    "port": 3260
   }
  ]
 }
]
```

### Metadata Keys for Shape Configuration
This command displays the OCPUs available in each compute shape. This information is useful for flex shapes where an application needs to know more about OCPUS, VNICs, or any configurable shape details.
The following metadata is available about the see [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) that are attached to the instance. The paths are relative to `http://169.254.169.254/opc/v2/instance/shapeConfig`.
Metadata Entry | Description  
---|---  
`Shape` | The name of the instance.  
`OCPU Count` | The number of OCPUs limited by the chosen VM shape and any OCPU quotas set for the tenancy.  
`networkingBandwidthInGbps` | The amount of data that can be transferred in a network between two points.  
`Memory` | The OCPU memory limit for the chosen VM shape. For more information, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).  
`maxVnicAttachments` | The maximum number of attachments between a VNIC and an instance.  
Use the following cURL command to issue a GET request to the instance shape configuration metadata that you're interested in. 
```
 curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254
/opc/v2/instance/shapeConfig
```

Here's an example response that shows the shape configuration metadata for a Linux instance.
```

{
 "ocpus" : 4.0,
 "memoryInGBs" : 60.0,
 "networkingBandwidthInGbps" : 4.0,
 "maxVnicAttachments" : 4
}
```

Was this article helpful?
YesNo

