Updated 2025-01-10
# Editing an Instance
You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same.
On supported instances, the following edits can be made:
  * [Renaming an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm#Renaming_an_Instance)
  * [Changing the Capacity Reservation for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm#editingcapacityreservation)
  * [Changing the Shape of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance)
  * [Changing the Windows License Type of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm#changing_the_windows_license "When working with a Windows instance, you must select the type of license to use.")
  * [Editing the Fault Domain for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm#edit-fault-domain)
  * [Editing the Launch Options for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#edit-launch-options)
  * [Enabling In-Transit Encryption Between an Instance and Boot Volumes or Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm#enable-intransit-encryption)
  * [Setting Instance Availability During Maintenance Events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#edit-maintenance-recovery-action)


## Required IAM Policy
To use OCI resources, you must be granted security access in a **policy (IAM)** by an administrator. This access is required whether you're using the Console, the CLI, or the REST API. If you get a message that you don't have permission or are unauthorized, verify with your administrator you have the correct security access for your **compartment**.
The simplest policy to let users [create](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), [edit](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm#edit-instance "You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same."), and [terminate (delete)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.") instances is [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances). The policies give the specified group general access to manage instances and images and access to attach existing block volumes to instances.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
Was this article helpful?
YesNo

