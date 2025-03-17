Updated 2024-06-04
# Attaching a Boot Volume
If a boot volume has been detached from the associated instance, you can reattach it to the instance. If you want to restart an instance with a detached boot volume, you must reattach the boot volume using the steps described in this topic.
If a boot volume has been detached from the associated instance, or if the instance is stopped or terminated, you can attach the boot volume to another instance as a data volume. For steps, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance."). 
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to attach and detach existing block volumes. The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Security Zones 🔗 
[Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm) ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a [policy for that security zone](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm), then the operation is denied.
The following security zone policies affect your ability to attach block volumes to compute instances.
  * The boot volume for a compute instance in a security zone must also be in the same security zone.
  * A compute instance that isn't in a security zone can't be attached to a boot volume that is in a security zone.


## Using the Console 🔗 
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
  2. Click the instance that you want to reattach the boot volume to.
  3. Under **Resources** , click **Boot Volume**.
  4. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Attach Boot Volume**. Confirm when prompted.
You can [start the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm) when the boot volume's state is **Attached**.


## Using the API 🔗 
To attach a volume to an instance, use the following operation:
  * [AttachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/AttachBootVolume)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Was this article helpful?
YesNo

