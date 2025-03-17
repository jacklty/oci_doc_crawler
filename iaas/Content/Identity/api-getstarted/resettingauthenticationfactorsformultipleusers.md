Updated 2024-07-09
# Resetting Authentication Factors for Multiple Users Using The Bulk Endpoint
You can use the Bulk endpoint to reset the authentication factors for up to 40 users at a time using a POST call.
## Sample Request
```
curl
-X POST
-H "Content-Type:application/scim+json"
-H "Authorization: Bearer <Access_Token>"
https://<domainURL>/admin/v1/Bulk
```

## Sample Payload
```
{
  "schemas": [
   "urn:ietf:params:scim:api:messages:2.0:BulkRequest"
  ],
  "Operations": [
   {
     "method": "POST",
     "path": "/AuthenticationFactorsRemover",
     "bulkId": "<bulkid1>",
     "data": {
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorsRemover"
      ],
      "user":
{        "value": "<user_1_id>"       }
     }
   },
   {
     "method": "POST",
     "path": "/AuthenticationFactorsRemover",
     "bulkId": "<bulkid2>",
     "data": {
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorsRemover"
      ],
      "user":
{        "value": "<user_2_id>"       }
     }
   }
  ]
}

```

Was this article helpful?
YesNo

