Updated 2024-09-16
# Supporting Social JIT Provisioning with Group Membership Support
Use the API to manage new identity domain users with social Just-In-Time (JIT) user provisioning for first-time users.
OCI REST API now supports social JIT Provisioning, to automate user account creation when the user first tries to access identity domains when the user doesn't exist in the identity domain. Social JIT provisioning also supports granting group membership as part of user provisioning.
## Attribute Definitions
  * **socialJitProvisioningEnabled** : You can enable/disable social JIT by controlling this social attribute.
  * **jitProvGroupStaticListEnabled** : When JIT is enabled, you can set this attribute to true to indicate social JIT user provisioning groups should be assigned from a static list.
  * **jitProvAssignedGroups** : This attribute contains a list of groups to be assigned to each social JIT-provisioned user. JIT user-provisioning applies this static list when **jitProvGroupStaticListEnabled** is set to true. 


## Examples
Toggle Social JIT GroupMembership support: `PATCH /admin/v1/SocialIdentityProviders/{idpID} `
Sample request body:```
{
 "Operations": [
  {
   "op": "replace",
   "path": "socialJitProvisioningEnabled",
   "value": true
  },
  {
   "op": "replace",
   "path": "jitProvGroupStaticListEnabled",
   "value": true
  },
  {
    "op": "add",
    "path": "jitProvAssignedGroups",
    "value": [
      {
       "value": “<identitydomain-group-id>”
      }
    ]
  }
 ],
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ]
}

```

Sample response:```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": “<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-04-29T17:26:15.646Z",
    "lastModified": "2024-06-06T22:03:43.284Z",
    "version": "<version number>",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL> /admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/15ae5123456123456aa123456xxx123456"
  },
  "partnerName": "Google",
  "ocid": “<domain-ocid>",
  "socialJitProvisioningEnabled": true,
  "jitProvGroupStaticListEnabled": true,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Google",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientID12345",
  "jitProvAssignedGroups": [
    {
      "value": "<idcs-group-id>",
      "$ref": "https://<domain-id>/admin/v1/Groups/"<idcs-group-id>"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "Google",
  "showOnLogin": true
}

```

Fetch Group Membership for JIT enabled IDP: `GET /admin/v1/SocialIdentityProviders/{idpId}?attributes=jitProvAssignedGroups`
Sample response:```
{
  "id": "<identity-provider-id>",
  "jitProvAssignedGroups": [
    {
      "value": "<idcs-group-id>",
      "$ref": "https://<domain-id>/admin/v1/Groups/"<idcs-group-id>"
    }
  ],
  "name": "Google"
}

```

Remove particular group GUID from JIT enabled IDP membership list: `PATCH /admin/v1/SocialIdentityProviders/{idpId}`
Sample request body:```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "remove",
   "path": "jitProvAssignedGroups[value eq \"<idcs-group-id>\"]"
  }
 ]
}

```

Sample response body:```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": “<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-04-29T17:26:15.646Z",
    "lastModified": "2024-06-06T22:16:47.515Z",
    "version": "<version number>",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL> /admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/15ae5123456123456aa123456xxx123456"
  },
  "partnerName": "Google",
  "ocid": “<domain-ocid>",
  "socialJitProvisioningEnabled": true,
  "jitProvGroupStaticListEnabled": true,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Google",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientID12345",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "Google",
  "showOnLogin": true
}

```

Remove Group Membership list for IDP enabled IDP: `PATCH /admin/v1/SocialIdentityProviders/{idpId}`
Sample request body:```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "remove",
   "path": "jitProvAssignedGroups"
  }
 ]
}

```

Sample response body:```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": “<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "id": "<identity-provider-id>",
  "meta": {
    "created": "2024-04-29T17:26:15.646Z",
    "lastModified": "2024-06-06T22:16:47.515Z",
    "version": "<version number>",
    "resourceType": "IdentityProvider",
    "location": "https://<domainURL> /admin/v1/IdentityProviders/<identity-provider-id>"
  },
  "enabled": true,
  "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/15ae5123456123456aa123456xxx123456"
  },
  "partnerName": "Google",
  "ocid": “<domain-ocid>",
  "socialJitProvisioningEnabled": true,
  "jitProvGroupStaticListEnabled": true,
  "accountLinkingEnabled": true,
  "registrationEnabled": true,
  "serviceProviderName": "Google",
  "consumerSecret": "clientSecret12345",
  "idAttribute": "email",
  "consumerKey": "clientID12345",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SocialIdentityProvider"
  ],
  "name": "Google",
  "showOnLogin": true
}

```

Was this article helpful?
YesNo

