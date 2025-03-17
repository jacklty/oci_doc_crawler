Updated 2025-01-14
# Registering the Custom SCIM Gateway Application
Register the custom SCIM gateway sample application with IAM.
  1. Open the navigation menu. Go to **Identity** , **Domains** , **Settings** , and select **Applications**.
  2. Select **Add** , and then select **App Catalog**.
  3. In the **Type of Integration** section, select **Provisioning** , locate the **GenericScim - Basic** template, and then select **Add**.
  4. In the **Details** pane of the **GenericScim - Basic** page, enter `SCIM Gateway Application` for both the name and description of your application, and then select **Next**.
  5. In the **Provisioning** pane, turn on the **Enable Provisioning** switch.
  6. In the **Confirmation** window, select **OK**.
  7. Use the following table to populate the fields of the **Configure Connectivity** section of the **Provisioning** tab.
Parameter | Value  
---|---  
**Host Name** | Enter the host name of your application.  
**Base URI** |  `/scimgate`  
**Administrator Username** |  `admin`  
**Administrator Password** | Enter the administrator's password you have set in the run script of the sample application.  
**HTTP Operation Types** |  `__ACCOUNT__.Update=PUT`  
For more information about the fields of the **Configure Connectivity** section, see the table in [Enable and Configure Connectivity for Provisioning for Your Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/enable-and-configure-connectivity-provisioning-your-application.htm#enable-and-configure-connectivity-provisioning-your-application "Enable provisioning for your application and provide connectivity information for it. IAM uses this information to connect to your application's SCIM REST API endpoint for provisioning purposes.").
  8. To save the application, select **Finish**.

If you deploy and run the sample application in a non-HTTPS server or a server which doesn't contain a valid certificate, then you might need to use a REST API to change the `SSLEnabled` parameter to `false`. If the server doesn't listen to the default HTTP port number, then change the `Port` parameter to the corresponding port number your application runs. After you update these parameters you can test connectivity between the application and IAM, and then activate the application.
Was this article helpful?
YesNo

