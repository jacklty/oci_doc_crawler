Updated 2025-01-14
# Adaptive Risk Analysis for Custom Client Applications
Customers moving to the Cloud can leverage IAM identity domain adaptive capabilities to meet risk-based analysis for their on-premises access management system, such as Oracle Access Manager (OAM), or client applications.
Identity domains provide an adaptive REST API interface to enable these on-premises access management systems or client applications to use an identity domain risk-based engine to evaluate authentication activities for users. 
For example, John Doe is a user in the OAM identity store and in an identity domain. John accesses a finance application protected by OAM. The OAM server redirects him to the OAM sign-in page for authentication. John Doe submits his credentials and based on the risk score returned by the identity domain adaptive risk-based engine, the OAM server may challenge the user with a second factor. If the risk score is high, then OAM may deny access to John and present him a message indicating his attempt to sign in failed.
The adaptive REST API interface implements three use cases in the form of the corresponding endpoints:
  * **Populate Risk** : `/admin/v1/sdk/adaptive/PopulateRisks`
  * **Fetch Risk Info** : `/admin/v1/sdk/adaptive/FetchRisks`
  * **Mitigate Risk** : `/admin/v1/sdk/adaptive/MitigateRisks`


To make REST API calls to these endpoints, your access management system or custom application needs an access token from a client credential application registered in an identity domain.
**Note** To obtain an access token, see [Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm "The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to programmatically manage users, groups, applications, and identity functions, such as password management and administrative tasks. To make REST API calls to your identity domain, you need an OAuth2 access token to use for authorization. The access token provides a session \(with scope and expiration\), that your client application can use to perform tasks in an identity domain.").
The adaptive REST API interface requires the client application to send information such as user identification, information of the device the user uses to sign in, and client's true IP address.
To gather device information that your access management system needs to use a device fingerprint JavaScript file. You can download the device fingerprint JavaScript file from the identity domain console.
  1. Sign in to identity domain Console as an application administrator.
  2. Expand the **Navigation Drawer** , select **Settings** , and then select **Downloads**.
  3. In the **Downloads** page, download the **Identity Cloud Service Device Fingerprint Utility**.


The file you download is a compressed (zip) file. Inside the zip file there's a JavaScript file that the access management system sign-in page or the client application itself needs to load to collect fingerprint information. Then use the `getFingerprint()` function to collect user's device fingerprint to send to the identity domains adaptive REST API interface.
See also [Enable the Access for an unknown device Event for a Custom Sign-In Page](https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:26834).
## Populate Risk
This endpoint is used to submit risk data to an identity domain to increase the user's risk score.
The cURL command structure is:```
  curl -k -X POST 'https://<domainURL>/admin/v1/sdk/adaptive/PopulateRisks' 
  -H 'Authorization: Bearer <Access_Token>' 
  -H 'Accept:application/json' 
  -d '<Request_Body>'
```

The following is the structure of the request body for the Populate Risk endpoint.```
{
  "userName": "<User_Name>",
  "data": [
    {
      "name": "device",
      "value": "<result_of_the_devicefingerprint_javascript_file>"
    },
    {
      "name": "client-ip",
      "value": "<ip_address_of_the_user_browser>"
    }
  ],
  "event": "MAX_PASSWORD_FAILED_ATTEMPTS"
}
```

The `event` attribute is optional. If not present in the request then all risk events are going to be used to evaluate risk score. You can use `MAX_MFA_FAILED_ATTEMPTS` or `MAX_PASSWORD_FAILED_ATTEMPTS` values.
The following is an example of a request body to evaluate risk for John Doe trying to sign in the access management system from the IP address `10.11.12.13`. The device fingerprint and IP address will be validated against all enabled risk events in an identity domain.```
  curl -k -X POST https://<domainURL>/v1/sdk/adaptive/PopulateRisks \
   -H 'Content-Type: application/json' \
 
  -H 'Authorization: Bearer <Access_Token>' \
 
  -d '{
  "userName": "johndoe@example.com",
  "data": [
    {
      "name": "device",
      "value": "{\"currentTime\":\"Wed Nov 13 2019 16:57:34 GMT-0700 (Pacific Daylight Time)\",\"screenWidth\":1920,\"screenHeight\":1080,\"screenColorDepth\":24,\"screenPixelDepth\":24,\"windowPixelRatio\":1,\"language\":\"en-US\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0\"}"
    },
    {
      "name": "client-ip",
      "value": "10.11.12.13"
    }
  ]
}'
```

The following is an example of response body of the populate risk endpoint.```
{
  "userName": "johndoe@example.com",
  "riskLevel": "LOW",
  "riskScores": [
    {
      "lastUpdateTimestamp": "2022-11-12T10:41:57.997Z",
      "score": 15,
      "riskLevel": "LOW",
      "value": "ORACLE_IDCS",
      "status": "ACTIVE",
      "source": "Default Risk Provider",
      "$ref": "https://<domainURL>/admin/v1/RiskProviderProfiles/ORACLE_IDCS"
    }
  ]
}
```

