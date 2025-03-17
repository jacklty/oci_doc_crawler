Updated 2024-02-13
# Understanding Full and Incremental Sync
You can synchronize users and groups from selected organizational units (OUs) in Microsoft Active Directory into IAM. You can perform either an incremental sync or a full sync. Learn about syncing new OUs and read some example use cases.
## Syncing New Organizational Units 🔗 
Before 20.1.3, OU sync was triggered by the bridge every minute so that newly added OUs in Microsoft Active Directory were automatically available in IAM. Starting with the 20.1.3 release, when you add a new organizational unit (OU) in Microsoft Active Directory, you must perform an incremental or full sync to see the newly created OU in IAM. We recommend that you to run an incremental sync when adding new OUs.
## Use Case: Unlink Users from Microsoft Active Directory 🔗 
When you perform a full sync on users from organizational units (OUs), all users in the selected OUs are synchronized in IAM. The next time you apply a filter to synchronize a specific OU, you perform an incremental sync and the users in that OU are resynchronized in IAM.
The synchronized users who were not part of the filter will be unlinked from Microsoft Active Directory. The unlinked users can no longer authenticate using delegated authentication because their link to Microsoft Active Directory is removed and their authentication falls back to IAM. Any new updates to these users won't be synced to IAM. You can use IAM to reset the passwords for these users. When you request a password change for the users, IAM sends a **Password Reset** notification to them so that they can provide their new passwords.
If you remove the filter and synchronize these users again using full sync, then all the users who were unlinked earlier are now linked, and their authentication falla back to Microsoft Active Directory.
Consider Human Resource and Marketing OUs with five users each. You're using full sync to sync them from Microsoft Active Directory to IAM. All the users are synced in IAM.
If you want the Marketing users alone in IAM, then you can perform an incremental sync along with a filter to resync the Marketing users into IAM. All the users who are part of the Human Resource OU are unlinked because they're not part of the filter that's used to resync users. The number of unlinked users appears in the UI.
[![the flow of On-demand full sync from Microsoft Active Directory to IAM](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-use-case_sync-users-oracle-identity-cloud-service-using-demand-full-sync.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-use-case_sync-users-oracle-identity-cloud-service-using-demand-full-sync.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | A full sync from Microsoft Active Directory will unlink the users who aren't synced in the identity domain either because of a change in OU selection, or an increase/decrease in the scope of the filter.  
## Use Case: Delete Users and Groups from Microsoft Active Directory 🔗 
Microsoft Active Directory is an authoritative source. Users that are deleted from Microsoft Active Directory are unlinked and deactivated in IAM. You can then remove these users from IAM. 
When groups are deleted from Microsoft Active Directory, upon a full or incremental sync, these groups are also removed from IAM.
## Use Case: Reattach an Unlinked User in IAM 🔗 
Consider you want to create previously unlinked users in Microsoft Active Directory with the same usernames. When you next perform a full or an incremental sync, these users in Microsoft Active Directory are reattached to the associated users in IAM.
The reattached user's authentication will be delegated to Microsoft Active Directory if delegated authentication is activated in IAM. For example, a user is synced from multiple Microsoft Active Directory domains into IAM. All these domains are authoritative because Microsoft Active Directory is an authoritative source. If you delete a user from one of the domains, then the user is unlinked in IAM. If you resync the user to a different Microsoft Active Directory domain, then this domain now becomes authoritative for the user.
Was this article helpful?
YesNo

