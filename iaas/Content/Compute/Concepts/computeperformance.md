Updated 2024-06-03
# Compute NVMe Performance
The content in the sections below apply to **Section 3.6** of the [Oracle PaaS and IaaS Public Cloud Services Pillar documentation](https://www.oracle.com/contracts/docs/paas_iaas_pub_cld_srvs_pillar_4021422.pdf?download=false).
Oracle Cloud Infrastructure provides a variety of instance configurations in both bare metal and virtual machine (VM) shapes. Each shape varies on multiple dimensions including memory, CPU cores, network bandwidth, and the option of local NVMe SSD storage found in DenseIO and HPC shapes.
Oracle Cloud Infrastructure provides a service-level agreement (SLA) for NVMe performance. Measuring performance is complex and open to variability.
An NVMe drive also has non-uniform drive performance over the period of drive usage. An NVMe drive performs differently when tested brand new compared to when tested in a steady state after some duration of usage. New drives have not incurred many write/erase cycles and the inline garbage collection has not had a significant impact on IOPS performance. To achieve the goal of reproducibility and reduced variability, our testing focuses on the steady state duration of the NVMe drive's operation.
## Performance Benchmarks 🔗 
The following table lists the minimum IOPS for the specified shape to meet the SLA. The results are generated running [FIO benchmark](https://fio.readthedocs.io/en/latest/fio_doc.html) with 4k block sizes for 100% random write tests.
Shape |  Minimum Supported IOPS  
---|---  
VM.DenseIO1.4 | 113k  
VM.DenseIO1.8 | 227k  
VM.DenseIO1.16 | 455k  
BM.DenseIO1.36 | 1.05MM  
VM.DenseIO2.8 | 206k  
VM.DenseIO2.16 | 420k  
VM.DenseIO2.24 | 843k  
BM.DenseIO2.52 | 1.67MM  
VM.DenseIO.E4.Flex with 8 OCPUs | 230k  
VM.DenseIO.E4.Flex with 16 OCPUs | 460k  
VM.DenseIO.E4.Flex with 32 OCPUs | 920k  
BM.DenseIO.E4.128 | 1.88MM  
BM.HPC2.36 | 216k  
BM.Optimized3.36 | 135k  
VM.DenseIO.E5.Flex with 8 OCPUs | 290K  
VM.DenseIO.E5.Flex with 16 OCPUs | 580K  
VM.DenseIO.E5.Flex with 24 OCPUs | 870K  
VM.DenseIO.E5.Flex with 32 OCPUs | 1160K  
VM.DenseIO.E5.Flex with 40 OCPUs | 1450K  
VM.DenseIO.E5.Flex with 48 OCPUs | 1740K  
BM.DenseIO.E5.128 | 3.4MM  
Although the NVMe drives are capable of higher IOPS, Oracle Cloud Infrastructure currently guarantees this minimum level of IOPS performance.
## Frequently Asked Questions 🔗 
[I suspect a slowdown in my NVMe drive performance. Is there a SLA violation? ](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeperformance.htm)
We test hosts on a regular basis to ensure that are our low-level software updates do not regress performance. If you have reproduced the testing methodology and your drive's performance does not meet the terms in the SLA, please contact your Oracle sales team.
[Why does the FIO benchmark not represent a diversity of IO workloads such as random reads and writes to reflect real world IO?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeperformance.htm)
We focused on reproducibility and we believe the tests provide a significant indicator of overall drive performance. 
[Will Oracle Cloud Infrastructure change the tests in this document?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeperformance.htm)
We will make changes to provide greater customer value through better guarantees and improved reproducibility.
Was this article helpful?
YesNo

