Updated 2024-06-04
# Listing Boot Volumes
You can list all boot volumes in a specific compartment, or detailed information on a single boot volume.
## Required IAM Service Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to list volumes. The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Choose your **Compartment**. 


A detailed list of volumes in the current compartment is displayed. To see detailed information for a specific volume, click the boot volume name. 
The instance associated with the boot volume is listed in the **Attached Instance** field. If the value for this field displays the message `None in this Compartment`, the boot volume has been detached from the associated instance, or the instance has been terminated while the boot volume was preserved. 
To view the volumes in a different compartment, change the compartment in the **Compartment** drop-down menu.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
### List Boot Volumes:
Get a list of boot volumes within a compartment.
  * [ListBootVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ListBootVolumes)


### Get a Single Boot Volume:
Get detailed information on a single boot volume:
  * [GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume)


Was this article helpful?
YesNo

