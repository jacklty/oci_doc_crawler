Updated 2024-02-13
# Managing Exadata Instances
**Important** The My Services dashboard and APIs are deprecated. 
The following procedures walk you through creating, modifying, and deleting Exadata instances used with the [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/).
**Important** These procedures are for use with Oracle Database Exadata Database Service on Cloud@Customer **ONLY**. For more information, see [Administering Oracle Database Exadata Cloud at Customer](https://docs.oracle.com/en/cloud/cloud-at-customer/exadata-cloud-at-customer/exacc/get-started-this-service.html). These procedures **DO NOT** apply to the Exadata Cloud Service available in Oracle Cloud Infrastructure.
## Prerequisites 🔗 
Before you can manage Exadata instances, you need to: 
  * Subscribe to an Oracle Cloud service 
  * Obtain account credentials with required roles assigned
  * Determine your API endpoint


[To subscribe to an Oracle Cloud service](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
To access [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/), you must request a trial or paid subscription to an Oracle Cloud service. 
[To obtain account credentials and role assignments](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Ask your account administrator for the following items to access [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/):
  * Account credentials:
    * User name and password
    * Identity domain ID
An identity domain ID can be either the _IDCS GUID_ that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the _Identity Domain name_ for a traditional Cloud Account.
  * Required roles assigned to above user name


[To determine your API endpoint](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Insert the identity domain ID provided by the account administrator (<domain>) between `/itas/` and `/myservices/`. 
Example:
Copy
```
https://itra.oraclecloud.com/itas/<domain>/myservices/api/v1/serviceEntitlements
```

## Creating Exadata Instances 🔗 
This section covers how to create a basic Exadata instance, an instance with custom IP network configuration, and an instance with multi-VM support. 
[To create a basic Exadata instance](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the required payload to create a new instance for a given service entitlement (Exadata in our case).
In the following example, <domain> is the identity domain ID. 
Copy
```
POST /itas/<domain>/myservices/api/v1/operations
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "requestPayload.name", 
     "value": "newinstanceName" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.adminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminFirstName", 
     "value": "John" 
    }, 
    { 
     "name": "requestPayload.adminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.invokerAdminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminFirstName", 
     "value": "John"
    }, 
    { 
     "name": "requestPayload.invokerAdminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.customAttributes.ExaUnitName", 
     "value": "systemname" 
    }, 
    { 
     "name": "requestPayload.customAttributes.CreateSparse", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.BackupToDisk", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.isBYOL", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.PickRackSize", 
     "value": "Quarter Rack" 
    }, 
    { 
     "name": "requestPayload.customAttributes.SELECTED_DC_ID", 
     "value": "US001"           
    }
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-CREATE" 
   } 
  } 
 ] 
}
```

#### Attributes
Name | Description  
---|---  
requestPayload.name  |  Required: Yes Type: String Name of the Exadata instance. This name:
  * Must not exceed 25 characters.
  * Must start with a letter.
  * Must contain only lower case letters and numbers.
  * Must not contain spaces or any other special characters.
  * Must be unique within the identity domain.

  
requestPayload. serviceEntitlementId |  Required: Yes  Type: String Service Entitlement for the Exadata instance. See "Exadata Service Entitlement discovery." Note that any "cesi-" or "sub-" prefix should not be included.  
requestPayload. customAttributes. ExaUnitName |  Required: Yes  Type: String A name for your Exadata Database Machine environment. This name is also used as the cluster name for the Oracle Grid Infrastructure installation.  
requestPayload. customAttributes. CreateSparse |  Required: Yes  Type: String "Y" to create a disk group that is based on sparse grid disks, else "N".  You must select this option to enable Exadata Cloud Service snapshots. Exadata snapshots enable space-efficient clones of Oracle databases that can be created and destroyed very quickly and easily.  
requestPayload. customAttributes. BackupToDisk |  Required: Yes  Type: String "Y" to use "Database backups on Exadata Storage", else "N".  This option configures the Exadata storage to enable local database backups on Exadata storage.  
requestPayload. customAttributes. isBYOL |  Required: Yes  Type: String "Y" to indicate that the Exadata Cloud Service instance uses Oracle Database licenses that are provided by you rather than licenses that are provided are part of the service subscription, else "N".  This option only affects the billing that is associated with the service instance. It has no effect on the technical configuration of the Exadata Cloud Service instance.  
requestPayload. customAttributes. PickRackSize |  Required: Yes  Type: String Specify the rack configuration for your service instance. Exact allowed values depend on your purchase. Typical values are like "Full Rack", "Half Rack", "Quarter Rack" or "Eighth Rack".  
requestPayload. customAttributes. SELECTED_DC_ID |  Required: Yes  Type: String Data center that will host your Exadata Cloud Service instance. See "Exadata Service Entitlement discovery" to obtain the Eligible Data Center IDs.  
[To create an Exadata instance with custom IP network configuration](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the attributes ClientNetwork and BackupNetwork as part of the payload. The following example includes these optional attributes as well as required attributes. 
In the following example, <domain> is the identity domain ID. 
Copy
```
POST /itas/<domain>/myservices/api/v1/operations
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "requestPayload.name", 
     "value": "newinstanceName" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.adminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminFirstName", 
     "value": "John" 
    }, 
    { 
     "name": "requestPayload.adminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.invokerAdminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminFirstName", 
     "value": "John"
    }, 
    { 
     "name": "requestPayload.invokerAdminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.customAttributes.ExaUnitName", 
     "value": "systemname" 
    }, 
    { 
     "name": "requestPayload.customAttributes.CreateSparse", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.BackupToDisk", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.isBYOL", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.PickRackSize", 
     "value": "Quarter Rack" 
    }, 
    { 
     "name": "requestPayload.customAttributes.SELECTED_DC_ID", 
     "value": "US001"           
    }
    { 
     "name": "requestPayload.customAttributes.ClientNetwork", 
     "value": "/root/root/1/ipnetwork1" 
    }, 
    { 
     "name": "requestPayload.customAttributes.BackupNetwork", 
     "value": "/root/root/1/ipnetwork2" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-CREATE" 
   } 
  } 
 ] 
}
```

#### Attributes
Name | Description  
---|---  
requestPayload. customAttributes. ClientNetwork |  Required: Yes  Type: Url IP network definitions for the network that is primarily used for client access to the database servers. Applications typically access databases on Exadata Cloud Service through this network using Oracle Net Services in conjunction with Single Client Access Name (SCAN) and Oracle RAC Virtual IP (VIP) interfaces.  
requestPayload. customAttributes. BackupNetwork |  Required: Yes  Type: Url IP network definitions for the network that is typically used to access the database servers for various purposes, including backups and bulk data transfers.  
[To create an Exadata instance with multi-VM support](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
If your Exadata system environment is enabled to support multiple virtual machine (VM) clusters, then you can define up to eight clusters and specify how the overall Exadata system resources are allocated to them.
In a configuration with multiple VM clusters, each VM cluster is allocated a dedicated portion of the overall Exadata system resources, with no over-provisioning or resource sharing. On the compute nodes, a separate VM is defined for each VM cluster, and each VM is allocated a dedicated portion of the available compute node CPU, memory, and local disk resources. Each VM cluster is also allocated a dedicated portion of the overall Exadata storage.
Post a request with the attributes EXAUNIT_ALLOCATIONS and MULTIVM_ENABLED as part of the payload. The following example includes these optional attributes as well as required attributes. 
In the following example, <domain> is the identity domain ID and <base64_encoded_string> is a base64 encoding of the payload following the example. 
Example payload for request:
Copy
```
POST /itas/<domain>/myservices/api/v1/operations
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "requestPayload.name", 
     "value": "newinstanceName" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.adminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.adminFirstName", 
     "value": "John" 
    }, 
    { 
     "name": "requestPayload.adminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.invokerAdminUserName", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminEmail", 
     "value": "john.smith@example.com" 
    }, 
    { 
     "name": "requestPayload.invokerAdminFirstName", 
     "value": "John"
    }, 
    { 
     "name": "requestPayload.invokerAdminLastName", 
     "value": "Smith" 
    }, 
    { 
     "name": "requestPayload.customAttributes.ExaUnitName", 
     "value": "systemname" 
    }, 
    { 
     "name": "requestPayload.customAttributes.CreateSparse", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.BackupToDisk", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.isBYOL", 
     "value": "N" 
    }, 
    { 
     "name": "requestPayload.customAttributes.PickRackSize", 
     "value": "Quarter Rack" 
    }, 
    { 
     "name": "requestPayload.customAttributes.SELECTED_DC_ID", 
     "value": "US001"           
    }
    { 
     "name": "requestPayload.customAttributes.EXAUNIT_ALLOCATIONS", 
     "value": "<base64_encoded_string>" 
    }, 
    { 
     "name": "requestPayload.customAttributes.MULTIVM_ENABLED", 
     "value": "true" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-CREATE" 
   } 
  } 
 ] 
}
```

Payload for <base64_encoded_string>:
Copy
```
{
 ExaunitProperties: [
  {name:requestId, value:27ac0ee3-0c72-4493-b02b-40038f07d2a0}, 
  {name:Operation, value:AddCluster},
  {name:TotalNumOfCoresForCluster, value:4},
  {name:TotalMemoryInGb, value:30},
  {name:StorageInTb, value:3},
  {name:OracleHomeDiskSizeInGb, value:60},
  {name:ClientNetwork, value:/root/root/1/ipnetwork1}, // Only if Higgs is also required
  {name:BackupNetwork, value:/root/root/1/ipnetwork2}, // Only if Higgs is also required
  {name:ExaUnitName, value:systemname},
  {name:CreateSparse, value:N},
  {name:BackupToDisk, value:N}
 ] 
}
```

#### Attributes
Name | Description  
---|---  
requestId |  Required: Optional  Type: String Unique UUID  
TotalNumOfCores ForCluster |  Required: Yes  Type: String The number of CPU cores that are allocated to the VM cluster. This is the total number of CPU cores that are allocated evenly across all of the compute nodes in the VM cluster. Must be a multiple of numComputes as returned by a call to ecra/endpoint/clustershapes.   
TotalMemoryInGb |  Required: Yes  Type: String The amount of memory (in GB) that is allocated to the VM cluster. This is the total amount of memory that is allocated evenly across all of the compute nodes in the VM cluster. Must be a multiple of numComputes as returned by a call to ecra/endpoint/clustershapes.   
StorageInTb |  Required: Yes  Type: String The total amount of Exadata storage (in TB) that is allocated to the VM cluster. This storage is allocated evenly from all of the Exadata Storage Servers.  
OracleHomeDiskSize InGb |  Required: Yes  Type: String The amount of local disk storage (in GB) that is allocated to each database server in the first VM cluster.   
## Modifying Exadata Instances 🔗 
This section covers how to add a cluster to an existing instance, reshape a cluster, and delete a cluster. 
[To add a cluster to an existing instance](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of AddCluster. 
In the following example, <domain> is the identity domain ID, <instanceId> and <serviceEntitlementId> are returned from iTAS serviceInstances, and <base64_encoded_string> is a base64 encoding of the payload following the example. 
Example payload for request:
Copy
```
POST /itas/<domain>/myservices/api/v1/operations HTTP/1.1
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "instanceId", 
     "value": "<instanceId>" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "<serviceEntitlementId>" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.customAttributes.EXAUNIT_ALLOCATIONS", 
     "value": "<base64_encoded_string>" 
    }, 
    { 
     "name": "requestPayload.customAttributes. MULTIVM_ENABLED", 
     "value": "true" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-UPDATE" 
   } 
  } 
 ] 
}
```

Payload for <base64_encoded_string>:
Copy
```
{
 ExaunitProperties: [
  {name:requestId, value:27ac0ee3-0c72-4493-b02b-40038f07d2a0}, 
  {name:Operation, value:AddCluster},
  {name:TotalNumOfCoresForCluster, value:4},
  {name:TotalMemoryInGb, value:30},
  {name:StorageInTb, value:3},
  {name:OracleHomeDiskSizeInGb, value:60},
  {name:ClientNetwork, value:/root/root/1/ipnetwork1}, // Only if Higgs is also required
  {name:BackupNetwork, value:/root/root/1/ipnetwork2}, // Only if Higgs is also required
  {name:ExaUnitName, value:Cluster2},
  {name:CreateSparse, value:N},
  {name:BackupToDisk, value:N}
 ] 
}
```

[To reshape a cluster](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of ReshapeCluster. 
In the following example, <domain> is the identity domain ID and <base64_encoded_string> is a base64 encoding of the payload following the example. 
Example payload for request:
Copy
```
POST /itas/<domain>/myservices/api/v1/operations HTTP/1.1
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "instanceId", 
     "value": "500076173" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.customAttributes.EXAUNIT_ALLOCATIONS", 
     "value": "<base64_encoded_string>" 
    }, 
    { 
     "name": "requestPayload.customAttributes. MULTIVM_ENABLED", 
     "value": "true" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-UPDATE" 
   } 
  } 
 ] 
}
```

Payload for <base64_encoded_string>:
Copy
```
{
 ExaunitProperties: [
  {name:requestId, value:27ac0ee3-0c72-4493-b02b-40038f07d2a0}, 
	{name:ExaunitID, value:1},		// From ecra/endpoint/exaservice/{serviceInstance}/resourceinfo
  {name:Operation, value:ReshapeCluster},
  {name:TotalNumOfCoresForCluster, value:10},
  {name:TotalMemoryInGb, value:10},
  {name:StorageInTb, value:4},
  {name:OhomePartitionInGB, value:100},
  {name:ClientNetwork, value:/root/root/1/ipnetwork1}, // Only if Higgs is also required
  {name:BackupNetwork, value:/root/root/1/ipnetwork2}  // Only if Higgs is also required
 ] 
}
```

**Important**
  * Only one attribute can be modified per Reshape request. The payload should contain only the modified attribute. Example:
```

{ExaunitProperties
:
[{name:Operation,value
:
ReshapeCluster},
{
name:ExaunitID,value:5
},{
name:TotalNumOfCoresForCluster
,
value:6}]
}
```

  * When doing a Reshape with the `OracleHomeDiskSizeInGb` attribute, use the name `OhomePartitionInGB`.
  * The value for `TotalNumOfCoresForCluster` must be a multiple of `numComputes` as returned by a call to `ecra/endpoint/clustershapes`. 
  * The value for `TotalMemoryInGb` must be a multiple of `numComputes` as returned by a call to `ecra/endpoint/clustershapes`. 


[To delete a cluster](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of DeleteCluster. 
In the following example, <domain> is the identity domain ID and <base64_encoded_string> is a base64 encoding of the payload following the example. 
Example payload for request:
Copy
```
POST /itas/<domain>/myservices/api/v1/operations HTTP/1.1 
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "instanceId", 
     "value": "500076173" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.size", 
     "value": "CUSTOM" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    }, 
    { 
     "name": "requestPayload.customAttributes.EXAUNIT_ALLOCATIONS", 
     "value": "<base64_encoded_string>" 
    }, 
    { 
     "name": "requestPayload.customAttributes. MULTIVM_ENABLED", 
     "value": "true" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-UPDATE" 
   } 
  } 
 ] 
}
```

Payload for <base64_encoded_string>:
Copy
```
{
 ExaunitProperties: [
  {name:requestId, value:27ac0ee3-0c72-4493-b02b-40038f07d202}, // Optional
	{name:ExaunitID, value:2},
  {name:Operation, value:DeleteCluster}
 ] 
}
```

## Deleting Exadata Instances 🔗 
This section covers how to delete Exadata instances. 
**Important** Delete all existing multi-VM clusters before deleting the Exadata instance. Following this guidance prevents the instance ending up in an invalid state.
[To delete an instance](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-DELETE. 
In the following example, <domain> is the identity domain ID. 
Example payload for request:
Copy
```
POST /itas/<domain>/myservices/api/v1/operations HTTP/1.1 
{ 
 "operationItems": [ 
  { 
   "attributes": [ 
    { 
     "name": "instanceId", 
     "value": "500076173" 
    }, 
    { 
     "name": "requestPayload.serviceEntitlementId", 
     "value": "500073421" 
    }, 
    { 
     "name": "requestPayload.serviceType", 
     "value": "Exadata" 
    } 
   ], 
    "operationItemDefinition": { 
    "id": "CIM-Exadata-CUSTOM-PRODUCTION-DELETE" 
   } 
  } 
 ] 
}
```

## Discovering Entitlements and Instances 🔗 
This section describes how to discover service entitlements and service instances. 
[To discover service entitlements](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Send the following request:
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceEntitlements?serviceDefinitionNames=Exadata
```

Example payload returned for this request: 
Copy
```
{
  "items": [
   {
    "id": "cesi-585927251",        // Unique ServiceEntitlementId
    "serviceDefinition": {
     "canonicalLink": "/itas/a517289/myservices/api/v1/serviceDefinitions/502579309",
     "id": "502579309",
     "name": "Exadata"         // The customer is entitled to use the Exadata Service
    },
    "status": "ACTIVE",
    ...
    "canonicalLink": "/itas/a517289/myservices/api/v1/serviceInstances/csi-585928949"
   }
  ...                       // More Service Entitlements could be displayed
  ],
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements",
 "hasMore": false,
 "limit": 25, 
 "offset": 0
}
```

Eligible Data Centers: 
Use:
```
/itas/<domain>/myservices/api/v1/serviceEntitlements/{ServiceEntitlementId}?expands=serviceInstancesEligibleDataCenters
```

where `{ServiceEntitlementId}` is a service entitlement ID such as `cesi-500074601`. This will provide additional information such as: 
Copy
```
 "serviceInstancesEligibleDataCenters": [
  {
   "id": "US001"
  }
 ],
```

[To discover service instances](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/managingexadatainstances.htm)
Send the following request:
Copy
```
GET /<domain>/myservices/api/v1/serviceInstances?serviceDefinitionNames=Exadata
```

Example payload returned for this request: 
Copy
```
{
  "items": [
   {
    "id": "csi-585928949",        // Unique ServiceInstanceId
    "serviceEntitlement": {
     "id": "cesi-585927251",     // Related ServiceEntitlementId   
     "canonicalLink": "/itas/a517289/myservices/api/v1/serviceEntitlements/cesi-585927251"
    },
    "serviceDefinition": {
     "canonicalLink": "/itas/a517289/myservices/api/v1/serviceDefinitions/502579309",
     "id": "502579309",
     "name": "Exadata"         // The customer is entitled to use the Exadata Service
    },
    ...
    "canonicalLink": "/itas/a517289/myservices/api/v1/serviceInstances/csi-585928949"
   }
  ...                       // More Service Entitlements could be displayed
  ],
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements",
 "hasMore": false,
 "limit": 25, 
 "offset": 0
}
```

Was this article helpful?
YesNo

