Updated 2024-10-30
# GET, POST, PUT, PATCH Request and Response Examples
`GET`, `POST`, `PUT`, and `PATCH` requests and responses require a JSON request body.
## GET Request and Response Example 🔗 
The following is an example of a JSON request body used with a `GET` method to list a user, and the response.
**Request:**
```

GET {{HOST}}/admin/v1/Users/{{userid}}
```

**Response:**
```
{
  "idcsCreatedBy": {
    "type": "App",
    "display": "Confidential App",
    "value": "<app_id>",
    "ocid": "ocid1.domainapp.oc1.<unique_id>",
    "$ref": "https://<domain_url>/admin/v1/Apps/<app_id>"
  },
  "id": "<user_id>",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
    "isFederatedUser": false,
    "preferredUiLandingPage": "MyApps"
  },
  "meta": {
    "created": "2024-10-24T19:07:26.810Z",
    "lastModified": "2024-10-24T19:07:26.810Z",
    "version": "ddf2b4979d704f3d813e2636630da678",
    "resourceType": "User",
    "location": "https://<domain_url>/admin/v1/Users/ocid1.user.oc1..<unique_id>"
  },
  "active": true,
  "displayName": "Barbara Jensen",
  "idcsLastModifiedBy": {
    "value": "<app_id>",
    "display": "Confidential App",
    "ocid": "ocid1.domainapp.oc1.<unique_id>",
    "type": "App",
    "$ref": "https://<domain_url>/admin/v1/Apps/<app_id>"
  },
  "name": {
    "givenName": "Barbara",
    "familyName": "Jensen",
    "formatted": "Barbara Jensen"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  "ocid": "ocid1.user.oc1..<unique_id>",
  "userName": "bjensen",
  "emails": [
    {
      "value": "bjensen@exmple.com",
      "type": "work",
      "secondary": false,
      "verified": false,
      "primary": true
    },
    {
      "value": "bjensen@exmple.com",
      "type": "recovery",
      "secondary": false,
      "verified": false,
      "primary": false
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
  ],
  "domainOcid": "ocid1.domain.oc1..<unique_id>",
  "compartmentOcid": "ocid1.compartment.oc1..<unique_id>",
  "tenancyOcid": "ocid1.tenancy.oc1..<unique_id>",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:capabilities:User": {
    "canUseApiKeys": true,
    "canUseAuthTokens": true,
    "canUseConsolePassword": true,
    "canUseCustomerSecretKeys": true,
    "canUseOAuth2ClientCredentials": true,
    "canUseSmtpCredentials": true,
    "canUseDbCredentials": true
  }
} 
```

## POST Request and Response Example 🔗 
The following is an example of a JSON request body used with a `POST` method to create a new user, and the response.
**Request:**
```
{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:SearchRequest"],
 "attributes": ["displayName", "userName"],
 "filter":
     "userName sw \"bje\"",
 "startIndex": 1,
 "count": 10
}
```
**Response:**```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 1,
  "Resources": [
    {
      "displayName": "Barbara Jensen",
      "userName": "bjensen",
      "id": "<user_id>"
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 10
}
```

## PUT Request and Response Example 🔗 
The following is an example of a JSON request body used with a `PUT` method to replace user information, and the response.
**Request:**
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "name": {
    "givenName": "Barbara",
    "familyName": "Jensen"
  },
  "userName": "bjensen@example.com",
  "active": true,
  "emails": [
    {
      "value": "bjensen@example.com",
      "primary": true,
      "type": "home",
      "verified": true
    },
    {
      "value": "bjensen@example.org",
      "type": "work"
    }
  ]
}

```

**Response:**
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "name": {
    "givenName": "Barbara",
    "familyName": "Jensen"
  },
  "userName": "bjensen@example.com",
  "active": true,
  "emails": [
    {
      "value": "bjensen@example.com",
      "primary": true,
      "type": "home",
      "verified": true
    },
    {
      "value": "bjensen@example.org",
      "type": "work"
    }
  ]
}

```

## PATCH Request and Response Example 🔗 
The following is an example of a JSON request body used with a `PATCH` method to amend user information, and the response.
**Request:**
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "phoneNumbers",
      "value": [
        {
          "value": "555-555-1111",
          "type": "home"
        }
      ]
    }
  ]
}
```
**Response:**```
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
          "value": "666-666-1111",
          "type": "home"
        }
      ]
    }
  ]
} 
```

**Note**
  * The `schemas` attribute is set to the schema collection that corresponds with the resource. For example, `urn:ietf:params:scim:schemas:core:2.0:User`, corresponds with `/Users`. See [SCIM Schema Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISSchema.htm#OCISSchema "A schema is a collection of attribute definitions that describe the contents of an entire or partial resource, for example, urn:ietf:params:scim:schemas:core:2.0:User. The attribute definitions specify the name of the attribute, and metadata such as type \(string, binary\), cardinality \(singular, multi, complex\), mutability, and returnability.").
  * The remaining attributes are user attributes to be set.


Was this article helpful?
YesNo

