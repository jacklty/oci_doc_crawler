Updated 2024-04-02
# API Rate Limits
Understand the rate limiting for APIs for different identity domain types.
Oracle APIs are subject to rate limiting to protect the API service usage for all Oracle's customers. If you reach the API limit for the identity domain type, then IAM returns a 429 error code.
## Rate Limits for all Identity Domain Types 🔗 
API Group | Per |  Free | Oracle Apps | Oracle Apps Premium | Premium | External User  
---|---|---|---|---|---|---  
**AuthN** | second | 10 | 50 | 80 | 95 | 90  
**AuthN** | minute | 150 | 1000 | 2100 | 4500 | 3100  
**Token Mgmt** | second | 10 | 40 | 50 | 65 | 60  
**Token Mgmt** | minute | 150 | 1000 | 1700 | 3400 | 2300  
**Others** | second | 20 | 50 | 55 | 90 | 80  
**Others** | minute | 150 | 1500 | 1750 | 5000 | 4000  
**Bulk** | second | 5 | 5 | 5 | 5 | 5  
**Bulk** | minute | 200 | 200 | 200 | 200 | 200  
**Import and export** | day | 4 | 8 | 10 | 10 | 10  
## APIs in API Groups 🔗 
API limits apply to the total of all APIs within a group.
[Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm)
  * `/sso/v1/user/login`
  * `/sso/v1/user/secure/login`
  * `/sso/v1/user/logout`
  * `/sso/v1/sdk/authenticate`
  * `/sso/v1/sdk/session`
  * `/sso/v1/sdk/idp`
  * `/sso/v1/sdk/secure/session`
  * `/mfa/v1/requests`
  * `/mfa/v1/users/{userguid}/factors`
  * `/oauth2/v1/authorize`
  * `/oauth2/v1/userlogout`
  * `/oauth2/v1/consent`
  * `/fed/v1/user/request/login`
  * `/fed/v1/sp/sso`
  * `/fed/v1/idp/sso`
  * `/fed/v1/idp/usernametoken`
  * `/fed/v1/metadata`
  * `/fed/v1/mex`
  * `/fed/v1/sp/slo`
  * `/fed/v1/sp/initiatesso`
  * `/fed/v1/sp/ssomtls`
  * `/fed/v1/idp/slo`
  * `/fed/v1/idp/initiatesso`
  * `/fed/v1/idp/wsfed`
  * `/fed/v1/idp/wsfedsignoutreturn`
  * `/fed/v1/user/response/login`
  * `/fed/v1/user/request/logout`
  * `/fed/v1/user/response/logout`
  * `/fed/v1/user/testspstart`
  * `/fed/v1/user/testspresult`
  * `/admin/v1/SigningCert/jwk`
  * `/admin/v1/HTTPAuthenticator`
  * `/admin/v1/PasswordAuthenticator`
  * `/admin/v1/Asserter`
  * `/admin/v1/MyAuthenticationFactorInitiator`
  * `/admin/v1/MyAuthenticationFactorEnroller`
  * `/admin/v1/MyAuthenticationFactorValidator`
  * `/admin/v1/MyAuthenticationFactorsRemover`
  * `/admin/v1/TermsOfUseConsent`
  * `/admin/v1/MyTermsOfUseConsent`
  * `/admin/v1/TrustedUserAgents`
  * `/admin/v1/AuthenticationFactorInitiator`
  * `/admin/v1/AuthenticationFactorEnroller`
  * `/admin/v1/AuthenticationFactorValidator`
  * `/admin/v1/MePasswordResetter`
  * `/admin/v1/UserPasswordChanger`
  * `/admin/v1/UserLockedStateChanger`
  * `/admin/v1/AuthenticationFactorsRemover`
  * `/admin/v1/BypassCodes`
  * `/admin/v1/MyBypassCodes`
  * `/admin/v1/MyTrustedUserAgents`
  * `/admin/v1/Devices`
  * `/admin/v1/MyDevices`
  * `/admin/v1/TermsOfUses`
  * `/admin/v1/TermsOfUseStatements`
  * `/admin/v1/AuthenticationFactorSettings`
  * `/admin/v1/SsoSettings`
  * `/admin/v1/AdaptiveAccessSettings`
  * `/admin/v1/RiskProviderProfiles`
  * `/admin/v1/Threats`
  * `/admin/v1/UserDevices`
  * `/session/v1/SessionsLogoutValidator`
  * `/ui/v1/signin`


[Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm)
  * `/oauth2/v1/token`
  * `/oauth2/v1/introspect`
  * `/oauth2/v1/revoke`
  * `/oauth2/v1/device`


[Import/Export](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm)
  * `/job/v1/JobSchedules?jobType=UserImport`
  * `/job/v1/JobSchedules?jobType=UserExport`
  * `/job/v1/JobSchedules?jobType=GroupImport`
  * `/job/v1/JobSchedules?jobType=GroupExport`
  * `/job/v1/JobSchedules?jobType=AppRoleImport`
  * `/job/v1/JobSchedules?jobType=AppRoleExport`


[Bulk](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm)
  * `/admin/v1/Bulk`
  * `/admin/v1/BulkUserPasswordChanger`
  * `/admin/v1/BulkUserPasswordResetter`
  * `/admin/v1/BulkSourceEvents`


[Other](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm)
Any API not in one of the other API Groups is included in the Other API Group
## Other Restrictions 🔗 
These restrictions are for Bulk, Import, and Export for all tiers:
  * Payload size: 1 MB
  * Bulk API: 50 operations limit per call
  * Only one of these can be run at a time: 
    * Import: For Users, Groups & App Role Memberships
    * Full sync from apps
    * Bulk APIs
    * Export: For Users, Groups & App Role Memberships
  * CSV Import: 100 K rows limit per CSV & Max file size: 10 MB
  * CSV Export: 100 K rows limit


Was this article helpful?
YesNo

