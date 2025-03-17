Updated 2023-07-07
# AD Bridge Connectivity Notifications
Learn about notifications that IAM sends to the tenant admin when connectivity between AD bridge and the IAM server is broken, and also when it is restored.
## Notifications sent when connectivity of AD Bridge with IAM server is broken 🔗 
Oracle sends notifications to the tenant admin when connectivity between AD bridge and the IAM server is broken. Connectivity could be broken for any of a number of reasons, for example if the AD bridge is stopped, or if the IAM is stopped on the Windows machine.
The notifications have the email subject: _Connectivity to AD bridge <windows machine name> is unreachable._
## Notifications sent when connectivity of AD bridge with IAM is restored 🔗 
Similarly, when connectivity is restored, an email is sent from Oracle to the tenant administrator.
The notifications have the email subject: _Connectivity to AD bridge <windows machine name> is restored._
![Screenshot of an email body for a restored connection.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-adbridge_email_connection_broken_restored.png)
Was this article helpful?
YesNo

