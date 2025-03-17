Updated 2025-01-14
# Enabling and Configuring Synchronization for Your Application
By enabling and configuring synchronization for your application, IAM can synchronize user accounts from your application and match these accounts to corresponding IAM users.
  1. Select **Edit provisioning** on your application page, scroll down and turn on the **Enable synchronization** switch.
  2. If you want IAM to communicate with your application's SCIM REST API to synchronize groups from the application into an identity domain, then select **Refresh application data**. Otherwise, go to the next step.
  3. Use the following table to populate the fields of the **Configure synchronization** section.
Parameter | Description and Value Information  
---|---  
User identifier | The IAM user attribute that matches user accounts synchronized from the application with users in IAM.  
Application identifier | The user attribute of your application's SCIM REST API that matches user accounts synchronized from the application with users in IAM.  
When exact match is found |  Use the values in this menu to control whether IAM or an application administrator confirms any user accounts that are synchronized from the application into IAM. Values are:
     * **Link and confirm** : Link the synchronized user accounts to corresponding IAM users automatically.
     * **Link but do not confirm** : Link the synchronized user accounts to corresponding IAM users, but application administrators need to confirm the linking operation in the **Import** tab manually.  
Maximum number of creates |  The value that you enter in this field represents the maximum number of user accounts that are created in IAM from the application. If you don't want to limit how many user accounts are created, then leave this field blank.  
Maximum number of deletes |  The value that you enter in this field represents the maximum number of user accounts that are deleted in IAM after these accounts are deleted from the application. If you don't want to limit how many user accounts are deleted, then leave this field blank.  
Synchronization schedule | Specify how often (in hours, days, or weeks) synchronization happens between the application and IAM automatically. If you want to synchronize the user accounts manually, then select **Never**.  
  4. Select **Finish**.


Was this article helpful?
YesNo

