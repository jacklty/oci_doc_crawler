Updated 2023-06-08
# Testing Authentication for E-Business Suite Mobile Applications
Test the authentication of the Oracle E-Business mobile applications in scenarios in which E-Business Suite uses IAM E-Business Suite Asserter.
If you configured E-Business Suite Mobile Applications to use IAM EBS Asserter, then you perform the following test:
  1. Use your mobile device to open the Oracle E-Business mobile application and access a protected feature.
The mobile device opens IAM **Sign In** page.
  2. Sign in to IAM.
After successful authentication, the mobile application completes the login process and activates the requested feature.


The mobile application completes the login flow and shows the protected feature only if it detects a successful return that redirects to the URL configured in the **Login Success URL** parameter.
Was this article helpful?
YesNo

