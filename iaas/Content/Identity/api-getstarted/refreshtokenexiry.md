Updated 2024-04-15
# Updating Refresh Token Expirations
Refresh tokens carry the information necessary to get a new access token. In other words, whenever an access token is required to access a specific resource, a client may use a refresh token to get a new access token issued by the authentication server. 
A common use case is getting new access tokens after old ones have expired, such as an access token expiring on a mobile app. The mobile app sends the refresh token to obtain a new access token with no need for caching the user's password.
Refresh tokens do expire, but are typically long-lived.
Use the following steps when you want to see how long the refresh token is valid or when you need to update the refresh token value. 
**Note** The default value for the `refreshTokenExpiry` attribute is seven days. The value is listed in seconds: `604800.`
## Get the Current Refresh Token Expiration Value 🔗 
Make a GET request to the `/Apps` endpoint, requesting a specific App ID, and then specify the `refreshTokenExpiry` attribute.
**Request Example**
```
GET <domainURL>/admin/v1/Apps/{{appID}}**?attributes=refreshTokenExpiry**
```

**Response Example**
The `refreshTokenExpiry` attribute is returned in the response (in bold in the example).
```
{
  "isAliasApp": false,
  "displayName": "ResourceOwner",
  **"refreshTokenExpiry": 604800,**
  "id": "{{appID}}",
  "basedOnTemplate": {
    "value": "CustomWebAppTemplateId"
  }
}
```

Alternatively, you can make a GET request to the `/Apps` endpoint, requesting a specific App ID to return all application-specific attributes, including the `refreshTokenExpiry` attribute.
**Request Example**
```
GET <domainURL>/admin/v1/Apps/{{appID}}
```

**Response Example**
The `refreshTokenExpiry` attribute is returned in the response (in bold in the example).
```
{
  "accessTokenExpiry": 3600,
  "clientType": "confidential",
  "isAliasApp": false,
  "audience": "<domainURL>",
  "meta": {
    "created": "2022-06-25T16:10:26.953Z",
    "lastModified": "2022-06-25T20:37:14.039Z",
    "resourceType": "App",
    "location": "https://<domainURL>/admin/v1/Apps/9fc12da9eecd4927a9ef88512ce5612e"
  },
  "active": true,
  "isLoginTarget": true,
  "idcsCreatedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "855344f8015347e1a26c1ac9b2a2898e",
    "$ref": "https://<domainURL>/admin/v1/Users/855344f8015347e1a26c1ac9b2a2898e"
  },
  "displayName": "ResourceOwner",
  "showInMyApps": false,
  "isMobileTarget": false,
  "allowOffline": true,
  "isUnmanagedApp": false,
  "idcsLastModifiedBy": {
    "display": "OAuthClient",
    "type": "App",
    "value": "66efab799b084c21bf84edcf1f587380",
    "$ref": "https://<domainURL>/admin/v1/Apps/66efab799b084c21bf84edcf1f587380"
  },
  "isOPCService": false,
  **"refreshTokenExpiry": 604800,**
  "name": "3fd7476a48a94381bd5e1bc88cc92021",
  "isOAuthClient": true,
  "isManagedApp": false,
  "isSamlServiceProvider": false,
  "infrastructure": false,
  "allUrlSchemesAllowed": true,
  "trustScope": "Explicit",
  "id": "9fc12da9eecd4927a9ef88512ce5612e",
  "isWebTierPolicy": false,
  "loginMechanism": "OIDC",
  "allowAccessControl": false,
  "isOAuthResource": true,
  "migrated": false,
  "isKerberosRealm": false,
  "attrRenderingMetadata": [
    {
      "name": "aliasApps",
      "visible": false
    }
  ],
  "basedOnTemplate": {
    "lastModified": "2022-05-04T10:47:12Z",
    "value": "CustomWebAppTemplateId",
    "$ref": "https://<domainURL>/admin/v1/AppTemplates/CustomWebAppTemplateId"
  },
  "redirectUris": [
    "http://localhost:8943"
  ],
  "allowedGrants": [
    "client_credentials",
    "refresh_token",
    "authorization_code"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ],
  "clientSecret": "this-is-not-the-secret",
  "grantedAppRoles": [
    {
      "value": "29722be952c14f9fac5237e5dd088660",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/29722be952c14f9fac5237e5dd088660",
      "appId": "IDCSAppId",
      "display": "identity domain administrator",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    },
    {
      "value": "6aa28be4b79143099e90e5dcdd820844",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/6aa28be4b79143099e90e5dcdd820844",
      "appId": "IDCSAppId",
      "display": "Me",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    },
    {
      "value": "99224c8907d84560b9621dcda9ecb8b4",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/99224c8907d84560b9621dcda9ecb8b4",
      "appId": "IDCSAppId",
      "display": "Cloud Gate",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    }
  ]
}
```

