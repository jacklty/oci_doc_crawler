Updated 2024-04-02
# Client Credentials Grant Type
Use this grant type when authorization scope is limited to the protected resources under the control of the client or to protected resources registered with the OAuth Authorization Server.
The following diagram displays the Client Credentials Grant Type flow.
![A diagram that illustrates the Client Credentials Grant Type flow.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/diag3_client_creds_granttype.png)
In this OAuth flow:
  1. A client-initiated event (for example, a scheduled background update for an app on your mobile device) requests access to a protected resource from an OAuth client application.
  2. The client application presents its own credentials to obtain an access token and often a refresh token. This access token is either associated with the client's own resources, and not a particular resource owner, or is associated with a resource owner for whom the client application is otherwise authorized to act.
  3. The Authorization Server returns the access token to the client application.
  4. The client application uses the access token in an API call to update the app on your device.


Function | Available  
---|---  
Requires client authentication | Yes  
Requires client to know user credentials | No  
Browser-based end user interaction | No  
Can use an external Identity Provider for authentication | No  
Refresh token is allowed | No  
Access token is in the context of the client application | Yes  
See [Client Credentials Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CCGT.htm#ClientCredServerAppAuth "The Client Credentials grant type provides a specific grant flow in which the Resource Owner isn't involved. In this scenario example, the client application is executing processes that don't have Resource Owner participation, for example, a batch process or a server-to-server task.") for an example flow.
## Client Credentials Grant Type Authorization Flow Example 🔗 
The Client Credentials grant type provides a specific grant flow in which the Resource Owner isn't involved. In this scenario example, the client application is executing processes that don't have Resource Owner participation, for example, a batch process or a server-to-server task.
When using this grant, the client application requests an access token with its own credentials (the ID and secret) or an assertion, and uses the access token on behalf of the client application itself. This grant flow is best suited when a Service Provider wants to provide some API methods that are to be used by the client application in general, instead of methods that apply to a certain Resource Owner, for example, API methods for maintenance.
When you create an application using the Client Credentials grant type in the identity domain Console:
  * Specify **Trusted Application** as the application type, because a mobile/browser application doesn't have a client secret and cannot use the Client Credentials grant.
  * Select**Client Credentials** as the grant type.


See [Client Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CCGT.htm#CCGT "Use this grant type when authorization scope is limited to the protected resources under the control of the client or to protected resources registered with the OAuth Authorization Server.") for more information on the Client Credentials grant type and an authorization flow diagram.
**Authorization Flow**
  1. A client-initiated event (for example, a scheduled task) requests access to protected resources from an OAuth client application.
The event URL contains query parameters that indicate the type of access being requested:
Example Request Using the Authorization Header
```
  curl -i
  -H 'Authorization: Basic <base64Encoded clientid:secret>'
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=client_credentials&scope=<scope value>'
```

Example Request Using a JWT Client Assertion
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token 
  -d 'grant_type=client_credentials&client_id=<client-id>&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<client-assertion>&scope=<scope value>'
```

  2. The client application requests an access token from the OAuth Authorization Server.
  3. The OAuth Authorization Server authenticates the client application based on the Authorization header or the assertion sent and returns an access token containing all applicable scopes based on the privileges represented by the application roles granted to the requesting client application.
  4. The client application uses the access token to perform a request.


Was this article helpful?
YesNo

