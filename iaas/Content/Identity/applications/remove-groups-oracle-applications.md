Updated 2025-01-14
# Removing Groups from Oracle Applications
You can remove groups from Oracle applications from the **Application Roles** tab. You can remove groups from Oracle applications only after you activate the applications.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that you want to modify.
  4. Select **Application roles**.
  5. Select the checkbox for the application role of the Oracle application from which you want to remove groups.
**Tip** You can see which application roles have groups assigned to them by the group icon and the **Groups assigned** link that appears in the application role.
  6. Select the **Actions** menu, and then select **Revoke groups**.
  7. In the **Revoke groups** window, select the checkbox for each group that you want to remove from the application role.
**Note** The **All tenant users** group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you remove the **All tenant users** group from your applications, then access rights to these applications are revoked for every IAM user.
  8. Select **Revoke**.


Was this article helpful?
YesNo

