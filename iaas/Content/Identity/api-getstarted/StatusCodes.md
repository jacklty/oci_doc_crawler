Updated 2024-04-02
# Response Codes
When you call any of the identity domains REST API resources, the Response header returns one of the standard HTTP status codes.
See the [Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) section of the Hypertext Transfer Protocol -- HTTP/1.1.
HTTP Status Code |  Description  
---|---  
`200 OK` | The request was successfully completed. A 200 status is returned for a successful `GET` method.  
`201 Created` | The request has been fulfilled and resulted in a new resource being created. The response includes a Location header containing the canonical URI for the newly created resource.A 201 status is returned from a synchronous resource creation or an asynchronous resource creation that completed before the response was returned.  
`202 Accepted` | The request has been accepted for processing, but the processing hasn't been completed. The request might or might not eventually be acted upon, as it might be disallowed at the time processing actually takes place.When specifying an asynchronous `(__detached=true)` resource creation (for example, when deploying an application), or update (for example, when redeploying an application), a 202 is returned if the operation is still in progress. If `__detached=false`, a 202 may be returned if the underlying operation doesn't complete in a reasonable amount of time.The response contains a Location header of a job resource that the client should poll to determine when the job has finished. Also, returns an entity that contains the current state of the job  
`204 No Content` | Operation succeeded and there's no content to send in the response body. This is typically sent on successful `DELETE.`  
`307 Temporary Redirect` | The request should be repeated at the temporary location identified, but use the original location as the permanent reference to the resource.  
`308 Permanent Redirect` | The request should be repeated at the location identified and use that as the permanent reference to the resource.  
`400 Bad Request` | The request couldn't be processed because it contains missing or invalid information (such as, a validation error on an input field, a missing required value, and so on).  
`401 Unauthorized` | The request isn't authorized. The authentication credentials included with this request are missing or invalid.  
`403 Forbidden` | The request operation isn't supported.  
`404 Not Found` | The request includes a resource URI that doesn't exist.  
`405 Method Not Allowed` | The HTTP verb specified in the request `(DELETE, GET, POST, PUT)` isn't supported on this resource, or the method requires a filter, which wasn't provided.  
`409 Conflict` | Either the version number doesn't match, or a duplicate resource was requested and can't be recreated.  
`412 Precondition Failed` | Failed to update, as resource changed.  
`413 Request Entity Too Large` | maxOperations (1000) or maxPayload (1048576) was exceeded.  
`415 Not Acceptable` | The client's ContentType header isn't correct (for example, the client attempts to send the request in XML, but the resource can accept only JSON).  
`500 Internal Server Error` | The server encountered an unexpected condition that prevented it from fulfilling the request.  
`501 Not Implemented` | The requested operation isn't supported.  
`503 Service Unavailable` | The server is unable to handle the request because of temporary overloading or maintenance of the server. The identity domains REST web application isn't currently running.  
Was this article helpful?
YesNo

