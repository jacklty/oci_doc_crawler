Updated 2025-01-14
# Importing Groups
Import groups using a comma-separated values (CSV) file.
**Before you begin:**
Before you can import groups, create a CSV file that is properly formatted for the import process. To create and prepare a file for import, follow these steps.
  1. Use these [sample files](https://docs.oracle.com/iaas/Content/Resources/Assets/bulkImportSampleFilesCSV.zip) as a starting point.
  2. Extract the compressed file and then open the `Groups.csv` file.
  3. **Optional.** To familiarize yourself with the import process, consider importing just the demo data. You can then delete the unwanted demo data before you begin importing live data.
  4. Review and then delete any demo data in the `Groups.csv` file.
  5. Create an import file using the `Groups.csv` file. The `Groups.csv` file is a simple text file in a tabular format (rows and columns). The first row in the file defines the columns (fields) in your table. At a minimum, the file must have these exact column headings:
     * Display Name
     * Description
     * User Members
**Tip** Ensure that the fields in these columns are unique. Also, verify that the user names in the **User Members** column already exist in the identity domain.
For each account, you create a new row (line) and enter data into each column (field). Each row equals one record.
**Important**
The data provided in the CSV file must meet the following requirements:
     * The IDs of the users in the file must contain at least three characters. The names of the groups must contain at least five characters.
     * The telephone numbers of the users that you want to import must meet the requirements of the RFC 3966 specification.
     * The maximum number of rows in group import file must not exceed 100,000 and the import file size must not exceed 52 MB. 
To create a CSV file, you can use a standard spreadsheet application, such as Microsoft Excel or Google Sheets, or you can use a text editor, such as Notepad or TextPad.
  6. Save your file in UTF-8 format. Saving the file in UTF-8 format ensures that non-English characters display properly.
    1. Open the CSV file with a text editor, such as Notepad. 
    2. Save the file with UTF-8 for encoding. 
**Note** If you don't save the file in a CSV format with UTF-8 encoding, the import fails.


To import groups, follow these steps.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Groups**.
  2. From the **More actions** menu, select **Import groups**.
  3. In the **Import groups** window, drag and drop the file or select **Select one** to browse for the file.
  4. Select **Import**.
If a group fails to import, ensure that the group doesn't already exist, and that the required values are given. If the identity domain can't import a group, then it evaluates the next group in the CSV file. 
  5. After the job completes, review the job results.
     * If the job _can_ be processed immediately, then a dialog box appears with the **Job ID** and a link for your import job. Select the link and review the details on the **Jobs** page.
     * If the job _cannot_ be processed immediately, then a message appears with a **Schedule ID** in it. Copy that **Schedule ID** , and use it to search for the job on the **Jobs** page. The job appears when processing completes. 
**Tip** A job ID is assigned to each file that's imported or exported, for auditing purposes.
  6. If needed, go to the **Jobs** page, locate, and open the job that you want to view.
The **Job Details** page shows how many groups you imported, how many groups imported successfully, and how many groups can't be imported because of a system error. For each group that you imported successfully, this page also shows how many users are assigned to the group.

See [Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/export-job-errors.htm#export-job-errors "Download a comma-separated value \(CSV\) file of job errors for an identity domain in IAM to a local machine so that you can review and correct them.") to download a CSV file of any errors to your local machine.
Was this article helpful?
YesNo

