Updated 2025-01-14
# Modifying an AD Bridge Between IAM and Microsoft Active Directory
Modify details of bridge between IAM and Microsoft Active Directory.
You can change the following items for a Microsoft Active Directory (AD) bridge:
  * The Microsoft Active Directory users and groups that you want IAM to import using the AD bridge.
  * Whether, after a user or group is synchronized from Microsoft Active Directory to IAM, if you activate or deactivate a user, modify the user's attribute values, or change the group memberships for the user in IAM, these changes are propagated to Microsoft Active Directory.
  * How often you want IAM to use the AD bridge to import users and groups from Microsoft Active Directory.
  * The predefined and custom attribute mappings defined between Microsoft Active Directory and IAM.
  * Whether users can use their Microsoft Active Directory or their IAM passwords, or their federated accounts, to sign in to IAM to access resources protected by IAM, such as the My Profile Console, IAM Console, and apps assigned to the users.


**Note**
You can upgrade the client for the AD bridge. By doing this, you can install the latest client without removing the existing client that's installed.
To upgrade the client, download it and follow the instructions in [Create a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/create-microsoft-active-directory-ad-bridge.htm#create-microsoft-active-directory-ad-bridge "Create a bridge between IAM and Microsoft Active Directory."). When you see the **Specify Oracle Identity Cloud Service Credentials** or the **Specify Microsoft Active Directory Credentials** dialog boxes, use the credentials you provided in the previous installation. For this reason, the values are unavailable to edit.
## Modifying an AD Bridge 🔗 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the bridge that you want to modify.
  4. To edit configuration information about the bridge, select **Configuration**.
    1. In the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes, select or clear checkboxes to enable or prevent IAM from importing users and groups using the bridge.
See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.") for more information about the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes.
    2. In the **Supported operations** area, select or clear checkboxes to enable or prevent IAM from propagating changes for a user's activation status, attribute values, or group memberships to To edit configuration information about the bridge.
See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.") for more information about the **Supportedoperations** area.
    3. In the **Set import frequency** area, change how often you want IAM to use the bridge to import users and groups from To edit configuration information about the bridge.
    4. In the **Configure attribute mappings** area, select **Edit attribute mappings**. The **Edit attribute mappings** window opens and two tabs appear:
       * **Microsoft Active Directory to Identity cloud:** In this tab, you can modify inbound attribute mappings from Microsoft Active Directory to IAM.
       * **Identity cloud to Microsoft Active Directory:** Use this tab to modify outbound attribute mappings from IAM to Microsoft Active Directory.
      1. Select the **Microsoft Active Directory to Identity cloud** or **Identity cloud to Microsoft Active Directory** tab.
      2. In the **Directory User Attributes** and IAM **User Attributes** columns, change the Microsoft Active Directory or IAM attribute used for the predefined or custom attribute mapping.
      3. To remove an attribute mapping, select the **X** button to the right of the mapping.
**Note** Inbound attribute mappings with asterisks in the **Microsoft Active Directory to Identity cloud** tab are required by the bridge to pass values associated with Microsoft Active Directory user accounts into IAM so that the accounts can be created in IAM. You can't delete these mappings.
      4. Select **Save** to close the **Edit Attribute Mappings** window.
See [Define Attribute Mappings for a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/define-custom-attribute-mappings-microsoft-active-directory-ad-bridge.htm#define-custom-attribute-mappings-microsoft-active-directory-ad-bridge "When you create an AD bridge, attribute mappings are defined between Microsoft Active Directory and IAM. Attribute mappings enable the AD bridge to pass values associated with user accounts between Microsoft Active Directory and IAM.") for more information about the Directory User Attributes and IAM User Attributes columns of the Microsoft Active Directory to IAM and IAM to **Microsoft Active Directory** tabs of the **Edit Attribute Mappings** window.
    5. In the **Authentication Settings** area, select the **Enable local authentication** option if you want users to use their IAM or their Microsoft Active Directory passwords to sign in to IAM to access IAM-protected resources.
If you select this option, then configure delegated authentication for the bridge. See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.").
If you select **Enable local authentication** , then select or clear **Don't send Welcome Notifications** to enable or prevent IAM from notifying users by email that they must activate the IAM accounts that are created for them.
Otherwise, select **Enable federated authentication** to have users use their federated accounts to sign in to IAM.
    6. Select **Save**.
    7. In the **Confirmation** window, select **OK**.
See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.") for more information about the areas of the **Configuration** tab.


Was this article helpful?
YesNo

