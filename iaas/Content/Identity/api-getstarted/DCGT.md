Updated 2024-04-02
# Device Code Grant Type
Use this grant type when a client runs on devices that don't have an easy data-entry method (for example, game consoles, streaming media players and digital picture frames), and the client is incapable of receiving incoming requests from the authorization server.
For example, a customer buys a Roku, digital picture frame, or game console. The customer needs an access token to fetch movies, pictures, or games from the cloud. Instead of interacting with the user's streaming media player (such as a Roku) or digital picture frame, the client instructs the user to use another computer or device (a desktop computer, smart phone, or tablet) and connect to the authorization server to approve the access request. Because the client can't receive incoming requests, it polls the authorization server repeatedly until the user completes the approval process.
The following diagram displays the Device Code Grant Type flow. 
![A diagram that illustrates the Device Code Grant Type flow.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/diag6_device_code_granttype.png)
In this OAuth flow:
**Note** This device flow doesn't use the client secret to obtain the device code and the user code. The client secret is used (if assigned to the client) when obtaining the access token.
  1. A device client makes an unauthenticated request to an identity domain `/device` endpoint. The device receives a device code, user code, and a verification URI.
The device client displays the user code `(user_code)` to the user and provides the URL `(verification-uri)` where the user needs to go to enter the user code (not shown in diagram).
  2. The device client doesn't know if the user is authorized. The device client requests the access token repeatedly (to `oauth2/v1/token)` in the background until the user enters the user code on the verification page.
  3. The user access the verification page, signs in, and then enters the user code.
  4. After the user enters the user code and authorizes access, an access token is issued by the OAuth server, and the user is given access to the protected data through the device.


Function | Available  
---|---  
Browser-based end-user interaction | Yes  
Can use an external Identity Provider for authentication | Yes  
Refresh token is allowed | Yes  
See an example [Device Code Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/DCGT.htm#DeviceCodeFlowAuth "The Device Code grant type provides a specific grant flow in which a device client runs on a device that doesn't have an easy data-entry method \(for example, game consoles, streaming media players and digital picture frames\), and the device client is incapable of receiving incoming requests from the authorization server.").
## Device Code Grant Type Authorization Flow Example 🔗 
The Device Code grant type provides a specific grant flow in which a device client runs on a device that doesn't have an easy data-entry method (for example, game consoles, streaming media players and digital picture frames), and the device client is incapable of receiving incoming requests from the authorization server.
To obtain an access token to access protected resources through a device client, instead of interacting directly with the device client, the device client instructs the user to use another computer or device and connect to the authorization server to approve the access request. The device client polls the authorization server repeatedly until the user completes the approval process.
When you create an application using the Device Code grant type in the identity domain Console, select **Device Code** as the grant type.
See [Device Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/DCGT.htm#DCGT "Use this grant type when a client runs on devices that don't have an easy data-entry method \(for example, game consoles, streaming media players and digital picture frames\), and the client is incapable of receiving incoming requests from the authorization server.") for more information on the Device Code grant type and an authorization flow diagram.
**Authorization Flow**
  1. A device client makes an unauthenticated request to the `/oauth2/v1/device` endpoint.
The event URL contains query parameters that indicate the type of access being requested:
**Request Example**
```
  curl -i -k 
  -H 'Authorization: application/x-www-form-urlencoded; charset=utf-8'
  --request POST 'https://<domainURL>/oauth2/v1/device'
  -d 'response_type=device_code&scope=http://example.com/quotes&client_id=<client-id>'
```

  2. The response contains a device code, user code, and a verification URI from the OAuth client application.
**Response Example**
```
{ 
"expires_in": 300, 
"device_code": "**4d03f7bc-f7a5-4795-819a-5748c4801d35**", 
"user_code": "SDFGHJKL",
"verification_uri": "http://<domainURL>/ui/v1/device" 
}
```

  3. The device displays the user code `(user_code)` and provides the URL `(validation-uri)` where the user needs to go to enter the user code.
  4. The device client application doesn't know if the user is authorized. While the user authorizes (or denies) the client's request, the client repeatedly polls the authorization server at the token endpoint `(oauth2/v1/token)` to find out if the user completed the user authorization step. The client includes the verification code and its client identifier in the request.
**Request Example: Confidential Client**
```
  curl -i -k 
  -H 'Authorization: application/x-www-form-urlencoded; charset=utf-8' 
  -H 'Authorization: Basic <base64 clientid:secret> 
  --request POST 'https://<domainURL>/oauth2/v1/token'
  -d 'grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=4d03f7bc-f7a5-4795-819a-5748c4801d35'
```

**Request Example: Public Client**
```
  curl -i -k 
  -H 'Authorization: application/x-www-form-urlencoded; charset=utf-8' 
  --request POST 'https://<domainURL>/oauth2/v1/token'
  -d 'grant_type=urn:ietf:params:oauth:grant-type:device_code&client_id=3e51760ceb1245b7b77d0b1ff280bb72&device_code=4d03f7bc-f7a5-4795-819a-5748c4801d35'
```

**Request Example Using a Client Assertion**
```
  curl -i -k 
  -H 'Authorization: application/x-www-form-urlencoded; charset=utf-8' 
  --request POST 'https://<domainURL>/oauth2/v1/token'
  -d 'grant_type=urn:ietf:params:oauth:grant-type:device_code&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<clientAssertion>&device_code=4d03f7bc-f7a5-4795-819a-5748c4801d35'
```

**Request Example Using a SAML Assertion**
```
  curl -i -k 
  -H 'Authorization: application/x-www-form-urlencoded; charset=utf-8' 
  --request POST 'https://<domainURL>/oauth2/v1/token'
  -d 'grant_type=urn:ietf:params:oauth:grant-type:device_code&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Asaml2-bearer&client_assertion=<samlAssertion>&device_code=4d03f7bc-f7a5-4795-819a-5748c4801d35'
```

  5. After the user enters the user code and authorizes access, the OAuth Authorization Server authenticates the user and returns an access token that contains all applicable scopes based on the privileges represented by the application roles granted to the requesting client application.
  6. The requesting device client uses the access token in an API call to obtain protected data.


Was this article helpful?
YesNo

