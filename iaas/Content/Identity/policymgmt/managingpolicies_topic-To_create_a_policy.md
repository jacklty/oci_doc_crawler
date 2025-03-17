Updated 2025-01-14
# Creating a Policy
Create IAM policies to manage access to OCI resources.
The group and compartment that you're writing the policy for must already exist.
**Note**
If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies. 
To recompile the policy, open a policy, and make a small edit. Save the policy.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
A list of the policies in the compartment you're viewing is displayed.
  2. Select **Create Policy**.
  3. Enter the following information:
     * **Name:** A unique name for the policy. The name must be unique across all policies in the tenancy. You can't change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later.
     * **Compartment:** If you want to attach the policy to a compartment other than the one you're viewing, select it from list. Where the policy is attached controls who can later modify or delete it (see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.")).
  4. Enter the policy statements using the [policy builder](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-Using_the_Policy_Builder.htm#builder "Work with Policy Builder."). Use the basic option if you want to choose from common policy templates, which you can also customize. Select **Show manual editor** if you already know how to write the statements you need and you want to enter them in a text box.
To use the policy builder basic option:
    1. Select from the **Policy use cases** menu to filter the list of policy templates. If you're not sure which use case to choose, you can browse all the templates in the **Common policy templates** list.
    2. Select the template that best matches your requirements from the **Common policy templates** list.
The policy builder displays the description of the chosen policy and lists the policy statements that it includes.
    3. Select the identity domain that contains the group to which you want to apply this policy.
    4. Select the group that this policy applies to.
    5. Select a location. The location is the compartment that this policy grants access to. The compartment you choose here must be either the compartment you chose to attach the policy to in Step 3, or a compartment within the hierarchy of that compartment.
    6. If you need to modify the policy statements, select **Show manual editor**. 
To use the **Show manual editor** option:
    1. Select **Show manual editor**.
    2. Enter or edit policy statements by using the format described in [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies."),entering one statement per line.
  5. To add tags to this policy, select **Show advanced options**.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  6. If you want to create another policy, select **Create another policy**.
  7. Select **Create**. 
Your changes go into effect typically within 10 seconds.


Was this article helpful?
YesNo

