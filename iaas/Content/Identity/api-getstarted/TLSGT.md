Updated 2024-04-02
# TLS Client Authentication Grant Type
Use the Transport Layer Security (TLS) grant type when the authorization scope is limited to the protected resources under the control of the client or to protect resources registered with the OAuth Authorization Server.
The following diagram displays the TLS Client Authentication Grant Type flow.
![A diagram that illustrates the TLS Client Authentication Grant Type.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/diag_tls_client_granttype.png)
In this OAuth flow:
**Note** **Prerequisite:** Upload the client certificate to the client certificate store.
  1. As part of the TLS handshake, the client application presents its own certificate and Client ID to obtain an access token. Note: This certificate must match the certificate in the client certificate store.
  2. This requested access token is either associated with the client's own resources, and not a particular resource owner, or is associated with a resource owner for whom the client application is otherwise authorized to act.
  3. The Authorization Server returns the access token to the client application only after successful certificate validation.
  4. The client application uses the access token in an API call to update the app.


Function | Available  
---|---  
Requires client authentication | Yes  
Requires client to know user credentials | No  
Browser-based end user interaction | No  
Can use an external Identity Provider for authentication | No  
Refresh token is allowed | No  
Access token is in the context of the client application | Yes  
See [TLS Client Authentication Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TLSGT.htm#TLSAuthFlow "The Transport Layer Security \(TLS\) Client Authentication grant type provides a specific grant flow in which the Resource Owner isn't involved. In this scenario, the client application is running processes that don't have Resource Owner participation, for example, a batch process or a server-to-server task.") for an example flow.
## TLS Client Authentication Grant Type Authorization Flow Example 🔗 
The Transport Layer Security (TLS) Client Authentication grant type provides a specific grant flow in which the Resource Owner isn't involved. In this scenario, the client application is running processes that don't have Resource Owner participation, for example, a batch process or a server-to-server task.
When using this grant type, the client application requests an access token with its own certificate (the certificate that's uploaded in the client profile) together with the Client ID and uses the access token on behalf of the client application itself. This grant flow is best suited when a Service Provider wants to provide some API methods that are to be used by the client application in general, instead of API methods that apply to a certain Resource Owner, for example, API methods for maintenance.
When you create an application using the TLS Client Authentication grant type in the identity domain Console:
  * Specify Confidential Application as the application type. Mobile/browser applications don't have a client certificate and cannot use the TLS Client Authentication grant type.
  * Select **TLS Client Authentication** as the grant type.
  * Select **Trusted** or **Confidential** as the **Client Type**.
  * Import the **Client Certificate**. This certificate is used to validate the token request. **Note:** The client must use this same certificate in the token request.


See [TLS Client Authentication Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TLSGT.htm#TLSGT "Use the Transport Layer Security \(TLS\) grant type when the authorization scope is limited to the protected resources under the control of the client or to protect resources registered with the OAuth Authorization Server.") for more information on the TLS Client Authentication grant type and an authorization flow diagram.
  1. A client-initiated event (for example, a scheduled task) requests access to protected resources from an OAuth client application.
The event URL contains query parameters that indicate the type of access being requested:
**Example Request Using the Authorization Header**
**Note**
**cacert.crt** is the CA certificate that signed the server's certificate for this TLS.
**client.key** is client private key.
**client.crt** is client certificate.
```
  curl -i
  --cacert cacert.crt --key client.key --cert client.crt
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=tls_client_auth&client_id=<client ID>&scope=<scope value>'
```

  2. The client application requests an access token from the OAuth Authorization Server.
  3. The OAuth Authorization Server: 
    1. Authenticates the client application based on the certificate sent as part of TLS handshake.
    2. Returns an access token containing all applicable scopes based on the privileges specified by the application roles granted to the requesting client application.
  4. The client application uses the access token to perform a request.


Was this article helpful?
YesNo

