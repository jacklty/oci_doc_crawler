Updated 2025-01-14
# JIT Provisioning from ADFS to OCI IAM
In this tutorial, you configure Just-In-Time (JIT) Provisioning between the OCI and Microsoft ADFS, where ADFS acts as the IdP.
You can set up JIT provisioning so that identities can be created in the target system during run time, as and when they make a request to access the target system.
This tutorial covers the following steps:
  1. Update the Relying Party configurations in ADFS.
  2. Update the ADFS IdP in OCI IAM for JIT.
  3. Test that you can provision users from ADFS to OCI IAM.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/jit_adfs/adfs_jit.htm)
To perform this tutorial, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An ADFS installation. 
**Note** This tutorial describes using the ADFS software provided with Microsoft Windows Server 2016 R2.
  * In addition, you must verify that:
    * The same user exists in OCI and ADFS.
    * ADFS is working.


[1. Update the Trusted Relying Party Configurations in ADFS](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/jit_adfs/adfs_jit.htm)
  1. Open the ADFS management utility. For example, in Windows 2016 Server Manager utility, select **Tools** , then select **Microsoft Active Directory Federation Services Management**.
  2. Under ADFS, select **Relying Party Trusts**.
  3. Right-click the Relying Partying Trust you previously configured for OCI called `OCI IAM` in the tutorial [SSO Between OCI and ADFS](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm#azure-sso "In this tutorial, configure SSO between the OCI IAM and ADFS, using ADFS as the identity provider \(IdP\).").
  4. Choose **Edit Claim Issuance Policy**.
  5. Edit the Email claim to add three additional claim rules for First Name, Last Name, and Group.
First Name attribute:
     * LDAP Attribute: `Given-Name`
     * Outgoing Claim Type: `Given Name`
Last Name attribute:
     * LDAP Attribute: `Surname`
     * Outgoing Claim Type: `Surname`
Group attribute:
     * LDAP Attribute: `Token-Groups - Unqualified Names`
     * Outgoing Claim Type: `Group`
  6. Select **OK** on the rules page, then **OK** again.


You can add additional attributes to suit your business requirements, but you only need these for this tutorial.
[2. Update the ADFS IdP in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/jit_adfs/adfs_jit.htm)
In the OCI IAM Console, configure the ADFS IdP for JIT.
  1. Open a [supported browser ](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain which will be used to configure SSO.
  4. Sign in with your username and password.
  5. Open the navigation menu and select **Identity & Security**.
  6. Under **Identity** , select **Domains**.
  7. Select the identity domain in which you have already configured ADFS as IdP in [step 1](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm#unique_641400847) of the tutorial "SSO Between OCI and ADFS".
  8. Select **Security** from menu on the left, and then **Identity providers**.
  9. Select the ADFS IdP.
**Note** This is the ADFS IdP you created as part of the tutorial [SSO Between OCI and ADFS](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm#azure-sso "In this tutorial, configure SSO between the OCI IAM and ADFS, using ADFS as the identity provider \(IdP\).").
  10. On the ADFS IdP page, select **Configure JIT**.
  11. On the Configure Just-in-time (JIT) provisioning page:
     * Select **Enable Just-In-Time (JIT) provisioning**.
     * Select **Create a new identity domain user**.
     * Select **Update the existing identity domain user**.
[![enable just in time provisioning](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-jit-config-jit.png)
  12. Under **Map user attributes** :
    1. Leave the first row for `NameID` unchanged.
    2. For other attributes, under **IdP user attribute** select `Attribute`.
    3. Provide the IdP user attribute name as follows:
       * familyName: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
       * primaryEmailAddress: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
    4. Select **Add Row** :
       * Under **IdP user attribute** select `Attribute`.
       * For IdP user attribute name, enter `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
[![Mapping of attributes between ADFS and OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-jit-attrib.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-jit-attrib.png)
  13. Select **Assign group mapping**.
  14. Enter the **Group membership attribute name**. Use `http://schemas.xmlsoap.org/claims/Group`.
  15. Select **Define explicit group membership mappings**.
  16. Under **IdP group name maps to identity domain group name** , do the following:
     * In **IdP Group name** , provide the name of the group in ADFS which will be present in the SAML assertion sent by ADFS.
     * In **Identity domain group name** , in OCI IAM select the group in OCI IAM to be mapped to the corresponding group in ADFS.
[![Assign group mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-jit-2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-jit-2.png)
  17. Under **Assignment rules** , select the following:
    1. When assigning group memberships: **Merge with existing group memberships**
    2. When a group is not found: **Ignore the missing group**
**Note** Select options based on your organization's requirements.
  18. Select **Save changes**.


[3. Test JIT Provisioning Between ADFS and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/jit_adfs/adfs_jit.htm)
In this section, you can test that JIT provisioning works between ADFS and OCI IAM
  1. In ADFS, create a user in ADFS which doesn't exist in OCI IAM.
  2. Restart your browser, and enter the Console URL to access the OCI Console:
`cloud.oracle.com`
  3. Enter the **Cloud Account Name** , also referred to as the tenancy name, and select **Next**.
  4. Select the identity domain in which JIT configuration has been enabled.
  5. From the sign in options, select **ADFS**.
[![ADFS icon on sign in page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-login.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-login.png)
  6. On the ADFS login page, provide the newly created user's credentials.
  7. On successful authentication, an account is created for the user in OCI IAM and the user is signed in to the OCI Console.
You can view the new user in the OCI domain, and verify that it has the same identity attributes and group memberships as you entered.


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/jit_adfs/adfs_jit.htm)
Congratulations! You have successfully set up JIT provisioning between ADFS and OCI IAM.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

