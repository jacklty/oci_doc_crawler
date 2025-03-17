Updated 2025-02-18
# Exporting Users
Export users to a comma-separated values (CSV) file.
You can export the users for the following attributes only: _User Name_ , _Work Email_ , _Home Email_ , _Primary Email Type_ , _Honorific Prefix_ , _First Name_ , _Middle Name_ , _Last Name_ , _Honorific Suffix_ , and _Password_.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  2. Select the checkbox for each user that you want to export. 
  3. From the **More actions** menu, select **Export users**.
  4. In the **Export users** window, select **Export**.
  5. After the job completes, review the job results.
     * If the job _can_ be processed immediately, then a dialog box appears with the **Job ID** and a link for your import job. Select the link and review the details on the **Jobs** page.
     * If the job _cannot_ be processed immediately, then a message appears with a **Schedule ID** in it. Copy that **Schedule ID** , and use it to search for the job on the **Jobs** page. The job appears when processing completes.
  6. If needed, go to the **Jobs** page, locate, and open the job that you want to view.
A page shows how many users you exported, how many accounts exported successfully, and how many accounts can't be exported because of a system error.
  7. Select **Download exported file**.
  8. Save your file in a UTF-8 format. Saving the file in UTF-8 format ensures that non-English characters display properly. 
    1. Open the CSV file with a text editor, such as Notepad. 
    2. Save the file with UTF-8 for encoding.
  9. (Optional) In addition to saving the file in UTF-8 format, if you're using Microsoft Excel to open and save the file, perform the additional steps to ensure that non-English characters display properly.
    1. In Microsoft Excel, open a new workbook, select the **Data** tab, and then choose **From Text/CSV**.
    2. On the **Import Data** window, choose your CSV file, and then select **Import**.
    3. For **File Origin** , select **65001: Unicode (UTF-8)**.
    4. For **Delimiters** , select **Comma**. 
    5. For **Data Type Detection** , select **Based on first 200 rows** , and then select **Transform Data**.
    6. Select **Close and Load**. 
    7. Save the file.

See [Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/export-job-errors.htm#export-job-errors "Download a comma-separated value \(CSV\) file of job errors for an identity domain in IAM to a local machine so that you can review and correct them.") to download a CSV file of any errors to your local machine.
Was this article helpful?
YesNo