## Change the Refresh Token Value 🔗 
To update the `refreshTokenExpiry` attribute value, make a PATCH request to the `/Apps` endpoint specifying the App ID, and then define the updated `refreshTokenExpiry` attribute value in the payload.
**Request Example**
```
PATCH <domainURL>/admin/v1/Apps/{{appid}}
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [{
   "op": "replace",
   "path": "refreshTokenExpiry",
   **"value": 904800 **
  }
]
}
```

**Response Example**
The response returned includes the updated `refreshTokenExpiry` attribute value (in bold in the example).
```
{
  "accessTokenExpiry": 3600,
  "clientType": "confidential",
  "isAliasApp": false,
  "audience": "https://<domainURL>",
  "meta": {
    "created": "2022-06-25T16:10:26.953Z",
    "lastModified": "2022-06-25T20:37:14.039Z",
    "resourceType": "App",
    "location": "https://<domainURL>/admin/v1/Apps/9fc12da9eecd4927a9ef88512ce5612e"
  },
  "active": true,
  "isLoginTarget": true,
  "idcsCreatedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "855344f8015347e1a26c1ac9b2a2898e",
    "$ref": "https://<domainURL>/admin/v1/Users/855344f8015347e1a26c1ac9b2a2898e"
  },
  "displayName": "ResourceOwner",
  "showInMyApps": false,
  "isMobileTarget": false,
  "allowOffline": true,
  "isUnmanagedApp": false,
  "idcsLastModifiedBy": {
    "display": "OAuthClient",
    "type": "App",
    "value": "66efab799b084c21bf84edcf1f587380",
    "$ref": "https://<domainURL>/admin/v1/Apps/66efab799b084c21bf84edcf1f587380"
  },
  "isOPCService": false,
  **"refreshTokenExpiry": 904800,**
  "name": "3fd7476a48a94381bd5e1bc88cc92021",
  "isOAuthClient": true,
  "isManagedApp": false,
  "isSamlServiceProvider": false,
  "infrastructure": false,
  "allUrlSchemesAllowed": true,
  "trustScope": "Explicit",
  "id": "9fc12da9eecd4927a9ef88512ce5612e",
  "isWebTierPolicy": false,
  "loginMechanism": "OIDC",
  "allowAccessControl": false,
  "isOAuthResource": true,
  "migrated": false,
  "isKerberosRealm": false,
  "attrRenderingMetadata": [
    {
      "name": "aliasApps",
      "visible": false
    }
  ],
  "basedOnTemplate": {
    "lastModified": "2022-05-04T10:47:12Z",
    "value": "CustomWebAppTemplateId",
    "$ref": "https://<domainURL>/admin/v1/AppTemplates/CustomWebAppTemplateId"
  },
  "redirectUris": [
    "http://localhost:8943"
  ],
  "allowedGrants": [
    "client_credentials",
    "refresh_token",
    "authorization_code"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ],
  "clientSecret": "this-is-not-the-secret",
  "grantedAppRoles": [
    {
      "value": "29722be952c14f9fac5237e5dd088660",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/29722be952c14f9fac5237e5dd088660",
      "appId": "IDCSAppId",
      "display": "identity domain administrator",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    },
    {
      "value": "6aa28be4b79143099e90e5dcdd820844",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/6aa28be4b79143099e90e5dcdd820844",
      "appId": "IDCSAppId",
      "display": "Me",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    },
    {
      "value": "99224c8907d84560b9621dcda9ecb8b4",
      "$ref": "https://<domainURL>/admin/v1/AppRoles/99224c8907d84560b9621dcda9ecb8b4",
      "appId": "IDCSAppId",
      "display": "Cloud Gate",
      "type": "direct",
      "appName": "IDCSApp",
      "adminRole": true
    }
  ]
}
```

Was this article helpful?
YesNo

