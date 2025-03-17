Updated 2024-04-02
# Exporting Using the REST API
This section provides example requests and responses when you want to export users, groups, and AppRoles from your environment into another identity domain using the identity domains REST API.
The following sections walk you through the steps:
  * [Schedule the Export Job](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ScheduleTheExportJob-3FFF2CA7)
  * [View Job Details](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ViewJobDetails-40007695)
  * [View the Job Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ViewJobReport-40010B63)
  * [Download the File](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__DownloadTheFile-400160A5)


**Note** To safely handle the export of the CSV file from an identity domain, any cell values that start with the following characters are escaped. This ensures that if a cell value starts with one of these blocklisted values, it's escaped in the CSV, which avoids CSV injection. For example, during export if the value is `@test`, the actual value will be `'@test'`.
  * At: `@`
  * Plus: `+`
  * Minus: `-`
  * Equals to: `=`
  * Pipe: `|`
  * Percentage: `%`


## Schedule the Export Job 🔗 
**Note**
To access the complete list of allowed CSV column names and their descriptions, use the following request: ```
GET <domainURL>/admin/v1/ResourceTypeSchemaAttributes?filter=resourceType eq "User" and idcsCsvAttributeName pr&attributes=name,idcsCsvAttributeName,idcsDisplayName,description,type,required,canonicalValues,mutability,caseExact,multiValued,idcsMinLength,idcsMaxLength,idcsSearchable
```

