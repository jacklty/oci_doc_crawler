Updated 2025-02-18
# Managing User Credentials
This topic describes the basics of working with Oracle Cloud Infrastructure Identity and Access Management (IAM) user credentials. If you're not already familiar with the available credentials, see [User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#User_Credentials). 
## Working with Console Passwords and API Keys 🔗 
Each user automatically has the ability to change or reset _their own_ Console password, as well as manage _their own_ API keys. An administrator does not need to create a policy to give a user those abilities.
**Note** Federated users might need to create a policy to modify API keys. For example, users who were provisioned through SCIM.
To manage credentials for users other than yourself, you must be in the Administrators group or some other group that has permission to work with the tenancy. Having permission to work with a compartment within the tenancy is not sufficient. For more information, see [The Administrators Group and Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#The). 
IAM administrators (or anyone with permission to the tenancy) can use either the Console or the API to manage all aspects of both types of credentials, for themselves and all other users. This includes creating an initial one-time password for a new user, resetting a password, uploading API keys, and deleting API keys. 
Users who are not administrators can manage _their own_ credentials. In the Console, users can:
  * Change or reset their own password.
  * Upload an API key in the Console for their own use (and also delete their own API keys).


And with the API, users can:
  * Reset their own password with [CreateOrResetUIPassword](https://docs.oracle.com/iaas/api/#/en/identity/latest/UIPassword/CreateOrResetUIPassword).
  * Upload an additional API key to the IAM service for their own use with [UploadApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/UploadApiKey) (and also delete their own API keys with [DeleteApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/DeleteApiKey)). Remember that a user can't use the API to change or delete their own credentials until they themselves upload a key in the Console, or an administrator uploads a key for that user in the Console or the API.


A user can have a maximum of three API keys at a time.
## Working with Auth Tokens 🔗 
**Note** "Auth tokens" were previously named "Swift passwords". Any Swift passwords you had created are now listed in the Console as auth tokens. You can continue to use the existing passwords.
Auth tokens are Oracle-generated token strings that you can use to authenticate with third-party APIs that do no support Oracle Cloud Infrastructure's signature-based authentication. Each user created in the IAM service automatically has the ability to create, update, and delete their own auth tokens in the Console or the API. An administrator does not need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also have the ability to manage auth tokens for other users.
Note that you cannot change your auth token to a string of your own choice. The token is always an Oracle-generated string.
Auth tokens do not expire. Each user can have up to two auth tokens at a time. To get an auth token in the Console, see [To create an auth token](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create_swift_password). 
### Using an Auth Token with Swift 🔗 
Swift is the OpenStack object store service. If you already have an existing Swift client, you can use it with the Recovery Manager (RMAN) to back up an Oracle Database System (DB System) database to Object Storage. You will need to get an auth token to use as your Swift password. When you sign in to your Swift client, you provide the following:
  * Your Oracle Cloud Infrastructure Console user login
  * Your Swift-specific auth token, provided by Oracle
  * Your organization's Oracle tenant name


Any user of a Swift client that integrates with Object Storage needs permission to work with the service. If you're not sure if you have permission, contact your administrator. For information about policies, see [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work). For basic policies that enable use of Object Storage, see [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
## Working with Customer Secret Keys 🔗 
**Note** "Customer Secret keys" were previously named "Amazon S3 Compatibility API keys". Any keys you had created are now listed in the Console as Customer Secret keys. You can continue to use the existing keys.
Object Storage provides an API to enable interoperability with Amazon S3. To use this Amazon S3 Compatibility API, you need to generate the signing key required to authenticate with Amazon S3. This special signing key is an Access Key/Secret Key pair. Oracle provides the Access Key that is associated with your Console user login. You or your administrator generates the Customer Secret key to pair with the Access Key.
Each user created in the IAM service automatically has the ability to create, update, and delete their own Customer Secret keys in the Console or the API. An administrator does not need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also have the ability to manage Customer Secret keys for other users. 
Any user of the Amazon S3 Compatibility API with Object Storage needs permission to work with the service. If you're not sure if you have permission, contact your administrator. For information about policies, see [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work). For basic policies that enable use of Object Storage, see [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
Customer Secret keys do not expire. Each user can have up to two Customer Secret keys at a time. To create keys using the Console, see [To create a Customer Secret key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create-secret-key). 
## Working with OAuth 2.0 Client Credentials 🔗 
**Note** OAuth 2.0 Client Credentials are not available in the United Kingdom Government Cloud (OC4). 
OAuth 2.0 client credentials are required to interact programmatically with those services that use the OAuth 2.0 authorization protocol. The credentials enable you to obtain a secure token to access those service REST API endpoints. The allowed actions and endpoints granted by the token depend on the scopes (permissions) that you select when you generate the credentials. The services that use the OAuth 2.0 protocol are:
  * Oracle Analytics Cloud
  * Oracle Integration


An OAuth 2.0 access token is valid for 3600 seconds (1 hour). 
To create the credentials, you need to know the service resource and scope. Typically, you can select these from a drop-down list. However, if the information is not available in the list, you can manually enter the resource and scope. The scope defines the allowed permissions for the token, so ensure to set the scope at the minimum required access level.
A user can create the credentials for themselves or an Administrator can create the credentials for another user. The lists of available resources and scopes display only those resources and permission levels that the user has been granted access to.
### OAuth 2.0 Client Credential Limits 🔗 
Each user can have up to 10 OAuth 2.0 client credentials. You can increase this limit by [Requesting a Service Limit Increase](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
Each OAuth 2.0 client credential can have up to 10 scopes.
### Obtaining an OAuth 2.0 Access Token  🔗 
To obtain the token, use your credentials in a request against the OAuth2 token service endpoint as follows: 
  1. Create the OAuth 2.0 client credentials. See [To create OAuth 2.0 client credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#create-oauth20). 
After you create the OAuth 2.0 client credential note the following information:
     * The generated secret
     * The OCID of the OAuth 2.0 client credential
     * The scope and audience (fully-qualifed scope)
  2. Using the information from the previous step, make a request against the `/oauth2/token` endpoint to obtain a token as follows:
Copy
```
curl -k -X POST -H "Content-Type: application/x-www-form-urlencoded;charset=UTF-8" --user '<Oauth 2.0 client credential OCID>:<credential secret>' https://auth.<oci_region>.oraclecloud.com/oauth2/token -d 'grant_type=client_credentials&scope=<audience>-<scope>'
```



Where: 
  * <Oauth 2.0 client credential OCID>:<credential secret> is the OCID of the OAuth 2.0 client credential that you created joined by a colon (:) with the generated secret for the credential. Note that this secret is only displayed at the time you generate it and it must be copied immediately. You can retrieve the OCID from the details of the credential at any time.
  * ` https://auth.<oci_region>.oraclecloud.com/oauth2/token ` is the Oracle Cloud Infrastructure OAuth 2.0 authorization endpoint where <OCI_region> is a region your tenancy is subscribed to. For example, `us-ashburn-1`.
  * <scope>-<audience> is the fully-qualifed scope, that is, the scope and audience joined by a hyphen (-). The scope and audience are available from the details page of the credential.


Example request:
```
curl -k -X POST -H "Content-Type: application/x-www-form-urlencoded;charset=UTF-8" --user 'ocid1.credential.region1..aaaaaaexamplestringaapgpedxq:{SAMplESeCreta5y' https://auth.us-ashburn-1.oraclecloud.com/oauth2/token -d 'grant_type=client_credentials&scope=https://2aexampley3uytc.analytics.ocp.oraclecloud.com-urn:opc:resource:consumer::all'
```

The response will include the token. Example response:
```
{
"access_token" : "eyJraWQiOiJhcDVfwqKdi...8lTILrzc4cof2A",
"token_type" : "Bearer",
"expires_in" : "3600"
}
```

The token string is truncated in the example response. Copy the entire `access_token` string (within the quotation marks) as shown in your response.
### Using the OAuth 2.0 Token in a Request 🔗 
After you obtain an OAuth 2.0 access token, you provide the token in a bearer token header of the REST API request. 
For example:
Copy
```
curl -i -X GET -H "Authorization: Bearer <token-string>" "https://<audience>/<rest-endpoint-path>"
```

### What to Do When the Token Expires 🔗 
The token expires after 3600 seconds (1 hour). When the token expires, request a new token following the instructions in [Obtaining an OAuth 2.0 Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#topic_tv2_f1x_mmb).
### Adding Scopes 🔗 
You can add scopes to an existing OAuth 2.0 client credential to add access to more services with the same credential. After you add scopes, you do not need to regenerate the secret. 
To request a token for multiple scopes, You can include additional scopes in a token request by appending 
```
&scope=<scope>-<<audience>
```

to the final argument of the request and specifying the scope and audience for the scope you want to add. 
## Working with SMTP Credentials 🔗 
Simple Mail Transfer Protocol (SMTP) credentials are needed in order to send email through the Email Delivery service. Each user is limited to a maximum of two SMTP credentials. If more than two are required, they must be generated on other existing users or additional users must be created.
**Note**
You cannot change your SMTP username or password to a string of your own choice. The credentials are always Oracle-generated strings.
Each user created in the IAM service automatically has the ability to create and delete their own SMTP credentials in the Console or the API. An administrator does not need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also have the ability to manage SMTP credentials for other users. 
**Tip** Although each user can create and delete their own credentials, it is a security best practice to create a new user and generate SMTP credentials on this user rather than generating SMTP credentials on your Console user that already has permissions assigned to it.
SMTP credentials do not expire. Each user can have up to two credentials at a time. To get SMTP credentials in the Console, see [To generate SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#To5). 
For information about using the Email Delivery service, see [Overview of the Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).
## Working with IAM Database User Names and Passwords 🔗 
### **Easier to use** 🔗 
Database end users can easily use IAM database passwords because they can continue to use a well-known authentication method to access the database. You can access database passwords that you manage through your OCI profile after you successfully authenticate to OCI. 
Before users can access or manage their database password, IAM administrators can create an extra layer of protection by enforcing multifactor authentication using [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingmfa.htm#Managing_MultiFactor_Authentication). For example, this can be a FIDO authenticator, or by pushing notifications through authenticator applications. 
### IAM Database Password Security 🔗 
Using IAM database usernames and IAM database passwords to access databases improves security because they allow IAM administrators to centrally manage users and user access to database passwords within IAM instead of locally in each database. When a user leaves an organization, their IAM account is suspended and therefore, their access to all databases are automatically suspended. This method removes the possibility of unauthorized accounts being left on database servers after a user has left. For more information, see [IAM Database Passwords](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#usercredentials_iam_db_pwd "Manage your IAM database passwords overview."). See the [Oracle Security Guide, Chapter 7 ](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/authenticating-and-authorizing-iam-users-oracle-autonomous-databases.html)for information about how IAM users authenticate and authorize to OCI databases.
### IAM Database User Names 🔗 
If your OCI IAM database username is longer than 128 bytes, you must set a different database username and a database password that is less than 128 bytes. IAM enforces the uniqueness of database usernames within a tenancy. The database user name is not case-sensitive and has the same allowable characters as an IAM user name (ASCII letters, numerals, hyphens, periods, underscores, +, and @)). This is more restrictive than local database usernames, which are governed by the character set of the database. See [Database Object Names and Qualifiers](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Database-Object-Names-and-Qualifiers.html) for more information. 
To create, change, and delete IAM database user names, see [Working with IAM Database User Names](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#iam_database_user_names "You can manage your own IAM database user name with the Console, including creating, changing, and deleting it.").
### Alternate IAM Database User Names
You can create an alternate IAM database user name that contains only letters and numbers, does not include special characters, and can be shorter than regular IAM database user names. 
You can create an alternate IAM database user name:
  * If your user name is too long or hard to type
  * To make logging in easier with a user name that does not include special characters


### **IAM Database Password Specifications** 🔗 
The IAM database password complexity uses almost the same rules supported in IAM for Console passwords (no double quotes ["] in IAM passwords). For details, see [Creating an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#usercredentials_topic_creating_a_database_password "You can manage your own IAM database password with the Console, including creating, changing and deleting it.").
### **Failed Login Lockout** s 🔗 
For information about failed logins, see [IAM Database Password Lockouts](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#usercredentials_topic_password_lockouts "A user's account gets locked if the user encounters 10 consecutive failed sign-in attempts.").
### **Password Rollovers** 🔗 
Applications have a password in a wallet or other secure mechanism and in the database. When changing a database password, you also need to change the password in the application wallet. You normally do this during application downtime. However, having a second password allows you to change passwords without application downtime. Since both passwords are usable, the application admin can swap passwords in the application wallet files at their convenience, and can remove the old password from IAM later. This is independent of the database gradual password rollover status in the database. The database still reflects open status, that is, not open and in rollover.
## Using the Console 🔗 
[To change your Console password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
You're prompted to change your initial one-time password _the first time_ you sign in to the Console. The following procedure is for changing your password again later. 
**Note**
For Federated Users
If your company uses an identity provider (other than Oracle Identity Cloud Service) to manage user logins and passwords, you can't use the Console to update your password. You do that with your identity provider.
  1. Sign in to the Console using the Oracle Cloud Infrastructure User Name and Password.
  2. After you sign in, select the **Profile** menu on the upper-right side of the navigation bar at the top of the page, and then select **Change password**.
  3. Enter the **Current Password**.
  4. Enter your new password in the **New Password** and **Confirm New Password** fields, and then select **Save New Password**.


[To create or reset another user's Console password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
If you're an administrator, you can use the following procedure to create or reset a user's password. The procedure generates a new one-time password that the user must change the next time they sign in to the Console.
  1. View the user's details: Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. Select **Create/Reset Password**.
The new one-time password is displayed. If you're an administrator performing the task for another user, you need to securely deliver the new password to the user. The user will be prompted to change their password the next time they sign in to the Console. If they don't change it within 7 days, the password will expire and you'll need to create a new one-time password for the user.


[To reset your password if you forgot it](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
If you have an email address in your user profile, you can use the **Forgot Password** link on the sign on page to have a temporary password sent to you. If you don't have an email address in your user profile, you must ask an administrator to reset your password for you.
[To unblock a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
If you're an administrator, you can unblock a user who has tried 10 times in a row to sign in to the Console unsuccessfully. See [To unblock a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#unblock_user).
[To add an API signing key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
You can use the Console to generate the private/public key pair for you. If you already have a key pair, you can choose to upload the public key. When you use the Console to add the key pair, the Console also generates a configuration file preview snippet for you. 
The following procedures work for a regular user or an administrator. Administrators can manage API keys for either another user or themselves. 
**About the Config File Snippet**
When you use the Console to add the API signing key pair, a configuration file preview snippet is generated with the following information:
  * `user` - the OCID of the user for whom the key pair is being added.
  * `fingerprint` - the fingerprint of the key that was just added.
  * `tenancy` - your tenancy's OCID.
  * `region` - the currently selected region in the Console.
  * `key_file`- the path to your downloaded private key file. You must update this value to the path on your file system where you saved the private key file. 


If your config file already has a DEFAULT profile, you'll need to do one of the following:
  * Replace the existing profile and its contents.
  * Rename the existing profile.
  * Rename this profile to a different name after pasting it into the config file.


You can copy this snippet into your config file, to help you get started. If you don't already have a config file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one. You can also retrieve the config file snippet later for an API signing key whenever you need it. See: To get the config file snippet for an API signing key.
[To generate an API signing key pair](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
**Prerequisite:** Before you generate a key pair, create the `.oci` directory in your home directory to store the credentials. See [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for more details.
  1. View the user's details:
     * If you're adding an API key for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator adding an API key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Click **Add API Key**.
  3. In the dialog, select **Generate API Key Pair**.
  4. Click **Download Private Key** and save the key to your `.oci` directory. In most cases, you do not need to download the public key.
**Note** : If your browser downloads the private key to a different directory, be sure to move it to your `.oci` directory.
  5. Click **Add**. 
The key is added and the **Configuration File Preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config file`. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) 
After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file. 
If your config file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the config file.
  6. Update the permissions on your downloaded private key file so that only you can view it:
    1. Go to the `.oci` directory where you placed the private key file.
    2. Use the command `chmod go-rwx                     ~/.oci/<oci_api_keyfile>.pem` to set the permissions on the file.


[To upload or paste an API key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
**Prerequisite:** You have generated a public **RSA key in PEM format (minimum 2048 bits)**. The PEM format looks something like this:
Copy
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoTFqF...
...
-----END PUBLIC KEY——
 OCI_PRIVATE_KEY
```

We recommend that you include a label at the end of the key. For example, `OCI_PRIVATE_KEY`.
  1. View the user's details:
     * If you're adding an API key for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator adding an API key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Click **Add API Key**.
  3. In the dialog, select **Choose Public Key File** to upload your file, or **Paste Public Key** , if you prefer to paste it into a text box 
  4. Click **Add**.
The key is added and the **Configuration File Preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config file`. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) 
After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file. 
If your config file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the config file.


[To get the config file snippet for an API signing key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. 
  1. View the user's details:
     * If you're getting an API key config file snippet for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator getting an API key config file snippet for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. On the left side of the page, click **API Keys**. The list of API key fingerprints is displayed. 
  3. Click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the fingerprint, and select **View configuration file**.
The **Configuration File Preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config file`. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file. 
If your config file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the config file.


[To delete an API signing key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. Administrators can delete an API key for either another user or themselves. 
  1. View the user's details:
     * If you're deleting an API key for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator deleting an API key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. Select **API Keys**.
  3. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the API key you want to delete, and then select **Delete**.
  4. Confirm when prompted.

The API key is no longer valid for sending API requests. 
[To create an auth token](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
  1. View the user's details:
     * If you're creating an auth token for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an auth token for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **Auth Tokens**.
  3. Select **Generate Token**.
  4. Enter a description that indicates what this token is for, for example, "Swift password token". 
  5. Select **Generate Token**.
The new token string is displayed.
  6. Copy the token string immediately, because you can't retrieve it again after closing the dialog box.


If you're an administrator creating an auth token for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.
[To delete an auth token](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. Administrators can delete an auth token for either another user or themselves.
  1. View the user's details:
     * If you're deleting an auth token for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator deleting an auth token for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **Auth Tokens**.
  3. For the auth token you want to delete, select **Delete**.
  4. Confirm when prompted.


The auth token is no longer valid for accessing third-party APIs.
[To create a Customer Secret key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
  1. View the user's details:
     * If you're creating a Customer Secret key for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating a Customer Secret key for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **Customer Secret Keys**.
A Customer Secret key consists of an Access Key/Secret key pair. Oracle automatically generates the Access Key when you or your administrator generates the Secret Key to create the Customer Secret key.
  3. Select **Generate Secret Key**.
  4. Enter a friendly description for the key and select **Generate Secret Key**. 
The generated **Secret Key** is displayed in the **Generate Secret Key** dialog box. At the same time, Oracle generates the **Access Key** that is paired with the **Secret Key**. The newly generated Customer Secret key is added to the list of **Customer Secret Keys**. 
  5. Copy the **Secret Key** immediately, because you can't retrieve the **Secret Key** again after closing the dialog box for security reasons.
If you're an administrator creating a Secret Key for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.
  6. Select **Close**.
  7. To show or copy the **Access Key** , select the **Show** or **Copy** action to the left of the **Name** of a particular Customer Secret key.


[To delete a Customer Secret key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. Administrators can delete a Customer Secret key for either another user or themselves.
  1. View the user's details:
     * If you're deleting a Customer Secret key for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator deleting a Customer Secret key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **Customer Secret Keys**.
  3. For the Customer Secret key you want to delete, select **Delete**.
  4. Confirm when prompted. 


The Customer Secret key is no longer available to use with the Amazon S3 Compatibility API.
[To create OAuth 2.0 client credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
**Note** OAuth 2.0 Client Credentials are not available in the following **realms** : 
  * the commercial realm (OC1)
  * the United Kingdom Government Cloud (OC4)


  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **OAuth 2.0 Client Credentials**.
  3. Select **Generate OAuth 2.0 client credential**.
  4. Select **Name** , and then enter a name for this credential.
  5. Select **Title** , and then enter a description for this credential.
  6. Add the URI for the OAuth 2.0 services that this credential will provide access to.
To **Select an audience-scope pair** :
    1. In **Audience** , enter the URI for the OAuth 2.0 services.
    2. Next, select the **Scope** for this credential. Always select the minimum required privileges.
  7. To add more permissions to this credential, select **+ Another scope** and follow the instructions in the previous step.
  8. Select **Generate**. The new secret string is generated.
Copy the token string immediately, because you can't retrieve it again after closing the dialog box..
If you're an administrator creating a Secret Key for another user, you need to securely deliver it to the user.


You will need the following information from the credential for the token request:
  * The generated secret
  * The OCID of the OAuth 2.0 client credential
  * The scope and audience (fully-qualifed scope)


[To add scopes to an existing OAuth 2.0 client credential](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **OAuth 2.0 Client Credentials**.
  3. Select the name of the credential that you want to add scopes to.
  4. Select **Add Scopes**.
  5. Add the URI for the OAuth 2.0 services that you want to add access to. 
To **Select a Resource-Scope Pair**
    1. Select the **Select a Resource-Scope Pair** option.
    2. The **Resource** list displays the resources you have permission to view. Select the resource you want to add credentials for. After you select the resource, the **Audience** field is automatically populated.
    3. Next, select the **Scope** for this credential. Always select the minimum required privileges.
To **Enter Fully Qualified Scope** :
    1. Select the **Enter Fully Qualified Scope** option.
    2. Enter the **Audience** and **Scope** for this credential.
  6. To add more permissions to this credential, select **+ Another Scope** and follow the instructions in the previous step.
  7. Select **Save Changes**.


[To regenerate the OAuth 2.0 client credential secret](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
**IMPORTANT:** When you regenerate the secret for a credential, requests made with the previous secret will be denied access to target scopes.
  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **OAuth 2.0 Client Credentials**.
  3. Select the name of the credential that you want to regenerate the secret for.
  4. Select **Add Scopes**.
  5. Select **Regenerate Secret**.
  6. Acknowledge the warning dialog and select **Regenerate Secret**.
  7. Copy the token string immediately, because you can't retrieve it again after closing the dialog box.


Ensure to update existing token requests with the new secret string.
[To delete an OAuth 2.0 Client Credential](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. Administrators can delete an auth token for either another user or themselves.
  1. View the user's details:
     * If you're deleting an OAuth 2.0 Client Credential for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator deleting an auth token for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **OAuth 2.0 Client Credentials**.
  3. For the OAuth 2.0 Client Credential you want to delete, select **Delete**.
  4. Confirm when prompted.


The OAuth 2.0 Client Credential is no longer available to use.
[To generate SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
  1. View the user's details:
     * If you're generating SMTP credentials for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator generating SMTP credentials for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Click **SMTP Credentials**.
  3. Click **Generate SMTP Credentials**.
  4. Enter a **Description** of the SMTP Credentials in the dialog box.
  5. Click **Generate SMTP Credentials**. A user name and password is displayed.
  6. Copy the user name and password for your records and click **Close**. Copy the credentials immediately, because you can't retrieve the password again after closing the dialog box for security reasons.
If you're an administrator creating the credential set for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.


[To delete SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
The following procedure works for a regular user or an administrator. Administrators can delete SMTP credentials for either another user or themselves.
  1. View the user's details:
     * If you're deleting SMTP credentials for _yourself_ : In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator deleting SMTP credentials for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **SMTP Credentials**.
  3. For the SMTP credentials you want to delete, select **Delete**.
  4. Confirm when prompted. 


The SMTP credentials are no longer available to use with the Email Delivery service.
[To create an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
Use the Console to create a database password.
You can create an IAM database password to meet the Oracle Database password-creation guidelines. See [Creating an IAM Database Password](https://confluence.oci.oraclecorp.com/Concepts/usercredentials_topic-creating_a_database_password.dita) for the IAM database password specifications.
  1. Log in to the OCI IAM console.
  2. In the upper right corner of the window, select the profile icon to display your user profile page.
  3. In your user profile page, select your user name. 
  4. Under **Resources** , select **Database Passwords.**
  5. In the **Database Passwords** section, select **Create Database Password.**
The **Create Database Password** dialog box is displayed.
  6. Enter a description of the password.
  7. Note the password guidelines and restrictions listed on the page. See [Creating an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#usercredentials_topic_creating_a_database_password "You can manage your own IAM database password with the Console, including creating, changing and deleting it.") for more information about password rules.
  8. Select **Create Database Password.**
The dialog box closes and the description for which you have created a password is displayed in the Database Passwords section.


[To change an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
Use the Console to change a database password.
To change your IAM database password, delete your current password and then create a new one. See [To Delete an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#delete_iam_db_password) and [To create an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#to_create_an_iam_password "Use the Console to create a database password.").
[To Delete an IAM Database Password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
You can delete your own IAM database password.
  1. Log in to the OCI IAM console.
  2. In the upper right corner of the window, select the profile icon to display your user profile page.
  3. In your user profile page, select your user name. 
  4. Under **Resources** , select **Database Passwords.**
  5. Your user name is displayed in the **Database Passwords** section.
  6. At the right end of the row with your user name in it, select the**three-dot menu** , and then select **Delete**. 


[To create an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
Use the Console to create a database user name.
To change your IAM database username:
  1. Log in to the OCI IAM console. 
  2. Select **Identity & Security**. 
  3. Under **Identity** , select **Users**. 
  4. In the table of database users, select **Create User**.
  5. In the **Name** field, enter your database user name. Enter only letters, numerals, hyphens, periods, underscores, +, and @. You cannot use spaces in the name.
  6. In the **Description** field, optionally enter the name of the database that this user name is for or any other relevant information.
  7. Optionally select **Advanced Options** to show the Tags dialog box.
  8. In the Tag Namespace, Tag Key, and Value fields, enter a tag name 
  9. Select **Save Changes**.


[To change an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
Use the Console to change a database user name.
To change your IAM database user name:
  1. Log in to the OCI IAM console. 
  2. Select **Identity & Security**. 
  3. Under **Identity** , select **Users**. 
  4. In the table of database users, locate your database user name and left select it. 
The page for your user name is displayed.
  5. Select **Edit User**.
  6. In the **Description** field, edit your database user name and select **Save Changes**.


[To delete an IAM Database User Name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)
Use the Console to delete a database user name.
To change your IAM database user name:
  1. Log in to the OCI IAM console. 
  2. Select **Identity & Security**. 
  3. Under **Identity** , select **Users**. 
  4. In the table of database users, locate your database user name and left select it. 
The page for your user name is displayed.
  5. At the right end of the row that contains your user name select the three-dot menu and then select **Delete**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to manage Console passwords and access:
  * [CreateOrResetUIPassword](https://docs.oracle.com/iaas/api/#/en/identity/latest/UIPassword/CreateOrResetUIPassword): This generates a new one-time Console password for the user. The next time the user signs in to the Console, they'll be prompted to change the password.
  * [UpdateUserState](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUserState): Unblocks a user who has tried to sign in 10 times in a row unsuccessfully. 


Use these API operations to manage API signing keys: 
  * [ListApiKeys](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/ListApiKeys)
  * [UploadApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/UploadApiKey)
  * [DeleteApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/DeleteApiKey)


Use these API operations to manage auth tokens:
  * [CreateAuthToken](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthToken/CreateAuthToken)
  * [UpdateAuthToken](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthToken/UpdateAuthToken): You can only update the auth token's description, not change the token string itself.
  * [ListAuthTokens](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthToken/ListAuthTokens)
  * [DeleteAuthToken](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthToken/DeleteAuthToken)


Use these API operations to manage Customer Secret keys:
  * [CreateCustomerSecretKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/CustomerSecretKey/CreateCustomerSecretKey)
  * [UpdateCustomerSecretKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/CustomerSecretKeySummary/UpdateCustomerSecretKey): You can only update the secret key's description, not change the key itself.
  * [ListCustomerSecretKeys](https://docs.oracle.com/iaas/api/#/en/identity/latest/CustomerSecretKeySummary/ListCustomerSecretKeys)
  * [DeleteCustomerSecretKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/CustomerSecretKey/DeleteCustomerSecretKey)


Use these API operations to manage OAuth 2.0 client credentials:
  * [CreateOAuthClientCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/CreateOAuthClientCredential)
  * [UpdateOAuthClientCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateOAuthClientCredential)
  * [ListOAuthClientCredentials](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListOAuthClientCredentials)
  * [DeleteOAuthClientCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/DeleteOAuthClientCredential)


Use these API operations to manage SMTP credentials:
  * [CreateSmtpCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/SmtpCredential/CreateSmtpCredential)
  * [UpdateSmtpCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/SmtpCredentialSummary/UpdateSmtpCredential): You can only update the description.
  * [ListSmtpCredentials](https://docs.oracle.com/iaas/api/#/en/identity/latest/SmtpCredentialSummary/ListSmtpCredentials)
  * [DeleteSmtpCredential](https://docs.oracle.com/iaas/api/#/en/identity/latest/SmtpCredential/DeleteSmtpCredential)


Was this article helpful?
YesNo

