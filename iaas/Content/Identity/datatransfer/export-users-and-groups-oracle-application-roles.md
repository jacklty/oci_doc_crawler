Updated 2025-01-14
# Exporting Users and Groups for Oracle Application Roles
Export users and groups assigned to Oracle application roles of Oracle applications to a comma-separated values (CSV) file.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  2. In the **Applications** page, select the Oracle application that has application roles with users and groups assigned to them.
  3. Select **Application roles**.
  4. Select the checkbox for application role that you want to export and select **Export**.
  5. Select **Confirm**.
  6. After the job completes, review the job results.
     * If the job _can_ be processed immediately, then a dialog box appears with the **Job ID** and a link for your import job. Select the link and review the details on the **Jobs** page.
     * If the job _cannot_ be processed immediately, then a message appears with a **Schedule ID** in it. Copy that **Schedule ID** , and use it to search for the job on the **Jobs** page. The job appears when processing completes.
  7. If needed, go to the **Jobs** page, locate, and open the job that you want to view.
This page shows how many application roles that you attempted to export, how many application roles exported successfully, and how many application roles can't be exported because of a system error.
  8. Select **Download exported file**.

See [Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/export-job-errors.htm#export-job-errors "Download a comma-separated value \(CSV\) file of job errors for an identity domain in IAM to a local machine so that you can review and correct them.") to download a CSV file of any errors to your local machine.
Was this article helpful?
YesNo

