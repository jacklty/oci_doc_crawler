Updated 2025-01-14
# Synchronizing IAM with an AD Bridge
You can run an bridge to synchronize IAM with Microsoft Active Directory immediately.
As part of configuring an AD bridge, you specified how often, in hours and minutes, you want IAM to use the bridge to import users and groups from Microsoft Active Directory. You're synchronizing IAM with your Microsoft Active Directory enterprise directory structure.
When the interval you specified elapses, IAM synchronizes with the directory structure so that any new, updated, or deleted user or group records are transferred into IAM. Because of this, the state of each record is synchronized between Microsoft Active Directory and IAM.
For security purposes, you may want to import users and groups from Microsoft Active Directory immediately. There are two types of imports that you can run:
  * Full import: The AD bridge polls Microsoft Active Directory and retrieves data associated with all user and groups that you selected in the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes of the **Configuration** tab for the bridge. This data represents users and groups that were created, modified, or removed inMicrosoft Active Directory AD. As a best practice, we recommend that you perform a full import the first time you run the bridge.
  * Incremental import: Similar to a full import, but for this type of import, the bridge polls Microsoft Active Directory and retrieves only user and group data that changed since you last used the bridge to import users and groups into IAM.


By running the bridge, you can propagate changes for IAM users in Microsoft Active Directory. After users are imported into IAM through the bridge, if you activate or deactivate a user, modify the user's attribute values, or change the group memberships for the user in IAM, then these changes are reflected in Microsoft Active Directory.
You can also use the bridge to view a synchronization log of the communication between IAM and Microsoft Active Directory.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the AD Bridge that you want to use to import users and groups from Microsoft Active Directory.
  4. Select **Configuration**.
  5. In the **Configuration** tab:
    1. In the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes, select the checkbox for each OU that contains users or groups that you want to import.
    2. In the **Supported Operations** area, select checkboxes to enable IAM to propagate a user's activation status, attribute values, or group memberships to AD. See [Configuring an AD Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.") for more information about the **Supported Operations** area.
    3. Select **Save**.
The bridge propagates any changes to an IAM user's activation status, attribute values, or group memberships to Microsoft Active Directory.
  6. In the **Confirmation** window, select **OK**.
  7. Select **Import**.
  8. In the **Import Type** window, choose whether you want to run an incremental import or a full import, and then select **OK**.
IAM imports the users and groups from Microsoft Active Directory.
**Note** Based on how many users and groups you're importing, the job may take several minutes or even hours.
  9. Select the**Import** tab. The status of the job IAM uses to import users and groups from AD is **Running**. After all users and groups are imported, the status changes to **Success**.
Also, on this tab, you'll see a synchronization log of all traffic that occurs between IAM and Microsoft Active Directory for the current import job that ran. This includes the start date and time, and completion date and time, for the import job, how many users and groups were imported from Microsoft Active Directory successfully, and how many users and groups couldn't be imported.
**Note** If you don't see the status change after a few minutes, then select **Refresh**. Also, if the status of the job is **Failed** , then an error occurred while the bridge was transferring users and groups from Microsoft Active Directory to IAM.


Was this article helpful?
YesNo

