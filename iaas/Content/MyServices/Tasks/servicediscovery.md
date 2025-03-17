Updated 2023-01-04
# Service Discovery Use Case
This use case shows how you can get the list of your service entitlement IDs.
**Important** The My Services dashboard and APIs are deprecated. 
## Discover Current Service Entitlement IDs 🔗 
Many of the My Services API operations require you to specify the `serviceEntitlementId`. To get the list of all your service entitlement IDs, use the [GET ServiceEntitlements](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSServiceEntitlements/resource_MSServiceEntitlementsResource_get_GET) operation. This operation returns information that you can use to make more specific requests using the [Oracle Cloud My Services API.](https://docs.oracle.com/iaas/api/#/en/itas/latest/)
Example:
Copy
```
GET /itas/<domain>/myservices/api/v1/serviceEntitlements
```

**Note**
In the examples, <domain> is the identity domain ID. An identity domain ID can be either the _IDCS GUID_ that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the _Identity Domain name_ for a traditional Cloud Account.
Example payload returned for this request: 
Copy
```
{
   "items": [
     {
       "id": "cesi-511202718",             // Unique ServiceEntitlementId
       "purchaseEntitlement": {             // Purchase Entitlement is the entity bought by a customer
         "subscriptionId": "511203590",
         "id": "511203590",
         "canonicalLink": "/itas/<domain>/myservices/api/v1/purchaseEntitlements/511203590"
       },
       "serviceDefinition": {
         "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceDefinitions/500089778",
         "id": "500089778",
         "name": "Storage"              // The customer is entitled to use the Storage Service
       },
       "createdOn": "2017-12-20T16:23:23.326Z",
       "createdBy": "paul.smith@oracle.com",
       "modifiedOn": "2017-12-20T18:35:40.628Z",
       "modifiedBy": "paul.smith@oracle.com",
       "identityDomain": {               // Identity Domain to which the Service Entitlement is associated
         "id": "511203592",
         "name": "myenvironment",
         "displayName": "myenvironment"
       },
       "cloudAccount": {                // Cloud Account to which the Service Entitlement is associated
         "id": "cacct-be7475efc2c54995bc842d3379d35812",
         "name": "myenvironment",
         "canonicalLink": "/itas/<domain>/myservices/api/v1/cloudAccounts/cacct-be7475efc2c54995bc842d3379d35812"
       },
       "status": "ACTIVE",               // Current Status
       "serviceConfigurations": {            // Specific configuration information such as Exadata configuration
         "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-511202718/serviceConfigurations"
       },
       "canonicalLink": "/itas/{domain}/myservices/api/v1/serviceEntitlements/cesi-511202718"
     },
     {
       "id": "cesi-511202719",
       "purchaseEntitlement": {
         "subscriptionId": "511203590",
         "id": "511203590",
         "canonicalLink": "/itas/<domain>/myservices/api/v1/purchaseEntitlements/511203590"
       },
       "serviceDefinition": {
         "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceDefinitions/500123193",
         "id": "500123193",
         "name": "Compute"              // The customer is entitled to use the Compute Service
       },
       "createdOn": "2017-12-20T16:23:23.326Z",
       "createdBy": "paul.smith@oracle.com",
       "modifiedOn": "2017-12-20T18:35:40.628Z",
       "modifiedBy": "paul.smith@oracle.com",
       "identityDomain": {
         "id": "511203592",
         "name": "myenvironment",
         "displayName": "myenvironment"
       },
       "cloudAccount": {
         "id": "cacct-be7475efc2c54995bc842d3379d35812",
         "name": "myenvironment",
         "canonicalLink": "/itas/<domain>/myservices/api/v1/cloudAccounts/cacct-be7475efc2c54995bc842d3379d35812"
       },
       "status": "ACTIVE",
       "serviceConfigurations": {
         "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-511202719/serviceConfigurations"
       },
       "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements/cesi-511202719"
     },
     ...                         // More Service Entitlements could be displayed
   ],
 "canonicalLink": "/itas/<domain>/myservices/api/v1/serviceEntitlements",
 "hasMore": false,
 "limit": 25,
 "offset": 0
 }
```

[To obtain the IDCS GUID](https://docs.oracle.com/en-us/iaas/Content/MyServices/Tasks/servicediscovery.htm)
Go to the Users page in My Services dashboard and click **Identity Console**. The URL in the browser address field displays the IDCS GUID for your identity domain. For example:
Copy
```
https://idcs-105bbbdfe5644611bf7ce04496073adf.identity.oraclecloud.com/ui/v1/adminconsole/?root=users
```

In the above URL, `idcs-105bbbdfe5644611bf7ce04496073adf` is the IDCS GUID for your identity domain.
Was this article helpful?
YesNo

