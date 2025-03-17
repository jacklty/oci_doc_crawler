Updated 2024-04-02
# Working with CORS
Cross-Origin Resource Sharing (CORS) is a header-based protocol that allows JavaScript to make requests on your behalf to access resources in another domain. Configure Cloud Gate so that it enables CORS and enforces CORS settings for Cloud Gate running in App Gateway.
CORS helps to prevent rogue JavaScript (planted in a site by attackers, for example, by using advertisements) from making AJAX requests on your behalf. Fraudulent AJAX requests could withdraw money from your bank or make purchases in your name at an online shopping site. These requests could succeed if you currently have an active session with those sites. CORS stipulates that if a server doesn't respond with the correct set of Response Headers, the browser doesn't allow the JavaScript to see (or access) the response. 
A CORS request is triggered when JavaScript attempts an HTTP Request to a different:
  * domain - for example, `site1.oraclecloud.com` calls `oracle.com`
  * subdomain - for example, `site1.oraclecloud.com` calls `site7.oraclecloud.com`
  * port - for example, `site1.oraclecloud.com` calls `site1.oraclecloud.com:3030`
  * protocol - for example, `https://site1.oraclecloud.com` calls `http://site1.oraclecloud.com`


A CORS Request comes in two forms: a Simple CORS Request or a Preflight CORS Request.
## **Simple CORS Request**
A Simple CORS Request is performed if the JavaScript Request against a resource in another domain has the following characteristics:
  * The method is one of the following: 
    * `GET`
    * `POST`
    * `HEAD`
  * The allowed HTTP Headers that can be manually added to the Simple CORS Request are: 
    * `Accept`
    * `Accept-Language`
    * `Content-Language`
    * `Content-Type`
    * `DPR`
    * `Downlink`
    * `Save-Data`
    * `Viewport-Width`
    * `Width`
  * The `Content-Type`, if set, must be: 
    * `application/x-www-form-urlencoded`
    * `multipart/form-data`
    * `text/plain`


## Preflight CORS Request 🔗 
If the JavaScript request doesn't meet the characteristics of a Simple CORS Request, then a Preflight CORS Request is sent to the resource located in the other domain. 
The Preflight CORS Request tests whether the actual request can be sent to that resource by including specific HTTP headers in the request containing the data that resulted in the preflight request flow being triggered. In other words, if the JavaScript HTTP Request specified some method/headers in the HTTP Request that required a Preflight CORS Request, then the Preflight CORS Request queries the resource for those method/headers to see whether the resource accepts such a cross-domain request.
## Cloud Gate CORS Configuration Properties and Attributes
The following table describes the Cloud Gate CORS configuration properties and attributes.
CORS Property | Description  
---|---  
`cloudGateCorsEnabled` |  Boolean property to turn on Cloud Gate CORS support. This setting must be configured to: `true`. The default is `false`. **Best practice.** Configure `cloudGateCorsAllowedOrigins` at the same time. If this is property is left empty, all CORS Requests fail.  
`cloudGateCorsAllowedOrigins` |  The property is a String Array that contains the list of allowed CORS Origins. The default is an empty array. Every CORS Request specifies its source or origin in the Origin Request Header. The value of the Origin Header is matched to this list.  If the Origin is matched, Cloud Gate adds the appropriate CORS Headers to its response.  If the Origin isn't matched, Cloud Gate doesn't return any CORS Response Headers - causing the response to be rejected by the browser. Allowed CORS values in the entry template:
  * Entry: `* |                          <PROTOCOL>"://"<HOST><PORT>`
  * <PROTOCOL>: `* | http |                          https`
  * <HOST>: `[<DOMAIN>.]<DOMAIN>`
  * <DOMAIN>: < any alphanumerical character, * and - >
    * A <DOMAIN> can't start or end with a '`-`'.
    * Any <DOMAIN> can be a wild card. The wild card must include the entire domain. For example, `www.*.com` is valid but `www.*racle.com` isn't.
    * Use https://tools.ietf.org/html/rfc1123 as a reference
  * <PORT>: `<EMPTY> | ":"                          <PORT_VALUE>`
  * <PORT_VALUE>: `* |                          <numerical                          characters>`. <PORT_VALUE> must be in the range 1 - 65535.

