Updated 2025-01-14
# Microsoft AD Bridge
Learn how to troubleshoot common Active Directory (AD) issues.
## Active Directory (AD) Bridge Client Connecting to Wrong Domain 🔗 
When you see that the AD Bridge client is connecting to a different domain.
The domain to which the AD Bridge client is connected is determined from the domain of the signed-in user who is installing the AD Bridge client on the Windows Server.
Check whether your user is present in the correct domain through the Active Directory Users and Computers utility.
This is what you see when DummyUser is present in the domain `adfs.fed.oracle.com`.
![User present in ADFS](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/user-present-adfs.png)
## Cannot Connect to Active Directory on SSL Port 🔗 
When you cannot connect to Active Directory on an SSL port.
Active Directory must be configured for an SSL Connection. Try connecting ldp.exe with Active Directory on SSL. To verify the SSL connection:
  1. Ensure that the Windows Support Tools is installed on the Active Directory machine.
    1. Select **Start** , then **All Programs** , then **Windows Support Tools** then **Command Prompt**.
    2. Start the ldp tool by typing **ldp** at the command prompt.
  2. From the ldp window, select Connection | Connect and supply the host name and port number (636). Also, select the SSL checkbox.
    1. If the connection is successful, a window displays listing the information related to the Active Directory SSL connection.
    2. If the connection is unsuccessful, restart your system, and repeat this procedure. If Active Directory still doesn't connect, complete the following instructions to enable SSL [Enable LDAP over SSL with a third-party certification authority](https://docs.microsoft.com/troubleshoot/windows-server/identity/enable-ldap-over-ssl-3rd-certification-authority).


## Connectivity to AD Bridge Restored Notification 🔗 
When you receive an email notification that connectivity to AD Bridge has been restored
the AD Bridge server might become disconnected to IAM because of network connectivity issues. After connectivity has been restored an email notification is sent.
**Note** Any connectivity issues delay synchronization. Any new data will be synced after connectivity is restored.
If you don't want to receive these email notifications, change the Notifications settings from the IAM Admin Console. See [About Email Notifications](https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/about-notifications-concepts.htm#concept_about_notifications "You can configure Identity domains if you want them to automatically send email notifications to users and administrators.") to access Administrator notifications. You can choose to turn on the following Administrator AD Bridge connectivity notifications:
  * Synchronization job summary
  * Notify an administrator when connectivity between AD-ADbridge-Identity domain server is broken.
  * Notify an administrator when connectivity between AD-ADbridge-Identity domain server is restored.
  * Bridge update available
  * Notify an administrator when sync between AD-ADbridge-Identity domain server has succeeded.
  * Notify an administrator when sync between AD-ADbridge-Identity domain server has failed.


## Log File shows LDAP Server Unavailable 🔗 
When you see an "LDAP Server unavailable" error in the log file, use the following steps
The "LDAP Server unavailable" error occurs when the server on which the AD Bridge client in installed is unable to connect to the Active Directory Domain Controller through LDAP. Verify that the Active Directory services are running (In Windows Services list, check the status for AD DS Domain Controller service.) and then try to connect using the client utility `ldp.exe`.
  1. Open a run window from Start.
  2. Enter ldp to open the client utility.
  3. Select Connection and then New Connection. Complete the details and then check whether the connection is successful.
![Successful LDAP connection](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/successful-ldap-connection.png)


## ADBridge Unreachable Error 🔗 
When you see the message "ADBridge Unreachable" in the user interface, use the information below to determine the cause.
AD Bridge has one-way communication with IAM. This means that IAM can't directly communicate with the server on which AD Bridge is installed. Instead, AD Bridge frequently polls IAM to check whether any operation (like sync) is pending. An "AD Bridge Unreachable" message means that the polling is not being performed. The following are some reasons that the AD Bridge might be unreachable.
  * The AD Bridge is not installed.
  * The AD Bridge is installed but unable to reach to IAM over the internet. 
    * Check your connection/proxy settings.
    * Test the connectivity using the AD Bridge user interface.
  * The background service is stopped.
    * Start **Identity Cloud Service Microsoft Active Directory Bridge Service** from Windows Services.
    * Ensure that the **Startup type** is Automatic.


