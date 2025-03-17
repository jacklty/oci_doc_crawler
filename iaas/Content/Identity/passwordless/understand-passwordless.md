Updated 2025-01-14
# Understanding Passwordless Authentication
Passwordless authentication lets users sign in without entering their username and password every time.
The first time the user signs in, they enter their username and password on the standard sign-in page. The next time, and on future occasions, the user is shown two pages when they sign in. In the first page, the user provides their username, and then clicks **Sign in**. IAM evaluates the criteria in the identity provider policies to determine which identity providers and local authentication factors (such as **Email** , **Mobile App notification** , or **Mobile App passcode**) are available to use to sign in to IAM. These identity providers and local authentication factors appear in the second sign in page. The user uses one of the identity providers or authentication factors to access IAM.
Passwordless authentication is sometimes confused with Multi factor Authentication (MFA). Both MFA and passwordless authentication use a wide variety of authentication factors, but MFA is often used as an extra layer of security on top of regular password-based authentication. Whereas passwordless authentication doesn't require a memorized secret and usually uses just one secure factor to authenticate identity, making it faster and simpler for users.
If you later choose to turn off passwordless authentication, then the user can authenticate into IAM at the sign-in page by providing their credentials (username and password), or by using a SAML or social identity provider.
To define passwordless authentication, you must be assigned to either the identity domain administrator role or the security administrator role.
## User Sign-In Experience 🔗 
After you have configured passwordless authentication for your users, their sign-in experience changes.
  1. The sign in page has only a username field. There isn't a password field.
  2. The user enters their username, and they select **Sign In**.
  3. A second page appears where they enter the verification required by the authentication factor you have chosen, for example a passcode in an email.
  4. If there is more than one passwordless authentication factor, the user can select **Show alternative login methods** to choose a different one.


Was this article helpful?
YesNo

