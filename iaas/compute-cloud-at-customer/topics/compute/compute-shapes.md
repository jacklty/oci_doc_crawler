Updated 2025-02-28
# Compute Shapes
A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.
You choose the shape configuration when you create an instance. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
When you create instances using any of the platform images that are provided with Compute Cloud@Customer, all common workloads can be handled with the VM.PCAStandard.E5.Flex shape. Because it's a flexible shape, it lets you customize the number of OCPUs and the amount of memory for each instance. You can optimize instance performance for a specific workload and ensure that resources are used efficiently.
The GPU VM shapes are optimized for enterprise GPU-accelerated workloads. They can only be used if the Compute Cloud@Customer deployment includes a [GPU expansion rack](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/gpu-expansion.htm#gpu-expansion "To enable GPU-accelerated workloads in the local data center, a Compute Cloud@Customer installation can be expanded with server nodes that have GPUs installed."). Instances created with a GPU shape have direct (passthrough) access to 1-4 physical GPUs. The ratio between GPUs, OCPUs and memory is fixed.
## Generic Flexible Shape 🔗 
The following table lists the number of OCPUs and the amount of memory you can configure using the VM.PCAStandard.E5.Flex Shape.
The number of OCPUs you select determines the maximum VNIC attachments and the network bandwidth for the instance.
VM.PCAStandard.E5.Flex Specification | Possible Values  
---|---  
**Shape name** | VM.PCAStandard.E5.Flex  
**OCPUs, minimum - maximum** | 1 to 96  
**Memory, default** | 10 GB per OCPU  
**Memory, minimum** | 1 GB per OCPU  
**Memory, maximum** | 64 GB per OCPU, up to 960 GB  
**VNICs, maximum** | 
  * **1 OCPU:** 2 VNICs
  * **2 to 24 OCPUs:** 1 VNIC per OCPU
  * **25 to 96:** 24 VNICs

  
**Bandwidth, maximum** | 
  * **1 to 24 OCPUs:** 24.6 Gbps
  * **25 to 40 OCPUs:** 1 Gbps per OCPU
  * **41 to 96 OCPUs:** 40 Gbps

  
The following table illustrates how the properties of the VM.PCAStandard.E5.Flex Shape can be optimized for each individual instance.
Shape Configuration Examples OCPUs Selected | Possible Memory Range (GB) | Maximum VNICs | Maximum Bandwidth (Gbps)  
---|---|---|---  
4 | 4 to 256 | 4 | 24.6  
20 | 20 to 960 | 20 | 24.6  
30 | 30 to 960 | 24 | 30  
96 | 96 to 960 | 24 | 40  
## Dedicated GPU Shapes 🔗 
For GPU-accelerated workloads, you have a choice between these shapes: VM.GPU.L40S.1, VM.GPU.L40S.2,VM.GPU.L40S.3, VM.GPU.L40S.4. To access these dedicated shapes, you must create an instance based on the Oracle Linux 8 or Oracle Linux 9 platform image.
**Note**
No GPU drivers are included in the current Oracle Linux platform images. The instance OS detects the allocated GPUs, but to use them, you need the CUDA Toolkit from the [NVIDIA developer site](https://developer.nvidia.com/cuda-downloads) to install the required drivers.
The large download and local repository installation need a large amount of disk space. The default 50GB boot volume is insufficient on Oracle Linux 9 and only just large enough on Oracle Linux 8. It is highly recommended to increase the boot volume size to at least 60GB, and extend the file system accordingly.
[Installing GPU Drivers in an Oracle Linux 9 Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm)
  1. From the command line of the instance, download and install the CUDA Toolkit rpm for your OS.
```
$ wget https://developer.download.nvidia.com/compute/cuda/12.8.0/local_installers/cuda-repo-rhel9-12-8-local-12.8.0_570.86.10-1.x86_64.rpm
$ sudo rpm -i cuda-repo-rhel9-12-8-local-12.8.0_570.86.10-1.x86_64.rpm
$ sudo dnf clean all
$ sudo dnf install cuda-toolkit-12-8
```

  2. Enable the Oracle Linux 9 EPEL yum repository. Install the `dkms` package.
```
$ sudo yum-config-manager --enable ol9_developer_EPEL
$ sudo dnf install dkms
```

  3. Install the GPU drivers.
```
$ sudo dnf install cuda-12-8
```

  4. Verify the installation with the NVIDIA System Management Interface.
```
$ nvidia-smi
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.86.10       Driver Version: 570.86.10   CUDA Version: 12.8   |
|-----------------------------------------+------------------------+----------------------+
| GPU Name         Persistence-M | Bus-Id     Disp.A | Volatile Uncorr. ECC |
| Fan Temp  Perf     Pwr:Usage/Cap |      Memory-Usage | GPU-Util Compute M. |
|                     |            |        MIG M. |
|=========================================+========================+======================|
|  0 NVIDIA L40S          Off |  00000000:00:05.0 Off |          0 |
| N/A  26C  P8       23W / 350W |    1MiB / 46068MiB |   0%   Default |
|                     |            |         N/A |
+-----------------------------------------+------------------------+----------------------+
+-----------------------------------------------------------------------------------------+
| Processes:                                       |
| GPU  GI  CI       PID  Type  Process name            GPU Memory |
|    ID  ID                                Usage   |
|=========================================================================================|
| No running processes found                               |
+-----------------------------------------------------------------------------------------+
```



[Installing GPU Drivers in an Oracle Linux 8 Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm)
  1. From the command line of the instance, download and install the CUDA Toolkit rpm for your OS.
```
$ wget https://developer.download.nvidia.com/compute/cuda/12.8.0/local_installers/cuda-repo-rhel8-12-8-local-12.8.0_570.86.10-1.x86_64.rpm
$ sudo rpm -i cuda-repo-rhel8-12-8-local-12.8.0_570.86.10-1.x86_64.rpm
$ sudo dnf clean all
$ sudo dnf install cuda-toolkit-12-8
```

  2. Enable the Oracle Linux 8 EPEL yum repository. Install the `dkms` package.
```
$ sudo yum-config-manager --enable ol8_developer_EPEL
$ sudo dnf install dkms
```

  3. Install the GPU drivers.
```
$ sudo dnf install cuda-12-8
```

  4. Install the NVIDIA kernel module.
```
$ sudo scl enable gcc-toolset-13 bash
# dkms install nvidia-open -v 570.86.10
```

If this `make` error appears while the kernel module is built, you can safely ignore it.
```
Cleaning build area...(bad exit status: 2)
Failed command:
make -C /lib/modules/5.15.0-206.153.7.el8uek.x86_64/build M=/var/lib/dkms/nvidia-open/570.86.10/build clean
```

  5. Verify the installation with the NVIDIA System Management Interface.
```
# nvidia-smi
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.86.10       Driver Version: 570.86.10   CUDA Version: 12.8   |
|-----------------------------------------+------------------------+----------------------+
| GPU Name         Persistence-M | Bus-Id     Disp.A | Volatile Uncorr. ECC |
| Fan Temp  Perf     Pwr:Usage/Cap |      Memory-Usage | GPU-Util Compute M. |
|                     |            |        MIG M. |
|=========================================+========================+======================|
|  0 NVIDIA L40S          Off |  00000000:00:05.0 Off |          0 |
| N/A  26C  P8       23W / 350W |    1MiB / 46068MiB |   0%   Default |
|                     |            |         N/A |
+-----------------------------------------+------------------------+----------------------+
+-----------------------------------------------------------------------------------------+
| Processes:                                       |
| GPU  GI  CI       PID  Type  Process name            GPU Memory |
|    ID  ID                                Usage   |
|=========================================================================================|
| No running processes found                               |
+-----------------------------------------------------------------------------------------+
```



VM.GPU.L40S.x Specification | Possible Values  
---|---  
**Shape name** | 
  * VM.GPU.L40S.1
  * VM.GPU.L40S.2
  * VM.GPU.L40S.3
  * VM.GPU.L40S.4

  
**GPUs** | 1-4 – corresponding with the shape name  
**OCPUs** | 27 per GPU  
**Memory** | 200 GB per GPU  
**VNICs** | Up to 24  
**Bandwidth** | Up to 400 Gbps  
Was this article helpful?
YesNo

