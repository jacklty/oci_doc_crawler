Updated 2024-03-22
# Recovering a Deleted Object Version from Roving Edge Infrastructure
Describes how to recover a deleted object version contained within an object storage bucket on your Roving Edge Infrastructure devices.
Recovering a deleted object version requires removing the delete marker that was created when you deleted the latest version of an object. The previous version of the object listed just below the delete marker is recovered and becomes the latest version of the object.
## Using the Device Console 🔗 
  1. Open the navigation menu and select **Object Storage > Object Storage**. The **Buckets** page appears. All buckets are listed in tabular form.
  2. Click the bucket containing the object whose deleted version you want to recover. The bucket's **Details** page appears. All objects are listed in tabular form.
  3. Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted.
  4. Click the Down arrow at the right side of the object's entry to display the versions that you can recover. Look for the entry that includes "**(Delete Marker)** " under the **Last Modified** column. 
  5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) of the entry with the Delete Marker identifier and click **Delete**.
  6. Confirm the deletion.


The previous version of the object listed just below the delete marker is recovered and becomes the latest version of the object.
Was this article helpful?
YesNo

