Updated 2024-08-06
# Task 8: Add a Block Volume
Add additional storage by adding a block volume to your instance.
After a block volume is created, you attach the volume to one or more instances. You can use the volume like a regular hard drive.
Avoid entering confidential information in names and tags.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
  2. Click **Create Block Volume**.
  3. In the **Create Block Volume** dialog box, enter the following information:
     * **Name:** Enter a descriptive name for your block volume.
     * **Create in Compartment:** Select the Sandbox compartment.
     * **Size:** Leave the default size (1024 GB).
     * **Backup Policy:** Don't select a backup policy.
     * **Tags:** Leave blank. This tutorial doesn't use tags.
  4. Click **Create Block Volume**.
  5. Monitor the state of the new block volume.
The state is displayed above the icon for the object. You can also scroll down to the Resources section and check the Work Request.
Initially, the block volume is in the provisioning state. When the volume changes to the available state, you can attach it to your instance.


**Perform the next task:**
[Task 9: Attach the Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/9-attach-the-block-volume-to-an-instance.htm#attach-the-block-volume-to-an-instance "Attach the block volume to an instance.")
Was this article helpful?
YesNo

