Updated 2025-01-14
# Refresh Token Grant Type
Use this grant type when you want a refresh token issued along with the access token. The refresh token is used to obtain a new access token without requiring the user to reauthenticate.
To refresh a token, the access token must have been requested with a grant type that supports refresh tokens, such as Authorization Code, Resource Owner Password Credentials, and Assertion. A request is then made to the token endpoint with the `grant_type` parameter set to `refresh_token.`
**Note** This grant type doesn't influence authorization flows.
Select a link to view a cURL example that includes a refresh token in the request:
  * [Authorization Code Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#ACWebServerAppAuth "This authorization flow example walks you through an OpenID Connect login request using an authorization code.")
  * [Resource Owner Password Credentials Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROWebServerAppAuth "This authorization flow example walks you through obtaining an access token by using the resource owner's \(user\) credentials.")
  * [Assertion Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm#AssertionClientSideAppAuth "In this example flow, Example.com has subscribed to several Oracle Cloud PaaS and SaaS applications. Example.com users want to be able to access Oracle Cloud properties without having to go through the authorization process themselves \(delegated authorization\).")


See a cURL example that uses the [Refresh Token Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm#RTAuthFlow "This authorization flow example walks you through obtaining a new access token without requiring the user to reauthenticate.")
## Refresh Token Grant Type Authorization Flow Example 🔗 
This authorization flow example walks you through obtaining a new access token without requiring the user to reauthenticate.
Be sure to select the refresh token grant type when specifying a grant type that supports refresh tokens, such as [Authorization Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#AuthCodeGT "Use this grant type when you want to obtain an authorization code by using an authorization server as an intermediary between the client application and the resource owner using identity domains."), [Resource Owner Password Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROPCGT "Use this grant type when the resource owner has a trust relationship with the client, such as a computer OS or a highly privileged application, because the client must discard the password after using it to obtain the access token."), or [Assertion Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm#AssertGT "Use this grant type when you want to use an existing trust relationship expressed as an assertion and without a direct user approval step at the OAuth Authorization Server.").
See [Refresh Token Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm#RefreshGT "Use this grant type when you want a refresh token issued along with the access token. The refresh token is used to obtain a new access token without requiring the user to reauthenticate.") for more information on the Refresh Token grant type.
When an application makes a request to an identity domain to obtain an access token, the request URL contains query parameters that indicate the type of access being requested.
**Example Request Using the Authorization Header**
```
curl -i
  -H 'Authorization: Basic <base64Encoded clientid:secret' 
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=refresh_token&refresh_token=<refresh-token>&scope=<optional scope value>'
```

**Example Request Using a JWT Client Assertion** ```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=refresh_token&refresh_token=<refresh-token>&client_id=<client-id>&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<client-assertion>&scope=<optional scope value>'
```

**Example Request Using a Public Client**```
  curl -i 
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' 
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=refresh_token&refresh_token=<refresh-token-value>&client_id=<client-id-value>'
```

Was this article helpful?
YesNo

