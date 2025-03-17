Updated 2025-01-14
# Importing Using the REST API
This section provides example requests and responses when you want to import users, groups, and AppRoles into your environment using the identity domains REST API..
The following sections walk you through the steps:
  * [Import the CSV File to Storage](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__ImportTheCSVFileToStorage-3F97EBFF)
  * [Schedule the Job to Import the CSV File into Your Environment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__CreateTheScheduledJobToImportTheCSV-3F984404)
  * [Verify That the Job Was Successful](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__VerifyThatTheJobIsSuccessful-3F986154)
  * [Review the Job Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__ReviewTheJobReport-3F987990)
  * [When There Are Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__WhenThereAreErrors-3FFEAD0C)
  * [Replacing Existing Values to Complex Multi-Valued Attributes (CMVA)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__replaceCMVAAttributes)


**Note** To safely handle the import of the CSV file into an IAM identity domain, if any cell values are escaped to avoid CSV injection, the quotes are removed. For example, during import if the cell value is `'@test'`, the actual value will be `@test`.
  * At: `@`
  * Plus: `+`
  * Minus: `-`
  * Equals to: `=`
  * Pipe: `|`
  * Percentage: `%`


## Import the CSV File to Storage 🔗 
To import the CSV file to storage, send a POST request to the `/storage/v1/Files` endpoint.
**Note** See [Importing and Exporting Users, Groups, and AppRoles](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/BulkImportExport.htm#BulkImportExport "An identity domain might be one among many repositories in an organization. When you start using identity domains, you might want to load data from the other repositories. Bulk loading offers a solution to this requirement.") for more information on the CSV file.
Parameter | Description  
---|---  
`fileName` | Enter the name that you want the file to have when you save it to storage.  
`isPublic` | Indicates whether the file is private or public. Currently, only private files are supported. Set this value to `false.`  
`contentType` | Files are limited to a `contentType` of `text/csv` or `application/directory.`  
`file` | Enter the name of file that you want to upload.  
**Example Request**
```
$ curl
  -X POST
  -H "Authorization: Bearer <Access Token Value>"
  -H "Cache-Control: no-cache"
  -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
  -F "fileName=UsersImp1.csv"
  -F "contentType=text/csv"
  -F "isPublic=false"
  -F file=@"C:/examplefilelocation/Users1.csv" "https://<domainURL>/storage/v1/Files"
```

**Example Response**
**Note** Make note of the `fileName` value (bold in the example response).
```
{
  "fileName": "**files/201608261841/Users1.csv**",
  "isPublic": false,
  "fileUrl": "https://<domainURL>/v1/Storage-example2/90C63D43D7E226D7A8C5E9F8BF7A24291FA5876BDC413AF9F37A3D94B8A02C5F/files/201608261841/Users1.csv"
}
```

## Schedule the Job to Import the CSV File into Your Environment 🔗 
**Note**
To access the complete list of allowed CSV column names and their descriptions, use the following request: ```
GET <domainURL>/admin/v1/ResourceTypeSchemaAttributes?filter=resourceType eq "User" and idcsCsvAttributeName pr&attributes=name,idcsCsvAttributeName,idcsDisplayName,description,type,required,canonicalValues,mutability,caseExact,multiValued,idcsMinLength,idcsMaxLength,idcsSearchable
```

See [Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/overview.htm#overview "Import and export users, groups, and Oracle application roles into and out of an identity domain.") for more information on bulk loading using the identity domain Console.
To create a scheduled job, send a POST request to the `/job/v1/JobSchedules` endpoint. In the JSON example request body below, for resource specific `jobType` imports, the value for `jobType` can be `UserImport,` `GroupImport`, or `AppRoleImport`, depending on the type of data that you're trying to import.
There's also a generic import option available where the value for `jobType` is `Import`, and then the attribute `resourceType` is added and the values can be `User,` `Group`, or `Grant` (for AppRole), depending on the type of data that you're trying to import.
**Note** Use of the `resourceType` of `AppRole` for import isn't supported.
The examples below show both the resource specific `jobType` import and the generic import options.
**Example Request for Resource Specific jobType Import**
```
$ curl
-X POST
  -H "Content-Type: application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"
  -H "Cache-Control: no-cache" 
  -d '{
  "schemas": [
   "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
  ],
 "jobType": "**UserImport**",
  "runNow": true,
  "parameters": [
  {
   "name": "fileLocation",
   "value": "**files/201608261841/UsersImp1.csv**"
   },
  {
    "name": "fileType",
    "value": "csv"
   }
  ]
 }' "https://<domainURL>/job/v1/JobSchedules"
```

An additional parameter is required for the `AppRoleImport jobType:`
```
{
 "name": "appDisplayName",
 "value": "MyApp"
}
```

**Example Response for Resource Specific jobType Import**
**Note** Make note of the `id` value (bold in the example response). This is the value for the `jobScheduleid` that you specify in the next section.
```
{
 "id": "**ffecd68a-fc08-4177-8afc-84a1d523b911**",
 "jobType": "UserImport",
 "nextFireTime": "2022-08-26T18:42:19.883Z",
 "runAt": "2022-08-26T18:42:19.883Z",
 "parameters": [
  {
   "name": "fileLocation",
   "value": "files/201608261841/Users1.csv"
  },
  {
   "name": "fileType",
   "value": "csv"
  }
 ],
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
 ]
}
```

**Example Request for Generic Import**
```
$ curl
-X POST
  -H "Content-Type: application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"
  -H "Cache-Control: no-cache" 
  -d '{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
 ],
 "jobType": "**Import**",
 "runNow": true,
 "parameters": [
  {
   "name": "fileLocation",
   "value": "**files/201608261841/UsersImp1.csv**"
  },
  {
   "name": "fileType",
   "value": "csv"
  },
  {
   "name": "**resourceType**",
   "value": "**User**"
  }
 ]
}' "https://<domainURL>/job/v1/JobSchedules""
```

An additional parameter is required for the `Grant ResourceType:`
```
{
 "name": "appDisplayName",
 "value": "MyApp"
}
```

**Example Response for Generic Import**
**Note** Make note of the `id` value (bold in the example response). This is the value for the `jobScheduleid` that you specify in the next section.
```
{
 "id": "**ffecd68a-fc08-4177-8afc-84a1d523b911**",
 "jobType": "Import",
 "nextFireTime": "2022-08-26T18:42:19.883Z",
 "runAt": "2022-08-26T18:42:19.883Z",
 "parameters": [
  {
   "name": "fileLocation",
   "value": "files/201608261841/Users1.csv"
  },
  {
   "name": "fileType",
   "value": "csv"
  },
  {
   "name": "resourceType",
   "value": "User"
  }
 ],
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
 ]
}
```

## Verify That the Job Was Successful 🔗 
To verify that the import job succeeded, send a GET request to the `/job/v1/JobHistories` endpoint using `jobScheduleid` as the identifier.
**Example Request**
```
$  curl
  - X GET
  - H "Content-Type: application/json"
  - H "Authorization: Bearer Access Token Value"
  - H "Cache-Control: no-cache"
  "https://<domainURL>/job/v1/JobHistories?filter=jobScheduleid%20eq%20%22**ffecd68a-fc08-4177-8afc-84a1d523b911%22**"
```

**Example Response**
**Note** Make note of the `id` value (bold in the example response). This is the value for the `historyId` that you specify in the next section.
```
{{
 "schemas": [
  "urn:scim:api:messages:2.0:ListResponse"],
 "totalResults": 1,
 "Resources": [
  {
   "endTime": "2022-08-26T18:42:21.878Z",
   "jobType": "UserImport",
   "failureCount": 0,
   "successCount": 5,
   "percentage": 100,
   "status": "succeeded",
   "jobDisplayName": "User File Import Job",
   "startTime": "2022-08-26T18:42:19.883Z",
   "jobDisplayId": "44",
   "jobScheduleId": "ffecd68a-fc08-4177-8afc-84a1d523b911",
   "jobDescription": "A job for importing users into IDCS from a file",
   "instanceId": "qa1siteb-2105-jobsv1-114718228563211471822859774",
   "totalCount": 5,
   "id": "**2071a27f549843a48e00cadbb8f4364e**",
   "meta": {
    "created": "2022-08-26T18:42:19.973Z",
    "lastModified": "2022-08-26T18:42:21.889Z",
    "resourceType": "JobHistory",
    "location": "https://<domainURL>/job/v1/JobHistories/2071a27f549843a48e00cadbb8f4364e"
   },
   "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:JobHistory"
   ],
   "idcsCreatedBy": {
    "value": "3f461931ecde403c85bf367379b417d3",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/3f461931ecde403c85bf367379b417d3"
   },
   "idcsLastModifiedBy": {
    "value": "3f461931ecde403c85bf367379b417d3",
    "display": "admin opc",
    "type": "User",
    "$ref": "https://<domainURL>/admin/v1/Users/3f461931ecde403c85bf367379b417d3"
   }
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 50
}
```

## Review the Job Report 🔗 
To review the status of the import job, send a GET request to the `/job/v1/JobReports` endpoint using `historyId` as the identifier. If there are any failures in the import process, it lists those failures in the form of a CSV file in storage.
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
  "https://<domainURL>/job/v1/JobReports?filter=historyId%20eq%20%2071a27f549843a48e00cadbb8f4364e"
```

## When There Are Errors 🔗 
If you encounter errors during a bulk-load operation and you can't fix them by modifying the entries in the import file, you can set a diagnostics level to capture operational logs during the bulk-load operation. You can then view those logs to help you to determine the cause of the problem. See [Running the Diagnostic Data Report](https://docs.oracle.com/en-us/iaas/Content/Identity/reports/run-diagnostic.htm#run-diagnostic-report "Run a diagnostic data report for an IAM identity domain.") for more information.
If you encounter errors after a bulk-load operation, use the Jobs page to help you resolve the errors.
  1. Access the Jobs page by selecting **Jobs** in the Identity Cloud Service console.
  2. Select **View Details** for the failed job.
  3. Select **Export Errors,** and then download the exported error file.
  4. Open the comma-separated value error file using any .csv file manager, such as Microsoft Excel. The exported file contains all the failed rows, and the failure reason in the **Error Message** column.
  5. Correct the errors, and then remove the **Type** and **Error Message** columns from the file.
  6. Reimport the file.


See the [Viewing Jobs and Job Details](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/understand_jobs.htm#undertand_jobs "Review the status of all jobs, the details for a specific job, and export a list of the job errors for an identity domain in IAM.") for more information.
## Replacing Existing Values to Complex Multi-Valued Attributes (CMVA) 🔗 
When administrators update users by using Import, by default new values will be added to existing multivalued attributes.
For example, say that a user has set her work email to **alice@myservice.invalid**. Email is a multivalued attribute, and when an administrator imports a CSV file with the updated email value (for example **administrator@myservice.invalid**), the new email is added to the existing instance of email, and both the values are saved.
You can also update the email values. For example, to update the email value to **alice1@myservice.invalid** , pass the `replaceExistingMultiValuedValues` attribute when scheduling an Import job.
Sample JSON payload: ```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:JobSchedule"
 ],
 "jobType": "UserImport",
 "runNow": true,
 "parameters": [
  {
   "name": "fileLocation",
   "value": "files/202003260936/User.csv"
  },
  {
   "name": "fileType",
   "value": "csv"
  },
  {
   "name": "replaceExistingMultiValuedValues",
   "value": "true"
  }
 ]
}

