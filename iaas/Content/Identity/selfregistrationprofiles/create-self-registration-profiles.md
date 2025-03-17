Updated 2025-01-14
# Creating a Self-Registration Profile
Create self-registration profiles in IAM to manage self-registration for different sets of users, approval policies, and applications.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Self registration**.
  5. Select **Add profile**.
  6. Enter details about the self-registration profile.
    1. Enter a unique name for the profile.
    2. To require a user to accept the terms of use during self-registration, select **User consent required**. To hide the terms of use from the user during self-registration, deselect the option.
    3. To add groups to the profile, select **Assign** in the **Assign to group** section.
    4. Add the user's email domains allowed during the self-registration process in the **Allowed email domains** field. Enter all or leave this field blank to allow all email domains.
  7. Add design elements to the profile. Upload footer and header logos or keep the default logos.
  8. Complete the **Self-registration content** section.
     * Enter the registration page name that you want to appear as a link on your customized login page.
     * Add header, footer, and success text, or keep the default values.
     * If you have selected **User consent required** , enter the text in **User consent text**.
**Tip** To discard your changes and return to the **Manage self-registration profiles** page, select **Cancel**.
  9. Select **Add profile**.
The profile ID that you need for the self-registration link is created.
  10. On the **Self registration** page, activate the profile. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), choose **Activate**.
Next, [construct a self-registration URL](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/construct-self-registration-url.htm#create-self-registration-profiles "After creating a self-registration profile in IAM, you must create a self-registration URL.").


Was this article helpful?
YesNo

