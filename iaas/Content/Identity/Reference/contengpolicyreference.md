Updated 2024-08-13
# Details for Kubernetes Engine
This topic covers details for writing policies to control access to Kubernetes Engine.
## Resource-Types 🔗 
### Aggregate Resource-Type
  * `cluster-family`


### Individual Resource-Types
  * `clusters`
  * `cluster-node-pools`
  * `cluster-pod-shapes`
  * `cluster-virtualnode-pools`
  * `cluster-work-requests`
  * `cluster-workload-mappings`


### Comments
A policy that uses `<verb> cluster-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm#contengverbresourcetypecombinationdetails) for details of the API operations covered by each verb, for each individual resource-type included in `cluster-family`.
## Supported Variables 🔗 
Kubernetes Engine supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the ones listed here.
The `clusters` resource type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.cluster.id` | Entity (OCID)  
The `cluster-node-pools` resource type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.nodepool.id` | Entity (OCID)  
The `cluster-virtual-node-pools` resource type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.virtualnodepool.id` | Entity (OCID)  
`target.cluster.id` | Entity (OCID)  
The `cluster-workload-mappings` resource type can use the following variables:
Variable | Variable Type | Comments  
---|---|---  
`target.clusterworkloadmapping.id` | Entity (OCID)  
`target.mapping.cluster_id` | Entity (OCID)  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `clusters` resource-type includes the same permissions and API operations as the `inspect` verb, plus the CLUSTER_READ permission and a number of API operations (e.g., `GetCluster`, etc.). The `use` verb covers still another permission and API operation compared to `read`. Lastly, `manage` covers more permissions and operations compared to `use`.
[clusters](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CLUSTER_INSPECT | `ListClusters` `ListWorkRequests` | none  
read | INSPECT + CLUSTER_READ | INSPECT + `GetCluster` `GetWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` `ListAddons` `GetAddon` `GetCredentialRotationStatus` | none  
use | READ + CLUSTER_USE | READ + `CreateKubeconfig` | none  
manage | USE + CLUSTER_CREATE CLUSTER_DELETE CLUSTER_UPDATE CLUSTER_MANAGE CLUSTER_JOIN | USE + `UpdateCluster` `AdministerK8s` `InstallAddon` `UpdateAddon` `DisableAddon` `JoinCluster` `StartCredentialRotation` `CompleteCredentialRotation` | `CreateCluster` (also need `use subnets`, `read                   virtual-network-family`, `inspect                   compartments`, `use vnics`, `use                   network-security-groups`, `use                   private-ips`, and `manage                 public-ips`) `DeleteCluster` (also need `manage                   cluster-node-pools`, `manage                   instance-family`, `use subnets`, `use vnics`,` use private-ips`, and` manage public-ips`) `UpdateClusterEndpointConfig` (also need `use                   vnics`, ` use network-security-groups`, `use private-ips`, and `manage                   public-ips`)  
[cluster-node-pools](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CLUSTER_NODE_POOL_INSPECT | `ListNodePools` `ListWorkRequests` | none  
read | INSPECT + CLUSTER_NODE_POOL_READ | INSPECT + `GetNodePool` `GetWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` | none  
use | no extra | no extra | none  
manage | USE + CLUSTER_NODE_POOL_CREATE CLUSTER_NODE_POOL_DELETE CLUSTER_NODE_POOL_UPDATE | no extra | `CreateNodePool`, `DeleteNodePool`, and `UpdateNodePool` (also need `manage instance-family`, `use subnets`, `use vnics`, and `inspect compartments`)   
[cluster-pod-shapes](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CLUSTER_VIRTUAL_NODE_POOL_INSPECT |  `ListPodShapes` |  none  
read | no extra |  no extra |  none  
use |  no extra |  no extra |  none  
manage |  no extra |  no extra |  none  
[cluster-virtual-node-pools](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CLUSTER_VIRTUAL_NODE_POOL_INSPECT |  `ListVirtualNodePools` `ListPodShapes` |  none  
read | INSPECT + CLUSTER_VIRTUAL_NODE_POOL_READ |  INSPECT + `GetVirtualNodePool` `ListPodShapes` `ListVirtualNodes` `GetVirtualNode` |  none  
use |  no extra |  no extra |  none  
manage |  USE + CLUSTER_VIRTUAL_NODE_POOL_CREATE CLUSTER_VIRTUAL_NODE_POOL_UPDATE CLUSTER_VIRTUAL_NODE_POOL_DELETE |  USE + `CreateVirtualNodePool` `UpdateVirtualNodePool` `DeleteVirtualNodePool` `UpdateVirtualNode` `DeleteVirtualNode` |  none  
[cluster-work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CLUSTER_WORK_REQUEST_INSPECT | `ListWorkRequests` | none  
read | INSPECT + CLUSTER_WORK_REQUEST_READ | INSPECT + `GetWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` | none  
use | no extra | no extra | none  
manage | USE + CLUSTER_WORK_REQUEST_DELETE | USE + `DeleteWorkRequest` | none  
[cluster-workload-mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CLUSTER_WORKLOAD_MAPPING_INSPECT | `ListWorkloadMappings` |  none  
read | INSPECT + CLUSTER_WORKLOAD_MAPPING_READ |  INSPECT + `GetWorkloadMapping` |  none  
use |  READ + CLUSTER_WORKLOAD_MAPPING_UPDATE CLUSTER_WORKLOAD_COMPARTMENT_BIND CLUSTER_WORKLOAD_COMPARTMENT_UNBIND |  `UpdateWorkloadMapping` |  none  
manage |  USE + CLUSTER_WORKLOAD_MAPPING_CREATE CLUSTER_WORKLOAD_MAPPING_DELETE |  USE + `CreateWorkloadMapping` `DeleteWorkloadMapping` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListClusters` | CLUSTER_INSPECT  
`CreateCluster` | CLUSTER_CREATE  
`CreateKubeconfig` | CLUSTER_USE  
`GetCluster` | CLUSTER_READ  
`UpdateCluster` | CLUSTER_UPDATE  
`JoinCluster` | CLUSTER_MANAGE  
`DeleteCluster` | CLUSTER_DELETE, CLUSTER_NODE_POOL_DELETE  
`UpdateClusterEndpointConfig` | CLUSTER_MANAGE  
`AdministerK8s` | CLUSTER_MANAGE  
`GetCredentialRotationStatus` | CLUSTER_READ  
`StartCredentialRotation` | CLUSTER_UPDATE  
`CompleteCredentialRotation` | CLUSTER_UPDATE  
`ListNodePools` | CLUSTER_NODE_POOL_INSPECT  
`CreateNodePool` | CLUSTER_NODE_POOL_CREATE  
`GetNodePool` | CLUSTER_NODE_POOL_READ  
`GetNodePoolOptions` | CLUSTER_READ  
`UpdateNodePool` | CLUSTER_NODE_POOL_UPDATE  
`DeleteNodePool` | CLUSTER_NODE_POOL_DELETE  
`ListWorkRequests` | CLUSTER_WORK_REQUEST_INSPECT, CLUSTER_NODE_POOL_INSPECT, CLUSTER_INSPECT  
`GetWorkRequest` | CLUSTER_WORK_REQUEST_READ, CLUSTER_NODE_POOL_READ, CLUSTER_READ  
`ListWorkRequestErrors` | CLUSTER_WORK_REQUEST_READ, CLUSTER_NODE_POOL_READ, CLUSTER_READ  
`ListWorkRequestLogs` | CLUSTER_WORK_REQUEST_READ, CLUSTER_NODE_POOL_READ, CLUSTER_READ  
`DeleteWorkRequest` | CLUSTER_WORK_REQUEST_DELETE  
`ListVirtualNodePools` | CLUSTER_VIRTUAL_NODE_POOL_INSPECT  
`GetVirtualNodePool` | CLUSTER_VIRTUAL_NODE_POOL_READ  
`CreateVirtualNodePool` | CLUSTER_VIRTUAL_NODE_POOL_CREATE  
`UpdateVirtualNodePool` | CLUSTER_VIRTUAL_NODE_POOL_UPDATE  
`DeleteVirtualNodePool` | CLUSTER_VIRTUAL_NODE_POOL_DELETE  
`ListVirtualNodes` | CLUSTER_VIRTUAL_NODE_POOL_READ  
`GetVirtualNode` | CLUSTER_VIRTUAL_NODE_POOL_READ  
`DeleteVirtualNode` | CLUSTER_VIRTUAL_NODE_POOL_UPDATE  
`ListPodShapes` | CLUSTER_VIRTUAL_NODE_POOL_INSPECT  
`GetVirtualNode` | CLUSTER_VIRTUAL_NODE_POOL_READ  
`ListVirtualNodes` | CLUSTER_VIRTUAL_NODE_POOL_READ  
`DeleteVirtualNode` | CLUSTER_VIRTUAL_NODE_POOL_UPDATE  
`UpdateVirtualNode` | CLUSTER_VIRTUAL_NODE_POOL_UPDATE  
`ListAddons` | CLUSTER_READ  
`GetAddon` | CLUSTER_READ  
`UpdateAddon` | CLUSTER_UPDATE  
`DisableAddon` | CLUSTER_UPDATE  
`InstallAddon` | CLUSTER_UPDATE  
`ListWorkloadMappings` | CLUSTER_WORKLOAD_MAPPING_INSPECT  
`GetWorkloadMapping` | CLUSTER_WORKLOAD_MAPPING_READ  
`CreateWorkloadMapping` | CLUSTER_WORKLOAD_MAPPING_CREATE, CLUSTER_WORKLOAD_COMPARTMENT_BIND  
`UpdateWorkloadMapping` | CLUSTER_WORKLOAD_MAPPING_UPDATE, CLUSTER_WORKLOAD_COMPARTMENT_BIND, CLUSTER_WORKLOAD_COMPARTMENT_UNBIND  
`DeleteWorkloadMapping` | CLUSTER_WORKLOAD_MAPPING_DELETE, CLUSTER_WORKLOAD_COMPARTMENT_UNBIND  
Was this article helpful?
YesNo

