Updated 2025-01-14
# Adding an X.509 Authenticated Identity Provider
Use an X.509 authenticated identity provider (IdP) with certificate-based authentication with an identity domain in IAM to comply with FedRAMP requirements and Personal Identity Verification (PIV) cards.
Adding an X.509 authenticated IdP provides users a method to sign in using two-way SSL. Two-way SSL ensures that both the client and the server authenticate each other by sharing their public certificates, and then verification is performed based on those certificates.
To add an X.509 authenticated identity provider:
  1. Navigate to the identity domain: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Select **Add IdP** , and then select **Add X.509 IdP**.
  4. Enter a name and description for the X.509 identity provider.
  5. (Optional) Select **Enable EKU Validation** if you need to enable EKU validation as part of an X.509 identity provider.
The IAM supports the following EKU values:
     * SERVER_AUTH
     * CLIENT_AUTH
     * CODE_SIGNING
     * EMAIL_PROTECTION
     * TIME_STAMPING
     * OCSP_SIGNING
  6. Configure the Trusted certificate chain. 
    1. Select **Import Certificate** , and then attach a trusted certificate.
    2. To preserve the certificate file name, select **Keep the file name same as the original file**.
    3. Select **Import certificate**.
    4. Repeat to add all the certificates that form the trusted certificate chain.
The Trusted certificate chain is used to authenticate the X509 sign-in request. During authentication the user cert is validated to check if its certificate chain leads to any of the configured trusted certificates.
  7. (Optional) To preserve the certificate file name, select the checkbox **Keep the file name same as the original file**.
  8. (Optional) To identify the certificate keystore with an alias, enter a name for the certificate in the **Alias** box. Avoid entering confidential information
  9. Select **Import certificate**.
  10. Under **Certificate attribute** , select a method for matching identity domain user attributes to certificate attributes.
     * **Default:** Use this option to associate the identity domain user attributes to certificate attributes.
     * **Simple filter:** Use this option to select an identity domain user attribute to associate it to a certificate attribute.
     * **Advanced filter:** Use this option to create a custom filter to associate the identity domain user attributes with certificate attributes. For example:```
userName eq "$(assertion.fed.subject.cn)"
emails[primary eq true].value co "$(serialNumber)"
name.givenName eq "$(assertion.fed.subject.cn)@$(assertion.fed.serialNumber)"
username eq "$(assertion.fed.subject.cn)" or emails[primary eq true].value sw "$(assertion.fed.serialNumber)"
```

  11. (Optional) Enable and configure OCSP validation.
    1. Check **Enable OCSP validation** to enable the Online Certificate Status Protocol certificate validation during authentication.
    2. Configure the OCSP signing certificate. Import the OCSP responder certificate. This certificate is used to verify the signature on OCSP response. If the signature verification using this certificate fails then the OCSP responder's certificate chain leads to one of the configured trusted certificates (Delegated Trust Model). If not then OCSP response will be considered as UNKNOWN. 
    3. Enter OCSP responder URL. During authentication the OCSP validation request is sent to this URL only if the Users certificate doesn't have the OCSP URL configured. If the User's certificate has the OCSP URL configured that are used.
    4. To enable access for Unknown certificates, select the **Allow access if OSCP response is unknown**. When set to `true`, authentication succeeds when the OCSP response is `Unknown`. The following are potential OCSP responses.
       * **GOOD** : The OCSP responder has verified that the user certificate is present and not revoked.
       * **REVOKED** : The OCSP responder has verified that the user certificate is present and is REVOKED.
       * **UNKNOWN** : The OCSP response can be UNKNOWN because of any of the following reasons:
         * The OSCP server doesn't recognize the certificate.
         * The OCSP server doesn't know if the certificate is revoked 
  12. Select **Add IdP**.
  13. (Optional) Activate the IdP before adding it to any policies. For more information, see [Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm#activate-identity-provider "Activate or deactivate an identity provider \(IdP\) for an identity domain in IAM.").


Was this article helpful?
YesNo

