Updated 2025-01-14
# Viewing SAML Certificate Metadata
Allow clients to access the signing certificate for the identity domain in IAM without logging in to an identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Domain settings**.
  4. Under **Access signing certificate** , select **Configure client access** to enable clients to access the tenant signing certificate without signing in to IAM. 
If this option is cleared, clients can access the tenant signing certificate and the SAML metadata only after they authenticate by signing in to the identity domain.
  5. Select **Save changes**.
  6. In the overview page for the identity domain overview, select **Copy** next to the **Domain URL** in Domain information.
  7. In a new browser tab, paste the URL you copied and add ``/fed/v1/metadata`` to the end of it, and then press **Enter**. For example:
```
https://_<domain_url_/fed/v1/metadata
```



Was this article helpful?
YesNo

