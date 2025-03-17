Updated 2024-08-06
# Task 9: Attach the Block Volume to an Instance
Attach the block volume to an instance.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
  2. Ensure that the **Sandbox** compartment is selected at the top of the page.
  3. In the **Instances** list, click the name of your instance to view its details.
  4. Scroll down to the **Resources** panel, and click **Attached Block Volumes**.
  5. Click **Attach Block Volume**.
  6. In the **Attach Block Volume** dialog box, enter the following information:
     * **Select from Compartment:** Select the Sandbox compartment.
     * **Block Volume:** Select the block volume you created.
     * **Access:** Select Read/Write.
  7. Click **Attach to Instance**.
The attachment process takes about a minute. The volume is ready when the Attachment State for the volume is attached.
If your block volume isn't displayed, reload the web page.


When a block volume is initially attached to an instance, the instance sees the volume as a new disk. To make the volume available to the instance OS, you need to give the volume a file system and mount it to the OS.
**To learn about the block volume and how to make it available to the instance OS, refer to these sections outside of this tutorial:**
  * [Find Your Volume in the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/find-your-volume-in-the-instance.htm#find-volume-in-the-instance "In Compute Cloud@Customer, when a block volume is initially attached to an instance, the instance sees the volume as a new disk, for example: as device /dev/sdb. This procedure describes how to list the disk devices in an instance so that you can find the volume and administer it in the OS.")
  * [Configuring Volumes to Automatically Mount (Linux Instances)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/configuring-volumes-to-automatically-mount.htm#configuring-volumes-to-automatically-mount-linux "On Compute Cloud@Customer, for Linux instances, if you want to automatically mount volumes during an instance boot, you need add the volumes to the /etc/fstab file.")


**Perform the next task:**
[Task 10: (Optional) Clean Up Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#clean-up-resources "After you've finished with the resources you created for this tutorial, you can delete and release the resources you no longer plan to use.")
Was this article helpful?
YesNo

