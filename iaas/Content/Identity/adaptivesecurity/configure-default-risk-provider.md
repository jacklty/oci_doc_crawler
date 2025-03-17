Updated 2025-01-14
# Updating the Default Risk Provider
Update the default risk provider for an identity domain in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Adaptive security**.
  3. Select the Actions menu in the **Default risk provider** row and then **Edit risk provider**. Change the description or risk range. To learn about risk ranges, see [Creating a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/add-third-party-risk-provider.htm#add-third-party-risk-provider "Create a risk provider for an identity domain in IAM that you can use to obtain a user's risk score from the Symantec third-party risk engine.").
  4. Select or clear a checkbox to enable or disable the event. You can't disable all events for the default risk provider.
**Note**
To set the maximum number of unsuccessful logins for the Too many unsuccessful login attempts event, see [Modifying the Custom Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/modify-custom-password-policy.htm#modify-custom-password-policy "Adjust the strength of the custom password policy in an identity domain in IAM to meet the business and security requirements for your enterprise applications.").
To set the maximum number of unsuccessful MFA logins for the Too many unsuccessful MFA attempts event, see [Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.").
  5. Set a value (Weighting) for each event that corresponds to the risk range for this risk provider.
For example, you can set the Low risk range for the risk provider to be 0-10, the Medium risk range to be 11-80, and the High risk range to be 81-100. 
If you set the weighting of the Access from an unknown device event to 20, and a low-risk user accesses an identity domain with an unknown device, the user's risk range changes to Medium.
  6. Select **Save changes**.
  7. Confirm the changes.


Was this article helpful?
YesNo

