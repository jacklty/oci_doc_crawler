Updated 2024-11-07
# Deleting a Boot Volume
On Oracle Cloud Infrastructure, you can delete a boot volume that's detached from an instance. 
**Caution**
Any data on a volume is permanently deleted when the volume is deleted. You can't restart the associated instance.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-boot-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-boot-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-boot-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance with the boot volume you want to delete.
    3. For the instance that has the boot volume you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Stop**.
    4. When prompted, select **Force stop the instance by immedidately powering off** , then click **Force Stop Instance**.
    5. Wait for the instance to reach the **Stopped** state.
    6. Click the name of the instance that has the boot volume you want to delete.
    7. Under **Resources** , click **Boot Volumes**.
    8. For the boot volume that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Detach**.
Confirm when prompted.
    9. Click the name of the boot volume.
    10. Click the **Controls** button (upper right), then click **Terminate**.
    11. Confirm the termination.
The block volume enters the TERMINATED state, and remains in that state for about 24 hours until it's removed.
  * Use the command and required parameters to delete a boot volume.
Command
CopyTry It
```
oci bv boot-volume delete --boot-volume-id <boot_volume_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DeleteBootVolume) operation to delete a boot volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

