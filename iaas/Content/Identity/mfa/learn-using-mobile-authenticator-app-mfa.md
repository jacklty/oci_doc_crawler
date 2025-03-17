Updated 2024-09-30
# Using Mobile Authenticator Apps with MFA
Using a mobile authenticator application for MFA in an identity domain in IAM provides a second factor of authentication in the form of a time-based one-time passcode (OTP) or push notification, and offers several options for implementing app protection and compliance policy.
A mobile authenticator app is a soft token that's installed on a mobile device. A mobile authenticator app uses either OTP or push notifications to prove that the user has possession of the mobile device. Only the mobile authenticator app that's in possession of the user's secret key can generate a valid OTP. During MFA enrollment, when a user scans the Quick Response (QR) code or uses the enrollment URL, the mobile authenticator app is automatically configured with the IAM server. The mobile authenticator app retrieves a secret key, which is required to generate the OTP and to receive push notifications on the mobile authenticator app. That secret key is then shared between the client and the IAM server. If the user is enrolling offline, IAM shares the secret with the Mobile Authenticator through a QR Code. If the user is enrolling online, IAM shares the secret with the Mobile Authenticator through the enrollment notification. 
A user can use the mobile authenticator app to generate an OTP both online or offline. However, registering for push notifications and performing device compliance checks (jailbreak detection/PIN protection) can only be done while online.
  * **Mobile App Passcode** : Use a mobile authenticator app, such as the Oracle Mobile Authenticator app, to generate an OTP. A new OTP is generated every 30-60 seconds and is valid for 90-180 seconds. After the user enters their username and password, a prompt appears for the passcode. After generating the passcode using the mobile authenticator app, the user enters that code as the second verification method.


  * **Mobile App Notification** : Send a push notification to the OMA app that contains an approval request to allow or deny a login attempt. After the user enters their username and password, a login request is sent to their phone. The user taps **Allow** to authenticate.


**Note**
  * The OMA app is available for Android, iOS, and Windows operating systems.
  * To learn how to configure mobile passcodes and notifications, see [Configuring Mobile OTP and Notifications](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-mobile-otp-and-notifications.htm#configure-mobile-otp-and-notifications "Configure a policy an identity domain in IAM for the time-based one-time passcode \(OTP\), and protection and compliance policies for the Oracle Mobile Authenticator \(OMA\) app.").
  * During MFA enrollment, a user must enter the key manually or use the enrollment URL when using the OMA app on a Surface Pro or Windows Desktop device. The QR code scanner can't be used because of a camera limitation. When a user enters that key manually, the OMA app supports only BASE32 encoding.


When you enable both the **Mobile App Passcode** and **Mobile App Notification** factors and a user is enrolled in Mobile App as a second method of verification, the Mobile App Notification factor is the default that's presented to the user. Users can change which factor they want to use by either selecting a different backup verification method when signing in or by selecting a different method as their default option. IAM users can use the OMA app or any supported third-party authenticator app that they want to generate OTPs. However, users must use the OMA app to receive push notifications.
IAM works with any third-party authenticator app (such as Google Authenticator) that adheres to the TOTP: Time-Based One-Time Password Algorithm specification. No special administrator configuration steps for third-party authenticator apps are required. When a user enrolls in MFA and selects **Mobile App** as the method, the user can either select the **Enter Key Manually** or **Offline Mode or Use Another Authenticator App** options to set up third-party authenticators. We recommend the use of the OMA app as it supports notifications and security features such as app protection policy, compliance policy, and silent key refresh.
Was this article helpful?
YesNo

