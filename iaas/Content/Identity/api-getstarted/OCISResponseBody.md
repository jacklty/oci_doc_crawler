Updated 2024-04-02
# Response Body
The identity domains REST API requests return a JSON response body. The status code indicates success or failure.
## Supported Response Codes 🔗 
**Note** See [Response Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/StatusCodes.htm#StatusCodes "When you call any of the identity domains REST API resources, the Response header returns one of the standard HTTP status codes.") for more information on the supported response codes.
## Response Body on Success 🔗 
The response format for all REST API requests is a JSON object. The exact contents of the response depends on the contents and type of request, whether the request succeeded or failed, and any query filtering that was performed.
**Note** See the **Examples** tab on each endpoint page for specific response body examples.
## Successful POST Response Body 🔗 
The following is an example response indicating successful creation of a `User` resource with a `POST` request:
```
{
  "idcsCreatedBy": {
    "type": "App",
    "display": "Confidential App",
    "value": "<app-id>",
    "ocid": "<app-ocid>",
    "$ref": "https://<domainURL>/admin/v1/Apps/<app-id>"
  },
  "id": "<user-id>",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
    "isFederatedUser": false
  },
  "meta": {
    "created": "2023-08-29T21:04:25.379Z",
    "lastModified": "2023-08-29T21:04:25.379Z",
    "version": "7fd6be02ffc542809e3ea193d1942df7",
    "resourceType": "User",
    "location": "https://<domainURL>/admin/v1/Users/<user-id>"
  },
  "active": true,
  "displayName": "Clarence Saladna",
  "idcsLastModifiedBy": {
    "value": "<app-id>",
    "display": "Confidential App",
    "ocid": "<app-ocid>",
    "type": "App",
    "$ref": "https://<domainURL>/admin/v1/Apps/<app-id>"
  },
  "name": {
    "givenName": "Clarence",
    "familyName": "Saladna",
    "formatted": "Clarence Saladna"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  "ocid": "<user-ocid>",
  "userName": "csaladna@example.com",
  "emails": [
    {
      "secondary": false,
      "verified": false,
      "type": "recovery",
      "primary": false,
      "value": "csaladna@example.com"
    },
    {
      "secondary": false,
      "verified": false,
      "type": "work",
      "primary": true,
      "value": "csaladna@example.com"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
  ],
  "domainOcid": "<domain-ocid>",
  "compartmentOcid": "<compartment-ocid>",
  "tenancyOcid": "<tenancy-ocid>",
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

## Successful GET Response Body 🔗 
`GET` requests typically return a `ListResponse` object, which might contain multiple records. This example shows the results of a `GET` search on Users, with the query parameter: `filter=userName sw "d"`, that is, users whose usernames begin with `d`.
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 3,
  "Resources": [
    {
      "idcsCreatedBy": {
        "type": "User",
        "display": "dennis@example.com",
        "value": "OCI User",
        "ocid": "<user-ocid>",
        "$ref": "https://<domainURL>/admin/v1/Users/OCI User"
      },
      "id": "<user-id>",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
        "isFederatedUser": false
      },
      "meta": {
        "created": "2023-08-15T20:48:12.736Z",
        "lastModified": "2023-08-15T20:48:12.736Z",
        "version": "087a80ea35614663b05ea69b24b425a7",
        "resourceType": "User",
        "location": "https://<domainURL>/admin/v1/Users/<user-id>"
      },
      "active": true,
      "displayName": "Dean",
      "idcsLastModifiedBy": {
        "value": "OCI User",
        "display": "dean@example.com",
        "ocid": "<user-ocid>",
        "type": "User",
        "$ref": "https://<domainURL>/admin/v1/Users/OCI User"
      },
      "name": {
        "givenName": "Dean",
        "familyName": "",
        "formatted": "Dean"
      },
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
        "locked": {
          "on": false
        }
      },
      "ocid": "<user-ocid>",
      "userName": "dean@example.com",
      "emails": [
        {
          "secondary": false,
          "verified": false,
          "type": "recovery",
          "primary": false,
          "value": "dean@example.com"
        },
        {
          "secondary": false,
          "verified": false,
          "type": "work",
          "primary": true,
          "value": "dean@example.com"
        }
      ],
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
      ],
      "domainOcid": "<domain-ocid>",
      "compartmentOcid": "<compartment-ocid>",
      "tenancyOcid": "<tenancy-ocid>",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:capabilities:User": {
        "canUseApiKeys": true,
        "canUseAuthTokens": true,
        "canUseConsolePassword": true,
        "canUseCustomerSecretKeys": true,
        "canUseOAuth2ClientCredentials": true,
        "canUseSmtpCredentials": true,
        "canUseDbCredentials": true
      }
    },
    {
      "idcsCreatedBy": {
        "type": "User",
        "display": "joel@example.com",
        "value": "OCI User",
        "ocid": "<user-ocid>",
        "$ref": "https://<domainURL>/admin/v1/Users/OCI User"
      },
      "id": "<user-id>",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
        "isFederatedUser": false
      },
      "meta": {
        "created": "2023-07-19T18:23:28.381Z",
        "lastModified": "2023-08-09T16:22:41.590Z",
        "version": "0ecbeddb823247d8a24a67739b006892",
        "resourceType": "User",
        "location": "https://<domainURL>/admin/v1/Users/<user-id>"
      },
      "active": true,
      "displayName": "Dennis",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:mfa:User": {
        "preferredDevice": {
          "value": "<device-id>",
          "$ref": "https://<domainURL>/admin/v1/Devices/<device-id>"
        },
        "loginAttempts": 0,
        "mfaStatus": "ENROLLED",
        "preferredAuthenticationFactor": "PUSH"
      },
      "idcsLastModifiedBy": {
        "value": "<app-id>",
        "display": "idcssso",
        "ocid": "<app-ocid>",
        "type": "App",
        "$ref": "https://<domainURL>/admin/v1/Apps/<app-id>"
      },
      "name": {
        "givenName": "Dennis",
        "familyName": "",
        "formatted": "Dennis"
      },
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
        "locked": {
          "on": false
        }
      },
      "ocid": "<user-ocid>",
      "userName": "dennis@example.com",
      "emails": [
        {
          "secondary": false,
          "verified": true,
          "type": "recovery",
          "primary": false,
          "value": "dennis@example.com"
        },
        {
          "secondary": false,
          "verified": true,
          "type": "work",
          "primary": true,
          "value": "dennis@example.com"
        }
      ],
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:mfa:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
      ],
      "domainOcid": "<domain-ocid>",
      "compartmentOcid": "<compartment-ocid>",
      "tenancyOcid": "<tenancy-ocid>",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:capabilities:User": {
        "canUseApiKeys": true,
        "canUseAuthTokens": true,
        "canUseConsolePassword": true,
        "canUseCustomerSecretKeys": true,
        "canUseOAuth2ClientCredentials": true,
        "canUseSmtpCredentials": true,
        "canUseDbCredentials": true
      }
    },
    {
      "idcsCreatedBy": {
        "type": "User",
        "display": "colin.torretta@oracle.com",
        "value": "OCI User",
        "ocid": "<user-ocid>",
        "$ref": "https://<domainURL>/admin/v1/Users/OCI User"
      },
      "id": "<user-id>",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
        "isFederatedUser": false
      },
      "meta": {
        "created": "2023-08-21T22:36:22.978Z",
        "lastModified": "2023-08-22T03:00:22.934Z",
        "version": "d91908a80bb44ea8bc23e063b42a5e1b",
        "resourceType": "User",
        "location": "https://<domainURL>/admin/v1/Users/<user-id>"
      },
      "active": true,
      "displayName": "Diane",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:mfa:User": {
        "preferredDevice": {
          "value": "<device-id>",
          "$ref": "https://<domainURL>/admin/v1/Devices/<device-id>"
        },
        "mfaStatus": "ENROLLED",
        "preferredAuthenticationFactor": "TOTP"
      },
      "idcsLastModifiedBy": {
        "value": "<app-id>",
        "display": "idcssso",
        "ocid": "<app-ocid>",
        "type": "App",
        "$ref": "https://<domainURL>/admin/v1/Apps/<app-id>"
      },
      "name": {
        "givenName": "Diane",
        "familyName": "",
        "formatted": "Diane"
      },
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
        "locked": {
          "on": false
        }
      },
      "ocid": "<user-ocid>",
      "userName": "diane@example.com",
      "emails": [
        {
          "secondary": false,
          "verified": true,
          "type": "recovery",
          "primary": false,
          "value": "diane@example.com"
        },
        {
          "secondary": false,
          "verified": true,
          "type": "work",
          "primary": true,
          "value": "diane@example.com"
        }
      ],
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:mfa:User",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
      ],
      "domainOcid": "<domain-ocid>",
      "compartmentOcid": "<compartment-ocid>",
      "tenancyOcid": "<tenancy-ocid>",
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
  ],
  "startIndex": 1,
  "itemsPerPage": 50
}
```

## Simple Response Body on Error 🔗 
On error, and on success, the response body is JSON. The format for all identity domains REST API error responses is similar. This example is a simple exception detailing the status code and exception message for an invalid request.
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:Error"
 ],
 "detail": "Request failed: HTTP 400 Bad Request.",
 "status": "400"
}
```

## Validation Exception Response Example 🔗 
This example is a validation exception where some required attributes are missing.
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:Error",
  "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error"
 ],
 "detail": "Missing required attribute(s): mappingAttributeValue,password.",
 "status": "400",
 "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error": {
  "messageId": "error.common.validation.missingReqAttributes"
 }
}
```

