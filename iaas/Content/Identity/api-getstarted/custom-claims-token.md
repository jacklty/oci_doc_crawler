Updated 2024-04-02
# Managing Custom Claims
You can use the identity domains REST API to add custom claims to an access token, an identity token, or both the tokens. 
Custom claims are rules that you can add to a token for the identity domain. There's no limit for the number of custom claims in a token. Token size is limited and the allowed values are "8000", "16000","32000", "128000".
The cURL command examples use the URL structure:```
https://<domainURL>/admin/v1/CustomClaims/{id}
```

  1. Specify the headers on the cURL command line:
```
  -H Authorization: Bearer <Access Token>
  -H Cache-Control: no-cache
  -H Accept:application/json
```

To obtain an access token, see [Working with OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm "The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to programmatically manage users, groups, applications, and identity functions, such as password management and administrative tasks. To make REST API calls to your identity domain, you need an OAuth2 access token to use for authorization. The access token provides a session \(with scope and expiration\), that your client application can use to perform tasks in an identity domain.").
  2. Create the custom claim name `MyATCustomClaim` and value `MyATValue` for the access token by running the following command:
```
  curl -i -X POST https://<domainURL>/admin/v1/CustomClaims
```

**Example**
```
  curl -i -X POST https://<domainURL>/admin/v1/CustomClaims
```

The following is an example of a JSON request body to create the custom claim:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ],
  "name": "MyATCustomClaim",
  "value": "MyATValue",
  "expression": false,
  "mode": "always",
  "tokenType": "AT",
  "allScopes": true
}
```

Attribute |  Description  
---|---  
`name` |  The custom claim name. **Note:** Maximum length is 100 characters.  
`value` |  The custom claim value. **Note:** Maximum length is 100 characters. If the value comes from the evaluation of a user expression, then there's no limit.  
`expression` |  Specify if the custom claim value is a user expression. You can determine the user expression by using the Users endpoints. Value: `true` or `false` **Example User Expression**
     * `$user.name.formatted expression` with value `admin opc`.
     * `$user.emails.0.type` expression with value `recovery`.
     * `$user.emails.1.type` expression with value `work`.
     * `$user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User.myCustomAttribute` expression with value `customValue`.
Based on user expressions, a claim returns either a single value attribute or all the attributes associated with the expression. For example, the following expressions return a single value within an array:
     * `$user.emails.0.value`
     * `$(user.emails[0].value)`
While the following expressions return an array:
     * `$user.emails.*.value`
     * `$(user.emails[*].value)`  
`allScopes` |  Specify whether associate the custom claim with a set of scopes or all the scopes. Value: `true` or `false`  
`mode` | Specify how you want to attach the custom claim to a token.
     * `always`: The custom claim will be attached to the token.
     * `request`: The custom claim will be attached to the token only if it's requested or overridden.
     * `never`: The custom claim will not be attached to the token.  
`tokenType` |  Specify the token type.
     * `AT`: To add custom claim for an access token.
     * `IT`: To add custom claim for an identity token.
     * `BOTH`: To add custom claim for the access and identity token.  
scopes |  Optional. The Custom Claim will be embedded to tokens if any scope in the scopes array is requested in the token request. You can either specify `allScopes` equals to `true` with no associated scopes array or has `allScopes` equals to `false` with associated scopes array.  
The following shows an example of the response body:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ],
  "name": "MyATCustomClaim",
  "value": "MyATValue",
  "expression": false,
  "mode": "always",
  "tokenType": "AT",
  "allScopes": true,
  "id": "ddc7f88bea2a46258c593bddccaf2b86",
  "meta": {
    "created": "2022-05-17T04:33:43.640Z",
    "lastModified": "2022-05-17T04:33:43.640Z",
    "resourceType": "CustomClaim",
    "location": "https://<domainURL>/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86"
  },
  "idcsCreatedBy": {
    "value": "bac027a9500c4db9a09f5cfbcbda5076",
    "type": "App",
    "display": "exampleDomainAdmin",
    "$ref": "https://<domainURL>/admin/v1/Apps/bac027a9500c4db9a09f5cfbcbda5076"
  },
  "idcsLastModifiedBy": {
    "value": "bac027a9500c4db9a09f5cfbcbda5076",
    "type": "App",
    "display": "exampleDomainAdmin",
    "$ref": "https://<domainURL>/admin/v1/Apps/bac027a9500c4db9a09f5cfbcbda5076"
  }
}
```

