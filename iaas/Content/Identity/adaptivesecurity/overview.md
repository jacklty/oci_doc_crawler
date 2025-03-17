Updated 2024-09-26
# Managing Adaptive Security and Risk Providers
Learn about adaptive security and risk providers, how to activate adaptive security, how to configure the Default risk provider, and how to create a third-party risk provider for an identity domain in IAM. 
This section contains the following topics:
  * [Understanding Adaptive Security](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/understand-adaptive-security.htm#understand-adaptive-security "Adaptive Security provides strong authentication capabilities for users based on their historical behavior in an identity domain in IAM.")
  * [Understanding Risk Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/understand-risk-providers.htm#understand-risk-providers "Identity domain administrators and security administrators use identity domain risk providers to configure various contextual and threat events to be analyzed within an identity domain in IAM. An identity domain can also consume user risk scores from third-party risk providers.")
  * [Activating Adaptive Security](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-adaptive-security.htm#activate-adaptive-security "Activate adaptive security for an identity domain in IAM to evaluate contextual and threat event analysis, and obtain user risk scores from the configured third-party risk providers.")
  * [Deactivating Adaptive Security](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/deactivate-adaptive-security.htm#deactivate-adaptive-security "Deactivate adaptive security for an identity domain in IAM to stop performing contextual and threat event analysis, and stop obtaining user risk scores from third-party risk providers.")
  * [Updating the Default Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/configure-default-risk-provider.htm#configure-default-risk-provider "Update the default risk provider for an identity domain in IAM.")
  * [Creating a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/add-third-party-risk-provider.htm#add-third-party-risk-provider "Create a risk provider for an identity domain in IAM that you can use to obtain a user's risk score from the Symantec third-party risk engine.")
  * [Activating a Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-risk-provider.htm#activate-risk-provider "Activate a risk provider for an identity domain in IAM to collect user risk scores.")
  * [Deactivating a Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/deactivate-risk-provider.htm#deactivate-risk-provider "Deactivate a risk provider for an identity domain in IAM to stop collecting user risk scores.")
  * [Viewing a Risk Provider's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/view-details-risk-provider.htm#view-details-risk-provider "View details, such as the name, company, and activation status, of each risk provider in an identity domain in IAM. You can also see other information, such as the risk levels and authentication information associated with the risk provider.")
  * [Updating a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/modify-third-party-risk-provider.htm#modify-third-party-risk-provider "Update the values for a third-party risk provider in an identity domain in IAM.")
  * [Deleting a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/remove-third-party-risk-provider.htm#remove-third-party-risk-provider "Delete a third-party risk provider that's no longer needed to provide user risk scores in an identity domain in IAM.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

