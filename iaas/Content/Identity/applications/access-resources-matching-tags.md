Updated 2025-01-14
# Accessing Resources with Matching Tags
The **Tagged** authorized resource option enables the client to access any resource with matching tags.
Request an access token using the trusted or confidential client and request the scope `urn:opc:resource:consumer::all`. The access token in the response contains the audience `urn:opc:resource:scope:tag=<base64 encoded           JSON>` and the scope `urn:opc:resource:consumer::all`, which gives access to Resource Apps that have tags that match the allowed tags specified in the Client App.
In the tags mode, clients can get token for any specific resource provided either the client has matching tags with the resource and `urn:opc:resource:consumer::all` or the specific resource is added in the allowed scopes.
Select **Tagged** to enable your confidential application to access tags from other applications.
When you select **Tagged** , you can choose scopes from an OPC application that aren't specific, such as `urn:opc:resource:consumer`. 
  1. Select **Tagged**.
  2. Select **Add Scope** under **Resources**.
  3. Select `urn:opc:resource:consumer` on the **Select scope** page and select **>**.
  4. Select the OPC scopes that you want to add and provide a named qualifier, such as read and write to each of the scopes. You can edit these qualifiers dynamically.
  5. Select **Add**.
The scopes appear under **Resources**.


In addition to using the `urn:opc:resource:consumer::all` scope, you can also specify the following fine-grained scopes:
  * `urn:opc:resource:consumer:paas::read`
  * `urn:opc:resource:consumer:paas:stack::all`
  * `urn:opc:resource:consumer:paas:analytics::read`


**Note** The requested scope must always exist and match, either directly or hierarchically, the client's defined allowed scopes to allow the client access to the resource.
For example, a client uses the `urn:opc:resource:consumer:paas:analytics::read` scope in its request for access to a resource. If the scope directly matches an allowed scope defined, then in the returned access token the audience is `urn:opc:resource:scope:tag=<base64 encoded JSON>` and the scope is `urn:opc:resource:consumer:paas:analytics::read`.
For client allowed tags `color:green` and `color:blue`, the sample JSON is as follows: 
`{"tags":[{ "key":"color","value":"green"},{"key":"color","value":"blue"}           ]}`
If the allowed scope defined by the client is `urn:opc:resource:consumer:paas::read`, then the client is allowed to access the resource hierarchically if the client requests one of the following scopes:
  * `urn:opc:resource:consumer:paas::read`
  * `urn:opc:resource:consumer:paas:analytics::read`


However, if the requested scope is `urn:opc:resource:consumer:paas:analytics::write`, then the client isn't allowed access to the resource, since that isn't one of the allowed scopes defined by the client.
Was this article helpful?
YesNo

