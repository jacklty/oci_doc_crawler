Updated 2024-07-04
# Setting Up a Microsoft Active Directory Bridge
The Microsoft Active Directory (AD) bridge provides a link between a Microsoft Active Directory enterprise directory structure and IAM.
**Note** The AD Bridge is only needed if you have a Windows Domain controller on premises and **do not** have Entra ID (formerly known as Azure AD). If you are using Entra ID you can setup synchronization directly from Azure to OCI IAM without installing any software. See the guidance in the [OCI IAM with Microsoft Entra ID Tutorials](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/azure_ad_tutorials.htm#tutorials-azure-overview "This set of tutorials provides step-by-step instructions to get you working with Microsoft Entra ID \(formerly Azure AD\) and OCI IAM.").
## Understand the AD Bridge 🔗 
IAM can synchronize with this directory structure so that any new, updated, or deleted user or group records are transferred into IAM. Each minute, the AD bridge polls Microsoft Active Directory for any changes to these records and brings these changes into IAM. So, if a user is deleted in Microsoft Active Directory, then this change is propagated into IAM. Because of this synchronization, the state of each record is synchronized between Microsoft Active Directory and IAM.
After users are synchronized from Microsoft Active Directory to IAM, if you activate or deactivate a user, modify the user's attribute values, or change the group memberships for the user in IAM, then these changes are propagated to Microsoft Active Directory through the bridge.
**Note** The Microsoft Active Directory organizational units (OUs) contain the users and groups that are imported into IAM.
You can configure IAM to synchronize with one or multiple Microsoft Active Directory domains by installing a bridge for each domain.
**Note** You must install the bridge on the machine that's attached to the Microsoft Active Directory domain for auto discovery. You don't have to install the bridge on the domain controller.
The following image shows inbound directory synchronization:
[![Inbound directory synchronization from Microsoft Active Directory to IAM by installing and configuring a bridge for each Microsoft Active Directory domain.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-bridge01.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-bridge01.png)
The following image shows outbound directory synchronization:
[![Outbound directory synchronization from IAM to Microsoft Active Directory for updates to a user's activation status, attribute values, or group memberships.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-outbound_directory_synchronization.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-outbound_directory_synchronization.png)
In the diagram above, Clarence Saladna (CSALADNA) is a user who's been synchronized from Microsoft Active Directory to IAM through the bridge. In IAM, an administrator deactivates Clarence's account because they're on vacation. Also, because Clarence received a promotion, they have a new job title of Director and belongs to different groups that are associated with their new role, including the Executive and Management groups. The bridge can be used to propagate these changes to Microsoft Active Directory.
Both the bridges and your Microsoft Active Directory enterprise directory structure are in your Microsoft Windows environment (for example, Microsoft Windows 2003). Because IAM is an Oracle Cloud Infrastructure service, it's in an Oracle environment.
The following image shows bridge security:
![The Internet connection that links each bridge to IAM contains a firewall.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-bridge02.png)
**Note** If an Microsoft Active Directory user attribute is multi valued, then the bridge transfers only the first value of the attribute into IAM.
## Why Use the AD Bridge 🔗 
Most customers have Microsoft Active Directory as their central directory service. These customers also use Microsoft Active Directory as their network directory. This directory is where all their workstations are connected to and from where they manage their users.
In addition to Microsoft Active Directory, customers use an enterprise LDAP to centralize all their user identities. So, a customer uses Microsoft Active Directory to manage their employees, but in the centralized LDAP, the customer manages their partners, consumers, and any other users with which the customer has relationships.
For these reasons, it's imperative that IAM can integrate with both Microsoft Active Directory and an enterprise LDAP (for example, Oracle Internet Directory).
By using IAM, customers can control when they migrate their directory-based applications to the cloud. In the interim, they can use one of the following: 
  * AD Bridge: This bridge provides a link between your Microsoft Active Directory enterprise directory structure and IAM. IAM can synchronize with this directory structure so that any new, updated, or deleted user or group records are transferred into IAM. Each minute, the bridge polls Microsoft Active Directory for any changes to these records and brings these changes into IAM. So, if a user is deleted in Microsoft Active Directory, then this change will be propagated into IAM. As a result, the state of each record is synchronized between Microsoft Active Directory and IAM. After the user is synchronized from Microsoft Active Directory to IAM, if you activate or deactivate a user, modify the user's attribute values, or change the group memberships for the user in IAM, then these changes are propagated to Microsoft Active Directory through the AD bridge.
  * Provisioning Bridge: This bridge provides a link between your enterprise LDAP (such as Oracle Internet Directory) and IAM. Through synchronization, account data that's created and updated directly on the LDAP is pulled into IAM and stored for the corresponding IAM users and groups. As a result, any changes to these records are transferred into IAM. Because of this, the state of each record is synchronized between the LDAP and IAM. See [Managing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/managing-provisioning-bridge.htm#understand-provisioning-bridge "The provisioning bridge provides a link between your on-premises apps and IAM. Through synchronization, account data that's created and updated directly on the apps is pulled into an identity domain and stored for the corresponding identity domain users and groups. As a result, any changes to these records are transferred into an identity domain. So, if a user is deleted in one of your apps, then this change is propagated into the identity domain. Because of this, the state of each record is synchronized between your apps and the identity domain.").


## Certified Components 🔗 
The following table lists the certified versions for IAM, Microsoft Active Directory, your operating system, and the Microsoft .NET software framework (which is required for the AD bridge to run).
IAM | AD  | 64–Bit | Operating System | .NET Framework  
---|---|---|---|---  
20.1.3 |  Microsoft Windows Server 2008 Microsoft Windows Server 2008 R2 Microsoft Windows Server 2012 Microsoft Windows Server 2012 R2 Microsoft Windows Server 2016 Microsoft Windows Server 2019 | Yes |  [Windows 10 v1607](https://docs.microsoft.com/en-us/windows/win32/secauthn/tls-cipher-suites-in-windows-10-v1607) or later Windows Server 2016 or later | Version 4.6+  
## Statuses 🔗 
The Microsoft Active Directory domain with which the AD bridge is communicating has two statuses:
  * Partially Configured: The AD bridge is installed, but it's not configured to communicate with either the Microsoft Active Directory domain or IAM.
  * Configured: The AD bridge is installed and configured, and available to synchronize with the Microsoft Active Directory domain.


The AD bridge has three statuses:
  * Active: The AD bridge is installed and configured, and available to synchronize with Microsoft Active Directory to retrieve user accounts and groups.
  * Inactive: The AD bridge is installed and configured, but it's not available to synchronize with Microsoft Active Directory. This is done for performance reasons.
  * Unreachable: The AD bridge is installed and configured. However, one of the following conditions has occurred: 
    * The backend service used to establish communication between IAM and Microsoft Active Directory is stopped.
    * The IAM administrator uninstalled the client associated with the AD bridge, but the bridge couldn't be removed from the **Directory Integrations** page of the IAM Console because the client can't connect to the server. IAM can't use the bridge to communicate with Microsoft Active Directory. See [Remove a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/remove-microsoft-active-directory-ad-bridge.htm#remove-microsoft-active-directory-ad-bridge "Remove an AD bridge from an IAM identity domain.").
    * The administrator regenerated the client secret for the AD bridge, and then uninstalled the client for the bridge.


## Hardware Requirements 🔗 
The minimum hardware requirements are:
  * 1 GB of RAM
  * 1 GB of disk space
  * A quad-core CPU


Was this article helpful?
YesNo

