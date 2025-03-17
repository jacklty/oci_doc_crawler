Updated 2024-08-06
# Creating a Volume Group
On Compute Cloud@Customer, you can create volume groups that include block and boot volumes using the Compute Cloud@Customer Console, CLI, and API.
**Prerequisite**
Ensure that the volumes you plan to group are created. See [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm#creating-a-block-volume "On Compute Cloud@Customer, block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-volume-group-from-existing-volumes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-volume-group-from-existing-volumes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-volume-group-from-existing-volumes.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. Click **Create Volume Group**.
    3. Provide the following information:
       * **Name** : A user-friendly name or description for the volume group. Avoid entering confidential information.
       * **Compartment** : The compartment for the volume group.
       * **Volumes** : Select a volume to add to the group from the volume drop-down list. You might need to select a different compartment above the volume drop-down list. Click **+ Add Volume** to add another volume.
       * **Backup Policy:** (Optional) Select a backup policy from the drop-down list. You might need to change the compartment.
    4. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Volume Group**.
  * Use the [oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html) command and required parameters to create a volume group.
Command
CopyTry It
```
oci bv volume-group create --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> --source-details <json_string> or file://<path_to_JSON_file> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup) operation to create a volume group:
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

