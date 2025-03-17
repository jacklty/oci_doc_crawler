Updated 2024-04-02
# Creating an Enterprise Application with Authorization Policy
These use cases provide example requests to create an enterprise application with an authorization policy using the identity domains REST API.
The following use cases walk you through the steps to create an enterprise application with authorization policy using the REST APIs:
  * [Create an Enterprise Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_n2y_xzw_mjb)
  * [Create an App Resource](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ahr_wjx_mjb)
  * [Update the App Resource ID Reference in an Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gbt_qmx_mjb)
  * [Add Web Tier Policy to an Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_t5w_ppx_mjb)
  * [Creating an Enterprise Application with Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_mb4_rhz_mjb "These use cases provide example requests to create an enterprise application with an authorization policy using the identity domains REST API.")
  * [Create Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ol4_4th_njb "These use cases provide example requests to create the deny authorization policy for an enterprise application using the identity domains REST API.")


## Create an Enterprise Application 🔗 
The following example shows how to create an enterprise application by submitting a POST request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Apps
```

**Note** Template id should map to the Enterprise app template.
### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:samlServiceProvider:App",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:requestable:App",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App"
  ],
  "displayName": "Enterprise App",
  "description": "Enterprise Application",
  "landingPageURL": "http://google.com",
  "basedOnTemplate": {
    "value": "CustomEnterpriseAppTemplateId"
  },
  "isSamlServiceProvider": false,
  "isOAuthResource": false,
  "isOAuthClient": false,
  "showInMyApps": false,
  "isWebTierPolicy": false,
  "isEnterpriseApp": true,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:requestable:App": {
    "requestable": false
  }
}
```

### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "isAliasApp": false,
  "meta": {
    "created": "2022-01-07T17:30:36.385Z",
    "lastModified": "2022-01-07T17:30:36.385Z",
    "resourceType": "App",
    "location": "https://<domainURL>/admin/v1/Apps/69130ad799814b3a82d2cd3b19aba7ce"
  },
  "active": false,
  "isLoginTarget": false,
  "idcsCreatedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "64c266200ba04b1bb1591482f8fd204f",
    "$ref": "https://<domainURL>/admin/v1/Users/64c266200ba04b1bb1591482f8fd204f"
  },
  "displayName": "Enterprise App",
  "showInMyApps": false,
  "isMobileTarget": false,
  "allowOffline": false,
  "isUnmanagedApp": false,
  "idcsLastModifiedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "64c266200ba04b1bb1591482f8fd204f",
    "$ref": "https://<domainURL>/admin/v1/Users/64c266200ba04b1bb1591482f8fd204f"
  },
  "isOPCService": false,
  "description": "Enterprise Application",
  "isOAuthClient": false,
  "isManagedApp": true,
  "isEnterpriseApp": true,
  "isSamlServiceProvider": false,
  "infrastructure": false,
  "allUrlSchemesAllowed": false,
  "id": "69130ad799814b3a82d2cd3b19aba7ce",
  "landingPageUrl": "http://google.com",
  "isWebTierPolicy": false,
  "loginMechanism": "OIDC",
  "allowAccessControl": false,
  "isOAuthResource": false,
  "migrated": false,
  "isKerberosRealm": false,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App": {
    "flatFileBundleConfigurationProperties": [
      {
        "required": true,
        "helpMessage": "Enter the character that specifies the boundary between separate, independent fields in the flat file.",
        "confidential": false,
        "displayName": "Field Delimiter",
        "name": "fieldDelimiter",
        "icfType": "String",
        "value": [
          ","
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the character that specifies the boundary between sub-fields in the flat file. As an example, if Address is a field, then Street Address, City, State, and Zip Code can be designated as sub-fields of the Address field.",
        "confidential": false,
        "displayName": "Sub-Field Delimiter",
        "name": "subFieldDelimiter",
        "icfType": "String"
      },
      {
        "required": true,
        "helpMessage": "Enter the attribute name that represents the unique identifier (UID) for each record in the flat file.",
        "confidential": false,
        "displayName": "UID",
        "name": "uidAttribute",
        "icfType": "String",
        "value": [
          "ID"
        ]
      },
      {
        "required": true,
        "helpMessage": "Enter the attribute name that represents the user-friendly name for each record in the flat file.",
        "confidential": false,
        "displayName": "Name",
        "name": "nameAttribute",
        "icfType": "String",
        "value": [
          "NAME"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the attribute name that represents the status for each record in the flat file.",
        "confidential": false,
        "displayName": "Status",
        "name": "statusAttribute",
        "icfType": "String",
        "value": [
          "ACTIVE"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the value for the Status attribute that represents the Active or Enabled status for each record in the flat file.",
        "confidential": false,
        "displayName": "Active",
        "name": "statusEnabledValue",
        "icfType": "String",
        "value": [
          "true"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the value for the Status attribute that represents the Inactive or Disabled status for each record in the flat file.",
        "confidential": false,
        "displayName": "Inactive",
        "name": "statusDisabledValue",
        "icfType": "String",
        "value": [
          "false"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the fully qualified name (including the package name) of the post-process class. If you haven't implemented a post-process task, then skip this field.",
        "confidential": false,
        "displayName": "Post-Process Task Class Name",
        "name": "postProcessClassName",
        "icfType": "String"
      },
      {
        "required": false,
        "helpMessage": "Enter a number that represents how many records in the flat file will be processed before the progress will be logged.",
        "confidential": false,
        "displayName": "Progress Checkpoint",
        "name": "progressCheckPoint",
        "icfType": "Integer",
        "value": [
          "100"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the fully qualified name (including the package name) of the parser class. If you haven't implemented a custom parser, then skip this field.",
        "confidential": false,
        "displayName": "Parser Class Name",
        "name": "parserClassName",
        "icfType": "String",
        "value": [
          "org.identityconnectors.flatfile.csv.CSVParser"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the configuration parameters for your parser class in the following format: param1=value1;param2=value2 ;... and so on. If you haven't implemented a custom parser, then skip this field.",
        "confidential": false,
        "displayName": "Custom Configuration Parameters",
        "name": "customConfigParams",
        "icfType": "String"
      },
      {
        "required": false,
        "helpMessage": "Enter the fully qualified name (including the package name) of the pre-process class. If you haven't implemented a pre-process task, then skip this field.",
        "confidential": false,
        "displayName": "Pre-Process Task Class Name",
        "name": "preProcessClassName",
        "icfType": "String"
      },
      {
        "required": true,
        "helpMessage": "Select the flat file that you want to import.",
        "confidential": false,
        "displayName": "Flat File",
        "name": "flatFile",
        "icfType": "File"
      },
      {
        "required": false,
        "helpMessage": "Provide the encoding format of the flat file that you're importing. Refer to the Java API documentation for the Charset class for valid encoding formats.",
        "confidential": false,
        "displayName": "Encoding Format",
        "name": "encoding",
        "icfType": "String",
        "value": [
          "UTF-8"
        ]
      },
      {
        "required": false,
        "helpMessage": "Enter the character that represents the comment syntax for the flat file. The lines in the flat file starting with this character will be inert and will be ignored during parsing.",
        "confidential": false,
        "displayName": "Comment Syntax",
        "name": "commentCharacter",
        "icfType": "Character"
      },
      {
        "required": false,
        "helpMessage": "Enter the character that specifies the boundary between multiple values of a single field in the flat file. As an example, if Email is a field, then you can have multiple email addresses as values for that field.",
        "confidential": false,
        "displayName": "Multi-Value Field Delimiter",
        "name": "multiValueDelimiter",
        "icfType": "String"
      },
      {
        "required": false,
        "helpMessage": "Enter the character that marks special text in the flat file. Any text that starts and ends with this character won't be processed or won't be split further using delimiters.",
        "confidential": false,
        "displayName": "Special Text Character",
        "name": "textQualifier",
        "icfType": "Character"
      }
    ],
    "flatFileConnectorBundle": {
      "wellKnownId": "FlatFileConnectorBundleId",
      "value": "FlatFileConnectorBundleId",
      "$ref": "https://<domainURL>/admin/v1/ConnectorBundles/FlatFileConnectorBundleId"
    },
    "isAuthoritative": false,
    "accountFormVisible": false,
    "isThreeLeggedOAuthEnabled": false,
    "connected": false,
    "bundleConfigurationProperties": [
      {
        "icfType": "String",
        "displayName": "host",
        "required": false,
        "helpMessage": "host",
        "confidential": false,
        "name": "host"
      }
    ],
    "objectClasses": [
      {
        "value": "997f5dc686124e069489f2f4d111253c",
        "type": "AccountObjectClass",
        "isAccountObjectClass": true,
        "display": "__ACCOUNT__",
        "resourceType": "ManagedApp997f5dc686124e069489f2f4d111253c",
        "$ref": "https://<domainURL>/admin/v1/AccountObjectClasses/997f5dc686124e069489f2f4d111253c"
      }
    ],
    "connectorBundle": {
      "wellKnownId": "NoOperationConnectorBundleId",
      "value": "NoOperationConnectorBundleId",
      "$ref": "https://<domainURL>/admin/v1/ConnectorBundles/NoOperationConnectorBundleId"
    }
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App": {
    "allowAuthzPolicy": {
      "value": "5b246375d1774feb87e5c1be39b48c0f",
      "$ref": "https://<domainURL>/admin/v1/Policies/5b246375d1774feb87e5c1be39b48c0f"
    },
    "denyAuthzPolicy": {
      "value": "9ca3adcc0be7497cb1ea5395f368a505",
      "$ref": "https://<domainURL>/admin/v1/Policies/9ca3adcc0be7497cb1ea5395f368a505"
    }
  },
  "attrRenderingMetadata": [
    {
      "name": "aliasApps",
      "visible": false
    }
  ],
  "basedOnTemplate": {
    "value": "CustomEnterpriseAppTemplateId",
    "wellKnownId": "CustomEnterpriseAppTemplateId",
    "lastModified": "2022-01-07T10:16:49Z",
    "$ref": "https://<domainURL>/admin/v1/AppTemplates/CustomEnterpriseAppTemplateId"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App"
  ]
}
```

## Create an App Resource 🔗 
The following example shows how to create an app resource by submitting a POST request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>" https://<domainURL>/admin/v1/AppResources
```

**Note** Replace the `{{appid}}` placeholder with the app id from the app creation response.
### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AppResource"
  ],
  "name": "My Resource",
  "resourceURL": "http://google.com",
  "isRegex": false,
  "description": "My resource url content",
  "app": {
    "value": "{{appid}}"
  }
}
```

### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "description": "My resource url content",
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "resourceURL": "http://google.com",
  "id": "64eb6207fbdd45b3807f857c69b52bc9",
  "isRegex": false,
  "meta": {
    "created": "2022-10-21T12:12:30.130Z",
    "lastModified": "2022-10-21T12:12:30.130Z",
    "resourceType": "AppResource",
    "location": "https://<domainURL>/admin/v1/AppResources/64eb6207fbdd45b3807f857c69b52bc9"
  },
  "name": "My Resource",
  "app": {
    "value": "23b7bf0f79854002b2db81b808e6a54b",
    "display": "Enterprise App",
    "$ref": "https://<domainURL>/admin/v1/Apps/23b7bf0f79854002b2db81b808e6a54b"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AppResource"
  ]
}
```

## Update the App Resource ID Reference in an Enterprise App 🔗 
The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>" https://<domainURL>/admin/v1/Apps/<ID>
```

### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations":[ 
   { 
     "op":"replace",
     "path":"urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App:appResources",
     "value":[ 
      { 
        "value":"f3b3d95cd43049468f82b6e596747a5e"
      }
     ]
   }
  ]
}
```

### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{ 
  "isAliasApp":false,
  "meta":{ 
   "created":"2022-01-08T07:18:52.803Z",
   "lastModified":"2022-01-08T11:13:54.645Z",
   "resourceType":"App",
   "location":"https://<domainURL>/admin/v1/Apps/ef246fab9d9f4e6185190af186baeb3a"
  },
  "active":false,
  "isLoginTarget":false,
  "idcsCreatedBy":{ 
   "display":"admin opc",
   "type":"User",
   "value":"64c266200ba04b1bb1591482f8fd204f",
   "$ref":"https://<domainURL>/admin/v1/Users/64c266200ba04b1bb1591482f8fd204f"
  },
  "displayName":"Enterprise App",
  "showInMyApps":false,
  "isMobileTarget":false,
  "allowOffline":false,
  "isUnmanagedApp":false,
  "idcsLastModifiedBy":{ 
   "display":"admin opc",
   "type":"User",
   "value":"64c266200ba04b1bb1591482f8fd204f",
   "$ref":"https://<domainURL>/admin/v1/Users/64c266200ba04b1bb1591482f8fd204f"
  },
  "isOPCService":false,
  "isOAuthClient":false,
  "isManagedApp":true,
  "isEnterpriseApp":true,
  "isSamlServiceProvider":false,
  "infrastructure":false,
  "allUrlSchemesAllowed":false,
  "id":"ef246fab9d9f4e6185190af186baeb3a",
  "isWebTierPolicy":false,
  "loginMechanism":"OIDC",
  "allowAccessControl":false,
  "isOAuthResource":false,
  "migrated":false,
  "isKerberosRealm":false,
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App":{ 
   "connectorBundle":{ 
     "wellKnownId":"NoOperationConnectorBundleId",
     "value":"NoOperationConnectorBundleId",
     "$ref":"https://<domainURL>/admin/v1/ConnectorBundles/NoOperationConnectorBundleId"
   },
   "flatFileBundleConfigurationProperties":[ 
     { 
      "required":false,
      "helpMessage":"Enter the character that specifies the boundary between sub-fields in the flat file. As an example, if Address is a field, then Street Address, City, State, and Zip Code can be designated as sub-fields of the Address field.",
      "confidential":false,
      "displayName":"Sub-Field Delimiter",
      "name":"subFieldDelimiter",
      "icfType":"String"
     },
     { 
      "required":true,
      "helpMessage":"Enter the attribute name that represents the unique identifier (UID) for each record in the flat file.",
      "confidential":false,
      "displayName":"UID",
      "name":"uidAttribute",
      "icfType":"String",
      "value":[ 
        "ID"
      ]
     },
     { 
      "required":true,
      "helpMessage":"Enter the attribute name that represents the user-friendly name for each record in the flat file.",
      "confidential":false,
      "displayName":"Name",
      "name":"nameAttribute",
      "icfType":"String",
      "value":[ 
        "NAME"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Provide the encoding format of the flat file that you're importing. Refer to the Java API documentation for the Charset class for valid encoding formats.",
      "confidential":false,
      "displayName":"Encoding Format",
      "name":"encoding",
      "icfType":"String",
      "value":[ 
        "UTF-8"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the configuration parameters for your parser class in the following format: param1=value1;param2=value2 ;... and so on. If you haven't implemented a custom parser, then skip this field.",
      "confidential":false,
      "displayName":"Custom Configuration Parameters",
      "name":"customConfigParams",
      "icfType":"String"
     },
     { 
      "required":false,
      "helpMessage":"Enter the fully qualified name (including the package name) of the pre-process class. If you haven't implemented a pre-process task, then skip this field.",
      "confidential":false,
      "displayName":"Pre-Process Task Class Name",
      "name":"preProcessClassName",
      "icfType":"String"
     },
     { 
      "required":true,
      "helpMessage":"Select the flat file that you want to import.",
      "confidential":false,
      "displayName":"Flat File",
      "name":"flatFile",
      "icfType":"File"
     },
     { 
      "required":false,
      "helpMessage":"Enter the character that represents the comment syntax for the flat file. The lines in the flat file starting with this character will be inert and will be ignored during parsing.",
      "confidential":false,
      "displayName":"Comment Syntax",
      "name":"commentCharacter",
      "icfType":"Character"
     },
     { 
      "required":false,
      "helpMessage":"Enter the character that specifies the boundary between multiple values of a single field in the flat file. As an example, if Email is a field, then you can have multiple email addresses as values for that field.",
      "confidential":false,
      "displayName":"Multi-Value Field Delimiter",
      "name":"multiValueDelimiter",
      "icfType":"String"
     },
     { 
      "required":false,
      "helpMessage":"Enter the character that marks special text in the flat file. Any text that starts and ends with this character won't be processed or won't be split further using delimiters.",
      "confidential":false,
      "displayName":"Special Text Character",
      "name":"textQualifier",
      "icfType":"Character"
     },
     { 
      "required":true,
      "helpMessage":"Enter the character that specifies the boundary between separate, independent fields in the flat file.",
      "confidential":false,
      "displayName":"Field Delimiter",
      "name":"fieldDelimiter",
      "icfType":"String",
      "value":[ 
        ","
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the value for the Status attribute that represents the Active or Enabled status for each record in the flat file.",
      "confidential":false,
      "displayName":"Active",
      "name":"statusEnabledValue",
      "icfType":"String",
      "value":[ 
        "true"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the attribute name that represents the status for each record in the flat file.",
      "confidential":false,
      "displayName":"Status",
      "name":"statusAttribute",
      "icfType":"String",
      "value":[ 
        "ACTIVE"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the value for the Status attribute that represents the Inactive or Disabled status for each record in the flat file.",
      "confidential":false,
      "displayName":"Inactive",
      "name":"statusDisabledValue",
      "icfType":"String",
      "value":[ 
        "false"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the fully qualified name (including the package name) of the post-process class. If you haven't implemented a post-process task, then skip this field.",
      "confidential":false,
      "displayName":"Post-Process Task Class Name",
      "name":"postProcessClassName",
      "icfType":"String"
     },
     { 
      "required":false,
      "helpMessage":"Enter a number that represents how many records in the flat file will be processed before the progress will be logged.",
      "confidential":false,
      "displayName":"Progress Checkpoint",
      "name":"progressCheckPoint",
      "icfType":"Integer",
      "value":[ 
        "100"
      ]
     },
     { 
      "required":false,
      "helpMessage":"Enter the fully qualified name (including the package name) of the parser class. If you haven't implemented a custom parser, then skip this field.",
      "confidential":false,
      "displayName":"Parser Class Name",
      "name":"parserClassName",
      "icfType":"String",
      "value":[ 
        "org.identityconnectors.flatfile.csv.CSVParser"
      ]
     }
   ],
   "isAuthoritative":false,
   "accountFormVisible":false,
   "isThreeLeggedOAuthEnabled":false,
   "connected":false,
   "bundleConfigurationProperties":[ 
     { 
      "icfType":"String",
      "displayName":"host",
      "required":false,
      "helpMessage":"host",
      "confidential":false,
      "name":"host"
     }
   ],
   "objectClasses":[ 
     { 
      "value":"05cf9ba4b2bd4ff9bb10ce134a821c33",
      "type":"AccountObjectClass",
      "isAccountObjectClass":true,
      "display":"__ACCOUNT__",
      "resourceType":"ManagedApp05cf9ba4b2bd4ff9bb10ce134a821c33",
      "$ref":"https://<domainURL>/admin/v1/AccountObjectClasses/05cf9ba4b2bd4ff9bb10ce134a821c33"
     }
   ],
   "flatFileConnectorBundle":{ 
     "wellKnownId":"FlatFileConnectorBundleId",
     "value":"FlatFileConnectorBundleId",
     "$ref":"https://<domainURL>/admin/v1/ConnectorBundles/FlatFileConnectorBundleId"
   }
  },
  "basedOnTemplate":{ 
   "value":"CustomEnterpriseAppTemplateId",
   "wellKnownId":"CustomEnterpriseAppTemplateId",
   "lastModified":"2022-01-07T10:16:49Z",
   "$ref":"https://<domainURL>/admin/v1/AppTemplates/CustomEnterpriseAppTemplateId"
  },
  "attrRenderingMetadata":[ 
   { 
     "name":"aliasApps",
     "visible":false
   }
  ],
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App":{ 
   "denyAuthzPolicy":{ 
     "value":"a5a367a2e5794b2ab00a75100c23e79f",
     "$ref":"https://<domainURL>/admin/v1/Policies/a5a367a2e5794b2ab00a75100c23e79f"
   },
   "allowAuthzPolicy":{ 
     "value":"37ac22197b2f418c85cb6c8a22507f1e",
     "$ref":"https://<domainURL>/admin/v1/Policies/37ac22197b2f418c85cb6c8a22507f1e"
   },
   "appResources":[ 
     { 
      "value":"f3b3d95cd43049468f82b6e596747a5e",
      "$ref":"https://<domainURL>/admin/v1/AppResources/f3b3d95cd43049468f82b6e596747a5e"
     }
   ]
  },
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:App",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App"
  ]
}
```

## Add Web Tier Policy to an Enterprise App 🔗 
The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Apps/<ID>?attributes=urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:webTierPolicyJson,urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:webTierPolicyAZControl,urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:resourceRef
```

### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations":[ 
   { 
     "op":"replace",
     "path":"isWebTierPolicy",
     "value":true
   },
   { 
     "op":"add",
     "path":"urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:webTierPolicyAZControl",
     "value":"server"
   },
   { 
     "op":"add",
     "path":"urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:webTierPolicyJson",
     "value":"{\"cloudgatePolicy\":{\"version\":\"2.6\",\"requireSecureCookies\":true,\"allowCors\":true,\"disableAuthorize\":true,\"webtierPolicy\":[{\"policyName\":\"WebtierTest policy\",\"comment\":\"Webtier policy\",\"resourceFilters\":[{\"filter\":\"<app resource id>\",\"comment\":\"\",\"type\":\"resource\",\"method\":\"http\"}]}]}}"
   }
  ]
}
```

### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{ 
  "isAliasApp":false,
  "displayName":"Enterprise App",
  "id":"13f13b9893134eda987957a271eab748",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App":{ 
   "webTierPolicyJson":"{\"cloudgatePolicy\":{\"allowCors\":true,\"requireSecureCookies\":true,\"webtierPolicy\":[{\"resourceFilters\":[{\"filter\":\"http://google.com\",\"method\":\"http\",\"resourceRefId\":\"83043a729d1040868aad6e0e93519cb4\",\"comment\":\"\",\"resourceRefName\":\"My Resource\",\"type\":\"text\"}],\"policyName\":\"WebtierTest policy\",\"comment\":\"Webtier policy\"}],\"version\":\"2.6\",\"disableAuthorize\":true}}",
   "webTierPolicyAZControl":"server"
  },
  "basedOnTemplate":{ 
   "value":"CustomEnterpriseAppTemplateId"
  }
}
```

## Create Allow Authorization Policy 🔗 
These use cases provide example requests to create the allow authorization policy for an enterprise application using the identity domains REST API.
The following use cases walk you through the steps to create the allow authorization policy for an enterprise application using the identity domains REST API:
  * [Add Allow Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_zdy_w5y_mjb)
  * [Create Allow Authorization Policy Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_pkk_xwy_mjb)
  * [Create Allow Authorization Policy Condition Group](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_xx4_lcz_mjb)
  * [Create Allow Authorization Policy Rule](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ljj_ndz_mjb)
  * [Update Allow Authorization Policy Rule Reference](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gqx_l2z_mjb)
  * [Update App Resource Reference for Allow Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gqs_hfz_mjb)


### Add Allow Authorization Policy 🔗 
The Allow Authorization Policy is automatically added while creating an enterprise application.
The created policy ID is available in the response as follows:
```
"urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App": {
  "allowAuthzPolicy": {
    "value": "1680009a68d947fc94e817102300e362",
    "$ref": "https://<domainURL>/admin/v1/Policies/1680009a68d947fc94e817102300e362"
  },
  "denyAuthzPolicy": {
    "value": "8f91bf044dd34415936a035434bd766c",
    "$ref": "https://<domainURL>/admin/v1/Policies/8f91bf044dd34415936a035434bd766c"
  }
}
```

### Create Allow Authorization Policy Conditions 🔗 
The following example shows how to create a condition to be evaluated by submitting a POST request on the REST resource using cURL. Conditions are referenced from Condition Groups. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Conditions
```

#### Example of Request Body - Group Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"isInTheseGroups",
  "attributeName":"user.groups[*].value",
  "operator":"coany",
  "attributeValue":"[\"<group guid>\"]"
}
```

#### Example of Response Body - Group Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "isInTheseGroups",
  "attributeName": "user.groups[*].value",
  "operator": "coany",
  "attributeValue": "[\"6d89b1f9b5b84753926b3aedbf71c289\"]",
  "id": "c25d88b87320467da4467b2a12168cec",
  "meta": {
    "created": "2022-10-21T15:24:08.007Z",
    "lastModified": "2022-10-21T15:24:08.007Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/c25d88b87320467da4467b2a12168cec"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - User Not in Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"isNotInTheseUsers",
  "attributeName":"user.userName",
  "operator":"nin",
  "attributeValue":"[\"<user name>\"]"
}
```

#### Example of Response Body - User Not in Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "isNotInTheseUsers",
  "attributeName": "user.userName",
  "operator": "nin",
  "attributeValue": "[\"bf11562fd0dd4fda85fde3690b104dd3\"]",
  "id": "16a2cd31f0114adc856fadb06a18648c",
  "meta": {
    "created": "2022-10-21T15:25:17.519Z",
    "lastModified": "2022-10-21T15:25:17.519Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/16a2cd31f0114adc856fadb06a18648c"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - Administrator Role Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"idcsAdminRole",
  "attributeName":"user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:appRoles[*].adminRole",
  "operator":"co",
  "attributeValue":"[\"true\"]"
}
```

#### Example of Response Body - Administrator Role Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "idcsAdminRole",
  "attributeName": "user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:appRoles[*].adminRole",
  "operator": "co",
  "attributeValue": "[\"true\"]",
  "id": "e742c4b2a391451da6dfc42dfd8a4c7d",
  "meta": {
    "created": "2022-10-21T15:25:39.399Z",
    "lastModified": "2022-10-21T15:25:39.399Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/e742c4b2a391451da6dfc42dfd8a4c7d"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - Network Perimeter Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"SubjectIPAddress",
  "attributeName":"subject.ip",
  "operator":"eq",
  "attributeValue":"#inIPRange(\"<Network perimeter id>\")"
}
```

#### Example of Response Body - Network Perimeter Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "SubjectIPAddress",
  "attributeName": "subject.ip",
  "operator": "eq",
  "attributeValue": "#inIPRange(\"83bad53f0a50454d909a4709d1335e0d\")",
  "id": "4d7afc63249943a3b6136876f30f7860",
  "meta": {
    "created": "2022-10-21T15:27:45.819Z",
    "lastModified": "2022-10-21T15:27:45.819Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/4d7afc63249943a3b6136876f30f7860"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

### Create Allow Authorization Policy Condition Group 🔗 
The following example shows how to create a condition group to be evaluated by submitting a POST request on the REST resource using cURL. Condition groups are referenced from a Rule. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/ConditionGroups
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "name":"ConditionGroup",
  "operator":"and",
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:ConditionGroup"
  ],
  "conditions":[ 
   { 
     "value":"<group condition id>",
     "type":"Condition"
   },
   { 
     "value":"<user condition id>",
     "type":"Condition"
   },
   { 
     "value":"<admin role condition id>",
     "type":"Condition"
   },
   { 
     "value":"<network perimeter condition id>",
     "type":"Condition"
   }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "operator": "and",
  "id": "d073eb1df00f4b388fbb06430b70173e",
  "meta": {
    "created": "2022-10-21T15:29:51.218Z",
    "lastModified": "2022-10-21T15:29:51.218Z",
    "resourceType": "ConditionGroup",
    "location": "https://<domainURL>/admin/v1/ConditionGroups/d073eb1df00f4b388fbb06430b70173e"
  },
  "name": "ConditionGroup",
  "conditions": [
    {
      "type": "Condition",
      "value": "c25d88b87320467da4467b2a12168cec",
      "$ref": "https://<domainURL>/admin/v1/Conditions/c25d88b87320467da4467b2a12168cec"
    },
    {
      "type": "Condition",
      "value": "16a2cd31f0114adc856fadb06a18648c",
      "$ref": "https://<domainURL>/admin/v1/Conditions/16a2cd31f0114adc856fadb06a18648c"
    },
    {
      "type": "Condition",
      "value": "e742c4b2a391451da6dfc42dfd8a4c7d",
      "$ref": "https://<domainURL>/admin/v1/Conditions/e742c4b2a391451da6dfc42dfd8a4c7d"
    },
    {
      "type": "Condition",
      "value": "4d7afc63249943a3b6136876f30f7860",
      "$ref": "https://<domainURL>/admin/v1/Conditions/4d7afc63249943a3b6136876f30f7860"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:ConditionGroup"
  ]
}
```

### Create Allow Authorization Policy Rule 🔗 
The following example shows how to create a rule by submitting a POST request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Rules
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Rule"
  ],
  "name": "Allow Authorization policy rule",
  "policyType": {
    "value": "AllowAuthz"
  },
  "return": [
    {
      "name": "effect",
      "value": "ALLOW"
    },
    {
      "name": "setHeader",
      "value": "USER_NAME=$(user.userName),USER_ID=$(user.id)"
    }
  ],
  "conditionGroup": {
    "value": "<allow authz policy condition group id>",
    "type": "ConditionGroup"
  }
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "id": "7a8dfdc5d175418ea7babb63cf0301ee",
  "meta": {
    "created": "2022-10-21T15:39:49.097Z",
    "lastModified": "2022-10-21T15:39:49.097Z",
    "resourceType": "Rule",
    "location": "https://<domainURL>/admin/v1/Rules/7a8dfdc5d175418ea7babb63cf0301ee"
  },
  "name": "Allow Authorization policy rule",
  "policyType": {
    "value": "AllowAuthz",
    "$ref": "https://<domainURL>/admin/v1/PolicyTypes/AllowAuthz"
  },
  "conditionGroup": {
    "value": "d073eb1df00f4b388fbb06430b70173e",
    "type": "ConditionGroup",
    "name": "ConditionGroup",
    "$ref": "https://<domainURL>/admin/v1/ConditionGroups/d073eb1df00f4b388fbb06430b70173e"
  },
  "return": [
    {
      "name": "effect",
      "value": "ALLOW"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Rule"
  ]
}
```

### Update Allow Authorization Policy Rule Reference 🔗 
The following example shows how to update values for a policy by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>" https://<domainURL>/admin/v1/Policies/<ID>
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "replace",
      "path": "rules",
      "value": [
        {
          "value": "<AllowAuthzRule id>",
          "sequence": 1
        }
      ]
    }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "description": "Authorization allow policy",
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "id": "bb7988b1b4434528836171a3c2ce6fe6",
  "meta": {
    "created": "2022-10-21T15:20:31.144Z",
    "lastModified": "2022-10-21T15:41:30.341Z",
    "resourceType": "Policy",
    "location": "https://<domainURL>/admin/v1/Policies/bb7988b1b4434528836171a3c2ce6fe6"
  },
  "active": false,
  "name": "Allow Authorization policy",
  "policyType": {
    "value": "AllowAuthz",
    "$ref": "https://<domainURL>/admin/v1/PolicyTypes/AllowAuthz"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Policy"
  ]
}
```

### Update App Resource Reference for Allow Authorization Policy 🔗 
The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Apps/<ID>
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "replace",
      "path": "",
      "value": "<AllowAuthzPolicy id>"
    }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "isAliasApp": false,
  "meta": {
    "created": "2022-10-20T19:23:16.937Z",
    "lastModified": "2022-10-21T15:44:02.110Z",
    "resourceType": "App",
    "location": "https://<domainURL>/admin/v1/Apps/23b7bf0f79854002b2db81b808e6a54b"
  },
  "active": false,
  "isLoginTarget": false,
  "idcsCreatedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "displayName": "Enterprise App",
  "showInMyApps": false,
  "isMobileTarget": false,
  "allowOffline": false,
  "isUnmanagedApp": false,
  "idcsLastModifiedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "isOPCService": false,
  "description": "Enterprise Application",
  "isOAuthClient": false,
  "isManagedApp": false,
  "isSamlServiceProvider": false,
  "infrastructure": false,
  "allUrlSchemesAllowed": false,
  "id": "23b7bf0f79854002b2db81b808e6a54b",
  "isWebTierPolicy": true,
  "loginMechanism": "OIDC",
  "allowAccessControl": false,
  "isOAuthResource": false,
  "migrated": false,
  "isKerberosRealm": false,
  "attrRenderingMetadata": [
    {
      "visible": false,
      "name": "aliasApps"
    }
  ],
  "basedOnTemplate": {
    "lastModified": "2022-10-16T17:17:34Z",
    "value": "CustomWebAppTemplateId",
    "wellKnownId": "CustomWebAppTemplateId",
    "$ref": "https://<domainURL>/admin/v1/AppTemplates/CustomWebAppTemplateId"
  },
  "allowAuthzPolicy": {
    "value": "bb7988b1b4434528836171a3c2ce6fe6",
    "$ref": "https://<domainURL>/admin/v1/Policies/bb7988b1b4434528836171a3c2ce6fe6"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ]
}
```

## Create Deny Authorization Policy 🔗 
These use cases provide example requests to create the deny authorization policy for an enterprise application using the identity domains REST API.
The following use cases walk you through the steps to create the deny authorization policy for an enterprise application using the identity domains REST API:
  * [Add Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_vtn_5th_njb)
  * [Create Deny Authorization Policy Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_zr1_l5h_njb)
  * [Create Deny Authorization Policy Condition Group](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_atb_y5h_njb)
  * [Create Deny Authorization Policy Rule](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ofs_2vh_njb)
  * [Update Deny Authorization Policy Rule Reference](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_hzs_5vh_njb)
  * [Update App Resource Reference for Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_h4x_nvh_njb)


### Add Deny Authorization Policy 🔗 
The Deny Authorization Policy is automatically added while creating an enterprise application.
The created policy id is available in the response as follows:
```
"urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App": {
  "allowAuthzPolicy": {
    "value": "1680009a68d947fc94e817102300e362",
    "$ref": "https://<domainURL>/admin/v1/Policies/1680009a68d947fc94e817102300e362"
  },
  "denyAuthzPolicy": {
    "value": "8f91bf044dd34415936a035434bd766c",
    "$ref": "https://<domainURL>/admin/v1/Policies/8f91bf044dd34415936a035434bd766c"
  }
}
```

### Create Deny Authorization Policy Conditions 🔗 
The following example shows how to create a condition to be evaluated by submitting a POST request on the REST resource using cURL. Conditions are referenced from Condition Groups. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl 
  -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Conditionss
```

