Updated 2024-04-02
# Authorization Code Grant Type
Use this grant type when you want to obtain an authorization code by using an authorization server as an intermediary between the client application and the resource owner using identity domains. 
The following diagram displays the Authorization Code Grant Type flow.
![A diagram that illustrates the authorization code grant type flow.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/daig1_authz_code_granttype.png)
In this OAuth flow:
  1. A user clicks a link in a web server client application, requesting access to protected resources.
  2. The client application redirects the browser to the authorization endpoint `oauth2/v1/authorize` with a request for an authorization code.
  3. The Authorization Server returns an authorization code to the client application through a browser redirect after the resource owner gives consent.
  4. The client application then exchanges the authorization code for an access token, and often a refresh token.
  5. The Authorization Server returns the access token to the client application.
  6. The client application uses the access token in an API call to obtain protected data.
**Note** Resource owner credentials are never exposed to the client.


Function | Available  
---|---  
Requires client authentication | No  
Requires client to know user credentials | No  
Browser-based end-user interaction | Yes  
Can use an external Identity Provider for authentication | Yes  
Refresh token is allowed | Yes  
Access token is in the context of the end user | Yes  
See an example [Authorization Code Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#ACWebServerAppAuth "This authorization flow example walks you through an OpenID Connect login request using an authorization code.").
## Authorization Code Grant Type Authorization Flow Example 🔗 
This authorization flow example walks you through an OpenID Connect login request using an authorization code.
This flow is a three-legged OAuth flow, which refers to scenarios in which the application calls the identity domain APIs on behalf of end users, and in which user consent is sometimes required. This flow shows how to configure Federated Single Sign-On between an identity domain and a custom application using OAuth 2.0 and OpenID Connect.
When you create an app using the Authorization Code grant type in the identity domain Console:
  * Specify **Trusted Application** as the type of application.
  * Select **Authorization Code** as the grant type.
  * Specify the **Redirect URI,** which is where responses to authentication requests are sent.
  * Optionally, select the **Refresh Token** grant type to return a refresh token with the access token.


See [Authorization Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#AuthCodeGT "Use this grant type when you want to obtain an authorization code by using an authorization server as an intermediary between the client application and the resource owner using identity domains.") for more information on the Authorization Code grant type and an authorization flow diagram.
**Authorization Flow**
  1. A user clicks a link in the web server client application (Customer Quotes), requesting access to protected resources.
  2. The Customer Quotes app redirects the browser to the identity domain authorization endpoint `(oauth2/v1/authorize)` with a request for an authorization code.
The request URL contains query parameters that indicate the type of access being requested. 
**Note** A nonce value is a cryptographically strong random string that you use to prevent intercepted responses from being reused.
Example Request: Confidential/Trusted Client
```
GET https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=openid&nonce=<nonce-value>&state=1234
```

Example Request: Confidential/Trusted Client Including Refresh Token in Request
```
GET https://<domainURL>/oauth2/v1/authorize?client_id=<client-id&response_type=code&redirect_uri=<client-redirect-uri>&scope=openid%20<Resource
Server Scope>**%20offline_access**&nonce=<nonce-value>&state=1234
```

Example Request: Public Client
```
GET https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=id_token&redirect_uri=<client-redirect-uri>&scope=openid&nonce=<nonce-value>&state=1234
```

Example Request Using PKCE
```
GET https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=openid&nonce=<nonce-value>&state=1234&code_challenge=<code-challenge>&code_challenge_method=<plain|S256>'
```

  3. The identity domain receives the request and identifies that the Customer Quotes app (identified by its `client_id`) is requesting an authorization code to get more information about the resource owner (scope `openid).`
  4. If the user isn't already logged in, IAM challenges the user to authenticate. IAM checks the user's credentials.
  5. If the login is successful, IAM redirects the browser to the Customer Quotes application with an authorization code. 
**Note** If the user doesn't authenticate, an error is returned rather than the authorization code.
  6. The Customer Quotes application extracts the authorization code and makes a request to an identity domain to exchange the authorization code for an access token.
Request Example: Confidential/Trusted Client
```
  curl -i 
  -H 'Authorization: Basic <base64-clientid-secret>' 
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' 
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=authorization_code&code=<authz-code>'
```

Request Example: Public Client
```
  curl -i 
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' 
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=authorization_code&code=<authz-code>&redirect_uri=<client-redirect-uri>&client_id=<client-id>'
```

Example Request Using PKCE
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=authorization_code&code=<authz-cod>e&redirect_uri=<client-redirect-uri>&client_id=<client-id>&code_verifier=<code-verifier>'
```

  7. IAM validates the grant and user data associated with the code (`client_id, client_secret`, and the authorization code).
  8. An [Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm#AccessToken "Successful OAuth transactions require the IAM identity domain Authorization Server to issue access tokens for use in authenticating an API call. An access token represents an authorization issued to the client application containing credentials used to access protected OAuth resources.") and an [Identity Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#IdentityToken "An Identity Token is an integrity-secured, self-contained token \(in JSON Web Token \(JWT\) format\) that's defined in the OpenID Connect standard containing claims about the end user. The Identity Token is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication in an identity domain.") are returned. The access token contains information about which scopes the Customer Quotes application can request on behalf of the user. The application can use this token when requesting APIs on behalf of the user. 
The Identity Token is retrieved only when you request the `openid` scope. This token contains identification information about the user and is used for federated authentication.
  9. The Customer Quotes application processes the `id_token` and then extracts the user's information returned from IAM.
  10. Customer Quotes displays the home page that contains information about the user. 


Was this article helpful?
YesNo

