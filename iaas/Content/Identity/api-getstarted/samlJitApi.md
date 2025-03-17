Updated 2024-04-02
# Configuring SAML JIT Provisioning
SAML Just-In-Time (JIT) Provisioning automates user account creation when the user first tries to perform SSO and the user doesn't yet exist in the identity domain. In addition to automatic user creation, SAML JIT Provisioning allows granting and revoking group memberships as part of provisioning. SAML JIT Provisioning can be configured to update provisioned users so the users' attributes in the Service Provider (SP) store can be kept in sync with the Identity Provider (IdP) user store attributes.
When configuring SAML JIT Provisioning, you define how the user data sent by your SAML IdP will be used to create and/or update users in your identity domain. First, you create and configure a SAML IdP for federated SSO, and then you enable and configure the SAML JIT Provisioning options for that IdP.
SAML JIT Provisioning can be configured only using the `/admin/v1/IdentityProviders` REST API endpoint.
The following table describes the IdP configuration attributes relevant to SAML JIT Provisioning. For information on using OAuth 2 to Access the REST API, see [Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm "The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to programmatically manage users, groups, applications, and identity functions, such as password management and administrative tasks. To make REST API calls to your identity domain, you need an OAuth2 access token to use for authorization. The access token provides a session \(with scope and expiration\), that your client application can use to perform tasks in an identity domain.").
`IdentityProvider` Property | Description | JSON Example  
---|---|---  
`jitUserProvEnabled` | Boolean property to enable/disable the SAML JIT Provisioning feature for this IdP.If this property is `true` at least one of `jitUserProvCreateUserEnabled` or `jitUserProvAttributeUpdateEnabled` also must be `true`. |  ```
"jitUserProvEnabled": true,
```
  
`jitUserProvCreateUserEnabled` |  Boolean property indicating whether a user should be created, based on the incoming assertion, if the user doesn't yet exist. By default, users created using SAML JIT Provisioning are "federated" users. Federated users don't have credentials to sign in directly to the identity domain, but instead must be authenticated by the external identity provider. A user's federated status can be changed using the Admin console, and by updating the `isFederatedUser` attribute using the REST API. For example, you might want to change federated status for users with administrator privileges, so that they can sign in directly to the Console. If you prefer all users created using SAML JIT Provisioning to be created as nonfederated users (created with an identity domain sign-in password), set `isFederatedUser=false` in the JIT attribute mappings configuration. See `attributeMappings` in the table below. |  ```
"jitUserProvCreateUserEnabled": true,
```
  
`jitUserProvAttributeUpdateEnabled` |  Boolean property indicating whether the user's attributes should be updated, based on the incoming assertion, if the user already exists. |  ```
"jitUserProvAttributeUpdateEnabled": true,
```
  
`jitUserProvAttributes` |  This is a reference to a `MappedAttributes` object, which defines the mapping of the IdP SAML assertion attribute values to the identity domain user attributes, for both dynamic user creation and user attribute updates. (Set at creation of the `IdentityProvider`, don't update this reference.) See below for details of the `jitUserProvAttributes` usage of the `MappedAttributes` resource.  
`jitUserProvGroupAssertionAttributeEnabled` |  Boolean property indicating whether group memberships should be assigned to the user based on a list of group names received from the IdP in a SAML attribute. If this property is `true`, then the property `jitUserProvGroupSAMLAttributeName` must be set. |  ```
"jitUserProvGroupAssertionAttributeEnabled": true,
```
  
`jitUserProvGroupMappingMode` |  String property that controls how the groups in IdP are mapped to those in the identity domain. The value must be one of: **explicit** - IdP groups are explicitly mapped to the groups in the identity domain using the configuration property `jitUserProvGroupMappings`. **implicit** - Group names in the SAML assertion must match group names in the identity domain. Defaults to **explicit** if no value is specified. |  ```
"jitUserProvGroupMappingMode": "explicit",
```
  
`jitUserProvGroupMappings` |  Array of mappings between groups in the IdP assertion and groups in the identity domain. Every object in the array represents a mapping between an IdP group and an identity domains group. `idpGroup` is the group identifier in the IdP assertion, and **value** is the group identifier in the identity domain. The maximum number of group mappings per IdP is 250. |  ```

		"jitUserProvGroupMappings": [
  {
   "idpGroup": "7e18e37e-1b2f-46d9-9d9c-6df136570b27",
   "value": "4bce9b677ab447f18b65ba7bf9a61c21"
  },
  {
   "idpGroup": "cf6f7594-d454-40ac-971b-07cf0627ca17",
   "value": "6d8448a643b94b268d986e9d31e20cbc"
  }
 ]
