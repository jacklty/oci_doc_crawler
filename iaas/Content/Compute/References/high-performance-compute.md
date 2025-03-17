Updated 2023-11-20
# High Performance Computing
High Performance Computing (HPC) performs complex calculations and processes data faster than traditional Compute. HPC uses bare metal servers, ultralow latency cluster networking, high-performance storage options, and parallel file systems. This infrastructure enables parallel processing for compute-intensive workloads such as artificial intelligence, deep learning, data analysis, scientific simulations, and any other highly intensive workload.
## Getting Started with High Performance Computing 🔗 
You can create a single-node HPC instance with the standard instance creation workflow. If you want to use multiple HPC instances in a RDMA network group, you can create them through a [Cluster Networks with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#top) or [Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters).
## Using RDMA Cluster Networks 🔗 
Remote Direct Memory Access (RDMA) cluster networks are groups of high performance computing (HPC), GPU, or optimized instances that are connected with a high-bandwidth, ultra low-latency network. Each node in the cluster is a bare metal machine located in close physical proximity to the other nodes. A remote direct memory access (RDMA) network between nodes provides latency as low as single-digit microseconds, comparable to on-premises HPC clusters.
Cluster networks are designed for highly demanding parallel computing workloads. For example:
  * Computational fluid dynamics simulations for automotive or aerospace modeling
  * Financial modeling and risk analysis
  * Biomedical simulations
  * Trajectory analysis and design for space exploration
  * Artificial intelligence and big data workloads


Oracle Cloud Infrastructure offers two types of cluster networks. In both cases, the networks are groups of bare metal instances that are connected with an ultra low latency network.
  * [Cluster networks with instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#top) let you use instance pools to manage groups of identical instances in the RDMA network group. If you want predictable capacity for a specific number of identical instances that are managed as a group, use cluster networks with instance pools.
  * [Compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters) let you manage instances in the cluster individually. When you create a compute cluster, you create an empty RDMA network group. After the group is created, you can add instances to the group, or delete instances from the group. If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, use compute clusters.


## Oracle Cloud Agent Plugins for HPC 🔗 
Oracle Cloud Infrastructure offers a cloud agent plugin specific for HPC bare metal instances to simplify the configuration and authentication of HPC networks, and provide specialized monitoring for high performance computing.
The HPC plugin is available for HPC in all commercial regions. 
Supported shapes and images for HPC Shape | Supported Images | Default Setting  
---|---|---  
BM.GPU.A10.4 | Ubuntu 20.04+, OL7, OL8, CentOS 7+ | Recommended on OCA 1.37.0 or above  
BM.GPU.A100 | Ubuntu 20.04+, OL7, OL8, CentOS 7+ | Recommended on OCA 1.37.0 or above  
BM.GPU.H100.8 | Ubuntu 20.04+, OL7, OL8 | Enabled on OCA 1.37.0 or above  
BM.GPU4.8 | Ubuntu 20.04+, OL7, OL8, CentOS 7+ | Recommended on OCA 1.37.0 or above  
BM.HPC2.36 | Ubuntu 20.04+, OL7, OL8, CentOS 7+ | Recommended on OCA 1.37.0 or above  
BM.Optimized3.36 | Ubuntu 20.04+, OL7, OL8 | Enabled on OCA 1.37.0 or above  
The sub-modules of the HPC plugin can be individually enabled or disabled:
  * **Auto Configuration**
    * Applies recommended network adapter settings on GPU shapes
    * Applies recommended Mellanox Connect-X settings on GPU shapes
    * Assigns IP addresses to RDMA network interfaces based on the primary VCN
  * **RDMA Authentication/Configuration**
    * Configures RDMA network interfaces with recommended QoS and MTU
    * Configures and maintains required RDMA network authentication
  * **GPU & RDMA Monitoring**
    * Emits additional RDMA and GPU performance metrics


To enable the HPC plugin on an existing bare metal instance, you must create or migrate the existing instance to Oracle Cloud Agent 1.35.0 or above. See [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins) for more information. 
### Enabling GPU and RDMA Metrics
When you install the Oracle Cloud Agent and enable the HPC monitoring plugin, the GPU and RDMA metrics are automatically enabled. OCI sends the metrics to the customer namespace and bills them against the tenancy.
To determine if these metrics will result in additional charges, see [metering pricing](https://www.oracle.com/cloud/price-list/#pricing-observability).
For a detailed list of HPC metrics, see [Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics).
Was this article helpful?
YesNo

