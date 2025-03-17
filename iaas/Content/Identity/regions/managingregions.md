Updated 2024-09-26
# Managing Regions
This topic describes the basics of managing your region subscriptions. For more information about regions in Oracle Cloud Infrastructure, see [Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#top). For information about Platform Services regions, see [Managing Platform Services Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/platformsvcregions/managingregionsplatform.htm#Managing_Platform_Services_Regions).
This section contains the following topics.
  * [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#one)
  * [The Home Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Home)
  * [Provisioning SaaS Applications and Geo-Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#provisioning_saas_applications_geo_regions "SaaS applications are provisioned in the geo-region specified on your order.")
  * [Find Out More](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#regfaq)
  * [Listing Infrastructure Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm#To_view_the_list_of_infrastructure_regions "View a list of all infrastructure regions in IAM.")
  * [Listing Subscribed Infrastructure Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/list_subscribed_infrastructure_regions.htm#subscribe "View a list of regions you're subscribed to in IAM.")
  * [Subscribing to an Infrastructure Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#subscribe "Subscribe to an infrastructure region in IAM.")


## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access to manage region subscriptions. 
If you're new to policies, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies."),.
## The Home Region 🔗 
When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one region. This is your _home region_. Your home region is where your IAM resources are defined. When you subscribe to another region, your IAM resources are available in the new region. However, the definitions reside in your home region and can only be changed there.
**Important** Your home region contains your account information and identity resources. You can't make changes after your tenancy is provisioned. If you're unsure which region to select as your home region, contact your sales representative before you create your account.
Resources that you can create and update only in the home region are:
  * Users
  * Groups
  * Policies
  * Compartments
  * Dynamic groups
  * Federation resources


When you use the API to update your IAM resources, you must use the endpoint for your home region. (See [What is the tenancy home region? How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How)) IAM automatically propagates the updates to all regions in your tenancy.
When you use the Console to update your IAM resources, the Console sends the requests to the home region for you. You don't need to switch to your home region first. IAM then automatically propagates the updates to all regions in your tenancy.
**Note**
IAM Updates Aren't Immediate Across All Regions
When you create or update an IAM resource, be aware that it might take several minutes for the changes in your home region to become available in all regions.
When you subscribe your tenancy to a new region, you can replicate the home region in one or more alternate regions. If you home region is down, you can sign in to the tenancy. Full IAM functionality is limited until the home region is back up. To subscribe to a new region, see [Subscribing to an Infrastructure Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#subscribe "Subscribe to an infrastructure region in IAM.").
The policies from the home region are enforced in the new region. To limit access for groups of users to specific regions, you can write policies to grant access to specific regions only. For an example policy, see [Restrict admin access to a specific region](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#restrict-admin-to-specific-region).
**Note**
## Provisioning SaaS Applications and Geo-Regions 🔗 
SaaS applications are provisioned in the geo-region specified on your order.
After creating a cloud account to add your subscription, a Default identity domain is created in the _home region_. For SaaS applications, the _home region_ isn't the provisioning location. SaaS applications are provisioned in the Data Center region (sometimes called the _geo-region_) specified on your order. For example, the North America _geo-region_ includes three regions (Ashburn, Phoenix, and Toronto).
**Note**
Depending on the SaaS application, the application user credentials might also be stored at the same _home region_ as the Default identity domain. 
In some cases, the home region displayed in the Console may be different than the Data Center Region that you selected or is identified in your order for your Services. The information stored in your home region consists of only cloud services administrator credentials that are shared with Oracle to create and manage the Oracle Cloud account and is information that is required to log in to your account. Your Oracle Application services production and backup data remain permanently stored by Oracle only in the Data Center Region that is identified in your order.
For more information about identity domains, see [Managing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/overview.htm#overview-identity-domains "An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On \(SSO\) configuration, and SAML/OAuth based Identity Provider administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings \(such as MFA\).")
## Find Out More 🔗 
[Can an individual user subscribe to a region?](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
A region subscription is at the tenancy level. An administrator can subscribe the tenancy to a region. All IAM polices are enforced in the new region, so _all_ users in the tenancy will have the same access and permissions in the new region.
[Can I see my existing resources in the new region?](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
When you select a region in the Console, you are shown a view of the resources in your selected region. Most cloud resources (instances, VCNs, buckets, etc.) exist only in a specific region, so you only see them when you select the region where they were created. The exception is IAM resources: compartments, users, groups, and policies are global across all regions. See also [Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
[How do my service limits apply to the new region?](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
Service limits can be scoped to the tenant level, the region level, or the availability domain level. When you subscribe to a new region, you get access to the region and its availability domains. Service limits apply accordingly. The [service limits page](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.") lists the scope of each resource limit.
[Can I restrict access to a specific region?](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
Yes. You can write policies that grant permissions in a specified region only.
[Can I change my home region?](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
No. Oracle assigns your home region and you can't change it. See also: [What is the tenancy home region? How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How)
Was this article helpful?
YesNo

