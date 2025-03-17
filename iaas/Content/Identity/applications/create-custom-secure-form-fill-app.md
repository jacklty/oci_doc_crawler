Updated 2023-06-28
# Creating a Custom Secure Form Fill App
Custom secure form fill apps give you the flexibility to define tenant-level form fill apps that aren't in the global Oracle App Catalog.
Secure Form Fill is the IAM alternative for single sign-on into apps that require auto-form fill but don't support OAuth, SAML, or federated sign-on methods.
Users enter their application credentials for form-fill-enabled apps in IAM once. IAM stores and encrypts the information, and automatically fills in the login form so that users can sign in without having to reenter the information each time.
IAM stores the user's credentials in an encrypted format using strong encryption combined with a customer-specific private key. When a user opens the secure form fill application, which in turn prompts the login page, IAM detects and securely fills the user's credentials, submits the credentials to the app login page, and then the user is automatically signed in.
Was this article helpful?
YesNo

