Updated 2025-01-14
# Setting the Audit Retention Period
Set the retention period for audit logs for an identity domain in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Domain settings**.
  4. Under Audit, select **Configure audit retention period** and then enter a value of 30, 60 or 90 (in days). The tenancy purges the audit data for all the users, based on the interval set here. 
**Note** As an administrator, when you delete a user, you can manually purge the audit data of that user by entering the user's OCID in **Enter the OCID of the deleted user to purge audit data** and then selecting **Purge**. All the audit data of that user is permanently deleted from the tenancy.
  5. Select **Save changes**.


Was this article helpful?
YesNo

