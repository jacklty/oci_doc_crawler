Updated 2024-04-02
# Token Expiry Table
The token expiry table contains the expiry setting name and provides the default value for the setting.
Setting Name | Default Value | Description  
---|---|---  
Per Tenant SSO Session Expiry | Per Tenant | Per Tenant session expiry time (SSOSettings) that the tenant can modify. The default expiration is eight hours.   
Global SSO Session Expiry | 8 Hours | Global Session expiry time (SSOConfig)  
Request Cookie Expiry | 15 Minutes | Cookie expiry time for IDCS_REQUEST cookie  
OAuth Access Token Expiry |  3600 Seconds **Note:** The default is used when a Resource App Expiry, User Session Expiry or Custom Expiry isn't set. |  An access token's (AT) expiry time is in seconds. AT expiry time is determined by a combination of the following factors:
  * **OAuthConfig Access Token Expiry time.** A global configuration applied to all tenants. Expiry time is in seconds. The default is 3600 seconds. The range is 60 seconds to 1 year. 
  * **Resource App Expiry time.** A configuration applied only to the related Resource App. Expiry time is in seconds. The default is 3600 seconds. The range is 60 seconds to 1 year. 
  * **User Session Expiry time.** A tenant level configuration that applies to all users in the tenant. Expiry time is in minutes. The default is 480 minutes. The expiry time is based on the time remaining in the session. For example, if the time remaining in a session is 15 minutes out of a total of 480 minutes, then 15 minutes is used to calculate the AT expiry time.
  * **Custom Expiry time.** Specified in the token request by sending urn:opc:resource:expiry=<seconds> in the scope parameter.
    1. If the Resource App Expiry time (400 Seconds) and the User Session Expiry time (15 minutes) are both configured and the Custom Expiry time (500 seconds) is specified in token request, then the AT expiry is a minimum of all three, for example, AT: min(400,500,15*60) = 400s.
    2. If only the Resource App Expiry time (400 Seconds) is configured and the Custom Expiry time (500 seconds) is specified in the token request, then the AT expiry is a minimum of the Resource App Expiry time and the Custom Expiry time (500 seconds), for example, AT: min(400, 500) = 400s.
    3. If only the User Session Expiry time (15 minutes) is configured, then the AT is the minimum of the User Session Expiry time and the OAuth Access Token Expiry time (500 seconds), for example, AT: min(500,15*60) = 500s.
    4. If neither the Resource App Expiry time nor the User Session Expiry time is configured but the Custom Expiry time (500 seconds) is specified in token request, then AT expiry is set to the Custom Expiry time with the max limit of 1 year, for example, AT: min(500s,1yrs) = 500s.
    5. If neither the Resource App Expiry time nor the User Session Expiry time is configured and the Custom Expiry time isn't specified either, then the AT expiry will default to the OAuth Access Token Expiry time of 3600 seconds.

  
OAuth Identity Token Expiry | Set to SSO session Expiry | Set to SSO session expiry.  
OAuth Refresh Token Expiry | 1 week | Coming from Resource Server's configuration, if available. Otherwise, it's coming from OAuthConfig for the refresh token-type expiry. If the expiry value isn't defined in OAuthConfig, the default value is one week.  
OAuth AZ Code Expiry  | 3 minutes  
Was this article helpful?
YesNo

