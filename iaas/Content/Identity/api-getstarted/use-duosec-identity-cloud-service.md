Updated 2024-05-29
# Using Duo Security with Identity Domains
These use cases provide a step-by-step example of using Duo Web SDK v2 or Duo Web SDK v4 with an identity domain.
  * [Updating the Authentication Factor Settings with Duo Security Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_qpm_p2h_4jb)
  * [Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4 "Duo Web SDK v2 \(iFrame\) is enabled in an identity domain by default. To use Duo Web SDK v4, you must enable it.")
  * [Authenticating User Name and Password with Duo Security as an Authentication Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_uwx_chp_mjb "This use case provides a step-by-step example of using the identity domains REST API to authenticate users and perform multifactor enrollment and authentication with Duo Web SDK v2 or Duo Web SDK v4.")
  * [Enrolling in MFA with Duo Security Using Self Service](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security "This use case provides a step-by-step example of using the identity domains REST API for self-service enrollment in Multifactor Authentication \(MFA\) using Duo Security.")


## Updating the Authentication Factor Settings with Duo Security Settings 🔗 
The following example shows how to update Multifactor Authentication settings for a tenant by submitting a PUT request on the REST resource using cURL. For more information about cURL, see [Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
### cURL Command
**Note** The command in this example uses the URL structure `https://<domainURL>/resource-path`, where `<domainURL>` represents the Identity Service URL, and the resource path represents the Identity Service API. See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for the appropriate URL structure to use.
```
  curl
-X PUT
  -H "Content-Type:application/scim+json"
  -H "Authorization: Bearer <Access Token Value>"
https://<domainURL>/admin/v1/AuthenticationFactorSettings/<ID>
```

### Request Body
The following shows an example of the request body in JSON format:
[Example Request Body](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm)
```
{
 "bypassCodeSettings": {
  "helpDeskCodeExpiryInMins": 60,
  "helpDeskGenerationEnabled": true,
  "helpDeskMaxUsage": 5,
  "length": 12,
  "maxActive": 5,
  "selfServiceGenerationEnabled": true
 },
 "clientAppSettings": {
  "deviceProtectionPolicy": "NONE",
  "initialLockoutPeriodInSecs": 30,
  "keyPairLength": 2048,
  "lockoutEscalationPattern": "Constant",
  "maxFailuresBeforeLockout": 10,
  "maxFailuresBeforeWarning": 5,
  "maxLockoutIntervalInSecs": 86400,
  "minPinLength": 6,
  "policyUpdateFreqInDays": 7,
  "requestSigningAlgo": "SHA256withRSA",
  "sharedSecretEncoding": "Base32",
  "unlockAppForEachRequestEnabled": false,
  "unlockAppIntervalInSecs": 300,
  "unlockOnAppForegroundEnabled": false,
  "unlockOnAppStartEnabled": false
 },
 "compliancePolicy": [
  {
   "action": "Allow",
   "name": "lockScreenRequired",
   "value": "false"
  },
  {
   "action": "Allow",
   "name": "lockScreenRequiredUnknown",
   "value": "false"
  },
  {
   "action": "Allow",
   "name": "jailBrokenDevice",
   "value": "false"
  },
  {
   "action": "Allow",
   "name": "jailBrokenDeviceUnknown",
   "value": "false"
  },
  {
   "action": "Allow",
   "name": "minWindowsVersion",
   "value": "8.1"
  },
  {
   "action": "Allow",
   "name": "minIosVersion",
   "value": "7.1"
  },
  {
   "action": "Allow",
   "name": "minAndroidVersion",
   "value": "4.1"
  },
  {
   "action": "Allow",
   "name": "minIosAppVersion",
   "value": "4.0"
  },
  {
   "action": "Allow",
   "name": "minAndroidAppVersion",
   "value": "8.0"
  },
  {
   "action": "Allow",
   "name": "minWindowsAppVersion",
   "value": "1.0"
  }
 ],
 "endpointRestrictions": {
  "maxEndpointTrustDurationInDays": 15,
  "maxEnrolledDevices": 5,
  "maxTrustedEndpoints": 5,
  "trustedEndpointsEnabled": true,
  "maxIncorrectAttempts": 10
 },
 "id": "AuthenticationFactorSettings",
 "mfaEnrollmentType": "Required",
 "pushEnabled": false,
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorSettings"
 ],
 "thirdPartyFactor": {
    "duoSecurity": true
  },
 "notificationSettings": {
    "pullEnabled": true
  },
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings": {
    "duoSecuritySettings": {
      "integrationKey": "XXXXXXXXXXXXXXXXXXXX",
      "secretKey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "apiHostname": "api-example.duosecurity.com",
      "userMappingAttribute": "userName"
  }
  },
 "securityQuestionsEnabled": false,
 "smsEnabled": false,
 "emailEnabled": false,
 "bypassCodeEnabled": false,
 "totpEnabled": false,
 "totpSettings": {
  "hashingAlgorithm": "SHA1",
  "jwtValidityDurationInSecs": 300,
  "keyRefreshIntervalInDays": 60,
  "passcodeLength": 6,
  "smsOtpValidityDurationInMins": 10,
  "smsPasscodeLength": 6,
  "timeStepInSecs": 30,
  "timeStepTolerance": 3,
	"emailOtpValidityDurationInMins": 10,
	"emailPasscodeLength": 6
 },
 "mfaEnabledCategory": "NONE"
}
```

### Response Body
The following example shows the contents of the response body in JSON format:
[Example Response Body](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm)
```
{
  "bypassCodeSettings": {
    "helpDeskCodeExpiryInMins": 60,
    "helpDeskGenerationEnabled": true,
    "helpDeskMaxUsage": 5,
    "length": 12,
    "maxActive": 5,
    "selfServiceGenerationEnabled": true
  },
  "clientAppSettings": {
    "deviceProtectionPolicy": "NONE",
    "initialLockoutPeriodInSecs": 30,
    "keyPairLength": 2048,
    "lockoutEscalationPattern": "Constant",
    "maxFailuresBeforeLockout": 10,
    "maxFailuresBeforeWarning": 5,
    "maxLockoutIntervalInSecs": 86400,
    "minPinLength": 6,
    "policyUpdateFreqInDays": 7,
    "requestSigningAlgo": "SHA256withRSA",
    "sharedSecretEncoding": "Base32",
    "unlockAppForEachRequestEnabled": false,
    "unlockAppIntervalInSecs": 300,
    "unlockOnAppForegroundEnabled": false,
    "unlockOnAppStartEnabled": false
  },
  "compliancePolicy": [
    {
      "action": "Allow",
      "name": "lockScreenRequired",
      "value": "false"
    },
    {
      "action": "Allow",
      "name": "lockScreenRequiredUnknown",
      "value": "false"
    },
    {
      "action": "Allow",
      "name": "jailBrokenDevice",
      "value": "false"
    },
    {
      "action": "Allow",
      "name": "jailBrokenDeviceUnknown",
      "value": "false"
    },
    {
      "action": "Allow",
      "name": "minWindowsVersion",
      "value": "8.1"
    },
    {
      "action": "Allow",
      "name": "minIosVersion",
      "value": "7.1"
    },
    {
      "action": "Allow",
      "name": "minAndroidVersion",
      "value": "4.1"
    },
    {
      "action": "Allow",
      "name": "minIosAppVersion",
      "value": "4.0"
    },
    {
      "action": "Allow",
      "name": "minAndroidAppVersion",
      "value": "8.0"
    },
    {
      "action": "Allow",
      "name": "minWindowsAppVersion",
      "value": "1.0"
    }
  ],
  "endpointRestrictions": {
    "maxEndpointTrustDurationInDays": 15,
    "maxEnrolledDevices": 5,
    "maxTrustedEndpoints": 5,
    "trustedEndpointsEnabled": true,
    "maxIncorrectAttempts": 10
  },
  "id": "AuthenticationFactorSettings",
  "mfaEnrollmentType": "Required",
  "pushEnabled": false,
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorSettings"
  ],
  "thirdPartyFactor": {
    "duoSecurity": true
  },
  "notificationSettings": {
    "pullEnabled": true
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings": {
    "duoSecuritySettings": {
      "integrationKey": "XXXXXXXXXXXXXXXXXXXX",
      "secretKey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "apiHostname": "api-example.duosecurity.com",
      "userMappingAttribute": "userName"
    }
  },
  "securityQuestionsEnabled": false,
  "smsEnabled": false,
  "emailEnabled": false,
  "bypassCodeEnabled": false,
  "totpEnabled": false,
  "totpSettings": {
    "hashingAlgorithm": "SHA1",
    "jwtValidityDurationInSecs": 300,
    "keyRefreshIntervalInDays": 60,
    "passcodeLength": 6,
    "smsOtpValidityDurationInMins": 10,
    "smsPasscodeLength": 6,
    "timeStepInSecs": 30,
    "timeStepTolerance": 3,
    "emailOtpValidityDurationInMins": 10,
    "emailPasscodeLength": 6
  },
  "meta": {
    "lastModified": "2022-10-15T07:44:53.601Z",
    "resourceType": "AuthenticationFactorSettings",
    "created": "2022-10-04T06:56:10.285Z",
    "location": "https://<domainURL>/admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings"
  },
  "idcsLastModifiedBy": {
    "value": "5753639d3ca046f094a8f4aeaf9ea5e5",
    "type": "App",
    "display": "testPostman",
    "$ref": "https://<domainURL>/admin/v1/Apps/5753639d3ca046f094a8f4aeaf9ea5e5"
  },
  "idcsCreatedBy": {
    "value": "c480fd39014e40f3bf4f963b3b6a423b",
    "type": "App",
    "display": "idcssm",
    "$ref": "https://<domainURL>/admin/v1/Apps/c480fd39014e40f3bf4f963b3b6a423b"
  },
  "mfaEnabledCategory": "NONE"
}
```

## Enabling Duo Web SDK v4 🔗 
Duo Web SDK v2 (iFrame) is enabled in an identity domain by default. To use Duo Web SDK v4, you must enable it.
Use the following instructions to enable Duo Web SDK v4.
  1. Using cURL, `GET /admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings`
**Response Example**
You should see the following Duo Web SDK v2 settings.
```
"urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings": {
  "duoSecuritySettings": {
   "integrationKey": "<integration-key>",
   "secretKey": "<secret-key>",
   "apiHostname": "api-example.duosecurity.com",
   "userMappingAttribute": "userName"
}
```

  2. Backup your instance in case rollback is required.
  3. Update the payload from step 1 by adding `enableWebSDKv4` and `duoSecurityAuthzRedirectUrl` under the `urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings` section.
     * `enableWebSDKv4`: The default value is `false`. If `enableWebSDKv4` is false, Duo Web SDK v2 is used. 
     * `duoSecurityAuthzRedirectUrl`: The default value is blank. Add your organization's URL here. The redirect URL is used to initiate Duo security authentication, which receives a response from the Duo security server with the `duoSecurityAuthzState` and `duoSecurityAuthzCode`. This URL can be overridden by using the custom UI. The custom UI must use this endpoint to receive the code and parameter from the Duo Security Server. 
Note the following attribute changes from v2 to v4.
     * `client_id` (`integrationKey` in v2)
     * `clientSecret` (`secretKey` in v2)
     * `apiHostName` (no change from v2)
     * `userMappingAttribute` (no change from v2)
**Request Example**
```
"urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings": {
  "duoSecuritySettings": {
    "integrationKey": "<integration-key>",
    "secretKey": ""<secret-key>"",
    "apiHostname": "api-6ff7f509.duosecurity.com",
    "userMappingAttribute": "primaryEmail",
    "enableWebSDKv4": true,
    "duoSecurityAuthzRedirectUrl": "https://abc.co/a/c"
  }
}
```

  4. Using cURL, `PUT /admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings` using step 3 payload.


## Authenticating User Name and Password with Duo Security as an Authentication Factor 🔗 
This use case provides a step-by-step example of using the identity domains REST API to authenticate users and perform multifactor enrollment and authentication with Duo Web SDK v2 or Duo Web SDK v4.
**Note**
  * Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
  * This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.


**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
The following example sets are included in this use case: 
  * [Enroll a New User with Duo Security Using Web SDK v2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb "This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v2.")
  * [Enroll a New User with Duo Security Using Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#unique_1442166793 "This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v4.")
  * [Authenticate a User Account with Duo Security Using Web SDK v2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb "This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v2.")
  * [Authenticate a User Account with Duo Security Using Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#unique_1237012178 "This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v4.")
  * [Authenticate a User with Duo Security When Used as a Backup Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb "This use case provides a step-by-step example of using the identity domains REST API to authenticate a user account with Duo Security even when it's configured as a backup factor.")
  * [Set Duo Security as the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor "This use case provides a step-by-step example of using the identity domains REST API to set Duo Security as the preferred factor for authentication.")
  * [Support Trusted Device When Using Duo as an Authentication Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor "This use case provides a step-by-step example of using the identity domains REST API to support trusted device when using Duo as an authentication factor.")


### Enroll a New User with Duo Security Using Web SDK v2 🔗 
This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v2.
**Note**
  * Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
  * This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.


**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_inc_rdj_mjb)
  * [Step 3: Initiate Duo Security Enrollment Request](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_lzs_5z3_mjb)
  * [Step 4: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_fnh_1wg_4jb)
  * [Step 5: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_bjw_51j_mjb)
  * [Step 6: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_r34_kcj_mjb)


**Note** These steps assume that MFA is enabled and a sign-on policy is created for MFA. See [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "nextAuthFactors": [
    "TOTP",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY",
    "SMS",
    "EMAIL",
    "PUSH"
  ],
  "EnrolledAccountRecoveryFactorsDetails": {
    "EMAIL": {
      "credentials": [
        "accountRecoveryFactor"
      ],
      "enrolledDevices": [
        {
          "displayName": "clarence.saladna@example.com"
        }
      ]
    },
    "enrolledAccRecFactorsList": [
      "EMAIL"
    ]
  },
  "TOTP": {
    "credentials": [
      "offlineTotp"
    ]
  },
  "SMS": {
    "credentials": [
      "phoneNumber",
      "countryCode"
    ]
  },
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In this use case example, enrollment is sent in the next step to initiate enrollment for the user.
#### Step 3: Initiate Duo Security Enrollment Request 🔗 
This step initiates Duo Security enrollment. The client must include the following attributes:
  * `op`: tells the server what kind of operation the client wants
  * `authFactor`: defines which authentication factor that the user wants to enroll in
  * `requestState`: received in the Step 2 response


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "enrollment",
  "authFactor": "DUO_SECURITY",
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the request in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "DUO_SECURITY": {
   "credentials": [
     "duoSecurityResponse"
   ],
   "authnDetails": {
     "duoSecurityChallenge": "TX
     |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjMwNTM=
     |5853cc561ded98c72426b633a1b1e719401e2345:APP
     |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjYzNTM=
     |37f594101a380ff3902e0a2cb545346ed196bbca",
     "duoSecurityHost": "api-example.duosecurity.com"
   }
  },
  "nextOp": [
    "credSubmit",
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `credSubmit` is sent in the next step.
#### Step 4: Initiate Duo Security Authentication 🔗 
Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.
After primary authentication, you must pass the authentication details such as `duoSecurityHost` and `duoSecurityChallenge` that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```
function duo(msg, duoSecurityCallback) {
  Duo.init({iframe: "duo_iframe",
      host: msg.DUO_SECURITY.authnDetails.duoSecurityHost,
      sig_request: msg.DUO_SECURITY.authnDetails.duoSecurityChallenge,
      submit_callback: duoSecurityCallback,
      post_argument: "resp"
  });
}
```

After completing the Duo authentication process, Duo calls the `duoSecurityCallback` method to get a Duo response.
```
var duoSecurityCallback = function(details, credentials) {
    var credentials = {};
    credentials.duoSecurityResponse = details.firstElementChild.value;
    operation = "credSubmit";
    initiateAuth(credentials); 
}
```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.
#### Step 5: Submit Factor Credentials 🔗 
This step submits the factor credentials in the requestState that were received in the Step 3 response. Note that the request payload doesn't contain the authFactor attribute because the requestState contains it. The client must include the following attributes:
  * `op`: tells the server what kind of operation the client wants
  * `requestState`: received in the Step 3 response


**Request Example**
The following example shows the contents of the POST request in JSON format to submit the factor credentials:
```
{ 
  "op":"credSubmit",
  "credentials": { 
    "duoSecurityResponse": "AUTH
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjM5NjA=
   |f2d0df2a189219a8e85db190ac66fab33be996c3:APP
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1Njc0NTU=
   |a3b7c901e845ebd80451ab670473e983707a8459"
  },
  "requestState":"{{requestState}}"
}

```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "displayName": "{{username}}'s Duo Security Account",
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

The `nextOp` values indicate what can be sent as the `op` value in the next request. In this use case example, `createToken` is sent in the next step.
#### Step 6: Create the Authentication Token 🔗 
This step indicates that the client is done and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
  * `op`: tells the server what kind of operation the client wants
  * `requestState`: received in the Step 5 response


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{ 
  "op":"createToken",
  "requestState":"{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{ "authnToken": "{{authnToken}}", "status": "success" }
```

### Enroll a New User with Duo Security Using Web SDK v4 🔗 
This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v4.
**Note** If you need to enable Duo Web SDK v4, see [Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4 "Duo Web SDK v2 \(iFrame\) is enabled in an identity domain by default. To use Duo Web SDK v4, you must enable it.").
**Note**
  * Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
  * This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.


**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_inc_rdj_mjb)
  * [Step 3: Initiate Duo Security Enrollment Request](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_lzs_5z3_mjb)
  * [Step 4: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_fnh_1wg_4jb)
  * [Step 5: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_bjw_51j_mjb)
  * [Step 6: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_r34_kcj_mjb)


**Note** These steps assume that MFA is enabled and a sign-on policy is created for MFA. See [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "nextAuthFactors": [
    "TOTP",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY",
    "SMS",
    "EMAIL",
    "PUSH"
  ],
  "EnrolledAccountRecoveryFactorsDetails": {
    "EMAIL": {
      "credentials": [
        "accountRecoveryFactor"
      ],
      "enrolledDevices": [
        {
          "displayName": "clarence.saladna@example.com"
        }
      ]
    },
    "enrolledAccRecFactorsList": [
      "EMAIL"
    ]
  },
  "TOTP": {
    "credentials": [
      "offlineTotp"
    ]
  },
  "SMS": {
    "credentials": [
      "phoneNumber",
      "countryCode"
    ]
  },
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In this use case example, enrollment is sent in the next step to initiate enrollment for the user.
#### Step 3: Initiate Duo Security Enrollment Request 🔗 
**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "enrollment",
  "authFactor": "DUO_SECURITY",
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the request in JSON format.
```
{
  "status": "success",
  "ecId": "i2tul0R0000000000",
  "nextAuthFactors": [
   "DUO_SECURITY"
  ],
  "DUO_SECURITY": {
   "credentials": [
     "duoSecurityAuthzCode",
     "duoSecurityAuthzState"
   ],
   "authnDetails": {
     "duoSecurityAuthzRequest": "https://api-xxxxxxxx.duosecurity.com/oauth/v1/authorize?response_type=code&client_id=<client_id>&redirect_uri=duoSecurityAuthzRedirectURL&state=3047103d-d707-4b94-a960-203430071154&request=<request>"
   }
  },
  "nextOp": [
   "credSubmit",
   "getBackupFactors"
  ],
  "scenario": "AUTHENTICATION",
  "requestState": "requestState",
  "trustedDeviceSettings": {
   "trustDurationInDays": 15
  }
}

```

#### Step 4: Initiate Duo Security Authentication 🔗 
During Duo Security authentication, the browser redirects to the Duo Security Server, the Duo Security Server then loads the secondary authentication page where the user performs the secondary authentication. After successful authentication, the Duo Security Server responds with the state (duoSecurityAuthzState) and code (duoSecurityAuthzCode) parameters. These parameters must be submitted to the identity domain to complete authentication.
Use the following steps to get the state and code parameters:
  1. Get the URL to redirect to from `duoSecurityAuthzRequest`.
For example: ```
"duoSecurityAuthzRequest": "https://api-xxxxxxxx.duosecurity.com/oauth/v1/authorize?response_type=code&client_id=<client_id>&redirect_uri=duoSecurityAuthzRedirectURL&state=3047103d-d707-4b94-a960-203430071154&request=<request>"
```

The is the redirect URL for `duoSecurityAuthzRedirectURL`.
  2. Do 303 Redirect to the Duo Security Server.
  3. Complete the Duo Security enrollment and authentication process.
The Duo Security Server redirects back to `duoSecurityAuthzRedirectURL` with `duoSecurityAuthzState` and `duoSecurityAuthzCode`. 


#### Step 5: Submit Factor Credentials 🔗 
Pass `duoSecurityAuthzState` and `duoSecurityAuthzCode` from the response to the identity domain to complete authentication.
**Request Example**
The following example shows the contents of the request in JSON format:
```
{
  "op": "credSubmit",
  "credentials":
  {
   "duoSecurityAuthzCode": "<duo-security-authz-code>",
   "duoSecurityAuthzState": "<duo-security-authz-state>"
  }
,
  "requestState": "requestState"}'
```

**Response Example**
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "displayName": "{{username}}'s Duo Security Account",
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

#### Step 6: Create the Authentication Token 🔗 
This step indicates that the client is done and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
  * `op`: tells the server what kind of operation the client wants
  * `requestState`: received in the Step 5 response


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{ 
  "op":"createToken",
  "requestState":"{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{ "authnToken": "{{authnToken}}", "status": "success" }
```

### Authenticate a User Account with Duo Security Using Web SDK v2 🔗 
This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v2.
**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_wz2_54k_mjb)
  * [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_jk4_gxg_4jb)
  * [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_orw_spk_mjb)


**Note** These steps assume that MFA is enabled and a sign-on policy is created for MFA. See [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.")
#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "nextAuthFactors": [
    "TOTP",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY",
    "SMS",
    "EMAIL",
    "PUSH"
  ],
  "EnrolledAccountRecoveryFactorsDetails": {
    "EMAIL": {
      "credentials": [
        "accountRecoveryFactor"
      ],
      "enrolledDevices": [
        {
          "displayName": "clarence.saladna@example.com"
        }
      ]
    },
    "enrolledAccRecFactorsList": [
      "EMAIL"
    ]
  },
  "TOTP": {
    "credentials": [
      "offlineTotp"
    ]
  },
  "SMS": {
    "credentials": [
      "phoneNumber",
      "countryCode"
    ]
  },
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `credSubmit` is sent in the next step.
#### Step 3: Initiate Duo Security Authentication 🔗 
Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.
After primary authentication, you must pass the authentication details such as `duoSecurityHost` and `duoSecurityChallenge` that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```
function duo(msg, duoSecurityCallback) {
  Duo.init({iframe: "duo_iframe",
      host: msg.DUO_SECURITY.authnDetails.duoSecurityHost,
      sig_request: msg.DUO_SECURITY.authnDetails.duoSecurityChallenge,
      submit_callback: duoSecurityCallback,
      post_argument: "resp"
  });
}
```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```
var duoSecurityCallback = function(details, credentials) {
    var credentials = {};
    credentials.duoSecurityResponse = details.firstElementChild.value;
    operation = "credSubmit";
    initiateAuth(credentials); 
}
```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.
#### Step 4: Submit Factor Credentials 🔗 
This step submits the factor credentials in the `requestState` that were received in the Step 2 response. Note that the request payload doesn't contain the `authFactor` attribute because the `requestState` contains it. The client must include the following attributes:
  * `op`: tells the server what kind of operation the client wants
  * `requestState`: received in the Step 2 response


**Request Example**
The following example shows the contents of the POST request in JSON format to submit the factor credentials:
```
{ 
  "op":"credSubmit",
  "credentials": { 
    "duoSecurityResponse": "AUTH
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjM5NjA=
   |f2d0df2a189219a8e85db190ac66fab33be996c3:APP
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1Njc0NTU=
   |a3b7c901e845ebd80451ab670473e983707a8459"
  },
  "requestState":"{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "authnToken": "{{authnToken}}",
  "status": "success",
  "ecId": "5MyZ41m0000000000"
}
```

### Authenticate a User Account with Duo Security Using Web SDK v4 🔗 
This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v4.
**Note** If you need to enable Duo Web SDK v4, see [Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4 "Duo Web SDK v2 \(iFrame\) is enabled in an identity domain by default. To use Duo Web SDK v4, you must enable it.").
**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_wz2_54k_mjb)
  * [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_jk4_gxg_4jb)
  * [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_orw_spk_mjb)


**Note** These steps assume that MFA is enabled and a sign-on policy is created for MFA. See [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "nextAuthFactors": [
    "TOTP",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY",
    "SMS",
    "EMAIL",
    "PUSH"
  ],
  "EnrolledAccountRecoveryFactorsDetails": {
    "EMAIL": {
      "credentials": [
        "accountRecoveryFactor"
      ],
      "enrolledDevices": [
        {
          "displayName": "clarence.saladna@example.com"
        }
      ]
    },
    "enrolledAccRecFactorsList": [
      "EMAIL"
    ]
  },
  "TOTP": {
    "credentials": [
      "offlineTotp"
    ]
  },
  "SMS": {
    "credentials": [
      "phoneNumber",
      "countryCode"
    ]
  },
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `credSubmit` is sent in the next step.
#### Step 3: Initiate Duo Security Authentication 🔗 
During Duo Security authentication, the browser redirects to the Duo Security Server, the Duo Security Server then loads the secondary authentication page where the user performs the secondary authentication. After successful authentication, the Duo Security Server responds with the state (duoSecurityAuthzState) and code (duoSecurityAuthzCode) parameters. These parameters must be submitted to the identity domain to complete authentication.
Use the following steps to get the state and code parameters:
  1. Get the URL to redirect to from `duoSecurityAuthzRequest`.
For example: ```
"duoSecurityAuthzRequest": "https://api-xxxxxxxx.duosecurity.com/oauth/v1/authorize?response_type=code&client_id=<client_id>&redirect_uri=duoSecurityAuthzRedirectURL&state=3047103d-d707-4b94-a960-203430071154&request=<request>"
```

The is the redirect URL for `duoSecurityAuthzRedirectURL`.
  2. Do 303 Redirect to the Duo Security Server.
  3. Complete the Duo Security enrollment and authentication process.
The Duo Security Server redirects back to `duoSecurityAuthzRedirectURL` with `duoSecurityAuthzState` and `duoSecurityAuthzCode`. 


#### Step 4: Submit Factor Credentials 🔗 
Pass `duoSecurityAuthzState` and `duoSecurityAuthzCode` from the response to the identity domain to complete authentication.
**Request Example**
The following example shows the contents of the request in JSON format:
```
{
  "op": "credSubmit",
  "credentials":
  {
   "duoSecurityAuthzCode": "<duo-security-authz-code>",
   "duoSecurityAuthzState": "<duo-security-authz-state>"
  }
,
  "requestState": "requestState"}'
```

**Response Example**
```
{
  "authnToken": "{{authnToken}}",
  "status": "success",
  "ecId": "5MyZ41m0000000000"
}
```

### Authenticate a User with Duo Security When Used as a Backup Factor 🔗 
This use case provides a step-by-step example of using the identity domains REST API to authenticate a user account with Duo Security even when it's configured as a backup factor.
**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_dby_jyp_mjb)
  * [Step 3: Get the List of Backup Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_rk2_dvk_mjb)
  * [Step 4: Select Duo Security from the List of Backup Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_s4j_1wk_mjb)


#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "4uy3^1k0000000000",
  "nextAuthFactors": [
    "TOTP",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY",
    "SMS",
    "EMAIL",
    "PUSH"
  ],
  "EnrolledAccountRecoveryFactorsDetails": {
    "EMAIL": {
      "credentials": [
        "accountRecoveryFactor"
      ],
      "enrolledDevices": [
        {
          "displayName": "clarence.saladna@example.com"
        }
      ]
    },
    "enrolledAccRecFactorsList": [
      "EMAIL"
    ]
  },
  "TOTP": {
    "credentials": [
      "offlineTotp"
    ]
  },
  "SMS": {
    "credentials": [
      "phoneNumber",
      "countryCode"
    ]
  },
  "nextOp": [
    "createToken",
    "createSession",
    "enrollment"
  ],
  "mfaSettings": {
    "enrollmentRequired": false
  },
  "scenario": "ENROLLMENT",
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `getBackupFactors` is sent in the next step.
#### Step 3: Get the List of Backup Factors 🔗 
This step enables you to get the list of backup factors.
**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "getBackupFactors",
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "5MyZ41p0000000000",
  "nextAuthFactors": [
    "EMAIL",
    "BYPASSCODE",
    "SECURITY_QUESTIONS",
    "DUO_SECURITY"
  ],
  "EMAIL": {
    "credentials": [
      "preferred",
      "deviceId"
    ],
    "enrolledDevices": [
      {
        "deviceId": "790ed820aee048a78de17ebe1ebddb19",
        "displayName": "ashXXXXX@oracle.com"
      }
    ]
  },
  "BYPASSCODE": {
    "credentials": [
      "bypassCode"
    ]
  },
  "SECURITY_QUESTIONS": {
    "credentials": [
      "questionId",
      "answer"
    ],
    "questions": [
      {
        "questionId": "FirstCar",
        "text": "What's the model of your first car?"
      }
    ],
    "preferred": true
  },
  "DUO_SECURITY": {
    "enrolledDevices": [
      {
        "deviceId": "3053eed6249a4dd4835c51bf873c5f85",
        "displayName": "jarvis's Duo Security Account"
      }
    ]
  },
  "nextOp": [
    "credSubmit",
    "getBackupFactors"
  ],
  "scenario": "AUTHENTICATION",
  "requestState": "{{requestState}}",
  "trustedDeviceSettings": {
    "trustDurationInDays": 15
  }
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 4: Select Duo Security from the List of Backup Factors 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "authFactor": "DUO_SECURITY",
  "credentials": {
    "deviceId": "3053eed6249a4dd4835c51bf873c5f85"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
	"status": "success",
	"ecId": "5MyZ41q0000000000",
	"DUO_SECURITY": {
	"credentials": [
		 "duoSecurityResponse"
	],
	"authnDetails": {
		"duoSecurityChallenge": "TX
			 |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjQ1NDg=
			 |230d8328f53ec537ecd033fbb175fbce65930c3e:APP
			 |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1Njc4NDg=
			 |af94d927d3e027141177e8f88baa19f6427502ee",
		  "duoSecurityHost": "api-example.duosecurity.com"
		}
	},
	"nextOp": [
		"credSubmit",
	    "getBackupFactors"
	],
	"scenario": "AUTHENTICATION",
	"requestState": "{{requestState}}",
	"trustedDeviceSettings": {
		"trustDurationInDays": 15
	}
}
```

### Set Duo Security as the Preferred Factor 🔗 
This use case provides a step-by-step example of using the identity domains REST API to set Duo Security as the preferred factor for authentication.
You can set the `preferred` flag to `true` to make Duo Security as a preferred factor, if a user already has other factor other than Duo Security as preferred.
**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__submit-user-credentials)
  * [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__initiate-duo-sec-auth)
  * [Step 4: Enable Duo Security as the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__enable-duo-preferred-factor)


#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "g5CAF1i1000000000",
  "nextAuthFactors": [
   "DUO_SECURITY"
  ],
  "DUO_SECURITY": {
   "credentials": [
     "duoSecurityResponse"
   ],
   "authnDetails": {
     "duoSecurityChallenge": "TX
      |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjM2Njc=
      |73894f83e7ee87c81388f84b4c0015cb86c6fd0b:APP
      |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjY5Njc=
      |11f57d2ad044abee78d3290fdff69af7c3d22d71",
     "duoSecurityHost": "api-example.duosecurity.com"
   }
  },
  "nextOp": [
   "credSubmit",
   "getBackupFactors"
  ],
  "scenario": "AUTHENTICATION",
  "requestState": "{{requestState}}",
  "trustedDeviceSettings": {
   "trustDurationInDays": 15
  }
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `credSubmit` is sent in the next step.
#### Step 3: Initiate Duo Security Authentication 🔗 
Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.
After primary authentication, you must pass the authentication details such as `duoSecurityHost` and `duoSecurityChallenge` that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```
function duo(msg, duoSecurityCallback) {
  Duo.init({iframe: "duo_iframe",
      host: msg.DUO_SECURITY.authnDetails.duoSecurityHost,
      sig_request: msg.DUO_SECURITY.authnDetails.duoSecurityChallenge,
      submit_callback: duoSecurityCallback,
      post_argument: "resp"
  });
}
```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```
var duoSecurityCallback = function(details, credentials) {
    var credentials = {};
    credentials.duoSecurityResponse = details.firstElementChild.value;
    operation = "credSubmit";
    initiateAuth(credentials); 
}
```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.
#### Step 4: Enable Duo Security as the Preferred Factor 🔗 
This step enables Duo Security as the preferred factor. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
 "op": "credSubmit",
 "credentials": {
  "duoSecurityResponse": "AUTH
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjQzMzg=
   |4a40cc9c79d4a65b48d0f9b871d7a4e83481b3ca:APP
   |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1Njc4NDg=
   |af94d927d3e027141177e8f88baa19f6427502ee",
  "preferred": true
 },
 "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "authnToken": "{{authnToken}}",
  "status": "success",
  "ecId": "5MyZ41r0000000000"
}
```

### Support Trusted Device When Using Duo as an Authentication Factor 🔗 
This use case provides a step-by-step example of using the identity domains REST API to support trusted device when using Duo as an authentication factor.
**Tip** Download the identity domains authentication use case examples collection and the global variables file from the **idcs-authn-api-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__sec_begin-authn-flow)
  * [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__submit-user-cred)
  * [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__initiate-duo-auth)
  * [Step 4: Enable a Device as Trusted](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__enable-device-trusted)


#### Step 1: Begin the Authentication Flow 🔗 
Obtain the initial `requestState` to begin the authentication flow. 
**Request Example**
The following example shows the request in cURL format: 
```
  curl -X GET
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer {{access_token_value}}"
  https://<domainURL>/sso/v1/sdk/authenticate?appName={{app_name}}
```

**Note** The `appName` is optional. The `appName` is the name of the App that the client wants to access. If an `appName` is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.
**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "ecId",
 "nextOp": [
    "credSubmit"
  ],
  "nextAuthFactors": [
    "USERNAME_PASSWORD"
  ],
  "USERNAME_PASSWORD": {
    "credentials": [
      "username",
      "example-password"
    ]
  },
  "requestState": "{{requestState}}"
}
```

In the response, the `nextOp` value indicates what can be sent as the `op` value in the next request. In this use case example, `credSubmit` should be sent in the next step. The `requestState` contains contextual data needed to process the request.
#### Step 2: Submit the User's Credentials 🔗 
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
  * `credentials:` username and password
  * `requestState:` received in the Step 1 response
  * `op:` tells the server what kind of operation the client wants


**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
   "username": "{{username}}",
   "password": "{{password}}"
  },
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "status": "success",
  "ecId": "g5CAF1i1000000000",
  "nextAuthFactors": [
   "DUO_SECURITY"
  ],
  "DUO_SECURITY": {
   "credentials": [
     "duoSecurityResponse"
   ],
   "authnDetails": {
     "duoSecurityChallenge": "TX
      |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjM2Njc=
      |73894f83e7ee87c81388f84b4c0015cb86c6fd0b:APP
      |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjY5Njc=
      |11f57d2ad044abee78d3290fdff69af7c3d22d71",
     "duoSecurityHost": "api-example.duosecurity.com"
   }
  },
  "nextOp": [
   "credSubmit",
   "getBackupFactors"
  ],
  "scenario": "AUTHENTICATION",
  "requestState": "{{requestState}}",
  "trustedDeviceSettings": {
   "trustDurationInDays": 15
  }
}
```

In the response, the `nextOp` values indicate what can be sent as the op value in the next request. In this use case example, `credSubmit` is sent in the next step.
#### Step 3: Initiate Duo Security Authentication 🔗 
Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.
After primary authentication, you must pass the authentication details such as `duoSecurityHost` and `duoSecurityChallenge` that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```
function duo(msg, duoSecurityCallback) {
  Duo.init({iframe: "duo_iframe",
      host: msg.DUO_SECURITY.authnDetails.duoSecurityHost,
      sig_request: msg.DUO_SECURITY.authnDetails.duoSecurityChallenge,
      submit_callback: duoSecurityCallback,
      post_argument: "resp"
  });
}
```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```
var duoSecurityCallback = function(details, credentials) {
    var credentials = {};
    credentials.duoSecurityResponse = details.firstElementChild.value;
    operation = "credSubmit";
    initiateAuth(credentials); 
}
```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.
#### Step 4: Enable a Device as Trusted 🔗 
This step enables a device as trusted. After the device is trusted, then MFA will not be challenged even though Duo Security is enrolled.
**Request Example**
The following example shows the contents of the POST request in JSON format:
```
{
  "op": "credSubmit",
  "credentials": {
    "duoSecurityResponse": "AUTH
     |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjQ2MDY=
     |ba16e2eb734e00d9ebe6f8129ce32669437052e9:APP
     |amFydmlzfERJNThZNFhVMlFXWEVSUDQzVTRKfDE1NjE1NjgwNjc=
     |ba4f415559ff2c30b23a912a18ee5f717a398563"
  },
  "trustedDevice": true,
  "trustedDeviceDisplayName": "Postman on Windows",
  "requestState": "{{requestState}}"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{
  "authnToken": "{{authnToken}}",
  "trustToken": "{{trustToken}}",
  "status": "success",
  "ecId": "5MyZ41u0000000000"
}
```

## Enrolling in MFA with Duo Security Using Self Service 🔗 
This use case provides a step-by-step example of using the identity domains REST API for self-service enrollment in Multifactor Authentication (MFA) using Duo Security.
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-rest-clients** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
As a prerequisite step, you must obtain a ME token before following these steps. See [Generating Access Token Using Authentication API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken "This use case provides a step-by-step example of using the identity domains to generate access token using authentication API. The user gets user information through Me Access Token using Authentication API.") for information on obtaining a ME token.
Complete the following steps in this use case.
  * [Step1: Enroll a User with Duo Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_rzh_lvq_mjb)
  * [Step 2: Initiate Duo Authentication for the User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_jyr_zxq_mjb)
  * [Step 3: Validate Duo Factor for Enrollment Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_sml_ffr_mjb)


**Note** These steps assume that relevant factors of MFA are enabled using [Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
### Step1: Enroll a User with Duo Factor 🔗 
This step initiates Duo Security enrollment in a POST request to the `/admin/v1/MyAuthenticationFactorEnroller` endpoint. The client must include the following attribute: 
  * `value`: defines the user id. You can make a GET call to `{{HOST}}/admin/v1/Me` to get the "id" value.


### Request Example
The following example shows the contents of the POST request body in JSON format: 
```
{
  "authnFactors":["THIRDPARTY"],
  "thirdPartyFactor": {
    "thirdPartyVendorName" : "DUO_SECURITY",
    "thirdPartyFactorType" : "None"
  },
  "user": {
   "value" : "012832e2e63d4bfda5bc512f2b52ccbe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorEnroller"
  ]
}
```

### Response Example
The following example shows the contents of the response body in JSON format: 
```
{
  "authnFactors": [
    "THIRDPARTY"
  ],
  "thirdPartyFactor": {
    "thirdPartyFactorId": "1c3a069c240b4a9d9e6e90b9a2be8bed",
    "thirdPartyFactorType": "None",
    "thirdPartyVendorName": "DUO_SECURITY"
  },
  "user": {
    "value": "6852e4e2bc864b3b912d7bd48f9f4879",
    "$ref": "https://<domainURL>admin/v1/Users/6852e4e2bc864b3b912d7bd48f9f4879"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorEnroller"
  ],
  "meta": {
    "resourceType": "MyAuthenticationFactorEnroller",
    "location": "https://<domainURL>admin/v1/MyAuthenticationFactorEnroller"
  },
  "displayName": "test's Phone",
  "requestId": "fe520538-0da6-45a3-b23f-1256091e3f0c",
  "deviceId": "ca0ba497327c45d2a4a408301c78682b"
}
```

In the response, the `deviceId` and the `requestId` should be passed in the next step. 
### Step 2: Initiate Duo Authentication for the User 🔗 
This step initiates the authentication on the third-party side by submitting a POST request to the `/admin/v1/MyAuthenticationFactorInitiator` endpoint. The client must include the following attributes: 
  * `requestId:` received in the Step 1 response
  * `deviceId:` received in the Step 1 response
  * `userName:` username of the user


### Request Example
The following example shows the contents of the POST request body in JSON format:
```
{
  "requestId": "1e513691-9a41-4418-a0f0-f96e6f4c5735",
  "deviceId": "14a2a6f2f41b4c10acc9a6d4b54ffe4a",
  "authFactor": "THIRDPARTY",
  "thirdPartyFactor": {
    "thirdPartyFactorId": "7ed55e203ac7435eb6b4847dcfca28e0",
    "thirdPartyFactorType": "None",
    "thirdPartyVendorName": "DUO_SECURITY"
  },
  "userName": "testuser1",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
  ]
}
```

### Response Example
The following example shows the contents of the response in JSON format:
```
{
  "requestId": "fe520538-0da6-45a3-b23f-1256091e3f0c",
  "deviceId": "ca0ba497327c45d2a4a408301c78682b",
  "authFactor": "THIRDPARTY",
  "thirdPartyFactor": {
    "thirdPartyFactorId": "1c3a069c240b4a9d9e6e90b9a2be8bed",
    "thirdPartyFactorType": "None",
    "thirdPartyVendorName": "DUO_SECURITY"
  },
  "userName": "testuser1",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorInitiator"
  ],
  "meta": {
    "resourceType": "MyAuthenticationFactorInitiator",
    "location": "https://<domainURL>admin/v1/MyAuthenticationFactorInitiator"
  },
  "additionalAttributes": [
    {
      "name": "duoHost",
      "value": "api-0095dc4a.duosecurity.com"
    },
    {
      "name": "duoChallenge",
      "value": "TX
        |Njg1MmU0ZTJiYzg2NGIzYjkxMmQ3YmQ0OGY5ZjQ4Nzl8RElFWldUV0VMVUJYSEQ2RExKM1V8MTU0MDMyMDkz==
        |8a0b6f0472b1c03357e9d6b3348d0a341c96e6a0:APP
        |Njg1MmU0ZTJiYzg2NGIzYjkxMmQ3YmQ0OGY5ZjQ 4Nzl8RElFWldUV0VMVUJYSEQ2RExKM1V8MTU0MDMyNDIzNA==
        |5d45c215e6e5af7d866df480087d825aa1cf4279"
    }
  ]
}
```

In the response `deviceId` and `requestId` should be passed in the next step. 
### Step 3: Validate Duo Factor for Enrollment Scenario 🔗 
This step calls the third-party factor API with collected credentials to validate the enrollment of a user in a POST request to the `/admin/v1/MyAuthenticationFactorValidator` endpoint. 
The client must include the following attributes:
  * `requestId:` received in the Step 2 response 
  * `deviceId:` received in the Step 2 response


**Request Example**
The following example shows the contents of the POST request in JSON format: 
```
{
  "requestId": "1e513691-9a41-4418-a0f0-f96e6f4c5735",
  "deviceId": "14a2a6f2f41b4c10acc9a6d4b54ffe4a",
  "authFactor": "THIRDPARTY",
  "thirdPartyFactor": {
    "thirdPartyFactorId": "7ed55e203ac7435eb6b4847dcfca28e0",
    "thirdPartyFactorType": "None",
    "thirdPartyVendorName": "DUO_SECURITY"
  },
  "scenario": "ENROLLMENT",
  "username": "testuser1",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorValidator"
  ],
  "additionalAttributes": [
    {
      "name": "duoResponse",
      "value": "AUTH|YWJoaXNoZWsuanVsa2FAb3JhY2xlLmNvbXxESUVaV1RXRUxVQlhIRDZETEozVXwxNTM5ODMwNDc2|9439adbea1b90a90c9169f366cc028aabde8ac51:APP|YWJoaXNoZWsuanVsa2FAb3JhY2xlLmNvbXxESUVaV1RXRUxVQlhIRDZETEozVXwxNTM5ODMzODYx|94bcc9a0c4ab6da617827432d021171d3b393fd3"
    }
  ]
}
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{
  "requestId": "fe520538-0da6-45a3-b23f-1256091e3f0c",
  "deviceId": "ca0ba497327c45d2a4a408301c78682b",
  "authFactor": "THIRDPARTY",
  "thirdPartyFactor": {
    "thirdPartyFactorId": "1c3a069c240b4a9d9e6e90b9a2be8bed",
    "thirdPartyFactorType": "None",
    "thirdPartyVendorName": "DUO_SECURITY"
  },
  "scenario": "ENROLLMENT",
  "userName": "testuser1",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:AuthenticationFactorValidator"
  ],
  "meta": {
    "resourceType": "MyAuthenticationFactorValidator",
    "location": "https://<domainURL>admin/v1/MyAuthenticationFactorValidator"
  },
  "status": "SUCCESS",
  "displayName": "test's Phone",
  "mfaStatus": "ENROLLED",
  "mfaPreferredDevice": "0d37a1334bdf4c9ca80474dcadba8d10",
  "mfaPreferredAuthenticationFactor": "THIRDPARTY",
  "mfaPreferredThirdPartyFactorType": "None",
  "securityQuestionsPresent": false,
  "devicesCount": 1,
  "emailFactorEnrolled": false
}
```

In the response, the attribute `mfaStatus:"ENROLLED"` indicates that user has enrolled for MFA. The `mfaPreferredAuthenticationFactor` attribute indicates the factor set as the preferred method. In this case, it's `THIRDPARTY`.
Was this article helpful?
YesNo

