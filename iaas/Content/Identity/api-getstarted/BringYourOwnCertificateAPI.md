Updated 2025-01-21
# Bring Your Own Certificate
Use custom certificates to configure SAML SSO in an identity domain.
A Certificate Signing Request (CSR) is a block of encoded text submitted to a Certificate Authority (CA) to apply for a new Certificate. A CSR contains information included in the Certificate. For example, Common Name, Organization, Organizational Unit, and Public Key are included in the Certificate.
## Before You Begin
Perform the following actions before you start using your own CSR.
  1. Submit a service request (SR) to enable BYOC on your identity domains. Provide the following details in the SR:
     * The Identity Domain's GUID. For example, `ocid1.group.oc1..exampleuniqueID`.
     * Provide your reason and use case for the request.
     * Tenancy region.
     * The component must be "`SAML`".
  2. Create an access token with an `Identity Domain Administrator` role to perform the following API commands. For more information on how to create an Access token, see [Generating an Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-personal-access-tokens.htm#generate-personal-access-tokens "An access token is an authorization that's used by a client application to access an API or a resource application within a limited period.").
    1. Create a confidential application in the identity domain. For more information, see [Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server.").
       * Configure the application as a client.
       * On the page to configure OAuth, select **Add app roles** , and then select the application roles you want to apply to this application. Assign **Identity Domain Administrator** to the list of app roles. 
       * Use the client GUID and client secret to generate the Access token using a token endpoint.


## 1: Generating a Certificate Signing Request 🔗 
Create a CSR for an identity domain (ID), make a POST request to the `CertificateSigningRequests` endpoint:```
https://<domain-url>/admin/v1/CertificateSigningRequests
```

Sample request payload:```
{
  "schemas": [
     "urn:ietf:params:scim:schemas:oracle:idcs:CertificateSigningRequest"
     ],
  "certSubjectName":"CN=www.someDomainName.com,O=MyCompany,OU=IT,C=US,S=Massachusetts,L=Boston",
  "certSubjectAltName":["oracle.com", "10.0.0.1", "test.customCertificate@gmail.com"],
  "includeKeyUsage": true,
  "signatureAlgorithm": "SHA384WITHRSA"
}
```

Property name | Required? | Data type | Description  
---|---|---|---  
`certSubjectName` | Optional | Array |  Certificate Subject Name or Certificate Name details. Common Name is required and all other parameters are optional. For example, 
  * "CN=Sample Certificate,OU=Employees,O=Sample Corporation,C=US"
  * "CN=[www.samplecertificate.com](http://www.samplecertificate.com)"

  
`certSubjectAltName` | Required | String | Certificate Subject Alternate Name. For example, a certificate that lets several domain names to be protected by a single certificate has a SAN list defined in it.  
`includeKeyUsage` | Optional | Boolean | If true, key usages are included from the CSR. If false, key usages are omitted.  
`signatureAlgorithm` | Optional | String | By default, the signature algorithm is `SHA256WITHRSA`. Supported values are 
  * "SHA256WITHRSA"
  * "SHA384WITHRSA"
  * "SHA512WITHRSA"

  
Expected response:```
{
  "csr": "-----BEGIN CERTIFICATE REQUEST-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END CERTIFICATE REQUEST-----"
}
```

Property name | Data type | Description  
---|---|---  
`csr` | String | Certificate Signing Request generated using the values defined in the API payload.  
## 2: Getting a Certificate Issued by a Preferred Certificate Authority 🔗 
Use the CSR you generated in step 1 to get a certificate issued from your preferred Certificate Authority (CA).
The expected outcome of this step is a certificate in `.pem`, `.cer`, or `.crt` format. Open this certificate in a text editor and copy the base64 encoded part of it, as required to create a SAML partner certificate.
## 3: Creating a SAML Partner Certificate 🔗 
The expected certificate format is `.pem`, `.cer`, or `.crt` format from your preferred certificate provider.
To create a SAML partner certificate for an identity domain, open the certificate file, copy the base64-encoded portion, and paste it into a POST request to the API endpoint `SamlPartnerCertificates`:```
https://<domain-url>/admin/v1/SamlPartnerCertificates
```

Sample request payload:```
{
  "certificateAlias": "TestCertificate1",
  "x509Base64Certificate": xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SamlPartnerCertificate"
  ]
}
```

Payload property details:
Property name | Required? | Data type | Description  
---|---|---|---  
`x509Base64Certificate` | Required | String | Certificate issued by a preferred CA which is generated using the CSR.  
`displayName` | Required | String | A unique user- friendly name for the certificate.  
`includeKeyUsage` | Optional | Boolean | If true, key usages are included from the CSR. If false, key usages are omitted.  
Expected response:```
{
  "certificateAlias": "TestCertificate1",
  "id": "dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx4",
  "x509Base64Certificate": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "sha1Thumbprint": "7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx9",
  "sha256Thumbprint": "axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc",
  "sha384Thumbprint": "1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxf",
  "certStartDate": "2024-05-28T17:22:51Z",
  "certEndDate": "2024-07-27T17:22:51Z",
  "ocid": "ocid1.domaincertificate.region1.sea.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "meta": {
    "lastModified": "2024-05-29T23:40:16.585Z",
    "created": "2024-05-29T23:40:16.585Z",
    "resourceType": "SamlPartnerCertificate",
    "location": "https://<domainURL>.oci.oracleiaas.com:443/admin/v1/SamlPartnerCertificates/xxxxxx"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:SamlPartnerCertificate"
  ],
  "base64Certificate": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```

Property name | Data type | Description  
---|---|---  
`Id` | String | Unique GUID for the SAML Partner Certificate resource.  
`x509Base64Certificate` | String | Certificate issued by customer's preferred CA, which is generated using the CSR.  
`displayName` | String | A customer defined, unique user-friendly name for the certificate.  
`b64certificate` | String | Base64 encoded string of customer's signing certificate.  
`description` | String | A short description about the certificate.  
`certStartDate` | Datetime | Issued date of the certificate.  
`certEndDate` | Datetime | Expiration date of the certificate.  
`sha1Thumbprint` | String | SHA-1 thumbprint of the certificate.  
`sha256Thumbprint` | String | SHA-256 thumbprint of the certificate.  
`sha384Thumbprint` | String | SHA-384 thumbprint of the certificate.  
## 4: Listing all SAML Partner Certificates for an Identity Domain 🔗 
To list all SAML partner certificate for an identity domain, make a GET request to the endpoint `SamlPartnerCertificates`:```
https://<domain-url>/admin/v1/SamlPartnerCertificates
```

Expected response:```
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 2,
  "Resources": [
    {
      "certificateAlias": "TestDemo1Certificate",
      "id": "18c7ad1f268c222262075fbc37ad96a",
      "x509Base64Certificate": "MIIDlDCCAnygAwIBAgICChowDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoTG2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MDIxNjQzNDRaFw0yNDA3MDExNjQzNDRaMFoxCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQBgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxGTAXBgNVBAMMEHd3dy50ZXN0YnlvYy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCUD5uHuP8KOrB9dlkO+vp61yjlc0moCI1cPeD0doTdHwLnSiBMFoR/gpSVZWiEi3iDRrK65/sj+qBUEDVZZ/0hDNq1j40HcUbyqQNqK5hIImPc9dXXIH9tmZkuVEMvgAupNhFznw8WTrf4LNRe7sxri/CFxt+Ajrm1CMlxRxZARYcUkFuc5aclgeYdCDhaI7xn8OuFJfUfsaoB4UYklpg2CyzSFOkHq7FhsW4/WkltSwxCwCZAe/eFmSemsmJkKhmuld/5D4+v3I1ghIImJ0ZpuvetPUv6ARqCIiwnRbY6ngdSaEPb5+BWsRqo6fXNlrQxxt5WdcCZMAcXy8qA/w3PAgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQDAgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4yLjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBACIbYxgP3H4RFa87TLLY3lOK4nlep6zsUmSzZonRmrnb39S0Oa9RQJJix1qX2RlRa4u57Mk3A3o+ixgBVLEol/HIEY6KqodM8gLZI8L2wdiYZkKtnYqk0Pk4fFLlTengfrx1xqX/m+etd85XkY29U5WehZuGBB57GcxD6zDhtvN7X/FeKTrXdhbo0LbnEgQIDKypNc4bXztYFloIqRZ7Si0ORWFjnA9vvzAWRMMCDq7YmUjUHYrxY7Uuxze/S7T60gjtLFs1bL6A+NUPvEmh2oyncMxhSDMKrFnUZ6o4uagwpq7u6KPgkx+JluSLU2MXCGHsz3y5o4nsOHjsZSdXnjw=",
      "sha1Thumbprint": "d4131b512b25187036a1d0f645b39393343fee02",
      "sha256Thumbprint": "2efeccf8cfe752ef51079413653bf0e35e9c58824e824c4a9667537d99c74260",
      "certStartDate": "2024-05-02T16:43:44Z",
      "certEndDate": "2024-07-01T16:43:44Z",
      "meta": {
        "lastModified": "2024-05-23T22:53:35.622Z",
        "created": "2024-05-23T22:53:35.622Z",
        "resourceType": "SamlPartnerCertificate",
        "location": "https://<domainURL>/com:443/admin/v1/SamlPartnerCertificates/xxx"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:SamlPartnerCertificate"
      ]
    },
    {
      "certificateAlias": "TestCertificate1",
      "id": "dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc",
      "x509Base64Certificate": "MIIDlzCCAn+gAwIBAgICDqEwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoTG2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MjgxNzIyNTFaFw0yNDA3MjcxNzIyNTFaMF0xCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQBgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxHDAaBgNVBAMME3d3dy5yMXVhdGVzdGluZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCY9/PVuAW5KsmuWu4MHmHhLiiqggV10SGZhF/eqEPeo6mwudkBh1+oOWamCiDucKh6eZqQpluhz2QA5yTfJGHrwv+S+YEp7ji5E7wAT/BCTl9dffxuBsjtUrhhVDiZG08KxKA+DG5P4bVXVv41chX5fULYUpDg75GfE6CTSkniCNYUIC84yi+XKqifqi4Eh0vDaXBRLLu9EI8n+vx6zYF/5nH4r03TOivsJoVsOQpbf3TYVMifaY9S/Sg1WnBRK4Jqwdk6K4e8vHpEMUhjtFHrBiJ/5DaEIbv1x3iCv5o1efUGVVoBTRZvOG9oNQuIA/S5ZF0UoAvhoTW2jADHhDs7AgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQDAgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4yLjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBAAmNfvzl89lE2FZilK9ho19HA0mGUi3E2uiwx5BqFqk25Aoidf7GGwWg3QyXJYD4krqvy33n9VD751EG8IolSUmjR2dG/KS5T7dxNC0CVWzImBIauL9lkxzKBO5r+bmzEOogXzU53GPHnRGjXtEpzrOgJiXV2co4VMiv0JI2JJAIAd4CKDu2hhleTrc1d1ArOOCWwl+ZOOmmp3bBrn18ROLxwqS02nLaG0xLeBePlUBuI15qMxr8URy5Zixnoqbv45lZAExVax3IUTBFICHSs1ZKtaq7WFpIH0VhA0dMNEJESYbAeG91sSWpcAhSbIoHu4q0lNa7nlg6NG2HrjlvS3E=",
      "sha1Thumbprint": "7dca26c12d3572e1c82a53da560c10e858a750a9",
      "sha256Thumbprint": "a26e378fb5f2f75308eac6213d9b7bdfa8216a2f2b64b698becbecf66d3f2b7c",
      "certStartDate": "2024-05-28T17:22:51Z",
      "certEndDate": "2024-07-27T17:22:51Z",
      "meta": {
        "lastModified": "2024-05-29T23:40:16.585Z",
        "created": "2024-05-29T23:40:16.585Z",
        "resourceType": "SamlPartnerCertificate",
        "location": "https://<domainURL>:443/admin/v1/SamlPartnerCertificates/58c118d3a4c14ddebe900b47d2210088"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:SamlPartnerCertificate"
      ]
    }
  ],
  "startIndex": 1,
  "itemsPerPage": 2
}
```

## 5: Generating the SAML Metadata with SAML Partner Certificate 🔗 
To generate SAML metadata using SAML Partner Certificate, make a `GET` request to this API endpoint: `https://idcs-<identity-domain-url>/fed/v1/metadata?samlPartnerCertificateId=<guid-of-certificate-resource>`
Expected response:```
<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" xmlns:enc="http://www.w3.org/2001/04/xmlenc#" xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute" xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:x500="urn:oasis:names:tc:SAML:2.0:profiles:attribute:X500" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ID="id-bFEYTCtV0U3U0rdsQ4zuD8FFVKs-" cacheDuration="P58DT0H0M0S" entityID="https://<domain_id>.identity.oci.oracleiaas.com:443/fed" validUntil="2024-07-27T17:22:51Z">
  <dsig:Signature>
    <dsig:SignedInfo>
      <dsig:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <dsig:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <dsig:Reference URI="#id-bFEYTCtV0U3U0rdsQ4zuD8FFVKs-">
        <dsig:Transforms>
          <dsig:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
          <dsig:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        </dsig:Transforms>
        <dsig:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <dsig:DigestValue>EyL6ijqEeWAbQs9J/MKPaftgYSmtjhanxHpSCw+Mp0Q=</dsig:DigestValue>
      </dsig:Reference>
    </dsig:SignedInfo>
    <dsig:SignatureValue>gBbj7RaEwEYfukcCHDSjkbVi8FUaQrkG5y8ACbbbfgPrrDIcrWmqaPX+UHQQ50V1
HFY3hyGQw+t9HLIW5usg9XVmawK54e87EVAFuaFPFd+YtKMZlAvVMXWeAzcKm4sc
lK3RsEBbk/mXLbfUtDpAFp5uWkIdLjaWuyjGTsNe7DBA085EhKc5fMtd6hEfgPux
CD4zb9Q0Aw8Lrmjy5nHp5SeYTANyH9XaO9getyU5J7Ikkz/8HuMi3gBHzOE0CNKz
64IVySS7uMdEXqHZGBI/mkA9XvZ09qxMew1ttQ3evd3KEG+q1+DpTeSHyfvBEYgp
dnNgy7P0g8W+rCJhRUROvw==</dsig:SignatureValue>
  </dsig:Signature>
  <md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      <dsig:KeyInfo>
        <dsig:X509Data>
          <dsig:X509Certificate>MIIDlzCCAn+gAwIBAgICDqEwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMx
EzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoT
G2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MjgxNzIyNTFaFw0y
NDA3MjcxNzIyNTFaMF0xCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQ
BgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxHDAaBgNVBAMME3d3dy5yMXVh
dGVzdGluZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCY9/PV
uAW5KsmuWu4MHmHhLiiqggV10SGZhF/eqEPeo6mwudkBh1+oOWamCiDucKh6eZqQ
pluhz2QA5yTfJGHrwv+S+YEp7ji5E7wAT/BCTl9dffxuBsjtUrhhVDiZG08KxKA+
DG5P4bVXVv41chX5fULYUpDg75GfE6CTSkniCNYUIC84yi+XKqifqi4Eh0vDaXBR
LLu9EI8n+vx6zYF/5nH4r03TOivsJoVsOQpbf3TYVMifaY9S/Sg1WnBRK4Jqwdk6
K4e8vHpEMUhjtFHrBiJ/5DaEIbv1x3iCv5o1efUGVVoBTRZvOG9oNQuIA/S5ZF0U
oAvhoTW2jADHhDs7AgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQD
AgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4y
LjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBAAmNfvzl
89lE2FZilK9ho19HA0mGUi3E2uiwx5BqFqk25Aoidf7GGwWg3QyXJYD4krqvy33n
9VD751EG8IolSUmjR2dG/KS5T7dxNC0CVWzImBIauL9lkxzKBO5r+bmzEOogXzU5
3GPHnRGjXtEpzrOgJiXV2co4VMiv0JI2JJAIAd4CKDu2hhleTrc1d1ArOOCWwl+Z
OOmmp3bBrn18ROLxwqS02nLaG0xLeBePlUBuI15qMxr8URy5Zixnoqbv45lZAExV
ax3IUTBFICHSs1ZKtaq7WFpIH0VhA0dMNEJESYbAeG91sSWpcAhSbIoHu4q0lNa7
nlg6NG2HrjlvS3E=
</dsig:X509Certificate>
          <dsig:X509IssuerSerial>
            <dsig:X509IssuerName>O=getaCert - www.getacert.com, L=Seattle, ST=Washington, C=US</dsig:X509IssuerName>
            <dsig:X509SerialNumber>3745</dsig:X509SerialNumber>
          </dsig:X509IssuerSerial>
          <dsig:X509SubjectName>CN=www.r1uatesting.com, OU=IT, O=MyCompany, L=Boston, C=US</dsig:X509SubjectName>
        </dsig:X509Data>
      </dsig:KeyInfo>
    </md:KeyDescriptor>
    <md:KeyDescriptor use="encryption">
      <dsig:KeyInfo>
        <dsig:X509Data>
          <dsig:X509Certificate>MIIDlzCCAn+gAwIBAgICDqEwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMx
EzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoT
G2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MjgxNzIyNTFaFw0y
NDA3MjcxNzIyNTFaMF0xCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQ
BgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxHDAaBgNVBAMME3d3dy5yMXVh
dGVzdGluZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCY9/PV
uAW5KsmuWu4MHmHhLiiqggV10SGZhF/eqEPeo6mwudkBh1+oOWamCiDucKh6eZqQ
pluhz2QA5yTfJGHrwv+S+YEp7ji5E7wAT/BCTl9dffxuBsjtUrhhVDiZG08KxKA+
DG5P4bVXVv41chX5fULYUpDg75GfE6CTSkniCNYUIC84yi+XKqifqi4Eh0vDaXBR
LLu9EI8n+vx6zYF/5nH4r03TOivsJoVsOQpbf3TYVMifaY9S/Sg1WnBRK4Jqwdk6
K4e8vHpEMUhjtFHrBiJ/5DaEIbv1x3iCv5o1efUGVVoBTRZvOG9oNQuIA/S5ZF0U
oAvhoTW2jADHhDs7AgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQD
AgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4y
LjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBAAmNfvzl
89lE2FZilK9ho19HA0mGUi3E2uiwx5BqFqk25Aoidf7GGwWg3QyXJYD4krqvy33n
9VD751EG8IolSUmjR2dG/KS5T7dxNC0CVWzImBIauL9lkxzKBO5r+bmzEOogXzU5
3GPHnRGjXtEpzrOgJiXV2co4VMiv0JI2JJAIAd4CKDu2hhleTrc1d1ArOOCWwl+Z
OOmmp3bBrn18ROLxwqS02nLaG0xLeBePlUBuI15qMxr8URy5Zixnoqbv45lZAExV
ax3IUTBFICHSs1ZKtaq7WFpIH0VhA0dMNEJESYbAeG91sSWpcAhSbIoHu4q0lNa7
nlg6NG2HrjlvS3E=
</dsig:X509Certificate>
          <dsig:X509IssuerSerial>
            <dsig:X509IssuerName>O=getaCert - www.getacert.com, L=Seattle, ST=Washington, C=US</dsig:X509IssuerName>
            <dsig:X509SerialNumber>3745</dsig:X509SerialNumber>
          </dsig:X509IssuerSerial>
          <dsig:X509SubjectName>CN=www.r1uatesting.com, OU=IT, O=MyCompany, L=Boston, C=US</dsig:X509SubjectName>
        </dsig:X509Data>
      </dsig:KeyInfo>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-1_5"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes192-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes128-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes192-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes256-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#tripledes-cbc"/>
    </md:KeyDescriptor>
    <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://<domainURL>/fed/v1/idp/slo" ResponseLocation="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/idp/slo"/>
    <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<domainURL>/fed/v1/idp/slo" ResponseLocation="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/idp/slo"/>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://<domainURL>/fed/v1/idp/sso"/>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<domainURL>/fed/v1/idp/sso"/>
  </md:IDPSSODescriptor>
  <md:SPSSODescriptor AuthnRequestsSigned="true" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      <dsig:KeyInfo>
        <dsig:X509Data>
          <dsig:X509Certificate>MIIDlzCCAn+gAwIBAgICDqEwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMx
EzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoT
G2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MjgxNzIyNTFaFw0y
NDA3MjcxNzIyNTFaMF0xCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQ
BgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxHDAaBgNVBAMME3d3dy5yMXVh
dGVzdGluZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCY9/PV
uAW5KsmuWu4MHmHhLiiqggV10SGZhF/eqEPeo6mwudkBh1+oOWamCiDucKh6eZqQ
pluhz2QA5yTfJGHrwv+S+YEp7ji5E7wAT/BCTl9dffxuBsjtUrhhVDiZG08KxKA+
DG5P4bVXVv41chX5fULYUpDg75GfE6CTSkniCNYUIC84yi+XKqifqi4Eh0vDaXBR
LLu9EI8n+vx6zYF/5nH4r03TOivsJoVsOQpbf3TYVMifaY9S/Sg1WnBRK4Jqwdk6
K4e8vHpEMUhjtFHrBiJ/5DaEIbv1x3iCv5o1efUGVVoBTRZvOG9oNQuIA/S5ZF0U
oAvhoTW2jADHhDs7AgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQD
AgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4y
LjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBAAmNfvzl
89lE2FZilK9ho19HA0mGUi3E2uiwx5BqFqk25Aoidf7GGwWg3QyXJYD4krqvy33n
9VD751EG8IolSUmjR2dG/KS5T7dxNC0CVWzImBIauL9lkxzKBO5r+bmzEOogXzU5
3GPHnRGjXtEpzrOgJiXV2co4VMiv0JI2JJAIAd4CKDu2hhleTrc1d1ArOOCWwl+Z
OOmmp3bBrn18ROLxwqS02nLaG0xLeBePlUBuI15qMxr8URy5Zixnoqbv45lZAExV
ax3IUTBFICHSs1ZKtaq7WFpIH0VhA0dMNEJESYbAeG91sSWpcAhSbIoHu4q0lNa7
nlg6NG2HrjlvS3E=
</dsig:X509Certificate>
          <dsig:X509IssuerSerial>
            <dsig:X509IssuerName>O=getaCert - www.getacert.com, L=Seattle, ST=Washington, C=US</dsig:X509IssuerName>
            <dsig:X509SerialNumber>3745</dsig:X509SerialNumber>
          </dsig:X509IssuerSerial>
          <dsig:X509SubjectName>CN=www.r1uatesting.com, OU=IT, O=MyCompany, L=Boston, C=US</dsig:X509SubjectName>
        </dsig:X509Data>
      </dsig:KeyInfo>
    </md:KeyDescriptor>
    <md:KeyDescriptor use="encryption">
      <dsig:KeyInfo>
        <dsig:X509Data>
          <dsig:X509Certificate>MIIDlzCCAn+gAwIBAgICDqEwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UEBhMCVVMx
EzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1NlYXR0bGUxJDAiBgNVBAoT
G2dldGFDZXJ0IC0gd3d3LmdldGFjZXJ0LmNvbTAeFw0yNDA1MjgxNzIyNTFaFw0y
NDA3MjcxNzIyNTFaMF0xCzAJBgNVBAYTAlVTMQ8wDQYDVQQHDAZCb3N0b24xEjAQ
BgNVBAoMCU15Q29tcGFueTELMAkGA1UECwwCSVQxHDAaBgNVBAMME3d3dy5yMXVh
dGVzdGluZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCY9/PV
uAW5KsmuWu4MHmHhLiiqggV10SGZhF/eqEPeo6mwudkBh1+oOWamCiDucKh6eZqQ
pluhz2QA5yTfJGHrwv+S+YEp7ji5E7wAT/BCTl9dffxuBsjtUrhhVDiZG08KxKA+
DG5P4bVXVv41chX5fULYUpDg75GfE6CTSkniCNYUIC84yi+XKqifqi4Eh0vDaXBR
LLu9EI8n+vx6zYF/5nH4r03TOivsJoVsOQpbf3TYVMifaY9S/Sg1WnBRK4Jqwdk6
K4e8vHpEMUhjtFHrBiJ/5DaEIbv1x3iCv5o1efUGVVoBTRZvOG9oNQuIA/S5ZF0U
oAvhoTW2jADHhDs7AgMBAAGjZDBiMAkGA1UdEwQCMAAwEQYJYIZIAYb4QgEBBAQD
AgTwMAsGA1UdDwQEAwIFIDA1BgNVHREELjAsggpvcmFjbGUuY29tggkxOTIuMC4y
LjGCE3Rlc3QuYnlvY0BnbWFpbC5jb20wDQYJKoZIhvcNAQELBQADggEBAAmNfvzl
89lE2FZilK9ho19HA0mGUi3E2uiwx5BqFqk25Aoidf7GGwWg3QyXJYD4krqvy33n
9VD751EG8IolSUmjR2dG/KS5T7dxNC0CVWzImBIauL9lkxzKBO5r+bmzEOogXzU5
3GPHnRGjXtEpzrOgJiXV2co4VMiv0JI2JJAIAd4CKDu2hhleTrc1d1ArOOCWwl+Z
OOmmp3bBrn18ROLxwqS02nLaG0xLeBePlUBuI15qMxr8URy5Zixnoqbv45lZAExV
ax3IUTBFICHSs1ZKtaq7WFpIH0VhA0dMNEJESYbAeG91sSWpcAhSbIoHu4q0lNa7
nlg6NG2HrjlvS3E=
</dsig:X509Certificate>
          <dsig:X509IssuerSerial>
            <dsig:X509IssuerName>O=getaCert - www.getacert.com, L=Seattle, ST=Washington, C=US</dsig:X509IssuerName>
            <dsig:X509SerialNumber>3745</dsig:X509SerialNumber>
          </dsig:X509IssuerSerial>
          <dsig:X509SubjectName>CN=www.r1uatesting.com, OU=IT, O=MyCompany, L=Boston, C=US</dsig:X509SubjectName>
        </dsig:X509Data>
      </dsig:KeyInfo>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-1_5"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes192-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes128-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes192-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes256-gcm"/>
      <md:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#tripledes-cbc"/>
    </md:KeyDescriptor>
    <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo" ResponseLocation="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo"/>
    <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo" ResponseLocation="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo"/>
    <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/sso" index="1" isDefault="true"/>
  </md:SPSSODescriptor>
</md:EntityDescriptor>
```

## 6: Setting Up SAML SSO 🔗 
Use the following to create a SAML application or a SAML Identity Provider:
  * [Adding a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-saml-application.htm#add-saml-application "Create a Security Assertion Markup Language \(SAML\) application and grant it to users so that your users can single sign-on \(SSO\) into your SaaS applications that support SAML for SSO.")
  * [Adding a SAML Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-saml-identity-provider.htm#add-saml-identity-provider-console "Entering the SAML details for an identity provider.")


**Note**
  * While setting up the SAML SSO between SP and IdP, use the identity domain SAML metadata generated from earlier. Don't download the SAML metadata using the download button from the Console.
  * Upload the partner application custom certificate issued by the preferred CA. Don't download the custom certificate from the Console.


## 7: PATCH the SAML Service Provider Application and Identity Provider (Optional) 🔗 
If the identity domain is an IdP, then update the SAML application created in the Identity Domain. For more details on this, please see [Update an Application](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-apps-id-patch.html) from an API. To add a SAML Partner Certificate to a Service Provider Application in an Identity Domain, make the HTTP PATCH request to this API endpoint. 
`https://idcs-<identity-domain-url>/admin/v1/Apps/<sp-application-guid>`
  * Update "useSamlPartnerCertificate" and "samlPartnerCertificateId" properties.
Sample request:```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "replace",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:samlServiceProvider:App:useSamlPartnerCertificate",
   "value": true
  },
  {
   "op": "replace",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:samlServiceProvider:App:samlPartnerCertificateId",
   "value": "deb8e9ad7a41111ea1cbe060ecbed55c"
  }
 ]
}
```

Expected response:```
{
  "urn:ietf:params:scim:schemas:oracle:idcs:extension:samlServiceProvider:App": {
    "partnerProviderId": "https://<domain_id>.identity.oci.oracleiaas.com:443/fed",
    "assertionConsumerUrl": "https://<domain_id>.identity.oci.oracleiaas.com:443/fed/v1/sp/sso",
    "logoutRequestUrl": "https://<domain_id>.identity.oci.oracleiaas.com:443/fed/v1/sp/slo",
    "logoutResponseUrl": "https://<domain_id>.identity.oci.oracleiaas.com:443/fed/v1/sp/slo",
    "nameIdFormat": "saml-emailaddress",
    "nameIdUserstoreAttribute": "emails.primary.value",
    "signingCertificate": "Q2VydGlmaWNhdGU6CiAgICBEYa...",
    "encryptAssertion": false,
    "includeSigningCertInSignature": true,
    "logoutEnabled": true,
    "logoutBinding": "Redirect",
    "signResponseOrAssertion": "AssertionAndResponse",
    "signatureHashAlgorithm": "SHA-256",
    "federationProtocol": "SAML2.0",
    "hokRequired": false,
    "useSamlPartnerCertificate": true,
    "samlPartnerCertificateId": "deb8e9ad7a48414ea1cbe060ecbed55c",
    .
    .
    .
  },
  "displayName": "saml-app-with-customCert",
  "showInMyApps": false,
  .
  .
  .
}
```

  * PATCH the Identity Provider
If IDCS is SP, then please update the SAML Identity Provider created in the IDCS Identity Domain. 
To add a Saml Partner Certificate to an Identity Provider Application in an Identity Domain, make the HTTP PATCH request to this API endpoint. ```
https://idcs-<identity-domain-url>/admin/v1/IdentityProviders/<idp-guid>
```

Update `useSamlPartnerCertificate` and `samlPartnerCertificateId` properties:```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "replace",
   "path": "useSamlPartnerCertificate",
   "value": true
  },
  {
   "op": "replace",
   "path": "samlPartnerCertificateId",
   "value": "deb8e9ad7a41111ea1cbe060ecbed55c"
  }
 ]
}
```

Expected response:```
{
  "samlPartnerCertificateId": "deb8e9ad7a48414ea1cbe060ecbed55c",
  "type": "SAML",
  "logoutRequestUrl": "https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo",
  "id": "926f41972ac04a58846375048f788b39",
  "idpSsoUrl": "https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/idp/sso",,
  "encryptionCertificate": "MIIDlzCCAn+gAwIBAgICDqEwD...",
  "jitUserProvCreateUserEnabled": false,
  "jitUserProvGroupAssignmentMethod": "Overwrite",
  "enabled": true,
  "jitUserProvEnabled": false,
  "includeSigningCertInSignature": true,
  "logoutBinding": "Post",
  "jitUserProvAttributeUpdateEnabled": false,
  "authnRequestBinding": "Post",
  "nameIdFormat": "saml-emailaddress",
  "logoutResponseUrl": "https://<domain_id>.identity.oci.oracleiaas.com/fed/v1/sp/slo",
  "partnerProviderId": "https://<domain_id>.identity.oci.oracleiaas.com:443/fed",
  "description": "saml-idp-with-post-customcert",
  "signatureHashAlgorithm": "SHA-256",
  "useSamlPartnerCertificate": true,
  "ocid": "ocid1.domainidentityprovider.region1.sea.amaaaaaanbv3uaqany7gxeoes6ehtgc6c5nt7itxyc5qurhtvieeos2lz7sq",
  "signingCertificate": "MIIDlzCCAn+gAwIBAgICD...",
  "schemas": [
    "urn:ietf:params:scim:schemas:oracle:idcs:IdentityProvider"
  ],
  "domainOcid": "ocid1.domain.region1..aaaaaaaaki5nnhngcf7k636efwrdleiuktokcxphf5pzzt3okjilfibrz2na",
  "compartmentOcid": "ocid1.tenancy.region1..aaaaaaaakucifbpnl253kl2mk2unu5zu4grq3c725vvkxwvlkd6h243k7smq",
  "tenancyOcid": "ocid1.tenancy.region1..aaaaaaaakucifbpnl253kl2mk2unu5zu4grq3c725vvkxwvlkd6h243k7smq",
  "userMappingMethod": "NameIDToUserAttribute",
  "userMappingStoreAttribute": "emails.primary"
  .
  .
  .
}
```



Was this article helpful?
YesNo

