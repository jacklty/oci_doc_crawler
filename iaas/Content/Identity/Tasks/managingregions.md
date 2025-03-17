Updated 2025-01-14
# Managing Regions
This topic describes the basics of managing your region subscriptions. For more information about regions in Oracle Cloud Infrastructure, see [Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#top). For information about Platform Services regions, see [Managing Platform Services Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregionsplatform.htm#Managing_Platform_Services_Regions).
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access to manage region subscriptions. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for managing regions or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## The Home Region 🔗 
When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one region. This is your _home region_. Your home region is where your IAM resources are defined. When you subscribe to another region, your IAM resources are available in the new region, however, the master definitions reside in your home region and can only be changed there.
**Important** Your home region contains your account information and identity resources. It is not changeable after your tenancy is provisioned. If you are unsure which region to select as your home region, contact your sales representative before you create your account
Resources that you can create and update only in the home region are:
  * Users
  * Groups
  * Policies
  * Compartments
  * Dynamic groups
  * Federation resources


When you use the API to update your IAM resources, you must use the endpoint for your home region. (See [What is the tenancy home region? How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How)) IAM automatically propagates the updates to all regions in your tenancy.
When you use the Console to update your IAM resources, the Console sends the requests to the home region for you. You don't need to switch to your home region first. IAM then automatically propagates the updates to all regions in your tenancy.
When you subscribe your tenancy to a new region, all the policies from your home region are enforced in the new region. If you want to limit access for groups of users to specific regions, you can write policies to grant access to specific regions only. For an example policy, see [Restrict admin access to a specific region](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#restrict-admin-to-specific-region).
**Note**
IAM Updates Are Not Immediate Across All Regions
When you create or update an IAM resource, be aware that you need to allow up to several minutes for the changes in your home region to become available in all regions.
## Provisioning SaaS Applications and Geo-Regions 🔗 
SaaS applications are provisioned in the geo-region specified on your order.
After creating a cloud account to add your subscription, a Default identity domain is created in the _home region_. For SaaS applications, the _home region_ isn't the provisioning location. SaaS applications are provisioned in the Data Center region (sometimes called the _geo-region_) specified on your order. For example, the North America _geo-region_ includes three regions (Ashburn, Phoenix, and Toronto).
**Note**
Depending on the SaaS application, the application user credentials might also be stored at the same _home region_ as the Default identity domain. 
In some cases, the home region displayed in the Console may be different than the Data Center Region that you selected or is identified in your order for your Services. The information stored in your home region consists of only cloud services administrator credentials that are shared with Oracle to create and manage the Oracle Cloud account and is information that is required to log in to your account. Your Oracle Application services production and backup data remain permanently stored by Oracle only in the Data Center Region that is identified in your order.
For more information about identity domains, see [Managing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/overview.htm#overview-identity-domains "An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On \(SSO\) configuration, and SAML/OAuth based Identity Provider administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings \(such as MFA\).")
## Using the Console to Manage Infrastructure Regions 🔗 
[To view the list of infrastructure regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
Open the Console, open the **Region** menu, and then select **Manage Regions**. A list of the regions offered by Oracle Cloud Infrastructure is displayed. Regions in the same realm that you have not subscribed to provide a button to create a subscription. See [About Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#About__The) for tables listing the commercial regions and realms. 
[To subscribe to an infrastructure region](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
  1. Open the Console, open the **Region** menu, and then select **Manage Regions**. The list of regions available to your tenancy is displayed. Your home region is labeled.
  2. Locate the region you want to subscribe to and select **Subscribe**.
**Note** It could take several minutes to activate your tenancy in the new region.
Remember, your IAM resources are global, so when the subscription becomes active, all your existing policies are enforced in the new region. 
To switch to the new region, use the **Region** menu in the Console. See [Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin) for more information.


You cannot unsubscribe from a region.
## Using the API to Work with Infrastructure Regions 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage infrastructure regions:
  * [GetTenancy](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tenancy/GetTenancy)
  * [ListRegions](https://docs.oracle.com/iaas/api/#/en/identity/latest/Region/ListRegions): Returns a list of regions offered by Oracle Cloud Infrastructure in your selected **realm**.
  * [CreateRegionSubscription](https://docs.oracle.com/iaas/api/#/en/identity/latest/RegionSubscription/CreateRegionSubscription)
  * [ListRegionSubscriptions](https://docs.oracle.com/iaas/api/#/en/identity/latest/RegionSubscription/ListRegionSubscriptions)


You cannot unsubscribe from a region.
## Region FAQs 🔗 
[Can an individual user subscribe to a region?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
A region subscription is at the tenancy level. An administrator can subscribe the tenancy to a region. All IAM polices are enforced in the new region, so _all_ users in the tenancy will have the same access and permissions in the new region.
[Can I see my existing resources in the new region?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
When you select a region in the Console, you are shown a view of the resources in your selected region. Most cloud resources (instances, VCNs, buckets, etc.) exist only in a specific region, so you only see them when you select the region where they were created. The exception is IAM resources: compartments, users, groups, and policies are global across all regions. See also [Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
[How do my service limits apply to the new region?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
Service limits can be scoped to the tenant level, the region level, or the availability domain level. When you subscribe to a new region, you get access to the region and its availability domains. Service limits apply accordingly. The [service limits page](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.") lists the scope of each resource limit.
[Can I restrict access to a specific region?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
Yes. You can write policies that grant permissions in a specified region only. For an example policy, see [Restrict admin access to a specific region](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#restrict-admin-to-specific-region).
[Can I change my home region?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm)
No. Oracle assigns your home region and you can't change it. See also: [What is the tenancy home region? How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How)
Was this article helpful?
YesNo

