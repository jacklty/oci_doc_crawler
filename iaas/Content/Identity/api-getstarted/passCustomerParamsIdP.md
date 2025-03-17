Updated 2024-04-02
# Passing Custom Parameters to a Social Identity Provider
Use the identity domains REST API to pass a custom parameter for social identity provider (IdP) configurations. For each social IdP, you can define both static and dynamic custom parameters, which are passed as-is to the IdP when sent in an authorization request.
## Custom Parameter Definition 🔗 
You can define relay parameter mappings by using the social attribute `relayIdpParamMappings`. This parameter stores mapping key-value pairs for a social IdP. A dynamic parameter type maps to an empty or null value. A static parameter type contains a value. 
  * If a key is defined as a static parameter, but passed with a different value, at runtime, the static value defined in the IdP configuration is used.
  * If a relay parameter variable is passed in authorization, and the URL is undefined in the IdP configuration, then this variable is ignored.


```
"relayIdpParamMappings": [
  {
  "relayParamKey": "brand",      //dynamic, since string value is empty
  "relayParamValue": ""
  },
  {
  "relayParamKey": "param1"      //dynamic, since value is null (not defined)
  },
  {
  "relayParamKey": "param2",     //static, since value is defined
  "relayParamValue": "value2"
  }
```

## Example of Relay Parameter Mappings Being Passed to an IdP 🔗 
This authorization URL that's passed to the identity domains REST API: 
```
https://<domainURL>/oauth2/v1/authorize?response_type=id_token&scope=openid&state=1234&nonce=123&client_id=<test_client>&redirect_uri=https://cloud.oracle.com& brand=abc&newParam=blah&param1=test&param2=newValue
```

The redirect from the identity provider becomes:
`<IDPProvider Authorize URI>?client_id=....redirect_uri=....&brand=abc&param1=test&param2=value2`.
The variable `newParam` is ignored because it wasn't defined in the original IdP configuration. The value for `param2` is static and doesn't get changed during runtime authorization. The dynamic parameter `brand` gets a value at runtime, because it was defined initially as a dynamic type during the IdP configuration.
## Create a Social IdP with Relay Parameter Mapping 🔗 
`cURL: POST /admin/v1/SocialIdentityProviders`
**Example Request Body**
```
{
  "registrationEnabled": true,
  "showOnLogin": true,
  "description": "description",
  "serviceProviderName": "Facebook",
  "enabled": true,
  "accountLinkingEnabled": true,
  "name": "test provider custom param",
  "schemas": 
      [
        "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
      ],
  "consumerKey": "clientId12345",
  "consumerSecret": "clientSecret12345",
  "relayIdpParamMappings": [
   {
    "relayParamKey": "brand", 
    "relayParamValue": ""
  },
  {
    "relayParamKey": "param1" 
  },
  {
    "relayParamKey": "param2", 
    "relayParamValue": "value2"
  }
]
}
```

**Example Response Body**
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-03-26T05:09:37.627Z",
    "lastModified": "2024-03-26T05:09:37.627Z",
    "version": "7f3acb03d59644ac956bc1b1a101f08b",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL>/admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:x509:IdentityProvider": {
    "crlEnabled": true
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "partnerName": "test provider custom param",
  "shownOnLoginPage": true,
  "description": "description",
  "ocid": "<domain-ocid>,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Facebook",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientId12345",
  "relayIdpParamMappings": [
    {
      "relayParamKey": "brand"
    },
    {
      "relayParamKey": "param1"
    },
    {
      "relayParamKey": "param2",
      "relayParamValue": "value2"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "test provider custom param",
  "showOnLogin": true
}
```

## Add a Relay Parameter Mapping to an Existing IdP 🔗 
```
cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}
```

**Example Request Body**
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "add",
   "path": "relayIdpParamMappings",
   "value": [
    {
     "relayParamKey": "param3"
    },
    {
     "relayParamKey": "param4",
     "relayParamValue": "value4"
    }
   ]
  }
 ]
}

```

