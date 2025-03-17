Updated 2023-11-20
# Using E-Business Suite Asserter: FAQ
This topic provides information about using the E-Business Suite Asserter.
[What is the E-Business Suite Asserter?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The IAM E-Business Suite Asserter is helps to simplify the deployment topology for Oracle E-Business Suite single sign-on (SSO) by replacing Oracle Access Manager and Oracle Internet Directory with IAM.
[How does the asserter work?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter works by using the OAuth protocol to get an access token from IAM which provides information about the user and the user's authentication. The asserter uses this token to generate a session cookie which is sent to Oracle E-Business Suite.
[What are the components needed for the asserter to work?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter is a lightweight Java application which needs to be deployed on Oracle WebLogic server. It can be deployed on both cloud and on-premises WebLogic Servers.
[Does the asserter support high availability?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
Yes, the asserter supports high availability (HA). Two or more separate nodes of the asserter can be deployed in the same environment and traffic to them can be managed using a Load Balancer. You can find detailed instructions for deploying and configuring the asserter in HA mode in the Solutions Playbook [Learn About Enabling SSO for Oracle E-Business Suite with OCI IAM using EBS Asserter in High Availability Mode](https://docs.oracle.com/en/solutions/ebs-asserter-ha/).
[Can custom properties for user.identifier be added?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
Yes, you can add a custom property to `user.identifier` to the properties file `Bridge.property`. The value that's fetched is a unique user from the Oracle E-Business Suite based on the `ebs.identifier` (username/email).
See [Updating the E-Business Suite Asserter Configuration File](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/update-ebs-asserter-configuration-file.htm#update-ebs-asserter-configuration-file "After you register the IAM E-Business Suite Asserter \(EBS Asserter\), you can configure the asserter configuration file to connect with IAM during authentication.").
[Does the asserter support integration with third-party IdPs for SSO?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter doesn't directly integrate with third-party IdPs, but it integrates with OCI IAM and Oracle Identity Cloud Service which support integration with third-party IdPs such as Microsoft Azure AD, Okta, and ADFS. These let organizations to sign in to Oracle eBusiness Suite applications using the third-party IdP credentials.
[Can the asserter be used to provision user accounts from OCI IAM and Oracle Identity Cloud Service to Oracle E-Business Suite applications?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter can only be used to sign users in to Oracle eBusiness Suite applications using their OCI IAM and Oracle Identity Cloud Service credentials. To provision user accounts from IAM into Oracle eBusiness Suite, use a [provisioning bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/managing-provisioning-bridge.htm#understand-provisioning-bridge "The provisioning bridge provides a link between your on-premises apps and IAM. Through synchronization, account data that's created and updated directly on the apps is pulled into an identity domain and stored for the corresponding identity domain users and groups. As a result, any changes to these records are transferred into an identity domain. So, if a user is deleted in one of your apps, then this change is propagated into the identity domain. Because of this, the state of each record is synchronized between your apps and the identity domain.").
[Does the asserter need an extra license from Oracle?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter doesn't incur extra charges for its usage. However the asserter is only available with the Standard License for Oracle Identity Cloud Service, and with the IAM identity domain types Oracle Apps Premium, Premium, and External Domains.
[Does the asserter include a WebLogic license?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The right to use Oracle E-Business Suite Asserter also includes the right to use WebLogic Server Enterprise Edition solely for the purposes of running the asserter application in accordance with all terms and conditions as described in the [Oracle Fusion Middleware Licensing Information User Manual](https://docs.oracle.com/en/middleware/fusion-middleware/fmwlc/).
[Which versions of WebLogic Server does the asserter work with?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
The asserter only works with the Standard version of Oracle WebLogic Server.
[Does the asserter support proxy configurations?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
Yes, Proxy configuration are configured in the `bridge.properties` file. See [Updating the E-Business Suite Asserter Configuration File](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/update-ebs-asserter-configuration-file.htm#update-ebs-asserter-configuration-file "After you register the IAM E-Business Suite Asserter \(EBS Asserter\), you can configure the asserter configuration file to connect with IAM during authentication.").
[Can we use the OCI IAM SSO only for the Oracle E-Business Suite and disable SSO for other modules?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
Yes, SSO can be enabled for only the E-Business Suite application modules and disabled for other modules such as iSupplier. You do this by configuring the Applications SSO Type (APPS_SSO) profile for both SITE and SERVER level, where `SITE` level is set to `SSWA/wSSO` and `SERVER` level is set to `SSWA`.
[Does the asserter support Simplified Chinese language?](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/faq_using-ebs-asserter-faq.htm)
Yes, simplified Chinese is supported by the asserter.
Was this article helpful?
YesNo

