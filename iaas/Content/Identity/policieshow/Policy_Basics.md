Updated 2024-10-11
# IAM Policies Overview
IAM policies govern control of resources in Oracle Cloud Infrastructure (OCI) tenancies.
A policy contains one or more policy statements. Each statement uses basic or conditional syntax.
Basic syntax:
```
Allow <subject> to <verb> <resource> in <location>
```

Conditional syntax:
```
Allow <subject> to <verb> <resource> in <location> where <conditions>
```

The following table briefly explains the elements in the syntax and provides links to detailed information about each element.
Element | Description  
---|---  
Allow | Required start word. A policy statement always begins with the word `Allow`. Policies only _allow_ access; they can't deny it.  
[<subject>](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/subject.htm#subject "The subject of an IAM policy specifies the groups or principals that the policy grants permission to.") |  A user, group, or other principal to be granted access. The subject includes the principal type and identifier (name or OCID), and is prefixed by the name of the identity domain unless the default identity domain is used. An administrator in your organization defines the groups and compartments in your tenancy.  ```
Allow group <identity_domain_name>/<group_name> to <verb> <resource-type> in tenancy
```
  
[<verb>](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Verbs.htm#top "The verb element of a policy statement specifies the type of access. For example, use inspect to let third-party auditors list the specified resources.") | The level of access. Oracle defines the possible verbs and resource-types you can use in policies, see [Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Verbs.htm#top "The verb element of a policy statement specifies the type of access. For example, use inspect to let third-party auditors list the specified resources.").  
[<resource>](https://docs.oracle.com/en-us/iaas/Content/Identity/policiesgs/policies_topic-ResourceTypes.htm#top "Resource types are defined by Oracle. The resource type specifies the type or resource to which the policy applies.") |  Resources to which the policy grants access. Oracle defines the possible resource-types you can use in policies, see [Resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policiesgs/policies_topic-ResourceTypes.htm#top "Resource types are defined by Oracle. The resource type specifies the type or resource to which the policy applies."). Some API operations require access to several resource-types. For example, `LaunchInstance` requires the ability to create instances and work with a cloud network. The `CreateVolumeBackup` operation requires access to both the volume and the volume backup. That requires separate policy statements to give access to each resource type. These individual statements don't have to be in the same policy. A user can gain the required access from being in different groups.   
[<location>](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/location.htm#location "Compartments are created by tenancy administrators in IAM. You can specify compartments by name or OCID.") |  (Optional) A compartment or tenancy to which the policy applies. For a compartment, the value includes an identifier (name or OCID). Sometimes the policy needs to apply to the entire tenancy, and not a compartment inside the tenancy. The following is an example of a compartment-specific policy statement, in which the <location> is a specific compartment: ```
Allow group <identifier> to <verb> <resource> in compartment <identifier>
```
Following is an example of a tenancy-wide policy statement, in which the <location> is tenancy: ```
Allow group <identifier> to <verb> <resource> in tenancy 
```
  
[<condition>](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM.") | (Optional) Limits access to a resource.  
[![Railroad diagram of IAM policy structure](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/IAM-with-id-Policies.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/IAM-with-id-Policies.png)
OCI also lets you create cross-tenancy policies. For more information, see [Cross-Tenancy Access Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/iam-cross-domain.htm#top "Use cross-tenancy policy statements to create IAM policies that work across tenancies."). 
## Cross-tenancy Policies
Cross-tenancy policy statements give subjects permission to use resources in other tenancies. See [Cross-Tenancy Access Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/iam-cross-domain.htm#top "Use cross-tenancy policy statements to create IAM policies that work across tenancies.").
Was this article helpful?
YesNo

