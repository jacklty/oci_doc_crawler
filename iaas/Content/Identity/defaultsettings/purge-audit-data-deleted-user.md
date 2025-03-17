Updated 2025-01-14
# Purging Audit Data for a Deleted User
When you delete a user from an identity domain in IAM, the audit data of the user remains in the system. You can manually and immediately purge the audit data of that deleted user.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Domain settings**.
  4. Under **Audit** , in the **Enter the OCID of the deleted user to purge audit data** text box, enter the OCID of the deleted user and select **Purge**.
All the audit data of that user is permanently deleted from the tenancy.


Was this article helpful?
YesNo

