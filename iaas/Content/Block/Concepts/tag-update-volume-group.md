Updated 2023-12-08
# Tagging a Volume Group When Updating
Add metadata to a volume group when you update it. This metadata enables you to define keys and values and to associate them with resources.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-update-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-update-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-update-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. In the **Volume Groups** list, click the volume group you want to tag.
    3. Click **Tags** to open the **Tags** tab.
    4. If the volume group doesn't have any tags yet, then follow these steps.
      1. Click **Add tags**.
      2. In the **Add tags** dialog box, for each tag that you want to add, enter the tag namespace, key, and value.
         * **Tag namespace** : To add a defined tag, select an existing namespace. To add a free-from tag, leave the value blank.
         * **Tag key** : To add a defined tag, select an existing tag key. To add a free-form tag, type the key name that you want.
         * **Tag value** : Type the tag value that you want.
         * **Add tag** : Click to add another tag.
    5. If the volume group already has tags, then you can edit them. Follow these steps.
**Note** To add a tag to an existing volume group, note existing tags, remove them (Remove tag for each tag), and then see the previous step for instructions on adding tags. Ensure that you add back the removed tags.
      1. Click the pencil icon for the tag that you want to edit.
      2. In the **Edit tag** dialog box, for each tag that you want to edit, enter the new value.
      3. Click **Save**.
  * Use the [oci bv volume-group update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html) command and required parameters to tag a volume group when you update it:
Command
CopyTry It
```
oci bv volume-group update [...] [--defined-tags | --freeform-tags] <tags>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup) operation to tag a volume group when you update it. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

