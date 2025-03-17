Updated 2024-06-06
# Details for the Streaming Service
This topic covers details for writing policies to control access to the Streaming service.
## Resource-Types 🔗 
`streams`
`stream-pull`
`stream-push`
`connect-harness`
`stream-pools`
`stream-family`
## Supported Variables 🔗 
The Streaming service supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)) plus the following:
The `streams` resource type can use the following variables:
Variable | Variable Type | Source  
---|---|---  
`target.stream.id` | Entity (OCID) | Request  
The `connect-harness` resource type can use the following variables:
Variable | Variable Type | Source  
---|---|---  
`target.connectharness.id` | Entity (OCID) | Request  
The `stream-pools` resource type can use the following variables:
Variable | Variable Type | Source  
---|---|---  
`target.streampool.id` | Entity (OCID) | Request  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
[streams](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STREAM_INSPECT | `ListStreams` | none  
read | INSPECT + STREAM_READ | `GetStream` | none  
use | READ + STREAM_UPDATE STREAM_MOVE STREAM_PRODUCE STREAM_CONSUME | `UpdateStream` `MoveStream` `PutMessages` `GetMessages` `CreateCursor` `CreateGroupCursor` `GetGroup` `UpdateGroup` `ConsumerHeartbeat` `ConsumerCommit` | none  
manage | USE + STREAM_CREATE STREAM_DELETE | `CreateStream` `DeleteStream` |  none  
[stream-pull](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | _none_ | none  
read | none | _none_ | none  
use | STREAM_CONSUME | `GetMessages` `CreateCursor` `CreateGroupCursor` `GetGroup` `UpdateGroup` `ConsumerHeartbeat` `ConsumerCommit` | none  
manage | no extra | no extra | none  
[stream-push](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | none | none | none  
use | STREAM_PRODUCE | `PutMessages` | none  
manage | no extra | no extra | none  
[stream-pools](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STREAM_POOL_INSPECT | `ListStreamPools` | none  
read | INSPECT + STREAM_POOL_READ | `GetStreamPools` | none  
use | READ + STREAM_POOL_UPDATE STREAM_POOL_MOVE | `UpdateStreamPool` `MoveStreamPool` | none  
manage | USE + STREAM_POOL_CREATE STREAM_POOL_DELETE | `CreateStreamPool` `DeleteStreamPool` |  none  
[connect-harness](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CONNECT_HARNESS_INSPECT | `ListConnectHarnesses` | none  
read | INSPECT + CONNECT_HARNESS_READ | `GetConnectHarness` | none  
use | READ + CONNECT_HARNESS_UPDATE CONNECT_HARNESS_MOVE CONNECT_HARNESS_USE | `UpdateConnectHarness` `MoveConnectHarness` | none  
manage | USE + CONNECT_HARNESS_CREATE CONNECT_HARNESS_DELETE | `CreateConnectHarness` `DeleteConnectHarness` |  none  
[stream-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  STREAM_INSPECT CONNECT_HARNESS_INSPECT STREAM_POOL_INSPECT |  `ListStreams` `ListConnectHarnesses` `ListStreamPools` |  none  
read |  INSPECT + STREAM_READ CONNECT_HARNESS_READ STREAM_POOL_READ |  `GetStreams` `GetConnectHarness` `GetStreamPools` |  none  
use |  READ + STREAM_UPDATE STREAM_MOVE STREAM_PRODUCE STREAM_CONSUME CONNECT_HARNESS_UPDATE CONNECT_HARNESS_MOVE CONNECT_HARNESS_USE STREAM_POOL_UPDATE STREAM_POOL_MOVE |  `UpdateStream` `MoveStream` `PutMessages` `GetMessages` `CreateCursor` `CreateGroupCursor` `GetGroup` `UpdateGroup` `ConsumerHeartbeat` `ConsumerCommit` `UpdateConnectHarness` `MoveConnectHarness` `UpdateStreamPool` `MoveStreamPool` |  none  
manage |  USE + STREAM_CREATE STREAM_DELETE CONNECT_HARNESS_CREATE CONNECT_HARNESS_DELETE  STREAM_POOL_CREATE  STREAM_POOL_DELETE |  `CreateStream` `DeleteStream` `CreateConnectHarness` `DeleteConnectHarness` `CreateStreamPool` `DeleteStreamPool` |  none  
## Permissions Required for Each API Operation 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListStreams` | STREAM_INSPECT  
`CreateStream` | STREAM_CREATE  
`GetStream` | STREAM_READ  
`DeleteStream` | STREAM_DELETE  
`GetMessages` | STREAM_CONSUME  
`PutMessages` | STREAM_PRODUCE  
`UpdateStream` | STREAM_UPDATE  
`CreateCursor` | STREAM_CONSUME  
`CreateGroupCursor ` | STREAM_CONSUME  
`GetGroup` | STREAM_CONSUME  
`UpdateGroup` | STREAM_CONSUME  
`ConsumerHeartbeat` | STREAM_CONSUME  
`ConsumerCommit` | STREAM_CONSUME  
`ListStreamPools` | STREAM_POOL_INSPECT  
`CreateStreamPool` | STREAM_POOL_CREATE  
`GetStreamPool` | STREAM_POOL_READ  
`DeleteStreamPool` | STREAM_POOL_DELETE  
`MoveStreamPool` | STREAM_POOL_MOVE  
`UpdateStreamPool` | STREAM_POOL_UPDATE  
`ListConnectHarnesses` | CONNECT_HARNESS_INSPECT  
`CreateConnectHarness` | CONNECT_HARNESS_CREATE  
`GetConnectHarness` | CONNECT_HARNESS_READ  
`DeleteConnectHarness` | CONNECT_HARNESS_DELETE  
`MoveConnectHarness` | CONNECT_HARNESS_MOVE  
`UpdateConnectHarness` | CONNECT_HARNESS_UPDATE  
Was this article helpful?
YesNo

