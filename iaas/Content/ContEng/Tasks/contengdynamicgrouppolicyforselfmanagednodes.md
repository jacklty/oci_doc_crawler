Updated 2025-01-15
# Creating a Dynamic Group and a Policy for Self-Managed Nodes
_Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine._
Before you can create self-managed nodes, you have to:
  * create a new dynamic group to contain the compute instance that you want to add to the cluster as a self-managed node
  * create a policy for the dynamic group, with a policy statement to allow compute instances in the dynamic group to join an existing Kubernetes cluster


To create a new dynamic group and a suitable policy using the Console:
  1. Create a new dynamic group to contain the compute instance that you want to add to the cluster as a self-managed node:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. 
    2. Follow the instructions in [To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), and give the dynamic group a name (for example, `acme-oke-self-managed-node-dyn-grp`).
    3. Enter a rule that includes the compute instances in the compartment, in the format:
Copy
```
ALL {instance.compartment.id = '<compartment-ocid>'}
```

where `<compartment-ocid>` is the OCID of the compartment to which the cluster belongs.
For example:
Copy
```
ALL {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaa23______smwa'}
```

    4. Click **Create Dynamic Group**.
  2. Create a policy for the dynamic group, with a policy statement to allow compute instances in the dynamic group to join an existing Kubernetes cluster:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-self-managed-node-policy`).
    3. Enter a policy statement to allow compute instances in the dynamic group to join the cluster, in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to {CLUSTER_JOIN} in compartment <compartment-name>

```

where:
       * `<dynamic-group-name>` is the name of the dynamic group you created earlier. For example, `acme-oke-self-managed-node-dyn-grp`. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format `dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format `dynamic-group id <dynamic-group-ocid>`.
       * `<compartment-name>` is the name of the compartment to which the cluster belongs. For example, `acme-oke-cluster-compartment`
For example:
Copy
```
Allow dynamic-group acme-oke-self-managed-node-dyn-grp to {CLUSTER_JOIN} in compartment acme-oke-cluster-compartment
```

If you consider this policy statement to be too permissive, you can restrict the permissions to explicitly specify the cluster to which you want to add the managed node, by entering a policy statement in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to {CLUSTER_JOIN} in compartment <compartment-name>
where { target.cluster.id = "<cluster-ocid>" }
```

    4. Click **Create** to create the new policy.


Was this article helpful?
YesNo

