Updated 2024-04-02
# Resending Email Verifications When The Email Address Is Already Verified
After a user creates an account in an identity domain using the self-registration process, an email notification is sent to the user to verify the user's email address. After users verify their email addresses, they can no longer verify their email addresses after that.
However, identity domains also allow custom clients to reinitiate the change email flow for the same email address as many times as needed. To support this capability, you must set the `triggerEmailVerificationFlowIfEmailAlreadyVerified` attribute to `true` in the `MeEmailVerifier` request payload.
Use the following steps to trigger the email verification flow, if an email address is already verified:
  * [Step 1: Create a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_e52_wkl_5jb)
  * [Step 2: Get a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_zgz_tll_5jb)
  * [Step 3: Initiate Self-Service Email Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_avt_xml_5jb)
  * [Step 4: Obtain a User Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_cr3_jql_5jb)
  * [Step 5: Self-Verify Email Address](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_nff_drl_5jb)


## Step 1: Create a User 🔗 
This step shows how to create a user by submitting a POST request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
```
  curl
  -X POST
  -H "Content-Type:application/json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Users

```

**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the identity domain URL, and the resource path represents the identity domain API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
**Example of Request Body**
The following shows an example of a request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User"
  ],
  "userName": "bjensen@example.com",
  "password": "{{password}}",
  "name": {
    "familyName": "Jensen",
    "givenName": "Barbara",
    "middleName": "Jane"
  },
  "emails": [
    {
      "value": "bjensen@example.com",
      "type": "work",
      "primary": true
    }
  ]
}
```

**Example of Response Body**
The following shows an example of the response body:
```
{
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "6aa2585abd464991929bcf05ace532e9",
    "$ref": "[https://<domainURL>/admin/v1/Users/6aa2585abd464991929bcf05ace532e9]"
  },
  "id": "ff9a9207fc8c4fd2b3d76af84235e8fd",
  "meta": {
    "created": "2022-03-01T05:19:52.765Z",
    "lastModified": "2022-03-01T05:19:52.765Z",
    "resourceType": "User",
    "location": "[https://<domainURL>/admin/v1/Users/ff9a9207fc8c4fd2b3d76af84235e8fd]"
  },
  "active": true,
  "displayName": "Barbara Jensen",
  "idcsLastModifiedBy": {
    "value": "6aa2585abd464991929bcf05ace532e9",
    "display": "admin opc",
    "type": "User",
    "$ref": "[https://<domainURL>/admin/v1/Users/6aa2585abd464991929bcf05ace532e9]"
  },
  "userName": "bjensen2",
  "emails": [
    {
      "verified": false,
      "primary": false,
      "secondary": false,
      "value": "[bjensen@example.com|mailto:bjensen@example.com]",
      "type": "recovery"
    },
    {
      "verified": false,
      "primary": true,
      "secondary": false,
      "value": "[bjensen@example.com|mailto:bjensen@example.com]",
      "type": "work"
    }
  ],
  "urn:ietf:params:scim:schemas:example:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  "name": {
    "familyName": "Jensen",
    "givenName": "Barbara",
    "formatted": "Barbara Jane Jensen",
    "middleName": "Jane"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:example:idcs:extension:userState:User"
  ]
}
```

## Step 2: Get a User 🔗 
This step shows how to retrieve a user by the user's ID by submitting a GET request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
```
  curl
  -X GET
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Users/<user_ocid or user_id>
```

**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
**Example of Response Body**
The following example shows the contents of the response body in JSON format:
```
{
  "displayName": "Barbara Jensen",
  "name": {
    "givenName": "Barbara",
    "formatted": "Barbara Jane Jensen",
    "middleName": "Jane",
    "familyName": "Jensen"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  "userName": "bjensen@example.com",
  "id": "ff9a9207fc8c4fd2b3d76af84235e8fd",
  "active": true,
  "emails": [
    {
      "verified": "false",
      "value": "bjensen@example.com",
      "type": "recovery"
    },
    {
      "primary": true,
      "value": "bjensen@example.com",
      "type": "work"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "meta": {
    "resourceType": "User",
    "created": "2022-07-13T07:28:59.227Z",
    "lastModified": "2022-07-13T07:28:59.227Z",
    "location": "http://<domainURL>/admin/v1/Users/ff9a9207fc8c4fd2b3d76af84235e8fd"
  },
  "idcsCreatedBy": {
    "value": "f8fa30db0f5f41f98de00bc07c05a73d",
    "$ref": "/OAuthClients/f8fa30db0f5f41f98de00bc07c05a73d",
    "type": "OAuthClient",
    "display": "admin"
  },
  "idcsLastModifiedBy": {
    "value": "f8fa30db0f5f41f98de00bc07c05a73d",
    "$ref": "/OAuthClients/f8fa30db0f5f41f98de00bc07c05a73d",
    "type": "OAuthClient",
    "display": "admin"
  }
}
```

## Step 3: Initiate Self-Service Email Verification 🔗 
This step shows how to initiate email validation of either the user's primary or recovery email address by submitting a PUT request on the REST resource using cURL. For more information about cURL, see [Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
```
  curl
  -X PUT
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/MeEmailVerifier
```

**Example of Request Body**
The following shows an example of a request body in JSON format:
```
{
  "email": "bjensen@example.com",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:MeEmailVerifier"
  ],
  "id": "ff9a9207fc8c4fd2b3d76af84235e8fd",
  "userFlowControlledByExternalClient": true,
  "triggerEmailVerificationFlowIfEmailAlreadyVerified": true
}
```

**Example of Response Body**
The following example shows the contents of the response body in JSON format:
```
{
  "email": "bjensen@example.com",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:MeEmailVerifier"
  ],
  "id": "ff9a9207fc8c4fd2b3d76af84235e8fd",
  "userFlowControlledByExternalClient": true,
  "triggerEmailVerificationFlowIfEmailAlreadyVerified": true,
  "meta": {
    "resourceType": "MeEmailVerifier",
    "location": "https://<domainURL>/admin/v1/MeEmailVerifier/57044ca14d274d789a586e5ec77c26f3"
  },
  "userToken": {
    "value": "db21a3578d27439ca9fab6349be46c30",
    "$ref": "https://<domainURL>/admin/v1/UserTokens/db21a3578d27439ca9fab6349be46c30"
  }
}
```

## Step 4: Obtain a User Token 🔗 
This step shows how to retrieve a user token using its ID by submitting a GET request on the REST resource using cURL. For more information about cURL, see [Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
```
  curl
-X GET
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/UserTokens/{{usertokenid}}
```

**Example of Response Body**
The following example shows the contents of the response body in JSON format:
```
{
  "expiryTime": "2022-07-13T07:28:59.227Z",
  "token": "KtXTrZkyIC2OWYVChbYEtfWnE7zhxlYJ0roEvsj0F2I=",
  "tokenType": "email",
  "userId": "5a7550ad5cfa4f50bdc608da1831481b",
  "data": "bjensen@example.com",
  "eventId": "admin.user.password.reset.success",
  "status": 0,
  "id": "3e4b69e99ddf472989e089a904a3c1a7",
  "meta": {
    "created": "2022-07-13T07:28:59.227Z",
    "lastModified": "2022-07-13T07:28:59.227Z",
    "resourceType": "UserToken",
    "location": "$baseUri/UserTokens/{id}"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:UserToken"
  ],
  "idcsCreatedBy": {
    "value": "14171fc6031a417cac680cdb9d82c2ea",
    "display": "admin",
    "type": "OAuthClient",
    "$ref": "$baseUri/OAuthClient/{id}"
  },
  "idcsLastModifiedBy": {
    "value": "14171fc6031a417cac680cdb9d82c2ea",
    "display": "admin",
    "type": "OAuthClient",
    "$ref": "$baseUri/OAuthClient/{id}"
  }
}
```

## Step 5: Self-Verify Email Address 🔗 
This step shows how to verify a new email address by submitting a POST request on the REST resource using cURL. This endpoint validates the token, and then marks the email address as verified. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
```
  curl
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/MeEmailVerified
```

**Example of Request Body**
The following shows an example of a request body in JSON format:
```
{
 "token": "YzQwYTc4NmE5YmEzNGU4MDg0YjFkY2FhZWRmNThlOTc6TEFGaWtuTXI5OjIwMTUtMDctMjRUMDI6Mjk6NDEuNzEwWg==",
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:MeEmailVerified"
 ]
}
```

**Example of Response Body**
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:MeEmailVerified"
  ],
  "id": "5fed0efce51f40b4a42b0773a65178c3",
  "meta": {
    "resourceType": "MeEmailVerified",
    "location": "https://<domainURL>/admin/v1/MeEmailVerified/57044ca14d274d789a586e5ec77c26f3"
  }
}
```

Was this article helpful?
YesNo