## Functional Exception Response Example 🔗 
This example is a functional exception with additional details.
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:Error",
  "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error"
 ],
 "detail": "INVALID_CREDENTIALS",
 "status": "400",
 "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error": {
  "additionalData": {
   "csr": false,
   "tenantName": "TENANT1",
   "id": "<tenancy-id>",
   "displayName": "Jane Smith",
   "locale": "en",
   "preferredLanguage": "en",
   "timezone": "America/Chicago"
  }
 }
}
```

## Dynamic Monitoring Using the ECID and RID HTTP Headers 🔗 
Dynamic monitoring is the mechanism by which HTTP requests can be uniquely identified and thus tracked as they flow through the system.
It also provides a means by which context information can be communicated between cooperating identity domain components involved in fulfilling requests. The Execution Context ID (ECID) and the Relationship ID (RID) are useful in tracking the sequence of events between services.
  * The ECID: A unique identifier. The ECID is unique for each new root task. This number remains the same as it's shared across the tree of tasks associated with the root task.
  * The RID: A relationship identifier. The RID is an ordered set of numbers that describes the location of each task in the tree of tasks. The leading number is typically a zero, and then the numbers increase for each additional subtask.


The `X-ORACLE-DMS-ECID` and the `X-ORACLE-DMS-RID` HTTP headers are returned as part of the REST response from the identity domain. These HTTP headers correspond to the ECID and the RID of the request. The values for these headers are set by the identity domain when returning the response. The caller can use the ECID and the RID to track and correlate requests that originate with events that arise from the identity domain.
For example, the client may include these values as part of an error message, because it's important to correlate events on the client side with errors on the server side. The Oracle standard format for logging involves a field dedicated to the ECID. After the ECID is known, when it's read from an error level log message, for example, it's possible to find all other log messages associated with that task by querying the log files for messages that contain that ECID.
Use the identity domains Diagnostic Data reports to view logging data captured for diagnostic purposes. You can find the ECID and the RID in the report, and then correlate those identifiers to the ECID and the RID that are returned by the identity domains REST calls that your applications make. See [Running the Diagnostic Data Report](https://docs.oracle.com/en-us/iaas/Content/Identity/reports/run-diagnostic.htm#run-diagnostic-report "Run a diagnostic data report for an IAM identity domain.").
### Dynamic Monitoring Examples 🔗 
This section contains examples that show the following:
  * A POST request on the `/Users` endpoint.
  * The cURL command headers that are a result of executing the POST on the `/Users` endpoint.
  * A return response of a GET on the `/AuditEvents` endpoint that shows that the ECID is the same as what was used by the server to create the user.
  * A section of the diagnostic report that was generated when the POST request on the `/Users` endpoint was run.


**POST Request to /Users**
```
curl -X POST -D dumpedHeadersPostUsers.txt
http://<domainURL>/admin/v1/Users
-H 'Authorization: Bearer eyJ4NXQjUzI....poYw'
-H 'Cache-Control: no-cache'
-H 'Content-Type: application/json'
-d '{
  "schemas": [ 
  "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "name": {
 	"givenName": "Clarence",
 	"familyName": "Saladna"
  },
  "userName": "csaladna@example.com",
  "emails": [
 	{
 	 "value": "csaladna@example.com",
 	 "type": "work",
 	 "primary": true
 	},
 	{
 	 "value": "csaladna1@example.com",
 	 "primary": false,
 	 "type": "recovery" 
	}
  ]
 }'
