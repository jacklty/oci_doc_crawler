Updated 2024-04-02
# Token Exchange Grant Type: Exchanging a Kerberos Token for a UPST
Use Kerberos token exchange where Kerberos is the authentication provider and you need to exchange Kerberos tokens for IAM tokens or principals to access OCI services. You exchange Kerberos tokens for OCI user principal session tokens (UPST) in IAM.
[Kerberos Token Terms](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm)
Term | Description  
---|---  
Kerberos |  A cross-platform authentication and single sign-on system. The Kerberos protocol provides mutual authentication between two entities relying on a shared secret (symmetric keys). Kerberos authentication requires a client, a server, and a trusted party to mediate between them called the Key Distribution Center (KDC). The following is also required:
  * A Principal: An identity for a user (a user is assigned a principal), or an identity for an application offering Kerberos services.
  * A Realm: A Kerberos server environment, which can be a domain name such as `example.com`. Each Kerberos realm has at least one Web Services Security KDC.

The Kerberos Token profile of WS-Security allows business partners to use Kerberos tokens in service-oriented architectures (SOAs).  
Kerberos Key Distribution Center (KDC) | A third-party authentication server.  
Active Directory (AD) | A repository for the KDC server.  
Keytab |  A file that stores the actual encryption key that can be used instead of a password challenge for a specific principal. Keytab files are useful for noninteractive use cases. **Tip:** The KDC admin tool can be used to create a keytab file. During keytab creation, the encryption type can be specified. Use the following encryption type: `aes256-cts-hmac-sha1-96`.  
Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO) |  Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO) is a GSSAPI "pseudo mechanism" used by client/server software to negotiate the choice of security technology. Kerberos tickets are wrapped as part of the SPNEGO token so that the token works with HTTP based application layer. SPNEGO Token Format and Details  The SPNEGO token format is defined in RFC 4178. The token is a serialized data structure that contains the following fields:
  * `mechTypes`: A sequence of object identifiers (OID) that lists the supported authentication mechanisms.
  * `mechToken`: An optimistic mechanism token. This is a token that's used to negotiate the actual authentication mechanism that will be used.
  * `krb5Creds`: A Kerberos blob. This is a binary blob that contains the Kerberos authentication information.

The SPNEGO token is encoded in ASN.1. The following is an example of a SPNEGO token: ```
NegTokenInit ::= SEQUENCE
{
mechTypes SEQUENCE OF Oid,
mechToken OCTET STRING,
krb5Creds [0] KerberosCreds OPTIONAL
}
```
  
GSSAPI | Generic Security Services Application Program Interface  
IAM Token Exchange Service API | IAM identity domain OAuth service: `/oauth2/v1/token`. The API accepts both standard OAuth based authentication headers/payload, and OCI Signatures. To learn how to use an OAuth client with an identity domain to access the REST APIs, see [Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm "The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to programmatically manage users, groups, applications, and identity functions, such as password management and administrative tasks. To make REST API calls to your identity domain, you need an OAuth2 access token to use for authorization. The access token provides a session \(with scope and expiration\), that your client application can use to perform tasks in an identity domain.").  
Identity Propagation Trust Configuration | Use Identity Propagation Trust configurations to establish the trust between OCI Identity and an external identity provider and validate the external identity provider token and the mapping of the external identity provider's user identity with the user identity in IAM. Identity Propagation Trust also facilitates identity propagation from an external identity provider into OCI. The `/IdentityPropagationTrust` endpoint design is generic and works with any cloud provider. To create an Identity Propagation Trust configuration, see [Step 6: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-propagation-trust-configuration).   
Service User | A user without interactive login privileges. These Service Users can be granted to groups and service roles. Applications can use these Service Users or the logged-in user can impersonate them to obtain a temporary UPST. Using a Service User is optional. For more information about using Service Users, see [Step 5: Use a Service User (Optional)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-service-user).  
User Principal Session Token (UPST)  | An IAM generated token. Also known as a security token. It represents the authenticated Service User.   
## Kerberos Token Exchange Steps 🔗 
Use the following steps to exchange a Kerberos token for a UPST:
  1. [Step 1: Create a Vault and Add the Keytab File Contents](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-oci-vault-add-keytab)
  2. [Step 2: Create the Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__keytab-required-iam-policy)
  3. [Step 3: Create an Identity Domain Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-domain-app-allow-token-exchange)
  4. [Step 4: Generate a SPNEGO Token For a Specific User Principal](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__generate_spnego_token)
  5. [Step 5: Use a Service User (Optional)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-service-user)
  6. [Step 6: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-propagation-trust-configuration)
  7. [Step 7: Get the OCI UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__get-oci-upst)


