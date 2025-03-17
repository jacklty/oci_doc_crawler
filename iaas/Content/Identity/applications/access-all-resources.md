Updated 2024-02-13
# Accessing All Resources
The **All** authorized resource option enables the client to access any resource within a domain.
Select **All** to allow your application to request an access token for trusted or confidential client using the scope `urn:opc:resource:consumer::all.` This option provides a wide scope. The access token in the response contains the audience `urn:opc:resource:scope:account` and the scope `urn:opc:resource:consumer::all,` which gives access to any of the services that are in the same domain without requiring explicit association with target services. 
Use only the `urn:opc:resource:consumer::all` scope in the request. An invalid scope error is returned if you attempt to include both the `urn:opc:resource:consumer::all` scope and another scope in the same request, such as `urn:opc:idm:__myscopes__.`
In the account mode, clients can get token for any specific resource provided either `urn:opc:resource:consumer::all` or the specific resource is added in the allowed scopes.
Apart from the scope defined above, you can also specify fine-grained scope as follows:
  * `urn:opc:resource:consumer:paas::read`
  * `urn:opc:resource:consumer:paas:stack::all`
  * `urn:opc:resource:consumer:paas:analytics::read`


**Note** The requested scope should always exist and match, either directly or hierarchically, the client's defined allowed scopes to allow the client access to the resource.
For example, a client uses the `urn:opc:resource:consumer:paas:analytics::read` scope in its request for access to a resource. If the scope directly matches an allowed scope defined, then in the returned access token the audience is `urn:opc:resource:scope:account` and the scope is `urn:opc:resource:consumer:paas:analytics::read`. 
If the allowed scope defined by the client is `urn:opc:resource:consumer:paas::read`, then the client is allowed to access the resource hierarchically if the client requests one of the following scopes:
  * `urn:opc:resource:consumer:paas::read`
  * `urn:opc:resource:consumer:paas:analytics::read`


However, if the requested scope is `urn:opc:resource:consumer:paas:analytics::write` with a different qualifier, then the client isn't allowed access to the resource.
**Note** The **All** option doesn't provide access to the IAM admin APIs. You must continue to use the scope `urn:opc:idm:__myscopes__` to access the admin APIs.
To generate a refresh token in addition to the access token, use the scope `urn:opc:resource:consumer::all offline_access` in the request.
Was this article helpful?
YesNo