See [Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/overview.htm#overview "Import and export users, groups, and Oracle application roles into and out of an identity domain.") for more information on bulk loading using the identity domain Console.
To export users, groups, or AppRoles, send a POST request to the `/job/v1/JobSchedules` endpoint and use the payload provided in the example request. In the JSON example request body below, for resource specific `jobType` exports, the value for `jobType` can be `UserExport,` `GroupExport`, or `AppRoleExport`, depending on the type of data that you're trying to export.
There's also a generic export option available where the value for `jobType` is `Export`, and then the attribute `resourceType` is added and the values can be `User,` `Group`, or `AppRole`, depending on the type of data that you're trying to export.
**Note** Export AppRole memberships to only a single application. Exporting across multiple applications exports the membership of various AppRoles across all applications.
The examples below show both the resource specific `jobType` export and the generic export options.
**Example Request for Resource-Specific jobType Export**
```
  curl
  -X POST
  -H "Authorization: Bearer <AccessToken>"
  -H "Content-Type: application/scim+json"
  -H "Cache-Control: no-cache"
-d '{
 "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"],
 "jobType": "UserExport",
 "runNow": true,
 "parameters": [
  {
   "name": "exportFormat",
   "value": "CSV"
  },
  {
   "name": "attributesToExclude",
   "value": "userName, profileUrl"
  }
 ]
}'
"https://<domainURL>/job/v1/JobSchedules"
```

**Example Response for Resource-Specific jobType Export**
**Note** Make note of the `id` value (bold in the example response). This is the value for the `jobScheduleid` that you specify in the next section.
```
{
  "id": "**fc565f0f-9555-4a44-803f-c06fe1d5d325**",
  "jobType": "UserExport",
  "nextFireTime": "2022-08-12T15:27:28.057Z",
  "runAt": "2022-08-12T15:27:28.057Z",
  "parameters": [
    {
      "name": "exportFormat",
      "value": "CSV"
    },
    {
      "name": "attributesToExclude",
      "value": "userName, profileUrl"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
  ]
}
```

**Example Request for Generic Export**
```
  curl
  -X POST
  -H "Authorization: Bearer <AccessToken>"
  -H "Content-Type: application/scim+json"
  -H "Cache-Control: no-cache"
-d '{
 "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"],
 "jobType": "Export",
 "runNow": true,
 "parameters": [
  {
   "name": "exportFormat",
   "value": "CSV"
  },
  {
			"name": "attributesToGet",
			"value": "userName,name,emails"
		},
  {
   "name": "resourceType",
   "value": "User"
  }
 ]
}'
"https://<domainURL>/job/v1/JobSchedules"
```

**Example Response for Generic Export**
**Note** Make note of the `id` value (bold in the example response). This is the value for the `jobScheduleid` that you specify in the next section.
```
{
 "id": "**9cc824a6-87df-4831-8d2b-6cb524384733**",
 "isDisabled": false,
 "jobType": "**Export**",
 "nextFireTime": "Apr 21, 2017 3:44:11 AM CDT",
 "runAt": "Apr 21, 2017 3:44:11 AM CDT",
 "parameters": [
  {
   "name": "exportFormat",
   "value": "CSV"
  },
  {
   "name": "attributesToGet",
   "value": "userName,name,emails"
  },
  {
   "name": "resourceType",
   "value": "User"
  }
 ],
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
 ],
 "meta": {
  "resourceType": "JobSchedule",
  "location": "https://<domainURL>/job/v1/JobSchedules"
 }
}
```

## View Job Details 🔗 
To view details from the export job, send a GET request to the `/job/v1/JobHistories` endpoint using the `jobScheduleid` as the identifier.
**Example Request**
```
  curl
-X GET
  -H "Authorization: Bearer <AccessToken>"
"https://<domainURL>/job/v1/JobHistories?filter=jobScheduleid%20eq%20%229cc824a6-87df-4831-8d2b-6cb524384733%22"
```

**Example Response**
**Note** Make note of the `id` value (bold in the example response). This is the value for the job `historyId` that you specify in the next section.
```
{
 "idcsLastModifiedBy": {
  "type": "User",
  "value": "ed39884ad56b42ae91d80b8db57251dc",
  "display": "admin opc",
  "$ref": "https://<domainURL>/admin/v1/Users/ed39884ad56b42ae91d80b8db57251dc"
 },
 "idcsCreatedBy": {
  "type": "User",
  "display": "admin opc",
  "value": "ed39884ad56b42ae91d80b8db57251dc",
  "$ref": "https://<domainURL>/admin/v1/Users/ed39884ad56b42ae91d80b8db57251dc"
 },
 "percentage": 100,
 "id": "**d17135ee4d2a4c2e8d7e29eccb7c4f71**",
 "jobScheduleId": "9cc824a6-87df-4831-8d2b-6cb524384733",
 "meta": {
  "created": "Apr 21, 2017 3:44:11 AM CDT",
  "lastModified": "Apr 21, 2017 3:44:12 AM CDT",
  "resourceType": "JobHistory",
  "location": "https://<domainURL>/job/v1/JobHistories/d17135ee4d2a4c2e8d7e29eccb7c4f71"
 },
 "jobDescription": "An Oracle Identity Cloud Service job to export User.",
 "failureCount": 0,
 "status": "succeeded",
 "scheduled": "Apr 21, 2017 3:44:11 AM CDT",
 "jobDisplayName": "User Export Job",
 "totalCount": 1,
 "instanceId": "afd082996a7b14927604199281492760419777",
 "successCount": 1,
 "startTime": "Apr 21, 2017 3:44:11 AM CDT",
 "jobType": "Export",
 "runNow": true,
 "endTime": "Apr 21, 2017 3:44:12 AM CDT",
 "parameters": [{
   "name": "exportFormat",
   "value": "CSV"
  }, {
   "name": "attributesToGet",
   "value": "userName,name,emails"
  }, {
   "name": "resourceType",
   "value": "User"
  }
 ],
 "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:JobHistory"]
}
```

## View the Job Report 🔗 
To view the job report for the export job, send a GET request to the `/job/v1/JobReports` endpoint using the job `historyId` as the identifier.
**Example Request**
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
"https://<domainURL>/job/v1/JobReports?filter=historyId%20eq%20%22d17135ee4d2a4c2e8d7e29eccb7c4f71%22"
```

**Example Response**
**Note** Make note of the `name` value (bold in the example response). This is the value for the `fileName` that you specify in the next section.
```
{
  "schemas": [
    "urn:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 1,
  "Resources": [
    {
      "idcsLastModifiedBy": {
        "type": "User",
        "value": "ed39884ad56b42ae91d80b8db57251dc",
        "display": "admin opc",
        "$ref": "https://<domainURL>/admin/v1/Users/ed39884ad56b42ae91d80b8db57251dc"
      },
      "idcsCreatedBy": {
        "type": "User",
        "display": "admin opc",
        "value": "ed39884ad56b42ae91d80b8db57251dc",
        "$ref": "https://<domainURL>/admin/v1/Users/ed39884ad56b42ae91d80b8db57251dc"
      },
      "type": "info",
      "historyId": "d17135ee4d2a4c2e8d7e29eccb7c4f71",
      "id": "9c1a12081ed04aeeaa9dd480c5f39094",
      "jobType": "Export",
      "meta": {
        "created": "Apr 21, 2017 3:44:12 AM CDT",
        "lastModified": "Apr 21, 2017 3:44:12 AM CDT",
        "resourceType": "JobReport",
        "location": "https://<domainURL>/job/v1/JobReports/9c1a12081ed04aeeaa9dd480c5f39094"
      },
      "message": "fileName",
      "name": "files/export/201704210844/Export_d17135ee4d2a4c2e8d7e29eccb7c4f71.csv",
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:JobReport"
      ]
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 1
}
```

## Download the File 🔗 
To download the file from the server, send a GET request to the `/storage/v1/Files` endpoint using the `fileName` as the identifier.
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Content-Type: multipart/form-data"
  -H "Cache-Control: no-cache"
"https://<domainURL>/storage/v1/Files?fileName=export/201704210844/Export_d17135ee4d2a4c2e8d7e29eccb7c4f71.csv"
```

Was this article helpful?
YesNo