```
  
`jitUserProvGroupSAMLAttributeName` |  The name of the SAML assertion attribute that will contain groups to be assigned to the user, if the property `jitUserProvGroupAssertionAttributeEnabled` is `true`. The assertion attribute can comprise either:
  * a single Attribute Value element, containing a comma-separated list of group names; or
  * multiple AttributeValue elements, each with a single group name.

|  ```
"jitUserProvGroupSAMLAttributeName": "FederatedGroups",
```
  
`jitUserProvGroupStaticListEnabled` |  Boolean property indicating whether group memberships should be assigned to the user based on a static list of group names. If this property is `true`, then the property `jitUserProvAssignedGroups` must be set. |  ```
"jitUserProvGroupStaticListEnabled": true,
```
  
`jitUserProvAssignedGroups` |  Array of groups to be assigned to the user, in addition to any values received in the SAML assertion, if the property `jitUserProvGroupStaticListEnabled` is `true`. **Note:** The values set in this array are group IDs (not group names). |  ```
"jitUserProvAssignedGroups": 
[
{"value": "21f273857a304684a8f7e353e452a2e1"},
{"value": "1962687f74b84121b69c5560769e8b06"}
],
```
  
`jitUserProvGroupAssignmentMethod` |  String property that controls how group memberships will be assigned to the user in the identity domain. The value must be one of:
  * `Overwrite` - Replace all the user's group memberships with the ones received in the SAML assertion and/or statically configured here.
  * `Merge` - Add to the user's existing group memberships the ones implicitly mapped from the SAML assertion and/or statically configured here. Explicitly mapped groups are always overwritten/replaced with the SAML assertion values. **Note:** When using the merge option, If you remove a user from the IdP, you must also remove the user from the identity domain. The permissions aren't automatically removed from the identity domain. 

|  ```
"jitUserProvGroupAssignmentMethod": "Merge",
```
  
`jitUserProvIgnoreErrorOnAbsentGroups` |  Boolean property that determines the action to take when the incoming assertion attribute specifies a group that doesn't exist or a group for which a group mapping doesn't exist in the identity domain. If this property is true, then the missing group is ignored, and the user is created. If this property is false, and a nonexistent group is specified, user creation will fail. Defaults to true for **explicit** mode, and false for **implicit** mode specified using `jitUserProvGroupMappingMode`. |  ```
"jitUserProvIgnoreErrorOnAbsentGroups": true,
```
  
## Configuring the jitUserProvAttributes Mapping 🔗 
After the `IdentityProvider` has been created, and the SAML JIT Provisioning attributes configured as needed, the `jitUserProvAttributes` resource must be updated to add your inbound attribute mappings. The `MappedAttributes` resource, referenced by `jitUserProvAttributes`, is automatically created and deleted with the `IdentityProvider` resource, and this property is marked immutable. The SAML JIT Provisioning attribute mappings are configured by updating the existing `MappedAttributes` object, not by replacing it.
The following table describes the `MappedAttributes` properties used by SAML JIT Provisioning.
`MappedAttributes` Property | Description | JSON Examples  
---|---|---  
`attributeMappings` |  The list of mappings between the SAML assertion attributes and the identity domain user attributes. Each mapping consists of:
  * `idcsAttributeName` - An expression defining the path to the user attribute that should be assigned an incoming value. Expressions follow the SCIM syntax, as used by the identity domains User Sync feature. The expression given for this attribute is validated against the `User` schema.
  * `managedObjectAttributeName` - A policy expression defining the value to be mapped into the user attribute. This can have values such as `$(assertion.firstname)` to refer to an assertion attribute called "firstname", or it can be a static string literal, or a function. 

**Note:** SAML assertion attribute names are case-sensitive.  |  ```
"attributeMappings":[
{
"idcsAttributeName": "userName",
"managedObjectAttributeName": "$(assertion.mail)"
},
{
"idcsAttributeName": "name.givenName",
"managedObjectAttributeName": "$(assertion.firstname)"
},
{
"idcsAttributeName": "name.familyName", 
"managedObjectAttributeName": "$(assertion.lastname)" 
}, 
{ 
"idcsAttributeName": "emails[primary eq true and type eq \"work\"].value", 
"managedObjectAttributeName": "$(assertion.mail)" 
}, 
{ 
 "idcsAttributeName": "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:isFederatedUser", 
"managedObjectAttributeName": "#toBoolean(\"false\")"
}, 
{
"idcsAttributeName":
"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:Organization",
"managedObjectAttributeName": "ACME Corporation"}, 
{ 
"idcsAttributeName": "externalId", 
"managedObjectAttributeName":
"#concat(\"ACME/\",$(assertion.fed.nameidvalue))" 
}
],
```
  
`refResourceType` |  The name of the resource that is using/has a reference to this mapped attribute (always `IdentityProvider` in case of SAML JIT Provisioning, don't update). |  ```
"refResourceType": "IdentityProvider",
```
  
`idcsResourceType` |  The type of the identity domain resource to which we're mapping (always `User` in the case of SAML JIT Provisioning, don't update). |  ```
"idcsResourceType": "User",
```
  
`direction` |  Direction of the mapping, with respect to the identity domain resource in question (always `inbound` in the case of SAML JIT Provisioning, don't update). |  ```
"direction": "inbound",
```
  
`refResourceID` |  The ID of the `IdentityProvider` resource that has a reference to this `MappedAttribute` resource (set at creation, don't update). |  ```
"refResourceID": "<IDP Resource ID>",
```
  
To update the attribute mappings, first you must identify the correct `MappedAttributes` resource for your IdP. This can be done by retrieving the `IdentityProvider` resource, and looking at the `$ref` attribute of the `jitUserProvAttributes` property.
For example, you might have a `MappedAttributes` resource such as `https://<domainURL>/admin/v1/MappedAttributes/6533d475754845a8b0e971c48b87edda`, which you would then PATCH to update its `attributeMappings` property.
## Sample PATCH Payload for MappedAttributes 🔗 
```

{
 "schemas": [
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],  "Operations": [
   {
     "op": "replace",
     "path": "attributeMappings",
     "value": [
       {
         "managedObjectAttributeName": "$(assertion.mail)",
         "idcsAttributeName": "userName"
       },
       {
         "managedObjectAttributeName": "$(assertion.firstname)",
         "idcsAttributeName": "name.givenName"
       },
       {
         "managedObjectAttributeName": "$(assertion.lastname)",
         "idcsAttributeName": "name.familyName"
       },
       {
         "managedObjectAttributeName": "$(assertion.mail)",
         "idcsAttributeName": "emails[primary eq true and type eq \"work\"].value"
       }
     ]
   }
 ]
}

```

