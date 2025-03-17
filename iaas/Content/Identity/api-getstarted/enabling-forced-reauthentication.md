Updated 2025-01-31
# Enabling Forced Reauthentication
To force a user to reauthenticate while accessing an application, even if a valid OCI IAM session is available, set `forceReauthenticateAfterInMinutes` using the REST API endpoint.
**Note**
To enable this functionality, the `access.sso.session.max.age` feature needs to be enabled.
OCI IAM maintains the attribute `forceReauthenticateAfterInMinutes` at the application level. When an application makes an authentication request to OCI IAM, the service evaluates if the time duration since last authentication has exceeded the value set in the `forceReauthenticateAfterInMinutes` attribute for that app. If it has, then OCI IAM forces the user to reauthenticate. By default the value is NULL and reauthentication isn't enforced.
Possible values for this attribute:
  * **NULL** (default)—No reauthentication
  * **-1** —No reauthentication
  * **0** to **32767** —Duration in minutes after which a user is forced to reauthenticate


If authenticating with external identity providers, OCI IAM tries to enforce reauthentication at the external IdPs.
  * For OIDC, OCI IAM passes the max_age attribute in the /authorize request.
  * For SAML, based on AuthNInstant returned in the SAML response by the external identity provider, OCI IAM sends a second SAML request to the IdP with `ForceAuthn=true`. 


The max_age attribute value received in the request takes precedence over the `forceReauthenticateAfterInMinutes` value configured at the app level, but the max_age protocol must be implemented correctly to work. For example, if the IdP doesn't return the id_token or include auth_time in the id_token, then the max_age protocol won't work, and your application will return an error when trying to sign in. Google and Facebook are examples of identity providers that haven't implemented the max_age protocol correctly as of now. 
**Note** When OCI IAM is federated to an external identity provider, OCI IAM can't guarantee if a user is forced to reauthenticate by an external identity provider. The behavior depends on how OIDC/SAML protocols are implemented at the external identity provider.
Curl to update `forceReauthenticateAfterInMinutes` attribute on app.```

curl --location --request PATCH 'https://{{IDCS_HOST}}/admin/v1/Apps/{{APP_ID}}' --header 'X-RESOURCE-IDENTITY-DOMAIN-NAME: tenantsp' --header 'Authorization: Bearer {{IDENTITY_DOMAIN_ADMINSTRATOR_TOKEN}}' --header 'Content-Type: application/json' --data-raw '{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "forceReauthenticateAfterInMinutes",
      "value": {{value}}
    }
  ]
}'
```

Was this article helpful?
YesNo

