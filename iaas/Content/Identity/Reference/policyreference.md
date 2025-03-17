Updated 2025-02-21
# Policy Reference
Get an overview of IAM policy reference topics, including verbs, resources types, and general variables.
This reference includes:
  * Fleet Application Management: See [Fleet Application Management Policies and Permissions](https://docs.oracle.com/iaas/Content/fleet-management/policies-permissions.htm)
  * [Details for Functions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/functionspolicyreference.htm#Details_for_Functions)
  * Full Stack Disaster Recovery: See [Full Stack Disaster Recovery Policies](https://docs.oracle.com/iaas/disaster-recovery/doc/disaster-recovery-policies.html)
  * Globally Distributed Autonomous Database: See [Globally Distributed Autonomous Database Policies](https://docs.oracle.com/en/cloud/paas/globally-distributed-autonomous-database/user/policies.html#GUID-2AA048F1-23C9-4031-90CC-7C72F680A0E3)
  * GoldenGate: See [Oracle Cloud Infrastructure GoldenGate Policies](https://docs.oracle.com/iaas/goldengate/doc/policies.html)
  * [Details for Health Checks](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/healthcheckpolicyreference.htm#top "Review advanced details for writing policies to control access to the Health Checks service.")
  * [Details for IAM with Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.")
  * [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top)
  * For Integration Generation 2 and Integration 3, see [Details for Oracle Integration](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicydetails_integration.htm#iampolicydetails_integration). 
  * [Details for the Java Management Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/javamanagementreference.htm#autonomousjavareference)
  * [Details for Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/contengpolicyreference.htm#Details_for_Container_Engine_for_Kubernetes)


For instructions on how to create and manage policies using the Console or API, see [Overview of Working with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies.htm#overview_policies).
## Verbs 🔗 
The verbs are listed in order of least amount of ability to most. The exact meaning of a each verb depends on which resource-type it's paired with. The tables later in this section show the API operations covered by each combination of verb and resource-type.
Verb | Target User | Types of Access Covered  
---|---|---  
`inspect` | Third-party auditors | Ability to list resources, without access to any confidential information or user-specified metadata that might be part of that resource. **Important:** The operation to list policies includes the contents of the policies themselves. The list operations for the Networking resource-types return all the information (for example, the contents of security lists and route tables).   
`read` | Internal auditors | Includes `inspect` plus the ability to get user-specified metadata and the actual resource itself.   
`use` | Day-to-day end users of resources | Includes `read` plus the ability to work with existing resources (the actions vary by resource type). Includes the ability to update the resource, except for resource-types where the "update" operation has the same effective impact as the "create" operation (for example, `UpdatePolicy`, `UpdateSecurityList`, and more), in which case the "update" ability is available only with the `manage` verb. In general, this verb doesn't include the ability to create or delete that type of resource.  
`manage` | Administrators | Includes all permissions for the resource.  
## Resource-Types 🔗 
A few common family resource-types are listed below. For the individual resource-types that make up each family, follow the links.
  * `all-resources`: All Oracle Cloud Infrastructure resource-types
  * `cluster-family`: See [Details for Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/contengpolicyreference.htm#Details_for_Container_Engine_for_Kubernetes)
  * `compute-management-family`: See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)
  * `data-catalog-family`: See [Data Catalog Policies](https://docs.oracle.com/iaas/data-catalog/using/policies.htm)
  * `data-science-family`: See [Data Science Policies](https://docs.oracle.com/iaas/data-science/using/policies.htm)
  * `database-family`: See [Details for the Database Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/databasepolicyreference.htm#Details_for_the_Database_Service)
  * `datasafe-family-resources`: See [OCI Resources for Oracle Data Safe](https://docs.oracle.com/en/cloud/paas/data-safe/admds/oci-resources-oracle-data-safe.html)
  * `dns`: See [Details for the DNS Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/dnspolicyreference.htm#Details_for_the_DNS_Service)
  * `email-family`: See [Details for the Email Delivery Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#Details_for_the_Email_Service)
  * `file-family`: See [Details for the File Storage Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/filestoragepolicyreference.htm#Details_for_the_File_Storage_Service)
  * `instance-agent-command-family` : See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)
  * `instance-agent-family`: See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)
  * `instance-family`: See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)
  * `object-family`: See [Details for Object Storage and Archive Storage](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#Details_for_Object_Storage_Archive_Storage_and_Data_Transfer)
  * `optimizer-api-family`: See [Creating Cloud Advisor Policies](https://docs.oracle.com/iaas/Content/CloudAdvisor/Reference/cloudadvisorpolicyreference.htm)
  * `appmgmt-family`: See [Details for Stack Monitoring](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#stackmonitoringpolicyreference "This topic covers details for writing policies to control access to the Stack Monitoring service.")
  * `stack-monitoring-family`: See [Details for Stack Monitoring](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#stackmonitoringpolicyreference "This topic covers details for writing policies to control access to the Stack Monitoring service.")
  * `virtual-network-family`: See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)
  * `volume-family`: See [Details for the Core Services](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services)


IAM has no family resource-type, only individual ones. See [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.") or [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top), depending on whether your tenancy has identity domains or not.
## General Variables for All Requests 🔗 
You use variables when adding conditions to a policy. For more information, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#one). Here are the general variables applicable to all requests.
Name | Type | Description  
---|---|---  
`request.user.id` | Entity (OCID) | The OCID of the requesting user.  
`request.user.name` | String | Name of the requesting user.  
`request.user.mfaTotpVerified` | Boolean |  Whether the user has been verified by multifactor authentication (MFA). To restrict access to only MFA-verified users, add the condition ``where request.user.mfaTotpVerified`='true'` See [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingmfa.htm#Managing_MultiFactor_Authentication) for information on setting up MFA.  
`request.groups.id` | List of entities (OCIDs) | The OCIDs of the groups the requesting user is in.  
`request.permission` | String | The underlying permission being requested (see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi)).  
`request.operation` | String | The API operation name being requested (for example, [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers)).  
`request.networkSource.name` | String | The name of the network source group that specifies allowed IP addresses the request may come from. See [Managing Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm#Managing_Network_Sources) for information.  
`request.utc-timestamp` | String | The UTC time that the request is submitted, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time) for more information.  
`request.utc-timestamp.month-of-year` | String | The month that the request is submitted in, specified in numeric [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (for example, '1', '2', '3', ... '12'). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time) for more information.  
`request.utc-timestamp.day-of-month` | String | The day of the month that the request is submitted in, specified in numeric format '1' - '31'. See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time) for more information.  
`request.utc-timestamp.day-of-week` | String | The day of the week that the request is submitted in, specified in English (for example, 'Monday', 'Tuesday', 'Wednesday', etc.). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time) for more information.  
`request.utc-timestamp.time-of-day` | String | The UTC time interval that request is submitted during, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (for example, '01:00:00Z' AND '02:01:00Z'). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time) for more information.  
`request.region` | String |  The 3-letter key for the region the request is made in. Allowed values are: **Note:** For [quota policies](https://docs.oracle.com/iaas/Content/Quotas/Concepts/managing_quota_policies.htm), the region name must be specified instead of the following 3-letter key values. Also see [Sample Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/sample_quotas.htm) for more information.
  * AMS - use for Netherlands Northwest (Amsterdam)
  * ARN - use for Sweden Central (Stockholm)
  * AUH - use for UAE Central (Abu Dhabi)
  * BEG - use for Serbia Central (Jovanovac)
  * BOG - use for Colombia Central (Bogota)
  * BOM - use for India West (Mumbai)
  * CDG - use for France Central (Paris)
  * CWL - use for UK West (Newport)
  * DXB - use for UAE East (Dubai)
  * FRA - use for Germany Central (Frankfurt)
  * GRU - use for Brazil East (Sao Paulo)
  * HYD - use for India South (Hyderabad)
  * IAD - use for US East (Ashburn)
  * ICN - use for South Korea Central (Seoul)
  * JED - use for Saudi Arabia West (Jeddah)
  * JNB - use for South Africa Central (Johannesburg)
  * KIX - use for Japan Central (Osaka) 
  * LHR - use for UK South (London) 
  * LIN - use for Italy Northwest (Milan)
  * MAD - use for Spain Central (Madrid)
  * MEL - use for Australia Southeast (Melbourne)
  * MRS - use for France South (Marseille)
  * MTY - use for Mexico Northeast (Monterrey)
  * MTZ - use for Israel Central (Jerusalem)
  * NRT - use for Japan East (Tokyo)
  * ORD - use for US Midwest (Chicago)
  * PHX - use for US West (Phoenix)
  * QRO - use for Mexico Central (Queretaro)
  * RUH - use for Saudi Arabia Central (Riyadh)
  * SCL - use for Chile Central (Santiago)
  * SIN - use for Singapore (Singapore)
  * SJC - use for US West (San Jose)
  * SYD - use for Australia East (Sydney)
  * VAP - use for Chile West (Valparaiso)
  * VCP - use for Brazil Southeast (Vinhedo)
  * XSP - use for Singapore West (Singapore)
  * YNY - use for South Korea North (Chuncheon)
  * YUL - use for Canada Southeast (Montreal)
  * YYZ - use for Canada Southeast (Toronto)
  * ZRH - use for Switzerland North (Zurich)

  
`request.ad` | String | The name of the availability domain the request is made in. To get a list of availability domain names, use the [ListAvailabilityDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/AvailabilityDomain/ListAvailabilityDomains) operation.  
`request.principal.compartment.tag` | String | The tags applied to the compartment that the requesting resource belongs to are evaluated for a match. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
`request.principal.group.tag` | String | The tags applied to the groups that the user belongs to are evaluated for a match. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
`target.compartment.name` | String | The name of the compartment specified in `target.compartment.id`.  
`target.compartment.id` | Entity (OCID) |  The OCID of the compartment containing the primary resource. **Note:**`target.compartment.id` and `target.compartment.name` cannot be used with a "List" API operation to filter the list based on the requesting user's access to the compartment.   
`target.resource.compartment.tag` | String  | The tag applied to the target compartment of the request is evaluated. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
`target.resource.tag` | String  | The tag applied to the target resource of the request is evaluated. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
Was this article helpful?
YesNo

