Updated 2023-06-28
# Adding Applications
You can add Custom Applications, if you're assigned to either the identity domain administrator role or the application administrator role.
See [Assigning Users to Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-users-roles.htm#top "Assign users in an OCI IAM identity domain to a role.") for information about assigning users to administrator roles.
You can add the following types of custom applications in IAM:
  * App Catalog application: Add an application from the Application Catalog, which contains pre-configured application templates.
  * Security Assertion Markup Language (SAML) application: Accessed by multiple users and hosted in a secure and protected place (server). Create a SAML application that supports SAML for single sign-on. This allows users to single sign-on (SSO) into your software as a service (SaaS) applications that support SAML for SSO.
  * Mobile application: Hosted directly on the resource owner's browser, machine, or mobile device. An example of this type of application is an Android or iPhone application. A mobile application can run in multiple environments outside of your control. Since these environments aren't trusted, this type of application has reduced integration options.
  * Confidential application: Accessed by multiple users and hosted in a secure and protected place (server). The application uses OAuth 2.0. Applications that can protect their OAuth client id and client secret are called confidential applications
  * Enterprise application: Web applications that require App Gateway to integrate with IAM for authentication purposes. App Gateway passes HTTP headers to the application after authenticating and authorizing user's access.


**Tip**
  * You can access the [Onboarding Applications](http://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:12417) infographic to see how to add custom applications in IAM.
  * You can access the [Integrating a Custom Client Application](http://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:13427) tutorial to see how to integrate a custom client application with IAM.
  * You can access the [Integrating a Custom Resource Server Application](http://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:13428) tutorial to see how to integrate a custom resource server application with IAM.
  * See [Manage IAM App Gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/understand-app-gateway.htm#understand-administrator-roles "App Gateway is a software appliance that lets you integrate applications hosted either on a compute instance, in a cloud infrastructure, or in an on-premises server with IAM for authentication purposes.") for information on integrating an enterprise application with IAM.


Was this article helpful?
YesNo

