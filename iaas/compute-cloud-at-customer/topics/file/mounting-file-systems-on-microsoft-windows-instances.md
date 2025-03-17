Updated 2025-02-05
# Mounting File Systems on Microsoft Windows Instances
On Compute Cloud@Customer, you can make file systems available to Microsoft Windows instances by mapping a network drive to the mount target IP address and export path provided by the File Storage service. You can accomplish this task using NFS or SMB protocols.
**Prerequisite**
Using the SMB protocol requires that the Microsoft Windows instances and Compute Cloud@Customer belong to the same Active Directory domain. Before performing any tasks in this section, ensure the following requirements are set up:
  * Installed and configured Microsoft Active Directory Federation Services for your organization.
  * Set up groups in Active Directory that will map to groups in Compute Cloud@Customer.
  * Created users in Active Directory who will sign in to the Compute Cloud@Customer Console.
**Note**
Consider naming Active Directory groups that you intend to map to Compute Cloud@Customer groups with a common prefix to make it easy to apply a filter rule, for example, `CCC_Administrators`, `CCC_NetworkAdmins`,` CCC_InstanceLaunchers`.
  * Open an Oracle support request to request an Active Directory configuration in the Compute Cloud@Customer Infrastructure. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).


Was this article helpful?
YesNo