```

**cURL Command Headers in the Response**
```
HTTP/1.1 201 Created
Date: Thu, 04 Jan 2018 12:57:37 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 1227
Proxy-Connection: Keep-Alive
X-ORACLE-DMS-RID: 0
X-ORACLE-DMS-ECID: 0000M31FtLAFo2H6yvR_6G1QJ7Wl0000K
```

**Response to the GET Request to /AuditEvents**
**Note:** This example shows that the ECID is the same as what was used by the server to create the user.
**Request** ```
http://<domainURL>/admin/v1/AuditEvents?filter=actorName sw "adm" and ecId eq "0000M31FtLAFo2H6yvR_6G1QJ7Wl0000K^"
```

**Response**
```
{
 "schemas": [
  "urn:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 1,
 "Resources": [
  {
   "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "<user-id>",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
   },
   "actorName": "admin@oracle.com",
   "id": "2a02fb8bc9a548edb21fe1c80ff6ada0",
   "actorDisplayName": "admin opc",
   "meta": {
    "created": "2024-01-04T12:57:46.314Z",
    "lastModified": "2024-01-04T12:57:46.314Z",
    "resourceType": "AuditEvent",
    "location": "https://<domainURL>/admin/v1/AuditEvents/2a02fb8bc9a548edb21fe1c80ff6ada0"
   },
   "actorId": "<user-id>",
   "adminResourceId": "a06ff8169b3640a29792a15ece75c906",
   "adminResourceName": "csaladna@example.com",
   "timestamp": "2024-01-04T12:57:46.312Z",
   "idcsLastModifiedBy": {
    "value": "<user-id>",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/<user-id>"
   },
   "quotaCount": 0,
   "ecId": "0000M31FtLAFo2H6yvR_6G1QJ7Wl0000K^",
   "rId": "0",
   "eventId": "admin.user.create.success",
   "ssoAuthnLevel": 0,
   "adminResourceType": "User",
   "actorType": "User",
   "serviceName": "Admin",
   "adminValuesAdded": "{\"schemas\":[\"urn:ietf:params:scim:schemas:core:2.0:User\"],\"name\":{\"familyName\":\"Saladna\",\"givenName\":\"Clarence\",\"formatted\":\"Clarence Saladna\"},\"userName\":\"csaladna@example.com\",\"emails\":[{\"value\":\"csaladna@example.com\",\"primary\":\"true\",\"type\":\"work\",\"verified\":\"false\"},{\"value\":\"csaladna@example.com\",\"primary\":\"false\",\"type\":\"recovery\",\"verified\":\"false\"}],\"id\":\"a06ff8169b3640a29792a15ece75c906\",\"displayName\":\"Clarence Saladna\",\"urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User\":{\"status\":\"verified\"},\"active\":\"true\",\"password\":\"*********\",\"urn:ietf:params:scim:schemas:oracle:idcs:extension:passwordState:User\":{\"mustChange\":\"true\",\"lastSuccessfulSetDate\":\"2024-01-04T12:57:37.940Z\",\"cantChange\":\"false\",\"expired\":\"false\",\"passwordHistory\":[{\"sequenceNumber\":\"1\",\"value\":\"*********\"}]},\"urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User\":{\"locked\":{\"on\":\"false\"},\"loginAttempts\":\"0\"},\"meta\":{\"created\":\"2024-01-04T12:57:37.951Z\",\"lastModified\":\"2024-01-04T12:57:37.951Z\"},\"idcsCreatedBy\":{\"value\":\"<user-id>\",\"type\":\"User\",\"display\":\"admin opc\"},\"idcsLastModifiedBy\":{\"value\":\"<user-id>\",\"type\":\"User\",\"display\":\"admin opc\"}}",
   "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuditEvent"
   ]
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 50
}
```

**Diagnostic Report Sample**
![This is a diagnostic report sample.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/DR.png)
Was this article helpful?
YesNo

