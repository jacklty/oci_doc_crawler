Updated 2024-09-26
# Policy Syntax
The overall syntax of a policy statement is as follows:
```
Allow <subject> to <verb> <resource-type> in <location> where <conditions>

```

Spare spaces or line breaks in the statement have no effect. 
For limits on the number of policies and statements, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
## Subject 🔗 
Specify one or more comma-separated groups by name or OCID. Or specify `any-group` to cover all users, instance principals and resource principals in the tenancy.
**Syntax:**{{ `group <group_name> | group id <group_ocid> | dynamic-group <dynamic-group_name> | dynamic-group id <dynamic-group_ocid>| any-group` | any-user}}
**Note** Any-user will grant access to all users, resource principals, and instance principals in your tenancy and service principal. We recommend against using `any-user` and instead using `any-group`. Alternately you can specify the resource type to prevent unnecessary princpals from having access. For example `{request.principal.type='disworkspace'}`.
**Examples:**
  * To specify a single group by name: ```
Allow 
group A-Admins
 to manage all-resources in compartment Project-A
```

  * To specify multiple groups by name (a space after the comma is optional): ```
Allow 
group A-Admins, B-Admins
 to manage all-resources in compartment Projects-A-and-B
```

  * To specify a single group by OCID (the OCID is shortened for brevity): ```
Allow group 
 id ocid1.group.oc1..aaaaaaaaqjihfhvxmum...awuc7i5xwe6s7qmnsbc6a 
to manage all-resources in compartment Project-A
```

  * To specify multiple groups by OCID (the OCIDs are shortened for brevity): ```
Allow group 
 id ocid1.group.oc1..aaaaaaaaqjihfhvxmumrl...wuc7i5xwe6s7qmnsbc6a,
 id ocid1.group.oc1..aaaaaaaavhea5mellwzb...66yfxvl462tdgx2oecyq 
to manage all-resources in compartment Projects-A-and-B
```

  * To specify any group or instance principal in the tenancy, or specify any-group to inspect users in a tenancy: ```
Allow any-group to inspect users in tenancy
```



## Verb 🔗 
Specify a single verb. For a list of verbs, see [Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#Verbs). Example:
```
Allow group A-Admins to manage all-resources in compartment Project-A
```

## Resource-Type 🔗 
Specify a single resource-type, which can be one of the following:
  * An individual resource-type (e.g., `vcns`, `subnets`, `instances`, `volumes`, etc.)
  * A family resource-type (e.g., `virtual-network-family`, `instance-family`, `volume-family`, etc.)
  * `all-resources`: Covers all resources in the compartment (or tenancy). 


A family resource-type covers a variety of components that are typically used together. This makes it easier to write a policy that gives someone access to work with various aspects of your cloud network. 
For a list of the available resource-types, see [Resource-Types](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#Resource).
**Syntax:**` <resource_type> | all-resources`
**Examples:**
  * To specify a single resource-type: ```
Allow group HelpDesk to manage users in tenancy
```

  * To specify multiple resource-types, use separate statements: ```
Allow group A-Users to manage instance-family in compartment Project-A
Allow group A-Users to manage volume-family in compartment Project-A

```

  * To specify all resources in the compartment (or tenancy): ```
Allow group A-Admins to manage all-resources in compartment Project-A
```



## Location 🔗 
Specify a single compartment or compartment path by name or OCID. Or simply specify `tenancy` to cover the entire tenancy. Remember that users, groups, and compartments reside in the tenancy. Policies can reside in (i.e., be attached to) either the tenancy or a child compartment. 
**Note**
Granting Access to Specific Regions or availability domains
To create a policy that gives access to a specific region or availability domain, use the `request.region` or `request.ad` variable with a condition. See [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm#five).
The location is required in the statement. If you want to attach a policy to a compartment, you must be in that compartment when you create the policy. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).
To specify a compartment that is not a direct child of the compartment you are attaching the policy to, specify the path to the compartment, using the colon (:) as a separator. For more information, see [Policies and Compartment Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#hierarchy).
**Syntax:** ``[ tenancy | compartment <compartment_name> | compartment id <compartment_ocid>` ] `
**Examples:**
  * To specify a compartment by name: ```
Allow group A-Admins to manage all-resources in compartment Project-A
```

  * To specify a compartment by OCID: ```
Allow group
 id ocid1.group.oc1..aaaaaaaaexampleocid to manage all-resources in compartment id ocid1.compartment.oc1..aaaaaaaaexampleocid
```

  * To specify multiple compartments, use separate statements: ```
Allow group InstanceAdmins to manage instance-family in compartment Project-A
Allow group InstanceAdmins to manage instance-family in compartment Project-B

```

  * To specify multiple compartments by OCID, use separate statements: ```
Allow group id ocd1.group.oc1..aaaaaaaavheexampleocid to manage all-resources in compartment id ocid1.compartment.oc1..aaaaaaaayzexampleocid
Allow group id ocd1.group.oc1..aaaaaaaaexampleocid to manage all-resources in compartment id ocid1.compartment.oc1..aaaaaexampledocid
```

  * To specify a compartment that is not a direct child of the compartment where you are attaching the policy, specify the path:
```
Allow group InstanceAdmins to manage instance-family in compartment Project-A:Project-A2
```



## Conditions 🔗 
Specify one or more conditions. Use `any` or `all` with multiple conditions for a logical OR or AND, respectively. 
**Syntax for a single condition:**` variable =|!= value`
**Syntax for multiple conditions:**` any|all {<condition>,<condition>,...}`
Additional operators can be used with time-based variables, see [Restricting Access to Resources Based on Time Frame](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Scoping_Policy_by_Time).
**Important** Condition matching is case insensitive. This is important to remember when writing conditions for resource types that allow case-sensitive naming. For example, the Object Storage service allows you to create both a bucket named "BucketA" and a bucket named "bucketA" in the same compartment. If you write a condition that specifies "BucketA", it will apply also to "bucketA", because the condition matching is case insensitive.
For a list of variables supported by all the services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General). Also see the details for each service in the [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies."). Here are the types of values you can use in conditions:
Type | Examples  
---|---  
String |  `'johnsmith@example.com'` `'ocid1.compartment.oc1..aaaaaaaaph...ctehnqg756a'` (single quotation marks are required around the value)   
Pattern |  `/HR*/` (matches strings that start with "HR") `/*HR/` (matches strings that end with "HR") `/*HR*/` (matches strings that contain "HR")   
Examples:
**Note** In the following examples, the statements that specify the condition do not let GroupAdmins actually list all the users and groups, therefore statements including the `inspect` verb are added for completeness. To understand why this is required, see [Variables that Aren't Applicable to a Request Result in a Declined Request](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Variable). 
  * A single condition. 
The following policy enables the GroupAdmins group to create, update, or delete any groups with names that start with "A-Users-":
Copy
```
Allow group GroupAdmins to manage groups in tenancy where target.group.name = /A-Users-*/
Allow group GroupAdmins to inspect groups in tenancy
```

The following policy enables the NetworkAdmins group to manage cloud networks in any compartment except the one specified: ```
Allow group NetworkAdmins to manage virtual-network-family in tenancy where target.compartment.id != 'ocid1.compartment.oc1..aaaaaaaaexampleocid'
```

  * Multiple conditions. 
The following policy lets GroupAdmins create, update, or delete any groups whose names start with "A-", except for the A-Admins group itself:
Copy
```
Allow group GroupAdmins to manage groups in tenancy where all {target.group.name=/A-*/,target.group.name!='A-Admins'}
 
Allow group GroupAdmins to inspect groups in tenancy
```



Was this article helpful?
YesNo

