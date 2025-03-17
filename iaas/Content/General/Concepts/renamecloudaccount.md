Updated 2024-02-13
# Renaming a Tenancy and Cloud Account
Use the **Rename Tenancy** button on the **Tenancy details** page to rename a tenancy and cloud account.
## Overview 🔗 
When you sign up for Oracle Cloud, you get a cloud _account_ and an Oracle Cloud Infrastructure _tenancy_. Both the cloud account and tenancy have an ID and a name. Oracle assigns the same name to the cloud account and the tenancy, but they each have a unique ID.
When you [sign in](https://docs.oracle.com/iaas/Content/GSG/Concepts/signinoptions.htm) to the Console, you need to specify the tenancy name so that you arrive at the correct account. Any programmatic access uses the tenant ID or cloud account ID, not its name. For example:
  * Sample account and tenancy name: "OracleCustomer1"
  * Sample cloud account ID: "cacct-<unique_ID>"
  * Sample tenancy ID: "ocid1.tenancy.oc1..<unique_ID>"


You can view your cloud account name on the **Tenancy details** page. For more information on viewing and getting your tenancy details, see [Viewing Tenancy Details](https://docs.oracle.com/en-us/iaas/Content/Identity/tenancy/managingtenancy.htm#Managing_the_Tenancy) and [Getting a Tenancy's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/tenancy/Viewing_the_Tenancy_Details_Page.htm#view "Use the following tasks to view a tenancy's details.").
You might need to rename your cloud account if the name that was initially assigned is no longer relevant or correct. For example:
  * You created a trial account called "MyTrial", and then it became the main account for your company.
  * You had an acquisition that's forcing name changes.


**Important** An active subscription is required to rename a tenancy and cloud account. Free Tier tenancies can't be renamed.
## Renaming the Tenancy 🔗 
Follow these guidelines for a successful rename:
  * You must be in your home region to do the rename.
  * Plan ahead and inform others that you plan on changing the name.
  * Change the name during off-hours to reduce impact on users in your tenancy.
  * Notify personnel who use Oracle Cloud when the rename is complete.


**Important** Parent tenancies can't rename child tenancies in an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization."). When renaming a _child_ tenancy, you must be _signed in to the child tenancy_ to do the rename. 
You can change your cloud account name using the **Rename Tenancy** button on the Console's **Tenancy details** page. Only an OCI administrator can do the rename.
**Note** Former **My Oracle Services** dashboard users must now use the **Rename Tenancy** function in the Console's **Tenancy details** page.
To rename a tenancy:
  1. While signed in as an OCI administrator, open the **Tenancy details** page. For more information, see [Getting a Tenancy's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/tenancy/Viewing_the_Tenancy_Details_Page.htm#view "Use the following tasks to view a tenancy's details."). If you're not signed in as an administrator, the **Rename Tenancy** button isn't available.
**Important** If you're renaming a child tenancy in an [organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm#organization_management_overview "Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization."), ensure you're signed in to the _child_ tenancy, not the parent.
  2. Click **Rename tenancy**.
  3. In the **Rename tenancy** dialog box, enter the new tenancy name in **New tenancy name**. 
  4. Confirm the name in **Confirm tenancy name**. 
The tenancy name can be a maximum of 25 characters and must start with a letter, and can have lowercase letters or numbers. No spaces or capital letters are allowed. Avoid entering confidential information.
  5. Click **Rename tenancy**. 
A message is displayed at the top of the **Tenancy details** page stating that the rename is in progress. You can continue to perform other operations in the Console. Sign in using the new tenancy name after the rename is complete.
Under **Work requests** , a new **RENAME_TENANCY** operation appears with the "In progress" state, the progress percentage, and the accepted, started, and finished times. You can click the work request operation to get more details.
After clicking the **RENAME_TENANCY** work request, its details page opens with the **Work request details** tab selected. You can view the status on this details page, and review log messages and error messages related to the rename.
Renaming the tenancy and cloud account takes about 15 minutes. While the rename is in progress, however, the old name is still visible. 
After the rename is complete, the **RENAME_TENANCY** work request changes to **Succeeded**. The **Tenancy details** page title, and the **Name** field under **Tenancy information** shows the new name when the rename has finished processing.


**Important** On the **Identity domain** **Branding** page, you must also update the **Company name** field to match the new tenancy name. Updating this field on the **Branding** page correlates with the new tenancy name in email notifications, and when signing back in to the Console after the rename. For more information, see [Customizing the Sign-In Page Branding](https://docs.oracle.com/en-us/iaas/Content/Identity/brand/customizing-the-signin-page.htm#customize-sign-page "Customize the sign-in page options for an identity domain in IAM.").
## After the Rename 🔗 
The next time signing in to the Console, you must use the _new_ tenancy name when prompted for a cloud account or tenancy name.
Renaming is irreversible. After the name has changed, you can't use the old name to sign in to the Console. Existing sessions keep working, but new sessions need to use the new name. You also can't change an account name back to its old name.
For SaaS services where the tenancy name is a part of the instance URL, existing URLs may be changed, so contact your service administrator for the updated URL.
When you rename the tenancy, all references to the cloud account name _and_ the tenancy name are updated, including the following names:
  * Amazon S3 Compatibility API Designated Compartment
  * SWIFT API Designated Compartment


The API Designated Compartment names are listed on the **Tenancy information** tab of the **Tenancy details** page, under **Object storage settings**. The **Object storage namespace** , also found under **Object storage settings** , isn't updated. This name is set as the name for older accounts. Newer accounts have a short random string as the namespace.
**Note** Optionally, you can edit your account in the Oracle Mobile Authenticator (OMA) app, because after the rename the tenancy name won't match. If you want your new tenancy name to match what is shown in the OMA app, you can select the account in OMA and edit the tenancy name. For more information, see [Editing Accounts in the OMA App](https://docs.oracle.com/en-us/iaas/Content/Identity/mobileauthapp/edit-accounts-oma-app.htm#edit-accounts-oma-app "You can edit your accounts in the Oracle Mobile Authenticator \(OMA\) app.").
If an error occurs or the rename takes longer than four hours, you can [open a support request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). The following are tenancy rename status messages and their meaning.
Erorr Message | Description  
---|---  
This service is not available outside your home region. | Renaming isn't allowed outside the tenancy home region.  
This service is not available because a rename work request is in progress. | The tenancy has a rename work request that's already open.  
This service is not available while a tenancy deletion work request is in progress. | The tenancy has a deletion work request that's already open.  
This service is not available while the tenancy is inactive. | The tenancy or account isn't in an active state. An active account is required to do tenancy renames.  
Tenancy renaming is not available while you're subscribed to the <service> unsupported service. | The tenancy is subscribed to an unsupported service and can't be renamed.  
The following are tenancy rename work request messages and their meaning.
Work Request Message | Work Request State | Description  
---|---|---  
Message: Start renaming WF. WR: ocid1.accountworkrequest.<region>..<unique_id> | INPROGRESS | The work request has started provisioning the rename request. If the work request is restarted, this message appears again in the work request logs.  
Rename for Tenancy Succeeded | SUCCEEDED | The work request completed.  
Rename for Tenancy didn't complete | WAITING | The work request is stuck and [support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) is required.  
FAILED | The work request failed, but you can resubmit the rename request.  
Was this article helpful?
YesNo

