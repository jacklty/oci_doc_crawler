Updated 2025-01-07
# **Enabling GPU metrics with the OCA HPC plugin**
You can enable GPU metrics with the Oracle Cloud Agent High Performance Computing plugin on your instances.
Current OCI HPC package | New OCA plugin | Description  
---|---|---  
oci-cn-auth | Compute HPC RDMA Authenticationoci-rdma-authentication | Configures RDMA/RoCE network interfaces with QoS, MTU, etc. settings and maintains authentication.  
oci-hpc-mlx-configure | Compute HPC RDMA Auto-Configurationoci-hpc-configure | Configures Mellanox ConnectX-5 firmware and PCIE settings.  
oci-hpc-rdma-configure | Compute HPC RDMA Auto-Configurationoci-hpc-configure | Configures RDMA interface ip addresses.  
oci-hpc-dapl-configure | Compute HPC RDMA Auto-Configurationoci-hpc-configure | Configure legacy MPI DAPL oci-dat.conf.   
**Note** You can transition from python-based solutions to use the Oracle Cloud Agent High Performance Computing plugin.
## Enabling Compute HPC RDMA Authentication and Auto-Configuration on an Existing Instance 🔗 
To enable HPC RDMA authentication and auto-configuration on a host that is running the current OCI HPC packages, follow these steps. 
**Note** Do not perform this workflow on a running workload. These actions can be disruptive and result in data loss.
  1. Determine which version of Oracle Cloud Agent is installed. Version 1.35.0 or above is required. If the version is not 1.35.0 or above, contact support to obtain the installation package.
**OL7/8**
```
# sudo yum info oracle-cloud-agent
```

**Ubuntu**
```
snap info oracle-cloud-agent
```

  2. Stop the existing oci-cn-auth services.
```
# sudo systemctl stop oci-cn-auth-renew
# sudo systemctl stop oci-cn-auth
```

  3. Verify that oci-cn-auth is stopped.
```
# sudo systemctl status oci-cn-auth
```

  4. Stop the wpa_supplicant services.
```
# sudo systemctl stop wpa_supplicant-wired*
```

  5. Verify that wpa_supplicant service are stopped.
```
# sudo systemctl status wpa_supplicant-wired*
```

  6. Remove the oci-cn-auth, oci-hpc-rdma-configure, oci-hpc-mlx-configure, and oci-hpc-dapl-configure package, if installed.
**OL7/8**
```
# sudo yum remove oci-cn-auth oci-hpc-rdma-configure oci-hpc-mlx-configure oci-hpc-dapl-configure
```

**Ubuntu20**
```
# sudo apt-get remove oci-cn-auth oci-hpc-rdma-configure oci-hpc-mlx-configure oci-hpc-dapl-configure
```

  7. Verify that the agent is enabled and running.
**OL7/8**
```
# sudo systemctl status oracle-cloud-agent
# sudo systemctl status oracle-cloud-agent-updater
```

**Ubuntu20**
```
# sudo systemctl status snap.oracle-cloud-agent.oracle-cloud-agent.service
# sudo systemctl status snap.oracle-cloud-agent.oracle-cloud-agent-updater.service
```

  8. Download the current agent configuration on the instance. See [Managing Plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins) for information on how to enable the plugin.
```
# curl --silent -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/ | jq -r '.agentConfig' > agent-config.json
```

  9. Modify the agent-config.json to enable one or more plugins.
```
# cat agent-config.json
{
"monitoringDisabled": false,
"managementDisabled": false,
"allPluginsDisabled": false,
 "isManagementDisabled": false,
 "pluginsConfig": [
  {
   "name": "Compute HPC RDMA Authentication",
   "desiredState": "ENABLED"
  },
  {
   "name": "Compute HPC RDMA Auto-Configuration",
   "desiredState": "ENABLED"
  }
 ]
}
```

  10. Use the OCI ZCLI or OCI SDK to update the agentConfig for the instance.
```
# oci compute instance update --instance-id <instance ocid> --agent-config file://agent-config.json
```

  11. Verify that OCA plugin is enabled for the instance via the command line of the SDK. 
```
# curl --silent -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/ | jq -r '.agentConfig'
```

  12. Verify that the plugin is running. It takes several minutes for the agentConfig changes to populate to the Oracle Cloud Agent.
```
# ps -leaf | grep oci-rdma-authentication
```

  13. Confirm that all RDMA network interfaces have a wpa_supplicant
```
# ps -leaf | grep wpa_supplicant
```



## Launching instance with HPC RDMA Authentication plug-in enabled 🔗 
Provided the custom image has Oracle Cloud Agent 1.35.0 or above and the OCI HPC packages are not present, the LaunchInstanceDetails is used to apply the agentConfig with the plug-in enabled. OS must have the NVIDIA GPU drivers and Mellanox OFED drivers installed.
For more information, see [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
## Enabling RDMA GPU monitoring 🔗 
With Oracle Cloud Agent 1.35.0 new functionality to monitor RDMA and GPU is available. To enable this functionality on an existing instance do the following:
  1. Download the current agent configuration on the instance. The sections below are only one way of enabling the plug-in. For more information, see [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
```
# curl --silent -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/ | jq -r '.agentConfig' > agent-config.json
```

  2. Modify the json by adding the "Compute RDMA GPU Monitoring".
```
# cat agent-config.json
{
 "monitoringDisabled": false,
 "managementDisabled": false,
 "allPluginsDisabled": false,
 "isManagementDisabled": false,
 "pluginsConfig": [
  {
   "name": "Compute HPC RDMA Authentication",
   "desiredState": "ENABLED"
  },
  {
   "name": "Compute HPC RDMA Auto-Configuration",
   "desiredState": "ENABLED"
  },
  {
   "name": "Compute RDMA GPU Monitoring",
   "desiredState": "ENABLED"
  }
 ]
}
```

  3. Use the OCI CLI or OCI SDK to update the agentConfig for the instance.
```
# oci compute instance update --instance-id <instance ocid> --agent-config file://agent-config.json
```



## Required policies for RDMA GPU monitoring 🔗 
If you use a private VPN, you need Service Gateway. If you use a public internet gateway, Service Gateway is not required.
For information on how to use the Monitoring service, see [Securing Monitoring](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm).
**Create a dynamic group**
This example creates a group that contains all instances in a specific compartment.
```
Any {instance.compartment.id = '<compartment_ocid>'}
```

**Create a policy**
Create a policy using the dynamic group to allow to instances to publish metrics. The HPC monitoring plug-in creates 2 custom namespaces that are billed:
  * `gpu_infrastructure_health`
  * `rdma_infrastructure_health`

```
Allow dynamic-group <group_name> to use metrics in compartment <compartment_name> where target.metrics.namespace=<metric_namespace>'
Allow dynamic-group <group_name> to read metrics in compartment <compartment_name>
```

For information on how to publish custom metrics to the Monitoring service, see [Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
Was this article helpful?
YesNo

