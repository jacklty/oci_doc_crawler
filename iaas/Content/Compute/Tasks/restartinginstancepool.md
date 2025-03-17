Updated 2025-02-13
# Stopping and Starting the Instances in an Instance Pool
You can stop and start all the instances in an instance pool as needed to update software or resolve error conditions.
To automatically stop and start instances in an instance pool based on a schedule, you can [enable autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#Autoscaling) for the pool.
**Tip** To stop all instances in an instance pool, stop the pool itself, rather than the individual instances. If you stop all of the instances in a pool without stopping the pool, the pool tries to relaunch the instances.
## Shutting Down or Restarting an Instance Using the Instance's OS 🔗 
You can shut down and restart instances using the commands available in the operating system when you are logged in to the instance. Shutting down an instance using the instance's OS does not stop billing for that instance. If you shut down the instances in an instance pool this way, be sure to also stop the instance pool from the Console or API.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For a typical policy that gives access to instance pools and instance configurations, see [Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
## Resource Billing for Stopped Instances 🔗 
For both VM and bare metal instances, billing depends on the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) that you use to create the instance:
  * **Standard shapes:** Stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits.
  * **Dense I/O shapes:** Billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must [delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#Deleting_an_Instance_Pool).
  * **GPU shapes:** For VM instances that use shapes in the VM.GPU.A10 series, stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits. For all other GPU shapes, billing continues for stopped instance pools because GPU resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must [delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#Deleting_an_Instance_Pool).
  * **HPC shapes:** Billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must [delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#Deleting_an_Instance_Pool).
  * **Optimized shapes:** For VM instances, stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits. For bare metal instances, billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must [delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#Deleting_an_Instance_Pool).


Shutting down an instance using the instance's OS does not stop billing for that instance. If you shut down the instances in an instance pool this way, be sure to also stop the instance pool from the Console or API.
For more information about Compute pricing, see [Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html). For more information about how instances running Microsoft Windows Server are billed when they are stopped, see [How am I charged for Windows Server on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#generalquestions__pricing-for-win-server)
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)


  * [To start all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. Click the name of the instance pool in which are the instances you want to start.
    3. Click **Start** , and then confirm when prompted.
[To stop all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. Click the name of the instance pool in which are the instances you want to stop.
    3. Click **Stop**.
    4. By default, the Console gracefully stops the instances by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instances are powered off.
**Note** If the applications that run on the instances take more than 15 minutes to shut down, then they could be improperly stopped, resulting in data corruption. To avoid this, [shut down the instances using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#os) before you stop the instances using the Console.
If you want to stop the instances immediately, without waiting for the OS to respond, select the **Force stop the instance pool by immediately powering off every instance in the pool** check box.
    5. Click **Stop instance pool**.
[To reboot all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm)
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. Click the name of the instance pool in which are the instances you want to reboot.
    3. Click **Reboot**.
    4. By default, the Console gracefully restarts the instances by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instances are powered off and then powered back on.
**Note** If the applications that run on the instances take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, [shut down the instances using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#os) before you restart the instance using the Console.
If you want to reboot the instances immediately, then without waiting for the OS to respond, select the **Force reboot the instance pool by immediately powering off every instance in the pool, then powering them back on** check box.
    5. Click **Reboot instance pool**.
  * To manage the lifecycle state of the instances in an instance pool using the CLI, open a command prompt and run any of the following commands.
To start (power on) the instances in the specified instance pool, use the [instance-pool start](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/start.html) command:
Command
CopyTry It
```
oci compute-management instance-pool start --instance-pool-id <INSTANCE_POOL_OCID>
```

To stop (immediate power off) the instances in the specified instance pool, use the [instance-pool stop](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/stop.html) command:
Command
CopyTry It
```
oci compute-management instance-pool stop --instance-pool-id <INSTANCE_POOL_OCID>
```

To softstop (ACPI shutdown) the instances in the specified instance pool, use the [instance-pool softstop](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/softstop.html) command:
Command
CopyTry It
```
oci compute-management instance-pool softstop --instance-pool-id <INSTANCE_POOL_OCID>
```

To reset (immediate power off and power on) the instances in the specified instance pool, use the [instance-pool reset](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/reset.html) command:
Command
CopyTry It
```
oci compute-management instance-pool reset --instance-pool-id <INSTANCE_POOL_OCID>
```

To softreset (ACPI shutdown and power on) the instances in the specified instance pool, use the [instance-pool softreset](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/softreset.html) command:
Command
CopyTry It
```
oci compute-management instance-pool softreset --instance-pool-id <INSTANCE_POOL_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To manage the lifecycle state of the instances in an instance pool with the API, use the following operations:
    * [StartInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StartInstancePool)
    * [StopInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StopInstancePool)
    * [SoftstopInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/SoftstopInstancePool)
    * [ResetInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/ResetInstancePool)
    * [SoftresetInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/SoftresetInstancePool)


Was this article helpful?
YesNo

