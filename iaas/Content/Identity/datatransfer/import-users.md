Updated 2025-02-18
# Importing Users
Import users using a comma-separated values (CSV) file.
**Before you begin:**
Before you can import users, first create a CSV file that is properly formatted for the import process. To create and prepare a file for import, follow these steps.
  1. Download these [sample files](https://docs.oracle.com/iaas/Content/Resources/Assets/bulkImportSampleFilesCSV.zip) as a starting point.
  2. Extract the compressed file and then open the `Users.csv` file.
  3. **Optional.** To familiarize yourself with the import process, consider importing just the demo data. You can then delete the unwanted demo data before you begin importing live data.
  4. Review and then delete any demo data in the `Users.csv` file.
  5. Create an import file using the `Users.csv` file. The `Users.csv` file is a simple text file in a tabular format (rows and columns). The first row in the file defines the columns (fields) in your table. 
**Note**
     * The maximum number of rows in the user import file must not exceed 100,000 and the import file size must not exceed 52 MB.
     * At a minimum, the file must have these exact column headings and the fields in these columns must be unique.
       * User ID
       * Last Name
       * First Name
       * Work Email
       * Primary Email
       * Primary Email Type
     * For each account, you create a new row (line) and enter data into each column (field). Each row equals one record.
     * The telephone numbers of the users that you want to import must meet the requirements of the RFC 3966 specification.
     * When importing users, the attribute `Recovery` cannot be specified as one of valid values for **Primary Email Type**. The valid values for Primary Email Type are `home`, `work`, or `other`.
     * If you want users to use their federated accounts to sign in, then you must set the **Federated** column to `TRUE` for those users. When the federated flag is set to `TRUE`, IAM no longer manages the federated user's password. This prevents IAM from forcing a password change for these imported user accounts.
     * If you don't want users to be notified that accounts were created for them, then you must set the **ByPass Notification** column to `TRUE` for those users. The **ByPass Notification** option determines whether an email notification is sent after creating or updating a user.
     * To create a CSV file, you can use a standard spreadsheet application, such as Microsoft Excel or Google Sheets, or you can use a text editor, such as Notepad or TextPad.
  6. Save your file in UTF-8 format. Saving the file in UTF-8 format ensures that non-English characters display properly.
    1. Open the CSV file with a text editor, such as Notepad. 
    2. Save the file with UTF-8 for encoding.
**Note** If you don't save the file in a CSV format with UTF-8 encoding, the import fails. 


To import users, follow these steps. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  2. From the **More actions** menu, select **Import users**.
  3. In the **Import users** window, drag and drop the file or select **Select one** to browse for the file.
  4. Select **Import**.
If a user account is missing a required value, such as the user's first name, last name, or username, then that account won't be imported and the next user account in the CSV file is evaluated.
  5. After the job completes, review the job results.
     * If the job _can_ be processed immediately, then a dialog box appears with the **Job ID** and a link for your import job. Select the link and review the details on the **Jobs** page.
     * If the job _cannot_ be processed immediately, then a message appears with a **Schedule ID** in it. Copy that **Schedule ID** , and use it to search for the job on the **Jobs** page. The job appears when processing completes.
**Tip** A job ID is assigned to each file that's imported or exported, for auditing purposes.
  6. If needed, go to the **Jobs** page, locate, and open the job that you want to view.
A table displays the first names, last names, email addresses, user names, and statuses of the users that you imported. 
**Note**
If a user account can be imported, then a **Creation Succeeded** or **Update Succeeded** link appears for the status, depending on whether you imported a new account or modification to an existing account. To see granular details about the account, select the link.
If a user account can't be imported, then a **Creation Failed** or **Update Failed** link appears for the status. To see information about why the account or modification can't be imported, select the link.
  7. Review the details on the **Jobs** page.

See [Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/jobs/export-job-errors.htm#export-job-errors "Download a comma-separated value \(CSV\) file of job errors for an identity domain in IAM to a local machine so that you can review and correct them.") to download a CSV file of any errors to your local machine.
Was this article helpful?
YesNo

