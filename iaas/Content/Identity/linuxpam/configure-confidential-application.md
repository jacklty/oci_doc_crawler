Updated 2025-01-14
# Configuring a Confidential Application
To register the IAM Linux PAM as a client application in IAM, you create a confidential application with the POSIX Viewer role.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  2. Select **Add application.**
  3. In the **Add application** window, select **Confidential Application** , and then select **Launch workflow**.
  4. In the **Add Confidential Application** page, enter a **Name** for the application. Select **Next**.
  5. On the **Add Confidential Application** page, select **Configure this application as a client now**.
  6. In the **Authorization** section, select these two **Allowed grant types** :
     * **Client Credentials**
     * **JWT Assertion**
  7. Select **Add app roles**.
  8. In the **Add app roles** dialog box, select these roles: 
     * **Me**
     * **POSIX Viewer**
     * **Signin**
     * **Identity Domain Administrator** or **User Administrator**
  9. Select **Add**.
  10. Select **Next**. 
  11. Select **Finish**. 
  12. Record the **Client ID** and **Client Secret** in the General Information section.
To integrate with your confidential application, use this ID and secret as part of your connection settings. The **Client ID** and **Client Secret** are equivalent to a credential (for example, an ID and password) that your application uses to communicate with IAM.
  13. Return to the **Add app roles** dialog box, and remove the following administrator role: **Identity Domain Administrator** or **User Administrator**. If you don't remove roles, the application will fail during testing.
  14. At the top of the page, to the right of the application name, select **Activate**. 
  15. In the **Activate application** dialog box, select **Activate application**. 


Was this article helpful?
YesNo

