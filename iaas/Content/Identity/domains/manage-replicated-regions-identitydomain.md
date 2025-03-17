Updated 2025-02-03
# Managing High Availability for Sign-in to the Console
Maximize High Availability for the Console by replicating identity domains in other regions. Replicating identity domains lets users sign in to the Console when the home region is unavailable.
The system detects when the home region is unavailable and redirects the sign in request to a replicated region. Users that sign in through a replicated region have only READ access to identity resources, however they can manage all workloads in that region. For example:
  * Users can view or list global IAM resources, such as policies.
  * Users can view or list domain resources, such as users, groups, applications, and more.
  * Users can't change, update, or create identity domain resources until the home region becomes available.
  * Users can manage their OCI resource in the subscribed region, such as create compute instances, access object buckets, and more.


When the home region recovers, the Console notifies the user with a message. Users can continue the using the existing session or they can sign out and then sign-in to the Console for complete access in OCI.
To enable high-availability for the Console we recommend that you subscribe to more than one region for an identity domain.
High Availability Console sign in automatically activates when:
  * The home region subscribes to at least one alternate region. See [Subscribing to an Infrastructure Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#subscribe "Subscribe to an infrastructure region in IAM.")
  * The home region is replicated by at least one alternate region. See [Replicating an Identity Domain to Multiple Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#manage-domain-regions "You can replicate an identity domain in IAM to additional regions to enable users in that domain to interact with OCI resources in those regions.").


**Note**
Tenancies created after Aug. 15 2024 support high availability for Console sign in.
Was this article helpful?
YesNo