## SAML JIT Provisioning Attribute Mapping Usage and Runtime Behavior 🔗 
If values for `userName`, `name.givenName` and `name.familyName` aren't present, there's an error at runtime, since those attributes are marked required in the `User` schema. The same is true for _primary email address_ , unless the tenant has been configured to make that optional.
At runtime, if any assertion attribute value cannot be converted to a data type that can be assigned to the user attribute to which it's mapped, there will be an error and SSO will fail.
If multiple attribute mappings are configured targeting the same identity domains user attribute, they're evaluated and executed in position order, and only the last mapping's result is retained.
An incoming assertion attribute that contains no values will result in the removal of the value from the corresponding mapped identity domains user attribute, if `jitUserProvAttributeUpdateEnabled` is `true`.
The SAML assertion attributes Issuer and Subject NameID are supported, even though they don't appear in the AttributeStatement. They can be mapped using these reserved expressions:
  * `${assertion.fed.issuerid)`
  * `$(assertion.fed.nameidvalue)`


Some identity domains user/account schema attributes aren't allowed for use in SAML JIT Provisioning:
  * Sensitive attributes - that is, attributes marked `"idcsSensitive: hash"` or `"idcsSensitive: encrypt"` in the schema
  * Attributes that are marked `"idcsInternal: true"` in the schema
  * Attributes that are readOnly
  * All attributes that User Sync disallows


When a user is created using SAML JIT Provisioning, the following attributes will be set. These attributes aren't configurable:
  * `bypassNotification : true` - For example, an account activation email will not be sent to the newly-created user.
  * `syncedFromApp` - A reference to the Identity Provider resource corresponding to the issuer of the inbound SAML assertion.


When a user is created using SAML JIT Provisioning, the `isFederatedUser` attribute is set to `true` by default. This behavior can be changed by setting the `isFederatedUser` attribute to `false` in the SAML JIT Provisioning `attributeMappings` configuration.
**Note** This default behavior (`isFederatedUser = true`) applies only to user creation, not user update; the `attributeMappings` configuration applies to both user creation and user update.
## Frequently Asked Questions 🔗 
**Q: Is it mandatory for groups to be present in identity domains to update group membership during SAML JIT Provisioning?**
A: Yes. Groups need to be synced or created manually in identity domains before group membership is updated. SAML JIT Provisioning will not create groups on the fly.
**Q: Can I map a literal in attribute mapping? For example, I want to map`isFederatedUser = true` during user creation?**
A: Yes.
**Q: Do we support multivalued attributes in attribute mapping? If yes, do we patch the payload or do an override?**
A: Yes. All values of the identity domain user attribute are replaced with the net result of the SAML JIT Provisioning attribute mapping.
**Q: If a user is removed from a group in the IdP, how do we handle it? What if that group is manually assigned in identity domains? Can we configure replace versus patch behavior?**
A: Group assignment using SAML JIT Provisioning update can be configured to have either Merge or Overwrite behavior, for the user's group assignments overall. For example, if update is configured for Overwrite, any manual group assignments that don't appear in the IdP assertion, will be removed.
**Q: Can we configure SAML JIT Provisioning to occur only during user creation, but not to update the user later?**
A: Yes. If `jitUserProvCreateUserEnabled` is true and `jitUserProvAttributeUpdateEnabled` is false, SAML JIT Provisioning will create users if they're missing, but will not update them on subsequent logins.
Was this article helpful?
YesNo

