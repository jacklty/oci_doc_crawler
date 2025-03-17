Updated 2024-01-18
# Reattaching a Boot Volume
On Oracle Cloud Infrastructure, you can reattach a boot volume to an instance.
A boot volume is automatically attached to an instance when the instance is launched. Sometimes you need to detach and reattach a boot volume as a data volume for troubleshooting purposes. For that information, see [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-boot-volume.htm#detaching-a-boot-volume "On Oracle Cloud Infrastructure, if you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume using the steps described in this topic. Then you can attach the boot volume to another instance as a data volume to troubleshoot it.") and [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance."). This procedure describes how to reattach a boot volume to an instance.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/reattaching-a-boot-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/reattaching-a-boot-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/reattaching-a-boot-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to reattach a boot volume.
    3. Click the instance name.
    4. Under **Resources** , click **Boot Volumes**.
    5. Click the boot volume Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Attach**.
Confirm when prompted.
Wait for the state of the boot volume to be **Attached**. Then you can restart the instance as described in [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.").
  * Use the [oci compute boot-volume-attachment attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/attach.html) command and required parameters to reattach a boot volume to an instance.
Command
CopyTry It
```
oci compute boot-volume-attachment attach --boot-volume-id <boot_volume_OCID> --instance-id <instance_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [AttachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/AttachBootVolume) operation to reattach a boot volume to an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

