Updated 2025-01-14
# Supported Tokens
A token is used to make security decisions to authorize a user and to store tamper-proof information about a system entity in an identity domain.
Identity domains support JSON Web Tokens (JWT). A JWT is a JSON-based open standard [(RFC 7519)](https://tools.ietf.org/html/rfc7519) that defines a compact and self-contained way for securely sending information between parties as a JSON object. This information can be verified and trusted because it's digitally signed. JSON Web Tokens consist of three parts separated by periods `(xxxx.yyyy.zzzz)`:
  * **Header**. Consists of two parts: the type of token (JWT) and the hashing algorithm being used, such as SHA256
  * **Payload**. Contains the claims (the token data)
  * **Signature**. Consists of the encoded token header and the encoded payload signed with the identity domain private key. The signature is used to verify that the sender of the JWT is who it says it's and ensures that the message wasn't changed along the way.


Identity domains support three different tokens: identity token, access token, and client assertion.
To access detailed information on each supported token, select any of the following links:
  * [Identity Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm#IdentityToken "An Identity Token is an integrity-secured, self-contained token \(in JSON Web Token \(JWT\) format\) that's defined in the OpenID Connect standard containing claims about the end user. The Identity Token is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication in an identity domain.")
  * [Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm#AccessToken "Successful OAuth transactions require the IAM identity domain Authorization Server to issue access tokens for use in authenticating an API call. An access token represents an authorization issued to the client application containing credentials used to access protected OAuth resources.")
  * [Client/User JWT Assertion](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ClientAssertion.htm "An assertion is a package of information that facilitates the sharing of identity and security information across security domains. An assertion typically contains information about a subject or principal, information about the party that issued the assertion and when it was issued. It also contains information about the conditions under which the assertion is to be considered valid, such as when and where it can be used. The intent is to provide an alternative client authentication mechanism. Clients can build client assertions and use them as credentials rather than using the client ID and client secret in an OAuth token request.")


For information about token expiration go to:
  * [Token Expiry Table](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenExpiryTable.htm "The token expiry table contains the expiry setting name and provides the default value for the setting.")
  * [Specifying a Custom Access Token Expiration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm#customexpiry "Use the following example request and response to specify a custom access token expiration value in an access token request to an identity domain.")


Was this article helpful?
YesNo

