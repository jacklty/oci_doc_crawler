Updated 2024-12-18
# User Credentials
There are several types of credentials that you manage with Oracle Cloud Infrastructure Identity and Access Management (IAM):
  * **Console password:** For signing in to the Console, the user interface for interacting with Oracle Cloud Infrastructure. Note that federated users can't have Console passwords because they sign in through their identity provider. See [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top).
  * **API signing key (in PEM format):** For sending API requests, which require authentication.
  * **Auth token:** An Oracle-generated token that you can use to authenticate with third-party APIs. For example, use an auth token to authenticate with a Swift client when using Recovery Manager (RMAN) to back up an Oracle Database System (DB System) database to Object Storage.
  * **Customer Secret Keys:** For using the Amazon S3 Compatibility API with Object Storage. See [Amazon S3 Compatibility API](https://docs.oracle.com/iaas/Content/Object/Tasks/s3compatibleapi.htm).
  * **OAuth 2.0 Client Credentials:** For interacting with the APIs of those services that use OAuth 2.0 authorization. See [OAuth 2.0 Client Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#OAuth_20_Credentials).
  * **SMTP Credentials:** For using the [Overview of the Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).
  * **IAM Database Password:** Users can create and manage their database password in their IAM user profile and use that password to authenticate to databases in their tenancy. See [IAM Database Passwords](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#usercredentials_iam_db_pwd "Manage your IAM database passwords overview.").


**Important** API signing keys are different from the SSH keys you use to access a compute instance (see [Security Credentials](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/credentials.htm#Security_Credentials)). For more information about API signing keys, see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). For more information about instance SSH keys, see [Managing Key Pairs](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
## User Password 🔗 
The administrator who creates a new user in IAM also needs to generate a one-time Console password for the user (see [To create or reset another user's Console password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create_password)). The administrator needs to securely deliver the password to the user by providing it verbally, printing it out, or sending it through a secure email service. 
When the user signs in to the Console the first time, they'll be immediately prompted to change the password. If the user waits more than 7 days to initially sign in and change the password, it will expire and an administrator will need to create a new one-time password for the user.
Once the user successfully signs in to the Console, they can use Oracle Cloud Infrastructure resources according to permissions they've been granted through policies. 
**Note**
A user automatically has the ability to change their password in the Console. An administrator does not need to create a policy to give a user that ability.
### Changing a Password 🔗 
If a user wants to change their own password _sometime after_ they change their initial one-time password, they can do it in the Console. Remember that a user can automatically change _their own_ password; an administrator does not need to create a policy to give the user that ability. 
For more information, see [To change your Console password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#change_password). 
### If a User Needs Their Console Password Reset 🔗 
If a user forgets their Console password and also has no access to the API, they can use the Console's **Forgot Password** link to have a temporary password sent to them. This option is available if the user has an email address in their user profile. 
If the user does not have an email address in their user profile, then they need to ask an administrator to reset their password for them. All administrators (and anyone else who has permission to the tenancy) can reset Console passwords. The process of resetting the password generates a new one-time password that the administrator needs to deliver to the user. The user will need to change their password the next time they sign in to the Console. 
If you're an administrator who needs to reset a user's Console password, see [To create or reset another user's Console password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create_password).
### If a User Is Blocked from Signing In to the Console 🔗 
If a user tries 10 times in a row to sign in to the Console unsuccessfully, they will be automatically blocked from further attempts. They'll need to contact an administrator to get unblocked (see [To unblock a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#unblock_user)). 
## API Signing Keys 🔗 
A user who needs to make API requests must have an **RSA public key in PEM format (minimum 2048 bits)** added to their IAM user profile and sign the API requests with the corresponding private key (see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm)). 
**Important** A user automatically has the ability to generate and manage _their own_ API keys in the Console or API. An administrator does not need to write a policy to give the user that ability. Remember that a user can't use the API to change or delete their own credentials until they themselves save a key in the Console, or an administrator adds a key for that user in the Console or the API.
If you have a non-human system that needs to make API requests, an administrator needs to create a user for that system and then add a public key to the IAM service for the system. There's no need to generate a Console password for the user.
For instructions on generating an API key, see [To add an API signing key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#upload_key). 
## OAuth 2.0 Client Credentials 🔗 
**Note** OAuth 2.0 Client Credentials are not available in the United Kingdom Government Cloud (OC4).
OAuth 2.0 client credentials are required to interact programmatically with those services that use the OAuth 2.0 authorization protocol. The credentials enable you to obtain a secure token to access those service REST API endpoints. The allowed actions and endpoints granted by the token depend on the scopes (permissions) that you select when you generate the credentials. For more information, see [Working with OAuth 2.0 Client Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#oauth).
## Auth Tokens 🔗 
Auth tokens are authentication tokens generated by Oracle. You use auth tokens to authenticate with third-party APIs that do not support the Oracle Cloud Infrastructure signature-based authentication, for example, the Swift API. If your service requires an auth token, the service-specific documentation instructs you to generate one and how to use it.
## IAM Database Passwords 🔗 
Manage your IAM database passwords overview.
### Overview 🔗 
An IAM database password is a different password than an Console password. Setting an IAM database password allows an authorized IAM user to sign in to one or more Autonomous Databases in their tenancy.
Centralizing user account management in IAM improves security and greatly minimizes database administrators having to manage users who are joining, moving within, and leaving an organization (also known as user lifecycle management). Users can set a database password in IAM and use that password to authenticate when logging in to appropriately configured Oracle databases in their tenancy.
### Easy to use 🔗 
Database end users can continue to use existing supported database clients and tools to access the database. However, instead of using their local database username and password, they use their IAM username and IAM database password. You can access database passwords that you manage through your OCI profile only after you successfully authenticate to OCI. This means administrators can create an extra layer of protection before users can access or manage their database password. They can enforce multifactor authentication on their Console password using, for example, FIDO authenticator, or push notifications through authenticator apps. 
### Supported Functions 🔗 
IAM database passwords support associating a database password directly with an IAM user. After you set a database password in IAM, you can use it to sign in to your IAM database in your tenancy, if you have been authorized to access the IAM database. You must be mapped to a global database schema to be authorized to access the database. See [Authenticating and Authorizing IAM Users for Oracle DBaaS Databases](https://docs.oracle.com/en/database/oracle/oracle-database/23/dbseg/authenticating-and-authorizing-iam-users-oracle-dbaas-databases.html#GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8) in the Oracle Database Security Guide for more information about mapping global database users to IAM users and groups. 
### Password Security 🔗 
IAM administrators can impose extra security access layers by enabling multifactor authorization before a user can access a database password in IAM. See [Authenticating and Authorizing IAM Users for Oracle DBaaS Databases](https://docs.oracle.com/en/database/oracle/oracle-database/23/dbseg/authenticating-and-authorizing-iam-users-oracle-dbaas-databases.html#GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8) in the Oracle Database Security Guide for more information about how IAM users authenticate and authorize to OCI databases. 
[Creating an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm)
You can manage your own IAM database password with the Console, including creating, changing and deleting it.
Creating an IAM database password follows the same rules as creating an Console password except that the double quote character (") is not allowed in the IAM database password. See [About the Password Policy Rules](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpasswordrules.htm) for the rules to create Console passwords.
To create your own IAM database password, see [To create an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#to_create_an_iam_password "Use the Console to create a database password.").
[Changing an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm)
Managed your own IAM database password.
You can manage your own IAM database password with the Console, including creating, changing and deleting it. To change an existing password, delete the existing password and add the new password. See [To change an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#change_iam_db_pwd "Use the Console to change a database password.").
[Deleting an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm)
Managing your IAM database password.
You can manage your own IAM database password with the Console, including creating, changing and deleting it. To delete your IAM database password, see [To Delete an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#delete_iam_db_password).
### IAM Database Password Lockouts 🔗 
A user's account gets locked if the user encounters 10 consecutive failed sign-in attempts.
IAM database and Console users are locked out after 10 consecutive failed sign-in attempts (total for both passwords). Only an IAM administrator can unlock your user account.
  * If you fail to sign in to IAM or the database after 10 consecutive attempts (total for both), your account is locked and you cannot sign in to either your database or the Console.
  * When you are locked out, an IAM administrator must explicitly unlock your account.
  * IAM does not support automatic unlocking.
  * A failed login count is tracked centrally across all regions in a realm. Failed logins are recorded in your home region and replicated to their subscribed regions.


#### **Failed login attempts** 🔗 
## Working with IAM Database User Names 🔗 
You can manage your own IAM database user name with the Console, including creating, changing, and deleting it.
You might need to change the database user name:
  * If your user name is too long or hard to type
  * To make logging in easier with a user name that does not include special characters and may be shorter


The following topics explain how to manage an IAM database user name.
  * [To create an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create_iam_db_username "Use the Console to create a database user name.")
  * [To change an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#to_change_an_iam_db_username "Use the Console to change a database user name.")
  * [To delete an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#managingcredentials_topic-to_delete_an_iam_database_user_name "Use the Console to delete a database user name.")


Was this article helpful?
YesNo

