Updated 2024-07-19
# Resource Owner Password Credentials Grant Type
Use this grant type when the resource owner has a trust relationship with the client, such as a computer OS or a highly privileged application, because the client must discard the password after using it to obtain the access token.
The following diagram displays the Resource Owner Password Credentials Grant Type flow.
![A diagram that illustrates the Resource Owner Password Credentials Grant Type flow.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/diag2_owner_pass_creds_granttype.png)
In this OAuth flow:
  1. User clicks a link in the client application requesting access to protected resources.
  2. The client application requests the resource owner's username and password.
  3. The user signs in with their username and password.
  4. The client application exchanges those credentials for an access token, and often a refresh token, from the Authorization Server.
  5. The Authorization Server returns the access token to the client application.
  6. The client application uses the access token in an API call to obtain protected data, such as a list of users.


Function | Available  
---|---  
Requires client authentication | No  
Requires client to have knowledge of user credentials | Yes  
Browser-based end-user interaction | No  
Can use an external Identity Provider for authentication | No  
Refresh token is allowed | Yes  
Access token is in the context of the end user | Yes  
See an example [Resource Owner Password Credentials Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROWebServerAppAuth "This authorization flow example walks you through obtaining an access token by using the resource owner's \(user\) credentials.").
## Resource Owner Password Credentials Grant Type Authorization Flow Example 🔗 
This authorization flow example walks you through obtaining an access token by using the resource owner's (user) credentials.
When you create an application using the Resource Owner grant type in the identity domain Console:
  * Specify **Trusted Application** as the application type.
  * Select**Resource Owner** as the grant type.
  * Specify the **Redirect URI,** which is where responses to authentication requests are sent.


See [Resource Owner Password Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROPCGT "Use this grant type when the resource owner has a trust relationship with the client, such as a computer OS or a highly privileged application, because the client must discard the password after using it to obtain the access token.") for more information on the Resource Owner Password Credentials grant type and an authorization flow diagram.
**Authorization Flow**
  1. A user clicks a link in the web server client application, requesting access to protected resources from a third-party web server application.
  2. The client application collects the user's username and password and requests an access token from the OAuth Authorization Server (AS).
The request URL contains query parameters that indicate the type of access being requested:
**Example Request Using the Authorization Header**
```
  curl -i
  -H 'Authorization: Basic <base64Encoded clientid:secret>'
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token -d 'grant_type=password&username=<user-name>&password=<example-password>&scope=<scope value>'
```

**Example Request Using the Authorization Header Including Refresh Token in the Request**
```
  curl -i
  -H 'Authorization: Basic <base64Encoded clientid:secret>'
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token -d 'grant_type=password&username=<user-name>&password=<example-password>&scope=<Resource Server Scope>%20offline_access'
```

**Example Request Using a JWT Client Assertion**
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token -d 'grant_type=password&username=<user-name>&password=<example-password>&client_id=<client-id>&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<client-assertion>&scope=<scope value>'
```

**Example Request Using a JWT Client Assertion Including Refresh Token in the Request**
```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token -d 'grant_type=password&username=<user-name>&password=<example-password>&client_id=<client-id>&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<client-assertion>&scope=<Resource Server Scope>%20offline_access'
```

  3. The OAuth Authorization Server returns the access token. The access token contains all applicable scopes based on the privileges represented by the identity domain application roles granted to the requesting client application and the user being specified by the client's request (if present).
**Note** If a request was made for an invalid scope, an error is returned instead of the access token. 
  4. The requesting site uses the access token in an API call to obtain protected data.


Was this article helpful?
YesNo

