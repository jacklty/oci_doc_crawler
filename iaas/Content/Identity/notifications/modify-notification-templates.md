Updated 2025-03-05
# Modifying Notification Templates
Modify the notification templates for an identity domain in IAM to meet the business and security requirements for your enterprise applications.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Notifications**.
  4. Update the **Sender's email address** from the default `no-reply@...` to a valid email address. You must update the **Sender's email address** which then updates the **Sender** field on the template from the default `no-reply@...` to a valid email address.
  5. Select the **Email templates** tab.
**Tip** The notification templates that appear on the **Email templates** tab reflect the selections that you made on the **Configure** tab. See [Selecting Notifications](https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/select-notifications.htm#select-notifications "Select the notifications that you want the identity domain to send to users and administrators.").
  6. Expand a notification template.
  7. Expand a notification template that you want to modify, and make changes to the following values as needed. 
**Important** When you add or change a variable in an email template, ensure that you use the correct syntax. For example, to use the variable `user.displayName`, the correct syntax is `${user.displayName}`.
     * **Language** : Select the language for the notification. To see a preview of the notification in that language you select, scroll through the **Email body** text area.
     * **Encoding** : Verify that UTF-8 appears as the character encoding for the notification (for security, encryption, and backward-compatibility purposes). This character encoding can encode all possible characters of the notification, or code points, in Unicode.
     * **Sender** : Verify that the email address for this field matches the email address you entered in the **Sender's email address** field. This field is the email address that appears in the **From** email field for all notifications. If you haven't verified the domain or the email address, then this value is be the previously validated email address from the previously validated domain. As soon as the domain or the email address is validated (the status changes to **Verified**), then the verified email address appears in the **Sender** field for all notifications. 
     * **Subject** : Enter or provide variables for content that appears in the **Subject** field of the email notification.
     * **Email body** : Revise the content of the notification to meet your needs. In addition to a customization toolbar, you can use the following variables. These variables are replaced with values specific to your business at runtime. 
       * `${account.emailID}`: The email address of the user's account from which an attempt is made to sign in using a device, IP address, or web browser that the identity domain doesn't recognize.
       * `${actorDisplayName}`: The identity domain administrator's email address.
       * `${admin.resource.name}`: The name of the Kerberos application.
       * `${app.displayName}`: The display name of the application that contains the users, groups, application accounts, and entitlements that are synchronized into this identity domain.
       * `${app.id}`: The ID of the application that contains the users, groups, application accounts, and entitlements that are synchronized into this identity domain.
       * `${authentication.targetApp}`: The name of the Microsoft Active Directory domain that contains the account of the user who's authenticating into this identity domain.
       * `${bypasscode.expiry}`: The time (in minutes) before a bypass code expires.
       * `${bypasscode.usage}`: How many times a bypass code can be used.
       * `${bypasscode.value}`: The bypass code that the user or administrator generates for use as part of the 2-Step Verification process.
       * `${companyName}`: The ID of the application that contains the users, groups, application accounts, and entitlements that are synchronized into this identity domain.
**Note** When you use the `${companyName}` variable, be sure to add your company name to the **Company name** field on the **Branding** page. If you don't, then your company's details won't appear in email notifications, SMS notifications, or in the Oracle Mobile Authenticator (OMA) app when a user completes MFA enrollment. See [Customizing the Sign-In Page Branding](https://docs.oracle.com/en-us/iaas/Content/Identity/brand/customizing-the-signin-page.htm#customize-sign-page "Customize the sign-in page options for an identity domain in IAM.") for more information about populating the **Company name** field.
       * `${contactEmails}`: The system administrator's email address.
       * `${date}`: The date associated with the action of the notification (for example, resetting a password).
       * `${device.ipAddress}`: The IP address from which an attempt is made to sign in to a user's account, but which the identity domain doesn't recognize.
       * `${device.enrollmentURL}`: The configuration URL that contains the parameters used to configure the Oracle Mobile Authenticator (OMA) app.
       * `${domain}`: The realm (or domain) that contains the Kerberos application.
       * `${domainName}`: The name of the domain that contains the Kerberos application.
       * `${email}`: The email address that appears in the **Sender's email address** field.
       * `${emailId}`: The user's email address.
       * `${end.dateTime}`: The date and time at which the job to synchronize users, groups, application accounts, and entitlements from an application into the identity domain finished
       * `${footerImage}`: The image that appears in the footer region of the notification.
       * `${headerImage}`: The image that appears in the header region of the notification.
       * `${homePageRedirectUrl}`: The redirect URL for the notification that can be used if the link in the notification doesn't work. This URL redirects users to the details page of the identity domain.
       * `${job.displayName}`: The display name of the job that's started, canceled, completed, or failed.
       * `${job.historyId}`: The ID number of the job that's started, canceled, completed, or failed.
       * `${kerberos.principalName}`: The Kerberos principal name that the user uses to access the Kerberos application to perform authentication to applications that support it.
       * `${linkExpirationTime}`: The date and time after which the link in the notification expires.
       * `${masked_UID}`: The account of the user who requests a one-time passcode (OTP) to enroll in 2–step verification.
       * `${OTP}`: The one-time passcode (OTP) that's sent to a user for the user to complete 2–step verification.
       * `${quota.limit}`: The allowable quota limit for the resource type. If an administrator can create 500,000 user accounts, then 500,000 represents the quota limit. 
       * `${quota.resourceType}`: The classification type of the identity domain entity (or resource) for which there is a quota limit (for example, users).
       * `${quota.usage}`: Records of the resource type that were created. If an administrator created 600,000 accounts, then 600,000 represents the quota usage.
       * `${redirectUrl}`: The redirect URL for the notification that can be used if the link in the notification doesn't work.
       * `${request.createdOn}`: The date and time that the request was created.
       * `${request.requestedItem}`: The groups or applications to which a user is requesting access.
       * `${request.requesteeDisplayName}`: The display name of the user who submitted a request for access to groups or applications.
       * `${start.dateTime}`: The date and time at which the job began to synchronize users, groups, application accounts, and entitlements from an application into the identity domain.
       * `${sync.status}`: The status of the job that's used to synchronize users, groups, application accounts, and entitlements from an application into the identity domain.
       * `${sync.summary}`: A summary of the synchronization job.
       * `${tenantName}`: The name of the identity domain (or tenant).
       * `${time}`: The time associated with the action of the notification.
       * `${user.displayName}`: The user's first name and last name (or display name).
       * `${user.userName}`: The user's username.
       * `${userToken}`: A token that the identity domain uses to identify the user.
       * `${validity}`: The amount of time (in minutes) after which the OTP is no longer valid. As a result, the user can't use it to enroll in 2–step verification.
  8. Select **Save template**.
  9. Select **Save changes**.
  10. In the confirmation window, select **Save changes**.


Was this article helpful?
YesNo

