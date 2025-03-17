Updated 2023-07-26
# Default Headers and Cookies App Gateway Adds to the Request
By Default App Gateway adds header variables and cookies to any request forwarded to a protected enterprise application. The following is a list of these headers and cookies and their respective values.
## Headers 🔗 
Header Name | Description | Authentication Method Usage  
---|---|---  
**idcs_service_url** |  The value of this header is your IAM's base URL. For example, `https://idcs-tenant.identity.oraclecloud.com` |  Used by all authentication method.  
**idcs_cloudgate_id** |  The **Client ID** value for the App Gateway registered in IAM. |  Used by all authentication method.  
**idcs_client_id** |  The **Client ID** value for the App Gateway registered in IAM. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by **Anonymous** or **Public** authentication methods.  
**idcs_authn_method** |  The authentication method configured in the enterprise application's authentication policy. Value depending on the authentication method used:
  * If resource is protected by **Anonymous** authentication method, then value is `anonymous`.
  * If resource is protected by **Form or Access Token** authentication method, then value is `oauth`.
  * If resource is protected by **Basic Auth** or **Basic Auth+ Session** authentication methods, then value is `http`.
  * If resource is protected by **Multitoken** authentication method, then value is `multitoken`.
  * If resource is protected by **Multitoken+Fallthrough** authentication method, then value is `multitoken` or `fallthrough` depending if the authorization header is a known value or not.

|  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public**.  
**idcs_authn_strength** |  Identifies if the user authentication has happened in one or two steps. If the user has signed in with IAM using their credentials only, then the authentication strength is `1`. If the user has signed in using multifactor authentication, then authentication level is `2`. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public** and **Anonymous**.  
**remote_user** |  Username of the user signed in to IAM. If the resource is protected by **Anonymous** authentication method, then the value of this header is `anonymous`. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public**.  
**idcs_remote_user** |  Username of the user signed in to IAM. If the resource is protected by **Anonymous** authentication method, then the value of this header is `anonymous`. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public**.  
**idcs_remote_user_mappingattr** |  The IAM user schema attribute used to identify the signed in user. For example, `userName`. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public** and **Anonymous**.  
**idcs_session_id** |  The session ID value IAM creates after user signs in. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by **Form or Access Token** or **Basic Auth+ Session** authentication method.  
**idcs_user_assertion** |  Value of the identity token issued by IAM. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by **Form or Access Token** authentication method.  
**idcs_user_display_name** |  Value of the `displayname` attribute of the user signed in with IAM. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public** and **Anonymous**.  
**idcs_user_id** |  Value of the unique identifier attribute of the user signed in with IAM. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public** and **Anonymous**.  
**idcs_user_tenant_name** |  IAM tenant name. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by any authentication method except **Public** and **Anonymous**.  
## Cookies 🔗 
Cookie Name | Description | Authentication Method Usage  
---|---|---  
**ORA_OCIS_CG_SESSION_ <idcs-tenant>_<aapgateway_host>** |  After the user authenticates with IAM, App Gateway sets this cookie to the request forwarded to the application.  The cookie name is composed by `ORA_OCIS_CG_SESSION` prefix, concatenated with IAM's tenant name, and suffixed with the App Gateway's **Host** value. |  App Gateway adds this header to the request forwarded to the enterprise application if the resource is protected by **Form or Access Token** authentication method.  
Was this article helpful?
YesNo