You can derive the user expression from the `/admin/v1/Users` endpoint. This is the JSON returned for an admin user.
The values are parsed as String, and the bold in the sample shows how the values are derived for the following expressions.
Expression |  Value  
---|---  
`$user.name.formatted` |  "admin opc"  
`$user.emails.0.type` This expression and the next are an unlabeled array, with a number that starts from 0 to indicate the index of the element in the array. |  "recovery"  
`$user.emails.1.type` |  "work"  
`$user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User.myCustomAttribute` |  "customValue"  
```
{
  "idcsCreatedBy": {
    "type": "App",
    "display": "idcssm",
    "value": "32e72bc93b30417697f323d5fa7bbe2e",
    "$ref": "https://<domainURL>/admin/v1/Apps/32e72bc93b30417697f323d5fa7bbe2e"
  },
  "id": "60703e0bddcf4dae9add114179bf042d",
  "meta": {
    "created": "2022-11-08T02:39:01.932Z",
    "lastModified": "2022-11-13T09:44:55.668Z",
    "resourceType": "User",
    "location": "https://<domainURL>/admin/v1/Users/60703e0bddcf4dae9add114179bf042d"
  },
  "active": true,
  "displayName": "admin opc",
  "idcsLastModifiedBy": {
    "value": "f79371bb03914056821a8afb9da5066d",
    "display": "idcssso",
    "type": "App",
    "$ref": "https://<domainURL>/admin/v1/Apps/f79371bb03914056821a8afb9da5066d"
  },
  "nickName": "TAS_TENANT_ADMIN_USER",
  "userName": "admin@oracle.com",
  **"urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"**: {
    "isFederatedUser": false,
    **"myCustomAttribute": "customValue"**
  },
  **"emails"**: [
    {
      "verified": false,
      "primary": false,
      "secondary": false,
      "value": "admin@oracle.com",
      **"type": "recovery"**
    },
    {
      "verified": false,
      "primary": true,
      "secondary": false,
      "value": "admin@oracle.com",
      **"type": "work"**
    }
  ],
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  **"name"**: {
    "familyName": "opc",
    "givenName": "admin",
    **"formatted": "admin opc"**
  }
}
```

  3. Replace all the attributes for the custom claim id `ddc7f88bea2a46258c593bddccaf2b86` by running the following command:
```
  curl -i -X PUT https://<domainURL>/admin/v1/CustomClaims/{id}
```

**Example**
```
  curl -i -X PUT https://<domainURL>/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86
```

The following shows an example of the request body.
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ],
  "name": "MyATClaim1",
  "value": "MyATValue1",
  "expression": false,
  "mode": "request",
  "tokenType": "AT",
  "allScopes": true
}
```

The following shows an example of the response indicating the request succeeded.
```
{
  "idcsLastModifiedBy": {
    "type": "App",
    "value": "bac027a9500c4db9a09f5cfbcbda5076",
    "display": "exampleDomainAdmin",
    "$ref": "https://<domainURL>/admin/v1/Apps/bac027a9500c4db9a09f5cfbcbda5076"
  },
  "idcsCreatedBy": {
    "type": "App",
    "display": "exampleDomainAdmin",
    "value": "bac027a9500c4db9a09f5cfbcbda5076",
    "$ref": "https://<domainURL>/admin/v1/Apps/bac027a9500c4db9a09f5cfbcbda5076"
  },
  "mode": "request",
  "id": "ddc7f88bea2a46258c593bddccaf2b86",
  "value": "MyATValue1",
  "expression": false,
  "meta": {
    "created": "2022-05-17T04:33:43.640Z",
    "lastModified": "2022-05-17T04:41:13.177Z",
    "resourceType": "CustomClaim",
    "location": "https://<domainURL>/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86"
  },
  "allScopes": true,
  "name": "MyATCustomClaim1",
  "tokenType": "AT",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ]
}
```

  4. Set the `allScopes` to `false` for the id `ddc7f88bea2a46258c593bddccaf2b86` by running the following command:
```
  curl -i -X PATCH https://<domainURL>/admin/v1/CustomClaims/{id}
