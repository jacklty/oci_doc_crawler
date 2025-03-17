Updated 2024-04-02
# Using OpenID Connect to Extend OAuth 2.0
OpenID Connect extends the OAuth 2.0 protocol to add a simple authentication and identity layer that sits on top of OAuth 2.0.
Use OpenID Connect when you want your cloud-based applications to get identity information, retrieve details about the authentication event (such as when, where, and how the authentication occurred), and to allow federated single sign-on (SSO).
OAuth 2.0 provides security tokens for use when calling backend resources on behalf of a user. OAuth provides a grant or license the ability to access resources rather than provide information about the authentication itself. Using OAuth for authentication is like an apartment manager giving someone who wants to know your identity a temporary key to your apartment. The key only implies a right to enter the apartment for a specific length of time. It doesn't imply that the individual is the owner. 
Using OpenID Connect completes the picture by providing applications with information about the user, the context of their authentication, and access to their profile information. OpenID Connect allows clients of all types, including web-based, mobile, and JavaScript clients to request and receive information about authenticated sessions and end users. See [OpenID Connect](http://openid.net/connect/) for more information.
Two concepts are introduced: 
  * OpenID Connect ID Token: This token contains information about the user's authenticated session.
  * UserInfo endpoint: This endpoint provides a way for the client to retrieve additional attributes about the user.


## Implementing OpenID Connect
There are three main actions required to implement OpenID Connect:
  1. Get an OpenID Connect ID Token: Use an OAuth2 grant type to request an OpenID Connect ID Token by including the `openid` scope in the authorization request.
The following use cases provide example requests and responses for obtaining the ID Token.
     * [Using the Authorization Code Flow with OpenID Connect](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#openidconnectauthcode "Use the Authorization Code flow when you have clients that can securely maintain a client secret between themselves and the Authorization Server. The Authorization Code flow returns an Authorization Code to the client, which can then exchange the code for an ID Token and an Access Token directly.")
     * [Using the Implicit Flow with OpenID Connect](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#implicitopenidconnect "Use the Implicit flow when you have implemented a browser-based client using a scripting language such as JavaScript. The Access Token and the ID Token are returned directly to the Client, which may expose these tokens to the user and applications that have access to the user's user agent \(such as a web browser\).")
     * [Using the Hybrid Flow with OpenID Connect](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#hybridopenidconnect "Use the Hybrid flow when you want to obtain tokens separately from both the front channel and the back channel. For example, you have a browser component like JavaScript and a backend server component such as Node.js. The browser component obtains the Authorization Code and the ID Token and can then personalize the UI content. The backend component obtains the Access Token to perform business API calls.")
     * [Using OpenID Connect for Log Out](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#logoutopenidconnect "You can use OpenID Connect for browser-based logout requests.")
  2. Validate the ID Token: Validate the ID Token to ensure that it originated from a trusted issuer and that the contents weren't tampered with during transit.
The following use case provides information on how and what to validate.
     * [Identity Token Validation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#IDTokenValidation "Why do we validate tokens? When your web application checks credentials directly, it verifies that the username and password that are presented correspond to what you maintain. When using claims-based identity, you're outsourcing that job to an identity provider.")
  3. Retrieve profile information from the `UserInfo` endpoint: Using the OAuth2 Access Token, access the `UserInfo` endpoint to retrieve profile information about the authenticated user.
The following use case provides example requests and responses for retrieving profile information from the `UserInfo` endpoint.
     * [Querying the UserInfo Endpoint](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#queryinguseinfo "The OpenID Connect UserInfo endpoint is used by an application to retrieve profile information about the identity that authenticated. Applications can use this endpoint to retrieve profile information, preferences, and other user-specific information.")


## Identity Token 🔗 
An Identity Token is an integrity-secured, self-contained token (in JSON Web Token (JWT) format) that's defined in the OpenID Connect standard containing claims about the end user. The Identity Token is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication in an identity domain.
The Identity Token JWT consists of three components, a header, a payload, and the digital signature. Following the JWT standard, these three sections are Base64URL encoded and separated by periods.
**Note** OpenID Connect requests must contain the `openid` scope value. 
OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows an IAM identity domain client application (registered as an OAuth 2 client with client ID and client secret) to verify the identity of the end user based on the authentication performed by an Authorization Server (AS), and to obtain basic profile information about the end user in an interoperable, REST-like manner. OpenID Connect allows clients of all types, including web-based, mobile, and JavaScript clients to request and receive information about authenticated sessions and end users. See [OpenID Connect](http://openid.net/connect/) for more information.
Name | Value  
---|---  
`amr` | Authentication Methods References. JSON array of strings that are identifiers for authentication methods used in the authentication. For example, values might indicate that both password and OTP authentication methods were used.  
`at_hash` | OAuth 2 Access Token hash value.   
`aud` | Identifies recipients for which this ID Token is intended. Must be the OAuth 2.0 `client_id` (per the [OpenID Connect specification).](http://openid.net/specs/openid-connect-core-1_0.html#IDToken) This is the OAuth client name (app.name) that's making the request. `Aud` also contains the IAM identity domain Issuer, thereby turning the token type (**IT**) into an IAM identity domain **User Assertion.**  
`authn_strength*` | The value returned by Cloud SSO indicating Authentication Strength from AuthN Context.  
`auth_time` | The time (UNIX epoch time) when Cloud SSO actually authenticated the user (in seconds, coming from AuthN Context).  
`azp` | Authorized party. The party to which the ID Token was issued. If present, it MUST contain the OAuth 2.0 Client ID of this party. This claim is only needed when the ID Token has a single audience value and that audience is different than the authorized party. It may be included even when the authorized party is the same as the sole audience. The azp value is a case-sensitive string that contains a StringOrURI value.  
`exp` | The expiration time (UNIX epoch time) on or after which the ID Token must not be accepted for processing. This value must be same as the `session_exp.`  
`iat` | The time (UNIX epoch time) when the JWT was created (in seconds). UNIX Epoch Time is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in Coordinated Universal Time (UTC) until the date/time.  
`iss` | The principal that issued the token: `https://<domainURL>`  
`jti` | The server-generated unique identifier for the JWT ID.  
`nonce` | The string value used to associate a client session with an ID Token and to mitigate replay attacks. This value is provided by Cloud Gate.  
`session_exp* ` | The time (UNIX epoch time) when the Cloud SSO session expires (seconds, must be the same SSO's session expiration in AuthN context).  
`sid` | The session ID from Cloud SSO (255 maximum ASCII characters) from AuthN Context.  
`sub` | Identifies the user. The subject identifier is locally unique, never reassigned, and is intended to be consumed by the client: User Login ID (255 maximum ASCII characters). This is the user's login ID from AuthN Context.  
`sub_mappingattr*` | The attribute used to find the sub in the ID store.  
`tok_type*` | Identifies the token type: `IT`  
`user_displayname*` | The User Display Name (255 maximum ASCII characters) from AuthN Context.  
`user_csr*` | Indicates (**true**) that the user is a Customer Service Representative (CSR).   
`user_id*` | The user's IAM identity domain GUID from AuthN Context.  
`user_lang*` | The user's preferred language.  
`user_locale*` | The user's locale.  
`user_tenantname*` | The User Tenant Name (255 maximum ASCII characters). Tenant's GUID is specifically not saved in the token  
`user_tz*` | The user's time zone.  
## Identity Token Validation 🔗 
Why do we validate tokens? When your web application checks credentials directly, it verifies that the username and password that are presented correspond to what you maintain. When using claims-based identity, you're outsourcing that job to an identity provider.
The responsibility shifts from verifying raw credentials to verifying that the requester went through your preferred identity provider and successfully authenticated. The identity provider represents successful authentication by issuing a token. Before you can use the information or rely on it as an assertion that the user has authenticated, you must validate it. 
**OpenID Discovery Document**
The OpenID Connect 1.0 protocol is a simple identity layer on top of the OAuth 2.0 protocol that requires the use of multiple endpoints for authenticating users and for requesting resources that include user information, tokens, and public keys. To help with discovering what these endpoints are that you need to use, OpenID Connect allows you to use a discovery document, which is a JSON document found at a well-known location. This discovery document contains key/value pairs that provide details about the OpenID Connect provider's configuration, including the URIs of the authorization, token, userinfo, and public keys endpoints. You can retrieve the discovery document for the IAM identity domain OpenID Connect service from: `https://<domainURL>/.well-known/openid-configuration.`
### Validating Identity Tokens
An Identity (ID) Token is an integrity-secured, self-contained token (in JSON Web Token format) that contains claims about the end user. It represents an authenticated user's session. Therefore, the token must be validated before an application can trust the contents of the ID Token. For example, if a malicious attacker replayed a user's ID Token that they had captured earlier, the application should detect that the token has been replayed or was used after it had expired and deny the authentication. 
The ID Token is defined in the OpenID Connect standard and is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication. ID Tokens are sensitive and can be misused if intercepted. Ensure that these tokens are handled securely by transmitting them only over HTTPS and only using POST data or within request headers. If you store them on your server, you must also store them securely. 
  1. Verify that the value of the audience (`aud`) claim contains the application's `client_id` value. The `aud` (audience) claim may contain an array with more than one element. The ID Token must be rejected if the ID token doesn't list the client as a valid audience, or if it contains additional audiences that aren't trusted by the client.
  2. Verify that the current time is before the time represented by the expiry time (`exp`) claim.
  3. Verify that the ID Token is properly signed by the issuer. Identity domain issued tokens are signed using one of the certificates found at the URI specified in the `jwks_uri` field of the discovery document.
     * Retrieve the tenant's public certificate from the `SigningCert/jwk` endpoint (for example, `https://acme.identity.oraclecloud.com/admin/v1/SigningCert/jwk`).
**Note** Since identity domains change public keys infrequently, you can cache the public keys and, in the vast majority of cases, efficiently perform local validation. This requires retrieving and parsing certificates and making the appropriate crypto calls to check the signature:
     * Use any JWT libraries available to validate, for example, Connect2id's Nimbus JWT Library for Java. See [JWT](http://jwt.io/) for a list of available libraries.
**Note** In case of signature validation failure, to prevent constant refetches in case of attacks with bogus tokens, the re-fetching/re-caching of the public key should be based on a time interval, such as 60 minutes, so that refetches only happen every 60 minutes.
**Example**
```
package sample;
 
import java.net.MalformedURLException;
import java.net.URL;
 
import com.nimbusds.jose.JWSAlgorithm;
import com.nimbusds.jose.jwk.source.JWKSource;
import com.nimbusds.jose.jwk.source.RemoteJWKSet;
import com.nimbusds.jose.proc.JWSKeySelector;
import com.nimbusds.jose.proc.JWSVerificationKeySelector;
import com.nimbusds.jose.proc.SecurityContext;
import com.nimbusds.jwt.JWTClaimsSet;
import com.nimbusds.jwt.proc.ConfigurableJWTProcessor;
import com.nimbusds.jwt.proc.DefaultJWTProcessor;
 
public class TokenValidation {
 
  public static void main(String[] args) {
    try {
      String tokenValue = "eyJ4NXQjUzI1....W9J4oQ";
   
      ConfigurableJWTProcessor jwtProcessor = new DefaultJWTProcessor();
 
      // change t
      JWKSource keySource = new RemoteJWKSet(new URL("https://<domainURL>/admin/v1/SigningCert/jwk"));
 
      // The expected JWS algorithm of the token (agreed out-of-band)
      JWSAlgorithm expectedJWSAlg = JWSAlgorithm.RS256;
 
      // Configure the JWT processor with a key selector to feed matching public
      // RSA keys sourced from the JWK set URL
      JWSKeySelector keySelector = new JWSVerificationKeySelector(expectedJWSAlg, keySource);
      jwtProcessor.setJWSKeySelector(keySelector);
 
      // Process the token
      SecurityContext ctx = null; // optional context parameter, not required here
      JWTClaimsSet claimsSet = jwtProcessor.process(tokenValue, ctx);
      // Print out the token claims set
      System.out.println(claimsSet.toJSONObject());
       
 
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
 
}
```

  4. Verify that the value of the Issuer Identifier (`iss`) claim exactly matches the value of the `iss` (issuer) claim: `https://<domainURL>/`


## Querying the UserInfo Endpoint 🔗 
The OpenID Connect `UserInfo` endpoint is used by an application to retrieve profile information about the identity that authenticated. Applications can use this endpoint to retrieve profile information, preferences, and other user-specific information.
The OpenID Connect profile consists of two components:
  * Claims describing the user
  * `UserInfo` endpoint providing a mechanism to retrieve these claims
**Note** User claims can also be presented inside the ID Token to eliminate a callback during authentication time.


**User Profile Claims**
The `UserInfo` endpoint provides a set of claims based on the OAuth2 scopes presented in the authentication request. OpenID Connect defines five scope values that map to a specific set of default claims:
OpenID Connect Scope | Returned Claims  
---|---  
openid |  None - Indicates this is an OpenID Connect request  
profile |  name, family_name, given_name, middle_name, nickname, preferred_username, profile, picture, website, gender, birthdate, zoneinfo, locale, updated_at  
address |  address  
email |  email, email_verified  
phone |  phone_number, phone_number_verified  
The client needs to present its credentials and an access token. The access token presented needs to contain the `openid` scope.
If a scope is omitted (for example, the `email` scope isn't used), the claim (`email`) won't be present in the returned claims.
**Sample UserInfo Endpoint Request Example**
After the client application has authenticated a user and has the access token, the client can then make a request to the `UserInfo` endpoint to retrieve the requested attributes about a user. The following example shows a request example. 
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded'
  -H 'Authorization: Bearer eyJ4NXQjUzI1....rtApFw'-H 'Accept: */*'
  -H 'Content_Language: en-US'--request GET https://<domainURL>/oauth2/v1/userinfo
```

**Response Example**
A successful response returns an HTTP 200 OK response and the user's claims in JSON format:
```
{
"birthdate":"",
"email":"user@example.com",
"email_verified":false,
"family_name":"user",
"gender":"",
"given_name":"user",
"appRoles":[],
"name":"alice alice",
"preferred_username":"user@example.com",
"sub":"user@example.com",
"updated_at":1495136783,"website":""
}
```

Before the client application can trust the values returned from the `UserInfo` endpoint (for example, as a check for token substitution attack), the client must verify that the `sub` claim returned from the `UserInfo` endpoint request matches the subject from the ID Token.
## Using the Authorization Code Flow with OpenID Connect 🔗 
Use the Authorization Code flow when you have clients that can securely maintain a client secret between themselves and the Authorization Server. The Authorization Code flow returns an Authorization Code to the client, which can then exchange the code for an ID Token and an Access Token directly.
This provides you with the benefit of not exposing any tokens to the user agent (such as a web browser) and possibly other malicious applications with access to the user agent. The Authorization Server can also authenticate the client before exchanging the Authorization Code for an Access Token. The Authorization Code flow works with both Confidential Clients and Public Clients.
**Confidential Clients**
There are two steps in the Authorization Code flow:
  1. Request the Authorization Code. In this request, the scope parameter value is `openid.` This is an OpenID Connect specification value.
**Request Example**
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client-id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=openid
```

**Response Example**
```
https://<domainURL>/?code=AQIDBAXv9lZQ....F9NCA=
```

     * You can provide additional scope values in your requests, for example:
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client-id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=phone+openid+offline_access+profile+address+email

```

     * This request contains both the openid and an OAuth resource scope:
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client-id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=http://<domainURL>/api+openid
```

  2. Request the Token. The client extracts the code parameter from the response and makes the token request. Also, the client provides its client id and secret as part of the Basic Authentication header.
**Request Example**
```
  curl -i
  -H 'Authorization: Basic ZWE1OGIwNDA0N2ZkNGQ4MTgyYThiYWQ0ZTNkMGFmZjU6ZGMxNGE4MjMtZGU2OC00YWNhLTg1OWUtMWNhZTJmNjQ0NTBi' 
  -H 'Accept: */*'
  --request POST 'https://<domainURL>/oauth2/v1/token' -d 'grant_type=authorization_code&code=AQIDBAXv9lZQ???.jF9NCA'
```

**Response Example**
The request contains both the Access Token and the ID Token.
```
{
"access_token":"eyJ4NXQjUzI1???.xhtnbw",
"token_type":"Bearer",
"expires_in":27261,
"id_token":"eyJ4NXQjUzI1???.._XLqUw"
}
```



**Public Clients**
Public clients don't have credentials, rather they have a client identifier. There are two steps in the Authorization Code flow. The requests involve a browser-based GET request, and then a back-channel POST request to get the Access Token.
  1. Request the Authorization Code.
**Request Example**
```
GET https://<domainURL>/oauth2/v1/authorize?client_id=<client-id>&response_type=code&redirect_uri=<client-redirect-uri>&scope=openid&nonce=<nonce-value>&state=1234
```

**Response Example**
**Note** These request and response examples are similar to the Confidential Client request and responses discussed previously.
```
https://<domainURL>/?code=AQIDBAXv9lZQ....F9NCA=
```

  2. Request the Token.
**Request Example**
**Note** This request is different from the Confidential Client request where the client id and client secret are specified in the Basic Authentication header. In the public client flow, there's no Basic Authentication header. The client id is specified as part of the request payload.
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'  
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=authorization_code&code=<authz-code>&reidrect_uri=<client-redirect-uri>&client_id=<client-id>'
```

**Response Example**
```
{
"access_token":"eyJ4NXQjUzI1???.xhtnbw",
"token_type":"Bearer",
"expires_in":27261,
"id_token":"eyJ4NXQjUzI1???.._XLqUw"
}

```



## Using the Implicit Flow with OpenID Connect 🔗 
Use the Implicit flow when you have implemented a browser-based client using a scripting language such as JavaScript. The Access Token and the ID Token are returned directly to the Client, which may expose these tokens to the user and applications that have access to the user's user agent (such as a web browser). 
There's no programmatic/back-channel token request involved in this flow (like the Public Client request in the [Authorization Code flow example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#openidconnectauthcode "Use the Authorization Code flow when you have clients that can securely maintain a client secret between themselves and the Authorization Server. The Authorization Code flow returns an Authorization Code to the client, which can then exchange the code for an ID Token and an Access Token directly.")). All tokens are returned from the `Authorization` endpoint, and the `token` endpoint isn't used. The Implicit flow works with confidential, trusted, and public clients.
**Note** Public clients don't have credentials, just a client identifier.
The following `response_type` values are supported with the Implicit flow:
  * `id_token` (ID Token)
  * `token` (Access Token) 
  * `id_token token` (both the ID Token and the Access Token)


**Obtaining an ID Token**
There are three steps in the Implicit flow to obtain an ID Token:
  1. Request the token.
**Request Example**
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=id_token&redirect_uri=<client_redirect_uri>&scope=address+openid+profile&nonce=abcdefg
```

  2. User logs in and gives consent (based on the requested scopes)
  3. Response with ID Token
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#id_token=eyJ4NXQjUzI1.....gF5uyQ
```



**Obtaining an Access Token**
There are three steps in the Implicit flow to obtain an Access Token:
  1. Request the Access Token.
**Request Example**
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=token&redirect_uri=<client_redirect_uri>&scope=address+openid+profile
```

  2. User logs in and gives consent (based on the requested scopes).
  3. Response with Access Token
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#access_token=eyJ4NXQjUzI1...4WGvJQ&token_type=Bearer&expires_in=3600
```



**Obtaining an ID Token and an Access Token**
There are three steps in the Implicit flow to obtain both the ID Token and the Access Token:
  1. Request the ID Token and Access Token.
**Request Example**```
https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=id_token token&redirect_uri=<client_redirect_uri>&scope=address+openid+profile&nonce=abcdefghijkl
```

  2. User logs in and gives consent (based on the requested scopes).
  3. Response with Access Token and ID Token.
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#access_token=eyJ4NXQjUzI....XWGmeQ&id_token=eyJ4NXQjUzI1....&token_type=Bearer&expires_in=3600
```



## Using the Hybrid Flow with OpenID Connect 🔗 
Use the Hybrid flow when you want to obtain tokens separately from both the front channel and the back channel. For example, you have a browser component like JavaScript and a backend server component such as Node.js. The browser component obtains the Authorization Code and the ID Token and can then personalize the UI content. The backend component obtains the Access Token to perform business API calls.
Clients need to support both browser-based requests and responses and programmatic/back-channel requests and responses to use the Hybrid flow. The Hybrid flow works with both Confidential Clients and Public Clients. The following `response_type` values are supported with the Hybrid flow:
  * `code id_token` (ID Token)
  * `code token` (Access Token) 
  * `code id_token token` (Authorization Code, ID Token, and Access Token)


**Obtaining an ID Token**
There are four steps in the Hybrid flow to obtain both the Authorization Code and the ID Token:
  1. Request the Authorization Code and the ID Token.
**Request Example**
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=code id_token&redirect_uri=<client_redirect_uri>&scope=http://<domainURL>/test+openid+offline_access&nonce=abcdefghijk
```

  2. User logs in and gives consent (based on the requested scopes).
  3. Response with ID Token and Authorization Code.
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#code=AQIDBAUrAi0l....F9NCA=&id_token=eyJ4NXQjUzI1....3R8b_Q
```

  4. The client application makes use of the Authorization Code and makes a back channel request to obtain a new Access Token and Refresh Tokens.
**Request Example**
```
  curl -i
  -H 'Authorization: Basic YjA3NTZkNDc5M2QwNDZjNjhjZWVmY2UxZjE4ZGUwMWM6NGYzZjJjN2EtZTBjZC00NzcyLWE5MTYtNjI3ZmExNzA2NWE5'
  -H 'Accept: */*'
  --request POST 'https://<domainURL>/oauth2/v1/token' -d 'grant_type=authorization_code&code=AQIDBAUrAi0l???.CA%3D'

```

**Response Example**
```
{
"access_token":"eyJ4NXQjUzI1....sJ5mCw",
"token_type":"Bearer",
"expires_in":3600,
"refresh_token":"AQIDBAUwxxoC....tZLvA"
}
```



**Obtaining an Access Token**
There are four steps in the Hybrid flow to obtain the Authorization Code and the Access Token:
  1. Request the Authorization Code and the Access Token.
**Request Example**
```
https://<domainURL>/oauth2/v1/authorize?client_id=<client_id>&response_type=code token&redirect_uri=<client_redirect_uri>&scope=http://<domainURL>/test
```

  2. User logs in and gives consent (based on the requested scopes).
  3. Response with ID Token and Authorization Code.
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#access_token=eyJ4NXQjUzI1....Pudw9A&code=AQIDBAU6d6Ae....F9NCA=&token_type=Bearer&expires_in=3600
```

  4. The client application makes use of the Authorization Code and makes a back channel request to obtain a new Access Token.
**Request Example** ```
  curl -i
 -H 'Authorization: Basic YjA3NTZkNDc5M2QwNDZjNjhjZWVmY2UxZjE4ZGUwMWM6NGYzZjJjN2EtZTBjZC00NzcyLWE5MTYtNjI3ZmExNzA2NWE5'
  -H 'Accept: */*''
  --request POST 'https://<domainURL>/oauth2/v1/token' -d 'grant_type=authorization_code&code=AQIDBAU6d6Ae...NCA%3D'
```

**Response Example**
```
{
"access_token":"eyJ4NXQjUzI1....Tgs9LA",
"token_type":"Bearer",
"expires_in":3600
}
```



**Obtaining an ID Token and an Access Token**
There are four steps in the Hybrid flow to obtain the Authorization Code, the ID Token, and the Access Token:
  1. Request the Authorization Code and the ID Token.
**Request Example**```
https://<domainURL>/oauth2/v1/authorize?client_id=client_id&response_type=cod id_token token&redirect_uri=client_redirect_uri&scope=http://<domainURL>/test+openid&nonce=abcdaer
```

  2. User logs in and gives consent (based on the requested scopes).
  3. Response with ID Token and Access Token.
**Response Example**
**Note** All response parameters are added to the fragment component of the redirection URI.
```
https://<domainURL>/#access_token=eyJ4NXQjUzI1....sDB7lA&code=AQIDBAVxZzy-....F9NCA=&id_token=eyJ4NXQjUzI1....&token_type=Bearer&expires_in=36004
```

  4. The client application makes use of the Authorization Code and makes a back channel request to obtain a new Access Token.
**Request Example**```
  curl -i
  -H 'Authorization: Basic YjA3NTZkNDc5M2QwNDZjNjhjZWVmY2UxZjE4ZGUwMWM6NGYzZjJjN2EtZTBjZC00NzcyLWE5MTYtNjI3ZmExNzA2NWE5'
  -H 'Accept: */*' ?request
  POST 'https://<domainURL>/oauth2/v1/token' -d 'grant_type=authorization_code&code=AQIDBAXUbLmS???.NCA%3D'
```

**Response Example**
```
{
"access_token":"eyJ4NXQjUzI1....g52XmQ",
"token_type":"Bearer",
"expires_in":3600,
"id_token":"eyJ4NXQjUzI1....f6JfWA"
}
```



## Using OpenID Connect for Log Out 🔗 
You can use OpenID Connect for browser-based logout requests.
There are two ways that you can request a logout using OpenID Connect:
  1. Redirect to the client who initiated the logout.
**Note** Be sure that you define the post logout redirect URI for the OAuth Client app and that the ID Token is sent in the request. The ID Token contains the client ID. That client id's corresponding post logout URL is fetched and validated.
**Request Example**
```
https://<domainURL>/oauth2/v1/userlogout?post_logout_redirect_uri=http://clienthost:port/myapp/return&state=c3004d28&id_token_hint=<IDToken>
```

  2. Use the tenant's landing page.
**Note** This uses the tenant's landing page that was set in the tenant's SSO settings.
**Request Example**
```
https://<domainURL>/oauth2/v1/userlogout 
```



Was this article helpful?
YesNo

