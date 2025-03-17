Updated 2025-01-14
# Importing a Trusted Partner Certificate
Import a trusted partner certificate to an identity domain in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Trusted partner certificates**.
  4. In the **Trusted Partner Certificates** page, select **Import certificate**.
  5. In the Import certificate dialog box, follow these steps:
    1. In the **Alias** field, enter an alias for the trusted partner certificate (for example, `TPcert1`).
The certificate that you import is an authorization certificate for the trusted partner. It contains a _keystore_. The keystore is used to authenticate and encrypt the data for the trusted partner for security purposes. A keystore entry is identified by an _alias_.
    2. Upload the Distinguished Encoding Rules (DER) file that contains the trusted partner certificate to import by dragging the file to the page or by selecting **select one** and browsing to its location.
    3. Verify that the path and name of the DER file you selected appear in the **Certificate** field.
    4. Select **Import**.


Was this article helpful?
YesNo

