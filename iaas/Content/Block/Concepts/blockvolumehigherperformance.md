Updated 2024-05-30
# Higher Performance
The **Higher Performance** option is recommended for workloads with high I/O requirements that don't require the performance of the **Ultra High Performance** level.
This option provides a linear performance scale of 75 IOPS/GB up to a maximum of 50,000 IOPS per volume. Throughput scales at the rate 600 KB/s/GB up to a maximum of 680 MB/s per volume.
[![Block Volume Performance slider specifying higher performance.](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderhigher.png)](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderhigher.png)
See [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details) for performance characteristics and instance details for Compute shapes.
## Volume Size and Performance 🔗 
The following table lists the Block Volume service's throughput and IOPS performance numbers based on volume size for this option. IOPS and KB/s performance scales linearly per GB volume size up to the service maximums so you can predictably calculate the performance numbers for a specific volume size. If you're trying to achieve certain performance targets for volumes configured to use the **Higher Performance** level, you can provision a minimum volume size using this table as a reference.
**Note** [Bare metal instances](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm) that use in-transit encryption will see a maximum throughput of 540 MB/s at the **Higher Performance** level. 
Volume Size |  Max Throughput (1 MB block size) |  Max Throughput (8 KB block size) |  Max IOPS (4 KB block size)  
---|---|---|---  
50 GB | 30 MB/s | 30 MB/s | 3,750  
100 GB | 60 MB/s | 60 MB/s | 7,500  
200 GB | 120 MB/s | 120 MB/s | 15,000  
400 GB | 240 MB/s | 240 MB/s | 30,000  
600 GB | 360 MB/s | 360 MB/s | 45,000  
700 GB | 420 MB/s | 420 MB/s | 50,000  
800 GB | 480 MB/s | 480 MB/s | 50,000  
1,024 GB | 614 MB/s | 614 MB/s | 50,000  
1,200 GB - 32 TB | 680 MB/s | 680 MB/s | 50,000  
## Adjusting iSCSI Queue Depth for Higher Performance Volumes 🔗 
**Note** The information in this section only applies to volumes attached to Linux instances. You do not need to make any adjustments to the iSCSI queue depth configuration to achieve higher performance for volumes attached to Windows instances.
When you configure the performance of an iSCSI-attached volume to the **Higher Performance** level from either the **Balanced** or **Lower Cost** performance levels, you need to adjust the iSCSI queue depth to achieve the performance maximum of 50,000 IOPS. The steps required to complete this depend on whether you are configuring the performance for a new volume attachment or an existing volume attachment. 
[To adjust the queue depth for a new block volume attachment to an instance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumehigherperformance.htm)
Update `/etc/iscsi/iscsid.conf` to change the `node.session.queue_depth` from 32 to 128, as follows: 
```
node.session.queue_depth = 128
```

[To adjust the queue depth for an existing volume attachment to an instance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumehigherperformance.htm)
  1. Run the following command to update the queue depth for the volume's iSCSI to 128:
```
iscsiadm -m node -T iqn.2015-12.com.oracleiaas:<IQN> -p <volume_IP> -o update -n node.session.queue_depth -v 128
```

  2. Run the following command to log out the iSCSI node:
```
iscsiadm -m node -T iqn.2015-12.com.oracleiaas:<IQN> -p <volume_IP> -u
```

  3. Run the following command to log the iSCSI node:
```
iscsiadm -m node -T iqn.2015-12.com.oracleiaas:<IQN> -p <volume_IP> -l
```

  4. Reboot the instance.


Was this article helpful?
YesNo

