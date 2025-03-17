Updated 2023-01-04
# Exadata Use Cases
**Important** The My Services dashboard and APIs are deprecated. 
The following use case examples can get you started working with the Exadata operations available in the [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/).
**Important** These procedures are for use with Oracle Database Exadata Database Service on Cloud@Customer **ONLY**. For more information, see [Administering Oracle Database Exadata Cloud at Customer](https://docs.oracle.com/en/cloud/cloud-at-customer/exadata-cloud-at-customer/exacc/get-started-this-service.html). These procedures **DO NOT** apply to the Exadata Cloud Service available in Oracle Cloud Infrastructure.
## Exadata Firewall Allowlisting 🔗 
To enable access to your Exadata Cloud Service instance, you can configure security rules and associate them with your instance. The security rules define an allowlist of allowed network access points.
The firewall provides a system of rules and groups. By default, the firewall denies network access to the Exadata Cloud Service instance. When you enable a security rule, you enable access to the Exadata Cloud Service instance. To enable access you must:
  * Create a security group and create security rules that define specific network access allowances.
  * Assign the security group to your Exadata Cloud Service instance.


You can define multiple security groups, and each security group can contain multiple security rules. You can associate multiple security groups with each Exadata Cloud Service instance, and each security group can be associated with multiple Exadata Cloud Service instances. You can dynamically enable and disable security rules by modifying the security groups that are associated with each Exadata Cloud Service instance.
To enable access to an Exadata Cloud Service instance:
**Note**
In the following examples, <domain> is the identity domain ID. An identity domain ID can be either the _IDCS GUID_ that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the _Identity Domain name_ for a traditional Cloud Account.
  1. Get the service instance IDs.
Operation: [GET ServiceInstances](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSServiceInstances/resource_MSServiceInstancesResource_get_GET)
Example 
Example request: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances?serviceDefinitionNames=Exadata&statuses=ACTIVE
```

Example payload returned for this request: 
Copy
```
{
 "items": [
  {
   "id": "csi-585928949",        // Unique ServiceInstanceId
   "serviceEntitlement": {
   "id": "cesi-585927251",
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-585927251"
  },
  "serviceDefinition": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceDefinitions/502579309",
   "id": "502579309",
   "name": "Exadata"        // The customer is entitled to use the Exadata Service
  },
  "cloudAccount": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/cloudAccounts/cacct-fd7a122448aaaa", 
   "id": "cacct-fd7a122448aaaa", 
   "name": "myAccountName"
  },
  ...
  "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949"
 }
...                       // More Service Instances could be displayed
 ],
"canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances",
"hasMore": false,
"limit": 25, 
"offset": 0
}
```

This example payload returns the service instance ID csi-585928949, which is part of the service entitlement ID cesi-585927251. 
  2. Get the service configuration IDs. 
Operation: [GET SIServiceConfigurations](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSIServiceConfiguration/resource_MSSIServiceConfigurationResource_get_GET)
Example 
Example request, using the service instance ID csi-585928949: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations
```

Example payload returned for this request: 
Copy
```
{
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations", 
 "items": [
  {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata", 
   "exadata": {
   "bursting": {
    "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/bursting"
   }, 
   "id": "Exadata", 
   "securityGroupAssignments": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments"
   }
  }, 
  "id": "Exadata"
  }
 ]
}
```

This example payload shows that /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments is used for Exadata Firewall.
  3. Get the current security groups for the service entitlement.
Operation: [GET SEExadataSecurityGroups](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSEExadataSecurityGroups/resource_MSSEExadataSecurityGroupsResource_get_GET)
Example 
Example request, using the service entitlement ID cesi-585927251: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-585927251/serviceConfigurations/Exadata/securityGroups
```

Example payload returned for this request: 
Copy
```
{
 "items": [
  {
   "id": "1",
   "customerId": "585927251",
   "name": "SecGroup 1",
   "description": "My first Security group",
   "version": 10,
   "rules": [
    {
     "direction": "ingress",
     "proto": "tcp",
     "startPort": 1159,
     "endPort": 1159,
     "ipSubnet": "0.0.0.0/0",
     "ruleInterface": "data"
    }
   ],
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/585927251/serviceConfigurations/Exadata/securityGroups/1"
  },
  {
   "id": "2",
   "customerId": "585927251",
   "name": " SecGroup 2",
   "description": "My second Security group",
   "version": 3,
   "rules": [
    {
     "direction": "egress",
     "proto": "tcp",
     "startPort": 8123,
     "endPort": 8123,
     "ipSubnet": "192.168.1.0/28",
     "ruleInterface": "data"
    }
   ],
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/585927251/serviceConfigurations/Exadata/securityGroups/2"
  }
 ],
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/585927251/serviceConfigurations/Exadata/securityGroups"
}
```

This example payload shows two security groups defined for the specified service entitlement ID. 
  4. Get the current security group assignments for the service instance 
Operation: [GET SIExadataSecurityGroupAssignments](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSEExadataSecurityGroups/resource_MSSEExadataSecurityGroupsResource_get_GET)
Example 
Example request, using the service instance ID csi-585928949: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments
```

