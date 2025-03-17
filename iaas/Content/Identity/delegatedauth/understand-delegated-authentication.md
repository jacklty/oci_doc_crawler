Updated 2025-01-14
# Managing Delegated Authentication
Use delegated authentication so that identity domain administrators and security administrators don't have to synchronize user passwords between an on-premises Microsoft Active Directory (AD) enterprise directory structure and IAM.
Users can use their AD passwords to sign in to their identity domain to access resources and applications protected by IAM.
Suppose you have an AD domain that contains user accounts that you want to import into identity domains. To transfer these accounts, install and configure an AD Bridge for the AD domain. The AD Bridge provides a link between the AD domain and IAM. IAM can synchronize with the AD domain so that any new, updated, or deleted user or group records are transferred into IAM. Because of this, the state of each record is synchronized between AD and IAM.
After using an AD Bridge to transfer user accounts from the AD domain into an Identity Domain, you want to configure the IAM so that users from the AD domain must use their AD passwords to sign in to OCI. To do this, activate delegated authentication for the AD Bridge. However, first, you might want to verify that the AD credentials from a user in the AD domain can be used to sign in to IAM. This way, if there are any issues, then you can resolve them before activating delegated authentication.
After you activate delegated authentication in IAM, if you change or reset a password in IAM, then the password is stored directly in AD. The AD password policies are applicable for the new password. Password policies configured in IAM aren't applicable for this password. IAM doesn't maintain the password.
## Statuses 🔗 
The status of connection between IAM and AD domains. There can be multiple bridges for an AD domain.
There are three statuses for an AD Bridge that IAM uses to communicate with an AD domain to delegate responsibilities for authenticating users of that domain into IAM: 
  * Connected: The AD Bridge is installed and configured, and can communicate with the domain.
  * No Clients Found: You installed or configured an AD Bridge without installing the client for the AD domain. Select **Select here to download the client** to download the client for the AD domain. Alternatively, the bridge was uninstalled.
  * Incompatible Client Found: You used an outdated version of the client to install or configure an AD Bridge. Select **Select here to download the client** to download the updated client for the AD domain.


Was this article helpful?
YesNo

