Updated 2024-04-02
# Importing and Exporting Users, Groups, and AppRoles
An identity domain might be one among many repositories in an organization. When you start using identity domains, you might want to load data from the other repositories. Bulk loading offers a solution to this requirement. 
Bulk loading automates the process of loading a large amount of data into an identity domain. You can bulk load users, groups, and application roles using the identity domains REST API or the UI. See [Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/overview.htm#overview "Import and export users, groups, and Oracle application roles into and out of an identity domain.") for more information on bulk loading using the identity domain Console.
**Note** To safely handle the export of the CSV file from an identity domain, any cell values that start with the following characters are escaped. This ensures that if a cell value starts with one of these blocklisted values, it's escaped in the CSV, which avoids CSV injection. For example, during export if the value is `@test`, the actual value will be `'@test'`.
  * At: `@`
  * Plus: `+`
  * Minus: `-`
  * Equals to: `=`
  * Pipe: `|`
  * Percentage: `%`

During import, if any cell values are escaped, the quotes are removed. For example, during import if the cell value is `'@test'`, the actual value will be `@test`.
Operation | Description | Administrator Role Required | More Information  
---|---|---|---  
Import Groups | Create groups, modify existing groups, and assign users to groups. |  The identity domain administrator has permissions to trigger the resource-specific job `GroupImport`, and Generic Import for the `resourceType` of `Group.` The user administrator has permissions to trigger the resource-specific job `GroupImport.` |  The maximum number of rows in group import file must not exceed 100,000 and import file size must not exceed 52 MB.  For best performance, ensure that maximum number of user members per group row in your CSV file doesn't exceed seven.   
Import Users | Create users and modify existing users. |  The identity domain administrator has permissions to trigger resource-specific job `UserImport`, and Generic Import for the `resourceType` of `User.` The user administrator has permissions to trigger the resource-specific job `UserImport.` |  The maximum number of rows in user import file must not exceed 100,000 and import file size must not exceed 52 MB You can include a password in unhashed plain text or in hashed format. Identity domains use {PBKDF2-HMAC-SHA256} by default for hashing passwords that are provided as a plain text value. Identity domains support the following crypto algorithms for user import:
  * {PBKDF2-HMAC-SHA1}
  * {PBKDF2-HMAC-SHA256}
  * {PBKDF2-HMAC-SHA384}
  * {PBKDF2-HMAC-SHA512}
  * {SSHA}
  * {SSHA256}
  * {SSHA384}
  * {SSHA512}

**Example Hashed Password** : ```
{PBKDF2-HMAC-SHA1}10000$T78t/00uHfSr95 czOvVufNLEfkwyBJKdZ0w3bV4wxIg/nb4pvTzvzA==
```
See [Create a User](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-users-post.html) for details on how to generate a hashed password value. If you want users to use their federated accounts to sign in, then you must set the **Federated** column to `TRUE` for those users. When the federated flag is set to `TRUE`, IAM no longer manages the federated user's password. This prevents IAM from forcing a password change for these imported user accounts. If you don't want users to be notified that the identity domain created accounts for them, then you must set the **ByPass Notification** column to `TRUE` for those users. The ByPass Notification flag controls whether an email notification is sent after creating or updating a user.  
Import Application Role Memberships | Assign users and groups to application roles. |  The identity domain administrator has permissions to trigger the resource-specific job `AppRoleImport` and Generic Import for the `resourceType` of `Grant.` The application administrator has permissions to trigger the resource-specific job `AppRoleImport.` |  Use of the `resourceType` of `AppRole` for import isn't supported. The maximum number of rows in Application Role Memberships import file must not exceed 100,000 and import file size must not exceed 52 MB.  
Export Groups | Export groups and group membership. |  The identity domain administrator has permissions to trigger the resource-specific job `GroupExport`, and Generic Export for the `resourceType` of `Group.` The user administrator has permissions to trigger the resource-specific job `GroupExport.`  
Export Users | Export users. |  The identity domain administrator has permissions to trigger the resource-specific job `UserExport`, and Generic Export for the `resourceType` of `User.` The user administrator has permissions to trigger the resource-specific job `UserExport.`  
Export Application Role Memberships | Export AppRole memberships. |  The identity domain administrator has permissions to trigger the resource-specific job `AppRoleExport` and Generic Export for the `resourceType` of `AppRole.` The application administrator has permissions to trigger the resource-specific job `AppRoleExport.` | Export AppRole memberships to only a single application. Exporting across multiple applications exports the membership of various AppRoles across all applications.  
**Download the Template**
Use the following link to download the `bulkImportSampleFilesCSV.zip` file: [Download the Templates.](http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/idcs/UI_Help_Files/bulkImportSampleFilesCSV.zip) The `bulkImportSampleFilesCSV.zip` file contains CSV templates for importing users `(Users.csv)`, groups `(Groups.csv)`, and AppRoles `(AppRoleMembership.csv)` to an identity domain.
There are many columns provided in the templates. For example, the **Federated** column (which supports either TRUE or FALSE) indicates whether to mark users that are created as federated. The **ByPass Notification** column (which supports either TRUE or FALSE), indicates whether an email notification is sent after creating or updating a user. 
**Note**
To access the complete list of allowed CSV column names and their descriptions, use the following request: ```
GET <domainURL>/admin/v1/ResourceTypeSchemaAttributes?filter=resourceType eq "User" and idcsCsvAttributeName pr&attributes=name,idcsCsvAttributeName,idcsDisplayName,description,type,required,canonicalValues,mutability,caseExact,multiValued,idcsMinLength,idcsMaxLength,idcsSearchable
```

See [Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/overview.htm#overview "Import and export users, groups, and Oracle application roles into and out of an identity domain.") for more information on bulk loading using the identity domain console.
**Example Response**
```
{
  "name": "customerId",
  "mutability": "readWrite",
  "idcsMinLength": 5,
  "type": "string",
  "idcsSearchable": true,
  "idcsDisplayName": "Customer ID",
  "description": "Customer Identification Number",
  "idcsMaxLength": 30,
  "multiValued": false,
  "required": false,
  "caseExact": true,
  "idcsCsvAttributeName": "Customer ID"
}
```

**More Information**
  * See [Importing Using the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing "This section provides example requests and responses when you want to import users, groups, and AppRoles into your environment using the identity domains REST API..") for the use case on importing user, group, and app role data using the identity domains REST API.
  * See [Exporting Using the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting "This section provides example requests and responses when you want to export users, groups, and AppRoles from your environment into another identity domain using the identity domains REST API.") for the use case on exporting user, group, and approve data using the identity domains REST APIs.


Was this article helpful?
YesNo