Examples: 
  * Match everything: `*`
  * Exact match: `https://www.acme.com,                          https://www.acme.com:4443`
  * Exact host/protocol, any port: `https://www.google.com:* `
  * Exact host/port, any protocol (HTTP or HTTPS): `*://www.acme.com,                          *://www.acme.com:8080`
  * Subdomain, exact protocol, no port: `https://*.oraclecloud.com`
  * Any domain, exact protocol, no port: `https://*`

  
`cloudGateCorsAllowNullOrigin` |  Boolean property to support scenarios where the browser sends a "null" Origin. This setting must be configured to: `true`.  The default is `false`. A "null" Origin is sent if the CORS Request is coming from a file on a user's computer or if a server redirects to another server in response to a CORS Request. The browser passes a "null" Origin when it considers the Origin "tainted". To increase security, by default, "null" Origins aren't allowed.  Some "null" Origins are valid. Applications that leverage the Oracle Identity Cloud Service OpenID Connect (OIDC) Browser Flow Login will see "null" Origins sent to their Cloud Gate node(s). When Cloud Gate redirects to the Oracle Identity Cloud Service authorize endpoint to start the OIDC Browser Login and when Oracle Identity Cloud Service redirects the request back to Cloud Gate, the Origin will be "null".  
`cloudGateCorsMaxAge` |  An integer that specifies the number of seconds the client (browser) can cache a Preflight CORS Response.  
`cloudGateCorsExposedHeaders` |  The property is a String Array that lists the Response Headers that can be added to the `Access-Control-Expose-Headers` Response Header. The default is an empty array.  
## Configuring Cloud Gate CORS Settings in Identity Domains 🔗 
Cloud Gate requires you to configure the following settings in identity domains for Cross-Origin Resource Sharing (CORS) support.
Before you start configuration, ensure that you have the correct version of the Cloud Gate. Earlier versions of the Cloud Gate module didn't provide support for CORS. It was left to Protected Applications to support CORS. If the `isCorsAllowed` setting in the Web Tier Policy document was configured to `true`, Cloud Gate would allow preflight CORS Requests through to Protected Applications. 
**Note** The minimum Cloud Gate version required is 21.1.2.
Use the `/admin/v1/Settings/Settings` endpoint to configure the CORS settings. The request is a `patch` operation. See [Update a Setting](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-settings-id-patch.html) for more information.
  1. Use this sample payload as a template to build the request body. Save the payload to a file, for example, `/tmp/cors-settings.json`. Edit the file with your deployment details.
Sample payload.```
  {
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [{
  "op": "replace",
  "path": "cloudGateCorsSettings",
  "value": {
  "cloudGateCorsEnabled": true,
  "cloudGateCorsAllowNullOrigin": true,
  "cloudGateCorsAllowedOrigins": [ "https://app.my-server.com:8080", "https://*:*" ],
  "cloudGateCorsMaxAge: 60,
  "cloudGateCorsExposedHeaders": [ "x-custom-header", "x-my-app-header" ]
  }
  }]
  }
```

Sample cURL request.```
  # $AT is a previously generated Admin Access Token.
  # IDCS URL is an example URL 
  $ curl --insecure --noproxy '*' -X PATCH -H "Content-Type: application/scim+json" -H "Accept: application/json" -H "Authorization: Bearer $AT" "https://<domainURL>/admin/v1/Settings/Settings" --data @"/tmp/cors-settings.json"
```

  2. Perform one of the following to enable CORS support.
     * Manually restart or reload the NGINX server.
     * Wait until the Cloud Gate CORS settings cache expires. This can take up approximately 15 minutes, by default.
  3. Issue the following commands to confirm that CORS support is enabled.
     * `Access-Control-Allow-Origin`
     * `Access-Control-Allow-Methods`
     * `Access-Control-Allow-Headers`
     * `Access-Control-Allow-Credentials`
     * `Access-Control-Max-Age`
     * `Access-Control-Expose-Headers`


