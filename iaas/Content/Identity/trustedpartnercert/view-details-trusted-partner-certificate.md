Updated 2025-01-14
# Viewing Details About a Trusted Partner Certificate
View details of a trusted partner certificate for an identity domain in IAM.
You can see the alias, SHA-1 and SHA-256 thumbprints, start date, and end date for each certificate that you import into the identity domain. You can see either the abbreviated version of a certificate (the _thumbprint_) or the entire certificate.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Trusted partner certificates**.
  4. In the **Trusted Partner Certificates** page, verify that you see the following information about the imported trusted partner certificate:
     * **Alias** : The alias for the trusted partner certificate.
     * **SHA-1 thumbprint** : A hash value computed over the complete certificate, which contains all its fields, including the signature. If SHA-1 is used as the algorithm to encrypt the certificate, then the encrypted value appears in this column. Otherwise, the column is empty.
     * **SHA-256 thumbprint** : If SHA-256 is used as the algorithm to encrypt the certificate, then the encrypted value appears in this column. Otherwise, the column is empty.
     * **Certificate start date** : The date and time after which the identity domain can use the certificate to authenticate the trusted partner.
     * **Certificate end date** : The date and time after which the identity domain can no longer use the certificate to authenticate the trusted partner.
  5. To view the entire trusted partner certificate, as opposed to the certificate's thumbprint, select the certificate and then select **View**.


Was this article helpful?
YesNo

