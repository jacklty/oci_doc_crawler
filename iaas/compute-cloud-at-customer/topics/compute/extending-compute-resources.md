Updated 2025-01-27
# Extending Compute Resources
On Compute Cloud@Customer, you can extend storage resources and add more network interfaces.
## Expanding Volumes 🔗 
You can expand the size of block volumes and boot volumes. You can't decrease the size.
You have several options to increase the size of your volumes:
  * Expand an existing volume in place with online resizing.
  * Restore from a volume backup to a larger volume. 
  * Clone an existing volume to a new, larger volume.
  * Expand an existing volume in place with offline resizing.


**Caution**
Before you resize a boot or block volume, create a backup of the volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
After a volume has been resized, the first backup of the resized volume is a full backup.
**Offline Resizing of Block Volumes**
With offline resizing, you detach the volume from a compute instance before you expand the volume size. After the volume is resized and reattached, you need to extend the partition, but you don't need to rescan the disk. 
Whenever you detach and reattach volumes, there are complexities and risks for both Linux-based and Microsoft Windows-based compute instances. For more information.
**Rescanning the Disk for a Block Volume or Boot Volume**
The Block Volume service lets you expand the size of block volumes and boot volumes while they're online and attached to compute instances. 
After the volume is provisioned, you need to run commands to rescan the disk so that the OS recognizes the expanded volume size. You run different rescan commands depending on the OS of the attached compute instance. 
For more information, see [Resizing Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-volumes.htm#resizing-volumes "On Oracle Cloud Infrastructure, the Block Volume service lets you expand the size of block volumes and boot volumes.").
## Adding Another Network Interface 🔗 
You can add additional VNICs to a compute instance. Each additional VNIC can be in a subnet in the same VCN as the primary VNIC, or in a different subnet that's either in the same VCN or a different one.
You might add a VNIC to connect a compute instance to subnets in multiple VCNs. For example, you might set up your own firewall to protect traffic between VCNs, so the compute instance needs to connect to subnets in different VCNs. 
Secondary VNICs are supported for these types of compute instances:
  * **Linux and Oracle Solaris**
  * **Microsoft Windows**


Here are more details about additional VNICs:
  * There's a limit to how many VNICs can be attached to a compute instance, and it varies by shape. See [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
  * VNICs can be added only after the compute instance is launched.
  * VNICs must always be attached to a compute instance and can't be moved. The process of creating an additional VNIC automatically attaches it to the compute instance. The process of detaching a secondary VNIC automatically deletes it. 
  * VNICs are automatically detached and deleted when you delete the compute instance. 
  * The compute instance's bandwidth is fixed regardless of the number of VNICs attached. You can't specify a bandwidth limit for a particular VNIC on a compute instance.
  * Attaching multiple VNICs from the same subnet CIDR block to a compute instance can introduce asymmetric routing, especially on instances using a variant of Linux. If you need this type of configuration, assign multiple private IP addresses to one VNIC, or using policy-based routing.


For more information, see [Configuring VNICs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vnics.htm#configuring-vnics-and-ip-adresses "On Compute Cloud@Customer, the compute nodes have physical network interface cards \(NICs\). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network.").
Was this article helpful?
YesNo