**Example Response Body**
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-03-26T05:09:37.627Z",
    "lastModified": "2024-03-26T05:15:53.551Z",
    "version": "c5e3dd4485904bc98d73aedb1a994a6e",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL>/admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:x509:IdentityProvider": {
    "crlEnabled": true
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "partnerName": "test provider custom param",
  "shownOnLoginPage": true,
  "description": "description",
  "ocid": "<domain-ocid>,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Facebook",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientId12345",
  "relayIdpParamMappings": [
    {
      "relayParamKey": "param3"
    },
    {
      "relayParamKey": "param4",
      "relayParamValue": "value4"
    },
    {
      "relayParamKey": "brand"
    },
    {
      "relayParamKey": "param1"
    },
    {
      "relayParamKey": "param2",
      "relayParamValue": "value2"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "test provider custom param",
  "showOnLogin": true
}

```

## Fetch Relay Parameter Mappings for an Existing IdP 🔗 
`cURL: GET /admin/v1/SocialIdentityProviders/{idpId}?attributes=relayIdpParamMappings`
**Example Request Body** : Not applicable. 
**Example Response Body**
```
{
  "id": "<identity-provider-id>",
  "relayIdpParamMappings": [
    {
      "relayParamKey": "param3"
    },
    {
      "relayParamKey": "param4",
      "relayParamValue": "value4"
    },
    {
      "relayParamKey": "brand"
    },
    {
      "relayParamKey": "param1"
    },
    {
      "relayParamKey": "param2",
      "relayParamValue": "value2"
    }
  ],
  "name": "test provider custom param"
}

```

## Update a Relay Parameter Mapping for an IdP 🔗 
`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`
**Example Request Body**
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "replace",
   "path": "relayIdpParamMappings[relayParamKey eq \"param2\"]",
   "value":[
    {
     "relayParamKey": "param2",
     "relayParamValue": "blah"
    }
   ]
  }
 ]
}

```

**Example Response Body**
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-03-26T05:09:37.627Z",
    "lastModified": "2024-03-26T05:17:16.894Z",
    "version": "cff0f9903fcf47fb9e079477565cc7fa",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL>/admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:x509:IdentityProvider": {
    "crlEnabled": true
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "partnerName": "test provider custom param",
  "shownOnLoginPage": true,
  "description": "description",
  "ocid": "<domain-ocid>,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Facebook",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientId12345",
  "relayIdpParamMappings": [
    {
      "relayParamKey": "param3"
    },
    {
      "relayParamKey": "param4",
      "relayParamValue": "value4"
    },
    {
      "relayParamKey": "brand"
    },
    {
      "relayParamKey": "param1"
    },
    {
      "relayParamKey": "param2",
      "relayParamValue": "blah"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "test provider custom param",
  "showOnLogin": true
}

```

## Delete a Relay Parameter Mapping from an IdP 🔗 
`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`
**Example Request Body**
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "remove",
   "path": "relayIdpParamMappings[relayParamKey eq \"param1\"]"
  }
 ]
}

```

**Example Response Body**
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-03-26T05:09:37.627Z",
    "lastModified": "2024-03-26T05:18:02.914Z",
    "version": "87dd609f85ee4a51905bc7d5071c487d",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL>/admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:x509:IdentityProvider": {
    "crlEnabled": true
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "partnerName": "test provider custom param",
  "shownOnLoginPage": true,
  "description": "description",
  "ocid": "<domain-ocid>,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Facebook",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientId12345",
  "relayIdpParamMappings": [
    {
      "relayParamKey": "param3"
    },
    {
      "relayParamKey": "param4",
      "relayParamValue": "value4"
    },
    {
      "relayParamKey": "brand"
    },
    {
      "relayParamKey": "param2",
      "relayParamValue": "blah"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "test provider custom param",
  "showOnLogin": true
}
```

## Delete All Relay Parameter Mappings from an IdP 🔗 
`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`
**Example Request Body**
```

 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "remove",
   "path": "relayIdpParamMappings"
  }
 ]
}

```

**Example Response Body**
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-03-26T05:09:37.627Z",
    "lastModified": "2024-03-26T05:18:39.488Z",
    "version": "b02a6f8463904f4f8567edf59cf1efd5",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL>/admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:x509:IdentityProvider": {
    "crlEnabled": true
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "partnerName": "test provider custom param",
  "shownOnLoginPage": true,
  "description": "description",
  "ocid": "<domain-ocid>,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Facebook",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientId12345",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "test provider custom param",
  "showOnLogin": true
}

```

Was this article helpful?
YesNo

