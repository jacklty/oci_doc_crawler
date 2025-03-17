Updated 2024-10-30
# Troubleshooting Organization Management
Use troubleshooting information to identify and address common issues that can occur while working with Organization Management.
  * [Governance Rules that Need Attention](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-troubleshooting.htm#govrules_need_attention "Sometimes governance rules require attention while attaching to one or many tenancies in the organization.")


## Governance Rules that Need Attention 🔗 
Sometimes governance rules require attention while attaching to one or many tenancies in the organization.
The [work request](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-management.htm#workrequest_management "Learn about work request, work request error, and work request log management.") for a specific tenancy gives detailed [logs](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-logs.htm#workrequest_list_logs "List all work request logs.") and [error messages](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-errors.htm#workrequest_list_errors "List all work request errors.") about the issue. Some typical scenarios include:
  * Creating a **Tags** governance rule and applying it to a tenancy, but the tenancy already has a tag namespace with the same name. For example, if you apply this kind of a rule to the parent tenancy, the template tag namespace prevents creation of another tag namespace with a matching name.
  * Syntax errors or mistakes in the quota policy statement still allow **Quota policy** governance rule creation, but such rules fail to attach to any of the tenancies.


Was this article helpful?
YesNo