## Simple and Preflight CORS Request Workflows 🔗 
Overview of Cross-Origin Resource Sharing (CORS) request workflows.
### Simple CORS Request Workflow
  1. The Request is identified as a CORS Request by the presence of the Origin Request Header.
  2. If necessary (for example, cache expiry), the Cloud Gate CORS settings are downloaded from identity domains in IAM.
  3. Cloud Gate processes the request - either rejecting the request or allowing it through to the upstream application server.
  4. Before a response is returned, Cloud Gate enforces CORS as defined by the Cloud Gate CORS settings.
    1. Cloud Gate always ensures that the Vary Response Header is part of the Response - and contains the "Origin" Header. This occurs even for non-CORS Requests.
    2. If `cloudGateCorsEnabled` is `false`, processing stops here. The Response is returned as-is.
    3. Cloud Gate verifies that the Origin is allowed - using the configured list of Allowed Origins.
If the Origin isn't allowed, all supported CORS Response Headers are stripped from the Response and processing ends.
    4. The `Access-Control-Allow-Origin` Response Header is added and configured to the value of the Origin Request Header.
    5. The `Access-Control-Allow-Credentials` Response Header is added and configured to `true`.
    6. The `Access-Control-Expose-Headers` is configured to the intersection between the `cloudGateCorsExposedHeaders` value, and the list of Headers being returned in the Response.
    7. The `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`, and `Access-Control-Max-Age Response Headers` are removed from the Response.
  5. Cloud Gate returns its Response.


**Note**
Cloud Gate overwrites the `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials Response` Headers if set by the upstream application server.
### Preflight CORS Request Workflow
  1. The Request is identified as a CORS Request by the presence of the Origin Request Header.
  2. If necessary (for example, cache expiry), the Cloud Gate CORS settings are downloaded from identity domains in IAM.
  3. The Request is identified as a Preflight CORS Request by the OPTIONS Method and the `Access-Control-Request-Method` Request Header - in addition to the Origin Request Header.
  4. If `cloudGateCorsEnabled` is `true`, the Request is allowed to go through to the upstream application server - to allow applications to implement CORS.
If `cloudGateCorsEnabled` is `false`, the old `isCorsAllowed` Web Tier Policy setting is still honored - just later in the request processing.
  5. Before the response is returned from Cloud Gate, CORS is enforced as defined by the Cloud Gate CORS settings.
    1. Cloud Gate always ensures that the Vary Response Header is part of the Response - and contains the "Origin" Header. This occurs even for non-CORS Requests.
    2. If `cloudGateCorsEnabled` is `false`, processing stops here. The Response is returned as-is.
    3. Cloud Gate verifies that the Origin is allowed - using the configured list of Allowed Origins.
If the Origin isn't allowed, all supported CORS Response Headers are stripped from the Response and processing ends.
    4. The `Access-Control-Allow-Origin` Response Header is added and configured to the value of the Origin Request Header.
    5. The `Access-Control-Allow-Credentials` Response Header is added and configured to `true`.
    6. If the upstream application server didn't add the `Access-Control-Allow-Methods` Response Header, Cloud Gate constructs its value as follows:
       * If the Allow Response Header is included in the Response, Cloud Gate uses its value.
       * If the `Access-Control-Request-Method` Request Header is found in the Request, Cloud Gate uses its value.
    7. If the upstream application server didn't add the `Access-Control-Allow-Headers` Response Header, Cloud Gate uses the value of the `Access-Control-Request-Headers` Request Header in the Request if it's present.
    8. If `cloudGateCorsMaxAge` is configured to a value greater than zero, the `Access-Control-Max-Age` Response Header is added and configured to the max age value. If the `cloudGateCorsMaxAge` value is zero or less, no action is taken for the `Access-Control-Max-Age` Response Header.
    9. The `Access-Control-Expose-Headers` Response Header is removed. It doesn't apply to Preflight Responses.
  6. Cloud Gate returns its Response.


Was this article helpful?
YesNo

