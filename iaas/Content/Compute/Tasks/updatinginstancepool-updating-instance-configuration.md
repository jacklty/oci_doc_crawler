Updated 2025-02-03
# Updating the Instance Configuration for an Instance Pool
Update the instance configuration that an instance pool uses when creating instances.
To update the instance configuration that an instance pool uses when creating instances, [create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) with the appropriate settings (if such a configuration doesn't already exist), and then attach the new instance configuration to the pool, as described in this topic.
If you want the instances in the pool to use the settings from the new instance configuration, such as a new shape, then [detach the existing instances from the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#detach-instance "Detach an instance from an instance pool when you no longer want to manage the instance as part of the pool.") and provision new instances.
**Note** When you detach instances from an instance pool, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the instance pool before detaching instances.
If you only want to update the display name or tags of an existing instance configuration, then you can [update the pool's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstanceconfig.htm#Deleting_an_Instance_Configuration). For any other updates, create an instance configuration and then attach it with the settings that you want to use.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool that has the instance configuration you want to update to display the details page.
    4. Click **Edit**.
    5. From the **Instance configuration in _compartment_** menu, select an instance configuration that you want the pool to use when you create instances.
    6. Click **Save**.
  * Use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command to attach a new instance configuration to a pool.
Copy
```
oci compute-management instance-pool update --instance-pool-id <INSTANCE_POOL_OCID> --instance-configuration-id <INSTANCE_CONFIGURATION_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to attach an instance configuration to an instance pool.


Was this article helpful?
YesNo

