Updated 2024-06-04
# Deleting a Boot Volume
When you terminate an instance, you choose to delete or preserve the associated boot volume. For more information, see [Terminating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm). You can also delete a boot volume if it has been detached from the associated instance. See [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume) for how to detach a boot volume.
**Caution** You cannot undo this operation. Any data on a volume will be permanently deleted once the volume is deleted. You will also not be able to restart the associated instance.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Choose your **Compartment**. 
  3. In the **Boot Volumes** list, find the volume you want to delete.
  4. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the boot volume.
  5. Click **Terminate** and confirm the selection when prompted.


## Using the API 🔗 
Use the [DeleteBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DeleteBootVolume) operation to delete a boot volume.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Was this article helpful?
YesNo

