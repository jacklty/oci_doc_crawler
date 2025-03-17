Updated 2025-01-14
# Creating a Secure Form Fill Configuration File
You use the Secure Form Fill Admin Client (Oracle Enterprise Single Sign-On (ESSO) Administrative Console) to create secure form fill configuration files for your custom secure form fill apps in IAM. Use these instructions to create secure form fill configuration files and then import those files into IAM.
**Before You Begin:**
Install the Secure Form Fill Admin Client. See [Install the Secure Form Fill Admin Client](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/install-secure-form-fill-admin-client.htm#install-secure-form-fill-admin-client "You use the Secure Form Fill Admin Client \(Oracle Enterprise Single Sign-On \(ESSO\) Administrative Console\) to create and update secure form fill configuration files for your custom secure form fill apps in IAM. Use these instructions to install the Secure Form Fill Admin Client.").
**Note** This documentation explains, at a high level, how to use the Secure Form Fill Admin Client only as it pertains to custom secure form fill apps and IAM. For additional instructions, see the help in the ESSO Administrative Console.
  1. Launch the Secure Form Fill Admin Client.
  2. Right-click **Applications** , and then choose **New Web App**. Alternatively, use any of the following options:
     * Select **Applications** , **Add** , and then choose **Application Type: Web** in the first pane of the wizard.
     * Choose **Insert** , **Application** , and then choose **Application Type: Web** in the first pane of the wizard.
  3. On the Add Application dialog, enter the name of the application.
**Important** The application name must be the same name that you use when you create the secure form fill application in IAM.
  4. Leave all other default options selected, and then select **Finish**.
  5. Choose the **Logon** form type. This form is used to set up your Web app template.
**Note** No other form type is supported.
  6. In the **Address** field, enter the URL for the Web app, select **Go** , and then navigate to the login page.
A list of all fields on the login page appear on the bottom of the screen. Select any field in the list on the bottom of the screen to highlight the field on the page.
  7. Using the fields on the bottom of the screen, complete the following steps:
**Note**
Do no use the **Third Field** or **Fourth Field** options.
Do not use the **Allow multiple field designation** option.
Only use ordinals if field names or attribute level matching is not possible. Using ordinals is less amenable to page changes or differences across browsers, and are not recommended in most scenarios.
    1. Select the user name field, right-click, and then choose **Username/ID**.
    2. Select the password field, right-click, and then choose **Password**.
    3. Select the submit button, right-click, and then choose **Submit**.
  8. Select **OK**.
  9. On the Web dialog, make any of the following changes as necessary.
Option | Description  
---|---  
**Identification Tab** |  Select **Edit** to make changes. This is the URL or the URLs of the form to configure. For applications that have varying text in their URLs, you can use substrings or regular expressions to specify how to match the variable text. Your Match Type change options are: 
     * **Exact Match.** Exact match matches a URL exactly as specified. This is generally an edge case and rarely used.
     * **Wildcards.**
       * ? matches any single character.
       * * matches zero or more occurrences of any character. If wild cards are used, to avoid a potential security issue, do not perform mid-string wildcard matches. Always exact match the start of the URL, for example, `https://server?.somesite.com/*`.
     * **Regular Expressions.** This is the recommended option. Use the set of regular expressions to specify a string pattern that the form-fill agent should recognize as a match, for example, `URL1=.*?https://www\.expedia\.co\.jp/user/login.*`  
**Fields Tab** |  Select a field, and then using the **Edit** button, adjust the primary form fields used for detection and injection of the user name and password fields as well as the submit button. **Note:** Do not use the **SendKeys** or the **SendKeys using journal hook** options. Check each field type to ensure that it is the appropriate type (such as Password for password input fields, and so on). Your Field options are: 
     * **Field Identification.** Allows you to fine-tune how the input fields for the form are located. Field identification can be adjusted for any form field. Select the ellipsis to display the Field identification options. Identify fields by:
       * **Name.** The default and recommended option. Beware that not every input field has a name or sometimes the name is not consistent every time the page is loaded. If so, then it's recommended to use the Matching option.
       * **Ordinal.** This option identifies fields based on sequence. This option is not the recommended alternative since it is easily impacted by minor changes to the page. Also, the fields and the field ordinals can be inconsistent across browsers.
       * **Matching.** Identifies fields based on tag types, attribute values, HTML, and so on. This option is the recommended option if Name is not possible. Often, matching is used to match the "id" attribute of the input field or a regex on the name attribute. Matching can be a regex, substring match, or whole string match.
     * **Events.** Pre Inject and Post Inject events allow secure form fill to trigger a specific event on the field before and after injecting the credentials into that field. This is useful as some fields will not recognize that injection has occurred unless a specific event is triggered in that field. Event values are: blur, change, select, focus, focusin, focusout, input, keydown, keypress, keyup, and mouseover.   
**Matching Tab** |  Create or modify granular page matching criteria for the selected web form. Secure Form Fill in IAM uses the matching criteria you supply here to distinguish among similar forms. Matching can also be used to refine the detection match criteria, that is, the set of HTML tags and values you use to identify a specific field to perform more specific matching beyond just the form fields themselves.  
**Proxy Tab** |  Do not change these settings.  
  10. Select **OK**.
  11. Use the following tabs to make any necessary changes:
**Note** Do not change any other options on any other sub tabs other than those listed in the table below.
Option | Description  
---|---  
**General Tab** |  Enter a description for the Web app. Add, edit, or delete forms. This option allows you to set all the forms relevant for this Web app. Use this option if you have multiple login forms for your Web app. All other settings are not required for secure form fill and should not be changed.  
**Error Loop Tab** |  Secure form fill supports the detection of an error loop condition. Error loop conditions generally occur if secure form fill has the wrong credentials for the Web app and attempts to submit these credentials repeatedly to the Web app.
     * **Logon timeout (sec.).** The maximum time in seconds between successive logon attempts before a logon error is triggered.
     * **Max. retries.** The maximum number of retries (after first try) allowed before a logon error is triggered.  
**Miscellaneous Tab** | 
     * **Logon Loop Grace Period.** Allows control over the response during login grace period (for example, controls reinjection).
     * **Auto-submit.** Use this option to turn auto-submit on or off for all forms used by the app.  
  12. Select **File** , and then **Save**.
**Tip** Name the Web app file, the *.ini file, and the name of the IAM app with the same name.
  13. To export the file, select **File** , **Export** , select the application to export, and then select **OK**.
  14. Name the file.
**Important** The *.ini file name must match the name of the application created in IAM.

**Post requisite:** Create an IAM secure form fill app.
Was this article helpful?
YesNo

