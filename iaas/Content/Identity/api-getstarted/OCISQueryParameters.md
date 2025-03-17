Updated 2024-04-02
# Query Parameters
You can include query parameters in requests to the identity domains REST API. These parameters are useful for finding resources with specific attributes or attribute values, and for sorting and paginating the output.
## About Query Parameters 🔗 
Using a query, you can filter the output to:
**Note** Query filtering capabilities depend on the REST service. REST services without SCIM might not support the advanced filtering and parameters that you want to use.
  * List only resources containing specified attributes or having specified values for attributes.
  * Limit the attributes returned in the response body.
  * Sort the output on a specified attribute, in ascending or descending order.
  * Limit the number of resources returned.
  * Specify where, in the list of resources in the collection, to start the request.


Query parameters are typically used with search methods:
  * GET: For filtering search results. See [Query Parameters With GET](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISQueryParameters.htm#OCISQueryParameters__QueryParametersWithGET-600D3359).
  * POST: For filtering search results using the parameters in the Request body (for security reasons). See [Query Parameters with a POST /.search Request Body](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISQueryParameters.htm#OCISQueryParameters__QueryParametersWithPOST-0F139095).


## Query Parameters With GET 🔗 
When you perform a search by using a `GET` request on a resource endpoint such as `/Users` or `/Groups`, you put the query in the URL. Append a question mark `(?)` to the URL, followed by the query. 
**Note** Characters in a URL that are outside the ASCII character set, such as spaces and quotes, must be URL encoded. Examples are provided with URL encoded characters. The **+** replaces spaces and **%22** replaces quotes **(").**
```
https://<domainURL>/admin/v1/Users?attributes=email&filter=userName+co+%22jensen%22
```

To find all Groups and AppRoles that are associated with a specific user:
```
https://<domainURL>/admin/v1/Users/1e895413c68d42c7bc006d0033794c1e?attributes=groups,urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:appRoles
```

## Query Parameters with a POST /.search Request Body 🔗 
You can create searches with a POST request on a resource endpoint ending in `/.search`. In that case, you put the query in the request body. When searching for sensitive information, such as usernames, where the sensitive information is submitted along with other data, use this method (for security reasons).
This example shows the request body of a POST method performed on the endpoint `/Users/.search`. It returns the first 10 user entries with `displayName` starting with `smith` and `meta.resourceType` equal to `User.` ```
{ 
"schemas":["urn:ietf:params:scim:api:messages:2.0:SearchRequest"], 
"attributes": ["displayName","userName"], 
"filter": "(displayName sw \"smith\")", "startIndex": 1, "count": 10
}
```

The `attributes` parameter can be used with all methods except `DELETE`. The other query parameters are only meaningful for search methods and are ignored by other methods.
HTTP Query Parameter | Description  
---|---  
`attributes=attribute1,attribute2` |  Specifies a multivalued list of strings indicating the names of resource attributes to return in the response. This query parameter also accepts the extension schema ID as a valid attribute name. Including the extension schema ID in the attributes returns all the default attributes within it.  
`attributeSets` | The search returns a group of attributes in the response rather than specifying each attribute individually. This query parameter accepts comma-separated values from the following parameters: 
  * all (returns all attributes)
  * always (returns all attributes marked as always in the schema)
  * default (returns all default attributes)
  * request (returns all attributes marked as request in the schema)

These values aren't case-sensitive. If both `attributes` and `attributeSets` are specified in the request, then the values from both are returned in the response.  
`count=N` | Indicates the maximum number of search results per page. Specify a non-negative number to retrieve a response. A negative number defaults to 50 and returns the first 50 resources.  
`startIndex=N` | Specifies the start page index. This is the 1-based index of the first query result. A value less than 1 is interpreted as 1.  
`filter=Expression` | The search returns all resources in the specified endpoint for which the expression is true. See [Using the Filter Query Parameter](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISQueryParameters.htm#OCISQueryParameters__UsingTheFilterQueryParameter-600D8285) for more information.  
`sortBy=attribute` | Provides the attribute name on which the response should be sorted.   
`sortOrder=ascending` | `sortOrder=descending` | Specifies the order in which the `sortBy` parameter is applied. If you specify a value for `sortBy` and don't specify a `sortOrder`, the `sortOrder` defaults to `ascending.`  
## Using the Filter Query Parameter 🔗 
You can use the `filter` query in searches that you perform with the `GET` method. The format of a filter query is: 
```
filter=Expression
```

A filter must contain at least one valid expression. Each expression contains an attribute name followed by an attribute operator and optional value. Searchable attributes vary from one resource to another. These are discussed in the topics for those `GET` requests.
The following URL includes a filter query for users with the attribute `userName` that contains `jensen:`
**Note** Characters in a URL that are outside the ASCII character set, such as spaces and quotes, must be URL encoded. Examples are provided with URL encoded characters. The **+** replaces spaces and **%22** replaces quotes **(").**
```
https://<domainURL>/admin/v1/Users?filter=userName+co+%22jensen%22
```

Attribute Operator | Description | Behavior  
---|---|---  
`eq` | Equal  | The attribute and operator values must be identical for a match.  
`ne` | Not equal | The attribute and operator values aren't identical.  
`co` | Contains | The entire operator value must be a substring of the attribute value for a match.  
`sw` | Starts with | The entire operator value must be a substring of the attribute value, starting at the beginning of the attribute value. This criterion is satisfied if the two strings are identical.  
`ew` | Ends with | The entire operator value must be a substring of the attribute value, matching at the end of the attribute value. This criterion is satisfied if the two strings are identical.  
`pr` | Present (has value) | If the attribute has a nonempty value, or if it contains a nonempty node for complex attributes, there's a match.  
`gt` | Greater than | If the attribute value is greater than operator value, there's a match. The actual comparison depends on the attribute type. For string attribute types, this is a lexicographical comparison and for `DateTime` types, it's a chronological comparison.   
`ge` | Greater than or equal | If the attribute value is greater than or equal to the operator value, there's a match. The actual comparison depends on the attribute type. For string attribute types, this is a lexicographical comparison and for `DateTime` types, it's a chronological comparison.  
`lt` | Less than | If the attribute value is less than operator value, there's a match. The actual comparison depends on the attribute type. For string attribute types, this is a lexicographical comparison and for `DateTime` types, it's a chronological comparison.   
`le` | Less than or equal to | If the attribute value is less than or equal to the operator value, there's a match. The actual comparison depends on the attribute type. For string attribute types, this is a lexicographical comparison and for `DateTime` types, it's a chronological comparison.   
You can combine multiple expressions by using the logical operators `and` and `or` and negate an expression by preceding it with the attribute operator `not.` Use parentheses `()` for precedence grouping and square brackets `[]` for complex attribute filter grouping.
## Query Parameters Filter Examples 🔗 
Use the following query parameters examples as a starting point for queries in an identity domain. 
**Note** Characters in a URL that are outside the ASCII character set, such as spaces and quotes, must be URL encoded. Examples are provided with URL encoded characters. The **+** replaces spaces and **%22** replaces quotes **(").**
### User Examples 🔗 
To search for users with the attribute `userName` equal to `example`, you would use this filter:
```
https://<domainURL>/admin/v1/Users?filter=userName+eq+%22example%22
```

This filter example searches for a user with a `userName` that contains `jensen:`
```
https://<domainURL>/admin/v1/Users?filter=userName+co+%22jensen%22
```

This filter example searches for a user with a `userName` that contains either `example` or that starts with `my:`
```
https://<domainURL>/admin/v1/Users?filter=userName+co+%22example%22+or+userName+sw+%22my%22
```

This filter example searches for a user with the `familyName` subattribute of `name` that contains `jensen:`
```
https://<domainURL>/admin/v1/Users?filter=name.familyName+co+%22jensen%22
```

This complex URL query example returns all users with a `userName` equal to `example`, lists the attributes `emails.value` and `name.familyName` in the JSON response body, and returns a maximum of eight users per page of output.
```
https://<domainURL>/admin/v1/Users?filter=userName+eq+%22example%22&attributes=emails.value,name.familyName&count=8
```

This filter example searches for users using the filter parameter in GET.
```
https://<domainURL>/admin/v1/Users/?filter=phoneNumbers.value co "415"
```

This filter example returns users who have the searchable custom attribute `Nickname`. To learn more about searchable custom attributes, see [Customizing User Schemas](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#schemacustomization "When you start using identity domains, you might load a different set of user identities based on requirements from various departments within or outside of your organization. Schema Customization allows you to create identity domain-specific custom schemas to supplement the out-of-the-box \(OOTB\) attributes for a resource and allows user schemas to be extended.") and [Customizing Schemas](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/overview.htm#overview "Learn how to add, edit, or remove custom schema attributes and change user permissions for out-of-the-box \(base\) schema attributes.").
```
GET https://<domainURL>/admin/v1/Users?filter=(urn:ietf:params:scim:schemas:idcs:extension:custom:User:Nickname pr)
```

This filter example returns users whose searchable custom attribute matches a string of text. To learn more about searchable custom attributes, see [Customizing User Schemas](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#schemacustomization "When you start using identity domains, you might load a different set of user identities based on requirements from various departments within or outside of your organization. Schema Customization allows you to create identity domain-specific custom schemas to supplement the out-of-the-box \(OOTB\) attributes for a resource and allows user schemas to be extended.") and [Customizing Schemas](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/overview.htm#overview "Learn how to add, edit, or remove custom schema attributes and change user permissions for out-of-the-box \(base\) schema attributes.").
```
GET https://<domainURL>/admin/v1/Users?filter=(urn:ietf:params:scim:schemas:idcs:extension:custom:User:Nickname eq "aabbccc")
```

### Phone Number Examples 🔗 
This filter example searches for users whose phone number starts with "+1"*. 
**Note**
Only works with POST operations.
```

POST https://<domainURL>/admin/v1/Users/.search
{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:SearchRequest"],
"filter": "phoneNumbers.value sw \"+1\""
}
```

This filter example searches for users who home phone number contains the string "503".
```

POST https://<domainURL>/admin/v1/Users/.search
{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:SearchRequest"], 
"filter": "phoneNumbers[type eq \"home\"].value co \"503\""
}
```

Or 
```

POST https://<domainURL>/admin/v1/Users/.search
{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:SearchRequest"], 
"filter": "phoneNumbers[type eq \"home\" and value co \"503\"]"
}
```

This filter example searches for users with phone number variations. 
**Note**
The SCIM filter parameter doesn't support RegEx patterns. You must have included all possible variations. Use the following example to get started.
```

POST https://<domainURL>/admin/v1/Users/.search 
{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:SearchRequest"],
"phoneNumbers.value eq \"+1 9xxxx xxxxx\" or phoneNumbers.value eq \"+19xxxx xxxxx\" or phoneNUmbers.value eq \"+19xxxxxxxxx\""
}
```

### App Role Examples 🔗 
This filter example searches for all users who have a specific AppRole:
```
https://<domainURL>/admin/v1/Users?filter=urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:approles.value+eq+<idOfAppRole>
```

This filter example returns members of the AppRole using the `approleid`.
```

GET https://<domainURL>/admin/v1/AppRoles/{{approleid}}?attributes=members
```

This filter example returns AppRoles for a specific application using the `appid`.
```

GET https://<domainURL>/admin/v1/AppRoles?filter=app.value eq "{{appid}}"
```

Was this article helpful?
YesNo

