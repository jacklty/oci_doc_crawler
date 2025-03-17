Updated 2025-02-13
# Cluster Networks with Instance Pools
Cluster networks use instance pools to manage groups of identical high performance computing (HPC), GPU, or optimized instances that are connected with a high-bandwidth, ultra low-latency network. Each node in the cluster is a bare metal machine located in close physical proximity to the other nodes. A remote direct memory access (RDMA) network between nodes provides latency as low as single-digit microseconds, comparable to on-premises HPC clusters.
Cluster networks are built on top of the [instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Instance) feature. Most operations in the instance pool are managed directly by the cluster network, though you can resize the underlying instance pool, change the instance configuration that the pool uses to create new instances, monitor the pool, and add tags.
**Tip** If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, then use [compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters) instead.
For steps to manage cluster networks with instance pools, see the following topics:
  * [Creating a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm#create-cluster-network "Create a cluster network with instance pools.")
  * [Detaching Instances from a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#detach-instance "Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.")
  * [Resizing a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm#top "Change the number of instances in a cluster network by resizing the underlying instance pool.")
  * [Updating the Instance Configuration for a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm#top "Update the instance configuration that a cluster network's underlying instance pool uses when creating instances.")
  * [Tagging Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks-tagging-resources.htm#tagging "Tag cluster networks to help organize the resources.")
  * [Renaming a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm#top "Edit a cluster network with instance pools to give it a new name.")
  * [Deleting a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm#top "Delete \(terminate\) a cluster network that you no longer need.")


For more information about how to access and store the data that you want to process in cluster networks, see [FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm), [Overview of File Storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm), [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm), and [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm).
## Supported Shapes 🔗 
The following [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) support cluster networks:
  * BM.GPU.A100-v2.8
  * BM.GPU.H100.8
  * BM.GPU4.8
  * BM.HPC2.36
  * BM.Optimized3.36


Typically, to create multiple HPC, GPU, or optimized instances that are contained in a cluster network, you must [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
## Supported Regions and Availability Domains 🔗 
Cluster networks are supported in selected regions within the Oracle Cloud Infrastructure [commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) and [Government Cloud realms](https://docs.oracle.com/iaas/Content/General/Concepts/govlanding.htm).
[Supported regions in the commercial realm](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm)
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Brazil East (Sao Paulo)
  * Brazil Southeast (Vinhedo)
  * Canada Southeast (Montreal)
  * Canada Southeast (Toronto)
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


[Supported regions in the Government Cloud realms](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm)
  * UK Gov South (London)
  * UK Gov West (Newport)
  * US Gov East (Ashburn) 


The availability domain that you create the cluster network in must have hardware that supports cluster networks.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For a typical policy that gives access to cluster networks, see [Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).
## Before You Begin 🔗 
[Create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) for the instance pool that is managed by the cluster network. Use the following settings:
  * **Image:** Click **Change image** , and then click **Oracle images**. Select the Oracle Linux HPC cluster networking image.
  * **Shape:** Click **Change shape**. Select **Bare metal machine**. Then, select a [shape that supports cluster networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#supported-shapes).
For more information about these shapes, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).


Was this article helpful?
YesNo

