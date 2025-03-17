Updated 2023-01-31
# Import File Specifications
Learn about import file specifications to reduce the possibility of errors.
Whether you're importing users, groups, or Oracle application roles, the import file itself must meet the following specifications:
  * Use a comma as the delimiter between the values
  * Save the file in a CSV format (*.csv)
  * Limit file size to 52 MB


**Tip**
Import just one _user_ to familiarize yourself with the process. You can then import a larger set of _users_ , for example, 100 _users_. If you don't experience any import errors, increase the import file size according to your comfort level.
The import file is a simple text file in a tabular format (rows and columns). The first row in the file defines the columns (fields) in your table. At a minimum, the import file must have these exact column headings.
Import File | Required Column Headings  
---|---  
Users |  User ID Last Name First Name Work Email  
Groups |  Display Name Description User Members Requestable  
Application Role Membership |  Entitlement Value Grantee Name Grantee Type App Name  
For each account, create a row (line) and enter data into each column (field). Each row equals one record.
To create an import file, you can use a standard spreadsheet application, such as Microsoft Excel or Google Sheets, or you can use a text editor, such as Notepad or TextPad.
**Important** Whichever application you use to create the file, ensure that you save the file in a valid CSV format.
Spreadsheet applications make it easy to create, edit, and save import files. You can use standard features to add and delete rows of data, edit individual fields, search for records, or sort the list. The following illustration shows an example of _group_ account data defined in a Microsoft Excel file. The layout lets you easily review the data.
[![CSV file displayed using Microsoft Excel.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-csv-import-file-displayed-ms-excel-file.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-csv-import-file-displayed-ms-excel-file.png)
When you save your spreadsheet as type CSV (*.csv), a comma separates the values in each row. For example, the following illustration shows the group data from the Microsoft Excel spreadsheet, saved as CSV file, and opened in Notepad.
![CSV file displayed using Notepad.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-csv-import-file-displayed-notepad.png)
Was this article helpful?
YesNo