Example payload returned for this request: 
Copy
```
{
 "items": [
  {
   "id": "11",
   "securityGroup": 
   {
    "id": "1",
    "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/585927251/serviceConfigurations/Exadata/securityGroups/1"
   },
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments/11"
  }
 ],
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments"
}
```

This example payload shows one security group assigned to the service instance csi-585928949. 
  5. Create a security group with security rules.
Operation: [POST SEExadataSecurityGroups](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSEExadataSecurityGroups/resource_MSSEExadataSecurityGroupsResource_post_POST)
Example 
Example request, using the service entitlement ID cesi-585927251: 
Copy
```
POST /itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-585927251/serviceConfigurations/Exadata/securityGroups
{
  "customerId": "585927251",     
  "name": "SecGroup 1",       
  "description": "My third Security group",
  "version": 1,
  "rules": [
   {
    "direction": "ingress",    
    "proto": "tcp",        
    "startPort": 30,        
    "endPort": 31,         
    "ipSubnet": "100.100.100.255", 
    "ruleInterface": "admin"   
   },
   {
    "direction": "egress",
    "proto": "tcp",
    "startPort": 32,
    "endPort": 32,
    "ipSubnet": "100.100.255.0/16",
    "ruleInterface": "admin"
   }
  ]
}
```

Attributes:
Name | Description  
---|---  
customerId |  Required: Yes  String This must be the same as the <serviceEntitlementId>  
direction |  Required: Yes  String Allowed values: [ingress | egress] for inbound or outbound.  
proto |  Required: Yes  String Allowed values: [tcp | udp].  
startPort |  Required: Yes  Integer startPort defines the beginning of a range of ports to open/white-list [0 - 65535].  
endPort |  Required: Yes  Integer endPort defines the ending of a range of ports to open/white-list [0 - 65535].  
ipSubnet |  Required: Yes  String Single IP address or range specified in CIDR notation.  
ruleInterface |  Required: Yes  String Allowed values: [admin | client | backup] where:
     * admin — specifies that the rule applies to network communications over the administration network interface. The administration network is typically used to support administration tasks by using terminal sessions, monitoring agents, and so on.
     * client — specifies that the rule applies to network communications over the client access network interface, which is typically used by Oracle Net Services connections.
     * backup — specifies that the rule applies to network communications over the backup network interface, which is typically used to transport backup information to and from network-based storage that is separate from Exadata Cloud Service.  
If successful, the POST request will return the unique ID of the newly created security group. For the next step, we'll assume that the newly created security group ID is 3. 
**Note** A security group can also be modified or deleted. See [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/). 
  6. Assign the security group to a service instance.
Operation: [POST SIExadataSecurityGroupAssignments](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSIExadataSecurityGroupAssignments/resource_MSSIExadataSecurityGroupAssignmentsResource_post_POST)
Example 
Example request, using the service instance csi-585928949 and the security group ID 3:
Copy
```
POST /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments 
{
  "securityGroup": {
   "id": "3", 
   "customerId": "585927251",
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/585927251/serviceConfigurations/Exadata/securityGroups/3"
  }
}
```

Attributes:
Name | Description  
---|---  
customerId |  Required: Yes String This must be the same as the serviceEntitlementId.  
If successful, the POST request will return the unique Id of the newly created security group assignment. 
**Note** A security group assignment can also be deleted. See [Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/). 
You can now verify all your security groups and assignments. See: 
     * [Get the current security groups for the service entitlement](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/Exadatausecases.htm#firewall__GetCurrentSecurityGroups).
     * [Get the current security group assignments for the service instance](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/Exadatausecases.htm#firewall__GetCurrentSecurityGroupAssignments).


[To obtain the IDCS GUID](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/Exadatausecases.htm)
Go to the Users page in My Services dashboard and click **Identity Console**. The URL in the browser address field displays the IDCS GUID for your identity domain. For example:
Copy
```
https://idcs-105bbbdfe5644611bf7ce04496073adf.identity.oraclecloud.com/ui/v1/adminconsole/?root=users
```

In the above URL, `idcs-105bbbdfe5644611bf7ce04496073adf` is the IDCS GUID for your identity domain.
## Exadata Scaling with Bursting 🔗 
You can temporarily modify the capacity of your Exadata environment by configuring bursting. Bursting is a method you can use to scale Exadata Cloud Service non-metered instances within an Exadata system.
To scale up your non-metered instances, increase the number of compute nodes by modifying the `burstOcpu` attribute of the host. When you no longer need the additional nodes, update the `burstOcpu` attribute back to its original setting.
**Note**
In the following examples, <domain> is the identity domain ID. An identity domain ID can be either the _IDCS GUID_ that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the _Identity Domain name_ for a traditional Cloud Account.
  1. Get the service instance IDs. 
Operation: [GET ServiceInstances](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSServiceInstances/resource_MSServiceInstancesResource_get_GET)
Example 
Example request: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances?serviceDefinitionNames=Exadata&statuses=ACTIVE
```

Example payload returned for this request: 
Copy
```
{
 "items": [
  {
   "id": "csi-585928949",        // Unique ServiceInstanceId
   "serviceEntitlement": {
   "id": "cesi-585927251",
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-585927251"
  },
  "serviceDefinition": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceDefinitions/502579309",
   "id": "502579309",
   "name": "Exadata"        // The customer is entitled to use the Exadata Service
  },
  "cloudAccount": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/cloudAccounts/cacct-fd7a122448aaaa", 
   "id": "cacct-fd7a122448aaaa", 
   "name": "myAccountName"
  },
  ...
  "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949"
 }
...                       // More Service Instances could be displayed
 ],
"canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances",
"hasMore": false,
"limit": 25, 
"offset": 0
}
```

This example payload returns the service instance ID csi-585928949. 
  2. Get the service configuration IDs. 
Operation: [GET SIServiceConfigurations](https://docs.oracle.com/iaas/api/#/en/itas/latestMSSIServiceConfigurations/resource_MSSIServiceConfigurationsResource_get_GET)
Example 
Example request, using the service instance ID csi-585928949: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations
```

