Updated 2025-01-14
# Adding a Terms of Use Document
Add a terms of use document for a an identity domain in IAM. A terms of use document lets you present disclaimers and acceptable use policies to the users in an identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. On the domain details page, click **Security**.
  3. Under **Security** , select **Terms of use**.
  4. Select **Create terms of use document**.
  5. On the **Add terms of use document** page, provide the following information:
     * **Name** : Enter a name for the terms of use to easily identify it.
     * **Description** : Enter a description to help understand the purpose and usage of this terms of use.
     * **Consent acceptance expiration** : Enter the duration for which the terms of use consent is valid. The value can range between 1 and 365 days. If you don't want the consent to expire, select **Never expires**.
  6. Select **Add terms of use document** to proceed to the statements options.
  7. On the **Add terms of use statements** page, select **Add terms of use statement** and provide the following information:
     * **Language** : Select the language in which you want to create the statement for your terms of use. (You can create more terms of use statements in other languages later.)
     * **Statement** : Enter or paste the statement content.
  8. To save changes, select **Add terms of use statement**.
  9. Select **Next**.
  10. On the **Add apps** page, select **Add app** and then search for and select the applications that you want to assign to this terms of use.
  11. When you're ready, select **Add app** and the app is listed as an app associated with this terms of use.
  12. Select **Close**.

The terms of use document is added in the deactivated state. You must activate it before it's used by the applications in your identity domain.
Was this article helpful?
YesNo

