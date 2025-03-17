Updated 2023-06-02
# Supported Operations
Manage user resources in SCIM applications in an OCI IAM identity domain.
`User` is a type of resource in the SCIM specification. To manage this resource, the SCIM gateway must expose REST API endpoints to enable operations such as creating, searching for, updating, and deleting users. The HTTP request for the operation that you want to perform and the HTTP response from that operation must be in a `JSON` format.
You can implement the following user operations:
User Operation | Description | HTTP Operation | HTTP Endpoint  
---|---|---|---  
Create a User | Create a user account in your custom application. |  `POST` |  `https://app.example.com/scimgate/Users`  
Search Users | Obtain a list of all users with their attributes that are in your custom application. |  `GET` |  `https://app.example.com/scimgate/Users`  
Search a User | Retrieve information about a specific user and their attributes in your custom application. |  `GET` |  `https://app.example.com/scimgate/Users/<id>`  
Update a User Attribute | Update an attribute value of a user account in your custom application. |  `PUT` |  `https://app.example.com/scimgate/Users/<id>`  
Delete a User | Remove a user account from your custom application. |  `DELETE` |  `https://app.example.com/scimgate/Users/<id>`  
Was this article helpful?
YesNo

