Updated 2024-10-07
# File Storage
On Compute Cloud@Customer, the File Storage service provides a durable, scalable, secure network file system. You can connect to a File Storage service file system from any Compute Cloud@Customer compute instance in your Virtual Cloud Network (VCN). 
## File Storage Overview 🔗 
The File Storage service supports these protocols:
  * Network File System version 4.1 (NFSv4.1)
  * Network File System version 4.0 (NFSv4)
  * Network File System version 3.0 (NFSv3)
  * Server Message Block (SMBv2 - SMBv3.1) – Requires Active Directory


**File Storage Connectivity**
You can connect to a File Storage service file system from any instance in your Virtual Cloud Network (VCN). 
**Suitable Workloads**
The File Storage service is designed to meet the needs of applications and users that need an enterprise file system across a wide range of use cases, including the following:
  * **General Purpose File Storage:** Access to a pool of file systems to manage growth of structured and unstructured data. 
  * **Big Data and Analytics:** Run analytic workloads and use shared file systems to store persistent data. 
  * **Lift and Shift of Enterprise Applications:** Migrate existing applications that need NFS storage, such as Oracle Cloud Infrastructure E-Business Suite and PeopleSoft. 
  * **Databases and Transactional Applications:** Run test and development workloads with Oracle Cloud Infrastructure, MySQL, or other databases. 
  * **Backups, Business Continuity, and Disaster Recovery:** Host a secondary copy of relevant file systems from on premises to the cloud for backup and disaster recovery purposes. 
  * **Portable OS Interface (POSIX)-compliant file system**
  * **MicroServices and Docker:** Deliver stateful persistence for containers. Easily scale as your container-based environments grow. 


