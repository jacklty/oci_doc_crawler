Updated 2025-01-21
# Configuring the State Relay Validation with an IdP-Initiated SSO
OCI identity domains validates the relay state URL based on the configuration settings. 
The state relay validates using the configured URL when the following conditions are met:
  * OCI identity domains acts as a Service Provider (SP).
  * Identity Providers (IdP), for example Azure and Pinfederate, act as external identity providers.


## Before You Begin
Perform the following actions before you configure the state relay validation.
  1. Submit a service request (SR) to enable Relay State Validation on your identity domains. Provide the following details in the SR:
     * The Identity Domain's GUID. For example, `idcs-xxxx`.
     * Provide your reason and use case for the request.
     * Tenancy region.
     * The component must be "`SAML`".
  2. Create an access token with an `Identity Domain Administrator` role to perform the following API commands. For more information on how to create an Access token, see [Generating an Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-personal-access-tokens.htm#generate-personal-access-tokens "An access token is an authorization that's used by a client application to access an API or a resource application within a limited period.").
    1. Create a confidential application in the identity domain. For more information, see [Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server.").
       * Configure the application as a client.
       * On the page to configure OAuth, select **Add app roles** , and then select the application roles you want to apply to this application. Assign **Identity Domain Administrator** to the list of app roles.
       * Use the client GUID and client secret to generate the Access token using a token endpoint.


## 1: Getting an Identity Provider ID 🔗 
Use a CURL command to view the `id` of the Identity Domains.
```
curl -XGET -H 'Authorization: Bearer <accessToken>' 
-H 'Content-Type: application/json' 
'https://<idcs stripe>.identity.oraclecloud.com/admin/v1/IdentityProviders'
```

Sample response:
```
{
 "type": "SAML",
 "id": "fdxsxxxxxxxxxxxxxxxxxxxxxxxxxxdb",
 "meta":{
  "created": "2024-08-23T21:21:29.703Z",
  "lastModified": "2025-01-07T17:16:51.186Z",
  "version": "bxxxxxxxxxxxxxxxxxxxxxxxxx",
  "resourceType": "IdentityProvider",
  "location": "https://idcs-aa2f86468523aa4668a.....identity.oci.oracleiaas.com:443/admin/v1/IdentityProviders/fd84848484848xxxxxxxxdb"
 },
 "jitUserProvCreateUserEnabled": false,
 "jitUserProvGroupAssignmentMethod": "Overwrite",
 "enabled": true,
 "idcsLastModifiedBy":{
  "value": "f256256256256xxxxxxxx3acb",
  "display": "opcInfra",
  "ocid": "ocid1.domainapp.region1.sea.amaaaaapppxxxxxxxxxxxxxxxxx",
  "type": "App",
  "$ref": "https://idcs-aa20505xxxxxxxxxxxxxxxxx......identity.oci.oracleiaas.com:443/admin/v1/Apps/f25xxxxxxxxxxxxxxxxxxxxxb"
 },
"partnerName": "azure-test",
.....
}
```

Find the `id` of the identity providers you want to update. Note the `id` and `partnerName` listed in the response.
## 2: PATCH the Allowed-IdP-Initiated-Relay-States attribute 🔗 
Use a CURL command to patch the `allowedIdPInitiatedRelayStates` of selected Identity Providers.
```
curl -XPATCH -H 'Authorization: Bearer <accessToken>' -H 'Content-Type: application/json' 
-d '{"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],"Operations": 
[{"op": "replace","path": "allowedIdpInitiatedRelayStates","value": [<List of Allowed Relay States>]}]}' 
'https://<idcs stripe>.identity.oraclecloud.com/admin/v1/IdentityProviders/<Identity Provider ID>'
```

In the response, look for the following replies:
  * `"partnerName"`: Confirm that the partner name is accurate.
  * ```
"allowedIdpInitiatedRelayStates:[
  "https://example.com/success",
  "https://example/fail"
],
```



Was this article helpful?
YesNo

