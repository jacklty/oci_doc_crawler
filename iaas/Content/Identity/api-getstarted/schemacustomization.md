Updated 2024-04-02
# Customizing User Schemas
When you start using identity domains, you might load a different set of user identities based on requirements from various departments within or outside of your organization. Schema Customization allows you to create identity domain-specific custom schemas to supplement the out-of-the-box (OOTB) attributes for a resource and allows user schemas to be extended.
A custom schema is available OOTB as an empty schema with no attributes defined. The following "Custom User" schema is an example of an empty custom schema with no attributes. This custom schema is used as an example for all example request payloads in this use case.
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "meta": {
    "resourceType": "Schema",
    "created": "2022-08-15T05:02:13.788Z",
    "lastModified": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  },
  "idcsLastModifiedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

**Note** You can't update the following properties. Any attempt to update these properties is ignored.
  * type
  * idcsSearchable
  * uniqueness
  * caseExact
  * idcsSensitive
  * multiValued
  * required


## Adding Custom User Schema Attributes
The following links provide information and example requests for adding custom user schema attributes using both the PUT and PATCH methods. Information on the validations performed when adding attributes is also included.
  * [Adding Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#addingattributestoemptyschema "Populate an empty custom schema by adding new attributes using the PUT method.")
  * [Adding Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#addingattributestocustomschema "This example shows you how to use PATCH "op": "add" to add custom attributes.")
  * [Validations Performed When Adding Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsadd "When you add custom attributes, identity domains perform certain validations. The following table describes the validations based on the Add operation.")


## Updating Custom User Schema Attributes
The following links provide information and example requests for updating custom user schema attributes using both the PUT and PATCH methods. Information on validations performed when updating attributes is also included.
  * [Updating Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#updatingattributesincustomschema "Update attributes in your custom schema using the PUT method.")
  * [Updating Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#replaceattributesincustomschema "Replace attributes in the custom schema using the PATCH method.")
  * [Validations Performed When Updating Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsupdate "Whenever you replace custom attributes, identity domains perform certain validations. The following table describes the validations based on the Replace/Update operation.")


## Removing Custom Schema Attributes
The following links provide information and example requests when removing custom user schema attributes using both the PUT and PATCH methods. Information on validations performed when removing attributes is also included.
  * [Removing Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#removingattributesfromcustomschema "Remove attributes in your custom schema using the PUT method.")
  * [Removing Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#replaceattributeswithfiltersincustomschema "This section describes the use of PATCH "op":"remove" when removing custom user schema attributes.")
  * [Validations Performed When Removing Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsincustomschema "Whenever you remove custom attributes, identity domains perform certain validations.")


## Enabling the Import of Custom User Schema Attributes
The following link provides information and example requests when importing custom user schema attributes.
  * [Enabling the Import of Custom User Schema Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#settingcolnamevalue "To import data into your new schema attributes using a .csv file, you must first set column name values for the new attributes.")


## Adding Custom User Schema Attributes Using PUT 🔗 
Populate an empty custom schema by adding new attributes using the PUT method.
In this example, we're updating the following attributes:
Attribute | Type  
---|---  
subDivision |  string  
branchAddress |  string  
**Example PUT Request**
```
PUT /admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:extension:custom:2.0:User",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "idcsResourceTypes": ["User"],
  "attributes": [
    {
      "name": "subDivision",
      "idcsDisplayName": "Sub Division",
      "type": "string",
      "idcsMinLength": 5,
      "idcsMaxLength": 30,
      "description": "SubDivision",
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    },
    {
      "name": "branchAddress",
      "idcsDisplayName": "Branch Address",
      "type": "string",
      "description": "Branch Office Address",
      "idcsMinLength": 5,
      "idcsMaxLength": 300,
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ]
}
```
**Example JSON Response** ```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "idcsDisplayName": "Sub Division",
      "name": "subDivision",
      "mutability": "readWrite",
      "idcsMinLength": 5,
      "description": "SubDivision",
      "type": "string",
      "idcsSearchable": true,
      "idcsMaxLength": 30,
      "multiValued": false,
      "returned": "always",
      "uniqueness": "none",
      "required": false,
      "caseExact": true,
      "idcsValuePersisted": true,
      "idcsTargetAttributeName": "I_VC_40_IFLEX_1"
    },
    {
      "name": "branchAddress",
      "description": "Branch Office Address",
      "mutability": "readWrite",
      "idcsMinLength": 5,
      "type": "string",
      "idcsSearchable": true,
      "idcsMaxLength": 300,
      "multiValued": false,
      "returned": "always",
      "idcsDisplayName": "Branch Address",
      "uniqueness": "none",
      "required": false,
      "caseExact": true,
      "idcsValuePersisted": true,
      "idcsTargetAttributeName": "I_VC_4K_IFLEX_1"
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T19:26:40.603Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
}
```

## Adding Custom User Schema Attributes Using PATCH 🔗 
This example shows you how to use PATCH "op": "add" to add custom attributes.
The validations performed while making these operations are similar to the PUT method. See the [Validations Performed When Adding Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsadd "When you add custom attributes, identity domains perform certain validations. The following table describes the validations based on the Add operation.") section for more information.
Update the custom schema to add new attributes using PATCH. In this example, the PATCH "add" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it's replaced automatically. If it doesn't exist, the attribute is automatically added. If the name property is missing, an error message appears.
**Example PATCH Request**
```
PATCH /Schemas/urn:itef:params:scim:schemas:idcs:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "attributes",
      "value": [
        {
          "idcsValuePersisted": true,
          "uniqueness": "none",
          "name": "nickName",
          "idcsDisplayName": "NICKNAME100",
          "description": "NICKNAME100",
          "required": false,
          "type": "string",
          "idcsMinLength": 10,
          "idcsMaxLength": 100,
          "idcsAuditable": true,
          "caseExact": true,
          "returned": "default",
          "idcsSearchable": true,
          "multiValued": false
        }
      ]
    }
  ]
}
```

**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "idcsTargetAttributeName": "I_VC_4K_IFLEX_2",
      "idcsDisplayName": "NICKNAME100",
      "description": "NICKNAME100",
      "type": "string",
      "idcsAuditable": true,
      "required": false,
      "returned": "default",
      "idcsValuePersisted": true,
      "idcsMaxLength": 100,
      "idcsSearchable": true,
      "idcsMinLength": 10,
      "multiValued": false,
      "caseExact": true,
      "uniqueness": "none",
      "name": "nickName"
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T19:31:37.247Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
}
```

## Validations Performed When Adding Attributes 🔗 
When you add custom attributes, identity domains perform certain validations. The following table describes the validations based on the Add operation.
**Add Validations**
This table describes the validations that identity domains perform when you add new custom attributes to the target schema.
Attribute Name | Validations Performed  
---|---  
name |  Check for duplicates. This value must be unique across the custom schema.  
idcsDisplayName |  Check for duplicates. This value must be unique across the custom schema.  
idcsMaxLength |  Value can't be less than 2.  
idcsMinLength |  Value can't be less than 1.  
returned |  Value must be a valid return value such as always, default, request, or never.  
type |  Value must be a string that can be single or multivalued.  
mutability |  Value must be a valid mutability like readWrite, readOnly, immutable, or writeonly.  
idcsCsvAttributeNameMappings.columnHeaderName |  Value must be unique across the custom schema.  
idcsCsvAttributeNameMappings.multiValueDelimiter |  Mandatory attribute for multivalued attributes having idcsCsvAttributeNameMappings.  
## Updating Custom User Schema Attributes Using PUT 🔗 
Update attributes in your custom schema using the PUT method.
### Updating Attributes
In this example, we're updating the attributes for "subDivision" and "branchAddress."
**Example PUT Request**
```
PUT /admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:extension:custom:2.0:User",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "idcsResourceTypes": ["User"],
  "attributes": [
    {
      "name": "subDivision",
      "idcsDisplayName": "Sub Division Office",
      "type": "string",
      "idcsMinLength": 5,
      "idcsMaxLength": 35,
      "description": "SubDivision",
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    },
    {
      "name": "branchAddress",
      "idcsDisplayName": "Branch Address",
      "type": "string",
      "description": "Branch Office Address",
      "idcsMinLength": 5,
      "idcsMaxLength": 350,
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ]
}
```

**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "idcsDisplayName": "Sub Division Office",
      "idcsMaxLength": 35,
      "required": false,
      "idcsValuePersisted": true,
      "caseExact": true,
      "uniqueness": "none",
      "idcsTargetAttributeName": "I_VC_40_IFLEX_1",
      "name": "subDivision",
      "type": "string",
      "idcsMinLength": 5,
      "description": "SubDivision",
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    },
    {
      "required": false,
      "idcsValuePersisted": true,
      "idcsTargetAttributeName": "I_VC_4K_IFLEX_1",
      "idcsMaxLength": 350,
      "caseExact": true,
      "uniqueness": "none",
      "name": "branchAddress",
      "idcsDisplayName": "Branch Address",
      "type": "string",
      "description": "Branch Office Address",
      "idcsMinLength": 5,
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T19:45:17.046Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

### Updating Multi-Valued String Attributes
You can update multivalued string attributes in your existing custom schema using the PUT method. In this example, we're adding the "hobbies" multivalued string attribute.
**Example PUT Request**
```
PUT admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "idcsResourceTypes": ["User"],
  "attributes": [
    {
      "name": "workName",
      "idcsDisplayName": "workName",
      "description": "workName",
      "required": false, 
      "type": "string",
      "idcsMinLength": 1,
      "idcsMaxLength": 4000,
      "idcsAuditable": true,
      "caseExact": true,
      "returned": "default",
      "idcsSearchable": false,
      "multiValued": false,
      "idcsCsvAttributeName": "CSV1"
    },
    {
      "name": "hobbies",
      "idcsDisplayName": "hobbies",
      "description": "hobbies",
      "required": true,
      "type": "string",
      "idcsMinLength": 1,
      "idcsMaxLength": 20,
      "idcsAuditable": true,
      "returned": "default",
      "idcsValuePersisted": true,
      "idcsSearchable": true,
      "multiValued": true
    },  
    {
      "name": "county",
      "idcsDisplayName": "county",
      "description": "county",
      "type": "string",
      "required": false, 
      "idcsMinLength": 1,
      "idcsMaxLength": 40,
      "idcsAuditable": true,
      "caseExact": true,
      "returned": "default",
      "idcsCsvAttributeName": "CSV3",
      "idcsSearchable": false,
      "multiValued": false 
    },
    {
      "name": "nationality",
      "idcsDisplayName": "nationality",
      "description": "nationality",
      "required": true,
      "type": "string",
      "idcsMinLength": 1,
      "idcsMaxLength": 20,
      "idcsAuditable": true,
      "returned": "default",
      "idcsValuePersisted": true,
      "idcsSearchable": true,
      "multiValued": false
    } 
  ]
}
```

## Updating Custom User Schema Attributes Using PATCH 🔗 
Replace attributes in the custom schema using the PATCH method.
### Using the Replace Operation
In this example, the PATCH "replace" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it replaces it automatically. If it doesn't exist, an error message appears.
**Example PATCH Request**
```
Patch /Schemas/urn:item:params:scam:schemas:idcs:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "replace",
      "path": "attributes",
      "value": [
        {
          "name": "nickName",
          "idcsDisplayName": "nickName",
          "description": "Nickname",
          "required": false,
          "type": "string",
          "idcsMinLength": 3,
          "idcsMaxLength": 25,
          "idcsAuditable": false,
          "caseExact": true,
          "returned": "default",
          "multiValued": false
        }
      ]
    }
  ]
}
```

**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "idcsTargetAttributeName": "U_VC_40_IFLEX_1",
      "idcsAuditable": false,
      "idcsValuePersisted": true,
      "description": "Nickname",
      "idcsSearchable": true,
      "idcsMaxLength": 25,
      "uniqueness": "none",
      "name": "nickName",
      "idcsDisplayName": "nickName",
      "required": false,
      "type": "string",
      "idcsMinLength": 3,
      "caseExact": true,
      "returned": "default",
      "multiValued": false
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T19:55:17.467Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

### Using the Replace Operation with Filters
  * In this example, the PATCH "replace" operation is used with filters to update to "true" all attributes that have the "required" property with the "returned" attribute set to "always":```
PATCH /Schemas/urn:item:params:scam:schemas:ides:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [{
      "op": "replace",
      "path": "attributes[name eq \"workName\"].idcsDisplayName",
      "value": "workplace Name"
    }]
}
```

  * In this example, the PATCH "replace" operation is used with filters to update to "false" all attributes with the "auditable" property set to "true".```
PATCH /Schemas/urn:item:params:scam:schemas:ides:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [{
      "op": "replace",
      "path": "attributes[returned eq \"default\"].required",
      "value": true
    }]
}
```



**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "idcsTargetAttributeName": "I_VC_40_IFLEX_1",
      "idcsMinLength": 1,
      "idcsValuePersisted": true,
      "idcsMaxLength": 20,
      "type": "string",
      "idcsSearchable": true,
      "idcsDisplayName": "nationality",
      "name": "nationality",
      "idcsAuditable": true,
      "multiValued": false,
      "description": "nationality",
      "returned": "default",
      "required": false,
      "uniqueness": "none",
      "caseExact": true
    },
    {
      "idcsTargetAttributeName": "U_VC_4K_IFLEX_1",
      "idcsDisplayName": "workplace Name",
      "description": "workName",
      "idcsCsvAttributeName": "CSV1",
      "type": "string",
      "idcsMaxLength": 4000,
      "idcsAuditable": true,
      "required": false,
      "returned": "default",
      "idcsMinLength": 1,
      "name": "workName",
      "idcsSearchable": false,
      "multiValued": false,
      "caseExact": true,
      "uniqueness": "none",
      "idcsValuePersisted": true
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T20:15:21.969Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

### Using the Replace Operation to Update a Multi-Valued String Attribute
You can replace multivalued string attributes in your custom schema using the PATCH method. In this example, the PATCH "replace" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it replaces it automatically. If it doesn't exist, an error message appears.
**Example PATCH Request**
```
Patch admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [{
      "op": "replace",
      "path": "attributes",
      "value": [
        {
          "name": "hobbies",
          "idcsDisplayName": "hobbies",
          "description": "hobbies",
          "required": true,
          "type": "string",
          "idcsMinLength": 1,
          "idcsMaxLength": 20,
          "idcsAuditable": true,
          "returned": "default",
          "idcsValuePersisted": true,
          "idcsSearchable": true,
          "multiValued": true
        }
      ] 
    }
  ]
}
```

## Validations Performed When Updating Attributes 🔗 
Whenever you replace custom attributes, identity domains perform certain validations. The following table describes the validations based on the Replace/Update operation.
**Replace/ Update Validations**
This table describes the validations that identity domains perform when you update existing custom attributes to the target schema.
Attribute Name | Validations Performed  
---|---  
idcsMinLength |  Value can't be less than 1. It can't be over the column limit allocated for the attribute. For example, if the U_VC_40 column was allocated, then idcsMinLength can't exceed 40.  
idcsMaxLength |  Value can't be less than 1. It must be equal to or greater than the idcsMaxLength value for the attribute, and can't be over the column limit allocated for the attribute. For example, if the U_VC_40 column was allocated, then idcsMaxLength can't exceed 40.  
idcsMinValue |  Value can't be less than what currently exists in the store.  
idcsMaxValue |  Value can't be greater than what currently exists in the store.  
canonicalValues |  Values must be a super set of what currently exists in the store.  
idcsCsvAttributeName |  Value must be unique across the custom schema.  
name |  Value must be unique across the custom schema.  
idcsDisplayName |  Value must be unique across the custom schema.  
## Removing Custom User Schema Attributes Using PUT 🔗 
Remove attributes in your custom schema using the PUT method.
If the custom attributes "subDivision" and "branchAddress" already exist in the custom schema, then you can remove branchAddress using the following PUT request.
**Note** It is recommended that you remove attributes from the custom schema only when you're putting together a custom schema for the first time. Removing attributes after you have built a custom schema could cause issues, as many users may have already been provisioned using the custom attributes. To remove custom schema attributes after users have been provisioned using the attributes, you must first delete all the data that pertains to the custom schema attributes from the database.
**Example PUT Request**
```
PUT /admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:extension:custom:2.0:User",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "idcsResourceTypes": ["User"],
  "attributes": [
    {
      "name": "subDivision",
      "idcsDisplayName": "Sub Division Office",
      "type": "string",
      "idcsMinLength": 5,
      "idcsMaxLength": 35,
      "description": "SubDivision",
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ]
}
```

**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "required": false,
      "idcsValuePersisted": true,
      "caseExact": true,
      "uniqueness": "none",
      "idcsTargetAttributeName": "I_VC_40_IFLEX_1",
      "name": "subDivision",
      "idcsDisplayName": "Sub Division Office",
      "type": "string",
      "idcsMinLength": 5,
      "idcsMaxLength": 35,
      "description": "SubDivision",
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T20:02:04.354Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

## Removing Custom User Schema Attributes Using PATCH 🔗 
This section describes the use of PATCH `"op":"remove"` when removing custom user schema attributes.
### Using the Remove Operation with Filters
  * In this example, the PATCH "remove" operation is used with filters to remove the "subDivision" attribute.```
