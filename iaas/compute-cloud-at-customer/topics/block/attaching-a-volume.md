Updated 2024-12-16
# Attaching a Volume
You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.
You can attach volumes to more than one instance at a time, see [Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume-to-multiple-instances.htm#attaching-a-volume-to-multiple-instances "The Compute Cloud@Customer Block Volume service provides the capability to attach a block volume to multiple compute instances. With this feature, you can share block volumes across instances in read/write or read-only mode.").
You can also attach a boot volume that has been detached from its instance to a different instance as a data volume. This operation is convenient for troubleshooting a boot volume and for performing administrative operations while the boot volume is detached from its instance.
**Important**
Only attach Linux volumes to Linux instances and Microsoft Windows volumes to Microsoft Windows instances.
**Important**
If you are reattaching a volume that was detached, the volume might be associated with a different device name, and the instance operating system might not recognize the volume.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. Select the compartment where the instance resides.
    3. In the Instances list, click the instance that you want to attach a volume to.
    4. Under **Resources** , select **Attached Block Volumes**.
    5. In the **Attached Block Volumes** panel, click **Attach Block Volume**.
    6. Enter the following information:
      1. Select the compartment where the block volume resides.
      2. Select a Block Volume.
      3. Select one of the following access modes:
         * **Read/Write:** (Default) Configures the volume attachment with read/write capabilities. The volume cannot be shared with other instances. This option enables attachment to a single instance only.
         * **Read/Write - Shareable:** Configures the volume attachment as read/write, shareable with other instances. This option enables read/write attachment to multiple instances.
         * **Read-Only - Shareable:** Configures the volume attachment as read-only, enabling attachment to multiple instances.
    7. Click **Attach to Instance**.
  * Use the **[oci compute boot-volume-attachment attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/attach.html) ** command and required parameters to attach a boot volume to an instance.
Copy
```
oci compute volume-attachment attach --instance-id instance_OCID \
--volume-id volume_OCID --type paravirtualizedS]
```

**Note**
The `--is-shareable` option is required to attach a shareable volume. The default value of this option is `false`.
Copy
```
--is-shareable true
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

