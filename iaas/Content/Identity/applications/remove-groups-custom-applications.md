Updated 2025-01-14
# Removing Groups from Custom Applications
You can modify custom applications by removing groups from them. Users who are members of these groups can no longer view these applications through the **My Apps** page.
Activate the application.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that you want to modify.
  4. Select **Groups**.
  5. Select the checkbox for each group that you want to remove from the application.
The **All tenant users** group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you remove the **All tenant users** group from your applications, then access rights to these applications are revoked for every IAM user.
  6. Select **Revoke access**.


Was this article helpful?
YesNo

