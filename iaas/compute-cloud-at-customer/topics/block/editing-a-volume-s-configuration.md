Updated 2024-12-16
# Updating a Block Volume
On Compute Cloud@Customer, you can change settings for block volumes while the volumes are online, without any downtime. You can change the display name, increase the size, and change tags.
To increase the volume size, see [Resizing Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-volumes.htm#resizing-volumes "On Oracle Cloud Infrastructure, the Block Volume service lets you expand the size of block volumes and boot volumes.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-volume-s-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-volume-s-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-volume-s-configuration.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    2. At the top of the page, select the compartment that contains the volume that you want to edit.
    3. For the volume that you want to edit, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. In the Edit Block Volume dialog box, make changes.
       * **Name:** The volume display name. The name does not have to be unique.
       * **Size (in GB):** You can increase the size in 1 GB increments up to 32 TB. You can't decrease the size. Before you change the size, see [Resizing Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-volumes.htm#resizing-volumes "On Oracle Cloud Infrastructure, the Block Volume service lets you expand the size of block volumes and boot volumes.") to understand the implications of this change.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
To use nondefault values for the block size, write bias, or secondary cache, specify the appropriate tags to set the values for these attributes. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
    5. Click **Save Changes**.
  * Use the [oci bv volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html) command and required parameters to update a volume.
Command
CopyTry It
```
oci bv volume update --volume-id <volume_OCID> --display-name <new-display-name> [OPTIONS]
```

To use nondefault values for the block size, write bias, or secondary cache, specify the appropriate tags to set the values for these attributes. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume) operation to update a volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

