Updated 2025-01-14
# Defining Attribute Mappings for an AD Bridge
When you create an AD bridge, attribute mappings are defined between Microsoft Active Directory and IAM. Attribute mappings enable the AD bridge to pass values associated with user accounts between Microsoft Active Directory and IAM.
You can map attributes in two different ways: inbound and outbound. Inbound mappings allow you to map attributes from Microsoft Active Directory to IAM. Outbound mappings allow you to map any changes in IAM attributes to Microsoft Active Directory attributes.
For example, when you run the Microsoft Active Directory bridge, the bridge can use the `givenName - First Name` mapping to transfer the first name of the user account from the **First name** field on the **General** tab of the **Properties** window of Microsoft Active Directory to the **First Name** field on the **Details** tab of the **Users** page of IAM. Similarly, you can perform an outbound mapping so that when you make any change to the first name of the user account in IAM, this change is reflected in Microsoft Active Directory.
In addition to the predefined attribute mappings, you can define custom attribute mappings between Microsoft Active Directory and IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the AD bridge for which you want to define custom attribute mappings.
  4. Select **Configuration.**
  5. In the **Configure Attribute Mappings** area, select **Edit Attribute Mappings**. In the **Edit Attribute Mappings** window, two tabs appear: 
     * **Microsoft Active Directory to Identity cloud:** This tab contains inbound attribute mappings from Microsoft Active Directory to IAM.
     * **Identity cloud to Microsoft Active Directory:** This tab contains outbound attribute mappings from IAM to Microsoft Active Directory.
  6. To define inbound attribute mappings, then select the **Microsoft Active Directory to Identity cloud** tab. Otherwise, go to step 9.
You'll see predefined inbound mappings from Microsoft Active Directory to IAM. These mappings include:
List of predefined attributes | Required | Description  
---|---|---  
sAMAccountName | Yes | The user's user name.  
givenName | No | The user's first name.  
sn | Yes | The user's last name.  
middleName | No | The user's middle name.  
displayName | No | The user's display name.  
title | No | The user's job title.  
preferredlanguage | No | The user's preferred language (for example, English).  
localeID | No | The user's language and region (locale).  
mail | Yes | The user's email address.  
telephonenumber | No | The user's telephone number.  
homePhone | No | The user's home telephone number.  
mobile | No | The user's mobile telephone number.  
postalAddress | No | The user's postal address.  
streetAddress | No | The user's street address.  
l | No | The user's work location.  
st | No | The state of the user's work address.  
postalCode | No | The zip code of the user's work address.  
c | No | The country of the user's work address.  
usercertificate | No | This multi-valued attribute contains the DER-encoded X509v3 certificates issued to the user.  
userAccountControl | Yes | Specifies flags that control behavior for the user, such as whether the user has an **Active** or **Inactive** status, or whether the user's account is locked.  
  7. Select **Add Row** because you want to define an inbound attribute mapping from Microsoft Active Directory to IAM.
  8. In the **Directory User Attributes** column, select the name of the Microsoft Active Directory attribute that contains a value which you want to transfer into IAM. If the attribute id isn't available in the drop-down list, you can enter the new attribute name. After you save the changes, this new attribute appears in the drop-down list.
  9. In the IAM User Attributes column, enter or select the name of the IAM attribute that contains the value transferred from Microsoft Active Directory.
  10. If you want to define outbound attribute mappings, then select the **Identity cloud to Microsoft Active Directory** tab. Otherwise, go to step 13.
You'll see predefined outbound mappings from IAM to Microsoft Active Directory. These mappings include:
List of predefined attributes | Required | Description  
---|---|---  
User Name | No | The user's user name.  
Display Name | No | The user's display name.  
Work Email | No | The user's work-related email address.  
First name | No | The user's first name.  
Last name | No | The user's last name.  
Middle name | No | The user's middle name.  
Title | No | The user's job title.  
Locale | No | The user's language and region (locale  
Preferred Language | No | The user's preferred language (for example, English).  
Work Phone number | No | The user's work-related telephone number.  
Mobile Phone number | No | The user's mobile telephone number.  
Work Address Formatted | No | The user's work-related postal address.  
Work Street Address | No | The user's street address.  
Work Locality | No | The user's work location.  
Work Address Region | No | The state or region of the user's work address.  
Work Address Zip Code | No | The zip code of the user's work address.  
Work Address Country | No | The country of the user's work address.  
Home Phone number | No | The user's home telephone number.  
  11. Select **Add Row** because you want to define an outbound attribute mapping from IAM to Microsoft Active Directory.
  12. In the IAM User Attributes column, enter or select the name of the IAM attribute that contains a value which you want to transfer into Microsoft Active Directory.
  13. In the Directory User Attributes column, enter or select the name of the Microsoft Active Directory attribute to contain the value transferred from IAM.
  14. Select **Save**.


Was this article helpful?
YesNo

