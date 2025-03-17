Updated 2025-02-13
# Console Announcements
This topic describes the announcements that Oracle Cloud Infrastructure displays in the Console. Console announcements communicate timely, important information about service status. You can view a list of ongoing and past announcements. If you want to receive announcements through email or another delivery mechanism, you can manage tenancy administrator email preferences or configure announcement subscriptions.
**Note**
  * If you use Oracle Platform Cloud Services or Oracle Cloud Applications and you have announcements about those service entitlements, the displays a banner with a link that you can use to access those announcements. For more information about these announcements, including how to set notification preferences, see [Monitoring Notifications.](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/mmocs/monitoring-notifications.html)


**Tip** Watch a [video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31897) to the service.
For more information about the ways that you can work with announcements, see the following:
  * [Viewing Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Viewing_Announcements.htm#viewing "View announcements. The Announcements icon displays a green dot if you have any unread announcements.")
  * [Email Delivery](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Email_Delivery.htm#email "As part of an organization's service agreement, Oracle Cloud Infrastructure also contacts the tenancy administrator with service status announcements through email.")
  * [Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm#subscriptions "Create and manage announcement subscriptions.")


## Types of Announcements 🔗 
Announcements belong to different categories. An announcement's prefix helps you understand, at a glance, the type and relative severity of the information and whether there's anything you can or must do. Announcement types currently include the following, in order of most important to least:
  * **Required action.** You must take specific action within your environment.
  * **Emergency change.** There is a time period during which an unplanned, but urgent, change associated with your environment will take place.
  * **Emergency maintenance extended.** The emergency maintenance period has been extended beyond what was previously communicated.
  * **Emergency maintenance rescheduled.** The emergency maintenance period has been postponed to a later time or date.
  * **Recommended action.** You have specific action to take within your environment, but the action is not required.
  * **Planned change.** There is a time period during which a planned change associated with your environment will take place.
  * **Planned change extended.** The scheduled change period has extended beyond what was previously communicated.
  * **Planned change rescheduled.** The planned change to your environment has been postponed to a later time or date.
  * **Event notification.** An impactful change to your environment either recently occurred or is actively occurring.
  * **Scheduled maintenance.** There is a time period during which planned maintenance activities will be performed on your environment. Maintenance activities can include restarting services or other similarly impactful actions.
  * **Emergency maintenance completed.** Emergency maintenance affecting your environment has been completed and regular operations have resumed.
  * **Planned change completed.** The planned change to your environment has been completed and regular operations have resumed.
  * **Information.** There is information that you might find useful, but is not urgent and does not require action on your part.


For announcements that require action and affect Oracle Cloud Infrastructure Compute instances, you will get 14 days of advance notice. If you need to delay the actions described in the announcement, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) to request one of the alternate dates listed in the announcement. For some announcements, you can reschedule for a date up to 2 weeks later. Critical vulnerabilities might not be eligible for delay.
## Required IAM Policy 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
Depending on whether you have access, you might not see any announcements. With access to announcements, you can either see only the summary version of any given announcement or you can also view announcement details.
For administrators: for typical policies that give users access to announcements, see [Restrict user access to view only summary announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#restrict-users-to-general-announcements), [Let users view details of announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#allow-users-to-view-announcement-details), . For more information, see [Details for the Announcements Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/announcementspolicyreference.htm#Details_for_the_Announcements_Service).
If you're new to policies, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
## Using the Command Line Interface (CLI) 🔗 
Some command line interface (CLI) commands require complex input. For example, creating a filter group requires you to provide filters in JSON format. You can see the expected format of the input by opening a command prompt and running the command with the `--generate-full-command-json-input` option. For example, to generate the JSON for creating a filter group, run the following command:
```
oci announce announcement-subscription create-filter-group --generate-full-command-json-input
```

In the output, the following shows how to input the filters in the new filter group:
```
{
 "announcementSubscriptionId": "string",
 "filters": [
  {
   "type": "string",
   "value": "string"
  },
  {
   "type": "string",
   "value": "string"
  }
 ],
 "ifMatch": "string",
 "name": "string"
}
```

Was this article helpful?
YesNo