#### Example of Request Body - Group Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"isInTheseGroups",
  "attributeName":"user.groups[*].value",
  "operator":"coany",
  "attributeValue":"[\"<group guid>\"]"
}
```

#### Example of Response Body - Group Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "isInTheseGroups",
  "attributeName": "user.groups[*].value",
  "operator": "coany",
  "attributeValue": "[\"6d89b1f9b5b84753926b3aedbf71c289\"]",
  "id": "c25d88b87320467da4467b2a12168cec",
  "meta": {
    "created": "2022-10-21T15:24:08.007Z",
    "lastModified": "2022-10-21T15:24:08.007Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/c25d88b87320467da4467b2a12168cec"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - User Not in Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"isNotInTheseUsers",
  "attributeName":"user.userName",
  "operator":"nin",
  "attributeValue":"[\"<user name>\"]"
}
```

#### Example of Response Body - User Not in Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "isNotInTheseUsers",
  "attributeName": "user.userName",
  "operator": "nin",
  "attributeValue": "[\"bf11562fd0dd4fda85fde3690b104dd3\"]",
  "id": "16a2cd31f0114adc856fadb06a18648c",
  "meta": {
    "created": "2022-10-21T15:25:17.519Z",
    "lastModified": "2022-10-21T15:25:17.519Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/16a2cd31f0114adc856fadb06a18648c"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - Administrator Role Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"idcsAdminRole",
  "attributeName":"user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:appRoles[*].adminRole",
  "operator":"co",
  "attributeValue":"[\"true\"]"
}
```

#### Example of Response Body - Administrator Role Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "idcsAdminRole",
  "attributeName": "user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:appRoles[*].adminRole",
  "operator": "co",
  "attributeValue": "[\"true\"]",
  "id": "e742c4b2a391451da6dfc42dfd8a4c7d",
  "meta": {
    "created": "2022-10-21T15:25:39.399Z",
    "lastModified": "2022-10-21T15:25:39.399Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/e742c4b2a391451da6dfc42dfd8a4c7d"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

#### Example of Request Body - Network Perimeter Condition
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name":"SubjectIPAddress",
  "attributeName":"subject.ip",
  "operator":"eq",
  "attributeValue":"#inIPRange(\"<Network perimeter id>\")"
}
```

