Updated 2025-01-14
# Using an OAuth Token for Platform Services
The OAuth 2.0 token service provided by identity domains is a mechanism that enables you to use a secured token to access the REST endpoints of Oracle Cloud Platform Services (PaaS).
**Note**
  * To access a cloud platform service that's integrated with identity domains, you need the identity domain URL. If you don't know the identity domain URL, see [Finding an Identity Domain URL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm#locate-identity-domain-url "You need the Domain URL to access a PaaS product that's integrated with identity domains using the REST APIs.").
  * cURL examples are used in the procedure to obtain an access token from identity domains, and then access a cloud platform service REST endpoint with the token.


An OAuth access token has an expiration value of 86,400 seconds (24 hours). To make REST API requests 24 hours after getting an access token, you need to obtain a new token.
## Prerequisites
Get the following information from the identity domain before you begin.
  * Identity domain URL
  * Client ID
  * Client secret
  * Primary audience URL
  * Allowed scope


  1. Sign in to the **My Services** dashboard for your identity domain.
**Note** You need to have either the identity domain administrator role or PaaS administrator role to follow the steps in this procedure.
  2. In the list of services, find the entry for the identity domain, and then select **Identity Cloud.**
  3. On the **Overview** tab, find the **Service Instances** section, and then copy the value shown in the **Service Instance URL** field.
For example: `https://<domainURL>.identity.oraclecloud.com/ui/v1/adminconsole`
Where `<domainURL>` is the REST server part of the identity domain URL (which forms part of the endpoint URL for requesting an access token).
  4. Select **Open Service Console,** expand the **Navigation Drawer,** and then select **Applications.**
  5. In the search field, enter `PSM` and then select the search icon. In the results, find the entry titled **PSM App for API OAuth support.**
**Note** The Platform Service Manager App (PSMApp) isn't available for Oracle Cloud accounts that were created before 18.1.4.
  6. Select the name of the application titled **PSM App for API OAuth support.** The name has the form `PSMApp-cacct-_string-of-letters-and-numbers_.`
For example:
`PSMApp-cacct-9z8x7c6v5b4n3m`
This is the identity domain trusted PSM client application, which is automatically created for Oracle Cloud accounts (after 18.1.4) and associated with the Oracle Cloud Platform Service.
  7. Select **Configuration.** Under **General Information,** copy the value shown in the **Client ID** field.
This is the PSMApp client ID. For example:
`PSMApp-cacct-9z8x7c6v5b4n3m_APPID`
  8. Select **Show Secret,** and then copy the value.
This is the PSMApp client secret. For example:
`c53b437-1768-4cb6-911e-1e6eg2g3543`
  9. Expand **Resources.** Copy the value shown in the **Primary Audience** field.
This is the PSMApp primary audience URL. For example:
`https://psm-cacct-9z8x7c6v5b4n3m.console.oraclecloud.com`
  10. In the **Allowed Scopes** section, copy the **Scope** value for **1PaaS Permission.**
`urn:opc:resource:consumer::all`


## Get an OAuth Access Token
With the information that you gathered, use the identity domains REST API endpoint `/oauth2/v1/token` to obtain a token.
```
  curl -k 
  -X POST -u "client-id:client-secret" 
  -d "grant_type=password&username=yourusername&password=yourpassword&scope=https://primary-audience-and-scope" "https://identity-cloud-service-instance-url/oauth2/v1/token"
```

Where:
  * `_client-id_`is the PSMApp client ID
  * `_client-secret_`is the PSMApp client secret
  * `_yourusername_`is the cloud platform service username with an administrator role
  * `_yourpassword_`is the password for the username
  * `_primary-audience-and-scope_`is a concatenation of the PSMApp primary audience URL and the 1PaaS permission scope
  * `_identity-cloud-service-instance-url_`is the REST server part of the identity domain URL


For example:
```
  curl -k 
-X POST -u "PSMApp-cacct-9z8x7c6v5b4n3m_APPID:c53b437-1768-4cb6-911e-1e6eg2g3543" 
-d "grant_type=password&username=yourusername&password=yourpassword&scope=https://psm-cacct-9z8x7c6v5b4n3m.console.oraclecloud.comurn:opc:resource:consumer::all" "https://<domainURL>.identity.oraclecloud.com/oauth2/v1/token"
```

The following shows an example of the returned response.
```
{
  "access_token": "eyJ7NXQ...fMf46Q0yKopDxQ",
  "token_type": "Bearer",
  "expires_in": 86400
}
```

**Note** The token string is truncated in the example response. Copy the entire token string (within the quotation marks) as shown in your response.
## Use the OAuth Access Token in Cloud Platform Service REST API Requests
After you obtain an OAuth 2.0 access token, you provide the token in a bearer token header of the cloud platform service REST request.
```
  curl -i 
  -X GET 
  -H "Authorization: Bearer token-string" "https://primary-audience/rest-endpoint-path"
```

Where:
  * `_token-string_`is the OAuth access token that you obtained
  * `_primary-audience_`is the PSMApp primary audience URL
  * `_rest-endpoint-path_`is the relative path that defines the cloud platform service REST resource. Note that the identity domain ID might be used in the path.


For example, the following cURL command retrieves all Oracle Java Cloud Service instances.```
  curl -i -X GET 
  -H "Authorization: Bearer eyJ7NXQ...fMf46Q0yKopDxQ" "https://psm-cacct-9z8x7c6v5b4n3m.console.oraclecloud.com/paas/api/v1.1/instancemgmt/idcs-9a888b7e6ebb44b4b65/services/jaas/instances"
```

Was this article helpful?
YesNo

