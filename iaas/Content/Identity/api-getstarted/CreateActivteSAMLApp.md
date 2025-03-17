Updated 2024-04-02
# Creating and Activating a SAML App
This section provides example requests to create and activate a Security Assertion Markup Language (SAML) App using the REST APIs.
## Create a SAML App
A SAML App is an application that supports SAML for single sign-on. The example shows how to craft a request to create a SAML App.
**Note** If you're using the optional `name` attribute in your request, be sure to use only alphanumeric characters and the underscore ( _ ) character in the value.
```
cat>/tmp/SAMLApp.json << __EOF__
{
 "schemas": ["urn:ietf:params:scim:schemas:oracle:idcs:App"],
 "active": true,
 "displayName": "testSAMLApp",
 "description": "SAML for Portal",
 "basedOnTemplate": {
  "value": "CustomSAMLAppTemplateId"
 },
 "name": "testSAMLPartner",
 "urn:ietf:params:scim:schemas:oracle:idcs:extension:samlServiceProvider:App":
     {
      "signResponseOrAssertion": "Assertion",
      "includeSigningCertificateInSignature": "true",
      "entityId": "IdcsSamlDomain",
      "nameIdFormat": "saml-emailaddress",
      "nameIdUserstoreAttribute": "emails.primary.value",
      "assertionConsumerUrl": "http://<domainURL>/saml2/sp/acs/post",
      "signatureHashingAlgorithm": {
       "value": "SHA-256"
      },
      "logoutEnabled": true,
      "logoutBinding": true,
      "logoutRequestURL": "http://<domainURL>/FederationSampleApp/logout",
      "singleLogoutURL": "http://<domainURL>/FederationSampleApp/logout",
      "logoutResponseUrl": "http://<domainURL>/FederationSampleApp",
      "groupAssertionAttributes": [
       {
        "name": "all",
        "condition": "All Groups"
       }
      ],
      "userAssertionAttributes": [
       {
        "name": "email",
        "userStoreAttributeName": "emails.primary.value"
       },
       {
        "name": "userid",
        "userStoreAttributeName": "userName"
       },
       {
        "name": "firstname",
        "userStoreAttributeName": "name.givenName"
       },
       {
        "name": "lastname",
        "userStoreAttributeName": "name.familyName"
       }
      ]
     }
} 
__EOF__
  curl -X POST 
  -H "Content-type: application/json" 
  -H "Authorization: Bearer <access token value>" 
  --data @/tmp/SAMLApp.json http://<domainURL>/admin/v1/Apps
```

**Required App Attributes for a SAML App**
Required App Attribute | Description  
---|---  
`entityId` | An entity ID is a globally unique name for a SAML entity, either an identity provider or a service provider. Usually, the value is a URL.  
`assertionConsumerUrl` | The assertion consumer URL is the endpoint at the service provider to which the SAML Assertions will be sent by the SAML identity provider.   
`nameIdFormat` | This attribute represents the Name ID format that will be used in the SAML assertion, such as Email Address, Windows Domain Qualified Name, or X.509 Subject Name. The service provider and identity provider use the Name ID format to easily identify a subject during their communication.   
`nameIdValue` | What you define for this attribute depends on the nameIdFormat type specified. This attribute is used to identify the user that's logged in.   
`logoutBinding` | This attribute identifies whether the log out request is sent as a Redirect or a Post. This is a required attribute if the attribute `logoutEnabled` is set to `True.`  
`logoutRequestURL` | Required if the attribute `logoutEnabled` is set to `True.` Enter the location where the log out request is sent (using HTTP or HTTPS).  
`logoutResponseURL` | Required if the attribute `logoutEnabled` is set to `True.` Enter the location where the log out response is sent (using HTTP or HTTPS).   
## Constructing the nameIdUserstoreAttribute Property
The `nameIdUserstoreAttribute` property specifies which user attribute is used as the NameID value in the SAML assertion.
**Supported Values**
  * `userName`
  * `emails.primary.value`


## Constructing the userStoreAttributeName Property
The `userStoreAttributeName` property is a subattribute of the `userAssertionAtributes` complex attribute. The `userStoreAttributeName` property specifies which user attribute should be used to create the value of the SAML assertion attribute.
**Supported Values**
  * `userName`
  * `name.givenName`
  * `name.middleName`
  * `name.familyName`
  * `emails.primary.value`
  * `emails[work].value`
  * `phoneNumbers[home].value`
  * `phoneNumbers[mobile].value`
  * `phoneNumbers[work].value`
  * `title`
  * `addresses[work].streetAddress`
  * `addresses[work].locality`
  * `addresses[work].postalCode`
  * `addresses[work].region`
  * `addresses[work].country`


## Activate a SAML App
Use this example to create a request to activate a SAML application.
```
echo "Activate SAML App"
cat>/tmp/SAMLApp.json << __EOF__
{
    "active" : true,
    "schemas": [
       "urn:ietf:params:scim:schemas:oracle:idcs:AppStatusChanger"
    ]
}
__EOF__
  curl -X PUT 
  -H "Content-type: application/json" 
  -H "Authorization: Bearer <access token value>" 
  --data @/tmp/SAMLApp.json http://domainURL/admin/v1/AppStatusChanger/<appID>
```

Was this article helpful?
YesNo

