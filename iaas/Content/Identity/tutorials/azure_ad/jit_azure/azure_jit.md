Updated 2025-02-03
# JIT Provisioning from Entra ID to OCI IAM
In this tutorial, you configure Just-In-Time (JIT) Provisioning between between the OCI Console and Entra ID, using Entra ID as the IdP.
You can set up JIT provisioning so that identities can be created in the target system during run time, as and when they make a request to access the target system.
This tutorial covers the following steps:
  1. Configure the Entra ID IdP in OCI IAM for JIT.
  2. Update the OCI IAM app configuration in Entra ID.
  3. Test that you can provision from Entra ID to OCI IAM.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm)
To perform this tutorial, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Entra ID account with one of the following Entra ID roles:
    * Global Administrator
    * Cloud Application Administrator
    * Application Administrator


In addition, you must have completed the tutorial [SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#azure-sso "In this tutorial, configure SSO between the OCI IAM and Microsoft Entra ID, using Entra ID as the identity provider \(IdP\)."), and collected the object ID of the groups which you are going to used for JIT Provisioning.
[1. Configure SAML Attributes Sent by Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm)
In order to JIT Provisioning to work, appropriate and required SAML attributes have to be configured, which will be sent in SAML Assertion to OCI IAM by Entra ID.
  1. In the browser, sign in to Microsoft Entra ID using the URL:```
https://entra.microsoft.com
```

  2. Navigate to **Enterprise Applications**.
  3. Select the Oracle Cloud Infrastructure Console application.
**Note** This is the app you created as part of [SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#azure-sso "In this tutorial, configure SSO between the OCI IAM and Microsoft Entra ID, using Entra ID as the identity provider \(IdP\).").
  4. In the left menu, select **Single sign-on**.
  5. In the Attributes and Claims section, select **Edit**.
  6. Verify that the attributes are properly configured:
     * `NameID`
     * `Email Address`
     * `First Name`
     * `Last Name`
If you require new claims, add them.
  7. Make a note of all the configured claim names. For example
`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
is the claim name for `First Name`.
[![Attributes and claims](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-claim2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-claim2.png)
  8. Navigate to **Groups**. You'll see all the groups available in Entra ID.
  9. Make a note of Object ids of the groups want to make part of SAML to send to OCI IAM.
[![Group details in Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-group-id.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-group-id.png)


**Additional Entra ID Configurations**
In Entra ID, you can filter groups based on the group name, or `sAMAccountName`, attribute.
For example, suppose only the `Administrators` group needs to be sent over using SAML:
  1. Select the group claim.
  2. In Group Claims, expand **Advanced options**.
  3. Select **Filter Groups**.
     * For **Attribute to match** , select `Display Name`.
     * For **Match with** , select `contains`.
     * For **String** , provide the name of the group, for example, `Administrators`.
[![Filter for groups](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure_filter_groups.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure_filter_groups.png)


Using this option, even if the user in the administrator group is part of other groups, Entra ID only sends the Administrators group in SAML.
**Note** This helps organisations to send only the required groups to OCI IAM from Entra ID.
[2. Configure JIT Attributes in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm)
In OCI IAM, update the Entra ID IdP for JIT.
  1. Open a [supported browser ](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain which will be used to configure SSO.
  4. Sign in with your username and password.
  5. Open the navigation menu and select **Identity & Security**.
  6. Under **Identity** , select **Domains**.
  7. Select the identity domain in which you have already configured Entra ID as IdP.
  8. Select **Security** from menu on the left, and then **Identity providers**.
  9. Select the Entra ID IdP.
**Note** This is the Entra ID IdP you created as part of [SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#azure-sso "In this tutorial, configure SSO between the OCI IAM and Microsoft Entra ID, using Entra ID as the identity provider \(IdP\).").
  10. On the Entra ID IdP page, select Configure JIT.
[![Configuration page for the Entra ID identity provider in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-iam.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-iam.png)
  11. On the Configure Just-in-time (JIT) provisioning page:
     * Select **Just-In-Time (JIT) provisioning**.
     * Select **Create a new identity domain user**.
     * Select **Update the existing identity domain user**.
[![enable just in time provisioning](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)
  12. Under Map User attributes:
    1. Leave the first row for `NameID` unchanged.
    2. For other attributes, under **IdP user attribute** select `Attribute`.
    3. Provide the IdP user attribute name as follows
       * familyName: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
       * primaryEmailAddress: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
    4. Select **Add Row** and enter: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`.
For the identity domain user attribute, choose `First name`.
**Note** The fully qualified display name (FQDN) is from [1. Configure SAML Attributes Sent by Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#jit-config-iam).
This diagram shows what the user attributes in OCI IAM should look like (on the right), and the mapping of user attributes between Entra ID and OCI IAM.
[![Mapping of user attributes between Entra ID and OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-azure-user-mapping.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-azure-user-mapping.png)
  13. Select **Assign group mapping**.
  14. Enter the **Group membership attribute name** : `http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`.
  15. Select **Define explicit group membership mappings**.
  16. In **IdP Group name** , provide the Object ID of the group in Entra ID from the previous step.
  17. In **Identity domain group name** , and select the group in OCI IAM to map the Entra ID group to.
[![Assign group mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-gp-map.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-gp-map.png)
This diagram shows what the group attributes in OCI IAM should look like (on the right), and the mapping of group attributes between Entra ID and OCI IAM.
[![Mapping of group attributes between Entra ID and OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-azure-group-mapping.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-azure-group-mapping.png)
  18. Under Assignment rules, select the following:
    1. **When assigning group memberships** : Merge with existing group memberships
    2. **When a group is not found** : Ignore the missing group
[![setting assignment rules](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-assign-rules.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-assign-rules.png)
**Note** Select options based on your organization's requirements.
  19. Select **Save changes**.


[3. Test JIT Provisioning Between Entra ID and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm)
In this section, you can test that JIT provisioning works between Entra ID and OCI IAM.
  1. In Entra ID console, create a new user with an email Id which is not present in OCI IAM.
  2. Assign the user to the required groups.
[![assign user to groups](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test-1.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test-1.png)
  3. In the browser, open the OCI Console.
  4. Select the identity domain in which JIT configuration has been enabled.
  5. Select **Next**.
  6. From the sign on options, select **Entra ID**.
  7. On the Microsoft login page, enter the newly created user id.
[![Microsoft login page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test-2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test-2.png)
  8. On successful authentication from Microsoft:
     * The user account is created in OCI IAM.
     * The user is logged into the OCI Console.
[![My Profile in OCI IAM for user](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test3.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test3.png)
  9. In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see. Check the user properties such as email id, first name, last name, and associated groups.
[![Check user properties in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test4.png)


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm)
Congratulations! You have successfully set up JIT provisioning between Entra ID and OCI IAM.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

