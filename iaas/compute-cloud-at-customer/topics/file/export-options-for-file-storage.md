Updated 2024-10-07
# Export Options for File Storage
On Compute Cloud@Customer, NFS export options enable you to create more granular access control than is possible using security list rules to limit VCN access. You can use NFS export options to specify access levels for IP addresses or CIDR blocks connecting to file systems through exports in a mount target. Access can be restricted so that each client’s file system is inaccessible and invisible to the other, providing better security controls in multitenant environments. 
Using NFS export option access controls, you can limit clients' ability to connect to the file system and view or write data. For example, if you want to allow clients to consume but not update resources in your file system, you can set access to read-only. You can also reduce client root access to your file systems and map specified User IDs (UIDs) and Group IDs (GIDs) to a single anonymous UID/GID of your choice.
## Export Options 🔗 
Exports control how NFS clients access file systems when they connect to a mount target. File systems are exported (made available) through mount targets. 
NFS export options are a set of parameters within the export that specify the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range. You can have up to 100 options per file system.
Each separate client IP address or CIDR block you want to define access for needs a separate export options entry in the export. For example, if you want to set options for NFS client IP addresses 10.0.0.6, 10.0.0.08, and 10.0.0.10, you need to create three separate entries, one for each IP address.
When there is more than one export using the same file system and same mount target, the export options that are applied to an instance are the options with a source that most closely matches the instance IP address. The smallest (most specific) match takes precedence across all the exports. Therefore, you can determine which export options are applied to an instance by looking at source value of all the exports.
For example, consider the following two export options entries specifying access for an export: 
Entry 1: Source: 10.0.0.8/32, Access: Read/Write
Entry 2: Source: 10.0.0.0/16, Access: Read-only
In this case, clients who connect to the export from IP address 10.0.0.8 have read/write access. When there are multiple export options, the most specific match is applied.
**Important**
When more than one file system is exported to the same mount target, you must export to the mount target with the smallest network (largest CIDR number) first. For detailed information and instructions, refer to My Oracle Support [Doc ID 2823994.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2823994.1). 
**Important**
File systems can be associated with one or more exports, contained within one or more mount targets. 
If the client source IP address does not match any entry on the list for a single export, then that export is not visible to the client. However, the file system could be accessed through other exports on the same or other mount targets. To completely deny client access to a file system, be sure that the client source IP address or CIDR block is not included in any export for any mount target associated with the file system.
For information about how to configure export options for various file sharing scenarios, see [NFS Access Control Scenarios](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/export-options-for-file-storage.htm#nfs-access-control-scenarios "On Compute Cloud@Customer, Learn different ways to control NFS access by reviewing some scenarios.").
For more information about configuring export options, refer to the section titled [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
## NFS Export Option Defaults 🔗 
When you create a file system and export, the NFS export options for that file system are set to the following defaults, which allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access: 
Note – When using the CLI to set the export options, if you set the options with an empty array (no options specified), the export is not accessible to any clients.
Export Option in the Compute Cloud@Customer Console | Export Option in the CLI | Default Value | Description  
---|---|---|---  
**Source:** |  `source` |  0.0.0.0/0 |  The IP address or CIDR block of a connecting NFS client.   
**Ports:** |  `require-privileged-source-port` |  Any |  Always set to:
  * Console: Any
  * CLI: `false`

  
**Access:** |  `access` |  Read/Write |  Specifies the source NFS client access. Can be set to one of these values:
  * `READ_WRITE`
  * `READ_ONLY`

  
**Squash:** |  `identity-squash` |  None |  Determines whether the clients accessing the file system as root have their User ID (UID) and Group ID (GID) remapped to the squash UID/GID. These are the possible values:
  * Root – Only the root user is remapped.
  * None – No users are remapped.

  
**Squash UID/GID:** |  `anonymous-uid`and `anonymous-gid` |  65534 |  This setting is used along with the Squash option. When remapping a root user, you can use this setting to change the default anonymousUid and anonymousGid to any user ID of your choice.  
## NFS Access Control Scenarios 🔗 
On Compute Cloud@Customer, Learn different ways to control NFS access by reviewing some scenarios. 
  * [Scenario A: Control Host Based Access](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/export-options-for-file-storage.htm#scenario-a-control-host-based-access "On Compute Cloud@Customer, provide a managed hosted environment for two clients. The clients share a mount target, but each has their own file system, and can't access each other's data."): Provides a managed environment for two clients. The clients share a mount target, but each has their own file system, and can't access each others data. 
  * [Scenario B: Limit the Ability to Write Data](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/export-options-for-file-storage.htm#scenario-b-limit-the-ability-to-write-data "On Compute Cloud@Customer, provide data to customers for consumption, but don't allow them to update the data."): Provides data to clients for consumption, but doesn't allow them to update the data.
  * [Scenario C: Improve File System Security](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/export-options-for-file-storage.htm#scenario-c-improve-file-system-security "On Compute Cloud@Customer, to increase security, you can limit the root user's privileges when connecting to File System A. Use Identity Squash to remap root users to UID/GID 65534."): Increases security by limiting the root user's privileges when connecting to a file system.


### Scenario A: Control Host Based Access 🔗 
On Compute Cloud@Customer, provide a managed hosted environment for two clients. The clients share a mount target, but each has their own file system, and can't access each other's data.
For example:
  * Client A is assigned to CIDR block 10.0.0.0/24, and requires read/write access to file system A, but not file system B. 
  * Client B is assigned to CIDR block 10.1.1.0/24, and requires read/write access to file system B, but not file system A. 
  * Client C is assigned to CIDR block 10.2.2.0/24, and has no access of any kind to file system A or file system B. 
  * Both file systems A and B are associated with a single mount target, MT1. Each file system has an export contained in the export set of MT1. 


Because Client A and Client B access the mount target from different CIDR blocks, you can set the client options for both file system exports to allow access to only a single CIDR block. Client C is denied access by not including its IP address or CIDR block in the NFS export options for any export of either file system.
#### Compute Cloud@Customer Console Example 🔗 
Set the export options for file system A to allow read/write access only to Client A, who is assigned to CIDR block 10.0.0.0/24. Client B and Client C aren't included in this CIDR block, and can't access the file system. 
**Note**
To learn how to access the NFS export options in the Compute Cloud@Customer Console see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
Source | Ports | Access | Squash | Squash UID/GID  
---|---|---|---|---  
10.0.0.0/24 | Any | Read/Write | None | (not used)  
Set the export options for file system B to allow read/write access only to Client B, who is assigned to CIDR block 10.1.1.0/24. Client A and Client C aren't included in this CIDR block, and can't access the file system.
Source | Ports | Access | Squash | Squash UID/GID  
---|---|---|---|---  
10.1.1.0/24 | Any | Read/Write | None | (not used)  
#### CLI Example 🔗 
**Note**
To learn how to access the NFS export options in the CLI, see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
Set the export options for file system A to allow `Read_Write` access only to Client A, who is assigned to CIDR block 10.0.0.0/24. Client B and Client C aren't included in this CIDR block, and can't access the file system. 
```
oci fs export update --export-id <File_system_A_export_ID> --export-options \
'[{"source":"10.0.0.0/24","require-privileged-source-port":"false","access":"READ_WRITE","identity-squash":"NONE","anonymous-uid":"65534","anonymous-gid":"65534"}]'
```

Set the export options for file system B to allow `Read_Write` access only to Client B, who is assigned to CIDR block 10.1.1.0/24. Client A and Client C are not included in this CIDR block, and can't access the file system. 
```
oci fs export update --export-id <File_system_B_export_ID> --export-options \
'[{"source":"10.1.1.0/24 ","require-privileged-source-port":"false","access":"READ_WRITE","identity-squash":"NONE","anonymous-uid":"65534","anonymous-gid":"65534"}]'
```

### Scenario B: Limit the Ability to Write Data 🔗 
On Compute Cloud@Customer, provide data to customers for consumption, but don't allow them to update the data.
For example, you'd like to publish a set of resources in file system A for an application to consume, but not change. The application connects from IP address 10.0.0.8. 
#### Compute Cloud@Customer Console Example 🔗 
Set the source IP address 10.0.0.8 to read-only in the export for file system A.
**Note**
To learn how to access the NFS export options in the Compute Cloud@Customer Console see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
Source | Ports | Access | Squash | Squash UID/GID  
---|---|---|---|---  
10.0.0.8 | Any | Read-only | None | (not used)  
#### CLI Example 🔗 
**Note**
To learn how to access the NFS export options in the CLI, see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
Set the source IP address 10.0.0.8 to `READ_ONLY` in the export for file system A. 
```
oci fs export update --export-id <File_System_A_export_OCID> --export-options \
'[{"source":"10.0.0.8","require-privileged-source-port":"false","access":"READ_ONLY","identitysquash":"NONE","anonymousuid":"65534","anonymousgid":"65534"}]'
```

### Scenario C: Improve File System Security 🔗 
On Compute Cloud@Customer, to increase security, you can limit the root user's privileges when connecting to File System A. Use Identity Squash to remap root users to UID/GID 65534. 
In UNIX-like systems, this UID/GID combination is reserved for '_nobody_ ', a user with no system privileges. 
#### Compute Cloud@Customer Console Example 🔗 
Set the source IP address 10.0.0.8 to read-only in the export for file system A.
**Note**
To learn how to access the NFS export options in the Compute Cloud@Customer Console see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
Source | Ports | Access | Squash | Squash UID/GID  
---|---|---|---|---  
0.0.0.0/0 | Any | Read/Write | Root | 65534  
#### CLI Example 🔗 
**Note**
To learn how to access the NFS export options in the CLI, see [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
```
oci fs export update --export-id <File_System_A_export_OCID> --export-options  \
'[{"source":"0.0.0.0/0","require-privileged-source-port":"false","access":"READ_WRITE","identitysquash":"ROOT","anonymousuid":"65534","anonymousgid":"65534"}]' 
```

Was this article helpful?
YesNo

