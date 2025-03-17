Updated 2024-04-02
# Enrolling in MFA using the SMS Factor Using Self Service
This use case provides a step-by-step example of using the identity domains REST API for Self-Service enrollment in Multifactor Authentication (MFA) using SMS Factor.
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
As a prerequisite step, you must obtain a ME token before following these steps. See [Generating Access Token Using Authentication API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken "This use case provides a step-by-step example of using the identity domains to generate access token using authentication API. The user gets user information through Me Access Token using Authentication API.") for information on obtaining a ME token.
There are three steps in this use case. Each step contains request and response examples:
  * [Step 1: Create the Self Service Enrollment Using the SMS Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_ycs_cy3_xhb)
  * [Step 2: Initiate the Self Service Enrollment Using the OTP by SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_o3z_3y3_xhb)
  * [Step 2a: Initiate the Self Service Enrollment Request to Resend OTP by SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_cnv_brw_23b)
  * [Step 3: Validate the Self Service Enrollment Using the OTP](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_hkk_hz3_xhb)


**Note** These steps assume that relevant factors of MFA are enabled using [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
## Step1: Create the Self Service Enrollment Using the SMS Factor 🔗 
This step initiates SMS enrollment in a POST request to the `/admin/v1/MyAuthenticationFactorEnroller` endpoint. The client must include the following attributes: 
  * `value`: defines the user id. You can make a GET call to `{{HOST}}/admin/v1/Me` to get the "id" value.
  * `displayName`: defines the display name for the device 
  * `countryCode`: defines the country code of the phone number where the SMS text will be sent
  * `phoneNumber`: defines the phone number where the SMS text will be sent


## Request Example
The following example shows the contents of the POST request body in JSON format: 
```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorEnroller"
 ],
 "user": {
  "value": "c810ff4522eb437abac013291c1984d1"
 },
 "displayName": "Joe's Personal Phone",
 "countryCode": "+44",
 "phoneNumber": "1122334455",
 "authnFactors": [
  "SMS"
 ]
} 
```

## Response Example
The following example shows the contents of the response body in JSON format: 
```
{
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorEnroller"
  ],
  "user": {
    "value": "c810ff4522eb437abac013291c1984d1",
    "$ref": "https://example.identitycloud.com/admin/v1/Users/c810ff4522eb437abac013291c1984d1"
  },
  "displayName": "Joe's Personal Phone",
  "countryCode": "+44",
  "phoneNumber": "XXXXXXX455",
  "authnFactors": [
    "SMS"
  ],
  "meta": {
    "resourceType": "MyAuthenticationFactorEnroller",
    "location": "https://example.identitycloud.com/admin/v1/MyAuthenticationFactorEnroller"
  },
  "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
  "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179"
}
```

In the response, the `deviceId` and the `requestId` should be passed in the next step. 
## Error Response Examples
The following example shows the error message in JSON format when the `userId` is invalid. You get a 400 HTTP response code. ```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:Error",
    "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error"
  ],
  "detail": "AuthenticationFactorEnroller.user references a User with ID 1fa35f74491d44ef5a7cc25bfdb1c8b1c that does not exist.",
  "status": "400",
  "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error": {
    "messageId": "error.common.validation.invalidReferenceResource"
  }
}
```

The following example shows the error message in JSON format if a `phoneNumber` is incorrect. You get a 400 HTTP response code.
```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:Error",
    "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error"
  ],
  "detail": "Your phone number +91123 is not valid.",
  "status": "400",
  "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error": {
    "messageId": "error.ssocommon.auth.invalidPhoneNumber",
    "additionalData": {
      "params": "+91123",
      "msgId": "error.ssocommon.auth.invalidPhoneNumber"
    }
  }
}
```

## Step 2: Initiate the Self Service Enrollment Using the OTP by SMS 🔗 
This step requests that the OTP be sent through SMS in a POST request to the `/admin/v1/MyAuthenticationFactorInitiator` endpoint. The client must include the following attributes: 
`requestId:` received in the Step 1 response
`deviceId:` received in the Step 1 response
`userName:` username of the user
## Request Example
The following example shows the contents of the POST request body in JSON format:
```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
 ],
 "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
 "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
 "userName": "jbloggs",
 "authFactor": "SMS"
}
```

## Response Example
The following example shows the contents of the response in JSON format:
```
{
  "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
  "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
  "authFactor": "SMS",
  "userName": "jbloggs",
  "displayName": "Joe's Personal Phone",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
  ]
}
```

An OTP code is sent by using SMS to the user's mobile device. In the response `deviceId` and `requestId` should be passed in the next step. 
## 2a. Initiate the Self Service Enrollment Request to Resend OTP by SMS 🔗 
In case the user wants the server to "resend" the OTP, then same payload as mentioned in the [Step 2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__section_xnc_3y5_ngb) should be sent to the server again.
## Request Example
The following example shows the contents of the POST request body in JSON format:
```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
 ],
 "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
 "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
 "userName": "jbloggs",
 "authFactor": "SMS"
}
```

## Response Example
The following example shows the contents of the response in JSON format:
```
{ 
  "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
  "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
  "authFactor": "SMS",
  "userName": "jbloggs",
  "displayName": "Joe's Personal Phone",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
  ]
}
```

An OTP code is sent using SMS to the user's mobile device. In the response `deviceId` and `requestId` should be passed in the next step. 
## Step 3: Validate the Self Service Enrollment Using the OTP 🔗 
This step validates the SMS enrollment of a user in a POST request to the `/admin/v1/MyAuthenticationFactorValidator` endpoint. 
The client must include the following attributes:
  * `otpCode:` the code received by the user on their device 
  * `requestId:` received in the Step 2 response 
  * `deviceId:` received in the Step 2 response


**Request Example**
The following example shows the contents of the POST request in JSON format: 
```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorValidator"
 ],
 "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
 "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
 "otpCode": "191224",
 "authFactor": "SMS",
 "scenario": "ENROLLMENT"
}
  
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{
  "authFactor": "SMS",
  "deviceId": "92142250e2ab4608b5c6532eb73e3d7c",
  "requestId": "a0a7f9bf-13a8-43f3-bcc7-2087dc3f7a18o-o1548346179",
  "scenario": "ENROLLMENT",
  "status": "SUCCESS",
  "displayName": "Joe's Personal Phone",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorValidator"
  ],
  "mfaStatus": "ENROLLED",
  "mfaPreferredDevice": "2b27b8c072d64b899d41c8470acea32a",
  "mfaPreferredAuthenticationFactor": "SMS",
  "securityQuestionsPresent": false,
  "devicesCount": 3,
  "emailFactorEnrolled": true
} 
```

In the response, the attribute `mfaStaus:"ENROLLED"` indicates that user has enrolled for MFA. The `mfapreferredAuthenticationFactor` attribute indicates the factor set as the preferred method. In this case, it's SMS.
**Note** This value may be different, if the first enrolled factor is different from SMS.
## Error Response Examples
The following example shows the error message in JSON format if OTP is incorrect. You get a 401 HTTP response code and the enrollment fails.
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:Error",
  "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error"
 ],
 "detail": "Invalid passcode.",
 "status": "401",
 "urn:ietf:params:scim:api:oracle:idcs:extension:messages:Error": {
  "messageId": "error.ssocommon.auth.invalidPasscode"
 }
}
```

Was this article helpful?
YesNo

