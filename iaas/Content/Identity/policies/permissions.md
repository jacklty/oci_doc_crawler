Updated 2024-10-03
# Permissions
_Permissions_ are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.
When you write a policy giving a group access to a particular [Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Verbs.htm#top "The verb element of a policy statement specifies the type of access. For example, use inspect to let third-party auditors list the specified resources.") verb and resource type, you're giving that group access to one or more predefined permissions. The purposes of verbs is to simplify the process of granting several related permissions that cover a broad set of access or a particular operational scenario. The next sections give more details and examples.
## Relation to Verbs 🔗 
To understand the relationship between permissions and verbs, let's look at an example. A policy statement that allows a group to `inspect volumes` actually gives the group access to a permission called VOLUME_INSPECT (permissions are always written with all capital letters and underscores). In general, that permission enables the user to get information about block volumes. 
As you go from `inspect` > `read` > `use` > `manage`, the level of access generally increases, and the permissions granted are cumulative. The following table shows the permissions included with each verb for the `volumes` resource-type. Notice that no additional permissions are granted going from `inspect` to `read`.
Inspect Volumes | Read Volumes | Use Volumes | Manage Volumes  
---|---|---|---  
VOLUME_INSPECT | VOLUME_INSPECT |  VOLUME_INSPECT VOLUME_UPDATE VOLUME_WRITE |  VOLUME_INSPECT VOLUME_UPDATE VOLUME_WRITE VOLUME_CREATE VOLUME_DELETE  
The [policy reference](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference.htm "Get an overview of IAM policy reference topics, including verbs, resources types, and general variables.") lists the permissions covered by each verb for each given resource-type. For example, for block volumes and other resources covered by the Core Services, see the tables in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-Details_for_Verb__ResourceType_Combinations.htm#Core "Core services details for verb and resource type combinations."). The left column of each of those tables lists the permissions covered by each verb. The other sections of the policy reference include the same kind of information for the other services.
## Relation to API Operations 🔗 
Each API operation requires the caller to have access to one or more permissions. For example, to use either `ListVolumes` or `GetVolume`, you must have access to a single permission: VOLUME_INSPECT. To attach a volume to an instance, you must have access to multiple permissions, some of which are related to the `volumes` resource-type, some to the `volume-attachments` resource-type, and some related to the `instances` resource-type:
  * VOLUME_WRITE
  * VOLUME_ATTACHMENT_CREATE
  * INSTANCE_ATTACH_VOLUME


The policy reference lists which permissions are required for each API operation. For example, for the Core Services API operations, see the table in [Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-Permissions_Required_for_Each_API_Operation.htm#Permissi "Core services permissions required for API operations."). 
## Understanding a User's Access 🔗 
The policy language is designed to let you write simple statements involving only verbs and resource-types, without having to state the desired permissions in the statement. However, there may be situations where a security team member or auditor wants to understand the specific permissions a particular user has. The tables in the [policy reference](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference.htm "Get an overview of IAM policy reference topics, including verbs, resources types, and general variables.") show each verb and the associated permissions. You can look at the groups the user is in and the policies applicable to those groups, and from there compile a list of the permissions granted. However, having a list of the permissions isn't the complete picture. Conditions in a policy statement can scope a user's access beyond individual permissions (see the next section). Also, each policy statement specifies a particular compartment and can have conditions that further scope the access to only certain resources in that compartment. 
Was this article helpful?
YesNo

