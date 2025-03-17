Updated 2023-09-26
# Lower Cost
The **Lower Cost** elastic performance option is recommended for throughput intensive workloads with large sequential I/O, such as streaming, log processing, and data warehouses.
This option gives you linear scaling 2 IOPS/GB upt to a maximum of 3000 IOPS per volume. Throughput scales at 240 KB/s/GB up to the maximum of 480 MB/s per volume.
[![Block Volume Performance slider specifying lower cost performance.](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderlowercost.png)](https://docs.oracle.com/en-us/iaas/Content/Block/Images/perfsliderlowercost.png)
The following table lists the Block Volume service's throughput and IOPS performance numbers based on volume size for this option. IOPS and KB/s performance scales linearly per GB volume size up to the service maximums so you can predictably calculate the performance numbers for a specific volume size. If you're trying to achieve certain performance targets for volumes configured to use the **Lower Cost** elastic performance option you can provision a minimum volume size using this table as a reference.
Volume Size |  Max Throughput (1 MB block size) |  Max Throughput (8 KB block size) |  Max IOPS (4 KB block size)  
---|---|---|---  
50 GB | 12 MB/s | 0.8 MB/s | 100  
100 GB | 24 MB/s | 1.6 MB/s | 200  
200 GB | 48 MB/s | 3.2 MB/s | 400  
300 GB | 72 MB/s | 4.8 MB/s | 600  
400 GB | 96 MB/s | 6.4 MB/s | 800  
500 GB | 120 MB/s | 8 MB/s | 1000  
750 GB | 180 MB/s | 12 MB/s | 1500  
1 TB | 240 MB/s | 16 MB/s | 2000  
1.5 TB - 32 TB | 480 MB/s | 23 MB/s | 3000  
Was this article helpful?
YesNo