#### Example of Response Body - Network Perimeter Condition
The following example shows the contents of the response body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Condition"
  ],
  "name": "SubjectIPAddress",
  "attributeName": "subject.ip",
  "operator": "eq",
  "attributeValue": "#inIPRange(\"83bad53f0a50454d909a4709d1335e0d\")",
  "id": "4d7afc63249943a3b6136876f30f7860",
  "meta": {
    "created": "2022-10-21T15:27:45.819Z",
    "lastModified": "2022-10-21T15:27:45.819Z",
    "resourceType": "Condition",
    "location": "https://<domainURL>/admin/v1/Conditions/4d7afc63249943a3b6136876f30f7860"
  },
  "idcsCreatedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsLastModifiedBy": {
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "type": "User",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  }
}
```

### Create Deny Authorization Policy Condition Group 🔗 
The following example shows how to create a condition group to be evaluated by submitting a POST request on the REST resource using cURL. Condition groups are referenced from a Rule. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/ConditionGroupss
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "name":"ConditionGroup",
  "operator":"or",
  "schemas":[ 
   "urn:ietf:params:scim:schemas:oracle:idcs:ConditionGroup"
  ],
  "conditions":[ 
   { 
     "value":"<group condition id>",
     "type":"Condition"
   },
   { 
     "value":"<user condition id>",
     "type":"Condition"
   },
   { 
     "value":"<admin role condition id>",
     "type":"Condition"
   },
   { 
     "value":"<network perimeter condition id>",
     "type":"Condition"
   }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "operator": "or",
  "id": "d073eb1df00f4b388fbb06430b70173e",
  "meta": {
    "created": "2022-10-21T15:29:51.218Z",
    "lastModified": "2022-10-21T15:29:51.218Z",
    "resourceType": "ConditionGroup",
    "location": "https://<domainURL>/admin/v1/ConditionGroups/d073eb1df00f4b388fbb06430b70173e"
  },
  "name": "ConditionGroup",
  "conditions": [
    {
      "type": "Condition",
      "value": "c25d88b87320467da4467b2a12168cec",
      "$ref": "https://<domainURL>/admin/v1/Conditions/c25d88b87320467da4467b2a12168cec"
    },
    {
      "type": "Condition",
      "value": "16a2cd31f0114adc856fadb06a18648c",
      "$ref": "https://<domainURL>/admin/v1/Conditions/16a2cd31f0114adc856fadb06a18648c"
    },
    {
      "type": "Condition",
      "value": "e742c4b2a391451da6dfc42dfd8a4c7d",
      "$ref": "https://<domainURL>/admin/v1/Conditions/e742c4b2a391451da6dfc42dfd8a4c7d"
    },
    {
      "type": "Condition",
      "value": "4d7afc63249943a3b6136876f30f7860",
      "$ref": "https://<domainURL>/admin/v1/Conditions/4d7afc63249943a3b6136876f30f7860"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:ConditionGroup"
  ]
}
```

