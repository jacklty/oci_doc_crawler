Updated 2024-01-18
# Detaching a Boot Volume
On Oracle Cloud Infrastructure, if you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume using the steps described in this topic. Then you can attach the boot volume to another instance as a data volume to troubleshoot it.
**Prerequisite** :
The instance must be in the Stopped state to detach a boot volume. You must reattach a boot volume before you can start the instance. See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.").
When you stop the instance, any application that's running on the instance is immediately stopped, possibly resulting in data corruption. To avoid stopping the instance while applications are running, manually shut down the instance by using the commands available in the instance OS. After the instance is shut down from the OS, then stop the instance.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-boot-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-boot-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-boot-volume.htm)


  *     1. Stop the instance:
      1. Shut down the instance from the instance OS.
      2. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
      3. At the top of the page, select the compartment that contains the instance you plan to stop.
      4. Click the name of the instance.
      5. On the instance details page, click **Controls** (upper right corner), then select **Stop**.
Wait for the status to change from **Stopping** to **Stopped**. Stopping an instance can take up to five minutes.
    2. Under **Resources** , click **Boot Volumes**.
    3. Click the boot volume Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then select **Detach**.
    4. Confirm when prompted.
  * Use the [oci compute boot-volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/detach.html) command and required parameters to detach a boot volume from an instance.
Command
CopyTry It
```
oci compute boot-volume-attachment detach --boot-volume-attachment-id <boot_volume-attachment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DetachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DetachBootVolume) operation to detach a boot volume from an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

