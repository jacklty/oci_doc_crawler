Updated 2025-01-15
# Performing an Out-of-Place Worker Node Update by Replacing an Existing Node Pool with a New Node Pool
_Find out how to update the properties of worker nodes in a node pool by replacing the original node pool with a new node pool that has new worker nodes with the required properties, using Kubernetes Engine (OKE)._
You can update the properties of worker nodes in a node pool by replacing the original node pool with a new node pool that has new worker nodes with the required properties. 
Having created the new node pool and specified the worker node properties you require, you drain existing worker nodes in the original node pool to prevent new pods starting and to delete existing pods. You can then delete the original node pool. When new worker nodes are started in the new node pool, they have the properties you specified.
## Using the Console 🔗 
To perform an 'out-of-place' update of a node pool in a cluster, by creating a new node pool:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster where you want to update worker node properties.
  4. On the **Cluster** page, display the **Node Pools** tab, and then click **Add Node Pool** to create a new node pool and specify the required worker node properties.
Note that if you specify a different Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See [Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).").
  5. If there are labels attached to worker nodes in the original node pool and those labels are used by selectors (for example, to determine the nodes on which to run pods), then use the `kubectl label nodes` command to attach the same labels to the new worker nodes in the new node pool. See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#step-one-attach-label-to-the-node) in the Kubernetes documentation.
  6. For the first worker node in the original node pool, prevent new pods from starting and delete existing pods by entering:
Command
CopyTry It
```
kubectl drain <node_name>
```

For more information:
     * about using kubectl, see [Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm#Accessing_a_Cluster_Using_Kubectl "Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
     * about the drain command, see [drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) in the Kubernetes documentation
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the drain operation.
  7. Repeat the previous step for each remaining worker node in the node pool, until all the worker nodes have been drained from the original node pool.
When you have drained all the worker nodes from the original node pool and pods are running on worker nodes in the new node pool, you can delete the original node pool.
  8. On the **Cluster** page, display the **Node Pools** tab, and then select **Delete Node Pool** from the **Actions** menu beside the original node pool.
The original node pool and all its worker nodes are deleted.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
### To perform an 'out-of-place' worker node update 🔗 
First create a new node pool with the worker node properties you require:
```
oci ce node-pool create \
--cluster-id <cluster-ocid> \
--name <node-pool-name> \
--node-image-id <image-ocid> \
--compartment-id <compartment-ocid> \
--kubernetes-version <version> \
--node-shape <shape> \
--placement-configs "[{\"availability-domain\":\"<domain-name>\", \"subnet-id\":\"<subnet-ocid>\"}]" \
--size <number-of-nodes> \
[OPTIONS]
```

Then, for each worker node in the original node pool, prevent new pods from starting and delete existing pods by draining each worker node in turn:
```
kubectl drain <node_name>
```

Finally, delete the original node pool:
Command
CopyTry It
```
oci ce node-pool delete --node-pool-id <node-pool-ocid> [OPTIONS]
```

For example: 
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaa____qea \
--name finance-node-pool \
--node-image-id oocid1.image.oc1.iad.aaa______vpq \
--compartment-id ocid1.compartment.oc1..aaa____fda \
--kubernetes-version v1.24.1 \
--node-shape VM.Standard2.1 \
--placement-configs "[{\"availability-domain\":\"s__D:US-ASHBURN-AD-1\", \"subnet-id\":\"ocid1.subnet.oc1.iad.aaa______2sq\"}]" \
--size 1
```

Command
CopyTry It
```
kubectl drain 10.0.10.196
```

```
kubectl drain 10.0.10.18
```
```
kubectl drain 10.0.10.84
```
```
oci ce node-pool delete --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya
```

Was this article helpful?
YesNo

