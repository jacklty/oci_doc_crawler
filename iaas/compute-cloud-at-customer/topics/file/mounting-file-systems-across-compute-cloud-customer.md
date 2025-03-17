Updated 2023-08-15
# Mounting File Systems Across Compute Cloud@Customer Infrastructures
You can create a file system on one Compute Cloud@Customer infrastructure, and mount the file system from an instance that's on another infrastructure. To achieve this scenario, you must configure certain network parameters on each infrastructure. 
**Restriction**
The Compute Cloud@Customer infrastructure hosting the file system and the instance on the remote infrastructure that mounts the file system can't have overlapping VCN CIDR blocks.
**On the Infrastructure Hosting the File System**
  1. Configure these network parameters:
    1. Create a Dynamic Routing Gateway (DRG).
See [Creating a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm#creating-a-dynamic-routing-gateway "On Compute Cloud@Customer, a DRG is the equivalent of a general purpose router. A DRG is used to connect a VCN to the data center's IP address space. The router is configured separately from the VCNs, at the compartment level and is not required to be in the same compartment as the VCN \(but it typically is\).").
    2. For the VCN subnet that will be used by the mount target, attach the VCN to the DRG.
See [Attaching VCNs to a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm#attaching-vcns-to-a-dynamic-routing-gateway "On Compute Cloud@Customer, you can connect many VCNs to a DRG, but each VCN can have only one DRG attached. Ensure that the route tables and security lists allow communication.").
    3. For the VCN subnet, add a route rule with the DRG as the target, and assign a destination CIDR that matches the remote infrastructure VCN CIDR. 
For example, if the remote instance that will mount the file system has a VCN with a 10.11.0.0/16 CIDR, the set the route rule destination CIDR to 10.11.0.0/16.
**Important**
Don’t specify 0.0.0.0/0 as the destination. Doing so causes serious internal network issues.
**Note**
This route rule configuration is only required for mounting file systems across Oracle Compute Cloud@Customer racks. This configuration isn't required for file system mounts within the same rack.
See [Working with Route Tables](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-route-tables.htm#working-with-route-tables "On Compute Cloud@Customer,").
  2. Create a mount target. See [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.").
  3. Create a file system. See [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.").
  4. Create an export that exports to both the source and remote VCN CIDR.
The export CIDR must be big enough to cover both VCN subnet CIDRs. For example, if the host VCN CIDR is 10.10.0.0/16, and the remote instance VCN is 10.11.0.0/16, you can configure the export to use 10.10.0.0/15. This requirement only applies to the Oracle Compute Cloud@Customer hosting the file system.
See [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").


**On the Remote Infrastructure**
  1. Configure these network parameters:
    1. Create a Dynamic Routing Gateway (DRG).
See [Creating a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm#creating-a-dynamic-routing-gateway "On Compute Cloud@Customer, a DRG is the equivalent of a general purpose router. A DRG is used to connect a VCN to the data center's IP address space. The router is configured separately from the VCNs, at the compartment level and is not required to be in the same compartment as the VCN \(but it typically is\).").
    2. For the VCN subnet, attach the VCN to the DRG.
See [Attaching VCNs to a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm#attaching-vcns-to-a-dynamic-routing-gateway "On Compute Cloud@Customer, you can connect many VCNs to a DRG, but each VCN can have only one DRG attached. Ensure that the route tables and security lists allow communication.").
    3. For the VCN subnet, add a route rule with the DRG as the target, and assign a destination CIDR that matches the host VCN CIDR.
For example, if the host mount target has a VCN 10.0.0.0/16 CIDR, set the route rule destination CIDR to 10.0.0.0/16.
**Important**
Don’t specify 0.0.0.0/0 as the destination. Doing so causes serious internal network issues.
**Note**
This route rule configuration is only required for mounting file systems across Oracle Compute Cloud@Customer racks. not required for file system mounts within the same Compute Cloud@Customer rack.
See [Working with Route Tables](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-route-tables.htm#working-with-route-tables "On Compute Cloud@Customer,").
  2. Log in to the instance and mount the file system.
See:
     * [Mounting File Systems on UNIX-based Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-uxix-based-instances.htm#mounting-file-systems-on-uxix-based-instances "On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.")
     * [Mounting File Systems on Microsoft Windows Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-microsoft-windows-instances.htm#mounting-file-systems-on-microsoft-windows-instances "On Compute Cloud@Customer, you can make file systems available to Microsoft Windows instances by mapping a network drive to the mount target IP address and export path provided by the File Storage service. You can accomplish this task using NFS or SMB protocols.")


Was this article helpful?
YesNo

