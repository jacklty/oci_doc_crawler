Updated 2024-09-26
# Viewing Tenancy Details
This topic describes options on the tenancy details page in the Console.
## Details About Your Tenancy 🔗 
The tenancy details page provides the following information about your tenancy: 

TENANCY OCID
    Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). You need your tenancy's OCID to use the API. You'll also need it when contacting support. 

HOME REGION
    When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one of the available regions. This is your _home region_. Your home region is where your IAM resources are defined. For more information about the home region, see [The Home Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Home). 

NAME
    The tenancy name. Your tenancy name is chosen when you set up your Oracle Cloud account. You can rename your tenancy. For more information, see [Renaming a Tenancy and Cloud Account](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/renamecloudaccount.htm#Renaming_a_Cloud_Account "Use the Rename Tenancy button on the Tenancy details page to rename a tenancy and cloud account."). 

CSI NUMBER
    Your Customer Service Identifier for Oracle Support.  

AUDIT RETENTION PERIOD
    The retention period for the Audit service logs. The value of the retention period setting affects all regions and all compartments for this tenancy. You can't set different retention periods for different regions or compartments. For more information about this setting, see [Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm). 

OBJECT STORAGE DESIGNATED COMPARTMENTS AND NAMESPACE
    The Object Storage service provides API support for both Amazon S3 Compatibility API and Swift API. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. You can designate a different compartment for the Amazon S3 Compatibility API or Swift API to create buckets in. For more information, see [Designating Compartments for the Amazon S3 Compatibility and Swift APIs](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm).     For information about your Object Storage namespace, see [Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm). 

TAGS
     Tagging allows you to define keys and values and associate them with resources. You can then use the tags to help you organize and list resources based on your business needs. If you have permissions to manage the tenancy, you also have permissions to apply free-form tags. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 

SERVICE LIMITS
    The limits allotted to your tenancy and usage against these limits. Not all service resources are included in the list shown here on the Console. For more information or to request an increase, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access to manage the tenancy. 
**Important** Granting users or groups the identity domain administrator role for domains other than the default domain grants them full administrator permissions to only that domain (not to the tenancy). At least one administrator for the identity domain must be granted the identity domain administrator role directly. This is in addition to any identity domain administrator roles granted by group membership. For more information, see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
If you're new to policies, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

