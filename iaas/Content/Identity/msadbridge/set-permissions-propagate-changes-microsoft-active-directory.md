Updated 2023-07-06
# Setting Permissions to Propagate Changes from IAM to Microsoft Active Directory
Set permissions for your AD bridge service account so that you can propagate changes you have done in IAM to Microsoft Active Directory through the AD bridge.
  1. Use your domain administrator credentials to sign in to the machine that contains your Microsoft Active Directory server.
  2. Open a command window.
  3. Set the **Generic Write** permission for the users, groups, and organizational units (OU) in the AD domain if you want to propagate the changes you have done in IAM to Active Directory.
```
dsacls <AD_Domain_Name> /I:T /g "<AD_Domain_Name>\<User/Group_Name>:GW"
```



Was this article helpful?
YesNo

