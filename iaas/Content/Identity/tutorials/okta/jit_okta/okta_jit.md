Updated 2025-02-03
# JIT Provisioning from Okta to OCI IAM
In this tutorial, you configure Just-In-Time (JIT) provisioning between the OCI Console and Okta, using Okta as the identity provider (IdP).
You can set up JIT provisioning so that identities can be created in the target system at the time that they make a request to access the target system. This can be easier to set up than having all users created in advance.
This tutorial covers the following steps:
  1. Configure SAML attributes sent by Okta.
  2. Configure JIT attributes in OCI IAM.
  3. Test JIT provisioning between OCI IAM and Okta.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm)
To perform this tutorial, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Okta account with one of the following Okta roles:
    * Global Administrator
    * Cloud Application Administrator
    * Application Administrator


In addition, you must have completed the tutorial [SSO With OCI and Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm#sso-get-started "In this tutorial, you set up Single Sign-On between OCI and Okta, where Okta acts as the identity provider \(IdP\) and OCI IAM is service provider \(SP\)."), and collected the object ID of the groups which you are going to use for JIT Provisioning.
[1. Configure SAML Attributes Sent by Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm)
In OCI IAM, update the Okta IdP for JIT.
  1. Open a [supported browser ](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain which will be used to configure SSO.
  4. Sign in with your username and password.
  5. Open the navigation menu and select **Identity & Security**.
  6. Under **Identity** , select **Domains**.
  7. Select the identity domain in which you had configured Okta as IdP.
  8. Select Security in the left menu, and then **Identity providers**.
  9. Select the Okta IdP. 
  10. Select Configure JIT.
[![Configuration page for the Okta identity provider in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-config-iam.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-config-iam.png)
  11. On the Configure Just-in-time (JIT) provisioning page:
     * Select **Just-In-Time (JIT) provisioning**.
     * Select **Create a new identity domain user**.
     * Select **Update the existing identity domain user**.
[![enable just in time provisioning](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)
  12. Under Map User attributes:
    1. Leave the first row for `NameID` unchanged.
    2. For other attributes, under **IdP user attribute** select `Attribute`.
    3. Provide the IdP user attribute name as follows
       * familyName: `familyName`
       * primaryEmailAddress: `email`
    4. Select **Add Row** and enter: `firstName`.
For the identity domain user attribute, choose `First name`.
**Note** If you configured additional user attributes to be sent as part of the user assertion from Okta, you can map them to identity domain user attributes by adding additional rows.
  13. Select **Assign group mapping**.
  14. Enter the **Group membership attribute name**. In this tutorial, use `groups`.
**Note** Make a note of the group membership attribute name, because you'll use it in the next section.
  15. Select **Define explicit group membership mappings**.
  16. Under IdP group name maps to identity domain group name, do the following:
     * In **IdP Group name** , provide name of the group in Okta.
     * In **Identity domain group name** , and select the group in OCI IAM to map the Okta group to.
[![Assign group mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-map-gp-map.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-map-gp-map.png)
**Note** Additional groups can be mapped by selecting **Add Row**.
This diagram shows the attributes configured in Okta on the left, and attributes mapped in OCI IAM on the right. 
[![Mapping of group attributes between Okta and OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-okta-group-mapping.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/jit-okta-group-mapping.png)
  17. Under Assignment rules, select the following:
    1. When assigning group memberships: **Merge with existing group memberships**
    2. When a group is not found: **Ignore the missing group**
[![setting assignment rules](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-assign-rules.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-map-assign-rules.png)
**Note** Select options based on your organization's requirements.
  18. Select **Save changes**.


[2. Configure JIT attributes for OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm)
In Okta, update the OCI IAM app configuration to send user attributes and the group name in the SAML assertion.
  1. In Okta, in the enterprise application you created for OCI IAM, select the Sign On tab.
  2. Select **Edit** next to Settings.
  3. Under Saml 2.0, select **>** next to **Attributes (Optional)**.
  4. Provide the following values:
Name | Name format | Value  
---|---|---  
`firstName` | `Unspecified` | `user.firstName`  
`familyName` | `Unspecified` | `user.lastName`  
`email` | `Unspecified` | `user.email`  
You can add additional attributes to suit your business requirements, but you only need these for this tutorial.
[![Okta attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-attr.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-attr.png)
  5. Under Group Attribute Statements, enter these value.
**Note** Okta provides a mechanism for filtering groups which can be sent in SAML Assertion. The filter has options including `Starts with`, `Equals`, `Contains`, and `Matches regex`.In this tutorial, we use the `Contains` filter, which means that Okta only sends those groups which are associated with the user and which contain the specified string. In this example, we have specified `Admin` as the string, so all the groups which contain the string `Admin` and are associated with the user, are sent in the SAML Assertion.
Name | Name format | Filter | Value  
---|---|---|---  
`groups` | `Unspecified` | `Contains` | `Admin`  
[![Okta group attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-attr2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-attr2.png)
  6. Select **Save**.


[3. Test JIT Provisioning Between Okta and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm)
In this section, you can test that JIT provisioning works between Okta and OCI IAM.
  1. In the Okta console, create a new user with an email Id which is not present in OCI IAM.
  2. Assign the user to the required groups, for example, `Administrators and Admins`.
  3. Log out of Okta.
  4. Assign the user to the OCI IAM app in Okta.
[![User in Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-iam-user.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-iam-user.png)
  5. In the browser, open the OCI Console.
  6. Select the identity domain in which JIT configuration has been enabled.
  7. From the sign in options, select **Okta**.
  8. On the Okta login page, provide the newly created user id.
  9. On successful authentication from Okta:
     * The user account is created in OCI IAM.
     * The user is logged into the OCI Console.
[![My Profile in OCI IAM for user](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test3.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-test3.png)
  10. In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see. Check the user properties such as email id, first name, last name, and associated groups.
[![Check user properties in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-test4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-jit-test4.png)


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm)
Congratulations! You have successfully set up JIT provisioning between Okta and IAM.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

