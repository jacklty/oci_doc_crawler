Updated 2023-12-08
# Viewing the Details of an Announcement
View detailed information when you want to know more about a particular announcement.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm)


  *     1. Do one of the following:
       * If you're viewing a banner, click the link embedded in the text of the banner.
       * If you're viewing a list of announcements, under the **Announcements** column, click the announcement summary.
    2. On the **Announcement details** page, you can view the following information:
       * **Summary.** A summary of the issue or event that serves as the announcement title.
       * **Lifecycle State.** The current lifecycle state of the announcement resource itself.
       * **Description.** A description of the issue or event that provides more detail than the summary text of the announcement.
       * **OCID.** The announcement's unique, Oracle-assigned identifier.
       * **Reference Ticket Number.** The number to use to refer to the issue when talking to Support.
       * **Type.** One of several predefined categories that helps to set expectations about the nature and severity of the issue described. For more information, see [Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Types).
       * **Affected Service.** The Oracle Cloud Infrastructure services affected by the issue or event.
       * **Region.** What Oracle Cloud Infrastructure regions are impacted.
       * **Start Time.** When the issue or event was first detected.
       * **End Time.** When the issue or event was resolved.
       * **Action Required By.** The date by which you must address any required actions described in the announcement.
       * **Created.** When the announcement was created.
       * **Updated.** When the announcement was updated.
       * **Additional Information.** Supplemental information, such as workarounds or background material.
       * **Impacted Resources.** Resources that were affected in some way by the event that prompted the announcement.
    3. (Optional) To refer to the list of impacted resources later, click **Download Impacted Resources List**.
  * Use the [oci announce announcements get](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/get.html) command and required parameters to view detailed information about an announcement:
Command
CopyTry It
```
oci announce announcements get --announcement-id <announcement_OCID>
```

For example: ```

oci announce announcements get --announcement-id ocid1.announcement.region1..<unique_ID>
```

Viewing the details of an announcement provides you with the following information:
    * **Summary.** A summary of the issue or event that serves as the announcement title.
    * **Lifecycle State.** The current lifecycle state of the announcement resource itself.
    * **Description.** A description of the issue or event that provides more detail than the summary text of the announcement.
    * **OCID.** The announcement's unique, Oracle-assigned identifier.
    * **Reference Ticket Number.** The number to use to refer to the issue when talking to Support.
    * **Type.** One of several predefined categories that helps to set expectations about the nature and severity of the issue described. For more information, see [Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Types).
    * **Affected Service.** The Oracle Cloud Infrastructure services affected by the issue or event.
    * **Region.** What Oracle Cloud Infrastructure regions are impacted.
    * **Start Time.** When the issue or event was first detected.
    * **End Time.** When the issue or event was resolved.
    * **Action Required By.** The date by which you must address any required actions described in the announcement.
    * **Created.** When the announcement was created.
    * **Updated.** When the announcement was updated.
    * **Additional Information.** Supplemental information, such as workarounds or background material.
    * **Impacted Resources.** Resources that were affected in some way by the event that prompted the announcement.
    * **Environment Name.** The name of the environment impacted by the issue or event.
    * **Platform Type.** The type of platforms affected by the issue or event, whether IaaS or SaaS.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetAnnouncement](https://docs.oracle.com/iaas/api/#/en/announcements/latest/Announcement/GetAnnouncement) operation to view the details of an announcement.


Was this article helpful?
YesNo

