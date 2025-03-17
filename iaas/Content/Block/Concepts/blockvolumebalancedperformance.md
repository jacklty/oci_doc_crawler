Updated 2024-05-30
# Balanced Performance
The **Balanced** performance level provides a good balance between performance and cost savings for most workloads, including those that perform random I/O such as boot volumes.
This option provides linear peformance scaling with 60 IOPS/GB up to 25,000 IOPS per volume. Throughput scales at 480 KB/s/GB up to a maximum of 480 MB/s per volume.
[![Block Volume Performance slider specifying balanced performance.](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderbalanced.png)](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderbalanced.png)
See [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details) for performance characteristics and instance details for Compute shapes.
## Volume Size and Performance 🔗 
The following table lists the Block Volume service's throughput and IOPS performance numbers based on volume size for this option. IOPS and KB/s performance scales linearly per GB volume size up to the service maximums so you can predictably calculate the performance numbers for a specific volume size. If you're trying to achieve certain performance targets for volumes configured to use the **Balanced** performance level you can provision a minimum volume size using this table as a reference.
Volume Size |  Max Throughput (1 MB block size) |  Max Throughput (8 KB block size) |  Max IOPS (4 KB block size)  
---|---|---|---  
50 GB | 24 MB/s | 24 MB/s | 3000  
100 GB | 48 MB/s | 48 MB/s | 6000  
200 GB | 96 MB/s | 96 MB/s | 12,000  
300 GB | 144 MB/s | 144 MB/s | 18,000  
400 GB | 192 MB/s | 192 MB/s | 24,000  
500 GB | 240 MB/s | 200 MB/s | 25,000  
750 GB | 360 MB/s | 200 MB/s | 25,000  
1 TB - 32 TB | 480 MB/s | 200 MB/s | 25,000  
Was this article helpful?
YesNo

