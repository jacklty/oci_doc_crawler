Updated 2024-09-26
# Subjects
The subject of an IAM policy specifies the groups or principals that the policy grants permission to.
**Syntax:**```
group '<identity_domain_name>'/'<group_name>' | group id <group_ocid> | dynamic-group '<identity_domain_name>'/'<dynamic-group_name>' | dynamic-group id <dynamic-group_ocid> | any-group service '<service_name>'
```

**Note** The subject <any-group> includes all groups and all dynamic groups.
The subject of an IAM policy to specify the principals that the policy grants permission to.
**Syntax:**```
group <identity_domain_name>/<group_name> | group id <group_ocid> | dynamic-group <identity_domain_name>/<dynamic-group_name> | dynamic-group id <dynamic-group_ocid> | any-userservice <service_name>
```

A policy statement can include only one type of principal, but you can include many instances of that principal.
**Note**
If the policy is for the default identity domain, you can omit <identity_domain_name>. The policy processes and interprets the policy statement as though it was written as `Default/<group_name>`.
**Examples:**
  * Single group by name in the default identity domain: ```
Allow group A-Admins to manage all-resources in compartment Project-A
```

  * Several groups by name in the default identity domain (a space after the comma is optional): ```
Allow group A-Admins, B-Admins to manage all-resources in compartment Projects-A-and-B
```

  * Single group by OCID in the default identity domain: ```
Allow group id ocid1.group.oc1..exampleuniqueID to manage all-resources in compartment Project-A
```

  * Several groups by OCID in the default identity domain: ```
Allow group id ocid1.group.oc1.exampleuniqueID, id ocid1.group.oc1.exampleuniqueID to manage all-resources in compartment Projects-A-and-B
```

  * Any user in the default identity domain tenancy: ```
Allow any-group to inspect users in tenancy
```

  * Service in the in the default identity domain tenancy:```
Allow service FaaS to use virtual-network-family in compartment <compartment-name>
```

  * Single group in a secondary identity domain by name:```
Allow group Domain-B/Domain-B-Admins to manage all-resources in compartment Project-B
```



Was this article helpful?
YesNo

