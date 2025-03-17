Updated 2024-04-02
# Creating and Activating an OAuth Client App
This section provides example requests to create and activate an OAuth Client App using the identity domains REST API.
## Create an OAuth Client App 🔗 
An OAuth client application is an HTTP client that can acquire, and then use an access token. There are three types of OAuth client applications that you can create: Confidential, Trusted, and Public. Both the confidential and trusted client apps are specified by using `CustomWebAppTemplateId` as the value for the `basedOnTemplate` attribute. The public client app is specified by using `CustomBrowserMobileTemplateId` as the value for the `basedOnTemplate` attribute. The following examples show how to craft a request to create each of the client application types.
If you're building an OAuth Client App that supports self-service operations, the client app must be granted the "Me" role. Granting the client this role ensures that the generated access token contains the scope `"urn:opc:idm:t.user.me"`. This scope allows the client to access endpoints to perform self-service operations such as `/Me,` `/MyApps`, and so on. Use the `/Grants` endpoint to grant an AppRole to an app.
**Note** If you're using the optional `name` attribute in your request, be sure to use only alphanumeric characters and the underscore ( _ ) character in the value.
**Confidential**
```
{
   "schemas": [
     "urn:ietf:params:scim:schemas:oracle:idcs:App"
    ],
   "displayName": "demoapp",
   "isOAuthClient" : true,
   "description": "demoapp",
   "active": true,
   "clientType": "confidential",
   "basedOnTemplate": {
     "value": "CustomWebAppTemplateId"
   },
   "redirectUris": [
     "http://<fully qualified url>/demoapp/return"
    ],
   "logoutUri": "http://<fully qualified url>/demoapp/logout.jsp",
   "postLogoutRedirectUris": ["http://<fully qualified url>/demoapp/logout.jsp"],
   "allUrlSchemesAllowed": true,
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
   "allowedGrants": [
     "authorization_code",
     "client_credentials",
     "password",
     "refresh_token",
     "urn:ietf:params:oauth:grant-type:jwt-bearer"
   ],
  "certificates":[ 
   {
   "certAlias":"SampleOAuthClient_1"
   }
  ]
}
curl -X POST
-H "Content-type: application/json"
-H "Authorization: Bearer <access token value>"
--data @/tmp/OAuthClientApp.json http://<domainURL>/admin/v1/Apps
```

**Trusted**
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ],
  "displayName": "trustedClientApp",
  "isOAuthClient" : true,
  "description": "trusted client",
  "active": true,
  "clientType": "trusted",
   "basedOnTemplate": {
    "value": "CustomWebAppTemplateId"
   },
  "redirectUris": [   
    "http://`hostname -f`:9090/demoapp/return",   
    "http://`hostname -f`:9090/IDCSExample"   
  ],
  "logoutUri": "http://`hostname -f`:9090/demoapp/logout.jsp",
  "postLogoutRedirectUris": ["http://`hostname -f`:9090/demoapp/logout.jsp"],
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
  "allowedGrants": [
    "authorization_code",
    "client_credentials",
    "password",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer"
  ],
  "certificates":[ 
   {
   "certAlias":"SampleOAuthClient_2"
   }
  ]
}
curl -X POST
-H "Content-type: application/json"
-H "Authorization: Bearer <access token value>"
--data @/tmp/OAuthClientApp.json http://<domainURL>/admin/v1/Apps
```

**Public**
**Note** See [onBehalfOf Allowed Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OnBehalfOf.htm "The onBehalfOf allowed operation provides a way to ensure that access privileges can be generated from the user's privileges alone, so that a client application can access endpoints to which the user has access, even if the client application by itself wouldn't normally have access.") for more information on using this allowed operation when you create a public OAuth Client application.
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ],
  "displayName": "publicClientApp",
  "isOAuthClient" : true,
  "description": "public client",
  "active": true,
  "clientType": "public",
   "basedOnTemplate": {
    "value": "CustomBrowserMobileTemplateId"
   },
  "redirectUris": [   
    "http://`hostname -f`:9090/demoapp/return",   
    "http://`hostname -f`:9090/IDCSPlayground"   
  ],
  "logoutUri": "http://`hostname -f`:9090/demoapp/logout.jsp",
  "postLogoutRedirectUris": ["http://`hostname -f`:9090/demoapp/logout.jsp"],
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
  "allowedGrants": [
    "authorization_code",
    "implicit"
  ]
} 
  curl -X POST
  -H "Content-type: application/json"
  -H "Authorization: Bearer <access token value>"
  --data @/tmp/OAuthClientApp.json http://<domainURL>/admin/v1/Apps
```

**Required App Attributes for an OAuth Client App**
Required App Attribute | Description  
---|---  
`displayName` | Identifies the display name of the application. Display name is intended to be user-friendly, and an administrator can change the value at any time.  
`basedOnTemplate` | Indicates the application template on which the application is based.  
`isOAuthClient` | If set to `true`, indicates that this application acts as an OAuth Client.  
`clientType` | Specifies the type of access that this App has when it acts as an OAuth Client. The possible values are `confidential,` `trusted`, and `public.`  
## Activate an OAuth Client App 🔗 
Use the following example to create a request to activate an OAuth Resource Server application.
```
{
    "active" : true,
    "schemas": [
       "urn:ietf:params:scim:schemas:oracle:idcs:AppStatusChanger"
    ]
}
  curl -X PUT 
  -H "Content-type: application/json"
  -H "Authorization: Bearer <access token value>"
  --data @/tmp/OAuthClientApp.json http://<domainURL>/admin/v1/AppStatusChanger/<appID>
```

Was this article helpful?
YesNo