### Create Deny Authorization Policy Rule 🔗 
The following example shows how to create a rule by submitting a POST request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X POST
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>" https://<domainURL>/admin/v1/Rules
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Rule"
  ],
  "name": "Deny Authz policy rule",
  "policyType": {
    "value": "DenyAuthz"
  },
  "return": [
    {
      "name": "effect",
      "value": "DENY"
    },
    {
      "name": "logout",
      "value": "true"
    }
  ],
  "conditionGroup": {
    "value": "< deny authz policy condition group id>",
    "type": "ConditionGroup"
  }
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "id": "7a8dfdc5d175418ea7babb63cf0301ee",
  "meta": {
    "created": "2022-10-21T15:39:49.097Z",
    "lastModified": "2022-10-21T15:39:49.097Z",
    "resourceType": "Rule",
    "location": "https://<domainURL>/admin/v1/Rules/7a8dfdc5d175418ea7babb63cf0301ee"
  },
  "name": "Deny Authz policy rule",
  "policyType": {
    "value": "DenyAuthz",
    "$ref": "https://<domainURL>/admin/v1/PolicyTypes/AllowAuthz"
  },
  "conditionGroup": {
    "value": "d073eb1df00f4b388fbb06430b70173e",
    "type": "ConditionGroup",
    "name": "ConditionGroup",
    "$ref": "https://<domainURL>/admin/v1/ConditionGroups/d073eb1df00f4b388fbb06430b70173e"
  },
  "return": [
    {
      "name": "effect",
      "value": "DENY"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Rule"
  ]
}
```

### Update Deny Authorization Policy Rule Reference 🔗 
The following example shows how to update values for a policy by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>" https://<domainURL>/admin/v1/Policies/<ID>
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations":[ 
   { 
     "op":"replace",
     "path":"rules",
     "value":[ 
      { 
        "value":"<DenyAuthzRule id>",
        "sequence":1
      }
     ]
   }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "idcsLastModifiedBy": {
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "display": "admin opc",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "description": "Authorization deny policy",
  "idcsCreatedBy": {
    "type": "User",
    "display": "admin opc",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "id": "bb7988b1b4434528836171a3c2ce6fe6",
  "meta": {
    "created": "2022-10-21T15:20:31.144Z",
    "lastModified": "2022-10-21T15:41:30.341Z",
    "resourceType": "Policy",
    "location": "https://<domainURL>/admin/v1/Policies/bb7988b1b4434528836171a3c2ce6fe6"
  },
  "active": false,
  "name": "Deny Authorization policy",
  "policyType": {
    "value": "DenyAuthz",
    "$ref": "https://<domainURL>/admin/v1/PolicyTypes/DenyAuthz"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:Policy"
  ]
}
```

