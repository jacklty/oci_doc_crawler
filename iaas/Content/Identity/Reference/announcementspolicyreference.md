Updated 2024-06-06
# Details for the Announcements Service
This topic covers details for writing policies to control access to the Announcements service.
## Resource-Types 🔗 
  * `announcements`
  * `announcement-subscriptions`


## Supported Variables 🔗 
Announcements supports all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
Variable | Variable Type | Comments  
---|---|---  
`target.announcement-subscription.id` | Entity (OCID) | Use this variable to control access to an announcement subscription based on the OCID of the subscription. (You cannot use this variable when creating a subscription, as the subscription does not exist to have an OCID yet.)  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `announcements` resource-type includes the same permissions and API operations as the `inspect` verb, plus the ANNOUNCEMENT_READ permission and an additional API peration, `GetAnnouncement`. However, the `use` verb and `manage` verbs cover no extra permissions or API operations compared to `read`.
[announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/announcementspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | ANNOUNCEMENT_LIST | `ListAnnouncements` | none  
read | INSPECT + ANNOUNCEMENT_READ | INSPECT + `GetAnnouncement` | none  
use | no extra | no extra | none  
manage | no extra | no extra | none  
[announcement-subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/announcementspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  ANNOUNCEMENT_SUBSCRIPTION_INSPECT | `ListAnnouncementSubscriptions` |  none  
read |  INSPECT + ANNOUNCEMENT_SUBSCRIPTION_READ |  INSPECT + `GetAnnouncementSubscription` |  none  
use |  READ + ANNOUNCEMENT_SUBSCRIPTION_UPDATE |  `UpdateAnnouncementSubscription` `CreateFilterGroup` `UpdateFilterGroup` `DeleteFilterGroup` |  none  
manage |  USE + ANNOUNCEMENT_SUBSCRIPTION_CREATE ANNOUNCEMENT_SUBSCRIPTION_DELETE ANNOUNCEMENT_SUBSCRIPTION_MOVE |  `CreateAnnouncementSubscription` `DeleteAnnouncementSubscription` `ChangeAnnouncementSubscriptionCompartment` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi). 
API Operation | Permissions Required to Use the Operation  
---|---  
`ListAnnouncements` | ANNOUNCEMENT_LIST  
`GetAnnouncement` | ANNOUNCEMENT_READ  
`ListAnnouncementSubscriptions` | ANNOUNCEMENT_SUBSCRIPTION_INSPECT  
`GetAnnouncementSubscription` | ANNOUNCEMENT_SUBSCRIPTION_READ  
`CreateAnnouncementSubscription` | ANNOUNCEMENT_SUBSCRIPTION_CREATE  
`UpdateAnnouncementSubscription` | ANNOUNCEMENT_SUBSCRIPTION_UPDATE  
`CreateFilterGroup` | ANNOUNCEMENT_SUBSCRIPTION_UPDATE  
`UpdateFilterGroup` | ANNOUNCEMENT_SUBSCRIPTION_UPDATE  
`DeleteFilterGroup` | ANNOUNCEMENT_SUBSCRIPTION_UPDATE  
`ChangeAnnouncementSubscriptionCompartment` | ANNOUNCEMENT_SUBSCRIPTION_MOVE  
`DeleteAnnouncementSubscription` | ANNOUNCEMENT_SUBSCRIPTION_DELETE  
Was this article helpful?
YesNo

