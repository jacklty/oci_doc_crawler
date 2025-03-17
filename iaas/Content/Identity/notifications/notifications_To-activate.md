Updated 2025-01-14
# Activating Notifications for an Identity Domain
Activate email notifications for an identity domain in IAM.
If you have configured a non-Oracle domain as the From email address for your notifications, then you must first configure the email authentication settings for Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) so that you can certify the domain. Oracle Support must help with this configuration. See [Configuring Email Authentication Settings for SPF and DKIM](https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/configure-email-auth-spf-dkim.htm#configure-email-auth-spf-dkim "If you have configured a non-Oracle domain as the From Email Address for your notifications, then you must configure the email authentication settings for Sender Policy Framework \(SPF\) and DomainKeys Identified Mail \(DKIM\) so that you can certify the domain. Oracle Support must help with the configuration."). 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Notifications**
  4. To activate notifications, turn on **Enable notifications for all identity domain users**.
  5. Select whether to verify the sender's domain or email address:
     * To send a validation email to the postmaster account of the email's domain, select **Verify sender's domain**. After the domain is verified, any email address from the domain is valid.
     * To send a validation email to the email address that you enter in the **Sender's email address** field, select **Verify sender's email address**. Unlike the **Verify sender's domain** option, a validation is initiated for every email address even though they're from the same domain.
  6. In the **Sender's email** address field, enter the email address that will appear in the **From** email field for all notifications.
  7. Select **Save changes**.
     * If you selected **Verify sender's domain** in step 5, then an email notification is sent to the postmaster to verify the email address and validate the domain associated with the address. 
     * If you selected **Verify sender's email** address, then a validation email is sent to the email address that you entered in the **Sender's email address** field.
  8. In the confirmation window, select **Save changes**.
  9. If you don't see a **Verified** status, then select **Check Status**.
IAM checks the status of the email verification. If it's verified, then the status changes to **Verified**. If it's not verified, then perform one of the following actions:
     * If the email address isn't verified, then access the notification that's sent to the email address you provided, select the verification link in the notification, and select **Check Status** again. The status will changes to **Verified**.
     * If the domain isn't verified, then contact the postmaster of your company so that the postmaster can verify the domain associated with the email address.


Was this article helpful?
YesNo

