Updated 2024-06-06
# Details for the Marketplace Service
Details for the Marketplace Service
This topic covers details for writing policies to control access to the Marketplace service.
## Individual Resource-Type 🔗 
`marketplace-listings`
`marketplace-publications`
`marketplace-community-listings`
## Supported Variables 🔗 
Marketplace supports all the general variables, plus the ones listed here. Specifically, you can use the variables listed here when writing policies that grant `read`, `use`, and `manage` verbs. You cannot use them with the `inspect` verb. For more information about general variables supported by Oracle Cloud Infrastructure services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
Resource-Type | Variable | Variable Type | Description  
---|---|---|---  
`marketplace-listings` | `listing.id` | String | Use this variable to control whether to return a specific listing (based on the given listing ID) in response to a request.  
`marketplace-listings` | `listing.publisher.id` | String | Use this variable to control whether to return only listings from a specific publisher (based on the given publisher ID) in response to a request.  
`marketplace-community-listings` | `listing.id` | String  
`marketplace-publications` | `listing.id` | String | Use this variable to control whether to return a specific publication (based on the given listing ID) in response to a request.  
`marketplace-publications` | `listing.type` | String | Use this variable to control whether to return only listings from a specific publisher category (based on the given listing type) in response to a request. A publication's publisher category informs where the listing appears for use.  
`marketplace-publications` | `listing.destination-compartment.id` | String  
`marketplace-publications` | `listing.source-compartment.id` | String  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` verb for the `marketplace-listings` resource-type includes the same permissions and API operations as the `read` verb, plus the MARKETPLACE_LISTING_LAUNCH permission and an additional API operation, `LaunchListing`. However, the `manage` verb covers no extra permissions or API operations compared to `use`.
[marketplace-listings](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/marketplacepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | MARKETPLACE_LISTING_INSPECT | `ListListings` | none  
read | INSPECT + MARKETPLACE_LISTING_READ | INSPECT + `GetListing` | none  
use | READ + MARKETPLACE_LISTING_LAUNCH | READ + `LaunchListing` | none  
manage | no extra | no extra | none  
[marketplace-publications](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/marketplacepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  MARKETPLACE_PUBLICATION_INSPECT |  `ListPublications` `ListPublicationPackages` |  none  
read |  INSPECT + MARKETPLACE_PUBLICATION_READ |  INSPECT + `GetPublication` `GetPublicationPackage` |  none  
use |  READ + MARKETPLACE_PUBLICATION_UPDATE |  READ + `UpdatePublication` |  none  
manage |  USE + MARKETPLACE_PUBLICATION_CREATE MARKETPLACE_PUBLICATION_DELETE MARKETPLACE_PUBLICATION_MOVE |  `CreatePublication` `DeletePublication` `ChangePublicationCompartment` |  none  
[marketplace-community-listings](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/marketplacepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
read |  MARKETPLACE_COMMUNITY_LISTING_READ |  `GetLaunchEligibility` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListListings` | MARKETPLACE_LISTING_INSPECT  
`GetListing` | MARKETPLACE_LISTING_READ  
`LaunchListing` | MARKETPLACE_LISTING_LAUNCH  
`ListPublications` | MARKETPLACE_PUBLICATION_INSPECT  
`ListPublicationPackages` | MARKETPLACE_PUBLICATION_INSPECT  
`GetPublication` | MARKETPLACE_PUBLICATION_READ  
`GetPublicationPackage` | MARKETPLACE_PUBLICATION_READ  
`UpdatePublication` | MARKETPLACE_PUBLICATION_UPDATE  
`CreatePublication` | MARKETPLACE_PUBLICATION_CREATE  
`DeletePublication` | MARKETPLACE_PUBLICATION_DELETE  
`ChangePublicationCompartment` | MARKETPLACE_PUBLICATION_MOVE  
`GetLaunchEligibility` | MARKETPLACE_COMMUNITY_LISTING_READ  
Was this article helpful?
YesNo

