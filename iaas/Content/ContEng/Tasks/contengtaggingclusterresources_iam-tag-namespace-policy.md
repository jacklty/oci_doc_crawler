Updated 2024-08-14
# Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments
_Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine (OKE)._
To apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, you must include a policy statement similar to the following in an IAM policy: 
Copy
```
Allow any-user to use tag-namespace in tenancy where all {request.principal.type = 'cluster'}
```

If you consider this policy statement to be too permissive, you can restrict the permissions to explicitly specify the compartment to which the tag namespace belongs, and/or to explicitly specify the cluster that belongs to a different compartment. For example:
Copy
```
Allow any-user to use tag-namespace in compartment <compartment-ocid> where all { request.principal.id = '<cluster-ocid>' }
```

Was this article helpful?
YesNo

