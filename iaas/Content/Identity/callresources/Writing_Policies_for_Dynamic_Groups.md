Updated 2024-10-08
# Writing Policies for Dynamic Groups
After you create a dynamic group, you need to create policies to permit the dynamic groups to access Oracle Cloud Infrastructure services.
Policy for dynamic groups follows the syntax described in [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies."). Review that topic to understand basic policy features.
To create policies, see [Creating a Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm#To_create_a_policy "Create IAM policies to manage access to OCI resources.").
The syntax to permit a dynamic group access to resources in a compartment is:
```
Allow dynamic-group <dynamic_group_name> to <verb> <resource-type> in compartment <compartment_name>
```

The syntax to permit a dynamic group access to a tenancy is:
```
Allow dynamic-group <dynamic_group_name> to <verb> <resource-type> in tenancy
```

Here are a few example policies:
To allow a dynamic group (FrontEnd) to use a load balancer in a specific compartment (ProjectA):
```
Allow dynamic-group FrontEnd to use load-balancers in compartment ProjectA
```

To allow a dynamic group to launch instances in a specific compartment:
```
Allow dynamic-group FrontEnd to manage instance-family in compartment ProjectA
Allow dynamic-group FrontEnd to use volume-family in compartment ProjectA
Allow dynamic-group FrontEnd to use virtual-network-family in compartment ProjectA
```

Was this article helpful?
YesNo

