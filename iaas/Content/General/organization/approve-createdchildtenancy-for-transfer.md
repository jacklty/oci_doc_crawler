Updated 2025-02-13
# Approving a Created Child Tenancy for Transfer
Approve an organization's created child tenancy for transfer.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/approve-createdchildtenancy-for-transfer.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/approve-createdchildtenancy-for-transfer.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/approve-createdchildtenancy-for-transfer.htm)


  * This task can't be performed using the Console.
  * Use the `oci organizations organization-tenancy approve-organization-tenancy-for-transfer` command to transfer a created child tenancy to another organization.
The following example scenario assumes you have a created child tenancy that you want to transfer from an existing MyOldParentTenancy tenancy, to the new Pay As You Go MyNewParentTenancy tenancy. After the child tenancy has been transferred out of MyOldParentTenancy, you can invite the child tenancy to join the new MyNewParentTenancy tenancy. Lastly, you must update the subscription mapping in the new MyNewParentTenancy tenancy to ensure all tenancies (including future tenancies) use the existing subscription from the MyOldParentTenancy tenancy.
Tenancy details are the following:
Tenancy Name | OCID  
---|---  
MyOldParentTenancy | ocid1.tenancy.oc1..<old-parent-tenancy-unique_ID>  
MyNewParentTenancy | ocid1.tenancy.oc1..<new-parent-tenancy-unique_ID>  
childtenancy1 | ocid1.tenancy.oc1..<child-tenancy1-unique_ID>  
To transfer a created child tenancy:
    1. While signed in as an administrator to MyOldParentTenancy, make a note of the subscription ID, because you will need it later to change the [subscription mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management."). 
Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**. On the **Subscription Mapping** page, copy the subscription ID from the **Subscription ID** field.
    2. Transfer childtenancy1 to MyNewParentTenancy. While signed in as the administrator to MyOldParentTenancy, select the home region of your child tenancy and [open Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellgettingstarted.htm).
    3. Run the following command:
Command
CopyTry It
```
oci organizations organization-tenancy approve-organization-tenancy-for-transfer --compartment-id ocid1.tenancy.oc1..<old-parent-tenancy-unique_ID> --organization-tenancy-id ocid1.tenancy.oc1..<child-tenancy1-unique_ID>
```

You can verify command success by examining the output:
```
{
 "data": {
 "is-approved-for-transfer": true,
 "lifecycle-state": "ACTIVE",
 "name": null,
 "role": "CHILD",
 "tenancy-id": "ocid1.tenancy.oc1..<unique_ID>"
 "time-joined": "<date-time>",
 "time-left": null
 }
}
```

For more information on the CLI, see [oci organizations organization-tenancy approve-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/approve-organization-tenancy-for-transfer.html).
    4. Sign out of MyOldParentTenancy, and then sign in to MyNewParentTenancy.
    5. Follow the steps in [Inviting a Tenancy to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#sender_invitation_create "Create an invitation to join an organization and asynchronously send the invitation to the recipient.") to invite childtenancy1.
In **Recipient tenancy OCID** , enter the OCID for childtenancy1 (ocid1.tenancy.oc1..<child-tenancy1-unique_ID>).
    6. Select **Next** and skip selection of any [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.").
    7. Review the summary step to ensure the invited tenancy settings you specified are correct. Select **Invite tenancy** to invite childtenancy1. 
Check the recipient email and follow the instructions to accept the invitation and complete the transfer process.
    8. You can repeat the previous steps for any extra tenancies, adjusting the `oci organizations organization-tenancy approve-organization-tenancy-for-transfer` command and the tenancy invitation to reflect the OCIDs for further tenancies.
    9. After the child tenancy has been transferred out of the old parent tenancy, the old parent tenancy can also be invited to become a child tenancy of the new parent tenancy. Follow the steps in [Inviting a Tenancy to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#sender_invitation_create "Create an invitation to join an organization and asynchronously send the invitation to the recipient.") to invite MyOldParentTenancy to join MyNewParentTenancy. 
In **Recipient tenancy OCID** , enter the OCID for MyOldParentTenancy (ocid1.tenancy.oc1..<old-parent-tenancy-unique_ID>).
    10. Select **Next** and skip selection of any [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.").
    11. Review the summary step to ensure the invited tenancy settings you specified are correct. Select **Invite tenancy** to invite MyOldParentTenancy.
Check the recipient email and follow the instructions to accept the invitation and complete the transfer process.
    12. Follow the instructions in [Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management.") to remap the subscription that was used by MyOldParentTenancy to MyNewParentTenancy, ensuring that you map the subscription to all tenancies.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ApproveOrganizationTenancyForTransfer](https://docs.oracle.com/iaas/api/#/en/organizations/latest/OrganizationTenancy/ApproveOrganizationTenancyForTransfer) operation to approve an organization's child tenancy for transfer.


Was this article helpful?
YesNo

