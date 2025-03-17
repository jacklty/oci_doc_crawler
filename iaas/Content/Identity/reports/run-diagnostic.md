Updated 2025-01-14
# Running the Diagnostic Data Report
Run a diagnostic data report for an IAM identity domain.
Use the [diagnostic data report](https://docs.oracle.com/en-us/iaas/Content/Identity/reports/diagnostic.htm#diagnostic-report "The diagnostic data report shows logging data captured in an IAM identity domain for diagnostic purposes.") to view data captured for an identity domain. You perform two separate actions to get diagnostic data:
  * Set the diagnostics type, which sets the level at which you capture operational logs. You do this in the **Settings** area.
  * Run the diagnostic data report in the **Reports** area.


After setting the diagnostics type and running the diagnostic data report, diagnostic data is captured for the next 15 minutes. After 15 minutes, the diagnostics type reverts to **None**.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, click **Settings**.
  4. Select **Diagnostics** , and then select the diagnostics type:
     * **None** doesn't collect any activity.
     * **Activity View** captures only high-level logging information only.
     * **Data View** captures mid level and high-level logging information.
     * **Service View** captures detailed logging information.
  5. Select **Identify item in search results** to identify the resources returned in the diagnostic log.
  6. Select **Save changes** to activate data logging in IAM.
  7. Go back to the Domain details page, and select **Reports**.
  8. Under **Diagnostics data report** , select **View report**.
  9. On the report page, enter filter values, such as dates and user names, to search for specific information.
  10. On the **Diagnostic Report** page, select **Run report**.
The report results are displayed on the page. You can download the results. IAM supports CSV report generation.
  11. Optionally, download the results by selecting **Download report**.
The report is created and saved at the location you choose or opened in Excel


Was this article helpful?
YesNo

