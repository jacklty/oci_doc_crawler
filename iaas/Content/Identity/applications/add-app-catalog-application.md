Updated 2025-01-14
# Adding an App Catalog Application
Add an application from the App Catalog to an identity domain in IAM.
Oracle creates and maintains the App Catalog, which is a collection of application templates, and provides step-by-step instructions on how to configure most of the popular software-as-a-service (SaaS) applications, such as Amazon Web Services and Google Suite.
The configuration options for each Application Catalog application can differ slightly. The steps in this task are for a basic configuration.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select **Add application**. 
  4. In the **Add application** window, select **Application Catalog** , and then **Launch app catalog**.
  5. Find the application that you want by choosing a category (predefined by Oracle), searching for the application name, or selecting an integration filter. By default, all applications are shown.
  6. Select the application that you want to add.
  7. Enter a name and optional description for the application.
**Note**
For applications with lengthy names, the application name appears truncated in the **My Apps** page. Consider keeping application names as short as possible.
  8. (Optional) If applicable, enter a custom sign-in URL, which is URL to which users are redirected to sign in. If you're using a default sign-in page provided by Oracle, leave this field blank.
  9. (Optional) If applicable, enter a custom sign-out URL, which is the URL to which users are directed after the sign-out process. If you're using a default sign-in page provided by Oracle, leave this field blank.
  10. (Optional) In the **Custom error URL** field, enter the error page URL to which a user is redirected, after a failure. If you don't provide a value, the tenant-specific error page URL is used. If neither of those error URLs is configured, then the user is redirected to the IAM error page (/ui/v1/error). 
When a user tries to use social authentication (for example, Google or Facebook) to log into IAM, the custom social linking callback URL must be configured in the **Custom error URL** field. Social providers need this callback URL to call IAM and send the response back after social authentication. The provided callback URL is used to verify whether the user exists or not (after first-time social login), and displays an error if the social authentication has failed.
  11. In the **Custom social linking callback URL** field, enter the URL that IAM can redirect to after the linking of a user between social providers and IAM is complete.
When you create a custom app using the IAM custom SDK and integrate with IAM social login, the custom app needs to have the custom social linking callback URL.
  12. In the **Display settings** section, select **Display in My Apps**.
**Important** You must select this option for the app to be visible on the **My Apps** page.
Selecting this option doesn't enable or disable SSO to the app. The flag to enable or disable SSO comes from the app template.
  13. If you want the app to be listed in the **Catalog** , select **User can request access**. 
This option allows end users to request access to applications from their **My Apps** page by selecting **Add** and then selecting the app from the **Catalog**. 
**Tip** Don't forget to activate the application so that users can request access.
  14. In the **Authentication and authorization** section, select **Enforce grants as authorization** if you want to allow access to this app only if the user has been granted this app.
  15. Select **Show advanced options** to add tags to the application.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  16. Perform one of the following actions, depending on the application.
     * Select **Create application**. The application is added in a deactivated state. Skip to step 21.
     * Select **Next** and configure SSO.
  17. To import the IAM signing signature into the application, select **Download signing certificate**. This certificate is used by the SAML application to verify that the SAML assertion is valid.
To get the issuing IAM root certificate, see [Getting the Root CA Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/obtain-root-ca-certificate.htm#obtain-root-ca-certificate "When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.").
  18. To import the IAM identity provider metadata into the application, select **Download identity provider metadata**. The SAML application needs this information so that it can trust and process the SAML assertion that's generated by IAM as part of the federation process. This information includes, for example, profile and binding support, connection endpoints, and certificate information.
  19. Complete the **General** , **Additional configurations** , and **Attribute configuration** sections, as necessary.
  20. Under **Resources** , select **Users** to assign users to the application, and select **Groups** to assign groups to the application. 

The applications you assign to a user are displayed on the user's **My Apps** page. Newly assigned applications and applications that a user hasn't yet accessed appear first in the application list and have an asterisk icon in the application tile. The icon appears on the tile until the user accesses the application.
Was this article helpful?
YesNo

