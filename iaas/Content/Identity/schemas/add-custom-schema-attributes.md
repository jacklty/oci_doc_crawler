Updated 2025-01-14
# Creating a Custom Schema Attribute
If you're creating your own user interface for IAM and you don't find a schema attribute that you need from the list of base schema attributes, create one and extend it to the existing schema.
You can add attributes to the **User information** tab of the **Users** page of the Console and the **My profile details** of the **My profile** console.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Schema management**.
  5. In the **Schema management** page, select **User attributes**.
**Filter attribute** allows you to filter user attributes.
     * **All:** All user attributes are listed.
     * **Base:** The OCI user attributes are listed. Occasionally, you may want to edit one or more user attributes. If the attribute cannot be edited, the fields are not available to edit.
     * **Custom:** These are the user attributes which you have added.
  6. Select **Add attribute**.
**Important** After you create a custom schema attribute, if data exists for that attribute, then you can't remove it.
  7. In the **Add attribute** window, enter the following information:
     * **Display name:** The attribute name that appears in the **Schema management** page, the **User information** tab of the **Users** page of the Console, and the **My Profile details** tab of the **My profile** console.
     * **Name:** The attribute name that's recognized by the IAM server.
     * **Description:** Provide further information related to its usage and other details that help the user identify this attribute.
     * **Data type:** If the value for this attribute can contain alphanumeric characters, special characters, or spaces, then select **String** for the data type. If you want to create a multivalued attribute, then select **String array**.
     * **Minimum length:** Select the minimum length of the attribute value. The minimum value allowed is 1.
**Note** After you've created the custom attribute, you can't increase the minimum length later. You can only make it smaller. So, if you create the custom attribute with a minimum length of 20, you can't later increase it to 25.
     * **Maximum length:** Select the maximum length of the attribute value. The maximum value allowed is 4,000.
**Note** After you've created the custom attribute, you can't decrease the maximum length later. Also, if the value of the maximum length field is set to below 40 when the custom schema attribute is created, you can't increase it above 40. However, if the value is set to above 40, then you can increase the maximum length to 4,000.
     * **Searchable:** If this checkbox is selected, then the values for this attribute can be used in searches. If this checkbox isn't selected, then the values can't be used for searches.
     * **End-user permissions:** Select the permission that you want to set for this attribute. Because this is a user permission, and not an administrator one, it applies to an attribute that's associated with the **My Profile Details** tab of the **My profile** console only.
You can grant the following permissions:
       * **Hide:** The attribute won't appear in the **My Profile Details** tab of the **My profile** console.
       * **Set once:** The user can provide a value for the attribute and save it, and then afterward, this becomes a read-only attribute.
       * **Read-Only:** The user can see but can't modify the value associated with this attribute.
       * **Read-Write:** The user can see and modify the value associated with this attribute.
  8. Select **Add**.

The custom attribute is created.
**Tip** Open the custom attribute to find its fully qualified name (FQN).
Was this article helpful?
YesNo

