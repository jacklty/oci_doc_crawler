Updated 2025-02-13
# Tagging a Sender Invitation at Creation
Describes how to add metadata to a sender invitation when you first create one. You can define keys and values, and associate them with resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-senderinvitation-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-senderinvitation-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/tag-senderinvitation-create.htm)


  *     1. Begin the steps for creating an invitation using the Oracle Cloud Infrastructure Console as described in [Inviting a Tenancy to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#sender_invitation_create "Create an invitation to join an organization and asynchronously send the invitation to the recipient.").
    2. Select **Show advanced options**. The advanced options appear.
    3. Complete the following. See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for descriptions of these fields. 
       * **Tag namespace**
       * **Tag key**
       * **Tag value**
Select **Add tag** to add another tag. Select **X** to remove the associated tag.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci organizations sender-invitation create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/create.html) command to tag a sender invitation when you create it:
Command
CopyTry It
```
oci organizations sender-invitation create [...] [--defined-tags | --freeform-tags] tags [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSenderInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/CreateSenderInvitation) operation to create a sender invitation. Include the definedTags and freeformTags attributes and their values.


Was this article helpful?
YesNo