PATCH  /Schemas/urn:item:params:scam:schemas:ides:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [{
      "op": "remove",
      "path": "attributes[name eq \"subDivision\"]"
    }]
}
```

  * In this example, the PATCH "remove" operation is used with filters to remove all attributes with the "required" property set to "false".```
Patch  /Schemas/urn:item:params:scam:schemas:ides:extension:custom:User
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [{
      "op": "remove",
      "path": "attributes[required eq false]"
    }]
}
```



**Example JSON Response**
```
{
  "name": "CustomUser",
  "description": "Custom User",
  "id": "urn:ietf:params:scim:schemas:idcs:extension:custom:User",
  "idcsResourceTypes": [
    "User"
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Schema"
  ],
  "attributes": [
    {
      "required": true,
      "idcsValuePersisted": true,
      "idcsTargetAttributeName": "I_VC_4K_IFLEX_1",
      "idcsMaxLength": 350,
      "caseExact": true,
      "uniqueness": "none",
      "name": "branchAddress",
      "idcsDisplayName": "Branch Address",
      "type": "string",
      "description": "Branch Office Address",
      "idcsMinLength": 5,
      "multiValued": false,
      "returned": "always",
      "mutability": "readWrite",
      "idcsSearchable": true
    }
  ],
  "meta": {
    "lastModified": "2022-08-15T20:06:53.745Z",
    "resourceType": "TenantSchema",
    "created": "2022-08-15T05:02:13.788Z",
    "location": "https://<domainURL>/admin/v1/TenantSchemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User"
  },
  "idcsLastModifiedBy": {
    "type": "App",
    "display": "admin",
    "$ref": "https://<domainURL>/admin/v1/Apps"
  },
  "idcsCreatedBy": {
    "value": "158d625222f442ef8fcc817593701dd9",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>/admin/v1/Apps/158d625222f442ef8fcc817593701dd9"
  }
}
```

## Validations Performed When Removing Attributes 🔗 
Whenever you remove custom attributes, identity domains perform certain validations.
When custom attributes are removed using PUT or PATCH, identity domains perform delete validations to ensure that no data has been previously provisioned in the database for that attribute. If data has been provisioned, then the remove operation fails.
## Enabling the Import of Custom User Schema Attributes 🔗 
To import data into your new schema attributes using a .csv file, you must first set column name values for the new attributes.
In this example, a new user attribute was created called `employeeStatus.` To set the column name value for this attribute so that you can import data to that attribute from a .csv file, internally map the attribute to `idcsCsvAttributeNameMappings`.
**Example PATCH Request**
The following request example shows how to set the column name value for the `employeeStatus` string custom attribute.
```
PATCH /admin/v1/Schemas/urn:ietf:params:scim:schemas:idcs:extension:custom:User
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {
      "op": "add",
      "path": "attributes[name eq \"employeeStatus\"].idcsCsvAttributeNameMappings",
      "value": [
        {
          "columnHeaderName": "Employee Status"
        }
      ]
    }
  ]
}
```

You can now import data using a .csv file that includes a column (with data) that's named **Employee Status.**
The following request example shows how to set a column name for a string array custom attribute named **Favorite Colors** whose values would be comma delimited in a .csv file.
```
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {
      "op": "add",
      "path": "attributes[name eq \"favoriteColors\"].idcsCsvAttributeNameMappings",
      "value": [
        {
          "columnHeaderName": "Favorite Colors",
          "multiValueDelimiter": ","
        }
      ]
    }
  ]
}
```

**More Information**
  * See [Importing](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing "This section provides example requests and responses when you want to import users, groups, and AppRoles into your environment using the identity domains REST API..") for the use case on importing user data using the identity domains REST API.


Was this article helpful?
YesNo

