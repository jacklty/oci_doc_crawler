Updated 2025-01-14
# Assigning Groups to Custom Applications
You can modify custom applications by assigning groups to them. Users who are members of these groups can access the **My Apps** page to view these applications.
**Prerequisite** : The application must be activated.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that you want to modify.
  4. Select **Groups**.
  5. Select **Assign groups**.
  6. In the **Assign groups** window, do one of the following.
    1. Select the checkbox for each group that you want to assign to the application.
    2. For a provisioned application, select **Assign** next to the group that you want to assign to the application. Enter the required values for the form, and then select **Save**.
**Note**
If the form contains multi-valued attributes, then an **Add** button appears to the right of each attribute. Select **Add** , and then in the **Allowed values** window, select the values for the attribute, and select **OK**.
The **All tenant users** group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you assign this group to any of your applications, then all users are assigned to these applications indirectly.
  7. Select **Assign**.


**Note** If you assigned a provisioned application to the group, then you can modify the values of the application form. To do this, select the **Actions** menu, select **Edit** , change the appropriate values, and then select **Save**.
Was this article helpful?
YesNo

