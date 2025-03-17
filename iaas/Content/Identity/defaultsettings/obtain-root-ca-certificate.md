Updated 2025-01-14
# Getting the Root CA Certificate
When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.
cURL must be installed to perform this task. See  Follow this procedure to obtain the root certificate.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Domain settings**.
  4. Under **Access signing certificate** , select **Configure client access** to enable clients to access the tenant signing certificate without logging in to IAM. 
  5. Select **Save changes** and confirm the action to save the default settings.
  6. In the overview page for the identity domain overview, select **Copy** next to the **Domain URL** in Domain information.
  7. In a new browser tab, paste the URL you copied and add `/admin/v1/SigningCert/jwk` to the end of it. For example:
```
https://_<domain_url_/admin/v1/SigningCert/jwk
```

  8. Use the following URL as the endpoint and press **Enter**.
`https://_<yourtenancy>_.identity.oraclecloud.com/admin/v1/SigningCert/jwk`
When you **Enter** , a block of code is returned.
![The result of the cURL command, showing the content to use.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_root_certificate.png)
The section of code you want for the key is the block marked with `1:` on the left, and immediately above `key_ops`.
  9. Open a text editor and paste the key in the following manner:
`-----BEGIN CERTIFICATE----- [Paste the key here] -----END CERTIFICATE-----`
For example, (abbreviated):
` -----BEGIN CERTIFICATE----- "MIIDdDCCAlygAwIBAgIGAVw4Ns68MA0GCS......./VaWgoMQ6J9t9CLarai" -----END CERTIFICATE-----`
  10. Save this file with the suffix `.pem` as your root certification file.


Was this article helpful?
YesNo

