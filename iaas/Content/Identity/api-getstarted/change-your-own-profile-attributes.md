Updated 2024-04-08
# Using allowSelfChange To Update Profile Attributes
You can use the API to change your own profile attributes (for example, an email address or a password) in an identity domain by setting the `allowSelfChange` attribute to `true` in the request payload or URL query string parameter. By default, this attribute is set to `false`.
Use the `allowSelfChange` attribute in the request payload for the following operations: 
  * Users (PATCH, REPLACE)
  * UserCapabilityChanger (REPLACE)
  * UserLockedStateChanger (CREATE)
  * UserPasswordChanger (REPLACE)
  * UserPasswordResetter (REPLACE)
  * UserStateChanger (PATCH)
  * UserStatusChanger (REPLACE)
  * UserDbCredentials (CREATE)
  * ApiKeys (CREATE, UPDATE)
  * AuthTokens (CREATE, UPDATE)
  * CustomerSecretKeys (CREATE, UPDATE)
  * OAuth2ClientCredentials (CREATE, UPDATE)
  * SmtpCredentials (CREATE, UPDATE)
  * SupportAccounts (CREATE)


Use the `allowSelfChange` attribute as a URL query string parameter for the DELETE operation on the following APIs. 
**Note** You must set `allowSelfChange=true` as a URL query string parameter for DELETE operations. 
  * UserDbCredentials
  * ApiKeys
  * AuthTokens
  * CustomerSecretKeys
  * OAuth2ClientCredentials
  * SmtpCredentials
  * SupportAccounts


## Sample Request: /Users
Operation: PATCH `/admin/v1/Users/<id>````
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "replace",
      "path": "phoneNumbers",
      "value": [
        {
          "type": "home",
          "value": "555-555-0100"
        }
      ]
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
  ]
}
```

## Sample Request: /UserCapabilitiesChanger
Operation: PUT `/admin/v1/UserCapabilitiesChanger/<id>````
{
  "canUseApiKeys": true,
  "canUseAuthTokens": false,
  "canUseConsolePassword": true,
  "canUseCustomerSecretKeys": true,
  "canUseOAuth2ClientCredentials": true,
  "canUseSmtpCredentials": true,
  "canUseDbCredentials": true,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:UserCapabilitiesChanger"
  ]
}
```

## Sample Request: /UserLockedStateChanger
Operation: POST `/admin/v1/UserLockedStateChanger````
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:UserLockedStateChanger"
  ],
  "userId": "<unique_ID>",
  "locked": false,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true
}
```

## Sample Request: /UserPasswordChanger
Operation: PUT `/admin/v1/UserPasswordChanger````
{
  "password": "example-password",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
   "urn:ietf:params:scim:schemas:oracle:idcs:UserPasswordChanger"
  ]
 }

```

## Sample Request: /UserPasswordResetter
Operation: PUT `/admin/v1/UserPasswordResetter````
{
  "schemas": [
   "urn:ietf:params:scim:schemas:oracle:idcs:UserPasswordResetter"
  ],
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true
 }

```

## Sample Request: /UserStatusChanger
Operation: PUT `/admin/v1/UserStatusChanger````
{
  "active": true,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
   "urn:ietf:params:scim:schemas:oracle:idcs:UserStatusChanger"
  ]
 }

```

## Sample Requests: /ApiKeys
Operation: POST `/admin/v1/ApiKeys````
{
  "user": {
    "value": "<unique_ID>"
  },
  "key": "-----BEGIN PUBLIC KEY-----<your_public_key>
 -----END PUBLIC KEY-----",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:apikey"
  ]
}

```

Operation: PATCH `/admin/v1/ApiKeys/<id>````
{
   "Operations": [
    {
     "op": "replace",
     "path": "description",
     "value": "<updated_api_key>"
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
   ],
   "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ]
  }

```

Operation: DELETE `/admin/v1/ApiKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
## Sample Requests: /SmtpCredentials
Operation: POST `/admin/v1/SmtpCredentials/<id>````
{
  "description": "John's smtp credential",
  "user": {
    "value": "<unique_ID>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:smtpCredential"
  ]
}

```

Operation: PATCH `/admin/v1/SmtpCredentials````
{
   "Operations": [
    {
     "op": "replace",
     "path": "description",
     "value": "updated_credential_description"
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
   ],
   "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ]
  }

```

Operation: DELETE `/admin/v1/SmtpCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
## Sample Requests: /AuthTokens
Operation: POST `/admin/v1/AuthTokens````
{
  "description": "John's auth token",
  "user": {
    "value": "<unique_ID>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:authToken"]
}

```

Operation: PATCH `/admin/v1/AuthTokens/<id>````
{
   "Operations": [
    {
     "op": "replace",
     "path": "description",
     "value": "<updated_credential_description>"
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
   ],
   "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ]
  }

```

Operation: DELETE `/admin/v1/SmtpCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
## Sample Requests: /CustomerSecretKeys
Operation: POST `/admin/v1/CustomerSecretKeys````
{
  "diplayName": "Alice Customer Secret Key",
  "description": "Alice's Customer Secret Key",
  "user": {
    "value": "<unique_ID>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:customerSecretKey"
  ]
}

```

Operation: PATCH `/admin/v1/CustomerSecretKeys/<id>````
{
   "Operations": [
    {
     "op": "replace",
     "path": "description",
     "value": "<updated_credential_description>"
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
   ],
   "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ]
  }

```

Operation: DELETE `/admin/v1/CustomerSecretKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
## Sample Requests: /OAuth2ClientCredentials
Operation: POST `/admin/v1/OAuth2ClientCredentials````
{
 "name": "User's oauth2 client credential",
 "scopes": [
  {
   "audience": "urn:opc:idm",
   "scope": "__myscopes__"
  }
 ],
 "user": {
  "value": "<unique_ID>"
 },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true,
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:oauth2ClientCredential"
 ]
}

```

Operation: PATCH `/admin/v1/OAuth2ClientCredentials/<id>````
{
   "Operations": [
    {
     "op": "replace",
     "path": "description",
     "value": "<updated_credential_description>"
    },
    {
      "op": "add",
      "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange",
      "value": true
    }
   ],
   "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ]
  }

```

Operation: DELETE `/admin/v1/OAuth2ClientCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
## Sample Request: /SupportAccounts
Operation: POST `/admin/v1/SupportAccounts````
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:supportAccount"
  ],
  "token": "dummy",
  "user": {
    "ocid": "ocid1.user.region1..<unique_ID>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User:allowSelfChange": true
}

```

Operation: DELETE `/admin/v1/ApiKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
Was this article helpful?
YesNo

