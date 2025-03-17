Updated 2025-01-24
# Managing the Tenancy
This topic describes options on the tenancy details page in the Console.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access to manage the tenancy. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for your tenancy and other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Viewing the Tenancy Details Page 🔗 
To view the tenancy details page:
In the navigation bar, select the **Profile** menu and then select **Tenancy: <your_tenancy_name>**.
## Details About Your Tenancy 🔗 
The tenancy details page provides the following information about your tenancy: 

TENANCY OCID
    Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). You need your tenancy's OCID to use the API. You'll also need it when contacting support. 

HOME REGION
    When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one of the available regions. This is your _home region_. Your home region is where your IAM resources are defined. For more information about the home region, see [The Home Region](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#The). 

NAME
    Your tenancy name. Your tenancy name is typically chosen when you set up your Oracle Cloud account. 

CSI NUMBER
    Your Customer Service Identifier for Oracle Support.  

OBJECT STORAGE DESIGNATED COMPARTMENTS AND NAMESPACE
    The Object Storage service provides API support for both Amazon S3 Compatibility API and Swift API. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. You can designate a different compartment for the Amazon S3 Compatibility API or Swift API to create buckets in. For more information, see [Designating Compartments for the Amazon S3 Compatibility and Swift APIs](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm).     For information about your Object Storage namespace, see [Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm). 

TAGS
     Tagging allows you to define keys and values and associate them with resources. You can then use the tags to help you organize and list resources based on your business needs. If you have permissions to manage the tenancy, you also have permissions to apply free-form tags. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 

SERVICE LIMITS
    The limits allotted to your tenancy and usage against these limits. Not all service resources are included in the list shown here on the Console. For more information or to request an increase, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
## Using the API 🔗 
Many of the options set on this page are managed through the owning service. For example, the Object Storage settings are managed with the [Object Storage service API](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm), and setting the Audit log retention period is handled by the Audit service API. 
To get information about your tenancy use the following operation:
  * [GetTenancy](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tenancy/GetTenancy)


To tag a tenancy, use the following operations:
  * [GetCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/GetCompartment)
  * [UpdateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/UpdateCompartment)


In the above operations, use the tenancy OCID for the `compartmentID` parameter. 
Was this article helpful?
YesNo

