Updated 2024-04-02
# Access Token
Successful OAuth transactions require the IAM identity domain Authorization Server to issue access tokens for use in authenticating an API call. An access token represents an authorization issued to the client application containing credentials used to access protected OAuth resources.
The Access Token provides a session (with scope and expiration), that your client application can use to perform tasks in the identity domains REST API. The access token can be obtained either by using the identity domain console or programmatically (performing a REST API call using the application client id and secret). Applications can request an access token to access protected endpoints in different ways, depending on the type of grant type specified in the application. A grant is a credential representing the Resource Owner's authorization to access a protected resource. See [Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm#SupportedAccessGrantTypes "The most important step for an application in the OAuth flow is how the application receives an access token \(and optionally a refresh token\). A grant type is the mechanism used to retrieve the token. OAuth defines several different access grant types that represent different authorization mechanisms.").
Name | Value  
---|---  
`tok_type*` | Identifies the token type: `AT`  
`iss` | The principal that issued the token: `https://<domainURL>`  
`sub` | Identifies the entity ( User/Client ) that's requesting access. The subject identifier is locally unique and is intended to be consumed by the client. In case of IDPropagation tokens, this contains the user's user ID. In other cases, it contains the `clientID.`  
`sub_mappingattr*` | The attribute used to find the `sub` in the ID store. This is the mapping `attr` from SSO settings.  
`sub_type` |  The identity domains access token contains the `sub_type` claim that indicates the type of subject (`sub` claim) that's conveyed by the token. If the token is issued solely on behalf of the client, the value of the claim is `client.` Otherwise, if the token is propagating a user identity, then the value of the claim is `user.` Entities processing and validating the access token can use the value of the `sub_type` claim to call the identity domains `/Asserter` REST API. Use this endpoint to request App Roles for a client that's indicated by the `sub` claim. The value of the `sub_type` claim is passed to `/Asserter` by using the `SubjectType` request parameter. Without specifically passing `client` to the `/Asserter` endpoint, identity domains normally assumes that the Asserter is requesting information for a user, rather than for a client. Hence, the `/Asserter` endpoint's `SubjectType` input parameter and the access token's `sub_type` claim can be used by entities processing the access token to assert the client's AppRoles.  
`user_id*` | The user's identity domains GUID from AuthN Context for user tokens. Not present in client-only tokens.  
`user_displayname*` | The user's identity domains Display Name (255 maximum ASCII characters) from AuthN Context. Not present in client-only tokens.  
`user_tenantname*` | The User Tenant Name (255 maximum ASCII characters). May be different from resource tenancy for cross tenant use cases. Tenant's GUID is specifically not saved in the token and isn't present in client-only tokens.  
`tenant*` | The Resource Tenant Name when the request for the access token was made (255 maximum ASCII characters). Resource Tenant's GUID is specifically not saved in the token.  
`user.tenant.name*` | Same as `tenant.` This is tracked for backward compatibility purposes until there are no more legacy consumers. **Note:** The Tenant Name is the identity domain.  
`aud` | Contains the URI string expected by the Resource Server to match the target URL's resource prefixes. Multiple URI strings may be specified using the standard AUD format. This is the case when OIDC request also contains scopes for some other resource server. For example: `["https://<domainURL>/", "https://example.com"]`  
`iat` | The time (UNIX epoch time) when the JWT was issued. UNIX Epoch Time is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in Coordinated Universal Time (UTC) until the date/time.  
`sid` | The session ID from the Identity Token is the Identity Token that was used during token request.  
`exp` | The time (UNIX epoch time) when the JWT expires (in seconds). See the [Token Expiry Table](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenExpiryTable.htm "The token expiry table contains the expiry setting name and provides the default value for the setting.").  
`scope` | The space-delimited string containing scopes.  
`jti` | The server-generated unique identifier for the JWT ID.  
`client_id*` | OAuth client ID. This is the GUID of the OAuth client making the request. When Cloud Gate is making requests, this is the GUID of the OAuth CloudGate defined in the global oracle tenancy.   
`client_name*` | OAuth client_name. This is the name of the OAuth client making the request. When CloudGate is making requests, this is the name of the CloudGate OAuth client defined in the global oracle tenancy.   
`client_tenantname*` | Client Tenant Name (max 255). May be different from resource tenancy for cross tenant use cases.  
## Specifying a Custom Access Token Expiration 🔗 
Use the following example request and response to specify a custom access token expiration value in an access token request to an identity domain.
**Note** The custom token expiry is still subject to the overall access token expiry rules. See the [Token Expiry Table](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenExpiryTable.htm "The token expiry table contains the expiry setting name and provides the default value for the setting.").
**Example Request**
```
  curl -k -i 
  -H 'Authorization: Basic dGVzdERvbWFpbkFkbWluOmZmNGUzNGE3LWVlNGQtNDAzNy1iNmNmLTUwZGVmMmNjMzM5Zg==' 
  -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' 
  --request POST 'https://<domainURL>/oauth2/v1/token'
  -d 'grant_type=client_credentials&scope=urn:opc:idm:__myscopes__**%20urn:opc:resource:expiry=300**'
```

**Example Response**
```
{
"access_token":"eyJ4NXQjUzIc....q3E8x1tTEwPthTg",
"token_type":"Bearer", 
"expires_in":300 
}
```

Was this article helpful?
YesNo

