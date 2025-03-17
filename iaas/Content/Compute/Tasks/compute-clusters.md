Updated 2025-02-13
# Compute Clusters
A compute cluster is a group of high performance computing (HPC), GPU, or optimized instances that are connected with a high-bandwidth, ultra low-latency network. Each node in the cluster is a bare metal machine located in close physical proximity to the other nodes. A remote direct memory access (RDMA) network between nodes provides latency as low as single-digit microseconds, comparable to on-premises HPC clusters.
When you create a compute cluster, you create an empty RDMA network group. After the group is created, you can add instances to the group, or delete instances from the group. Compute clusters allow you to manage instances in the cluster individually, and you can have different types of instances in the cluster.
**Tip** If you want predictable capacity for a specific number of identical instances that are managed as a group, use [cluster networks with instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#top) instead.
For steps to manage compute clusters, see the following topics:
  * [Creating a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm#top "When you first create a compute cluster, you create an empty RDMA network group. After the compute cluster is created, you can create instances in the compute cluster.")
  * [Retrieving a Compute Cluster's OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-ocid-compute-cluster.htm#top "If you don't already have the OCID of a compute cluster, you can retrieve a list of compute clusters in a compartment with their corresponding OCIDs.")
  * [Attaching Instances to a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm#top "After you create a compute cluster, you can create instances within the cluster. The instances must be in the same compartment and availability domain as the cluster.")
  * [Getting Details About a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-compute-cluster.htm#top "After you create a compute cluster, you can retrieve details about the cluster.")
  * [Editing the Name of a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-compute-cluster.htm#top "You can edit the name of a compute cluster.")
  * [Moving a Compute Cluster to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm#top "After you create a compute cluster, you can move it to a different compartment.")
  * [Deleting a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-compute-cluster.htm#top "You can delete a compute cluster if you no longer need it.")


For more information about how to access and store the data that you want to process in your compute clusters, see [FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm), [Overview of File Storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm), [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm), and [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: To allow users to do all things with compute clusters in all compartments, write the following policy:
Copy
```
Allow group ComputeClusterUsers to manage compute-clusters in tenancy
```

You must also allow users to create instances in cluster networks. For a typical policy, see [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).
## Supported Shapes 🔗 
The following [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) support compute clusters:
  * BM.GPU.A100-v2.8
  * BM.GPU.H100.8
  * BM.GPU4.8
  * BM.HPC2.36
  * BM.Optimized3.36


Typically, to be able to create multiple HPC, GPU, or optimized instances in a compute cluster, you must [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
## Supported Regions and Availability Domains 🔗 
Compute clusters are supported in selected regions within the Oracle Cloud Infrastructure [commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) and [Government Cloud realms](https://docs.oracle.com/iaas/Content/General/Concepts/govlanding.htm).
[Supported regions in the commercial realm](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm)
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Brazil East (Sao Paulo)
  * Brazil Southeast (Vinhedo)
  * Canada Southeast (Montreal)
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * India South (Hyderabad)
  * India West (Mumbai)
  * Israel Central (Jerusalem)
  * Italy Northwest (Milan)
  * Japan Central (Osaka)
  * Japan East (Tokyo)
  * Netherlands Northwest (Amsterdam)
  * Saudi Arabia West (Jeddah)
  * Singapore (Singapore)
  * South Africa Central (Johannesburg)
  * South Korea Central (Seoul)
  * South Korea North (Chuncheon)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich)
  * UAE East (Dubai)
  * UK South (London)
  * US East (Ashburn)
  * US Midwest (Chicago)
  * US West (Phoenix)
  * US West (San Jose)


[Supported regions in the Government Cloud realms](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm)
  * UK Gov South (London)
  * UK Gov West (Newport)
  * US Gov East (Ashburn) 


The availability domain that you create the compute cluster in must have hardware that supports compute clusters.
Was this article helpful?
YesNo

