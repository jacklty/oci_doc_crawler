Updated 2024-06-06
# Details for Management Agent
This topic covers details for writing policies to control access to the Management Agent service.
## Resource-Types 🔗 
`management-agents`
`management-agent-install-keys`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
### management-agents 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  MGMT_AGENT_INSPECT |  ListManagementAgentPlugins ListManagementAgents ListWorkRequestErrors ListWorkRequestLogs ListWorkRequests |  none  
read |  INSPECT + MGMT_AGENT_READ |  INSPECT + GetManagementAgent GetWorkRequest |  none  
use |  READ + MGMT_AGENT_UPDATE |  READ + UpdateManagementAgent |  none  
manage |  USE + MGMT_AGENT_CREATE MGMT_AGENT_DELETE MGMT_AGENT_DEPLOY_PLUGIN_CREATE |  USE + DeleteManagementAgent DeployPlugins DeleteWorkRequest |  none  
### management-agent-install-keys 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  MGMT_AGENT_INSTALL_KEY_INSPECT |  ListManagementAgentInstallKeys |  none  
read |  INSPECT + MGMT_AGENT_INSTALL_KEY_READ |  INSPECT + GetManagementAgentInstallKey GetManagementAgentInstallKeyContent |  none  
use |  READ + MGMT_AGENT_INSTALL_KEY_UPDATE |  READ + UpdateManagementAgentInstallKey |  none  
manage |  USE + MGMT_AGENT_INSTALL_KEY_CREATE MGMT_AGENT_INSTALL_KEY_DELETE |  USE + CreateManagementAgentInstallKey DeleteManagementAgentInstallKey |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateManagementAgentInstallKey` | MGMT_AGENT_INSTALL_KEY_CREATE  
`DeleteManagementAgent` | MGMT_AGENT_DELETE  
`DeleteManagementAgentInstallKey` | MGMT_AGENT_INSTALL_KEY_DELETE  
`DeleteWorkRequest` | MGMT_AGENT_DELETE  
`DeployPlugins` | MGMT_AGENT_DEPLOY_PLUGIN_CREATE  
`GetManagementAgent` | MGMT_AGENT_READ  
`GetManagementAgentInstallKey` | MGMT_AGENT_INSTALL_KEY_READ  
`GetManagementAgentInstallKeyContent` | MGMT_AGENT_INSTALL_KEY_READ  
`GetWorkRequest` | MGMT_AGENT_READ  
`ListManagementAgentInstallKeys` | MGMT_AGENT_INSTALL_KEY_INSPECT  
`ListManagementAgentPlugins` | MGMT_AGENT_INSPECT  
`ListManagementAgents` | MGMT_AGENT_INSPECT  
`ListWorkRequestErrors` | MGMT_AGENT_INSPECT  
`ListWorkRequestLogs` | MGMT_AGENT_INSPECT  
`ListWorkRequests` | MGMT_AGENT_INSPECT  
`UpdateManagementAgent` | MGMT_AGENT_UPDATE  
`UpdateManagementAgentInstallKey` | MGMT_AGENT_INSTALL_KEY_UPDATE  
For more details and examples, see [Set Up Oracle Cloud Infrastructure for Management Agents](https://docs.oracle.com/iaas/management-agents/doc/perform-prerequisites-deploying-management-agents.html#OCIAG-GUID-EFD288F4-55C4-4DEF-900D-0DEAA24360A2).
Was this article helpful?
YesNo

