Updated 2025-02-28
# GPU Expansion
To enable GPU-accelerated workloads in the local data center, a Compute Cloud@Customer installation can be expanded with server nodes that have GPUs installed.
GPU nodes are delivered in an expansion rack containing power distribution units (PDUs) and networking components to integrate the additional physical resources with the base rack. A GPU expansion rack contains at least 1 and a maximum of 6 factory-installed GPU nodes. More nodes can be installed after initial deployment. Up to two expansion racks can be connected to a base rack, for a maximum of 12 GPU nodes.
A GPU node is a 3 RU server with Intel Xeon Platinum 8480+ architecture, high-speed Ethernet connectivity, and four NVIDIA L40S GPUs with 48GB GDDR6 memory and 1466 peak FP8 TFLOPS. After these nodes have been fully provisioned, their use is seamless: when launching a new compute instance, users select a dedicated [compute shape](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.") to allocate one or more GPUs to the instance.
For detailed component specifications, refer to the manufacturer website.
  * [Intel Xeon Platinum 8480+ Processor specifications](https://www.intel.com/content/www/us/en/products/sku/231746/intel-xeon-platinum-8480-processor-105m-cache-2-00-ghz/specifications.html)
  * [NVIDIA L40S GPU data sheet](https://resources.nvidia.com/en-us-l40s/l40s-datasheet-28413?ncid=no-ncid)


Oracle Compute Cloud@Customer with GPU expansion provides a scalable platform to build AI and graphics intensive applications at the edge. It's built to power the next generation of data center workloads, including: 
  * Generative AI inference: real time inferencing for multimodel generative AI pipelines (text, image, audio, video)
  * LLM training and fine-tuning: accelerated performance for fine-tuning medium LLMs and training small LLMs with NVIDIA's transformer engine and FP8 support
  * Graphics-intensive and VDI applications: 3D graphics and rendering workflows with NVIDIA’s RTX and ray tracing capabilities
  * Digital twins using NVIDIA Omniverse: develop and operate complex 3D industrial digitization workflows
  * Media streaming: increased encode/decode density and AV1 support for 4K video streaming
  * HPC: scientific data analysis and simulation workloads with FP32 support


## Installation Requirements 🔗  

Site Preparation
    
If you have decided to expand your Compute Cloud@Customer environment with GPU nodes, carefully plan ahead for the installation of the additional hardware. The GPU expansion rack has the same external dimensions as the base rack, and contains the same type of hardware. Therefore, the base rack site requirements also apply for the expansion rack. They are described in detail in the installation section [Preparing Your Site](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-site.htm#prepare-your-site "Use the information in this section to learn about site requirements before the arrival of Oracle Compute Cloud@Customer."). 

Rack Cabling
    
The cable connections between the base rack and the GPU expansion rack must not exceed 25 meters. Allocate a space for the expansion rack near the base rack, ensuring that the inter-rack cabling is within the specified maximum length when routed through the floor or ceiling. The required cable length must be specified with the order. 

High-Performance Storage
    
The GPU compute shapes are optimized for high speed and low latency. They use high-performance storage exclusively, meaning the system's ZFS Storage Appliance must provide a high performance storage pool consisting of one or more _performance_ disk trays. In case no performance tray is present in the existing installation, one is added to the GPU expansion order. If the base rack has no rack units available to add the performance tray, it will be installed in a storage expansion rack. The high performance storage pool must be configured before the GPU expansion rack is activated.
## Installation Process 🔗  

Physical Installation
    
All installation tasks are performed by Oracle. When the GPU expansion rack is in its allocated space, it must be connected to the base rack. The expansion rack leaf switches are cross-connected to the base rack spine switches to extend the data network into the expansion rack. Similarly, the expansion rack components are added to the internal management network through a cable connection between the management switches of both racks. The ports required for this setup have been reserved on all connected switches. The GPU nodes are internally connected to the expansion rack switches at the factory. 

Rack Activation
    
When the physical connections are in place, the expansion rack is activated by running a script from one of the management nodes. The script powers on the switches and enables the required ports so the new hardware components can be detected and registered. When the script is finished, the data and management networks are operational across the interconnected racks. The system proceeds with the installation and configuration of the operating system and additional software on the new nodes, preparing them for provisioning. When the GPU nodes have been provisioned, they are fully integrated and ready to use.
GPU nodes are added to the existing fault domains alongside other compute nodes, but server families operate separately from each other and migrations between them are not supported. The fault domains might become unbalanced because, unlike standard compute nodes, GPU nodes can be added one by one.
Was this article helpful?
YesNo

