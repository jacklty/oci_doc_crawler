Updated 2024-12-18
# Required IAM Policies for Using Virtual Nodes
_Find out about the IAM policies to create to use virtual nodes with Kubernetes Engine (OKE)._
Administrator users do not require additional permissions to create and use clusters with virtual nodes and virtual node pools.
To enable non-administrator users to create and use clusters with virtual nodes and virtual node pools, you must give such users the required permissions. To grant these permissions, create an IAM policy with the following policy statements:
Copy
```
allow group <group-name> to manage cluster-virtualnode-pools in compartment <compartment-name>
```

Copy
```
allow group <group-name> to read virtual-network-family in compartment <compartment-name>
```

Copy
```
allow group <group-name> to manage vnics in compartment <compartment-name>
```

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.
Was this article helpful?
YesNo

