Updated 2024-04-05
# Using the Audit Event APIs
Identity domains Audit Events REST endpoints enable you to get Audit logs covering significant events, changes, or actions. Using these APIs, you can integrate all Security Information and Event Management (SIEM), User and Entity Behavior Analytics (UEBA), and Cloud Access Security Broker (CASB) to poll Audit data.
**Note**
Identity domains AuditEvents and certain reports templates in the Reports APIs will stop returning new data after December 15, 2024. Instead, you can use the [OCI Audit service](https://docs.oracle.com/iaas/Content/Audit/home.htm) to get this data. To view service change announcements for IAM, see Service Change Announcements for [IAM](https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm#servicechanges_topic_IAM).
Audit events enable you to review the actions performed by members of your organization using details provided by the Audit logs, such as who performed the action and what the action was. Identity domains is the central point of control for all activities happening in the system. It generates audit data in response to all administrator and end-user operations, such as User Login, Application Access, Password Reset, User Profile Update, CRUD operations on Users, Group, Applications, and so on.
**Note** Audit event-related dates and times use the Coordinated Universal Time (UTC) format: YYYY-MM-DDThh:mm:ss.mscZ. For example, 2022-03-24T10:24:24.022Z.
Comprehensive reports can be generated from many administrator and user activities, such as those on the left side of the diagram. Represented on the right side are examples of the historical user activity that you can capture and the statistics and analytics that you can generate by importing data into analytics tools.
**Audit Examples**
Audit examples are available to help get you up to speed. After you import the collection, type "audit" in the filter to find all the audit requests. Download the identity domains authentication use case examples collection and the global variables file from the **idcs-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
**Identity Domains Audit Events**
This table provides Event IDs of some of the most crucial events in identity domains.
Event Category | Event | Event ID  
---|---|---  
Single Sign-On |  User Logins Success |  `sso.session.create.success`  
Single Sign-On |  User Logins Failure |  `sso.authentication.failure`  
Application Access Events |  Application Access Success |  `sso.app.access.success`  
Application Access Events |  Application Access Failure |  `sso.app.access.failure`  
Multifactor Authentication |  Step-up authentication for User  |  `sso.auth.factor.initiated`  
Multifactor Authentication |  ByPass Code Creation |  `sso.bypasscode.create.success`  
Multifactor Authentication |  ByPass Code Deletion |  `sso.bypasscode.delete.success`  
Self-Registration |  User Self-Registration success |  `admin.me.register.success`  
Self-Service Access Request |  Access Request Success |  `admin.myrequest.create.success`  
Notifications |  Notification Delivery success |  `notification.delivery.success`  
Notifications |  Notification Delivery Failure |  `notification.delivery.failure`  
Identity Bridge Sync |  ID Bridge Sync Success |  `idbridge.sync.success`  
Identity Bridge Sync |  ID Bridge Sync Failure |  `idbridge.sync.failure`  
Forgot/Reset Password |  Password Reset success |  `admin.me.password.reset.success`  
Reset Password Initiated by Administrator |  Password Reset success |  `admin.user.password.reset.success`  
Change Password |  Password Change Success |  `admin.me.password.change.success`  
Change Password |  Password Change Failure |  `admin.me.password.change.failure`  
User CRUD Operations |  User Create Success |  `admin.user.create.success`  
User CRUD Operations |  User Activate Success |  `admin.user.activated.success`  
User CRUD Operations |  User Update Success |  `admin.user.update.success`  
User CRUD Operations |  User Delete Success |  `admin.user.delete.success`  
Group CRUD Operations |  Group Create Success |  `admin.group.create.success`  
Group CRUD Operations |  Group Update Success |  `admin.group.update.success`  
Group CRUD Operations |  Group Delete Success |  `admin.group.delete.success`  
Group CRUD Operations |  Group Membership Assignment |  `admin.group.add.member.success`  
Group CRUD Operations |  Group Membership Removal |  `admin.group.remove.member.success`  
Application CRUD Operations |  Application Create |  `admin.app.create.success`  
Application CRUD Operations |  Application Update |  `admin.app.update.success`  
Application CRUD Operations |  Application Delete |  `admin.app.delete.success`  
User Provisioning |  Successful User Provisioning |  `admin.account.create.success`  
User Provisioning |  Unsuccessful User Provisioning |  `admin.account.delete.success`  
**Event Resources**
The following table describes crucial event resources.
Event Resource | Description  
---|---  
eventID |  Event ID as defined by the identity domains components  
actorName |  Username (login name) from the security context  
actorDisplayName |  User display name from the security context  
actorId |  User GUID from the security context  
actorType |  The actor type, either User or Client  
ssoSessionId |  Cloud SSO identifier  
ssoIdentityProvider |  SSO Identity Provider  
ssoAuthFactor |  The Authentication Factor used for authentication  
ssoApplicationId |  Application identifier GUID  
ssoApplicationType |  SSO Application Type: Application Type indicates whether the application is an OPC or a NonOPC application and whether the type is SAML, OAuth, or Secure Form Fill based on the protocol.  
clientIp |  IP address of the client application that's making the request  
ssoUserAgent |  User's device information  
ssoPlatform |  Platform used to perform authentication  
ssoProtectedResource |  Protected resource URI (Resource host, port, and context)  
ssoMatchedSignOnPolicy |  Matched Sign-On Policy, added in version18.1.2  
Message |  Message for event-specific success or failure  
Timestamp |  Timestamp of when the event occurred  
## Audit Schema
You can find the Audit Schema using the identity domains REST API. The Audit Schema contains all the information discussed in the tables of this use case.
**Example Request**
Perform a GET on the `/Schemas` endpoint using the `AuditEvent` schema.
```
GET <domainURL>>/admin/v1/Schemas/urn:ietf:params:scim:schemas:oracle:idcs:AuditEvent
```

**Example Response Snapshot**
The following is a snapshot of the response.
```
{
  "attributes": [
    {
      "caseExact": false,
      "description": "Unique URI of the schema",
      "idcsDisplayName": "ID",
      "idcsSearchable": true,
      "multiValued": false,
      "mutability": "readOnly",
      "name": "id",
      "required": true,
      "returned": "always",
      "type": "string",
      "uniqueness": "global"
    },
    {
      "caseExact": false,
      "description": "An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.",
      "idcsDisplayName": "External ID",
      "idcsSearchable": false,
      "multiValued": false,
      "mutability": "readWrite",
      "name": "externalId",
      "required": false,
      "returned": "default",
      "type": "string",
      "uniqueness": "none"
    },
    {
      "caseExact": true,
      "description": "Event correlation ID (ECID) correlating a chain of events as belonging to the same business operation (root task). ECID is generated when the request enters the IDCS web tier.",
      "idcsDisplayName": "Execution Context Id",
      "idcsSearchable": true,
      "multiValued": false,
      "mutability": "readWrite",
      "name": "ecId",
      "required": false,
      "returned": "default",
      "type": "string",
      "uniqueness": "none"
    },
    {
      "caseExact": true,
      "description": "Relationship Identifier (RID). This value indicates the position of a particular event/sub-operation within the tree of tasks that begins with the root task.",
      "idcsDisplayName": "Relationship Id",
      "idcsSearchable": true,
      "multiValued": false,
      "mutability": "readWrite",
      "name": "rId",
      "required": false,
      "returned": "default",
      "type": "string",
      "uniqueness": "none"
    },
    {
      "caseExact": false,
      "description": "Timestamp of when the event occurred, provided by the Event Manager (not supplied by clients)",
      "idcsDisplayName": "Timestamp",
      "idcsSearchable": true,
      "multiValued": false,
      "mutability": "readWrite",
      "name": "timestamp",
      "required": false,
      "returned": "default",
      "type": "dateTime",
      "uniqueness": "none"
    },
```

Was this article helpful?
YesNo

