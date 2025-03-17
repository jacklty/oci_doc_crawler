Updated 2025-02-11
# Tagging a Recipient Invitation When Updating
Add metadata tags to an existing recipient invitation in Organization Management. This metadata enables you to define keys and values and associate them with resources.
For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-recipientinvitation-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-recipientinvitation-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-recipientinvitation-update.htm)


  *     1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
    2. On the **Invitations** page, select the invitation name from the **Invitation Name** field, or select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **View Invitation Details**.
    3. On the invitation details page, add or edit tags as needed:
       * To add one or more tags, select **Add tags** , and then enter the tag namespace (for a defined tag), key, and value.
       * To edit or remove a tag, select the **Tags** tab, select the edit icon next to a tag, and change its value or remove it.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci organizations recipient-invitation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/update.html) command and required parameters to tag a recipient invitation when you're updating it:
Command
CopyTry It
```
oci organizations recipient-invitation update [...] [--defined-tags | --freeform-tags] tags [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/UpdateRecipientInvitation) operation to edit a recipient invitation. Include the definedTags and freeformTags attributes and their values.


Was this article helpful?
YesNo

