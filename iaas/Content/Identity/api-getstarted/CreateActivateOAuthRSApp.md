Updated 2024-04-02
# Creating and Activating an OAuth Resource Server
This section provides example requests to create and activate an OAuth Resource Server using the identity domains REST API.
## Create an OAuth Resource Server App 🔗 
A resource server application is a third-party application that provides services that a web application can consume on behalf of the user. The example below shows how to craft a request to create an OAuth Resource application.
**Note** If you're using the optional `name` attribute in your request, be sure to use only alphanumeric characters and the underscore ( _ ) character in the value.
```
echo "Create OAuth Resource App"
cat>/tmp/OAuthResourceApp.json << __EOF__
{
"schemas":["urn:ietf:params:scim:schemas:oracle:idcs:App"],
"displayName":"Example_Service1",
"description":"example service1",
"audience":"http://example.com/",
"isOAuthResource": true,
"basedOnTemplate": {
   "value": "CustomWebAppTemplateId"
},
"scopes": [
        {
           "description": "photos",
           "requiresConsent": true,
           "value": "photos"
        },
        {
           "description": "presentations",
           "requiresConsent": true,
           "value": "presentations"
        },
        {
           "description": "documents",
           "requiresConsent": true,
           "value": "documents"
        },
        {
           "description": "user",
           "requiresConsent": false,
           "value": "UserProfile.me"
        },
        {
           "description": "sample",
           "requiresConsent": false,
           "value": "test1.scope"
        }
      ]
}
__EOF__
curl -X POST 
-H "Content-type: application/json" 
-H "Authorization: Bearer <access token value>" 
--data @/tmp/OAuthResourceApp.json http://<domainURL>/admin/v1/Apps
```

**Required App Attributes for an OAuth Resource Server App**
Required App Attribute | Description  
---|---  
`displayName` | Identifies the display name of the application. Display name is intended to be user-friendly, and an administrator can change the value at any time.  
`basedOnTemplate` | Indicates the application template on which the application is based.  
`isOAuthResource` | If set to `true`, indicates that this application acts as an OAuth Resource.  
`audience` | Identifies the base URI for all the scopes defined in this App. The value of `audience` is combined with the `value` of each scope to form an `fqs` (fully-qualified scope).  
## Activate an OAuth Resource App 🔗 
Use the following example to create a request to activate an OAuth Resource Server application.
```
echo "Activate OAuth Resource App"
cat>/tmp/OAuthResourceApp.json << __EOF__
{
    "active" : true,
    "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:AppStatusChanger"
    ]
}
__EOF__
curl -X PUT 
-H "Content-type: application/json" 
-H "Authorization: Bearer <access token value>" 
--data @/tmp/OAuthResourceApp.json http://<domainURL>/admin/v1/AppStatusChanger/<appID>
```

Was this article helpful?
YesNo

