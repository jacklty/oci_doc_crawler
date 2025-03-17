Updated 2023-04-14
# Supported Header Value Expressions for Authentication Policies
When you configure enterprise application's authentication policies, you can add header variables to requests forwarded to the application, by selecting a user attribute from a list of predefined user attributes, or by entering an expression.
In the header **Value** field for Authentication Policies, you can provide a simple literal string or an attribute identifier instead of selecting the user attribute from the list. If you use an attribute identifier, App Gateway attempts to replace the attribute identifier by the value of the attribute after authentication happens.
The following types of attribute identifiers are supported by authentication policies:
  * **Application** : This attribute identifier accesses the information of the enterprise application registered in IAM.
Format: `$subject.client.<attr>`
  * **User** : This attribute identifier accesses information of the user signed in to IAM.
Format: `$subject.user.<attr>`
  * **Request** : This attribute identifier accesses request information. 
Format: `$request.<attr>`


For user attribute scope, App Gateway supports any simple top-level attribute in the JSON Response from `/admin/v1/Users` such as `string`, `boolean`, or `int` values.
App Gateway also supports user extension attributes as header value expressions for authentication policies, using the following format `$subject.user.urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:<attributeName>`, and custom attributes using the following format `$subject.user.urn:ietf:params:scim:schemas:idcs:extension:custom:User:<customAttributeName>`
Example of User Attribute Scope Names and Return Values Attribute Name |  Header Value Expression |  Description  
---|---|---  
Full Name |  `$subject.user.name` |  The user's full name.  
User Name |  `$subject.user.userName` |  The user's login username.  
Emails |  `$subject.user.emails` Other types of emails also supported: `$subject.user.emails.recovery`, `$subject.user.emails.other`, `$subject.user.emails.home`, and `$subject.user.emails.work`. |  The user's primary email address.  
Phone Numbers |  `$subject.user.phoneNumbers` Other types of phone numbers supported:`                       $subject.user.phoneNumbers.mobile`, `$subject.user.phoneNumbers.home`, and `$subject.user.phoneNumbers.work`. |  The user's phone number.  
Addresses |  `$subject.user.addresses` |  The user's mailing address.  
Groups |  `$subject.user.groups` |  A list of comma-separated group names to which the user is assigned to through direct or indirect membership.  
idcsCreatedBy |  `$subject.user.idcsCreatedBy` |  The display name of the user or application who created this resource.  
idcsLastModifiedBy |  `$subject.user.idcsLastModifiedBy` |  The display name of the user or application who modified this resource.  
Department |  `$subject.user.urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department` |  The user's department.  
Employee Number |  `$subject.user.urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber` |  The user's employee number.  
Example of supported values for request attribute scope:
Example of Request Attribute scope names and supported values Attribute Name |  Header Value Expression |  Description  
---|---|---  
policy_appname |  `$request.policy_appname` |  Returns the name of the enterprise application registered in IAM.  
policy_name |  `$request.policy_name` |  Returns the policy name of the specific policy matched for the request.  
policy_res |  `$request.policy_res` |  Returns the resource URL pattern matched for the request. The format is: "<type>:<pattern>" Example: `text:/my/resource` or `regex:/my/resource/.*`  
policy_action |  `$request.policy_action` |  Returns the HTTP Method (`GET`, `POST`, and so on) used to access the requested resource.  
res_host |  `$request.res_host` |  Returns the host name from the original Request.  
res_port |  `$request.res_port` |  Returns the port number from the original Request.  
res_type |  `$request.res_type` |  Returns the protocol (HTTP or HTTPS) of the original Request.  
res_url |  `$request.res_url` |  Returns the full requested URL.  
Was this article helpful?
YesNo

