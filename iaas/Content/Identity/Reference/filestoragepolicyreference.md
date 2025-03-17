Updated 2025-03-04
# Details for the File Storage Service
This topic covers details for writing policies to control access to the File Storage Service.
## Aggregate Resource-Type 🔗 
  * `file-family`


## Individual Resource-Types 🔗 
  * `file-systems`
  * `filesystem-snapshot-policies`
  * `mount-targets`
  * `outbound-connectors`
  * `export-sets`
  * `replications`
  * `replication-targets`
  * `work-requests`


### Comments
A policy that uses `<verb> file-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm#Details) for details of the API operations covered by each verb, for each individual resource-type included in `file-family`.
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `file-systems` resource-type includes the same permissions and API operations as the `inspect` verb, plus the FILE_SYSTEM_READ permission and a number of API operations (e.g., `GetFileSystem`, `ListMountTargets`, etc.). The `use` verb covers still another permission and set of API operations compared to `read`. Lastly, `manage` covers two more permissions and operations compared to `use`.
[export-sets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | EXPORT_SET_INSPECT | `ListExportSets` | none  
read | INSPECT + EXPORT_SET_READ | INSPECT + `GetExport` `GetExportSet` `ListExports` | none  
use | no extra | no extra | none  
manage | USE + EXPORT_SET_CREATE EXPORT_SET_UPDATE EXPORT_SET_DELETE | USE + `CreateExportSet` `UpdateExportSet` `AddExportLock` `RemoveExportLock` `DeleteExportSet` | `CreateExport` `DeleteExport` (both also need `use file-systems`. )  
[file-systems](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  FILE_SYSTEM_INSPECT | `ListFileSystems` |  none  
read |  INSPECT + FILE_SYSTEM_READ |  INSPECT + `GetFileSystem` `GetSnapshot` `ListSnapshots` `GetQuotaRule` `ListQuotaRules ` |  none  
use |  READ + FILE_SYSTEM_NFSv3_EXPORT FILE_SYSTEM_NFSv3_UNEXPORT FILE_SYSTEM_CLONE FILE_SYSTEM_REPLICATION_SOURCE FILE_SYSTEM_UPDATE​_FILESYSTEM_SNAPSHOT_POLICY |  no extra |  `DeleteExport` (both also need `manage export-sets`. )  
manage |  USE + FILE_SYSTEM_CREATE FILE_SYSTEM_UPDATE FILE_SYSTEM_DELETE FILE_SYSTEM_MOVE FILE_SYSTEM_CREATE_SNAPSHOT  FILE_SYSTEM_DELETE_SNAPSHOT FILE_SYSTEM_CLONE FILE_SYSTEM_REPLICATION_TARGET | USE +`CreateFileSystem` `UpdateFileSystem` `AddFileSystemLock` `RemoveFileSystemLock` `DeleteFileSystem` `ChangeFileSystemCompartment` `CreateSnapshot` `DeleteSnapshot` `CreateQuotaRule``UpdateQuotaRule``DeleteQuotaRule``ToggleQuotaRules ` |  If creating a file system or clone _encrypted with a Key Management master encryption key_ , also need `use key-delegate` (for the caller) and `read keys` (for the service principal). For more information, see policy details for your service. Cloning a file system uses the `CreateFileSystem` API and requires FILE_SYSTEM_CLONE.  
[filesystem-snapshot-policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  FILESYSTEM_SNAPSHOT​_POLICY_INSPECT | `ListFilesystemSnapshotPolicies` |  none  
read |  INSPECT + FILESYSTEM_SNAPSHOT​_POLICY_READ | `ListFilesystemSnapshotPolicies``GetFilesystemSnapshotPolicy` |  none  
use |  READ + FILE_SYSTEM_UPDATE​_FILESYSTEM_SNAPSHOT_POLICY | `ListFilesystemSnapshotPolicies``GetFilesystemSnapshotPolicy` |  `UpdateFileSystem`  
manage |  USE + FILESYSTEM_SNAPSHOT​_POLICY_CREATE FILESYSTEM_SNAPSHOT​_POLICY_UPDATE FILESYSTEM_SNAPSHOT​_POLICY_MOVE FILESYSTEM_SNAPSHOT​_POLICY_DELETE | `ListFilesystemSnapshotPolicies``GetFilesystemSnapshotPolicy` `CreateFilesystemSnapshotPolicy``UpdateFilesystemSnapshotPolicy``AddFilesystemSnapshotPolicyLock``RemoveFilesystemSnapshotPolicyLock``MoveFilesystemSnapshotPolicy``DeleteFilesystemSnapshotPolicy` |  none  
[mount-targets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  MOUNT_TARGET_INSPECT | `ListMountTargets` |  none  
read |  INSPECT + MOUNT_TARGET_READ |  INSPECT + `GetMountTarget` |  none  
use |  no extra |  no extra |  none  
manage |  USE + MOUNT_TARGET_CREATE  MOUNT_TARGET_UPDATE MOUNT_TARGET_SHAPE_UPGRADE MOUNT_TARGET_SHAPE_DOWNGRADE MOUNT_TARGET_DELETE MOUNT_TARGET_MOVE | USE + `CreateMountTarget`, `DeleteMountTarget`, (both also need `use vnics`, `use private-ips`, and `use subnets`.) `ChangeMountTargetCompartment`, `UpgradeMountTarget`, `DowngradeMountTarget`, `AddMountTargetLock`, `RemoveMountTargetLock`  
[outbound-connectors](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  OUTBOUND_CONNECTOR​_INSPECT | `ListOutboundConnectors` |  none  
read |  INSPECT + OUTBOUND_CONNECTOR​_READ |  INSPECT + `GetOutboundConnector` |  none  
use |  no extra |  no extra |  none  
manage |  USE + OUTBOUND_CONNECTOR​_CREATE  OUTBOUND_CONNECTOR​_UPDATE OUTBOUND_CONNECTOR​_DELETE OUTBOUND_CONNECTOR​_MOVE |  USE + `CreateOutboundConnector` `UpdateOutboundConnector` `AddOutboundConnectorLock` `RemoveOutboundConnectorLock` `DeleteOutboundConnector` `ChangeOutboundConnectorCompartment` |  none  
[replications and replication-targets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  REPLICATION_INSPECT | `ListReplications` |  none  
read |  INSPECT + REPLICATION_READ |  INSPECT + `GetReplication` |  none  
use |  no extra |  no extra |  none  
manage |  USE + REPLICATION_CREATE  REPLICATION_UPDATE REPLICATION_DELETE REPLICATION_MOVE |  USE + `CreateReplication` `UpdateReplication` `ChangeReplicationCompartment` `AddReplicationLock` `RemoveReplicationLock` `DeleteReplication` `DeleteReplicationTarget` |  none  
[work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  FSS_WORK_REQUEST_INSPECT | `ListWorkRequests` |  none  
read |  INSPECT + FSS_WORK_REQUEST_READ |  INSPECT + `GetWorkRequest` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
**Tip** If a group uses the Console to create file systems, permissions to read mount targets is required. [See the File Storage policy examples](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#create-file-system) for further guidance.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi). 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListExports` | EXPORT_SET_READ  
`CreateExport` | EXPORT_SET_UPDATE + FILE_SYSTEM_NFSv3_EXPORT  
`GetExport` | EXPORT_SET_READ  
`AddExportLock` | EXPORT_SET_UPDATE + RESOURCE_LOCK_ADD  
`RemoveExportLock` | EXPORT_SET_UPDATE + RESOURCE_LOCK_REMOVE  
`DeleteExport` | EXPORT_SET_UPDATE + FILE_SYSTEM_NFSv3_UNEXPORT  
`ListExportSets` | EXPORT_SET_INSPECT  
`CreateExportSet` | EXPORT_SET_CREATE  
`GetExportSet` | EXPORT_SET_READ  
`UpdateExportSet` | EXPORT_SET_UPDATE  
`DeleteExportSet` | EXPORT_SET_DELETE  
`ListFileSystems` | FILE_SYSTEM_INSPECT  
`CreateFileSystem` | FILE_SYSTEM_CREATECloning a file system also requires FILE_SYSTEM_CLONEAssociating the file system with a snapshot policy also requires FILE_SYSTEM_UPDATE_FILESYSTEM​_SNAPSHOT_POLICY  
`GetFileSystem` | FILE_SYSTEM_READ  
`UpdateFileSystem` | FILE_SYSTEM_UPDATEAssociating the file system with a snapshot policy also requires FILE_SYSTEM_UPDATE_FILESYSTEM​_SNAPSHOT_POLICY  
`AddFileSystemLock` | FILE_SYSTEM_UPDATE + RESOURCE_LOCK_ADD  
`RemoveFileSystemLock` | FILE_SYSTEM_UPDATE + RESOURCE_LOCK_REMOVE  
`DeleteFileSystem` | FILE_SYSTEM_DELETE  
`ChangeFileSystemCompartment` | FILE_SYSTEM_MOVE  
`GetFilesystemSnapshotPolicy` | FILESYSTEM_SNAPSHOT_POLICY_READ  
`ListFilesystemSnapshotPolicies` | FILESYSTEM_SNAPSHOT_POLICY_INSPECT  
`CreateFilesystemSnapshotPolicy` | FILESYSTEM_SNAPSHOT_POLICY_CREATE  
`UpdateFilesystemSnapshotPolicy` | FILESYSTEM_SNAPSHOT_POLICY_UPDATE  
`AddFilesystemSnapshotPolicyLock` | FILESYSTEM_SNAPSHOT_POLICY_UPDATE + RESOURCE_LOCK_ADD  
`RemoveFilesystemSnapshotPolicyLock` | FILESYSTEM_SNAPSHOT_POLICY_UPDATE + RESOURCE_LOCK_REMOVE  
`DeleteFilesystemSnapshotPolicy` | FILESYSTEM_SNAPSHOT_POLICY_DELETE  
`MoveFilesystemSnapshotPolicy` | FILESYSTEM_SNAPSHOT_POLICY_MOVE  
`ListMountTargets` | MOUNT_TARGET_INSPECT  
`CreateMountTarget` |  MOUNT_TARGET_CREATE +  VNIC_CREATE(vnicCompartment) +  SUBNET_ATTACH(subnetCompartment) +  VNIC_ATTACH(vnicCompartment) +  PRIVATE _IP_CREATE(subnetCompartment) +  PRIVATE_IP_ASSIGN(subnetCompartment) +  VNIC_ASSIGN(subnetCompartment)   
`GetMountTarget` | MOUNT_TARGET_READ  
`UpdateMountTarget` | MOUNT_TARGET_UPDATE  
`UpgradeShapeMountTarget` | MOUNT_TARGET_SHAPE_UPGRADE  
`ScheduleDowngradeShapeMountTarget` | MOUNT_TARGET_SHAPE_DOWNGRADE  
`CancelDowngradeShapeMountTarget` | MOUNT_TARGET_SHAPE_DOWNGRADE  
`AddMountTargetLock` | MOUNT_TARGET_UPDATE + RESOURCE_LOCK_ADD  
`RemoveMountTargetLock` | MOUNT_TARGET_UPDATE + RESOURCE_LOCK_REMOVE  
`DeleteMountTarget` |  MOUNT_TARGET_DELETE +  VNIC_DELETE(vnicCompartment) +  SUBNET_DETACH(subnetCompartment) +  VNIC_DETACH(vnicCompartment) +  PRIVATE_IP_DELETE(subnetCompartment) +  PRIVATE_IP_UNASSIGN(subnetCompartment) +  VNIC_UNASSIGN(vnicCompartment)  
`ChangeMountTargetCompartment` | MOUNT_TARGET_MOVE  
`ListOutboundConnectors` | OUTBOUND_CONNECTOR_INSPECT  
`CreateOutboundConnector` | OUTBOUND_CONNECTOR_CREATE  
`GetOutboundConnector` | OUTBOUND_CONNECTOR_READ  
`UpdateOutboundConnector` | OUTBOUND_CONNECTOR_UPDATE  
`AddOutboundConnectorLock` | OUTBOUND_CONNECTOR_UPDATE + RESOURCE_LOCK_ADD  
`RemoveOutboundConnectorLock` | OUTBOUND_CONNECTOR_UPDATE + RESOURCE_LOCK_REMOVE  
`DeleteOutboundConnector` | OUTBOUND_CONNECTOR_DELETE  
`ChangeOutboundConnectorCompartment` | OUTBOUND_CONNECTOR_MOVE  
`ListQuotaRules` | FILE_SYSTEM_READ  
`CreateQuotaRule` | FILE_SYSTEM_UPDATE  
`GetQuotaRule` | FILE_SYSTEM_READ  
`UpdateQuotaRule` | FILE_SYSTEM_UPDATE  
`DeleteQuotaRule` | FILE_SYSTEM_UPDATE  
`ToggleQuotaRules ` | FILE_SYSTEM_UPDATE  
`ListSnapshots` | FILE_SYSTEM_READ  
`CreateSnapshot` | FILE_SYSTEM_CREATE_SNAPSHOT  
`GetSnapshot` | FILE_SYSTEM_READ  
`DeleteSnapshot` | FILE_SYSTEM_DELETE_SNAPSHOT  
`GetReplication` | REPLICATION_READ  
`ListReplications` | REPLICATION_INSPECT  
`CreateReplication` |  REPLICATION_CREATE + FILE_SYSTEM_REPLICATION_SOURCE (source file system) + FILE_SYSTEM_REPLICATION_TARGET (target file system)  
`UpdateReplication` | REPLICATION_UPDATE  
`AddReplicationLock` | REPLICATION_UPDATE + RESOURCE_LOCK_ADD  
`RemoveReplicationLock` | REPLICATION_UPDATE + RESOURCE_LOCK_REMOVE  
`ChangeReplicationCompartment` | REPLICATION_MOVE  
`DeleteReplication` | REPLICATION_DELETE  
`DeleteReplicationTarget` | REPLICATION_DELETE  
`GetWorkRequest` | FSS_WORK_REQUEST_READ  
`ListWorkRequests` | FSS_WORK_REQUEST_INSPECT  
Was this article helpful?
YesNo

