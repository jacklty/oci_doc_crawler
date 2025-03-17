Updated 2025-02-03
# Updating the Instance Configuration for a Cluster Network with Instance Pools
Update the instance configuration that a cluster network's underlying instance pool uses when creating instances.
To update the instance configuration for a cluster network, do either of the following:
  * [Create a new instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) with the settings you want and then attach the new instance configuration to the cluster network.
If you want the instances in the cluster network to use the settings from the new instance configuration, such as a new shape, then [detach the existing instances from the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#detach-instance "Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.") and provision new instances.
**Note** When you detach instances from a cluster network, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the cluster network before detaching instances.
  * If you only want to update the display name or tags of an existing instance configuration, you can [update the cluster network's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm#Deleting_an_Instance_Configuration). For any other updates, create and then attach the new instance configuration with the settings that you want to use.


**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
To update the instance configuration that a cluster network uses, first you [create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) with the settings that you want (if such a configuration doesn't already exist), and then you attach the new instance configuration to the cluster network, as described in the following steps.
If you want the instances in the cluster network to use the settings from the new instance configuration, such as a new shape, then [detach the existing instances from the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#detach-instance "Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.") and provision new instances.
**Note** When you detach instances from a cluster network, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the cluster network before detaching instances.
If you only want to update the display name or tags of an existing instance configuration, then you can [update the cluster network's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm#Deleting_an_Instance_Configuration). For any other updates, create and then attach the new instance configuration with the settings that you want to use.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm)


  * To attach a new instance configuration to a cluster network:
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. In the **List scope** section, select the compartment that contains the cluster network.
    3. Click the name of the cluster network that uses the instance configuration you want to update.
    4. Click **Edit**.
    5. Select the instance configuration from the **Instance configuration** menu to use when creating instances in the cluster network's instance pool.
    6. Click **Save changes**.
  * Use the [ instance-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create.html) command to update an instance configuration by creating an instance configuration:
Copy
```
oci compute-management instance-configuration create --compartment-id <COMPARTMENT_OCID> --instance-details <file://path/to/file.json>
```

For a complete list of flags and variable options for instance configuration CLI commands, see the [command line reference for instance configurations](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork) operation to update an instance configuration by attaching a new instance configuration to a cluster network.


Was this article helpful?
YesNo

