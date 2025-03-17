Updated 2025-02-13
# Deleting a Tenancy and Cloud Account
You can request to delete a tenancy and the associated cloud account in the Console's **Tenancy Details** page.
**Important** Deleting a tenancy permanently deletes the tenancy and the associated cloud account, and all its resources. Before deletion, we recommend you first delete any associated resources to avoid extra charges. Tenancy and cloud account deletion are irreversible and can't be undone. 
Only an OCI administrator for Free Trial customers (in a standalone tenancy scenario), or created child tenancies (in an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.")) can start a self-service deletion. The following conditions must apply:
  * The tenancy is in the home region.
  * The tenancy has no child tenancies.
  * The tenancy is using an Oracle Universal Credits subscription.
  * The tenancy is [Free Tier](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/deleting_tenancy_freetier.htm#deleting_tenancy_freetier "You can request to delete a Oracle Cloud Infrastructure Free Tier tenancy and cloud account from the Console's Tenancy Details page."), Free Trial, or you upgraded to Pay As You Go (otherwise, contact a sales representative).
  * The tenancy doesn't have any [Organization Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.") [work requests](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.").
  * You're _signed in as the child tenancy_ , not the parent.


When these conditions are met, then the **Request tenancy deletion** button is available on the **Tenancy Details** page, enabling you to delete the tenancy and cloud account.
Parent tenancies for an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.") can't be deleted, but both _standalone_ tenancies, and _child_ tenancies in an organization, can be deleted. The deletion process is different, however, for child tenancies, based on whether the child tenancy was a [created child tenancy](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/deleting_tenancy.htm#deleting_tenancy__delete-createdchild), or an [invited child tenancy](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/deleting_tenancy.htm#deleting_tenancy__delete-invitedchild) of an organization. 
**Important** Tenancy deletion isn't immediate and can take some time. Deleting the tenancy suspends all resources, and after 30 days, the tenancy is permanently deleted. After the tenancy is permanently deleted, neither you nor and any other users can sign in to the deleted tenancy.
## Delete a Standalone Tenancy 🔗 
  1. While signed in as an OCI administrator, [open](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingtenancy.htm#view) the **Tenancy Details** page. Otherwise, if not signed in as an administrator, the **Request tenancy deletion** button isn't available. 
  2. Click **Request tenancy deletion**. The **Request tenancy deletion** confirmation is displayed. 
  3. Confirm deletion in **Enter the tenancy name to confirm deletion** by entering the name of the tenancy to delete. 
  4. Click **Request tenancy deletion**. A message is displayed to indicate that you successfully created a [work request](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") to delete the tenancy.
Under **Work requests** , a **Tenancy deletion requested** operation appears, where you can view the status of the deletion request. The work request operation displays the [state](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#monitor), percent completion, date, and time accepted, and when the operation started and finished.
You can also click the **Delete Tenancy** work request to view the **Delete tenancy** work request details page. You also receive an email notifying you that the tenancy deletion process has completed.


## Delete a Created Child Tenancy of an Organization 🔗 
A _created child tenancy_ is a tenancy what was created by the parent tenancy within an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.").
  1. While signed in as an OCI administrator and as the _child_ tenancy, [open](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingtenancy.htm#view) the **Tenancy Details** page. Otherwise, if not signed in as an administrator, the **Request tenancy deletion** button isn't available. 
  2. Click **Request tenancy deletion**. The **Request tenancy deletion** confirmation is displayed.
  3. Confirm deletion in **Enter the tenancy name to confirm deletion** by entering the name of the tenancy to delete.
  4. Click **Request tenancy deletion**. A message is displayed to indicate that the delete request is in progress. A **Tenancy deletion requested** [work request](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") operation appears under **Work requests** , where you can view the status of the deletion request. 
The work request operation displays the [state](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#monitor), percent completion, date, and time accepted, and when the operation started and finished. After the request completes, the work request state changes to **Permanently delete tenancy**.
You can also click the **Delete Tenancy** work request to view the **Delete tenancy** work request details page.
You also receive an email confirmation of the tenancy deletion request. The tenancy is deleted 30 days after the work request was started, and you also receive a final email notifying you of the permanent deletion.


## Delete an Invited Child Tenancy of an Organization 🔗 
An _invited child tenancy_ is a tenancy that was a standalone tenancy before, but which was later invited to become part of an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization."). An invited child tenancy that was added to an organization using [Organization Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.") must first be removed with its subscription before it can be deleted.
  1. While signed in as an OCI administrator of the _parent_ tenancy, open the navigation menu and click **Governance & Administration**. Under **Organization Management** , click **Subscription Mapping**.
  2. Follow the instructions in [Mapping Subscriptions to Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm#subscription_mapping_create "Map tenancies to subscriptions within Organization Management.") to remap the invited child tenancy back to its original subscription on the **Subscription Mapping** page.
  3. Under **Organization Management** , click **Tenancies**.
  4. Follow the instructions in [Deleting Links to Invited Child Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm#delete_link "Use the link termination workflow to remove an invited child tenancy.") to remove the invited child tenancy on the **Tenancies** page.
  5. While signed in as an OCI administrator on the removed tenancy, [open](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingtenancy.htm#view) the **Tenancy Details** page.
  6. Click **Request tenancy deletion**. The **Request tenancy deletion** confirmation is displayed.
  7. Confirm deletion in **Enter the tenancy name to confirm deletion** by entering the name of the tenancy to delete.
  8. Click **Request tenancy deletion**. A message is displayed to indicate that you successfully created a [work request](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") to delete the tenancy.
Under **Work requests** , a **Tenancy deletion requested** operation appears, where you can view the status of the deletion request. The work request operation displays the [state](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#monitor), percent completion, date, and time accepted, and when the operation started and finished.
You can also click the **Delete Tenancy** work request to view the **Delete tenancy** work request details page. You also receive an email notifying you that the tenancy deletion process has completed.


Was this article helpful?
YesNo

