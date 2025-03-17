Updated 2024-04-02
# Send Requests
Follow these guidelines when you build send requests using the identity domains REST API.
## URL Structure 🔗 
Access the identity domains REST API through a URL, which includes the REST endpoint, the resource that you want to access, and any query parameters that you want to include in a request. Get the complete URL structure for the identity domains REST API from your Oracle Cloud administrator or identity domain administrator.
**Basic Endpoint**
The basic endpoint for the identity domains REST API is:
```
https://<domainURL>/
```

Where: `domainURL` represents the domain-specific URL. To get this URL using the identity domains Console, see [Finding an Identity Domain URL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm#locate-identity-domain-url "You need the Domain URL to access a PaaS product that's integrated with identity domains using the REST APIs."). 
Alternatively, get this URL from your Oracle Cloud administrator or identity domain administrator. 
**Resource Endpoints**
When you create a new resource or perform a search for members of a resource type, you append the name of the resource. For example, when you send a `POST` request to create a new user, you use the endpoint:
```
https://<domainURL>/admin/v1/Users
```

**Specific Resources Within an Endpoint**
To access a specific resource, you append the value of the `id` attribute for that resource to the resource endpoint. For example, if you created a User, and the response to your `POST` request included the `ocid` value `ocid1.user.oc1..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` in the response body, you would use the following endpoint to access that specific User resource in subsequent `GET,` `PATCH`, or `PUT` requests:
```
https://<domainURL>/admin/v1/Users/ocid1.user.oc1..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Supported Methods 🔗 
The identity domains REST API supports the following request methods.
**Note** The methods supported depend on the endpoint.
HTTP Method | Description  
---|---  
`GET` | Search for resources or search for a specific resource by ID.  
`HEAD` | Check for resource existence and/or modification. Doesn't return a response body. Read-only.  
`POST` | Create, change, reset, import, authenticate, schedule, or create a search request to identity domain resources.  
`PUT` | Replace (fully update) an existing identity domain resource, activate or deactivate an identity domain resource, and so on.  
`PATCH` | Modify (partially update) identity domain resources.  
`DELETE` | Delete or cancel identity domain resources.  
`OPTIONS` | Retrieve the allowed operations for the endpoint.  
## Supported Headers 🔗 
The identity domains REST API supports the following headers that may be passed in the header section of the HTTP request or response.
Header | Description | Example  
---|---|---  
`Content-Type` | Media type of the body of the request. Required for POST and PUT requests. |  `Content-Type: application/scim+json` `Content-Type: application/json`  
`Authorization` |  The OAuth access token used to access protected resources Or the request signatures in the Authorization header | Access tokens are very long strings. This example has been truncated: `Bearer VkdVAZrb_fw......eyJ4NXQjUzI1Ni`  
Was this article helpful?
YesNo