```

## Viewing a User Import Job Report 🔗 
This section provides example requests and responses when you want to view a user import job report when you import users into your environment using the identity domains REST API.
### Example Request 🔗 
To review the user import job, send a GET request to the `/job/v1/UserImportJobReports` endpoint using `historyId` as the identifier.
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
"https://<domainURL>/job/v1/UserImportJobReports?filter=historyId eq "227ef1ba8068cf43409884ed96254575fa"
```

### Example Response
```
{
 "schemas": [
  "urn:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 9,
 "Resources": [{
   "idcsLastModifiedBy": {
    "type": "User",
    "value": "d8dfed8ecdcf4df0b3a02333ae47b0a5",
    "display": "file_import_export_testIdentityDomainAdmin file_import_export_testIdentityDomainAdmin",
    "$ref": "https://<domainURL>/admin/v1/Users/d8dfed8ecdcf4df0b3a02333ae47b0a5"
   },
   "idcsCreatedBy": {
    "type": "User",
    "display": "file_import_export_testIdentityDomainAdmin file_import_export_testIdentityDomainAdmin",
    "value": "d8dfed8ecdcf4df0b3a02333ae47b0a5",
    "$ref": "https://<domainURL>/admin/v1/Users/d8dfed8ecdcf4df0b3a02333ae47b0a5"
   },
   "type": "info",
   "historyId": "cb4069d9ca904a609807d743e7e177ca",
   "id": "2a25c3f4df9a4c21a95236675e5ea561",
   "jobType": "UserImport",
   "meta": {
    "created": "Apr 20, 2017 4:40:20 AM CDT",
    "lastModified": "Apr 20, 2017 4:40:20 AM CDT",
    "resourceType": "UserImportJobReport",
    "location": "https://<domainURL>/job/v1/UserImportJobReports/2a25c3f4df9a4c21a95236675e5ea561"
   },
   "message": "User Imported Successfully.",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:UserImport:JobReport": {
    "responseData": "{\"location\":\"https://<domainURL>/admin/v1/Users/1d7a37c58ff84efc96d75b2499f0441a\",\"method\":\"PATCH\",\"requestNumber\":\"6aafefea-ae2a-4e8d-a56e-6882524d4d54\",\"status\":\"200\"}",
    "requestData": "User ID=integ.usertsVooUEwqA,Password=,First Name=firstName1Changed,Middle Name=,Last Name=User001Changed,Honorific Prefix=Mr,Honorific Suffix=,Display Name=,Title=,Profile URL=,User Type=,Nick Name=,Preferred Language=en,Locale=en-US,TimeZone=America/Los_Angeles,Active=TRUE,Work Phone=121-123-2245,Mobile No=1111000000,Work Email=workEmailAdded@myservice.invalid,Home Email=homeEmailAdded@myservice.invalid,Work Street Address=Sec 127,Work City=DELHI,Work State=DEL,Work Postal Code=110065,Work Country=IN,Employee Number=56273,Organization=ST,Division=IDM,Department=IDCS,Cost Center=Noida,Manager Name=integ.usertQAWkZLGOb,Federated=FALSE,Primary Email Type=home",
    "status": "Update Succeeded",
    "email": "workEmailAdded@myservice.invalid",
    "lastName": "User001Changed",
    "firstName": "firstName1Changed",
    "userId": "integ.usertsVooUEwqA"
   },
   "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:JobReport",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:UserImport:JobReport"
   ]
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 48
}

```

