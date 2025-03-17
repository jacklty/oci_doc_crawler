Updated 2025-01-14
# Editing a Custom Schema Attribute
After you create a custom attribute for the user schema for IAM, you might need to change its settings. For example, you might need to adjust the description or the minimum and maximum length.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Schema management**.
  5. Select **User attributes**.
  6. In the **Filter attribute** field, select **Custom**.
  7. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the custom attribute that you want to edit and select **Edit attribute**.
  8. You can edit the values for the following fields: **Display name** , **Description** , **Minimum length** , **Maximum length** , and End-user permissions. For more information about these fields, see [Creating a Custom Schema Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/add-custom-schema-attributes.htm#add-custom-schema-attributes "If you're creating your own user interface for IAM and you don't find a schema attribute that you need from the list of base schema attributes, create one and extend it to the existing schema.").
**Note** You can't increase the value of the **Minimum length** field or decrease the value of the **Maximum length** field. Also, if the value of the **Maximum length** field was set to below 40 when the custom schema attribute was added, then you can't increase it above 40. However, if the value was set to above 40, then you can increase the maximum length to 4,000.
  9. Select **Save changes**.


Was this article helpful?
YesNo

