Updated 2024-04-02
# Using cURL
cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API. 
## Using cURL to Access the REST APIs 🔗 
  1. Install cURL. See [Step 2: Install cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/QuickStart.htm#QuickStart__install_curl).
  2. In a command window, set the cURL environment variable, `CURL_CA_BUNDLE`, to the location of your local CA certificate bundle. For information about CA certificate verification using cURL, see: [http://curl.haxx.se/docs/sslcerts.html.](http://curl.haxx.se/docs/sslcerts.html)
**Note**
See [Authorization](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm "The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.") for more information about authorization and authentication requirements.
  3. Invoke cURL and specify one or more of the following command line options, as required, to direct its execution.
     * `-d, --data @file.json`: Identifies the request document, in JSON format, on the local machine.
     * `-F, --form @file.json`: Identifies form data, in JSON format, on the local machine.
     * `-H, --header`: Defines the request header in the format of HEADER: VALUE. The header values depend on which endpoint that you're accessing. 
       * The content type of the request document.
       * The `X-Client-ID,` `API_KEY_ID,` for OAuth 2.0 authorization
       * The `X-Client-Secret,` `API_KEY_SECRET,` for OAuth2.0 authorization
     * `-i`: Displays response header information.
     * `-X`: Indicates the HTTP request method `(DELETE, GET, POST, PATCH`, or `PUT).` If this option is omitted, the default is GET.


## The cURL Command URL 🔗 
The URL used with the cURL command is the same as that described in [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") except that you must replace spaces in the URL with plus characters **(+)** and replace quotes (") with**%22**. 
Any characters in a URL that are outside the ASCII character set, such as spaces and quotes, must be URL encoded. For example, the following URL contains a filter query that searches for a user with a username either containing `jen` or starting with `bj`. Note that it contains spaces.
```
https://<domainURL>/admin/v1/Users?filter=userName co "jen" or userName sw "bj"
```

To use this URL in a cURL command line, you would change it to: 
```
https://<domainURL>/admin/v1/Users?filter=userName+co+%22jen%22+or+userName+sw+%22bj%22
```

## cURL Command for Sending a GET Request 🔗 
```
curl 
-H "Accept: application/scim+json" 
-H "Authorization: Bearer <really long access token here>" 
-G https://<domainURL>/admin/v1/Groups?filter=displayName+co+%22admin%22"
```

## cURL Command for Sending a POST Request 🔗 
```
curl 
-H "Content-Type: application/scim+json" 
-H "Authorization: Bearer <really long access token here>" 
-d '{ "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],"userName":"bjensen@example.com","name": {"familyName":"Jensen","givenName": "Barbara","middleName": "Jane"},"emails": [{"value": "bjensen@example.com","type": "work","primary": true}]}' "https://<domainURL>/admin/v1/Users"
```

Was this article helpful?
YesNo