### Update App Resource Reference for Deny Authorization Policy 🔗 
The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
#### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl -X PATCH
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"https://<domainURL>/admin/v1/Apps/<ID>
```

#### Example of Request Body
The following shows an example of the request body in JSON format:
```
{ 
  "schemas":[ 
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations":[ 
   { 
     "op":"replace",
     "path":"urn:ietf:params:scim:schemas:oracle:idcs:extension:enterpriseApp:App:denyAuthzPolicy.value",
     "value":"<DenyAuthzPolicy id>"      
   }
  ]
}
```

#### Example of Response Body
The following example shows the contents of the response body in JSON format:
```
{
  "isAliasApp": false,
  "meta": {
    "created": "2022-10-20T19:23:16.937Z",
    "lastModified": "2022-10-21T16:02:21.720Z",
    "resourceType": "App",
    "location": "https://<domainURL>/admin/v1/Apps/23b7bf0f79854002b2db81b808e6a54b"
  },
  "active": false,
  "isLoginTarget": false,
  "idcsCreatedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "displayName": "Enterprise App",
  "showInMyApps": false,
  "isMobileTarget": false,
  "allowOffline": false,
  "isUnmanagedApp": false,
  "idcsLastModifiedBy": {
    "display": "admin opc",
    "type": "User",
    "value": "bf11562fd0dd4fda85fde3690b104dd3",
    "$ref": "https://<domainURL>/admin/v1/Users/bf11562fd0dd4fda85fde3690b104dd3"
  },
  "isOPCService": false,
  "description": "Enterprise Application",
  "isOAuthClient": false,
  "isManagedApp": false,
  "isSamlServiceProvider": false,
  "infrastructure": false,
  "allUrlSchemesAllowed": false,
  "id": "23b7bf0f79854002b2db81b808e6a54b",
  "isWebTierPolicy": true,
  "loginMechanism": "OIDC",
  "allowAccessControl": false,
  "isOAuthResource": false,
  "migrated": false,
  "isKerberosRealm": false,
  "attrRenderingMetadata": [
    {
      "visible": false,
      "name": "aliasApps"
    }
  ],
  "basedOnTemplate": {
    "lastModified": "2022-10-16T17:17:34Z",
    "value": "CustomWebAppTemplateId",
    "wellKnownId": "CustomWebAppTemplateId",
    "$ref": "https://<domainURL>/admin/v1/AppTemplates/CustomWebAppTemplateId"
  },
  "allowAuthzPolicy": {
    "value": "bb7988b1b4434528836171a3c2ce6fe6",
    "$ref": "https://<domainURL>/admin/v1/Policies/bb7988b1b4434528836171a3c2ce6fe6"
  },
  "denyAuthzPolicy": {
    "value": "0e094096e9314b1ab6c763acc3619909",
    "$ref": "https://<domainURL>/admin/v1/Policies/0e094096e9314b1ab6c763acc3619909"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:App"
  ]
}
```

Was this article helpful?
YesNo