**Data Protection with Snapshots**
The File Storage service supports snapshots for data protection of your file system. Snapshots are a consistent, point-in-time view of your file systems. Snapshots are copy-on-write, and scoped to the entire file system. The File Storage service encrypts all file system and snapshot data at rest. You can take as many snapshots as you need. 
For data protection, you can use a tool that supports NFS to copy your data to a different file system, object storage, or remote location.
For best performance, use the parallel tar (`partar`) and parallel copy (`parcp`) tools provided in the File Storage Parallel File Toolkit for this purpose. These tools work best with parallel workloads and requests. The Parallel File Toolkit is available for Oracle Linux, Red Hat Enterprise Linux, and CentOS. You can use `rsync` or regular `tar` for other OS types. See [Installing the Parallel File Tools](https://docs.oracle.com/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#install_par_tools) for more information. 
## File Storage Objects 🔗 
**Mount Target**
A mount target is an NFS endpoint in a subnet of your choice. The mount target provides the IP address that's used in the mount command when connecting NFS clients to a file system. File systems are exported (made available) through mount targets.
For an instance to mount a file system, the instance's Virtual Cloud Network (VCN) must have a mount target. A VCN can only have one mount target.
You can reuse the same mount target to make many file systems available. To reuse the same mount target for multiple file systems, create an export in the mount target for each file system.
**Export**
Exports control how NFS clients access file systems when they connect to a mount target. File systems are exported (made available) through mount targets. Each mount target maintains an export set which contains one or many exports. A file system must have at least one export in one mount target for compute instances to mount the file system. 
**Export Set**
An export set is a collection of one or more exports that control what file systems the mount target exports and how those file systems are found using the NFS mount protocol. Each mount target has an export set. Each file system associated with the mount target has at least one export in the export set.
**Export Path**
The export path uniquely identifies the file system within the mount target. The export path is used by a compute instance to mount (logically attach to) the file system. For more information, see [File Storage Paths](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/file-storage.htm#file-storage__file-storage-paths).
**Export Options**
NFS export options are a set of parameters within the export that specify the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range.
**File System**
In Compute Cloud@Customer, file system refers to a file system that's accessed by one or more clients over the network. File systems are associated with a single compartment. File systems must have at least one export in one mount target for any client to mount and use the file system. Data is added to a file system from the client that has mounted (has access to) the file system.
Data is added to a file system from the client that has mounted (has access to) the file system. A file system can have a quota of up to 8 petabytes.
The total number of file systems is limited to 100 per tenancy.
**Virtual Cloud Network (VCN)**
A private network that you set up in Compute Cloud@Customer, with firewall rules and specific types of communication gateways that you can choose to use. A VCN covers a single, contiguous IPv4 CIDR block of your choice.
**Subnet**
Subnets are subdivisions you define in a VCN (for example, 10.0.0.0/24 and 10.0.1.0/24). Subnets contain virtual network interface cards (VNICs), which attach to compute instances. A subnet consists of a contiguous range of IP addresses that don't overlap with other subnets in the VCN.
**Security Rules**
Security rules are virtual firewall rules for your VCN. Your VCN comes with a default security list, and you can add more. These security lists provide ingress and egress rules that specify the types of traffic allowed in and out of the compute instances. You can choose whether a particular rule is stateful or stateless. Security list rules must be set up so that clients can connect to file system mount targets.
Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to resource VNICs you add to the NSG.
**Snapshots**
Snapshots provide a consistent, point-in-time view of your file system, and you can take as many snapshots as you need. Each snapshot reflects only data that changed from the previous snapshot. 
## File Storage Paths 🔗 
The File Storage service uses these kinds of paths:
  * **Export Paths** are part of the information contained in an export that makes a file system available through a mount target. 
The export path is automatically generated when you create an export, and it uniquely identifies the file system within the mount target. 
**Note** – When you create an export from the CLI, you must specify a `--path` <path> argument. The path you specify is recorded but not used for mounting file systems. Compute Cloud@Customer auto-generates a path that's used to mount the file system.
Export path syntax:
```
/export/<file-system-OCID-unique-string>
           
```

where:
    * /export/ – Is the beginning of the export path.
    * <file-system-OCID-unique-string> – Is the unique character string portion of the file system's OCID. 
For example, a file system with this OCID . . .
```
ocid1.filesystem.oc1.pca.d0v812zdp48onybubehhx1c67i4p3mjfth5avt3z2rkn50uqpbce3fhsa8nm
```

. . . has an export path that looks like this:
```
/export/d0v812zdp48onybubehhx1c67i4p3mjfth5avt3z2rkn50uqpbce3fhsa8nm
```

The export path is used by a file system client to mount (logically attach to) the file system. This path is unrelated to any path within the file system or the client instance. It exists solely as a way to distinguish one file system from another within a single mount target.
Example of an export path in a client's mount command:
```
sudo mount -t nfs \
 -o nfsvers=4.0 192.0.2.0:/export/d0v812zdp48onybubehhx1c67i4p3mjfth5avt3z2rkn50uqpbce3fhsa8nm /mnt/fs
```

In this mount command example, `192.0.2.0` is the mount target IP address.`/export/d0v812zdp48onybubehhx1c67i4p3mjfth5avt3z2rkn50uqpbce3fhsa8nm` is the unique export path that was specified when the file system was associated with a mount target during creation. 
Export paths can't be edited after the export is created.
  * **Mount Point Paths** are paths within a client instance to a locally accessible directory to which the remote file system is mounted.
In this mount command example, `/mnt/fs` is the path to the directory on the client instance on which the external file system is mounted.
```
sudo mount -t nfs \
 -o nfsvers=4.0 192.0.2.0:/export/d0v812zdp48onybubehhx1c67i4p3mjfth5avt3z2rkn50uqpbce3fhsa8nm /mnt/fs
```

  * **File System Paths** are paths to directories within the file system, and contain the contents of the file system. When the file system is mounted, you can create any directory structure within it. 


## VCN Security Rules for File Storage 🔗 
On Compute Cloud@Customer, before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports. 
Security rules enable traffic for the following:
  * Open Network Computing Remote Procedure Call (ONC RPC) rpcbind utility protocol
  * Network File System (NFS) protocol
  * Network File System (MOUNT) protocol
  * Network Lock Manager (NLM) protocol


### Ways to Enable Security Rules for File Storage 🔗 
The Networking service offers two virtual firewall features that both use security rules to control traffic at the packet level. The two features are: 
  * **Security lists:** The original virtual firewall feature from the Networking service. When you create a VCN, a default security list is also created. Add the required rules to the security list for the subnet that contains the mount target.
  * **Network security groups (NSGs):** A subsequent feature designed for application components that have different security postures. Create an NSG that contains the required rules, and then add the mount target to the NSG. Each mount target can belong to up to five (5) NSGs.


**Important**
You can use security lists alone, network security groups alone, or both together. It depends on your particular security needs. 
If you choose to use both security lists and network security groups, the set of rules that applies to a given mount target VNIC is the combination of these items: 
  * The security rules in the security lists associated with the VNIC subnet 
  * The security rules in all NSGs that the VNIC is in 


It doesn't matter which method you use to apply security rules to the mount target VNIC, as long as the ports for protocols necessary for File Storage are correctly configured in the rules applied.
For additional conceptual information, see [Virtual Firewall](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/virtual-firewall.htm#virtual-firewall "On Compute Cloud@Customer, the Networking service offers two virtual firewall features that both use security rules to control traffic at the packet level – security lists and network security groups \(NSGs\). They offer different ways to apply security rules to a set of virtual network interface cards \(VNICs\).").
For instructions on how to create security rules and NSGs for the File Storage service, see [Controlling Access to File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/controlling-access-to-file-storage.htm#controlling-access-to-file-storage "On Compute Cloud@Customer, before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports.").
For general instructions for creating security lists and NSGs, see [Controlling Traffic with Security Lists](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-security-lists.htm#controlling-traffic-with-security-lists "On Compute Cloud@Customer, both security lists and network security groups \(NSGs\) are types of virtual firewalls for your compute instances. Both security lists and NSGs define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
## File Storage Network Ports 🔗 
On Compute Cloud@Customer, when configuring the File Storage service, you might need to know the ports that are used for a service or protocol.
This table lists the port numbers used for networking services that support File Storage.
When you configure security lists and network security groups for the File Storage service, use the port numbers for the particular service you are using. For example, for NFS configure ports 2048–2050 for TCP and UDP.
Service | Protocol | Port  
---|---|---  
RPC |  TCP, UDP |  111  
NFS |  TCP, UDP |  2048, 2049, 2050  
lockd |  TCP, UDP |  4045  
mountd |  TCP, UDP |  20048  
SMB |  TCP, UDP |  445  
LDAP |  TCP, UDP |  389  
Kerberos |  TCP, UDP |  88  
DNS |  TCP, UDP |  53  
## Deleting File System Resources Overview 🔗 
On Compute Cloud@Customer, you can't delete a file system resource that has dependencies. 

File Systems
    
You can delete a file system if it's not a parent file system. If it's a parent file system, all descendant snapshots and clones must first be deleted. 

**Snapshots** 
    
A parent snapshot can't be deleted. A snapshot that isn't a parent can be deleted. 

Clones
    A parent clone can't be deleted. A clone that isn't a parent can be deleted.
Was this article helpful?
YesNo

