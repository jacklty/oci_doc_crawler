Updated 2024-04-09
# Using the onBehalfOf Allowed Operation
The `onBehalfOf` allowed operation provides a way to ensure that access privileges can be generated from the user's privileges alone, so that a client application can access endpoints to which the user has access, even if the client application by itself wouldn't normally have access.
When an authorized client application implements functionality that requires it to access identity domains endpoints, that client is granted the necessary privileges to do so. A web application client, on the other hand, implements functionality that requires the client application to access endpoints using the privileges and scopes acquired from the logged-in user. With identity domains default authorization behavior, that client must still have the full set of privileges required to access those endpoints without regard to the privileges granted to the user. The `onBehalfOf` allowed operation provides an administrator a way to indicate that the user's privileges alone should be used rather than an intersection of the user's scopes (if a user is present) and the client's scopes.
Public or CLI applications have very limited privileges or no privileges to access endpoints. These types of clients rely on the user who is accessing the application to drive what rights the application has. When a user is accessing a public application, if the user was issued an access token that's constructed from the user's privileges alone, that user would be able to access the endpoints as long as the user is authorized.
The `onBehalfOf` allowed operation enables you to generate such an access token for the OAuth Client application. When computing the identity domains specific scopes (scopes that begin with "`urn:opc:idm:`") to set in the access token, identity domains ignores the client's privileges and uses a scope equal to or less than the scope originally granted to the authorized user. So, only the user's privileges (admin roles, groups, and so on) in conjunction with the requested scopes are used to determine access. If the requested scope `"urn:opc:idm:_myscopes_"` is used, then all scopes that are granted to the user are returned.
## Enabling the onBehalfOf Allowed Operation
Use the identity domains REST API to create or update an OAuth application, and specify `onBehalfOfUser` as an allowed operation. When you create an OAuth application using the identity domains UI, on the **Authorization** page, select the checkbox for the **On behalf Of** allowed operation. When users access the application, they can perform various functions based on their permissions.
**Example**
The example shows how to create an application and specify the `onBehalfOfUser` allowed operation (in bold in the example).
```
cat</tmp/OAuthClientApp.json << __EOF__
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:App"
 ],
 "displayName": "publicClientApp",
 "isOAuthClient": true,
 "description": "public client",
 "active": true,
 "clientType": "public",
 "basedOnTemplate": {
  "value": "CustomBrowserMobileTemplateId"
 },
 "redirectUris": [
  "http://example.com:9090/demoapp/return",
  "http://example.com:9090/IDCSPlayground"
 ],
 "logoutUri": "http://example.com:9090/demoapp/logout.jsp",
 "postLogoutRedirectUris": ["http://example.com:9090/demoapp/logout.jsp"],
 "allowedScopes": [
  {
   "fqs": "http://example.com/photos"
  },
  {
   "fqs": "http://example.com/presentations"
  },
  {
   "fqs": "http://example.com/documents"
  }
 ],
 "allowedOperations": [
  "onBehalfOfUser"  ],
 "allowedGrants": [
  "authorization_code",
  "implicit"
 ]
}
__EOF__
  
curl -X POST 
-H "Content-type: application/json" 
-H "Authorization: Bearer <access token value>" 
--data @/tmp/OAuthClientApp.json http://<domainURL>/admin/v1/Apps
```

Was this article helpful?
YesNo