```

**Example**
```
  curl -i -X PATCH https://<domainURL>/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86
```

The following shows an example of the request body.
```
{
  "Operations": [
    {
      "op": "replace",
      "path": "allScopes",
      "value": false
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
```

The following shows an example of the response indicating the request succeeded.
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "210d294a075a4c86bbf6f958bceacf0c",
    "display": "admin opc",
    "$ref": "https://yourtenant.identity.oraclecloud.com/admin/v1/Users/210d294a075a4c86bbf6f958bceacf0c"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "210d294a075a4c86bbf6f958bceacf0c",
    "$ref": "https://<domainURL>/admin/v1/Users/210d294a075a4c86bbf6f958bceacf0c"
  },
  "mode": "always",
  "id": "ddc7f88bea2a46258c593bddccaf2b86",
  "value": "MyATValue",
  "expression": false,
  "meta": {
    "created": "2022-05-31T05:43:32.518Z",
    "lastModified": "2022-05-31T05:58:10.362Z",
    "resourceType": "CustomClaim",
    "location": "https://yourtenant.identity.oraclecloud.com/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86"
  },
  "allScopes": false,
  "name": "MyATCustomClaim",
  "tokenType": "AT",
  "scopes": [
    "phone"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ]
}
```

  5. View all the custom claims in the tenant by running the following command:
```
  curl -i -X GET https://<domainURL>/admin/v1/CustomClaims
```

**Example**
```
  curl -i -X GET https://<domainURL>/admin/v1/CustomClaims
```

The following shows an example of the response body.```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "210d294a075a4c86bbf6f958bceacf0c",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/ddc7f88bea2a46258c593bddccaf2b86"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "ddc7f88bea2a46258c593bddccaf2b86",
    "$ref": "https://<domainURL>/admin/v1/Users/210d294a075a4c86bbf6f958bceacf0c"
  },
  "mode": "always",
  "id": "98e94996776845719cf3b737e565199a",
  "value": "MyATValue",
  "expression": false,
  "meta": {
    "created": "2022-05-31T05:43:32.518Z",
    "lastModified": "2022-05-31T05:58:10.362Z",
    "resourceType": "CustomClaim",
    "location": "https://<domainURL>/admin/v1/CustomClaims/98e94996776845719cf3b737e565199a"
  },
  "allScopes": false,
  "name": "MyATCustomClaim",
  "tokenType": "AT",
  "scopes": [
    "phone"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:CustomClaim"
  ]
}
```

  6. View the custom claims in a tenant by providing the query parameter.
```
  curl -i -X GET https://<domainURL>/admin/v1/CustomClaims?attributes=(schema attributes)
```

**Example**
```
  curl -i -X GET https://yourtenant.identity.oraclecloud.com/admin/v1/CustomClaims?attributes=name,value
```

The following shows an example of the response body after providing the query parameter `?attributes=name,value`:
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 4,
  "Resources": [
    {
      "name": "AlwaysAllScopesATClaim10",
      "id": "edf077cbae59435dab3f9de5ba1fd619",
      "value": "AlwaysAllScopesATValue"
    },
    {
      "name": "MyATCustomClaim1",
      "id": "ddc7f88bea2a46258c593bddccaf2b86",
      "value": "MyATValue1"
    },
    {
      "name": "MyATCustomClaim",
      "id": "150d1eae9f0f4301a22312bd680aa4df",
      "value": "MyATValue"
    },
    {
      "name": "MyATCustomClaim2",
      "id": "2680b220be904698b43575e3d654a88c",
      "value": "MyATValue2"
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 50
}
```

  7. Optionally, delete the custom claim from the tenant by running the following command:
```
  curl -i -X DELETE https://<domainURL>/admin/v1/CustomClaims/{id}
```

**Example**
```
  curl -i -X DELETE https://<domainURL>/admin/v1/CustomClaims/ddc7f88bea2a46258c593bddccaf2b86
```



Was this article helpful?
YesNo

