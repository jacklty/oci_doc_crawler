Updated 2024-09-26
# Managing Provisioning Bridges
The provisioning bridge provides a link between your on-premises apps and IAM. Through synchronization, account data that's created and updated directly on the apps is pulled into an identity domain and stored for the corresponding identity domain users and groups. As a result, any changes to these records are transferred into an identity domain. So, if a user is deleted in one of your apps, then this change is propagated into the identity domain. Because of this, the state of each record is synchronized between your apps and the identity domain.
Suppose you're using an on-premises app such Oracle Internet Directory as an authoritative source for your company's users and groups. This app lies within your company's firewall. For a provisioning bridge to communicate with on-premises apps such as Oracle Internet Directory, it must use Identity Connector Framework (ICF) connectors to access the associated apps. As a result, the provisioning bridge can poll the on-premises apps for changes to users and groups in the apps, and synchronize these changes with the identity domain. You can configure a provisioning bridge so that IAM can synchronize users and groups from one or multiple apps.
The following image shows directory synchronization:
[![Oracle Internet Directory is an on-premises app that's the authoritative source for the users and groups. The provisioning bridges poll the Oracle Internet Directory domains for changes to the users and groups, and synchronize these changes with IAM](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-directory_synchronization.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-directory_synchronization.png)
Both the provisioning bridges and your on-premises apps are in your Microsoft Windows or generic environment. A generic environment consists of any machine that has Java 8 installed on it and supports Bash shell.
Each provisioning bridge uses a client network to access the on-premises apps with which you want to synchronize identity domain users and groups. Because IAM is in a different environment, a bridge is needed to span the networks.
The following image shows provisioning bridge security:P
[![The provisioning bridge and Oracle Internet Directory are in your environment. The identity domain is in a different environment, and a bridge spans them](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-provisioning_bridge_security.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-provisioning_bridge_security.png)
To manage provisioning bridges, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
## Statuses
A provisioning bridge client has two statuses:
  * Started: The provisioning bridge started successfully.
  * Stopped: The provisioning bridge stopped unexpectedly or the identity domain administrator or security administrator stopped it. See [Stop a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm#stop-provisioning-bridge "Stop a provisioning bridges in an OCI IAM identity domain.").


A provisioning bridge has two statuses:
  * Active: The provisioning bridge is installed, started, and activated. It's available to poll the apps to which the provisioning bridge is assigned for changes to users and groups in the apps, and synchronize these changes with the identity domain. See [Activate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/activate-provisioning-bridges.htm#activate-provisioning-bridges "You can activate a single provisioning bridge, or you can activate multiple provisioning bridges simultaneously.").
  * Inactive: The provisioning bridge is installed and configured, but it's deactivated. It's not available to retrieve users and groups from the apps to which the provisioning bridge is assigned. For performance reasons, this is done. See [Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm#deactivate-provisioning-bridges "You can deactivate a single provisioning bridge, or you can deactivate multiple provisioning bridges simultaneously.").


  * [Creating a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm#create-provisioning-bridge "Create a provisioning bridge in an identity domain to link your on-premises apps with IAM.")
  * [Starting a Provisioning Bridge on a Generic Machine](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-generic-machine.htm#start-provisioning-bridge-generic-machine "Start a provisioning bridges in an IAM identity domain on a generic machine.")
  * [Starting a Provisioning Bridge on a Windows Machine](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-windows-machine.htm#start-provisioning-bridge-windows-machine "Start a provisioning bridges in an IAM identity domain on a Windows machine.")
  * [Stopping a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm#stop-provisioning-bridge "Stop a provisioning bridges in an OCI IAM identity domain.")
  * [Activating Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/activate-provisioning-bridges.htm#activate-provisioning-bridges "You can activate a single provisioning bridge, or you can activate multiple provisioning bridges simultaneously.")
  * [Deactivating Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm#deactivate-provisioning-bridges "You can deactivate a single provisioning bridge, or you can deactivate multiple provisioning bridges simultaneously.")
  * [Viewing Details about a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/view-details-provisioning-bridge.htm#view-details-provisioning-bridge "View the details of a provisioning bridge in an IAM identity domain.")
  * [Modifying a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/modify-provisioning-bridge.htm#modify-provisioning-bridge "Modify the name, description, or client secret of a provisioning bridge in an IAM identity domain.")
  * [Assigning a Provisioning Bridge to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/assign-provisioning-bridge-apps.htm#assign-provisioning-bridge-apps "After creating a provisioning bridge for an identity domain in IAM, you can assign it to on-premises apps in the App Catalog. Because this bridge serves as a provisioning and synchronizing agent between the identity domain and your apps, the bridge can poll for changes to users or groups in the apps and synchronize those changes into the identity domain.")
  * [Changing the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm#change-provisioning-bridge-assigned-apps "Only one provisioning bridge can be assigned to an app at any time. If you want to assign another bridge to the app, then you must replace the bridge that's already associated with the app with the designated bridge.")
  * [Managing Log Files for a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/manage-log-files-provisioning-bridge.htm#manage-log-files-provisioning-bridge "After you install and start a provisioning bridge, you might want to access the log files for troubleshooting purposes. You can locate these files in the logs folder.")


Was this article helpful?
YesNo

