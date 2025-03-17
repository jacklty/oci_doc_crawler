Updated 2024-09-26
# Policy Inheritance
A basic policy feature is the concept of _inheritance_ in IAM.
Compartments inherit any policies from a parent compartment. An example is the Administrators group, which automatically comes with your tenancy (see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.")). 
The following is the built-in policy that lets the Administrators group (in the default identity domain) do anything in the tenancy:
```
Allow group Administrators to manage all-resources in tenancy
```

Because of policy inheritance, the Administrators group can also do anything in _any_ of the compartments in the tenancy. 
For example, consider a tenancy that has three levels of compartments: CompartmentA, CompartmentB, and ComparmentC.
[![Image shows CompartmentA. CompartmentB, CompartmentC hierarchy](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)
Policies that apply to resources in CompartmentA also apply to resources in CompartmentB and CompartmentC.
The following example allows the group NetworkAdmins (in the default identity domain) to manage VCNs in CompartmentA, which also means that it can manage VCNs in CompartmentB, and CompartmentC.
```
Allow group default/NetworkAdmins to manage virtual-network-family in compartment CompartmentA
```

Was this article helpful?
YesNo

