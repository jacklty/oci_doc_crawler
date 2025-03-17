Updated 2024-11-08
# General Variables for All Requests
Use the following general variables for all requests
You use variables when adding conditions to a policy. For more information, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM."). Here are the general variables applicable to all requests.
Name | Type | Description  
---|---|---  
`request.user.id` | Entity (OCID) | The OCID of the requesting user.  
`request.user.name` | String | Name of the requesting user.  
`request.user.mfaTotpVerified` | Boolean |  Whether the user has been verified by multifactor authentication (MFA). To restrict access to only MFA-verified users, add the condition ``where request.user.mfaTotpVerified`='true'` See [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication "Multifactor Authentication \(MFA\) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.") for information on setting up MFA. This attribute is deprecated for IAM with identity domains, it works only with IAM without identity domains.  
`request.groups.id` | List of entities (OCIDs) | The OCIDs of the groups the requesting user is in.  
`request.permission` | String | The underlying permission being requested.  
`request.operation` | String | The API operation name being requested (for example, [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers)).  
`request.networkSource.name` | String | The name of the network source group that specifies allowed IP addresses the request may come from. See [Overview of Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/networksources/managingnetworksources.htm#Managing_Network_Sources) for information.  
`request.utc-timestamp` | String | The UTC time that the request is submitted, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm#scoping_policy_by_time "You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames.") for more information.  
`request.utc-timestamp.month-of-year` | String | The month that the request is submitted in, specified in numeric [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (for example, '1', '2', '3', ... '12'). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm#scoping_policy_by_time "You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames.") for more information.  
`request.utc-timestamp.day-of-month` | String | The day of the month that the request is submitted in, specified in numeric format '1' - '31'. See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm#scoping_policy_by_time "You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames.") for more information.  
`request.utc-timestamp.day-of-week` | String | The day of the week that the request is submitted in, specified in English (for example, 'Monday', 'Tuesday', 'Wednesday', etc.). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm#scoping_policy_by_time "You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames.") for more information.  
`request.utc-timestamp.time-of-day` | String | The UTC time interval that request is submitted during, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (for example, '01:00:00Z' AND '02:01:00Z'). See [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm#scoping_policy_by_time "You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames.") for more information.  
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
`request.principal.type` | String | The name of the resource type specified in `request.principal.type`. For example, user or cluster.  
`target.compartment.name` | String | The name of the compartment specified in `target.compartment.id.`  
`target.compartment.id` | Entity (OCID) |  The OCID of the compartment containing the primary resource. **Note:**`target.compartment.id` and `target.compartment.name` cannot be used with a "List" API operation to filter the list based on the requesting user's access to the compartment.   
`target.resource.compartment.tag` | String  | The tag applied to the target compartment of the request is evaluated. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
`target.resource.tag` | String  | The tag applied to the target resource of the request is evaluated. For usage instructions, see [Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).  
`target.workrequest.type` | String | The work request type, for example:
  * CREATE_ENVIRONMENT
  * UPDATE_ENVIRONMENT
  * DELETE_ENVIRONMENT
  * MOVE_ENVIRONMENT
  * CREATE_OCB_AGENT
  * UPDATE_OCB_AGENT
  * DELETE_OCB_AGENT
  * MOVE_OCB_AGENT
  * CREATE_AGENT_DEPENDENCY
  * UPDATE_AGENT_DEPENDENCY
  * DELETE_AGENT_DEPENDENCY
  * MOVE_AGENT_DEPENDENCY
  * CREATE_INVENTORY 
  * DELETE_INVENTORY
  * IMPORT_INVENTORY
  * DELETE_ASSET_SOURCE
  * REFRESH_ASSET_SOURCE
  * CREATE_ASSET_SOURCE
  * UPDATE_ASSET_SOURCE

  
Was this article helpful?
YesNo

