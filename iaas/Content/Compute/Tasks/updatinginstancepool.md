Updated 2025-02-13
# Updating Instance Pools
You can change the size of an instance pool, attach existing instances to a pool, attach load balancers and network load balancers, and update various other properties.
For background information about instance pools and instance configurations, see [Using Instance Configurations and Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Managing_Compute_Instances).
Updating instance pools includes the following tasks:
  * [Updating the Size of an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-update-instance-pool-size.htm#pool-size "You can manually update the number of instances for an instance pool.")
  * [Attaching an Instance to an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm#attach-instance "Attach an existing instance to an instance pool, and then select which instances you want to manage as a group.")
  * [Detaching an Instance from an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#detach-instance "Detach an instance from an instance pool when you no longer want to manage the instance as part of the pool.")
  * [Attaching a Load Balancer to an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_attach_a_load_balancer_to_an_instance_pool.htm#attach "Attach a load balancer or network load balancer to an instance pool.")
  * [Detaching a Load Balancer from an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm#detach "Detach a load balancer or network load balancer from an instance pool.")
  * [Updating the Instance Configuration for an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm#instance-configuration "Update the instance configuration that an instance pool uses when creating instances.")
  * [Renaming an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-pool.htm#rename-pool "Rename an instance pool without changing its Oracle Cloud Identifier \(OCID\).")
  * [Editing Custom Instance Display and Instance Host Names](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm#updatinginstancepool-renaming-custom-display-host-names "Change custom instance display name and host name for instances you create in an instance pool.")
  * [Updating Instance Placement in an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-placement.htm#placement "Update the location where the instances in an instance pool are placed. The placement includes the availability domains, fault domains, and subnets for the instances in the instance pool.")
  * [Tagging Resources](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-Tagging_Resources.htm#tags "Apply tags to instance pools.")


**Caution** Avoid entering confidential information when assigning descriptions, tags, or friendly names to cloud resources through the Oracle Cloud Infrastructure Console, API, or CLI.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For a typical policy that gives access to instance pools and instance configurations, see [Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).
Was this article helpful?
YesNo

