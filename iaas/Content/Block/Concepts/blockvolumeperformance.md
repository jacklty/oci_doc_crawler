Updated 2024-07-19
# Block Volume Performance
The Oracle Cloud Infrastructure Block Volume service uses NVMe-based storage infrastructure, designed for consistency, and offers flexible and elastic performance. You only need to provision the capacity needed and performance scales with the performance characteristics of the performance level selected up to the service maximums. 
You don't need to decide on performance needs ahead of creating and attaching block volumes. When you create a volume, by default, it's configured for the **Balanced** performance level. You can change this when create the volume or you can update it at any point after the volume is created. The elastic performance capability of the service lets you to pay for the performance characteristics you require independently from the size of block volumes and boot volumes. If the requirements change, you only need to adjust the performance settings for the volume, you don't need to re-create the volumes.
Block Volume provides dynamic performance scaling with autotuning, see [Dynamic Performance Scaling](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm#autotunevolumeperformance "Block Volume provides dynamic performance scaling with autotuning. This feature enables you to configure your volumes so that the service adjusts the performance level automatically to optimize performance.") for more information.
**Note** You should perform benchmark analysis during proof of concept testing to verify that the environment's configuration has adequate performance for the application's requirements, for more information, see [Metrics and Performance Testing](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance_topic-Metrics_and_Performance_Testing.htm#metrics "Observe performance for the Balanced elastic performance configuration option and learn about the host maximum.").
## Block Volume Performance Levels 🔗 
When you create a volume, you can select the performance level, see [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service."). You can also change the performance level for an existing volume. For more information, see [Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#Changing_the_Performance_of_a_Volume). In the Console, you configure the performance using the slider or the VPU control as shown in the following screenshot. 
[![Block Volume Performance slider](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/perfslideruhp.png)](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/perfslideruhp.png)
The following performance levels are available:
  * **Ultra High Performance** : Recommended for workloads with the highest I/O requirements, requiring the best possible performance. With this option, you can purchase between 30 – 120 VPUs per GB/month. For more information, including specific throughput and IOPS performance numbers for various volume sizes, see [Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance "The Ultra High Performance level is recommended for workloads with the highest I/O requirements, requiring the best possible performance, such as large databases."). 
  * **Higher Performance** : Recommended for workloads with high I/O requirements that don't require the performance of the **Ultra High Performance** level. With this option, you are purchasing 20 VPUs per GB/month. For more information, including specific throughput and IOPS performance numbers for various volume sizes, see [Higher Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumehigherperformance.htm#Higher_Performance "The Higher Performance option is recommended for workloads with high I/O requirements that don't require the performance of the Ultra High Performance level.").
  * **Balanced** : The default performance level for new and existing block and boot volumes, and provides a good balance between performance and cost savings for most workloads. With this option, you are purchasing 10 VPUs per GB/month. For more information, including specific throughput and IOPS performance numbers for various volume sizes, see [Balanced Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebalancedperformance.htm#Balanced_Performance "The Balanced performance level provides a good balance between performance and cost savings for most workloads, including those that perform random I/O such as boot volumes.").
  * **Lower Cost** : Recommended for throughput intensive workloads with large sequential I/O, such as streaming, log processing, and data warehouses. The cost is only the storage cost, there is no additional VPU cost. This option is only available for block volumes, it is not available for boot volumes. For more information, including specific throughput and IOPS performance numbers for various volume sizes, see [Lower Cost](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumelowercost.htm#Lower_Cost "The Lower Cost elastic performance option is recommended for throughput intensive workloads with large sequential I/O, such as streaming, log processing, and data warehouses.").


### Configuring the Performance Level for a Volume 🔗 
You can configure the volume performance level for a block volume when you create a volume, see [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service."). You can also change the volume performance level for an existing block volume, see [To change the volume performance for an existing block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#blockConfig). 
When you create a compute instance, the volume performance level for the instance's boot volume is set to **Balanced** by default. You can change this setting after the instance has launched, see [To change the volume performance for an existing boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#bootConfig).
### Volume Performance Units 🔗 
Block Volume performance includes the concept of volume performance units (VPUs). You can purchase more VPUs to allocate more resources to a volume, increasing IOPS/GB and throughput per GB. You also have the flexibility to purchase fewer VPUs, which reduces the performance characteristics for a volume, however it can also provide cost savings. You can also choose not to purchase any VPUs which can provide significant cost savings for volumes that don't require the increased performance characteristics.
For specific pricing details, see [Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html).
The following table lists the performance characteristics for each performance level, along with the number of VPUs.
Elastic Performance Level |  Volume Performance Units (VPUs) |  IOPS per GB |  Max IOPS per Volume |  Size for Max IOPS (GB) |  KBPS per GB |  Max MBPS per Volume  
---|---|---|---|---|---|---  
Lower Cost | 0 | 2 | 3,000 | 1,500 | 240 | 480  
Balanced | 10 | 60 | 25,000 | 417 | 480 | 480  
Higher Performance | 20 | 75 | 50,000 | 667 | 600 | 680  
Ultra High Performance | 30 | 90 | 75,000 | 833 | 720 | 880  
Ultra High Performance | 40 | 105 | 100,000 | 952 | 840 | 1,080  
Ultra High Performance | 50 | 120  | 125,000 | 1,042 | 960 | 1,280  
Ultra High Performance | 60 | 135 | 150,000 | 1,111 | 1,080 | 1,480  
Ultra High Performance | 70 | 150 | 175,000 | 1,167 | 1,200 | 1,680  
Ultra High Performance | 80 | 165 | 200,000 | 1,212 | 1,320 | 1,880  
Ultra High Performance | 90 | 180 | 225,000 | 1,250 | 1,440 | 2,080  
Ultra High Performance | 100 | 195 | 250,000 | 1,282 | 1,560 | 2,280  
Ultra High Performance | 110 | 210 | 275,000 | 1,310 | 1,680 | 2,480  
Ultra High Performance | 120 | 225 | 300,000 | 1,333 | 1,800 | 2,680  
### Calculating Volume Performance 🔗 
You can calculte the expected performance for a volume, using the following calculations:
  * Starting at 10 VPUs (**Balanced** performance level), for each 10 VPU/GB increment, performance scales as follows: 
    * + 15 IOPS/GB scale
    * + 25K IOPS for Max IOPS/Volume limit limit (up to maximum 300K IOPS for 120 VPU/GB)
    * + 120 KBPS/GB scale
    * + 200 Max MBPS/Volume limit
  * IOPS/GB = 1.5 * VPU/GB + 45
  * Max IOPS/Volume = 2,500 * VPU/GB
  * KBPS/GB = 12 * VPU/GB + 360
  * Max MBPS/Volume = 20 * VPU/GB + 280


## Performance Details for Shapes  🔗 
A shape is a template that specifies the number of OCPUs, amount of memory, and other resources that are allocated to a Compute instance, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm) for more information. An instance's shape impacts the performance of attached volumes. This section provides Block Volume specific details for shapes. 
Multipath-enabled attachments are required for volumes configured for the **Ultra High Performance** level. The shapes that support multipath-enabled attachments are identified with a value of **Yes** in the **Supports Ultra High Performance (UHP)** column.
See [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.") for more information about attaching volumes configured for **Ultra High Performance**.
The instance shapes listed in the following tables are current versions. For performance details of previous versions, see [Performance Details for Previous Generation Instance Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_details_prev_gen_shapes).
### Bare Metal Shapes  🔗 
The following table lists the applicable details for attaching volumes to instances based on bare metal shapes.
**Note** All current bare metal shapes support the **Ultra High Performance** level.
Shape | OCPU | Memory (GB) | Max Network Bandwidth | Max IOPS per Instance | Max Throughput per Instance (Block Volume) | Max Number of Attachments | Supports Ultra High Performance (UHP)  
---|---|---|---|---|---|---|---  
BM.Standard.E5.192 | 192 | 2304 | 1 x 100 Gbps | 1,300,000 | 12 GB/s | 32 | Yes  
BM.Standard.E4.128 | 128 | 2048 | 2 x 50 Gbps | 1,300,000 | 6 GB/s | 32 | Yes  
BM.DenseIO.E4.128 | 128 | 2048 | 2 x 50 Gbps | 1,300,000 | 6 GB/s | 32 | Yes  
BM.Standard3.64 | 64 | 1024 | 2 x 50 Gbps | 1,300,000 | 6 GB/s | 32 | Yes  
BM.Optimized3.36 | 36 | 512 |  2 x 50 Gbps 1 x 100 Gbps RDMA | 1,300,000 | 6 GB/s | 32 | Yes  
BM.GPU.A100-v2.8 | 128 | 640 |  2 x 50 Gbps 16 x 100 Gbps RDMA | 1,300,000 | 6 GB/s | 32 | Yes  
BM.GPU.A10.4 | 64 | 96 | 2 x 50 Gbps | 1,300,000 | 6 GB/s | 32 | Yes  
BM.GPU4.8 | 64 |  GPU: 320 GB CPU: 2048 GB |  1 x 50 Gbps 8 x 200 Gbps RDMA | 1,300,000 | 6 GB/s | 32 | Yes  
BM.Standard.A1.160 | 160 | 2048 | 2 x 50 Gbps | 800,000 | 6 GB/s | 32 | Yes  
BM.GPU3.8 | 52 |  GPU: 128 GB CPU: 768 GB | 2 x 50 Gbps | 625,000 | 3 GB/s | 32 | Yes  
BM.GPU2.2 | 28 |  GPU: 32 GB CPU: 192 GB | 2 x 25 Gbps | 625,000 | 3 GB/s | 32 | Yes  
### VM Shapes for iSCSI and Paravirtualized Attached Volumes 🔗 
The following table lists the applicable details for attaching volumes to instances based on VM shapes using iSCSI and paravirtualized attachments.
Shape | OCPU | Memory (GB) | Max Network Bandwidth | Max IOPS per Instance | Max Throughput per Instance (Block Volume) | Max Number of Attachments | Supports Ultra High Performance (UHP)  
---|---|---|---|---|---|---|---  
VM.Standard.E5.Flex | 1 OCPU minimum, 90 OCPU maximum | 1 GB minimum, 1049 GB maximum | 1 Gbps per OCPU, maximum 40 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.E4.Flex | 1 OCPU minimum, 64 OCPU maximum | 1 GB minimum, 1024 GB maximum | 1 Gbps per OCPU, maximum 40 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) | 32 for iSCSI16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO.E4.Flex | 8 / 16 / 32 | 128 / 256 / 512 | 8 Gbps / 16 Gbps / 32 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard3.Flex | 1 OCPU minimum, 32 OCPU maximum | 1 GB minimum, 512 GB maximum | 1 Gbps per OCPU, maximum 32 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Optimized3.Flex | 1 OCPU minimum, 18 OCPU maximum | 1 GB minimum, 256 GB maximum | 4 Gbps per OCPU, maximum 40 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.A1.Flex | 1 OCPU minimum, 80 OCPU maximum | 1 GB minimum, 1024 GB maximum | 1 Gbps per OCPU, maximum 40 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps (up to 4,800 MB/s) |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.GPU.A10.2 | 30 |  GPU: 48 GB CPU: 480 GB | 48 Gbps | 600,000 | 5,760 MB/s | 32 |  Yes  
VM.GPU.A10.1 | 15 |  GPU: 24 GB CPU: 240 GB | 24 Gbps | 480,000 | 2,880 MB/s | 32 |  No  
VM.GPU3.4 | 24 |  GPU: 64 GB CPU: 360 GB | 24.6 Gbps | 480,000 | 2,880 MB/s | 32 |  Yes  
VM.GPU3.2 | 12 |  GPU: 32 GB CPU: 180 GB | 8 Gbps | 160,000 | 960 MB/s | 32 |  No  
VM.GPU2.1 | 12 |  GPU: 16 GB CPU: 72 GB | 8 Gbps | 160,000 | 960 MB/s | 32 |  No  
VM.GPU3.1 | 6 |  GPU: 16 GB CPU: 90 GB | 4 Gbps | 80,000 | 480 MB/s | 32 |  No  
VM.Standard.E2.1.Micro | 1 | 1 | 480 Mbps | 6,000 | 60 MB/s | 32 | No  
## Block Volume Performance SLA 🔗 
The Block performance numbers outlined in this topic apply to **Section 3.6** (Oracle Cloud Infrastructure - Block Volume subsection) of the [Oracle PaaS and IaaS Public Cloud Services Pillar Document](https://www.oracle.com/contracts/docs/paas_iaas_pub_cld_srvs_pillar_4021422.pdf?download=false). 
## Performance Details for Previous Generation Instance Shapes 🔗 
The instance shapes listed in the following tables are previous generation shapes. See [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details) for a list of current instance shapes and their corresponding performance details.
See [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.") for more information about attaching volumes configured for **Ultra High Performance**.
For general information and additional details about compute instance shapes, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
### Previous Generation Bare Metal Shapes  🔗 
The following table lists the applicable details for attaching volumes to instances based on previous generation bare metal shapes.
**Note** All current bare metal shapes support the **Ultra High Performance** level.
Shape | OCPU | Memory (GB) | Max Network Bandwidth | Max IOPS per Instance | Max Throughput per Instance (Block Volume) | Max Number of Attachments | Supports Ultra High Performance (UHP)  
---|---|---|---|---|---|---|---  
BM.Standard.E3.128 | 128 | 2048 | 2 x 50 Gbps | 1,300,000 | 6 GB/s | 32 | Yes  
BM.Standard.E2.64 | 64 | 512 | 2 x 25 Gbps | 625,000 | 3 GB/s | 32 | Yes  
BM.Standard2.52 | 52 | 768 | 2 x 25 Gbps | 625,000 | 3 GB/s | 32 | Yes  
BM.DenseIO2.52 | 52 | 768 | 2 x 25 Gbps | 625,000 | 3 GB/s | 32 | Yes  
BM.HPC2.36 | 36 | 384 |  1 x 25 Gbps 1 x 100 Gbps RDMA | 625,000 | 3 GB/s | 32 | Yes  
BM.Standard.B1.44  | 44 | 512 | 1 x 25 Gbps | 625,000 | 3 GB/s | 32 | Yes  
BM.Standard1.36 | 36 | 256 | 1 x 10 Gbps | 300,000 | 1.2 GB/s | 32 | Yes  
BM.DenseIO1.36 | 36 | 512 | 1 x 10 Gbps | 300,000 | 1.2 GB/s | 32 | Yes  
### Previous Generation VM Shapes for iSCSI and Paravirtualized Attached Volumes 🔗 
The following table lists the applicable details for attaching volumes to instances based on previous generation VM shapes using iSCSI and paravirtualized attachments.
Shape | OCPU | Memory (GB) | Max Network Bandwidth | Max IOPS per Instance | Max Throughput per Instance (Block Volume) | Max Number of Attachments | Supports Ultra High Performance (UHP)  
---|---|---|---|---|---|---|---  
VM.Standard.E3.Flex | 1 OCPU minimum, 64 OCPU maximum | 1 GB minimum, 1024 GB maximum | 1 Gbps per OCPU, maximum 40 Gbps | 20,000 * max network bandwidth in Gbps (up to 600,000) | 120 MB/s * max network bandwidth in Gbps |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO2.24 | 24 | 320 | 24.6 Gbps | 480,000 | 2,880 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO2.16 | 16 | 240 | 16.4 Gbps | 320,000 | 1,920 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO2.8 | 8 | 120 | 8.2 Gbps | 160,000 | 960 MB/s |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.24 | 24 | 320 | 24.6 Gbps | 480,000 | 2,880 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.16 | 16 | 240 | 16.4 Gbps | 320,000 | 1,920 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.8 | 8 | 120 | 8.2 Gbps | 160,000 | 960 MB/s |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.4 | 4 | 60 | 4.1 Gbps | 80,000 | 480 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.2 | 2 | 30 | 2 Gbps | 50,000 | 240 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard2.1 | 1 | 15 | 1 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.E2.8 | 8 | 64 | 5.6 Gbps | 80,000 | 480 MB/s |  32 for iSCSI 16 for Paravirtualized |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.E2.4 | 4 | 32 | 2.8 Gbps | 50,000 | 240 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.E2.2 | 2 | 16 | 1.4 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.E2.1 | 1 | 8 | 700 Mbps | 12,500 | 60 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO1.16 | 16 | 240 | 4.8 Gbps | 80,000 | 480 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO1.8 | 8 | 120 | 2.4 Gbps | 50,000 | 240 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.DenseIO1.4 | 4 | 60 | 1.2 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.B1.16 | 16 | 192 | 9.6 Gbps | 160,000 | 960 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.B1.8 | 8 | 96 | 4.8 Gbps | 80,000 | 480 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.B1.4 | 4 | 48 | 2.4 Gbps | 50,000 | 240 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.B1.2 | 2 | 24 | 1.2 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard.B1.1 | 1 | 12 | 600 Mbps | 12,500 | 60 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard1.16 | 16 | 112 | 4.8 Gbps | 80,000 | 480 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard1.8 | 8 | 56 | 2.4 Gbps | 50,000 | 240 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard1.4 | 4 | 28 | 1.2 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard1.2 | 2 | 14 | 1.2 Gbps | 25,000 | 120 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
VM.Standard1.1 | 1 | 7 | 600 Mbps | 12,500 | 60 MB/s | 32 |  Yes (≥16 OCPUs) No (<16 OCPUs)  
## Performance Limitations and Considerations 🔗 
  * Block Volume performance SLA for IOPS per volume applies to the **Balanced** , **Higher Performance** , and **Ultra High Performance** levels only, not the **Lower Cost** level.
  * The performance results described in this topic are for unformatted data volumes. Performance could be lower based on the file system used.
  * Throughput performance results are for bare metal compute instances. Throughput performance on virtual machine (VM) compute instances depends on the network bandwidth that's available to the instance, and further limited by that bandwidth for the volume. For details about the network bandwidth available for VM shapes, see the **Network Bandwidth** column in the [VM Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vmshapes) table.
  * An instance's performance characteristics affect an attached volume's effective IOPS and throughput. For information about the performance characteristics for instance shapes, see [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details).
  * Block Volume performance SLA for IOPS per volume and IOPS per instance applies to raw, unformatted volumes, with iSCSI volume attachments and to paravirtualized volume attachments for 16 core or higher VMs for **Ultra High Performance** , and for 8 cores or higher VMs for **Balanced** and **Higher Performance** , at the Block Volume service level.
  * For the **Lower Cost** option, you might not see the same latency performance that you see with the other performance levels. You might also see a greater variance in latency with the **Lower Cost** option.
  * Third-party security tools for Compute instances that perform disk I/O operations can have a significant negative impact on performance. The IOPS performance characteristics described in this topic are valid for Compute instances with no security tools running on the instance.
  * Windows Defender Advanced Threat Protection (Windows Defender ATP) is enabled by default on all Windows platform images. This tool has a significant negative impact on disk I/O performance. The IOPS performance characteristics described in this topic are valid for Windows instances with Windows Defender ATP disabled for disk I/O. Customers must carefully consider the security implications of disabling Windows Defender ATP. See [Windows Defender Advanced Threat Protection](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-atp/windows-defender-advanced-threat-protection).
  * Block volume performance is per volume, so when a block volume is attached to multiple instances, the performance is shared across all the attached instances. See [Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm#Attaching_a_Volume_to_Multiple_Instances "The Oracle Cloud Infrastructure Block Volume service provides the capability to attach a block volume to multiple compute instances.").
  * Performance is lower for attachments with in-transit encryption enabled.


Was this article helpful?
YesNo

