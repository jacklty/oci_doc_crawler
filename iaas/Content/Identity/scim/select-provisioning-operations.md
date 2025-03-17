Updated 2025-01-14
# Selecting Provisioning Operations
Select the provisioning operations supported by an application's SCIM REST APIs in an OCI IAM identity domain.
  1. Select **Edit Provisioning** on your application page, scroll to the **Select Provisioning Operations** section.
  2. Select the following operations:
     * Authoritative Sync: If you enable this operation, then your application becomes an authoritative source for IAM. Users in the application are synchronized into IAM. If you select this operation, then the other provisioning operations are deactivated.
     * Create Account: If a user is assigned to your application in IAM, then an account is created for the user in the application.
     * Update Account: If an administrator edits the values of the provisioning form for a user who is assigned to your application, then these changes are propagated to the application.
     * De-activate Account: If an administrator activates or deactivates a user who is assigned to your application, then this change is propagated to the application.
     * Delete Account: If a user is removed from your application in the identity domain, then the user's account is removed from the application.


Was this article helpful?
YesNo

