Updated 2024-06-06
# Details for Container Registry
This topic covers details for writing policies to control access to Oracle Cloud Infrastructure Registry (also known as Container Registry).
## Resource-Types 🔗 
  * `repos`


Note that `repos` covers all Container Registry resources, namely repositories, images, and image signatures.
## Supported Variables 🔗 
Oracle Cloud Infrastructure Registry supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the ones listed here.
The `repos` resource-type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.repo.name` | String | Use this variable to control access to specific repositories. For an example policy, see [Policies to Control Repository Access](https://docs.oracle.com/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm).  
When authorizing an API operation to access a Container Registry resource using a tag specified by the `target.resource.tag` policy variable, you must apply the tag to a resource appropriate for the API operation:
API | Can you apply a tag to a resource to authorize access? | If yes, which resource  
---|---|---  
`ListContainerRepositories` | No | None  
`ListContainerImages` | No | None  
`ListContainerImageSignatures` | No | None  
`GetContainerConfiguration` | No | None  
`GetContainerRepository` | Yes | Repository  
`GetContainerImage` | Yes | Image  
`GetContainerImageSignature` | Yes | Image signature  
`CreateContainerRepository` | No | None  
`DeleteContainerRepository` | Yes | Repository  
`UpdateContainerImage` | Yes | Image  
`DeleteContainerImage` | Yes | Image  
`RestoreContainerImage` | Yes | Image  
`CreateContainerImageSignature` | No | None  
`UpdateContainerImageSignature` | Yes | Image signature  
`DeleteContainerImageSignature` | Yes | Image signature  
`RemoveContainerVersion` | Yes | Image  
`UpdateContainerRepository` | Yes | Repository  
`ChangeContainerRepositoryCompartment` | Yes | Repository  
`UpdateContainerConfiguration` | No | None  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `repos` resource-type includes the same permissions and API operations as the `inspect` verb, plus the REPOSITORY_READ permission and a number of API operations (e.g., `GetContainerRepository`, etc.). The `use` verb covers still another permission and API operation compared to `read`. Lastly, `manage` covers more permissions and operations compared to `use`.
[repos](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/registrypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  REPOSITORY_INSPECT |  `ListContainerRepositories` `ListContainerImages` ` ListContainerImageSignatures` `GetContainerConfiguration` |  none  
read |  INSPECT + REPOSITORY_READ |  `GetContainerRepository` `GetContainerImage` `GetContainerImageSignature` |  none  
use |  no extra |  none  
manage |  USE + REPOSITORY_CREATE REPOSITORY_DELETE REPOSITORY_UPDATE REPOSITORY_MANAGE |  `CreateContainerRepository` `DeleteContainerRepository` `DeleteContainerImage` `RestoreContainerImage` `UpdateContainerImage` `CreateContainerImageSignature` `UpdateContainerImageSignature` `DeleteContainerImageSignature` `RemoveContainerVersion` `UpdateContainerRepository` `ChangeContainerRepositoryCompartment` `UpdateContainerConfiguration` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListContainerRepositories` | REPOSITORY_INSPECT  
`CreateContainerRepository` | REPOSITORY_CREATE  
`GetContainerRepository` | REPOSITORY_READ  
`UpdateContainerRepository` | REPOSITORY_MANAGE  
`DeleteContainerRepository` | REPOSITORY_DELETE  
`ChangeContainerRepositoryCompartment` | REPOSITORY_MANAGE  
`ListContainerImages` | REPOSITORY_INSPECT  
`GetContainerImage` | REPOSITORY_READ  
`UpdateContainerImage` | REPOSITORY_UPDATE  
`DeleteContainerImage` | REPOSITORY_UPDATE  
`RestoreContainerImage` | REPOSITORY_UPDATE  
`RemoveContainerVersion` | REPOSITORY_UPDATE  
`ListContainerImageSignatures` | REPOSITORY_INSPECT  
`GetContainerImageSignature` | REPOSITORY_READ  
`CreateContainerImageSignature` | REPOSITORY_UPDATE  
`UpdateContainerImageSignature` | REPOSITORY_UPDATE  
`DeleteContainerImageSignature` | REPOSITORY_UPDATE  
`GetContainerConfiguration` | REPOSITORY_INSPECT  
`UpdateContainerConfiguration` | REPOSITORY_MANAGE  
Was this article helpful?
YesNo