After you have determined the cause, restart the AD Bridge service, either from the AD Bridge user interface (Stop/Start buttons) or from Windows Services.
**Note** Before restarting the AD Bridge service, take a thread dump of the IAM process and share it with the Oracle Support Team. See [30. How to take thread dump of AD Bridge service on AD Bridge machine?](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/troubleshooting-and-faqs-active-directory-ad-bridge.html#GUID-ED358060-D348-41A4-B9C0-A58E51B05332__THREAD_DUMP)
You must resolve this issue for the AD Bridge to function properly. If you don't fix this issue, AD Bridge functionalities including Sync and Delegated Authentication will not work properly.
## No Active Sync Message 🔗 
When you see the message "No active sync" in the Console, you can safely ignore it.
This message doesn't indicate that there is an issue. It means that currently a sync is not in progress. The next sync will run according to the interval set for the domain through the configuration page. Or, it can be triggered manually.
Since the incremental sync only reads changed data, a sync can happen very fast and it might appear that the "No active sync." message never disappears. You can always verify the last sync status from the Import page for that particular domain.
## Moving Domain Controller to Another Machine 🔗 
When you move the Domain Controller from its current machine to another machine, you can verify that everything is working correctly.
Moving the Domain Controller should not cause any issues. Verify Domain Controller connectivity by using the **Test Connectivity** option in the AD Bridge user interface. If there's an issue in the AD Bridge to Domain Controller (LDAP) communication, then select **Detect Domain Controller** to further detect whether the Domain Controller is accessible.
The following screen shots are examples of successful connection tests.
![Shows a successful test message](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/successful-test-message-example-1.png)
![Shows a successful test message](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/successful-test-message-example-2.png)
## Updating Credentials in AD Bridge Client 🔗 
When you have chanegd your user credentials to connect to Active Directory, this is how to change the credentials in the Active Directory Bridge client.
After AD Bridge version 21.3.1, this feature is available in the user interface. Download and install the latest version of AD Bridge.
**Note** You don't need to uninstall the current binaries. The install upgrades them. See "Update AD credentials" in the following screenshot.
![User credentials](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/user-credentials.png)
## Synced Users Cannot Sign In 🔗 
Users are synced, but they are not able to sign in.
The cause depends on which of the three authentication methods (listed below) are being used to sign in Active Directory (AD) users. These methods can be changed using the domain configuration page. Sign in functionality works differently in each case.
  * Local Authentication (default): After the sync, users will get a welcome notification to change the password for their account. They need to use the provided username (from AD) and password they set to sign in to their account. 
**Action to take:** Check whether the user is present in IAM. (The user sync might have failed because of invalid data.) If the user exists, try resetting the password from IAM.
  * Delegated Authentication: With local authentication, you can enable delegation from AD. With delegated authentication, users won't create a password but instead use their existing AD passwords to sign in. IAM delegates the user authentication to AD through AD Bridge.
**Action to take:** Check whether the user is present in IAM. Also, check whether the user is active in AD and that the password is not expired.
  * Federated Authentication: This method uses a third-party service like Microsoft AD FS to authenticate the user.
**Action to take:** Check the configuration of the third-party service.


Use the following screen shots as a guide.
![User synced](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/users-synced-example-1.png) ![User synced](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/users-synced-example-2.png)
## Cannot Enable Federation 🔗 
When you are unable to enable federation, check whether Delegated Authentication is enabled. If Delegated Authentication is enabled, Federated Authentication cannot be enabled. To enable it, use the following steps:
  1. Deactivate Delegated Authentication. See [Deactivating Delegated Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/deactivate-delegated-authentication.htm#deactivate-delegated-authentication "Deactivate delegated authentication for a Microsoft Active Directory \(AD\) Bridge associated with an AD domain. Users transferred into IAM through this bridge must use their IAM passwords to authenticate into the identity domain.").
  2. In Directory Integrations, turn on Federated Authentication.
  3. Perform a Full Import.


## Cannot Enable Delegated Authentication 🔗 
When you can't enable delegated authentication, use the following steps:
  1. On the Directory Integrations page, ensure that **Enable local authentication** is chosen.
  2. If you have Federated Authentication enabled, turn it off.
  3. Then go to the Delegated Authentication settings and activate it for domain you want.


## Change Username to an Email Address 🔗 
When you want to change your sign in username to an email address, use the following step:
Map the `mail` attribute of Active Directory (AD) to `User Name` in IAM inbound mapping as shown in screenshot below.
![Edit attribute mappings](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/edit-attr-mappings.png)
**Note** You can either configure `sAMAccountName` or `mail` with `User Name` but not both at same time. If users are already synced, then you need to trigger a Full Import after changing this attribute mapping. A Full Import will sync all users again and this time store `mail` from AD to `User Name` in IAM.
## Users Are Not Syncing Into IAM During Scheduled Sync Job 🔗 
AD Bridge is configured to sync users into IAM. Sometimes a few users are not syncing into IAM during scheduled sync job, but will sync if you run full import.
AD Bridge records updates in Active Directory using synchronization tokens and an update sequence number (USN). The previous highest USN value is stored in and any time an incremental sync is run; IAM reads the data from the stored USN to the latest USN.
Sometimes, because of factors such as a Domain Controller change, USN numbers get corrupted (if a new DC has large USN value than previous DC) causing users not to sync. A Full sync doesn't use tokens that is why the users appear in a Full sync.
Upgrade to the latest AD Bridge to resolve this issue.
## Can AD Bridge Client Sync with Azure AD 🔗 
Azure AD is not supported through AD Bridge. The AD Bridge only works with on-premise Active Directories.
Azure AD is supported through Microsoft Azure integration, as well as through Azure AD connector.
## Changing Attribute Mapping 🔗 
Attribute mappings can be changed at any time. Ensure that you perform a Full sync after saving the new configuration. User data will be updated by the Full sync. If you don't do a Full sync, existing user data remains the same and new users will have updated data. 
**Note** It is NOT recommended that you change attribute mapping frequently.
## Sync Doesn't Complete 🔗 
When you notice that sync hasn't completed for days, terminate it using the following steps:
  1. Use the Abort option on the Import page to quit the unresponsive job. This marks your previous stuck sync as Failed.
  2. Submit a new sync and then check connectivity from the Windows Server (on which AD Bridge is installed) to IAM.
If the problem persists, contact Oracle support.


## Suppress Notifications 🔗 
You can suppress some auto-generated emails and notifications.
IAM provides full control over notifications. Go to Settings, then Notifications. Here you can see three tabs: 
  * **Configure:** Select which notifications to send.
  * **Recipients:** To limit users to send notifications to. Don't make changes here unless you are sure.
  * **Email Templates:** Change the design or the contents of the email sent to the customers.


## Find Sync Failures 🔗 
Failures can be traced through AD Bridge Logs. You can find the log files from the AD Bridge client user interface. Search for your username or group name to see any failures that occurred during the sync.
The following example shows one user that was successfully synced and another where the sync failed.
[![Sync status](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/sync-fail-and-success-example.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/sync-fail-and-success-example.png)
## Delinked Users 🔗 
IAM keeps a mapping of all the AD users (IAM identifier mapped to AD identifier). When the user is removed from the active sync because of, for example, a new filter condition, the record in IAM is kept and just the mapping is removed. The removal of mapping is called delinking.
This case is different from deletion as user is not deleted from AD, if filters are reset, the user will be linked again.
## Installing Multiple AD Bridges 🔗 
To find out how many AD bridges you can install for your identity domain type, see [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
Only one Bridge can be installed on the same Windows Server machinea single Bridge can be installed. To use High Availability (HA), you need multiple machines connected to the same AD Domain.
## Upgrading the AD Bridge Client 🔗 
When a new version of the AD Bridge client is available:
  * You should always upgrade.
  * Make sure you don't the current version again. Reinstalling the current version removes the existing Bridge and may lead to authentication and sync failures.


You do not need to uninstall the existing AD Bridge to upgrade to a newer version.
You can verify the version number from the AD Bridge user interface.
[![AD version](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ad-version.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ad-version.png)
Existing data is not be impacted because of an upgrade, and you can perform an incremental sync. Also, the sync schedule won't be affected, and next sync will be performed as configured.
## Downgrading AD Bridge Client 🔗 
We do not recommend that you downgrade your AD Bridge client.
If you decide to downgrade the client, you must uninstall the current one AD Bridge client which can lead to a downtime of services (sync, delegated authentication, etc.).
You can then install the version you want.
## Users/Groups Not Getting Synced 🔗 
When you notice some users or groups are not getting synced, use this information to resolve it.
  * Check the OU configuration on the Directory Integrations page. You need to select the OUs for groups and users separately. Even if you have the same OU for groups and users, select them separately. Make sure to save the configuration page after you make the changes.
  * Confirm the filter used in users/groups on the configuration page. Use PowerShell to execute the filter and check whether your users are visible there.
  * Check the network connectivity from AD Bridge client to IAM. (Only if some all records are failing.)
  * Check the IDBridge log file ("View logs" from AD Bridge user interface). Look for an error like the following:
[![Groups not synced](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/groups-not-synced.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/groups-not-synced.png)


## Enable AD Bridge Trace Mode Logging 🔗 
When you want to enable AD Bridge trace mode logging, follow these steps.
**Note** The log level change does NOT require restart of AD Bridge client.
  1. Go to the AD Bridge installation folder. The default location is: `C:\Program Files\Oracle\IDBridge`.
  2. Open the file `log4net.config`.
  3. Change this line `<level value="info" />` to `<level value="trace" />`.
  4. If you get a permissions error, open the editor with Administrator privileges. If you are using Notepad, search for Notepad in the Start menu, right select, and choose "Run as Administrator," then open the log file to make changes.


## Taking Thread Dumps of AD Bridge Service 🔗 
How do I take a thread dump of the AD Bridge service on an AD Bridge machine?
When you need to take a thread dump of the AD Bridge service on an AD Bridge machine, follow these steps.
  1. Open Task Manager on a machine where the AD Bridge client binary is installed.
  2. Go to the Processes tab.
  3. Search for the process with the name "Identity Cloud Service Microsoft Active Directory Bridge" in the process list.
  4. Right select the process and select the option **Create dump file**.
[![Thread dump example 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/thread-dump-example-1.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/thread-dump-example-1.png)
  5. After a few seconds. the display dump location and dump file name display.
[![Thread dump example 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/thread-dump-example-2.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/thread-dump-example-2.png)


## Changing the Filter 🔗 
When you change your filter, use the following information to ensure that new users and groups sync.
Filters can prevent new users and groups from syncing into IAM.
Complete the following tasks before adding or modifying filters:
  * Verify the filters by running them using PowerShell commands. Ensure that all data is included.
  * Always run a Full sync after changing filters. This will make sure any previously ignored entries are synced. Also, this will cleanup existing redundant mappings.
  * Existing users/groups will not be deleted. Even if they are out of filter, they will be delinked, but kept in IAM.


## Delegated Authentication Requests Fail 🔗 
Delegated Authentication Requests fail when any of these is true:
  * AD Bridge client is down
  * AD Bridge client is NOT able to connect to IAM
  * Active Directory is down
  * AD Bridge client is busy processing other delegated authentication requests


In all these cases, the authentication request fails unless the password caching is enabled and the password is available in the cache.
For first three scenarios, the service will recover when the downstream system/connectivity issue resolves.
For the last scenario, the service will recover after the concurrent request load decreases.
## Which Password is Used for Delegated Authentication 🔗 
If I have enabled password caching, which password will be used for delegated authentication:
  * The cached password
  * The password stored in Active Directory


First, the password stored in Active Directory is used to authenticate the users. The request goes to the Active Directory through AD Bridge and the IAM stored password is not used.
But, if this request fails because of any of reasons mentioned in [Delegated Authentication Requests Fail](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/ms_ad_bridge.htm#troubleshooting32), then authentication will be tried using the cached password stored.
You can enable or disable fallback to the IAM cached password from the Delegated Authentication settings.
## Cached Passwords in IAM 🔗 
How password caching works in IAM.
If password caching is enabled and there isn't a cached password, or if the cache password is expired, then the next time the user sucessfully logs in to the system the password is stored.
The default expiration for a password is five days, but you can change this in delegated authentication settings.
## AD Bridge Installation Fails 🔗 
When AD bridge installation fails, this is due to:
  * Exceeding the number of identity domains for your identity domain type.
  * Exceeding the number of AD Bridge clients for your identity domain type.


To find out how many identity domains or AD bridges you can install for your identity domain type, see [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
## Installation Log Files 🔗 
When you've had issues with installation, use the log files to identify what's gone wrong.
Installer logs from under `%TEMP%` folder on the Windows machine where the installation was attempted. From Windows start menu, open run prompt and enter `%TEMP%`.
You will see three files per install:
  * `Identity_Cloud_Service_Microsoft_Active_Directory_Bridge_<timestamp>.log`
  * `Identity_Cloud_Service_Microsoft_Active_Directory_Bridge_<timestamp>_Internal.log`
  * `Identity_Cloud_Service_Microsoft_Active_Directory_Bridge_<timestamp>_ad_id_bridge.msi.log`


When you raise a service request, provide the latest versions of these files to Oracle support.
## Unable to See AD Attributes 🔗 
When you are unable to see AD attributes in the Configure Attribute Mapping section, use the information below to resolve the situation.
Note that the Directory User Attribute input is not a dropdown selection, but a suggestive text box. You can write anything to the text box, even if that attribute is not present in your AD.
Ensure you type the correct attribute exactly (including the uppercase and lowercase characters) the way the attribute name appears in Active Directory. 
If you don't do this, you will not see an error at mapping save time, but your AD sync will be impacted, and it will not be able to pull this attribute from Active Directory.
The suggestion are based on frequently used AD attributes only. The IAM attributes is a dropdown selection, and you will see all the attributes there.
Refer to following screen shots:
  1. Write your attribute name, for example, `someAdAttribute`.
[![Configure attribute mapping example 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/configure-attr-mapping-example-1.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/configure-attr-mapping-example-1.png)
  2. Save your row.
[![Configure attribute mapping example 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/configure-attr-mapping-example-2.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/configure-attr-mapping-example-2.png)


## Partially Configured Domain 🔗 
When you see that your domain shows that it's partially configured and the import option is disabled, use these steps.
A partially configured domain indicates that no OU is selected on the configuration page. Any OU selection for users, groups or both is required for configuring domain for sync. Till then there is nothing to import and import will stay disabled.
  1. Select the domain to open it.
  2. Select any OU to fetch users and groups from.
**Note** Users and groups OU selection must be done separately.
  3. You can choose a different set of OUs for users and groups.
  4. Any OU selection for a user or a group enables the import option.
[![Import option disabled](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/import-option-disabled.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/import-option-disabled.png)


Was this article helpful?
YesNo