Example payload returned for this request: 
Copy
```
{
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations", 
 "items": [
  {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata", 
   "exadata": {
   "bursting": {
    "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/bursting"
   }, 
   "id": "Exadata", 
   "securityGroupAssignments": {
   "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments"
   }
  }, 
  "id": "Exadata"
  }
 ]
}
```

This example payload shows that /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/securityGroupAssignments is used for Bursting.
  3. Get the current compute node configuration.
Operation: [GET SIExadataBursting](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSIExadataBursting/resource_MSSIExadataBurstingResource_get_GET)
Example 
Example request, using the service instance ID csi-585928949: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/bursting
```

Example payload returned for this request: 
Copy
```
{ 
  "ocpuOpInProgress": false,
  "exaunitId": 50,
  "ocpuAllocations": [
    {
     "hostName": "host1.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 0,                // Current Burst value
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0
    },
    {
     "hostName": "host2.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 0,                // Current Burst value
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0
    }
    ],
  "status": 200,
  "op": "exaunit_coreinfo",
  "additionalNumOfCores": "0", 
  "additionalNumOfCoresHourly": "0",
  "coreBursting": "Y"
}
```

  4. Modify the values for `burstOcpu`. 
Operation: [PUT SIExadataBursting](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSIExadataBursting/resource_MSSIExadataBurstingResource_put_PUT)
You can modify `burstOcpu` to a value that is up to the value of `maxBurstOcpu`. This example adds two compute nodes to each host. 
Example 
Example request, using the service instance csi-585928949:
Copy
```
PUT /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/bursting/
{
  "ocpuOpInProgress": false,
  "exaunitId": 50,
  "ocpuAllocations": [
    {
     "hostName": "host1.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 2,
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0    
    },
    {
     "hostName": "host2.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 2,
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0    
    }  
    ]
}
```

Attributes:
Name | Description  
---|---  
burstOcpu |  Required: Yes Type: Integer, Minimum Value: 0, Maximum Value: maxBurstOcpu Number of additional cores  
**Note** This action may take a few minutes to complete. 
  5. Verify the new compute node configuration. 
Operation: [GET SIExadataBursting](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSSIExadataBursting/resource_MSSIExadataBurstingResource_get_GET)
Example 
Example request, using the service instance ID csi-585928949: 
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceInstances/csi-585928949/serviceConfigurations/Exadata/bursting
```

Example payload returned for this request: 
Copy
```
{ 
  "ocpuOpInProgress": false,
  "exaunitId": 50,
  "ocpuAllocations": [
    {
     "hostName": "host1.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 2,           // New Burst value
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0    
    },
    {
     "hostName": "host2.oraclecloud.com",
     "subscriptionOcpu": 11,
     "meteredOcpu": 0,
     "burstOcpu": 2,           // New Burst value
     "minOcpu": 11,
     "maxOcpu": 42,
     "maxBurstOcpu": 11,
     "maxSubOcpu": 38,
     "maxMetOcpu": 0    
    }
    ],
  "status": 200,
  "op": "exaunit_coreinfo",
  "additionalNumOfCores": "0", 
  "additionalNumOfCoresHourly": "0",
  "coreBursting": "Y"
}
```



[To obtain the IDCS GUID](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/Exadatausecases.htm)
Go to the Users page in My Services dashboard and click **Identity Console**. The URL in the browser address field displays the IDCS GUID for your identity domain. For example:
Copy
```
https://idcs-105bbbdfe5644611bf7ce04496073adf.identity.oraclecloud.com/ui/v1/adminconsole/?root=users
```

In the above URL, `idcs-105bbbdfe5644611bf7ce04496073adf` is the IDCS GUID for your identity domain.
Was this article helpful?
YesNo