## Step 1: Create a Vault and Add the Keytab File Contents 🔗 
Create a Vault and add the keytab file content as a base64-encoded string. **Note:** IAM doesn't store the keytab file in its file system. 
Use the following steps as a guide:
  1. Create a Vault. See [Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm). 
  2. Read the keytab content in Base64 format.
  3. Go to the Vault and store it as is, making sure to check Base64 as the **Secret Type Template** while creating secret. See [Creating a Secret in a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm).


## Step 2: Create the Required IAM Policy 🔗 
Create an IAM policy in the tenancy to allow an identity domain resource to access Vault. This allows IAM to retrieve the keytab configuration from Vault. Use the following example as a guide:
```
allow resource iam-domain <domain_displayName> to read secrets from vault in compartment <compartment_ocid> where all {target.secret.id = <secret_ocid_where_the_keytab_is_present>}
```

## Step 3: Create an Identity Domain Application 🔗 
Create an identity domain Confidential application. After you create the application, save the _client id_ and the _client secret_ in a secure location. See [Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server."). 
## Step 4: Generate a SPNEGO Token For a Specific User Principal 🔗 
  1. Use Java code to connect to the KDC Server and generate the SPNEGO token.
  2. Copy that SPNEGO token to form the token request.


Use the following Java code example as a guide:
```
package com.oracle;
import com.sun.security.auth.module.Krb5LoginModule;
import org.ietf.jgss.GSSContext;
import org.ietf.jgss.GSSException;
import org.ietf.jgss.GSSManager;
import org.ietf.jgss.GSSName;
import org.ietf.jgss.Oid;
import javax.security.auth.Subject;
import java.io.IOException;
import java.security.Principal;
import java.security.PrivilegedAction;
import java.util.Base64;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
public class GenerateSpnegoToken {
  static String servicePrincipal = "HTTP/iamtesp@WINDOWSKDCSERVER.COM";
  static String userPrincipal = "HTTP/<sample-job>@WINDOWSKDCSERVER.COM";
  static String userPrincipalKeyTab = "keytabs/ms/<sample-job>.keytab";
  public static void main(String[] args) throws IOException {
    System.setProperty("sun.security.krb5.debug", "true");
    System.setProperty("sun.security.spnego.debug", "true");
    System.setProperty("java.security.krb5.conf", "ms_krb5.conf");
    String spnegoToken = generateSpnegoToken();
  }
  private static String generateSpnegoToken() {
    Subject subject = getAuthenticateSubject();
    return Subject.doAs(
        subject,
        (PrivilegedAction<String>)
            () -> {
              String SPNEGO_OID = "1.3.6.1.5.5.2";
              String KRB5_MECHANISM_OID = "1.2.840.113554.1.2.2";
              String KRB5_PRINCIPAL_NAME_OID = "1.2.840.113554.1.2.2.1";
              try {
                // Create GSS context for the service principal and the logged-in user
                Oid krb5Mechanism = new Oid(KRB5_MECHANISM_OID);
                Oid krb5PrincipalNameType = new Oid(KRB5_PRINCIPAL_NAME_OID);
                Oid spnegoOid = new Oid(SPNEGO_OID);
                GSSManager manager = GSSManager.getInstance();
                GSSName gssServerName =
                    manager.createName(servicePrincipal, krb5PrincipalNameType, krb5Mechanism);
                GSSContext gssContext =
                    manager.createContext(
                        gssServerName, spnegoOid, null, 240000);
                gssContext.requestMutualAuth(true);
                gssContext.requestCredDeleg(true);
                gssContext.requestLifetime(10);
                // Generate the SPNEGO token
                byte[] token = new byte[0];
                token = gssContext.initSecContext(token, 0, token.length);
                return Base64.getEncoder().encodeToString(token);
              } catch (GSSException e) {
                throw new RuntimeException(e);
              }
            });
  }
  private static Subject getAuthenticateSubject() {
    final Map<String, String> options = new HashMap<>();
    options.put("keyTab", userPrincipalKeyTab);
    options.put("principal", userPrincipal);
    options.put("doNotPrompt", "true");
    options.put("isInitiator", "true");
    options.put("refreshKrb5Config", "true");
    options.put("storeKey", "true");
    options.put("useKeyTab", "true");
    // Execute the login
    Subject subject = new Subject();
    Krb5LoginModule krb5LoginModule = new Krb5LoginModule();
    krb5LoginModule.initialize(subject, null, new HashMap<String, String>(), options);
    try {
      krb5LoginModule.login();
      krb5LoginModule.commit();
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
    Set<Principal> principals = (Set<Principal>) subject.getPrincipals();
    Iterator<Principal> iterator = principals.iterator();
    while (iterator.hasNext()) {
      System.out.println("\nprincipal : " + ((Principal) iterator.next()));
    }
    return subject;
  }
}

```

## Step 5: Use a Service User (Optional) 🔗 
A Service User is an identity domains User with the attribute `serviceUser` set to `true`.
**Note** Using a Service User is optional. If user impersonation will be used as part of the Trust configuration, then Service Users are needed. Otherwise, any other identity domain user is used. Only identity domain administrators can create, replace, update or delete a Service User. Other administrators may read Service Users and their attributes.
To use a Service User, create one without interactive login privileges. These Service Users can be granted to groups and service roles. Your applications can use these Service Users or the logged-in user can impersonate them to obtain a temporary UPST token.
Service Users have the following characteristics:
  * Must have a **userName**. First name and last name isn't required.
  * Can have an email address (Optional).
  * Can be a member of groups and application roles.
  * Can't have API keys.
  * Can't use self-service endpoints.
  * Can't have passwords and password policies don't apply.


**Request Example: Create a Service User**
The following shows an example of a request with the minimum attributes required to create a Service User.
```
## POST on https://<domainURL>/admin/v1/Users
## Payload:
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
    "serviceUser": true
  },
  "userName": "myServiceUserName"
}
```

**Response Example: Create a Service User**
The following shows an example of a response when creating a Service User.
```
{
  "idcsCreatedBy": {
    "type": "App",
    "display": "idcsadmin"
  },
  "id": "<user_id>",
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User": {
    "isFederatedUser": false,
    "isGroupMembershipSyncedToUsersGroups": true,
    "serviceUser": true
  },
  "meta": {
    "created": "2023-12-07T06:52:55.380Z",
    "lastModified": "2023-12-07T06:52:55.380Z",
    "version": "<version>",
    "resourceType": "User",
    "location": "https://<domainURL>/admin/v1/Users/<user_id>"
  },
  "active": true,
  "idcsLastModifiedBy": {
    "display": "idcsadmin",
    "type": "App"
  },
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User": {
    "locked": {
      "on": false
    }
  },
  "ocid": "ocid1.user.region1...<ocid>",
  "userName": "myServiceUserName",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:capabilities:User",
    "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
  ]
}
```

## Step 6: Create an Identity Propagation Trust Configuration 🔗 
The Identity Propagation Trust configuration is used to establish the trust between OCI Identity and the external Cloud providers, the validation of the Cloud provider token, and the mapping of the Cloud provider's user identity with the identity domains `service` user identity. 
[Detailed Description of an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm)
Attribute | Mandatory? | Descriptions and Examples  
---|---|---  
name | Yes |  The name of the trust.  
type | Yes |  The token type: 
  * spnego
  * jwt
  * saml
  * aws-credential

  
issuer | Yes |  Use Issuer to help find the Trust identification. For example, if the SPNEGO token is generated using the service principal, `IAMSp`, then `IAMSp` is the issuer value. Example: `IAMTokenExchangeServicePrincipal`  
active | Yes |  If enabled, `true`. If disabled, `false`.  
oauthClients | Yes |  A list of OAuth Clients who are allowed to get tokens for a specific trusted partner. Example: ```
"oauthClients": [
 "oauthclient-id"
 ],
```
  
allowImpersonation (make use of serviceUser) | No |  Boolean value. Specifies whether the resulting UPST should contain the authenticated user as the subject, or if it should impersonate a Service User in IAM.  
impersonatingServiceUser |  Yes, if `allowImpersonation` is set to `true`. | Specifies which resulting principal is going to impersonate based on the token claim name and the value conditions. You can: 
  * Allow a specific impersonating principal for all the identity provider (IdP) authenticated users. 
  * Set rules to define impersonation conditions: 
    * Based on the Token claim name 
    * Condition: contains (`co`) or equals (`eq`)
    * Value:
      * Can be a string.
      * Array of values and complex/composite values aren't supported.
      * With _equals_ condition: _wild card (*) is allowed_.
      * With _contains_ condition: _wild card (*) isn't supported_.
    * Impersonating principal.

Example:
  * Rule: `"username" eq kafka*`
  * Mapped Service User: `kafka`
  * Result: All the authenticated users starting with the `kafka` prefix are impersonated with the IAM Service User `kafka`. The resulting UPST contains `kafka` as the authenticated user principal.

If impersonation is allowed, the resulting OCI security token (UPST), will have the original authenticated user related claim (`source_authn_prin`) as well to indicate on whose behalf impersonation is done. 
  * _If subject claim name is configured_ , it will be used to extract that claim value.
  * _If subject claim name isn't configured_ , it defaults to `sub` in the incoming token. If `sub` claim itself isn't present, it's ignored.

Evaluation stops with the first matched rule and the corresponding resulting principal is returned using the display name attribute. If no rules are matched, then the token request fails with errors.  
keytab |  Yes, if the token type is `SPNEGO`. |  Retrieves the keytab configuration from Vault. **Important:**
  * The token exchange service retrieves the secret information based on the secret OCID and the secret version. 
  * If keytab is rotated in the KDC server, then you must update the secret information in the Identity Propagation Trust configuration.
  * If keytab is rotated in Vault, then you must update the secret information in the Identity Propagation Trust configuration.

  
**Request Example: Create an Identity Propagation Trust Configuration**
The following shows an example of a request to create an Identity Propagation Trust configuration.```
## POST on https://<domainURL>/admin/v1/IdentityPropagationTrusts
## Payload:
{
 "active": true,
 "allowImpersonation": false,
 "issuer": "idcs_psr_itp",
 "name": "<identity_propagation_trust_name>",
 "oauthClients": [
 "<oauthclient-id>"
 ],
 "keytab": {
 "secretOcid": "<secret_ocid>"
 },
 "subjectMappingAttribute": "userName",
 "subjectType": "User",
 "type": "SPNEGO",
 "schemas": [
 "urn:ietf:params:scim:schemas:oracle:idcs:IdentityPropagationTrust"
 ]
}
```

**Response Example: Create an Identity Propagation Trust Configuration**
The following shows an example of a response when creating an Identity Propagation Trust configuration.```
 "response": {
  "name": "<identity_propagation_trust_name>",
  "type": "<token_type>",
  "issuer": "idcs_psr_itp",
  "accountId": "<example_account_id>",
  "subjectClaimName": "cognito:username",
  "subjectMappingAttribute": "username",
  "subjectType": "User",
  "clientClaimName": "appId",
  "clientClaimValues": ["<client_claim_value>"],
  "active": true,
  "publicKeyEndpoint": "https://example.identityprovider.com/publickey/<publickey_value>",
  "publicCertificate": "<public_certificate_value>",
  "oauthClients": ["<oauthclient-id>"],
  "allowImpersonation": true,
  "impersonationServiceUsers": [
   {
    "rule": "groups co \"network-admin\"",
    "userId": "<user_id>"
   },
   {
    "rule": "groups co \"tenancy-admin\"",
    "userId": "<user_id>"
   }
  ],
  "keytab": {
   "secretOcid": "<secret_ocid>",
   "secretVersion": "<secret_version>"
  },
  "clockSkewSeconds": 60,
  "id": "<identity_propagation_trust_id>",
  "meta": {
   "created": "2023-11-09T23:26:53.224Z",
   "lastModified": "2023-11-09T23:26:53.224Z",
   "resourceType": "IdentityPropagationTrust",
   "location": "http://example.hostname.com:8990/admin/v1/IdentityPropagationTrusts/<identity_propagation_trust_id>"
  },
  "schemas": [
   "urn:ietf:params:scim:schemas:oracle:idcs:IdentityPropagationTrust"
  ],
  "idcsCreatedBy": {
   "value": "<app_id>",
   "display": "admin",
   "type":"App",
   "$ref": "http://example.hostname.com:8990/admin/v1/Apps/<app_id>"
  },
  "idcsLastModifiedBy": {
   "value": "<app_id>",
   "display": "admin",
   "type":"App",
   "$ref": "http://example.hostname.com:8990/admin/v1/Apps/<app_id>"
  }
 }
```

## Step 7: Get the OCI UPST 🔗 
[Detailed Description of the UPST Token Request Payload](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm)
Request Parameter | Valid Value  
---|---  
`grant_type` |  `'grant_type=urn:ietf:params:oauth:grant-type:token-exchange'`  
`requested_token_type` |  ``'requested_token_type=urn:oci:token-type:oci-upst'``  
`public_key` |  `'public_key=<public-key-value>'` The public key workflow:
  1. The workload generates a key pair.
  2. The public key is sent as part of token exchange request, which gets added as a claim, `jwk`, into the resulting UPST.
  3. The private key is used to generate the OCI signatures for the OCI native services API invocation along with the UPST.
  4. OCI services authentication validates the UPST, extracts the `jwk` claim from the UPST, and then uses it to validate OCI signature.

  
`subject_token_type` |  `'subject_token_type=spnego'`
  * spnego
  * jwt
  * saml
  * aws-credential

  
`subject_token` |  `'subject_token=<subject-token>'` If the token type is: 
  * `spnego`: The opaque encrypted token.
  * `jwt` or `saml`: The `jwt` or `saml` assertion value as is.
  * `aws-credential`: The base64 encoded value of the AWS Credentials which appear in XML format.

  
`issuer` |  Mandatory if the token type is `spnego`. Example: `IAMTokenExchangeServicePrincipal`  
**UPST Token Request Example: OCI Signature-based**
The following shows an example OCI signature-based cURL request.
```
## OCI Signature Based Request
curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
-H 'date: Wed, 06 Dec 2023 01:17:33 GMT' 
-H 'x-content-sha256: <key>' 
-H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
-H 'content-length: 197' 
-H 'Authorization: Signature version="1",keyId="<key_id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="a+aH0b...TLtPA=="' --data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
--data-urlencode 'requested_token_type=urn:oci:token-type:oci-upst' \
--data-urlencode 'public_key=<public_key>' \
--data-urlencode 'subject_token=<subject_token>' \
--data-urlencode 'subject_token_type=spnego' \
--data-urlencode 'issuer=<Issuer stored in the Identity Trust Propagation. For example, examplead@kdcserver.com>' -k
{
  "token": "<token_id>"
}
```

**UPST Token Request Example: Identity Domain App-based**
The following shows an example OCI identity domain app-based cURL request.
```
## IAM Domain App Based Request. Note that client credentials can be sent as part of basic authn header or in the payload. 
curl --location ' https://<domainURL>/oauth2/v1/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic <auth_code>' \
--data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
--data-urlencode 'requested_token_type=urn:oci:token-type:oci-upst' \
--data-urlencode 'public_key=<public_key>' \
--data-urlencode 'subject_token=<subject_token>' \
--data-urlencode 'subject_token_type=spnego' \
--data-urlencode 'issuer=<Issuer stored in the Identity Trust Propagation. For example, examplead@kdcserver.com>' -k
{
  "token": "<token_id>"
}
```

Was this article helpful?
YesNo

