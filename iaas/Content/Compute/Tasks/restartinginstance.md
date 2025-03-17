Updated 2025-02-03
# Stopping, Starting, or Restarting an Instance
You can stop, start, or restart an instance as needed to update software or resolve error conditions.
If the instance is scheduled for [infrastructure maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#infrastructure-maintenance), when it is restarted, it is restarted on a healthy physical host.
For steps to manage the lifecycle state of instances in an instance pool, see [Stopping and Starting the Instances in an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#Stopping_and_Starting_the_Instances_in_an_Instance_Pool "You can stop and start all the instances in an instance pool as needed to update software or resolve error conditions.").
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Shutting Down or Restarting an Instance Using the Instance's OS 🔗 
You can shut down and restart instances using the commands available in the operating system when you are signed in to the instance. Shutting down an instance using the instance's OS does not [stop billing](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm#top "When you stop an Oracle Cloud Infrastructure Compute instance, billing for the stopped instance depends on the shape that you used to create the instance.") for that instance. If you shut down an instance this way, be sure to also stop it from the Console or API.
## Starting an Instance 🔗 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. Click **Start**.
  * Use the [instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command and required parameters to start an instance:
Copy
```
oci compute instance action --instance-id <instance_OCID> --action START
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation to start an instance, passing the value `START` as the action to perform.


## Stopping an Instance 🔗 
When you stop an instance, [billing for the stopped instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm#top "When you stop an Oracle Cloud Infrastructure Compute instance, billing for the stopped instance depends on the shape that you used to create the instance.") depends on the shape that you used to create the instance.
Stopped bare metal instances are subject to [hardware reclamation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/hardware-reclamation-stopped-instances.htm#top "When an Oracle Cloud Infrastructure Compute bare metal instance remains in the stopped state for longer than 48 hours, the instance is taken offline and the physical hardware is reclaimed.") when the instance is stopped for longer than 48 hours.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. Click **Stop**.
    4. By default, the Console gracefully stops the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off.
**Note** If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, [shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#operatingsystem) before you stop the instance using the Console.
If you want to stop the instance immediately, without waiting for the OS to respond, select the **Force stop the instance by immediately powering off** check box.
    5. Click **Stop instance**.
  * Use the [instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command and required parameters to stop an instance:
Copy
```
oci compute instance action --instance-id <instance_OCID> --action SOFTSTOP
```

To power off the instance immediately, use the `STOP` action.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation to stop an instance, passing the value `SOFTSTOP` as the action to perform.
To power off the instance immediately, use the `STOP` action.


## Rebooting an Instance 🔗 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. Click **Reboot**.
    4. **Force reboot:** By default, the Console gracefully restarts the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off and then powered back on.
**Note** If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, [shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#operatingsystem) before you restart the instance using the Console.
If you want to reboot the instance immediately, without waiting for the OS to respond, select the **Force reboot the instance by immediately powering off, then powering back on** option.
    5. **Infrastructure maintenance:** If the instance is scheduled for [infrastructure maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#infrastructure-maintenance), for supported shapes, you can control when the maintenance downtime occurs by [proactively reboot migrating](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) the instance to a healthy physical host before the maintenance due date. Depending on the shape, do one of the following:
       * **Standard VM shapes:** The instance is migrated when you reboot it. You don't need to select any additional options.
       * **Dense I/O VM shapes:** If you want to reboot migrate the instance now, select the **Delete the local NVMe-based SSD and reboot migrate to a healthy host** option. For information about other maintenance options for dense I/O instances, see [Infrastructure Maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#infrastructure-maintenance).
**Caution** The NVMe-based SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.
       * **Standard bare metal shapes:** Select the **Reboot migrate the instance to a healthy host** option.
    6. Click **Reboot instance**.
  * Use the [instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command and required parameters to reboot an instance:
Copy
```
oci compute instance action --instance-id <instance_OCID> --action SOFTRESET
```

To reboot the instance immediately, use the `RESET` action.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation to reboot an instance, passing the value `SOFTRESET` as the action to perform.
To reboot the instance immediately, use the `RESET` action.


Was this article helpful?
YesNo

