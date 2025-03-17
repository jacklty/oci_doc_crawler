Updated 2024-04-02
# Using the On-Demand MFA API to Develop Custom Sign-In Page
This use case provides a step-by-step example of using the identity domains REST API to authenticate users and perform multifactor enrollment and authentication.
**Note** Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
**Note** This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
The On Demand MFA API is based on the concept of a state machine. Request responses inform an application client what has to be done next rather than requiring users to have third-party cookies enabled in their browsers. Third-party cookies enabled in browsers can pose problems, especially for B2C applications where controls on end-user behavior can't be enforced. The `requestState` provided in each request response is used in the next request, providing the client with the information that it needs to process the request, and then provide the next set of operations allowed.
The On Demand MFA API can:
  * Support user enrollment with MFA factors enabled by the administrator
  * Strengthen the security of password-based authentication using Multifactor Authentication (MFA) by requiring additional verification, such as using a time-based one-time passcode or an SMS passcode.
  * Perform MFA enrollment, MFA verification and User Authentication Factor management. 


The following example sets are included in this use case:
[Factor Enrollment With Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#enrollment "These use cases provide example requests using the identity domains REST API that allows a user to enroll for MFA factors.")
## Factor Enrollment With Verification 🔗 
These use cases provide example requests using the identity domains REST API that allows a user to enroll for MFA factors.
The following use cases walk you through the steps to enroll different MFA factors using the REST API:
  * [Fetch Enrolled Factors of a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb "This use case provides a step-by-step example of using the identity domains Verification API to fetch the factors that a user is enrolled in.")
  * [Initiate and Verify the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#unique_2082766434 "This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication \(MFA\) with Factor Verification.")
  * [Initiate and Verify a Backup Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#unique_2016818917 "This use case provides a step-by-step example of using the identity domains Verification API to complete factor verification of the backup factor.")
  * [Authentication Factor Enrollment With Factor Verification-SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_rt5_rxf_ngb "This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication \(MFA\) with Factor Verification.")
  * [Authentication Factor Enrollment With Factor Verification-Email](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_gqj_v5g_ngb "This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication \(MFA\) with Factor Verification.")


### Fetch Enrolled Factors of a User 🔗 
This use case provides a step-by-step example of using the identity domains Verification API to fetch the factors that a user is enrolled in. 
These steps assume that relevant factors of MFA are enabled using [Configure Multi-Factor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-enrollment-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
The step to follow in this use case depends on whether you want to request by using the `userGUID` or the `User Name`: 
  * [Step 1: Get Enrolled Factors for a User by userGUID](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__section_exs_rkg_ngb)
  * [Step 2: Get Enrolled Factors for a User by Using Filters](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__section_t33_1ch_ngb)


**Note** The examples in this section use `userGUID` in the requests. You may request both `userGUID` and `userOcid` in your requests.
#### Step 1: Get Enrolled Factors for a User by userGUID  🔗 
This step gets the enrolled factors for a user based on the `userGUID` or User name.
**Request Example**
```
GET {{HOST}}/mfa/v1/users/{{userGUID}}/factors
```

**Response Example**
The following example shows the contents of the response in JSON format:
```

{
  "userGUID": "7b3d902ab05b4214bae6b2924ca6be21",
  "status": "success",
  "preferredFactorId": "b3e04149d958437b9b801fa70c33ca70",
  "preferredMethod": "EMAIL",
  "factors": [
    {
      "factorId": "SecurityQuestions",
      "methods": [
        "SECURITY_QUESTIONS"
      ]
    },
    {
      "displayName": "+155XXXXX555",
      "factorId": "83889faeacaf4592a964405f87506fc6",
      "methods": [
        "SMS"
      ]
    },
    {
      "displayName": "uxxr1@example.com",
      "factorId": "b3e04149d958437b9b801fa70c33ca70",
      "methods": [
        "EMAIL"
      ]
    },
    {
      "factorId": "BypassCode",
      "methods": [
        "BYPASSCODE"
      ]
    }
  ]
}
```

The response contains the `userGUID`, the preferred factor, and the enrolled factor details. 
#### Step 2: Get Enrolled Factors for a User by Using Filters 🔗 
You can get enrolled factors for a user by using either User Name or User GUID. The following `userIdType` values are accepted: 
  * USER_GUID- For example, here `userId` should contain USER_GUID such as "7b3d902ab05b4214"
  * USER_NAME- For example, here `userId` should contain USER_NAME such as John. 


**Request Example to fetch the enrolled factors based on User Name**
The following example shows the request example to get the enrolled factors for a user based on their User Name in JSON format:```

GET {{HOST}}/mfa/v1/users?userId=user1@example.com&userIdType=USER_NAME&attributes=factors

```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{
  "userGUID": "589879c55b7340518141eab82493f0cc",
  "status": "success",
  "preferredFactorId": "88178d80636a428393a5674ba46dc867",
  "preferredMethod": "SMS",
  "factors": [
    {
      "factorId": "BypassCode",
      "methods": [
        "BYPASSCODE"
      ]
    },
    {
      "displayName": "user1@example.com",
      "factorId": "30db2274140043918edb033d9fe29ff3",
      "methods": [
        "EMAIL"
      ]
    },
    {
      "displayName": "+1554455555",
      "factorId": "88178d80636a428393a5674ba46dc867",
      "methods": [
        "SMS"
      ]
    }
  ]
}
```

The response contains the `userGUID`, the preferred factor, and the enrolled factor details. 
**Request Example to fetch the enrolled factors based on User GUID**
The following example shows the request example to get the enrolled factors for a user based on their User GUID in JSON format:```

GET {{HOST}}/mfa/v1/users?userId=589879c55b7340518141eab82493f0cc&userIdType=USER_GUID&attributes=factors
```

**Response Example**
The following example shows the contents of response in JSON format:
```
{
  "userGUID": "589879c55b7340518141eab82493f0cc",
  "status": "success",
  "preferredFactorId": "88178d80636a428393a5674ba46dc867",
  "preferredMethod": "SMS",
  "factors": [
    {
      "factorId": "BypassCode",
      "methods": [
        "BYPASSCODE"
      ]
    },
    {
      "displayName": "user1@example.com",
      "factorId": "30db2274140043918edb033d9fe29ff3",
      "methods": [
        "EMAIL"
      ]
    },
    {
      "displayName": "+1554455555",
      "factorId": "88178d80636a428393a5674ba46dc867",
      "methods": [
        "SMS"
      ]
    }
  ]
}
```

The response contains the `userGUID`, the preferred factor, and the enrolled factor details.
### Initiate and Verify the Preferred Factor 🔗 
This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication (MFA) with Factor Verification.
These steps assume that relevant factors of MFA are enabled using [Configure Multi-Factor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-verification-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Download the collection and the global variables file from the **idcs-factor-verification-api** folder within GitHub and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [usingondemandapis.htm#concept_l3p_vyg_ngb__mfa_initiate_verification](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__mfa_initiate_verification)
  * [usingondemandapis.htm#concept_l3p_vyg_ngb__mfa_verify_factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__mfa_verify_factor)


**Note** The examples in this section use `userGUID` in the requests. You may request both `userGUID` and `userOcid` in your requests.
#### Step1: Initiate Verification of the Preferred Factor  🔗 
This step initiates the verification of a user's preferred factor. If you need to use the verify factor API without providing the `userGUID`, you can provide a user unique id such as username as the `userId`. The `userIdType` in the request indicates what type of credential the user is passing as the value for the `userId`. The following `userIdType` values are accepted: 
  * USER_GUID - For example, here `userId` should contain USER_GUID such as "7b3d902ab05b4214" 
  * USER_NAME - For example, here `userId` should contain USER_NAME such as John.


The `userId` attribute contains the actual value of the user credential that's passed. 
**Request Example**
The following example shows the POST request to **`{{HOST}}/mfa/v1/requests`**endpoint in JSON format.
```
{
  "userId":"{{userGUID}}",
  "userIdType": "USER_GUID"
}
```

**Response Example**
The following example shows the contents of the POST response to **`{{HOST}}/mfa/v1/requests`**endpoint in JSON format after initiating preferred factor on the preferred ID :
```

{   
"status": "success",
"requestId": "f843736e-cbd8-4548-b41f-343b624a79fc",
"userGUID": "589879c55b7340518141eab82493f0cc", 
"factorId": "88178d80636a428393a5674ba46dc867",  
"method": "SMS",  
"displayName": "+4455665455",  
"requestState": "GwHJr3RvycjNEv.....MhQTLmWYzA/LVp0s"
}
```

In the response, the `requestId` value is the unique identifier generated for this request. Include the `requestId` in every subsequent call to complete factor verification. The `factorId` is the preferred device on which it was initiated. The `method` is the factor that the user has initiated. The `requestState` contains the contextual data needed to process the request.
In this example, an `otpCode`(in case of SMS and EMAIL factor) is sent using SMS to the user's mobile device. 
#### Step 2: Verify the Preferred Factor  🔗 
This step verifies the factor by passing the `otpCode` in a PATCH request to `**{{HOST}}/mfa/v1/requests/{{requestId}}**`.
The client must include the following attributes:
  * `otpCode:` the code received by the user on their device 
  * `requestState`: received in the Step 1 response 
  * `requestId`: received in the Step 1 response 


**Request Example**
The following example shows the contents of the PATCH request in JSON format: 
```
{ 
"otpCode":"170230", 
"requestState": "{{requestState}}" 
}
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{"status":"success"} 
```

Success indicates that verification was successful.
### Initiate and Verify a Backup Factor 🔗 
This use case provides a step-by-step example of using the identity domains Verification API to complete factor verification of the backup factor.
These steps assume that relevant factors of MFA are enabled using [Configure Multi-Factor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-verification-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Initiate and Verify the Backup Factor Security Questions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__section_z2g_3dh_ngb)
  * [Step 2: Initiate and Verify Backup Factor EMAIL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb__section_nng_h2h_ngb)


**Note** The examples in this section use `userGUID` in the requests. You may request both `userGUID` and `userOcid` in your requests.
#### Step 1: Initiate and Verify the Backup Factor Security Questions 🔗 
This step initiates the verification of a user's backup factor. The client must provide both the `factorId` and the `method` in the request. If you need to use the verify factor API without providing the `userGUID`, you can provide a user unique id such as username as the `userId`. The `userIdType` in the request indicates what type of credential the user is passing as the value for the `userId`. The following `userIdType` values are accepted: 
  * USER_GUID - For example, here `userId` should contain USER_GUID such as `"7b3d902ab05b4214"`. 
  * USER_NAME - For example, here `userId` should contain USER_NAME such as `Joe John`. 


The `userId` attribute contains the actual value of the user credential that's passed. 
To obtain a list of enrolled factors and their IDs for a user, see the [Fetch Enrolled Factors of a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_l3p_vyg_ngb "This use case provides a step-by-step example of using the identity domains Verification API to fetch the factors that a user is enrolled in.") Use Case. In this example, the backup factor chosen is Security Questions. 
**Request Example to Initiate Backup Factor Security Questions**
The following example shows the contents of the POST request to `**{{HOST}}/mfa/v1/requests/**`endpoint in JSON format:
**Note** The preferred `factorId` contains the unique ID of the preferred factor. In case of SECURITY_QUESTIONS, it will have the fixed string "SecurityQuestions".
```
{
  "userId":"{{userID}}",
  "userIdType":"USER_GUID",
  "factorId":"{{factorID}}",
  "method":"SECURITY_QUESTIONS"
}
```

In the response, the `requestId` value is the unique identifier generated for this request. Include the `requestId` in every subsequent call to complete factor verification. The `requestState` contains contextual data needed to process the request.
**Response Example**
The following example shows the contents of the response in JSON format for backup method SEQURITY_QUESTIONS: 
```
{
  "status": "success",
  "requestId": "8da79411-5388-41ee-990e-935e74cb40f3",
  "userGUID": "589879c55b7340518141eab82493f0cc",
  "factorId": "SecurityQuestions",
  "method": "SECURITY_QUESTIONS",
  "requestState": "hBJIvkyfsXBv....movYarft8HlYANV3c+0",
  "securityQuestions": [
    {
      "id": "MaidenName",
      "localizedText": "What's your mother's maiden name?"
    }
  ]
}

```

In the response, the `requestId` value is the unique identifier generated for this request. Include the `requestId` in every subsequent call to complete factor verification. The `requestState` contains contextual data needed to process the request. In this example, a question is sent back from the list of enrolled questions to which the user needs to answer.
**Request Example to Verify Backup Factor Security Questions**
This step verifies the backup factor by passing the answer to the Security Question in a PATCH request to `**{{HOST}}/mfa/v1/requests/{{requestID}}**`. The client must include the following attributes:
  * `requestState:` received in the Step 1 response
  * `securityQuestions id/answers`: defined by the user during enrollment


**Request Example**
The following example shows the contents of the PATCH request in JSON format for SECURITY_QUESTIONS: ```
{
 "securityQuestions":[
    {
      "id":"MaidenName",
      "answer":"Smith"
    }
  ],
"requestState": "{{requestState}}"
 }
 
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{"status":"success"} 
```

Success indicates that verification was successful.
#### Step 2: Initiate and Verify Backup Factor EMAIL  🔗 
This step initiates the verification of a backup factor EMAIL. 
**Request Example to Initiate EMAIL factor**
The following example shows the request example in JSON format for preferred method "EMAIL":
```
{
  "userId":"{{userID}}",
  "userIdType":"USER_GUID",
  "factorId":"{{factorID}}",
  "method":"EMAIL"
}
```

**Response Example**
The following example shows the response example to initiate EMAIL factor in JSON format:
```
{ 
 "status":"success",
 "requestId":"<Request ID>",
 "userGUID":"<User GUID>",
 "factorId":"factorID",
 "method":"EMAIL",
 "displayName":"Joe John",
 "requestState":"QYV81R9eoagwWQ"
 }
```

**Request Example to Verify EMAIL Factor**
The following example shows the PATCH request in JSON format for EMAIL factor:
```
{
  "otpCode":"170230"
   "requestState": "QYV81R9eoagwWQ"
 }
```

**Response Example**
The following example shows the contents of the response in JSON format to verify EMAIL Factor: 
```
{"status":"success"}
```

Success indicates that verification was successful. 
### Return OTP Factors without Notifying the User 🔗 
This use case provides an example of initiating the On Demand MFA API to return one-time passcode (OTP) factors (SMS or Email or Phone Call) in a response without notifying the user.
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-verification-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
These steps assume that relevant factors of MFA are enabled using [Configure Multifactor Authentication Settings](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/configure-multi-factor-authentication-settings.html) .
**Request Payload**
Attribute | Supported Values / Sample Values | Multi-Valued | Usage Details  
---|---|---|---  
`userFlowControlledByExternalClient` | true / false | false |  Set this option to ```
true
```
and the OTP will be returned in the response in the encrypted format specified.  **Note** : The certificate used for encryption is uploaded to the application in advance and is referred using the `x5t` attribute in the request example as mentioned below.  
x5t | String / X509 SHA-1 Certificate Thumbprint |  When specified, the service uses this uploaded certificate to encrypt the OTP data. **Note** : The "x5t" attribute should match the uploaded certificate.  
**Request Example**```
{
  "userId":"<Unique Id>",
  "userIdType":"USER_NAME/USER_GUID",
  "userFlowControlledByExternalClient": true,
  "x5t" :"<certificate thumbprint>"
}
```

**Response Payload**
Attribute | Supported Values / Sample Values | Multi-Valued | Usage Details  
---|---|---|---  
`otp` |  Map ```
"otp": {
  "value": "IMCw==",
  "alg": "RSAES-OAEP",
   "x5t": "<certificate thumbprint>"
 }

```
| false |  When present in the response, the attribute contains the encrypted OTP with following details. 
  * **value** : Encrypted value.
  * **alg** : Algorithm used for encryption.
  * **x5t** : SHA-1 X509 Thumbprint of the certificate used for encryption.

  
**Response Example**
```
{
  "status": "success",
  "requestId": "<Request ID>",
  "userGUID": "<User GUID>",
  "factorId": "<SMS/EMAIL/PHONE_CALL factor GUID>",
  "method": "SMS/EMAIL/PHONE_CALL",
  "displayName": "+91XXXXXXXX984",
  "requestState": "4p7ViEzP2bP1MIM",
  "otp": {
    "value": "<Encrypted OTP value>",
    "alg": "<Encryption algorithm>",
    "x5t": "<x5t of the certificate used to encrypt the OTP>"
      }
}
```

### Authentication Factor Enrollment With Factor Verification-SMS 🔗 
This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication (MFA) with Factor Verification.
These steps assume that relevant factors of MFA are enabled using [Configure Multi-Factor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-enrollment-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Initiate SMS Factor Enrollment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_rt5_rxf_ngb__section_exs_rkg_ngb)
  * [Step 1a: Resend the OTP](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_rt5_rxf_ngb__section_xnc_3y5_ngb)
  * [Step 2: Activating the SMS Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_rt5_rxf_ngb__section_l5n_spg_ngb)


**Note** The examples in this section use `userGUID` in the requests. You may request both `userGUID` and `userOcid` in your requests.
#### Step 1: Initiate SMS Factor Enrollment  🔗 
This step initiates SMS enrollment. The client must include the following attributes: 
  * `method`: defines to enroll in SMS factor
  * `phoneNumber`: defines the phone number where the SMS text will be sent 
  * `countryCode`: defines the country code of the phone number where the SMS text will be sent


**Request Example**
The following example shows the POST request to the `**{{HOST}}/mfa/v1/users/{{userGUID}}/factors**`endpoint in JSON format:
```
{ 
"method": "SMS",
"countryCode": "+44", 
"mobileNumber": "1122334455", 
}
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{
"status": "success", 
"factorId": "88178d80636a428393a5674ba46dc867",
"factorStatus": "ENROLLMENT_INITIATED", 
"methods": [ "SMS" ],
"displayName": "+1122334455", 
"requestState": "QK1.....y+OFP//0" 
}
```

`displayName` is the mobile number. An `otpCode` will be sent to the users mobile device, which is used to complete the enrollment. 
#### Step 1a: Resend the OTP  🔗 
If the user doesn't receive the OTP, this example shows how to request that an OTP be resent. The client must include the following attributes: 
`requestState:` received in the Step 1 response
`resendOtp:` Boolean to indicate that the OTP is received
**Request Example**
The following example shows the PATCH request to the `**{{HOST}}/mfa/v1/users/{{userGUID}}/factors/{{factorID}}**`endpoint in JSON format:
```
{
 "resendOtp":true,
 "requestState": "QK1.....y+OFP//0"
}
```

**Response Example**
The following example shows the contents of the response in JSON format:
```
{ 
"status": "success",
"factorId": "88178d80636a428393a5674ba46dc867", 
"factorStatus": "ENROLLMENT_INITIATED",
"methods": [ "SMS" ],
"displayName": "+445544455",
"requestState": "+HFVV...qgMUI" 
} 

```

The response contains the following parameters: 
  * `requestState:` that should be passed by the client in the next step
  * `displayName:` is the mobile number being enrolled 
  * `method:` SMS factor method 
  * `factorId:` unique identifier generated for the factor being enrolled


Success indicates that:
  * The `userGUID` that was provided is valid
  * The user is active
  * The user account isn't locked
  * The SMS factor is enabled 


#### Step 2: Activating the SMS Factor 🔗 
This step activates the SMS enrollment for the user, in a PATCH request to the `**/mfa/v1/users/{{userGUID}}/factors/{{factorID}}**`endpoint.
The client must include the following attributes:
  * `otpCode:` the code received by the user on their device 
  * `requestState`: received in the Step 1 response 


**Request Example**
The following example shows the contents of the PATCH request in JSON format: 
```
{ 
"otpCode":"170230", 
"requestState": "{{requestState}}"
 }
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{"status":"success"} 
```

Success indicates that: 
  * `OTP` is valid
  * The `userGUID` that was provided is valid
  * The user is active
  * The user account isn't locked
  * The SMS factor is enabled and factor is enrolled successfully


**Error Response Examples**
The following example shows the error message in JSON format when the `userGUID` is invalid. You get a 404 HTTP response code if the `userGUID` is invalid.```
{
  "status": "failed",
  "ecId": "0d1QwglU0000Fy",
  "cause": [
    {
      "code": "AUTH-3018",
      "message": "User not found."
    }
  ]
}
```

The following example shows the error message in JSON format when the user is locked. You get a 401 HTTP response code.
```
{
  "status": "failed",
  "ecId": "0ISDCif1Qy6wg0000A8",
  "cause": [
    {
      "code": "AUTH-1010",
      "message": "Your account is locked.Contact your system administrator."
    }
  ]
}
```

### Authentication Factor Enrollment With Factor Verification-Email  🔗 
This use case provides a step-by-step example of using the identity domains Factor Enrollment API to enroll for Multifactor Authentication (MFA) with Factor Verification.
These steps assume that relevant factors of MFA are enabled using [Configure Multi-Factor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
Download the identity domains authentication use case examples collection and the global variables file from the **idcs-factor-enrollment-api** folder within the [idm-samples](https://github.com/oracle-samples/idm-samples) GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
  * [Step 1: Initiate Email Factor Enrollment ](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_gqj_v5g_ngb__section_exs_rkg_ngb)
  * [Step 1a: Resend the OTP](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_gqj_v5g_ngb__section_ln1_mhv_ngb)
  * [Step 2: Activate the EMAIL Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_gqj_v5g_ngb__section_gc4_4xg_ngb)


**Note** The examples in this section use `userGUID` in the requests. You may request both `userGUID` and `userOcid` in your requests.
#### Step 1: Initiate Email Factor Enrollment  🔗 
This step initiates Email enrollment. The client must include the following attribute: 
  * `method`: defines to enroll in Email. User will not pass the email id. The primary email id is automatically fetched from the user's profile.


**Request Example**
The following example shows the contents of the POST request to `**{{HOST}}/mfa/v1/users/{{userGUID}}/factors**`endpoint in JSON format:
```
{ 
"method": "EMAIL",
}
```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{
  "status": "success",
  "factorId": "30db2274140043918edb033d9fe29ff3",
  "factorStatus": "ENROLLMENT_INITIATED",
  "methods": [
    "EMAIL"
  ],
  "displayName": "user1@example.com",
  "requestState": "Vxar...bWTTA"
}
```

An `otpCode` will be sent to the user's email id, which is used to complete the enrollment. 
The response contains:
  * `requestState:` that should be passed by the client in the next step
  * `displayName:` email id of the user enrolled 
  * `method:` EMAIL factor method


Success indicates that: 
The factor enrollment was initiated.
#### Step 1a: Resend the OTP  🔗 
The following example shows the PATCH request to `**{{HOST}}/mfa/v1/users/{{userGUID}}/factors/{{factorID}}**`endpoint in JSON format.
If the user doesn't receive the OTP, this example shows how to request that an OTP be resent. The client must include the following attributes: 
  * `requestState:` received in the Step 1 response
  * `resendOtp:` to indicate that the OTP is received


**Request Example**
The following example shows the contents of the PATCH request in JSON format: 
```
{ 
"resendOtp":true, 
 "requestState": "QK1.....y+OFP//0"
 }
 
```

The following example shows the contents of the response in JSON format: 
```
{  
"status": "success",   
"factorId": "30db2274140043918edb033d9fe29ff3",
"factorStatus": "ENROLLMENT_INITIATED",  
"methods": ["EMAIL"],
"displayName": "username@example.com", 
"requestState": "AmgsMN.....2sk4SI" 
}
  
```

The response contains: 
  * `requestState`: that should be passed by the client in the next step
  * `displayName`: email id fetched from the user's profile 
  * `method`: the list of method(s) being enrolled in EMAIL method
  * `factorId`: unique identifier generated for the factor being enrolled


Success indicates that: 
  * The `userGUID` or `userOcid` that was provided is valid
  * The user is active
  * The user account isn't locked
  * The EMAIL factor is enabled


#### Step 2: Activate the EMAIL Factor 🔗 
This step activates the EMAIL enrollment for the user, in a **PATCH** request to the `**/mfa/v1/users/{{userGUID}}/factors/{{factorID}}**`endpoint.
The client must include the following attributes:
  * `otpCode:` the code received by the user on their email id 
  * `requestState`: received in the Step 1 response 


**Request Example**
The following example shows the contents of the PATCH request in JSON format: 
```
{
"otpCode":"710130", 
"requestState": "{{requestState}}"
} 

```

**Response Example**
The following example shows the contents of the response in JSON format: 
```
{"status":"success"} 
```

Success indicates that: 
  * `OTP` is valid
  * The `userGUID` or `userOcid` that was provided is valid
  * The user is active
  * The user account isn't locked
  * The EMAIL factor is enabled and factor is enrolled successfully


**Error Response Examples**
The following example shows the error message in JSON format when the `userGUID` is invalid. You get a 404 HTTP response code if the `userGUID` or `userOcid` is invalid.```
{
  "status": "failed",
  "ecId": "0d1QwglU0000Fy",
  "cause": [
    {
      "code": "AUTH-3018",
      "message": "User not found."
    }
  ]
}
```

The following example shows the error message in JSON format when the EMAIL is disabled. You get a 401 HTTP response code.
```
{
  "status": "failed",
  "ecId": "0000M00000A",
  "cause": [
    {
      "code": "AUTH-1125",
      "message": "The EMAIL factor has been disabled."
    }
  ]
}
```

Was this article helpful?
YesNo

