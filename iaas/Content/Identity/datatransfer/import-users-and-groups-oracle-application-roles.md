Updated 2025-01-14
# Importing Users and Groups for Oracle Application Roles
You can import users and groups using a comma-separated value (CSV) file and assign them to Oracle application roles.
**Before you begin:**
**Note** To import or export users and groups for application roles, you must be assigned to either the identity domain administrator role or the application administrator role.
To import users and groups for Oracle application roles, follow these steps.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  2. In the **Applications** page, select the Oracle application that has roles to which you want to assign users and groups.
**Note** Importing application roles imports application roles memberships only. The application roles must already exist in the identity domain. If the application roles don't exist you will receive an error for the membership import for that application role. 
  3. Select **Application roles**.
  4. In the **Import application roles** window, drag and drop the file or select **Select one** to browse for the file.
**Note** Select **Download sample file** in the dialog box to download a sample file.
  5. Select **Import**.
If a user or a group is missing a required value, such as the user name or the group name, then that user or group can't be imported. If the user or group can't be imported, then the next user or group is evaluated in the CSV file.
  6. After the job completes, review the job results.
     * If the job _can_ be processed immediately, then a dialog box appears with the **Job ID** and a link for your import job. Select the link and review the details on the **Jobs** page.
     * If the job _cannot_ be processed immediately, then a message appears with a **Schedule ID** in it. Copy that **Schedule ID** , and use it to search for the job on the **Jobs** page. The job appears when processing completes.
**Tip** A job ID is assigned to each file that's imported or exported, for auditing purposes.
  7. If needed, go to the **Jobs** page, locate, and open the job that you want to view.
A table appears that displays the user names or group names, classification types (User or Group), and status of the users and groups that you imported and assigned to Oracle application roles in the identity domain.

See [Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/export-job-errors.htm#export-job-errors "Download a comma-separated value \(CSV\) file of job errors for an identity domain in IAM to a local machine so that you can review and correct them.") to download a CSV file of any errors to your local machine.
Was this article helpful?
YesNo

