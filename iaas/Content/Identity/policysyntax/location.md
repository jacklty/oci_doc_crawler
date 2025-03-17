Updated 2024-09-26
# Locations
Compartments are created by tenancy administrators in IAM. You can specify compartments by name or OCID.
The policy statement's compartment element specifies the scope of access to a compartment or tenancy. For example, use `tenancy` as a location to grant access to the specified resources across an entire tenancy.
**Note**
To create a policy that gives access to a specific region or availability domain, use the `request.region` or `request.ad` attribute with a condition. For more information, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM.").
The location is required in policy statements.
**Syntax:** ``[ tenancy | compartment <compartment_name> | compartment id <compartment_ocid>` ] `
**Note**
By default, the policy statement's compartment is assumed to be a direct child of the compartment where you create the policy. To specify a different parent compartment, use the compartment path, with a colon between the two compartments.
**Example**
Copy
```
Allow group InstanceAdmins to manage instance-family in compartment Project-A:Project-A2

```

**Examples** :
  * Single compartment by name
```
Allow group A-Admins to manage all-resources in compartment Project-A
```

  * Single compartment by OCID
Copy
```
Allow group id ocid1.group.oc1..exampleuniqueID to manage all-resources in compartment id ocid1.group.oc1..exampleuniqueID
```

  * Many compartments by name
Copy
```
Allow group InstanceAdmins to manage instance-family in compartment Project-A  
Allow group InstanceAdmins to manage instance-family in compartment Project-B

```

  * Many compartments by OCID
Copy
```
Allow group id ocid1.group.oc1..exampleuniqueID to manage all-resources in compartment id ocid1.compartment.oc1..exampleuniqueID
Allow group id ocid1.compartment.oc1..exampleuniqueID to manage all-resources in compartment id ocid1.compartment.oc1..exampleuniqueID
```



Was this article helpful?
YesNo

