Updated 2025-01-06
# Deleting a Filter Group
You can delete a filter group from an existing subscription.
**Note** You can't modify filter groups when a language display preference is part of a subscription. If you need changes to filter groups, you must create a new subscription.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to update, and then click the subscription name.
    4. Under **Filter groups** , find the filter you want to delete. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Delete**.
    5. To confirm, click **Delete**.
  * Use the [oci announce announcement-subscription delete-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/delete-filter-group.html) command and required parameters to delete a filter group from an announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription delete-filter-group --announcement-subscription-id <announcementsubscription_OCID> --filter-group-name <filter_group_name>
```

For example: ```
oci announce announcement-subscription delete-filter-group --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --filter-group-name filtergroup1
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/DeleteFilterGroup) operation to delete a filter group from an announcement subscription.


Was this article helpful?
YesNo

