Updated 2024-08-06
# Cloning a Boot Volume
On Oracle Cloud Infrastructure, you can create a clone from a boot volume using the Block Volume service. Cloning enables you to make a copy of an existing boot volume without needing to go through the backup and restore process. 
Any subsequent changes to the data on the source boot volume are not copied to the boot volume clone. The clone is the same size as the source boot volume unless you specify a larger volume size when you create the clone.
The clone operation occurs immediately and you can use the cloned boot volume when the state changes to available.
There is a single point-in-time reference for a source boot volume while it is being cloned. If you clone a boot volume while the associated compute instance is running, you need to wait for the first clone operation to complete before creating more clones. You also need to wait for any backup operations to complete.
You can only create a clone for a boot volume within the same tenant. You can create a clone of a boot volume in a different compartment from the source volume compartment if you have the required access permissions.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-boot-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-boot-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-boot-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Boot Volumes**.
    2. At the top of the page, select the compartment that contains the boot volume that you want to clone.
    3. For the volume you want to clone, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Create Clone**.
    4. In the dialog box, enter the following information:
       * **Name:** A name or description for the volume. Avoid entering confidential information.
       * **Compartment:** Select the compartment in which to clone the block volume.
       * **High-Performance Volume:** (Optional) By default, the clone has the same performance setting as the source volume. Use this button to change the performance setting for this clone. 
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Clone**.
The new boot volume is ready to use when it reaches the Available state. For example, you can click the Actions menu and then click **Create Instance** to use this new boot volume to create a new instance.
  * Use the [oci bv boot-volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/create.html) command and required parameters to clone a boot volume.
Copy
```
oci bv boot-volume create --source-boot-volume-id OCID_of_volume_to_clone
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

