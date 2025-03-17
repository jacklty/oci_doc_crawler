Updated 2023-12-08
# Tagging a Volume Group at Creation
Add metadata to a volume group when you first create it. This metadata enables you to define keys and values and to associate them with resources.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-create-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-create-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-create-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Click **Create volume group**.
    3. Click **Show Tagging Options**.
       * **Tag namespace** : To add a defined tag, select an existing namespace. To add a free-from tag, leave the value blank.
       * **Tag key** : To add a defined tag, select an existing tag key. To add a free-form tag, type the key name that you want.
       * **Tag value** : Type the tag value that you want.
       * **Add tag** : Click to add another tag.
    4. Provide values for other fields as needed.
See [Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#top "Create a volume group in the Block Volume service.").
    5. Click **Create**.
  * Use the [oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html) command and required parameters to tag a volume group at creation:
Command
CopyTry It
```
oci bv volume-group create [...] [--defined-tags | --freeform-tags] <tags>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup) operation to tag a volume group at creation. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

