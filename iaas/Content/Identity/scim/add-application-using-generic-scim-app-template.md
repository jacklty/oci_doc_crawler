Updated 2025-01-14
# Adding an Application Using the Generic SCIM App Template
Add an application to an OCI IAM identity domain using the Generic SCIM App Template.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select **Add application** , and then select **Application Catalog** and select **Launch app catalog**.
  4. In the **Types of integration** section, select **Provisioning** , choose one of the following templates:
**Note** Enter `GenericScim` in the search field to make it easier to find the template you want.
     * **GenericScim - Basic:** A Generic SCIM Template for SCIM interfaces that support basic authentication.
     * **GenericScim - Bearer Token:** A Generic SCIM Template for SCIM interfaces that support JWT tokens submitted as an authorization bearer.
     * **GenericScim - Client Credentials:** A Generic SCIM Template for SCIM interfaces that support client credentials for authentication.
     * **GenericScim - Resource Owner Password:** A Generic SCIM Template for SCIM interfaces that support the resource owner grant type.
  5. Select the template, and in the **Add application details** page for the template page, provide a name and description for your application, and then select **Next** to go to the Configure provisioning page.
  6. Use the following table to populate the fields of the **Configure connectivity** section. The fields available depend on the template type.
Parameter | Description and Value Information | Additional Information  
---|---|---  
**Host Name** |  The host name of your application's SCIM REST API endpoints. If the SCIM interface's URL is `https://api.example.com/scimgate/Users`, then the host name is `api.example.com`. | This parameter appears in the UI for all Generic SCIM App Templates.  
**Base URI** |  The base relative URL of your application's SCIM REST API. For example, if the SCIM interface's URL is `https://api.example.com/scimgate/Users`, then the Base URI is `/scimgate`. | This parameter appears in the UI for all Generic SCIM App Templates.  
**Administrator Username** |  The administrator's user name for your API authentication service. This value is sent as part of the body message of each request to your application's SCIM REST API. Format: Plain text. | This parameter appears in the UI for the **GenericScim - Basic** and **GenericScim - Resource owner password** templates.  
**Administrator Password** |  The administrator's password for your API authentication service. This value is sent as part of the body message of each request to your application's SCIM REST API. Format: Password type. | This parameter appears in the UI for the **GenericScim - Basic** and **GenericScim - Resource owner password** templates.  
**HTTP Operation Types** |  By default, the template request uses the `PATCH HTTP` operation for any user's update operation. If your SCIM interface uses the `PUT HTTP` operation for user attribute updates, then use this field following this example. Example: `__ACCOUNT__.Update=PUT` | This parameter appears in the UI for all Generic SCIM App Templates.  
**Access Token** |  The value of the access token to be used by the template when communicating with your application's SCIM REST API. Format: Password type. | This parameter appears in the UI for the **GenericScim - Bearer token** template.  
**Client Id** |  The client ID for your API authentication service. Format: Plain text. | This parameter appears in the UI for the **GenericScim - Client credentials** and **GenericScim - Resource owner password** templates.  
**Client Secret** |  The client secret for your API authentication service. Format: Plain text. | This parameter appears in the UI for the **GenericScim - Client credentials** and **GenericScim - Resource owner password** templates.  
**Scope** |  The scope for your application. Example: `https://www.example.com/auth/adm.direct.group https://www.example.com/auth/admin.direct.user` | This parameter appears in the UI for the **GenericScim - Client credentials** and **GenericScim - Resource owner password** templates.  
**Authentication Server Url** |  The URL of your authentication service. Example: `https://api.example.com/oauth2/v1/token` | This parameter appears in the UI for the **GenericScim - Client credentials** and **GenericScim - Resource owner password** templates.  
**Custom Authentication Headers** |  Used to send extra static header values to your API authentication service. Example: `Basic authorization base64encodedusernamepassword` | This parameter appears in the UI for the **GenericScim - Client Credentials** and **GenericScim - Resource owner password** templates.  
**Port Number** |  The port number of your application's SCIM REST API endpoints. The default port number for this parameter is `443`. For example, if the URL is `https//api.example.com:6355/scimgate/Users`, then set the port number value to `6355`. | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**SSL Enabled** |  If your application's SCIM REST API endpoints don't require SSL, then set the value of this parameter to `false`. Default value: `true` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**JSON Resource Tag** |  The name of the attribute used in JSON messages when your application's SCIM REST API returns multiple resources. The default value is `Resources`. For example, if the response message of the user for the `GET` operation is: ```
{ 
 "users": [ 
 {user1}, {user2} 
 ] 
}
```
then change the value to `users`. | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**UID Attributes** |  The mapping between the `__UID__` (guid) internal attribute and your application's SCIM attribute for user and group object classes. Default value: `["Users=id", "Groups=id"]` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Name Attributes** |  The mapping between the `__NAME__` internal attribute and your application's SCIM attribute for user and group object classes. Default value: `["Users=userName", "Groups=displayName"]` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Status Attributes** |  The mapping between the `__ENABLE__` (status) internal attribute and your application's SCIM attribute for the user object class. Default value: `Users=active` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Password Attributes** |  Your application's SCIM REST API attribute that corresponds to the user's password. The attribute is used for masking the password attribute in the log files. Default value: `Users=password` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Date Attributes** |  The list of date attributes available for your application's SCIM REST API. Example: `Users=meta.lastModified,joiningDate` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Date Format** |  The date-and-time format of the date attributes available for your application's SCIM REST API. Example: `MMM d, yyyy h:mm:ss a z` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Content Type** |  The content-type header that your application's SCIM REST API expects IAM to send as a header HTTP request. Default value: `application/scim+json` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Accept Type** |  The content-type header that is expected as an HTTP response from your application's SCIM REST API. Default value: `application/scim+json` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Custom Headers** |  Used to send extra static header values to the SCIM REST API endpoints of your application. Format: `<headerName1>=<value>,<headerName2>=<value>` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**SCIM Version** |  The version of your application's SCIM REST API. Default value:`13`. The range for this attribute varies from `1` to `19`. | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**OClass Mapping** |  Used to map an attribute of one object class to an attribute of another object class. For example, if the **groups** attribute of the `__ACCOUNT__` object class must be mapped to the `__GROUP__` object class, then enter `__ACCOUNT__.groups=__GROUP__`. | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Default Batch Size** |  The default page or batch size for the `GET` operation. Default value: `200` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
**Managed Object Classes** |  The classification type of the schemas that your application must manage. Default value: `["Users", "Groups"]` | You can't update the value for this parameter in the UI. To update this parameter value, use the REST APIs.  
  7. After populating the fields, select **Test connectivity** to verify whether IAM can communicate with your application's SCIM REST API endpoints.
If a successful connection can be established, then a **Connection successful.** message appears.
If you receive an error message, check the values that you provided, and then select **Test connectivity** again. If the problem persists, then contact your system administrator.
Before testing, you can save the application and use REST APIs to update the parameter values that don't appear in the UI. After updating the parameter values, open the application again using the Console, and then select **Test connectivity**.


Was this article helpful?
YesNo

