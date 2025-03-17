Updated 2024-09-19
# Compute Quotas
Compute quota details for instances, capacity reservations, custom images, instance configurations, instance pools, cluster networks, and autoscaling.
[Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm)
Quotas for compute instances are available by core (OCPU) or GPU, by the amount of memory (GB), and by shape. Available quotas depend on the shape.
**Important** For shapes that support container instances, quotas are shared between Compute resources and Container Instances resources.
### Core- and GPU-Based Quotas
Family name: `compute-core`
Name | Scope | Description  
---|---|---  
standard1-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.Standard1 and BM.Standard1 series  
standard-b1-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.Standard.B1 and BM.Standard.B1 series  
standard2-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.Standard2 and BM.Standard2 series  
standard3-core-count | Availability domain | Total number of OCPUs for shapes in the VM.Standard3 and BM.Standard3 series  
standard-e2-micro-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.Standard.E2.1.Micro series  
standard-e2-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.Standard.E2 and BM.Standard.E2 series  
standard-e3-core-ad-count | Availability domain  |  Total number of OCPUs for Compute instances created using shapes in the VM.Standard.E3 and BM.Standard.E3 series and container instances created using the CI.Standard.E3.Flex shape **Note:** This quota applies to both Compute and Container Instances resources. See [Container Instances Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-container-instances.htm#container-instances "Container Instances quota details.").  
standard-e4-core-count | Availability domain  |  Total number of OCPUs for Compute instances created using shapes in the VM.Standard.E4 and BM.Standard.E4 series and container instances created using the CI.Standard.E4.Flex shape **Note:** This quota applies to both Compute and Container Instances resources. See [Container Instances Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-container-instances.htm#container-instances "Container Instances quota details.").  
standard-a1-core-count | Availability domain | Total number of OCPUs for shapes in the VM.Standard.A1 and BM.Standard.A1 series  
dense-io1-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.DenseIO1 and BM.DenseIO1 series  
dense-io2-core-count | Availability domain  | Total number of OCPUs for shapes in the VM.DenseIO2 and BM.DenseIO2 series  
dense-io-e4-core-count | Availability domain | Total number of OCPUs for shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series  
gpu2-count | Availability domain  | Total number of GPUs for shapes in the VM.GPU2 and BM.GPU2 series  
gpu3-count | Availability domain  | Total number of GPUs for shapes in the VM.GPU3 and BM.GPU3 series  
gpu4-count | Availability domain  | Total number of GPUs for shapes in the BM.GPU4 series  
gpu-a10-count | Availability domain  | Total number of GPUs for shapes in the VM.GPU.A10 and BM.GPU.A10 series  
gpu-a100-v2-count | Availability domain  | Total number of GPUs for shapes in the BM.GPU.A100 series  
hpc2-core-count | Availability domain  | Total number of OCPUs for shapes in the BM.HPC2 series  
optimized3-core-count | Availability domain | Total number of OCPUs for shapes in the VM.Optimized3 and BM.Optimized3 series  
dvh-standard2-core-count | Availability domain  | Total number of OCPUs for DVH.Standard2.52 shapes  
dvh-standard-e2-core-count | Availability domain | Total number of OCPUs for DVH.Standard.E2.64 shapes  
dvh-standard-e3-core-count | Availability domain | Total number of OCPUs for DVH.Standard.E3.128 shapes  
dvh-standard-e4-core-count | Availability domain | Total number of OCPUs for DVH.Standard.E4.128 shapes  
dvh-standard-e5-core-count | Availability domain | Total number of OCPUs for DVH.Standard.E5.192 shapes  
dvh-dense-io2-core-count | Availability domain | Total number of OCPUs for DVH.DenseIO2.52 shapes  
### Example
Copy
```
set compute-core quota standard3-core-count to 480 in compartment MyCompartment
```

### Memory-Based Quotas
Family name: `compute-memory`
Name | Scope | Description  
---|---|---  
standard3-memory-count | Availability domain | Total amount of memory for shapes in the VM.Standard3 and BM.Standard3 series, in GB  
standard-e3-memory-count | Availability domain  |  Total amount of memory for Compute instances created using shapes in the VM.Standard.E3 and BM.Standard.E3 series and container instances created using the CI.Standard.E3.Flex shape, in GB **Note:** This quota applies to both Compute and Container Instances resources. See [Container Instances Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-container-instances.htm#container-instances "Container Instances quota details.").  
standard-e4-memory-count | Availability domain  |  Total amount of memory for Compute instances created using shapes in the VM.Standard.E4 and BM.Standard.E4 series and container instances created using the CI.Standard.E4.Flex shape, in GB **Note:** This quota applies to both Compute and Container Instances resources. See [Container Instances Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-container-instances.htm#container-instances "Container Instances quota details.").  
standard-a1-memory-count | Availability domain | Total amount of memory for shapes in the VM.Standard.A1 and BM.Standard.A1 series, in GB  
dense-io-e4-memory-count | Availability domain | Total amount of memory for shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series, in GB  
optimized3-memory-count | Availability domain | Total amount of memory for shapes in the VM.Optimized3 and BM.Optimized3 series, in GB  
### Example
Copy
```
set compute-memory quota standard-e4-memory-count to 120 in compartment MyCompartment
```

### Shape-Based Quotas
Family name: `compute`
**Important** Shape based quotas have been deprecated and are only supported for the following listed shapes. Newer shapes, not included in this list, do not support shape based quotas. Core and memory based quotas should be used instead.
Name | Scope | Description  
---|---|---  
bm-standard1-36-count | Availability domain  | Number of BM.Standard1.36 instances  
bm-standard-b1-44-count | Availability domain  | Number of BM.Standard.B1.44 instances  
bm-standard2-52-count | Availability domain  | Number of BM.Standard2.52 instances  
bm-standard-e2-64-count | Availability domain  | Number of BM.Standard.E2.64 instances  
bm-dense-io1-36-count | Availability domain  | Number of BM.DenseIO1.36 instances  
bm-dense-io2-52-count | Availability domain  | Number of BM.DenseIO2.52 instances  
bm-gpu2-2-count | Availability domain  | Number of BM.GPU2.2 instances  
bm-gpu3-8-count | Availability domain  | Number of BM.GPU3.8 instances  
bm-hpc2-36-count | Availability domain  | Number of BM.HPC2.36 instances  
vm-standard1-1-count | Availability domain  | Number of VM.Standard1.1 instances  
vm-standard1-2-count | Availability domain  | Number of VM.Standard1.2 instances  
vm-standard1-4-count | Availability domain  | Number of VM.Standard1.4 instances  
vm-standard1-8-count | Availability domain  | Number of VM.Standard1.8 instances  
vm-standard1-16-count | Availability domain  | Number of VM.Standard1.16 instances  
vm-standard2-1-count | Availability domain  | Number of VM.Standard2.1 instances  
vm-standard2-2-count | Availability domain  | Number of VM.Standard2.2 instances  
vm-standard2-4-count | Availability domain  | Number of VM.Standard2.4 instances  
vm-standard2-8-count | Availability domain  | Number of VM.Standard2.8 instances  
vm-standard2-16-count | Availability domain  | Number of VM.Standard2.16 instances  
vm-standard2-24-count | Availability domain  | Number of VM.Standard2.24 instances  
vm-standard-e2-1-micro-count | Availability domain  | Number of VM.Standard.E2.1.Micro instances  
vm-standard-e2-1-count | Availability domain  | Number of VM.Standard.E2.1 instances  
vm-standard-e2-2-count | Availability domain  | Number of VM.Standard.E2.2 instances  
vm-standard-e2-4-count | Availability domain  | Number of VM.Standard.E2.4 instances  
vm-standard-e2-8-count | Availability domain  | Number of VM.Standard.E2.8 instances  
vm-dense-io1-4-count | Availability domain  | Number of VM.DenseIO1.4 instances  
vm-dense-io1-8-count | Availability domain  | Number of VM.DenseIO1.8 instances  
vm-dense-io1-16-count | Availability domain  | Number of VM.DenseIO1.16 instances  
vm-dense-io2-8-count | Availability domain  | Number of VM.DenseIO2.8 instances  
vm-dense-io2-16-count | Availability domain  | Number of VM.DenseIO2.16 instances  
vm-dense-io2-24-count | Availability domain  | Number of VM.DenseIO2.24 instances  
vm-gpu2-1-count | Availability domain  | Number of VM.GPU2.1 instances  
vm-gpu3-1-count | Availability domain  | Number of VM.GPU3.1 instances  
vm-gpu3-2-count | Availability domain  | Number of VM.GPU3.2 instances  
vm-gpu3-4-count | Availability domain  | Number of VM.GPU3.4 instances  
dvh-standard2-52-count | Availability domain  | Number of DVH.Standard2.52 instances  
### Example
Copy
```
set compute quota vm-dense-io2-8-count to 10 in compartment MyCompartment where request.ad = 'us-phoenix-1-ad-2'
```

[Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm)
Quotas for capacity reservations are available by core (OCPU) or GPU, and by the amount of memory (GB). Available quotas depend on the shape.
Reserve capacity for future usage, and ensure that capacity is available to create Compute instances whenever you need them. The reserved capacity is used when you launch instances against the reservation. When these instances are terminated, the capacity is returned to the reservation, and the unused capacity in the reservation increases. Unused reserved capacity is metered differently than used reserved capacity.
  * To set quotas on how many instances can be reserved, use the **Reservable** quotas.
  * To set quotas on how many reserved instances can be created in capacity reservations, use the **Reserved** quotas.


### Core- and GPU-Based Quotas
Family name: `compute-core`
Name | Scope | Description  
---|---|---  
standard1-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard1 and BM.Standard1 series  
standard1-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard1 and BM.Standard1 series  
standard-b1-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard.B1 and BM.Standard.B1 series  
standard-b1-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard.B1 and BM.Standard.B1 series  
standard2-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard2 and BM.Standard2 series  
standard2-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard2 and BM.Standard2 series  
standard3-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard3 and BM.Standard3 series  
standard3-core-reserved-count | Availability domain | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard3 and BM.Standard3 series  
standard-e2-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard.E2 and BM.Standard.E2 series  
standard-e2-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard.E2 and BM.Standard.E2 series  
standard-e3-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard.E3 and BM.Standard.E3 series  
standard-e3-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard.E3 and BM.Standard.E3 series  
standard-e4-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard.E4 and BM.Standard.E4 series  
standard-e4-core-reserved-count | Availability domain | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard.E4 and BM.Standard.E4 series  
standard-a1-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Standard.A1 and BM.Standard.A1 series  
standard-a1-core-reserved-count | Availability domain | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Standard.A1 and BM.Standard.A1 series  
dense-io1-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.DenseIO1 and BM.DenseIO1 series  
dense-io1-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.DenseIO1 and BM.DenseIO1 series  
dense-io2-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.DenseIO2 and BM.DenseIO2 series  
dense-io2-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.DenseIO2 and BM.DenseIO2 series  
dense-io-e4-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series  
dense-io-e4-core-reserved-count | Availability domain | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series  
gpu2-core-count-reservable | Availability domain  | Total number of GPUs that can be reserved for shapes in the VM.GPU2 and BM.GPU2 series  
gpu2-reserved-count | Availability domain  | Total number of GPUs for creating instances in capacity reservations when using shapes in the VM.GPU2 and BM.GPU2 series  
gpu3-core-count-reservable | Availability domain  | Total number of GPUs that can be reserved for shapes in the VM.GPU3 and BM.GPU3 series  
gpu3-reserved-count | Availability domain  | Total number of GPUs for creating instances in capacity reservations when using shapes in the VM.GPU3 and BM.GPU3 series  
gpu4-core-count-reservable | Availability domain  | Total number of GPUs that can be reserved for shapes in the BM.GPU4 series  
gpu4-reserved-count | Availability domain  | Total number of GPUs for creating instances in capacity reservations when using shapes in the BM.GPU4 series  
gpu-a10-core-count-reservable | Availability domain  | Total number of GPUs that can be reserved for shapes in the VM.GPU.A10 and BM.GPU.A10 series  
gpu-a10-reserved-count | Availability domain  | Total number of GPUs for creating instances in capacity reservations when using shapes in the VM.GPU.A10 and BM.GPU.A10 series  
gpu-a100-v2-core-count-reservable | Availability domain  | Total number of GPUs that can be reserved for shapes in the BM.GPU.A100 series  
gpu-a100-v2-reserved-count | Availability domain  | Total number of GPUs for creating instances in capacity reservations when using shapes in the BM.GPU.A100 series  
hpc2-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the BM.HPC2 series  
hpc2-core-reserved-count | Availability domain  | Total number of OCPUs for creating instances in capacity reservations when using shapes in the BM.HPC2 series  
optimized3-core-count-reservable | Availability domain  | Total number of OCPUs that can be reserved for shapes in the VM.Optimized3 and BM.Optimized3 series  
optimized3-core-reserved-count | Availability domain | Total number of OCPUs for creating instances in capacity reservations when using shapes in the VM.Optimized3 and BM.Optimized3 series  
### Example
Copy
```
set compute-core quota standard3-core-reserved-count to 480 in compartment MyCompartment
```

### Memory-Based Quotas
Family name: `compute-memory`
Name | Scope | Description  
---|---|---  
standard3-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.Standard3 and BM.Standard3 series, in GB  
standard3-memory-reserved-count | Availability domain | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.Standard3 and BM.Standard3 series, in GB  
standard-e3-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.Standard.E3 and BM.Standard.E3 series, in GB  
standard-e3-memory-reserved-count | Availability domain  | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.Standard.E3 and BM.Standard.E3 series, in GB  
standard-e4-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.Standard.E4 and BM.Standard.E4 series, in GB  
standard-e4-memory-reserved-count | Availability domain | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.Standard.E4 and BM.Standard.E4 series, in GB  
standard-a1-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.Standard.A1 and BM.Standard.A1 series, in GB  
standard-a1-memory-reserved-count | Availability domain | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.Standard.A1 and BM.Standard.A1 series, in GB  
dense-io-e4-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series, in GB  
dense-io-e4-memory-reserved-count | Availability domain | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.DenseIO.E4 and BM.DenseIO.E4 series, in GB  
optimized3-memory-count-reservable | Availability domain  | Total amount of memory that can be reserved for shapes in the VM.Optimized3 and BM.Optimized3 series, in GB  
optimized3-memory-reserved-count | Availability domain | Total amount of memory for creating instances in capacity reservations when using shapes in the VM.Optimized3 and BM.Optimized3 series, in GB  
### Example
Copy
```
set compute-memory quota standard-e4-memory-reserved-count to 120 in compartment MyCompartment
```

[Custom Images](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm)
Family name: `compute`
Name | Scope | Description  
---|---|---  
custom-image-count | Regional | Number of custom images  
### Example
Copy
```
set compute quota custom-image-count to 15 in compartment MyCompartment
```

[Instance Configurations, Instance Pools, and Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm)
### Quotas for instance configurations, instance pools, and cluster networks that use instance pools
Family name: `compute-management`
Name | Scope | Description  
---|---|---  
cluster-network-count | Regional | Number of cluster networks that use instance pools  
config-count | Regional | Number of instance configurations  
pool-count | Regional | Number of instance pools  
### Quotas for compute clusters
Family name: `compute`
Name | Scope | Description  
---|---|---  
compute-cluster-count | Availability domain | Number of compute clusters  
### Example
Copy
```
set compute-management quota config-count to 10 in compartment MyCompartment
```

[Autoscaling](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm)
Family name: `auto-scaling`
Name |  Scope |  Description  
---|---|---  
config-count | Regional | Number of autoscaling configurations  
### Example
Copy
```
Set auto-scaling quota config-count to 10 in compartment MyCompartment
```

Was this article helpful?
YesNo