## Fetch Risk Info
This endpoint enables clients to get current risk information for a single user, multiple users, or for all users in an identity domain.
The cURL command structure is:```
  curl -k 
  -X POST 'https://<domainURL>/admin/v1/sdk/adaptive/FetchRisks' 
  -H 'Authorization: Bearer <Access_Token>' 
  -H 'Accept:application/json' 
  -d '<Request_Body>'
```

The following is the structure of the Request Body for the Fetch Risk Info cURL command.```
{
  "userNames": [
    "<user_name>"
  ]
}
```

You can call the fetch risk info endpoint for multiple users. To do so, use the following request body structure with the cURL command.```
{
  "userNames": [
    "<user_name_1>",
    "<user_name_2>"
  ]
}
```

If you want to fetch risk info for all users in an identity domain, use the following request body structure with the cURL command.```
{}
```

The following is an example of a request body to fetch risk info for John Doe.```
  curl -k -X POST https://<domainURL>/admin/v1/sdk/adaptive/FetchRisks \
   -H 'Content-Type: application/json' \
 
  -H "Authorization: Bearer <Access_Token>' \
 
  -d '{
  "userNames": [
    "johndoe@example.com"
  ]
}'
```

The following is an example of response body of the fetch risk info endpoint.```
{
  "totalResults": 1,
  "resources": [
    {
      "userName": "johndoe@example.com",
      "riskLevel": "LOW",
      "riskScores": [
        {
          "lastUpdateTimestamp": "2022-11-13T18:41:57.997Z",
          "score": 15,
          "riskLevel": "LOW",
          "value": "ORACLE_IDCS",
          "status": "ACTIVE",
          "source": "Default Risk Provider",
          "$ref": "https://<domainURL>/admin/v1/RiskProviderProfiles/ORACLE_IDCS"
        }
      ]
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 50
}
```

## Mitigate Risk
This endpoint enables client applications to request mitigation of a user's risk score because the user has logged in or reset their password successfully.
The cURL command structure is:```
  curl -k 
  -X POST 'https://<domainURL>/admin/v1/sdk/adaptive/MitigateRisks' 
  -H 'Authorization: Bearer <Access_Token>' 
  -H 'Accept:application/json' 
  -d '<Request_Body>'
```

The following is the structure of the request body for the Mitigate Risk cURL command.```
{
  "userName": "<User_Name>",
  "data": [
    {
      "name": "device",
      "value": "<result_of_the_devicefingerprint_javascript_file>"
    },
    {
      "name": "client-ip",
      "value": "<ip_address_of_the_user_browser>"
    }
  ],
  "event": "SSO_THREAT_MITIGATION_SUCCESS"
}
```

The `event` attribute of the request body can receive multiple values:
  * For successful user sign-in, provide `SSO_THREAT_MITIGATION_SUCCESS`.
  * For successful user password reset, provide `ADMIN_ME_PASSWORD_CHANGE_SUCCESS`.


The following is an example of a request body to the Mitigate Risk endpoint for John Doe because he successfully signed in to the access management system from the IP address `10.11.12.13`.```
  curl -X POST \
 https://<domainURL>/admin/v1/sdk/adaptive/MitigateRisks \
   -H 'Content-Type: application/json' \
   -H 'Authorization: Bearer <Access_Token>' \
 -d '{
  "userName": "johndoe@example.com",
  "data": [
    {
      "name": "device",
      "value": "{\"currentTime\":\"Thu Nov 14 2019 10:11:18 GMT-0700 (Pacific Daylight Time)\",\"screenWidth\":1440,\"screenHeight\":900,\"screenColorDepth\":24,\"screenPixelDepth\":24,\"windowPixelRatio\":2,\"language\":\"en-US\",\"userAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36\"}"
    },
    {
      "name": "client-ip",
      "value": "10.11.12.13"
    }
  ],
  "event": "SSO_THREAT_MITIGATION_SUCCESS"
}'
```

The following is an example of response body of the populate risk endpoint:```
{
  "userName": "johndoe@example.com",
  "riskLevel": "LOW",
  "riskScores": [
    {
      "lastUpdateTimestamp": 1574726401582,
      "score": 10,
      "riskLevel": "LOW",
      "providerId": "ORACLE_IDCS",
      "providerStatus": "ACTIVE",
      "providerDescription": "Default Risk Provider",
      "reference": "https://<domainURL>/admin/v1/RiskProviderProfiles/ORACLE_IDCS"
    }
  ]
}
```

Was this article helpful?
YesNo

