Updated 2025-01-14
# Importing Users into Applications
You can perform a full sync import of the users of third-party Cloud applications using a flat file. In a full sync import, the imported user in the CSV file replaces any existing user who is already assigned to the application.
  1. Create a CSV file for import in the following format or download the CSV file along with user data from the target system apps:
```
ID, NAME, ACTIVE
hercule.poirot@sampleapp.com,hercule.poirot@sampleapp.com,true
```

This table provides a description of the attributes in the CSV format file:
**Attribute Name** |  **Description** |  **Sample Value**  
---|---|---  
**ID** |  The unique identifier of the account in the target. |  hercule.poirot@sampleapp.com  
**NAME** |  The name of the account. NAME is the primary input that is matched with the username of a particular user in IAM>. |  hercule.poirot@sampleapp.com  
**ACTIVE** |  The status of the account on the target. The possible values are `true` and `false`. If the value is `true`, the user account is imported and activated. If the value is `false`, the user is imported in a deactivated state. |  true  
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that in which you want to import users.
  4. Select **Import**.
  5. Browse for the CSV file, and import it.
**Note** Import from CSV file is enabled for applications that support flat file synchronization.
  6. Refresh the page to view the import result. If the import succeeds, then the users present in the CSV file displays.
  7. Select **Users** to view the imported users.
**Note** Refresh the **Users** tab to view the imported users.
  8. Observe that the users with a `true` value for **ACTIVE** attribute are activated. However, if a user account has `false` value for **ACTIVE** attribute, the user account is imported in a deactivated state.
**Note** The **Users** tab displays only the matched and confirmed users.
  9. Synchronize the imported users. See [Synchronizing Imported User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/synchronize-imported-user-accounts.htm#synchronize-imported-user-accounts "After you import the users, if a matching user account doesn't exist in the identity domain, you can either assign the user account to an existing user or create a new user for the user account.") to synchronize the imported user accounts with the users in an identity domain.


Was this article helpful?
YesNo