## Viewing Group Import Job Reports 🔗 
This section provides example requests and responses when you want to view a group import summary job report and a group import detailed job report when you import groups into your environment using the identity domains REST API.
### Example Import Summary Job Request 🔗 
To review the group import summary job, send a GET request to the `/job/v1/GroupImportSummaryJobReports` endpoint using `historyId` as the identifier.
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
  "https://<domainURL>/job/v1/GroupImportSummaryJobReports?filter=historyId eq "99a693e0bc89421484f7d4dcb2193725"
```

### Example Import Summary Job Response
```
{
  "schemas": [
    "urn:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 6,
  "Resources": [
    {
      "idcsLastModifiedBy": {
        "type": "User",
        "value": "9df357a9767c499ab22b7808da07a722",
        "display": "file_import_export_testUserAdmin file_import_export_testUserAdmin",
        "$ref": "https://<domainURL>/admin/v1/Users/9df357a9767c499ab22b7808da07a722"
      },
      "idcsCreatedBy": {
        "type": "User",
        "display": "file_import_export_testUserAdmin file_import_export_testUserAdmin",
        "value": "9df357a9767c499ab22b7808da07a722",
        "$ref": "https://<domainURL>/admin/v1/Users/9df357a9767c499ab22b7808da07a722"
      },
      "type": "info",
      "historyId": "99a693e0bc89421484f7d4dcb2193725",
      "id": "76d122a2e68c436ea195e5d8077c248a",
      "jobType": "GroupImport",
      "meta": {
        "created": "Apr 20, 2017 4:58:56 AM CDT",
        "lastModified": "Apr 20, 2017 4:58:56 AM CDT",
        "resourceType": "GroupImportSummaryJobReport",
        "location": "https://<domainURL>/job/v1/GroupImportSummaryJobReports/76d122a2e68c436ea195e5d8077c248a"
      },
      "message": "-",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:groupImportSummary:JobReport": {
        "failRows": 0,
        "description": "This row is checked for re entrant quality",
        "displayName": "RandomGroupgMVlqkMewc",
        "succRows": 1,
        "failMembers": 0,
        "succMembers": 2,
        "totalMembers": 2
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:JobReport",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:groupImportSummary:JobReport"
      ]
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 48
}
```

### Example Import Detailed Job Request
To review the group import detailed job, send a GET request to the `/job/v1/GroupImportDetailedJobReports` endpoint using `historyId` as the identifier.
```
  curl
  -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
"https://<domainURL>/job/v1/GroupImportDetailedJobReports?filter=historyId eq "99a693e0bc89421484f7d4dcb2193725"
```

### Example Import Detailed Job Response
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
        "value": "9df357a9767c499ab22b7808da07a722",
        "display": "file_import_export_testUserAdmin file_import_export_testUserAdmin",
        "$ref": "https://<domainURL>/admin/v1/Users/9df357a9767c499ab22b7808da07a722"
      },
      "idcsCreatedBy": {
        "type": "User",
        "display": "file_import_export_testUserAdmin file_import_export_testUserAdmin",
        "value": "9df357a9767c499ab22b7808da07a722",
        "$ref": "https://<domainURL>/admin/v1/Users/9df357a9767c499ab22b7808da07a722"
      },
      "type": "info",
      "historyId": "99a693e0bc89421484f7d4dcb2193725",
      "id": "c76c5cc346d2461a89ecb66db9473a1e",
      "jobType": "GroupImport",
      "meta": {
        "created": "Apr 20, 2017 4:58:55 AM CDT",
        "lastModified": "Apr 20, 2017 4:58:55 AM CDT",
        "resourceType": "GroupImportDetailedJobReport",
        "location": "https://<domainURL>/job/v1/GroupImportDetailedJobReports/c76c5cc346d2461a89ecb66db9473a1e"
      },
      "message": "Group Imported Successfully.",
      "urn:ietf:params:scim:schemas:oracle:idcs:extension:groupImportDetailed:JobReport": {
        "description": "Employee Group5",
        "displayName": "RandomGroupfuJLZurEaY",
        "responseData": "{\"location\":\"https://<domainURL>/admin/v1/Groups/d44507d5747a46ea9fbf861cfd00549f\",\"method\":\"POST\",\"requestNumber\":\"a7655f03-cc86-4d22-9c7e-e9b398690775\",\"bulkId\":\"a7655f03-cc86-4d22-9c7e-e9b398690775\",\"status\":\"201\"}",
        "requestData": "Display Name=RandomGroupfuJLZurEaY,Description=Employee Group5,User Members=Gusty_HMtvdP.Rob@example.com;gusty_xputur.rob@example.com",
        "status": "Creation Succeeded",
        "members": "Gusty_HMtvdP.Rob@example.com;gusty_xputur.rob@example.com"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:JobReport",
        "urn:ietf:params:scim:schemas:oracle:idcs:extension:groupImportDetailed:JobReport"
      ]
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 48
}
```

## Viewing AppRole Membership Import Job Reports 🔗 
This section provides example requests and responses when you want to view an AppRole membership import summary job report and an AppRole membership import detailed job report when you import AppRole memberships into your environment using the identity domains REST API.
### Example Import Summary Job Request 🔗 
To review the AppRole membership import summary job, send a GET request to the `/job/v1/AppRoleMembershipImportSummaryJobReports` endpoint using `historyId` as the identifier.
```
  curl -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
"https://<domainURL>/job/v1/AppRoleMembershipImportSummaryJobReports? filter=historyId eq "258a235de81b4704bcbd1c03fb08d33b"
```

### Example Import Summary Job Response
```
{
 "schemas": [
  "urn:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 1,
 "Resources": [{
   "idcsLastModifiedBy": {
    "type": "User",
    "value": "2eee19172d154fd6a99a9761b158e469",
    "display": "file_import_export_testAppAdmin file_import_export_testAppAdmin",
    "$ref": "https://<domainURL>/admin/v1/Users/2eee19172d154fd6a99a9761b158e469"
   },
   "idcsCreatedBy": {
    "type": "User",
    "display": "file_import_export_testAppAdmin file_import_export_testAppAdmin",
    "value": "2eee19172d154fd6a99a9761b158e469",
    "$ref": "https://<domainURL>/admin/v1/Users/2eee19172d154fd6a99a9761b158e469"
   },
   "type": "info",
   "historyId": "258a235de81b4704bcbd1c03fb08d33b",
   "id": "d3c46c37cb5b49d9a431a3cb5503e57a",
   "jobType": "AppRoleImport",
   "meta": {
    "created": "Apr 13, 2017 5:38:44 AM CDT",
    "lastModified": "Apr 13, 2017 5:38:44 AM CDT",
    "resourceType": "AppRoleMembershipImportSummaryJobReport",
    "location": "https://<domainURL>/job/v1/AppRoleMembershipImportSummaryJobReports/d3c46c37cb5b49d9a431a3cb5503e57a"
   },
   "message": "-",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:AppRoleMembershipImportSummary:JobReport": {
    "succRows": 9,
    "failRows": 0,
    "AppRoleName": "JCSAppRoleEfHxHW",
    "appDisplayName": "JCSEfHxHW",
    "totalMembers": 9,
    "succUserMembers": 5,
    "failUserMembers": 0,
    "succGroupMembers": 4,
    "failGroupMembers": 0
   },
   "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:JobReport",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:AppRoleMembershipImportSummary:JobReport"
   ]
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 48
}
```

### Example Import Detailed Job Request
To review the AppRole membership import detailed job, send a GET request to the `/job/v1/AppRoleMembershipImportDetailedJobReports` endpoint using `historyId` as the identifier.
```
  curl -X GET
  -H "Authorization: Bearer <AccessToken>"
  -H "Cache-Control: no-cache"
"https://<domainURL>/job/v1/AppRoleMembershipImportDetailedJobReports?filter=historyId eq "22258a235de81b4704bcbd1c03fb08d33b"
```

### Example Import Detailed Job Response
```
{
 "schemas": [
  "urn:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 9,
 "Resources": [{
   "idcsLastModifiedBy": {
    "type": "User",
    "value": "2eee19172d154fd6a99a9761b158e469",
    "display": "file_import_export_testAppAdmin file_import_export_testAppAdmin",
    "$ref": "https://<domainURL>/admin/v1/Users/2eee19172d154fd6a99a9761b158e469"
   },
   "idcsCreatedBy": {
    "type": "User",
    "display": "file_import_export_testAppAdmin file_import_export_testAppAdmin",
    "value": "2eee19172d154fd6a99a9761b158e469",
    "$ref": "https://<domainURL>/admin/v1/Users/2eee19172d154fd6a99a9761b158e469"
   },
   "type": "info",
   "historyId": "258a235de81b4704bcbd1c03fb08d33b",
   "id": "18452ef094be484491e8df9777ab4437",
   "jobType": "AppRoleImport",
   "meta": {
    "created": "Apr 13, 2017 5:38:44 AM CDT",
    "lastModified": "Apr 13, 2017 5:38:44 AM CDT",
    "resourceType": "AppRoleMembershipImportDetailedJobReport",
    "location": "https://<domainURL>/job/v1/AppRoleMembershipImportDetailedJobReports/18452ef094be484491e8df9777ab4437"
   },
   "message": "AppRole Membership Imported Successfully.",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:AppRoleMembershipImportDetailed:JobReport": {
    "memberType": "Group",
    "status": "Creation Succeeded",
    "member": "TestCvAwSWGroup1",
    "AppRoleDisplayName": "JCSAppRoleEfHxHW",
    "requestData": "Entitlement Value=JCSAppRoleEfHxHW,Grantee Name=TestCvAwSWGroup1,Grantee Type=Group",
    "responseData": "{\"location\":\"https://<domainURL>/admin/v1/Grants/7ce75f5132e44e5c91f1e8ef76521778\",\"method\":\"POST\",\"requestNumber\":\"23f0330e-c84b-40ec-b939-a40066c8b659\",\"bulkId\":\"23f0330e-c84b-40ec-b939-a40066c8b659\",\"status\":\"201\"}"
   },
   "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:JobReport",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:AppRoleMembershipImportDetailed:JobReport"
   ]
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 48
}
```

Was this article helpful?
YesNo

