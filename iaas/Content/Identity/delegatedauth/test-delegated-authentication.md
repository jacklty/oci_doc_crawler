Updated 2025-01-14
# Testing Delegated Authentication
Verify that a user's Microsoft Active Directory (AD) credentials from a domain associated with an AD Bridge can be used to sign in to IAM. This way, if there are any issues, then you can resolve them before activating delegated authentication for the AD domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security**.
  4. Select **Delegated Authentication**.
  5. Expand the node to the right of the AD Bridge for which you want to test delegated authentication.
  6. Select **Test Delegated Authentication**.
  7. In the **Test Delegated Authentication** window, enter the AD user name and password that you want to use to sign in to IAM.
  8. Select **Test**.
If the test fails and you can't sign in with the AD user name and password:
     * Check that you are using the correct credentials, or try testing using another AD user name and password.
     * Consult the [troubleshooting information](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/ms_ad_bridge.htm#trouble_ms_ad_bridge "Learn how to troubleshoot common Active Directory \(AD\) issues.") for working with an AD bridge.


Was this article helpful?
YesNo

