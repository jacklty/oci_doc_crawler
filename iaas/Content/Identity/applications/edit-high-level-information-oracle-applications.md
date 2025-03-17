Updated 2025-01-14
# Editing High-Level Information for Oracle Applications
When you create an instance of an Oracle application in your identity domain, the application instance appears in the **Applications** page. As a Service Administrator, you can edit some of the high-level information for Oracle Applications. However, you can't edit attributes that are protected. Even in an editable attribute, you can't update certain values that were seeded by the system.
To view and edit high-level information about Oracle application, such as the application type, name, description, icon, URL, links, and whether the application appears on the **My Apps** page, select **Edit application**.
UI Elements | Attributes | Update Seeded Values | Add New Values  
---|---|---|---  
Description |  description | Yes | N/A  
Tags |  tags | No | Yes  
Allowed Scopes |  allowedScopes | No | Yes  
Allowed Tags |  allowedTags | No | Yes  
Redirect URL |  redirectUris | Yes | N/A  
Access Token Expiration |  accessTokenExpiry | Yes | N/A  
Refresh Token Expiration |  refreshTokenExpiry | Yes | N/A  
Scope |  scopes | No | Yes  
Secondary Audiences |  protectableSecondaryAudiences | No | Yes  
Is Refresh Token Allowed |  allowOffline | Yes | N/A  
Enforce Grants as Authorization |  allowAccessControl | N/A | N/A  
Trust Scope |  trustScope | N/A | N/A  
Activate |  active | N/A | N/A  
Not all attributes correspond to UI fields:
  * Web tier policy tab and all the UI fields within the tab are controlled and edited by one attribute `urn:ietf:params:scim:schemas:oracle:idcs:extension:webTierPolicy:App:webTierPolicyJson`.
  * `grantedAppRoles` attribute records each App Role defined by another application that has been granted to the client.
  * `signonPolicy` editable attribute indicates that you can assign Oracle Applications to Sign-On Policy.


**Note** You cannot change any of the fields other than the ones listed above for Oracle Public Cloud applications. You will encounter an error if you select **Save** after you try editing any of these values.
Apart from editing certain attributes, you can perform the following with Oracle Public Cloud Applications:
  * Edit only single scope. Bulk removal of scopes is not supported.
  * Grant client access to the IAM APIs
To enable your application to access IAM APIs, select **Add**.
In the **Add App Role** window, select the application roles that you want to assign to this application. This enables your application to access the REST APIs that each of the assigned application roles can access.
For example, select **Identity Domain Administrator** from the list. All REST API tasks available to the identity domain administrator will be accessible to your application.
You can't remove the following:
    * The assigned application roles from the application by selecting the **x** icon for the row of the required application role
    * The App Roles that were granted when an Oracle Public Cloud application was created because those seeded values are protected


Was this article helpful?
YesNo

