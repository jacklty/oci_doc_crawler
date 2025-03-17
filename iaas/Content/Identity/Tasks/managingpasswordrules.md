Updated 2025-01-14
# Managing Authentication Settings
This topic describes how to set authentication rules for your tenancy. Authentication settings include policy rules for local IAM users in your tenancy and network source restrictions for all users in your tenancy.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for authentication policy and network sources. 
To view authentication policy and network sources, you must be granted `inspect` access on the `authentication-policies` resource and the `network-sources` resource. For example:
Copy
```
Allow group GroupA to inspect authentication-policies in tenancy
```

```
Allow group GroupA to inspect network-sources in tenancy
```

To manage authentication policy and network sources, you must be granted manage permissions for both resources. For example:
Copy
```
Allow group GroupA to manage authentication-policies in tenancy
```

```
Allow group GroupA to manage network-sources in tenancy
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for groups or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Working with Password Policy Rules 🔗 
A password policy that you set in the IAM service is applicable for all local (or non-federated) users.
When a user is created or when a user changes their password, the IAM service validates the password that is provided against the password policy to ensure that it meets the criteria for the policy. When a user logs in for the first time to change the password, or resets the password at any time, the password policy is evaluated and enforced.
### When Do Changes to Password Policy Rules Take Effect 🔗 
Changes to password policy rules take effect immediately so that the next time any user changes their password they must create a password that meets the criteria. Existing passwords will continue to work even if they would be invalid under the new rules. Users are not forced to change existing passwords to meet the new criteria. Passwords are evaluated against the rules only at the time they are created or changed. 
## About the Password Policy Rules 🔗 
The following table describes the rules that you can include in your password policy:
Rule | Setting Options | Default IAM Service Setting  
---|---|---  
Minimum password length |  Minimum value is 8 (characters). Maximum value is 100. |  12 characters  
Special characters |  Require passwords to contain at least 1 special character. Special characters allowed in passwords are:  `!#$%&'()*+,-./:;<=>?@[\]^_`{|}~` Special characters not listed are not allowed. | Enforced  
Lowercase characters | Require passwords to contain at least 1 lowercase alphabetic character a-z. | Enforced  
Uppercase characters | Require passwords to contain at least 1 uppercase alphabetic character A-Z. | Enforced  
Numeric characters | Require passwords to contain at least 1 number 0-9. | Enforced  
Oracle recommends that you enforce all the password rules.
## Using the Console to Manage Password Policy Rules 🔗 
[To edit password policy rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpasswordrules.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Authentication Settings**. The authentication settings for your tenancy are displayed.
  2. Select **Edit**. 
  3. Enter the following to set the password policy: 
     * **Minimum Password Length:** Enter a number to define the minimum number of characters that a user's password must contain. Allowed values are 8 through 100.
  4. Select the**Password Rules** you want to enforce:
     * **Must contain at least 1 numeric character:** Select the checkbox to require at least 1 number (0-9) in the password. 
     * **Must contain at least 1 special character:** Select the checkbox to require at least 1 special character. Allowed special characters are: `!#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
     * **Must contain at least 1 lowercase character:** Select the checkbox to require at least 1 lowercase alphabetic character (a-z).
     * **Must contain at least 1 uppercase character:** Select the checkbox to require at least 1 uppercase alphabetic character (A-Z). 
  5. Select **Save Changes**.


## Working with Network Source Restrictions in Authentication Policy 🔗 
Network source restrictions let you specify an allowed set of IP ranges from which users can sign in to the Console. Users attempting to sign in from an IP address not on the allowed list will be denied access.
To enforce a network source restriction for your tenancy:
  1. Set up a network source that specifies the allowed IP addresses. See [Managing Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm#Managing_Network_Sources) for information on setting up the network source.
  2. Select the network source in the Authentication settings page.


An administrator can set only one network source in the authentication settings, but a single network source can include multiple allowed IP addresses.
A network source restriction is applied for every user in the tenancy. If an administrator is unable to access a network with an allowed IP address to sign in from, then they must do one of the following to gain access to the tenancy:
  * Use the authentication SDK to sign in and change the network source restriction setting programmatically.
  * Contact [Oracle Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). If you do not have an API signing key to enable access through the authentication SDK, then you must contact support to regain access to your tenancy.
**Caution** Before you set up a network source restriction, ensure that you have an API key set up to enable access to your tenancy in case an allowed network is not available. If you do not set up an API key and an allowed network is not available, then all users will be locked out of the tenancy until you contact Oracle Support. For information about setting up the API signing key, see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).


### When Do Changes to Network Source Restrictions Take Effect 🔗 
After a network source restriction is defined, users signed in to the Console can continue with their current session, but after they sign out, the network restriction will be applied the next time they try to sign in.
## Using the Console to Manage Network Source Restrictions 🔗 
[To set up a network source restriction](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpasswordrules.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Authentication Settings**. The authentication settings for your tenancy are displayed.
  2. Select **Edit**. 
  3. From the **Select Network Source** menu, select the network source that specifies the IP range restrictions you want to apply to all Console sign-ins. 
  4. Select **Save Changes**.


[To view or edit the value of a network source](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpasswordrules.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Authentication Settings**. The authentication settings for your tenancy are displayed.
  2. Select the name of the network source displayed for **Network Source Restrictions**. 
The details page of the network source is displayed. From here, you can edit or delete the definition. See [Managing Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm#Managing_Network_Sources) for information on managing network sources.


## Using the API to Work with Authentication Settings 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage authentication settings:
  * [GetAuthenticationPolicy](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthenticationPolicy/GetAuthenticationPolicy)
  * [UpdateAuthenticationPolicy](https://docs.oracle.com/iaas/api/#/en/identity/latest/AuthenticationPolicy/UpdateAuthenticationPolicy)


Was this article helpful?
YesNo

