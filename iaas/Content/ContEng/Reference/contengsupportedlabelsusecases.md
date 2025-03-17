Updated 2024-08-14
# Supported Labels for Different Usecases
_Find out about the labels that Kubernetes Engine (OKE) uses when creating and managing clusters._
Kubernetes Engine uses a number of different labels when creating and managing clusters, including:
  * [topology.kubernetes.io/zone](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengsupportedlabelsusecases.htm#failure-domain)
  * [oci.oraclecloud.com/fault-domain](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengsupportedlabelsusecases.htm#fault-domain)
  * [node.kubernetes.io/exclude-from-external-load-balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengsupportedlabelsusecases.htm#exclude-from-external-load-balancers)


For more information about Kubernetes labels, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/).
## topology.kubernetes.io/zone 🔗 
Kubernetes Engine automatically adds the `topology.kubernetes.io/zone` label to each worker node (both managed nodes and virtual nodes) in a cluster, according to the availability domain in which it is placed. (The `topology.kubernetes.io/zone` label was formerly the `failure-domain.beta.kubernetes.io/zone` label in earlier Kubernetes releases.)
An availability domain is one or more data centers located within a region. A region is composed of one or more availability domains. Availability domains are isolated from each other, fault tolerant, and very unlikely to fail simultaneously. See [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
You can use the `topology.kubernetes.io/zone` label in different ways:
  * You can use the `topology.kubernetes.io/zone` label (in conjunction with the `oci.oraclecloud.com/fault-domain` label) to constrain the worker nodes on which to run a pod, in the case of a cluster with worker nodes in multiple availability domains. Include the `topology.kubernetes.io/zone` label in the pod specification to specify the availability domain in which worker nodes must have been placed.
  * You can use the `topology.kubernetes.io/zone` label to specify the availability domain and region to provision persistent volume claims on the Block Volume service when using the FlexVolume volume plugin. See [Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.").


When you specify a value for the `topology.kubernetes.io/zone` label, you must use the correct shortened version of the availability domain name in an Oracle Cloud Infrastructure region. 
In most cases, the shortened versions of availability domain names are in the format `<region-identifier>-1-AD-<availability-domain-number>`. For example `UK-LONDON-1-AD-1`, `UK-LONDON-1-AD-2`, `UK-LONDON-1-AD-3`, `AP-MELBOURNE-1-AD-1`, `ME-JEDDAH-1-AD-1`. To find out the region identifiers and availability domains to use, see [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengprerequisites.htm#regional-availability).
Note that the shortened versions of availability domain names in the Ashburn and Phoenix regions are exceptions, as shown below:
  * For the Phoenix region, shortened versions of availability domain names are in the format `PHX-AD-<availability-domain-number>`. For example, `PHX-AD-1`, `PHX-AD-2`, `PHX-AD-3`.
  * For the Ashburn region, shortened versions of availability domain names are in the format `US-ASHBURN-AD-<availability-domain-number>`. For example, `US-ASHBURN-AD-1`, `US-ASHBURN-AD-2`, `US-ASHBURN-AD-3`.


## oci.oraclecloud.com/fault-domain 🔗 
Kubernetes Engine automatically adds the `oci.oraclecloud.com/fault-domain` label to each worker node (both managed nodes and virtual nodes) in a cluster, according to the fault domain in which it is placed.
A fault domain is a grouping of hardware and infrastructure that is distinct from other fault domains in the same availability domain. Each availability domain has three fault domains (named FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3). Every compute instance is placed in a fault domain. See [Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault).
You can constrain the worker nodes on which to run a pod by including the `oci.oraclecloud.com/fault-domain` label in the pod specification. Use the `oci.oraclecloud.com/fault-domain` label to specify the fault domain in which worker nodes must have been placed.
You'll typically use the `oci.oraclecloud.com/fault-domain` label to achieve high availability when a cluster is located in a region with a single availability domain.
For example:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
spec:
 containers:
 - name: nginx
  image: nginx:latest
  ports:
  - containerPort: 80
 nodeSelector:
  oci.oraclecloud.com/fault-domain: FAULT-DOMAIN-3
```

If you apply the above example pod spec to a cluster, an nginx pod is only created if the cluster has worker nodes in FAULT-DOMAIN-3 in the availability domain. If the cluster only has worker nodes in FAULT-DOMAIN-1 or FAULT-DOMAIN-2, the pod is not created and remains in a pending status.
If a cluster has worker nodes in multiple availability domains, include both the `failure-domain.beta.kubernetes.io/zone` label and the `oci.oraclecloud.com/fault-domain` label in a pod specification to specify both the availability domain and the fault domain of the worker nodes on which to run the pod.
## node.kubernetes.io/exclude-from-external-load-balancers 🔗 
Kubernetes Engine automatically enables the `ServiceNodeExclusion` feature gate on the clusters it creates. With the `ServiceNodeExclusion` feature gate enabled on a cluster, you can add a label to particular managed nodes to exclude them from the list of backend servers in an Oracle Cloud Infrastructure load balancer backend set. The fewer worker nodes included in a backend set, the faster the load balancer can be updated.
To exclude a worker node from the list of backend servers in a backend set, add the `node.kubernetes.io/exclude-from-external-load-balancers` label to the node by entering:
Command
CopyTry It
```
kubectl label nodes <node-name> node.kubernetes.io/exclude-from-external-load-balancers=true
```

For example:
Command
CopyTry It
```
kubectl label nodes 10.0.1.2 node.kubernetes.io/exclude-from-external-load-balancers=true
```

Note that having added the label to a node, the node is excluded from the list of backend servers regardless of the value of the label. For example, even if you specify `node.kubernetes.io/exclude-from-external-load-balancers       label=false`, the worker node is still excluded from the list of backend servers.
To remove the label from the node, enter:
Command
CopyTry It
```
kubectl label nodes <node-name> node.kubernetes.io/exclude-from-external-load-balancers-
```

To exclude all the nodes in a node pool from the list of backend servers, add `node.kubernetes.io/exclude-from-external-load-balancers=true` to the node pool's **Kubernetes Labels** property when you create or modify the node pool.
Note that the `node.kubernetes.io/exclude-from-external-load-balancers` label is not supported with virtual nodes.
Was this article helpful?
YesNo

