Updated 2024-12-18
# Working with Apps
Use cases in this section provide the steps to grant AppRoles to an App, and also provide example requests to create and activate OAuth Apps. Each use case also provides the required App attributes.
This section contains the following topics:
  * [Grant AppRoles to an App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm#GrantAppRoleToApp "Use the following example to create a request that grants application roles to an App.")
  * [Create and Activate an OAuth Resource Server App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CreateActivateOAuthRSApp.htm#CreateActivateOAuthRSApp "This section provides example requests to create and activate an OAuth Resource Server using the identity domains REST API.")
  * [Create and Activate an OAuth Client App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CreateActivateOAuthClientApp.htm#CreateActivateOAuthClientApp "This section provides example requests to create and activate an OAuth Client App using the identity domains REST API.")
  * [Create and Activate a SAML App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CreateActivteSAMLApp.htm#CreateActivteSAMLApp "This section provides example requests to create and activate a Security Assertion Markup Language \(SAML\) App using the REST APIs.")
  * [Enabling Forced Reauthentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/enabling-forced-reauthentication.htm#enabling_forced_reauthentication "To force a user to reauthenticate while accessing an application, even if a valid OCI IAM session is available, set forceReauthenticateAfterInMinutes using the REST API endpoint.")


## Grant AppRoles to an App 🔗 
Use the following example to create a request that grants application roles to an App.
The example includes the following steps: 
  * [Step 1: Identify the AppRole](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm#GrantAppRoleToApp__Step_IdentifyAppRole)
  * [Step 2: Retrieve the details](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm#GrantAppRoleToApp__Step_RetrieveDetails)
  * [Step 3: Grant the AppRole](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm#GrantAppRoleToApp__Step_GrantAppRole)
  * [Step 4: Retrieve the details again](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm#GrantAppRoleToApp__Step_RetrieveDetailsAgain)


### Step 1: Identify the AppRole 🔗 
Identify the AppRole that you want to assign.
```
GET HOST/admin/v1/AppRoles?filter=app.value eq "IDCSAppId"
{
 "displayName": "User Administrator",
 "id": "...",
 "uniqueName": "IDCSAppId_User Administrator",
 "app": {
  "name": "IDCSApp",
  "value": "IDCSAppId",
  "display": "IDCS Application",
  "$ref": "..."
 },
}
```

### Step 2: Retrieve the details 🔗 
Retrieve the details of the target app.
```
GET {{HOST}}/admin/v1/Apps?filter=displayName eq "target-appname"
{
  "displayName": "target-appname",
  "id": "...",
  "grantedAppRoles": [
   {
     "value": "...",
     "$ref": "...",
     "appId": "IDCSAppId",
     "display": "User Administrator",
     "type": "direct",
     "appName": "IDCSApp",
     "adminRole": true
   },
   {
     "value": "...",
     "$ref": "...",
     "appId": "IDCSAppId",
     "display": "Identity Domain Administrator",
     "type": "direct",
     "appName": "IDCSApp",
     "adminRole": true
   }
]
```

### Step 3: Grant the AppRole 🔗 
Grant the AppRole to an app.
```
POST {{HOST}}/admin/v1/Grants
{
  "grantee": {
    "type": "App",
    "value": "..." <------- "id" of the app/grantee that the AppRole will be assigned to.
  },
  "app": {
    "value": "IDCSAppId" <------- the AppId to be assigned to the App.
  },
  "entitlement" : {
    "attributeName": "appRoles",
    "attributeValue": "..." <---- the "id" of the AppRole e.g, IDA
  },
  "grantMechanism" : "ADMINISTRATOR_TO_APP",
  "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:Grant"]
}
```

### Step 4: Retrieve the details again 🔗 
Retrieve the details of the target app again.
```
GET {{HOST}}/admin/v1/Apps?filter=displayName eq "target-appname"
{
  "displayName": "target-appname",
  "id": "...",
  "grantedAppRoles": [
   {
     "value": "...",
     "$ref": "...",
     "appId": "IDCSAppId",
     "display": "User Administrator",
     "type": "direct",
     "appName": "IDCSApp",
     "adminRole": true
   },
   {
     "value": "...",
     "$ref": "...",
     "appId": "IDCSAppId",
     "display": "Identity Domain Administrator",
     "type": "direct",
     "appName": "IDCSApp",
     "adminRole": true
   }
]
```

Was this article helpful?
YesNo

