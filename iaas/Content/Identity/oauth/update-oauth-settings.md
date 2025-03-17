Updated 2025-01-14
# Updating an OAuth Setting
Configure the default token issuance policy in an identity domain in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **OAuth**.
  5. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **OAuth**.
  6. Under **Default token issuance policy** , select **Allow all resources**.
This setting allows the client to access any resource within the tenant regardless of the trust scope settings at the application level.
  7. (Optional) In the **Issuer** field, enter a custom issuer value. This issuer value is used in the newly issued tokens.
If you don't specify a custom issuer, the default IDCS issuer is used:```
https://identity.oraclecloud.com/
```

**Caution**
Only one previous issuer value is stored. If you make frequent changes in the issuer value, the old token validation might fail.
After changing the issuer value at the domain level, the issuer might be different on the client side based on the tenancy configuration. Validate the issuer value logic on the client side to use the new issuer value.
  8. Select **Save changes**.


Was this article helpful?
YesNo

