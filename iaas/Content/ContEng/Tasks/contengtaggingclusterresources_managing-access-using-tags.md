Updated 2025-01-15
# Managing Access By Applying Tags to Cluster-Related Resources
_Find out how to use tags and IAM policies to manage access to resources related to the clusters you create using Kubernetes Engine (OKE)._
Having applied tags to cluster-related resources, you can control access to other resources by including the tags in IAM policies. 
Including tags in IAM policies is particularly useful when authorizing worker nodes to access other resources. If you specify node tags when initially defining a node pool and the node pool is subsequently scaled out, the node tags are automatically applied to any new worker nodes that are created. Provided you have included the node tags in an IAM policy that grants access to other resources, the new worker nodes are automatically authorized to access the same resources as existing worker nodes in the node pool.
Note that you cannot use free-form tags in IAM policies to control access to resources.
## Example: Authorizing a managed node pool to read object storage objects 
To authorize only worker nodes in a particular managed node pool to read object storage objects in a certain compartment:
  1. Define a new managed node pool and specify:
     * A name for the node pool that is unique in the compartment. For example, `acme-pool-one`
     * A node tag set to the name of the node pool. For example, a defined tag named `acme-nodepool-name` in a tag namespace named `acme-project`, set to the value `acme-pool-one`.
When you create the node pool, the node tag `acme-project.acme-nodepool-name='acme-pool-one'` is applied to all the compute instances hosting worker nodes in the node pool.
  2. Define a dynamic group to represent the node pool:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. 
    2. Follow the instructions in [To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), and give the dynamic group a name (for example, `acme-oke-pool-one-dyn-grp`).
    3. Enter a rule that includes all worker nodes in the compartment to which the node tag has been applied, in the format:
Copy
```
All {instance.compartment.id = '<compartment_ocid>', tag.<tagnamespace>.<tagkey>.value = '<tagvalue>'}
```

For example:
```
All {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaa23______smwa', tag.acme-project.acme-nodepool-name.value = 'acme-pool-one'}
```

    4. Click **Create Dynamic Group**.
  3. Define an IAM policy that authorizes the dynamic group to read object storage objects in a compartment:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-read-object-dyn-grp-policy`).
    3. Enter a policy statement to allow the dynamic group to read object storage objects, in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to read objects in compartment <compartment-name>
```

where:
       * `<dynamic-group-name>` is the name of the dynamic group you created earlier. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format `dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format `dynamic-group id <dynamic-group-ocid>`.
       * `<compartment-name>` is the name of the compartment containing the object storage objects.
For example:
Copy
```
Allow dynamic-group acme-oke-pool-one-dyn-grp to read objects in compartment acme-oke-obj-storage-comp
```

    4. Click **Create** to create the new policy.
All worker nodes in the node pool can now read object storage objects in the compartment you specified.


Was this article helpful?
YesNo

