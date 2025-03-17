Updated 2025-01-06
# Editing an Existing Filter Group
You can add a filter to an existing filter group, change the values selected for a particular filter in the filter group, or delete a filter from the filter group.
**Note** You can't modify filter groups when a language display preference is part of a subscription. If you need changes to filter groups, you must create a new subscription.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to update, and then click the subscription name.
    4. Under **Filter groups** , find the filter you want to edit. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    5. Do one or more of the following:
       * To add a filter, click **+ Another filter** , and then continue to the next step.
       * To change the value of an existing filter, click **Value** and then either delete a value or specify a new value. To delete a value, click the X next to the value name. To specify a new value, enter a new value or click the arrows to choose from a menu, as appropriate. For help with entering a new value, refer to the table in the next step.
       * To delete a filter, click the X on the filter row.
    6. If, in the previous step, you deleted a filter, continue to the next step. Otherwise, click **Type** , and then use the following table to configure a **Value** for what announcements you want to receive:
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
    7. When you're finished, click **Submit**.
  * Use the [oci announce announcement-subscription update-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/update-filter-group.html) command and required parameters to update an existing filter group in an announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription update-filter-group --announcement-subscription-id <announcementsubscription_OCID> --filter-group-name <filter_group_name> --filters <filter_JSON>
```

For example, to add a filter: ```
oci announce announcement-subscription update-filter-group --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --filter-group-name filtergroup1 --filters file://filters.json
```

Or, to update the values selected for a given filter: ```
oci announce announcement-subscription update-filter-group --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --filter-group-name filtergroup1 --filters file://filters.json
```

Or, to delete a filter from the filter group: ```
oci announce announcement-subscription update-filter-group --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --filter-group-name filtergroup1 --filters file://filters.json
```

For more information about filter group options, see [FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails).
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/UpdateFilterGroup) operation to update an existing filter group in an announcement subscription.


Was this article helpful?
YesNo

