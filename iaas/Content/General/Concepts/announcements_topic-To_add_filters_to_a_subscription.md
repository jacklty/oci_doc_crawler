Updated 2025-01-06
# Adding a Filter Group to an Existing Subscription
You can add a filter group to an existing subscription.
**Note** You can't create a subscription with multiple filter groups when any filter group specifies Oracle Fusion Applications as the service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to update, and then click the subscription name.
    4. Under **Filter groups** , click **Add filter group**.
    5. Click **Name** , and then enter a name for the filter. Avoid entering confidential information.
**Note** Include only alphanumeric, hyphen, underscore, or whitespace characters in the filter group name.
    6. Under **Filters** , click **Type** , and then use the following table to configure a **Value** for what announcements you want to receive:
**Note** You can't have more than one of any particular filter type within a filter group.
Option | Description  
---|---  
**Announcement type** | Specify an announcement type to include in the filter. Every announcement is assigned to a category that helps you understand the relative severity of the information in the announcement. For more information, see [Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Types).  
**Compartment** | Specify a compartment to include in the filter. Not all announcements impact a specific compartment, but this filter lets you include announcements that do. **Note:** If you specify the root compartment, then subscribers receive all announcements for the tenancy. However, if you want all announcements, then we recommend you create a subscription for all announcements instead of creating a subscription for selected announcements only.  
**Platform** | Specify whether you want to see announcements that impact the Oracle Cloud Infrastructure (**IaaS**) platform or announcements that impact Software as a Service (**SaaS**) applications.  
**Region** | Specify a region to include in the filter.  
**Resource OCID** | Specify up to 5 resources that you want to include in the filter by doing the following:
       * Click **Browse** , select the check box next to the resource that you want to include, and then click **Add to filter**. (If needed, to list resources in a different compartment, click **Compartment** and choose a compartment.)
**Note:** You can't combine this filter with any other type of filter in a particular filter group.  
**Service** |  Select the name of the service that you want to include. To narrow the list, you can type or otherwise enter the service name. Not all announcements impact a particular service, but this filter lets you include announcements that do. If a filter specifies more than one service, then the Announcements service notifies subscribers of announcements impacting any of the specified services. **Note:** When you create a subscription based on a service, you get all the announcements for that service. You don't need to separately create a subscription for each region where you use the service.  
    7. (Optional) To add another filter to the filter group, click **+ Another filter** , and then repeat the previous step. (You can't do this if the filter you created in the previous step specified resource OCIDs. You can't combine that type of filter with any other filter in a particular filter group.)
    8. When you're finished, click **Submit**.
  * Use the [oci announce announcement-subscription create-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/create-filter-group.html) command and required parameters to add a filter group to an existing announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription create-filter-group --announcement-subscription-id <announcementsubscription_OCID> --filters <filter_JSON> --name <filter_group_name>
```

For example: ```
oci announce announcement-subscription create-filter-group --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --filters file://filters.json --name newfiltergroup
```

For more information about filter group options, see [FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails).
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/CreateFilterGroup) operation to add a filter group to an existing announcement subscription.


Was this article helpful?
YesNo

