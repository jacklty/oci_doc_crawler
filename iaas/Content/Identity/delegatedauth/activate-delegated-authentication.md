Updated 2025-01-14
# Activating Delegated Authentication
After verifying that the Microsoft Active Directory (AD) credentials of a user in the domain associated with an AD bridge can be used to sign in to IAM, activate delegated authentication for the AD domain. Users transferred into IAM through this AD domain use their AD passwords to authenticate into IAM.
To perform those verification steps, see [Testing Delegated Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/test-delegated-authentication.htm#test-delegated-authentication "Verify that a user's Microsoft Active Directory \(AD\) credentials from a domain associated with an AD Bridge can be used to sign in to IAM. This way, if there are any issues, then you can resolve them before activating delegated authentication for the AD domain.").
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security**.
  4. Select **Delegated Authentication**.
  5. Expand the node to the right of the AD Bridge for which you want to activate delegated authentication.
  6. Turn on the **Activate Delegated Authentication** switch.
**Activate delegated authentication** might be unavailable (that is, you can't turn the switch on or off) for one of the following reasons:
     * The status of the AD Bridge is `No Clients Found`. You can't activate delegated authentication for the AD domain because the AD domain doesn't work until you install a client for the AD domain. Select **Select here to download the client** to download the client for the AD domain.
     * The status of the AD Bridge is `Incompatible Client Found`. You can't activate delegated authentication for the AD domain because the AD domain doesn't work until you install the correct version of the client for the AD domain. Select **Select here to download the client** to download the updated client for the AD domain.
     * The AD Bridge isn't configured for delegated authentication. To configure it:
       1. Select the AD domain.
       2. Select **Configuration**.
       3. In the **Configure the Microsoft Active Directory Domain** page, scroll down until you see the Authentication Settings area.
       4. Select **Enable local authentication**.
       5. Select **Save**.
       6. In the **Save Configuration Changes?** dialog box, select **OK**.
  7. In the **Confirmation** window, select **Activate delegated authentication**.


Was this article helpful?
YesNo

