Updated 2023-10-19
# Cloning a Volume Group
On Compute Cloud@Customer, you can create a clone of an existing volume group.
A cloned volume group is a point-in-time direct disk-to-disk deep copy of the source volume group, so all the data that's in the source volume group is copied to the clone volume group. 
Any subsequent changes to the data on the source volume group are not copied to the clone. 
For additional details about clones and how they differ from backups, see [Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__volume-backups-clones).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-clone-of-a-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-clone-of-a-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-clone-of-a-volume-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume group that you want to clone.
    3. Click the name of the Volume Group you plan to clone.
    4. Under **Resources** , click **Volume Group Clones**.
    5. Click **Create Volume Group Clone**.
    6. Enter the following information:
       * **Volume Group Clone Name:** Enter a descriptive name for the clone. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment where the clone will be created.
    7. Click **Create Volume Group Clone**.
  * This task is not available in the CLI.
  * Use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation and specify [VolumeSourceFromVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/VolumeSourceFromVolumeDetails) for [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails).
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

