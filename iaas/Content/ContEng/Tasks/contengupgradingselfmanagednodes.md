Updated 2025-01-15
# Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node
_Find out how to upgrade the version of Kubernetes running on a self-managed node in an enhanced cluster created with Kubernetes Engine._
**Note** This section applies to self-managed nodes only. For information about upgrading managed nodes, see [Upgrading Managed Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm#Upgrading_the_Kubernetes_Version_on_Worker_Nodes_in_a_Cluster "Find out about the different ways to upgrade the Kubernetes version on managed nodes in clusters you've created with Kubernetes Engine \(OKE\).").
You can 'upgrade' the version of Kubernetes running on a self-managed node by replacing the original self-managed node with a new self-managed node running the newer Kubernetes version. Having drained the original self-managed node to prevent new pods starting and to delete existing pods, you can then terminate the compute instance hosting the original self-managed node.
Note that when creating the new self-managed node, it is your responsibility to specify an image containing a Kubernetes version that complies with the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/) described in the Kubernetes documentation. Kubernetes Engine does not check that the Kubernetes version in the image you specify for the new self-managed node is compatible with the Kubernetes version running on the cluster's control plane nodes. See [Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs).
To 'upgrade' the version of Kubernetes running on a self-managed node by replacing the original self-managed node with a new self-managed node:
  1. Create a new compute instance to host the new self-managed node:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. 
    2. Follow the instructions in the [Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See [Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm#contengprereqsforselfmanagednodes-accessreqs "Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine.").
    3. In the **Image and Shape** section, click **Change image**. 
    4. Click **My images** , select the **Image OCID** option, and then enter the OCID of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) image running the newer Kubernetes version. See [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
    5. Click **Show advanced options** , and on the **Management** tab, select the **Paste cloud-init script** option.
    6. Copy and paste the cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate into the **Cloud-init script** field. See [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.").
    7. Click **Create** to create the compute instance to host the self-managed node.
When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified. 
  2. Verify that the self-managed node has been added to the Kubernetes cluster and confirm the node's readiness status by entering:
Command
CopyTry It
```
kubectl get nodes
```

For example:
```
kubectl get nodes
NAME      STATUS  ROLES  AGE  VERSION
10.0.103.170  Ready  <none>  40m  v1.25.4
```

  3. Confirm that labels have been added to the node and set as expected by entering:
Command
CopyTry It
```
kubectl get node <node-name> -o json | jq '.metadata.labels'
```

For example
```
kubectl get node 10.0.103.170 -o json | jq '.metadata.labels'
{
...
"displayName": "oke-self-managed-node",
"oci.oraclecloud.com/node.info.byon": "true",
...
}
```

  4. If there are labels attached to the original self-managed node and those labels are used by selectors (for example, to determine the nodes on which to run pods), then use the `kubectl label nodes` command to attach the same labels to the new self-managed node. See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#step-one-attach-label-to-the-node) in the Kubernetes documentation.
  5. Prevent new pods from starting, and delete existing pods, on the original self-managed node by entering:
Command
CopyTry It
```
kubectl drain <node_name>
```

For more information:
     * about using kubectl, see [Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm#Accessing_a_Cluster_Using_Kubectl "Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
     * about the drain command, see [drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) in the Kubernetes documentation
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the drain operation.
  6. When you have drained the original self-managed node and pods are running on the new self-managed node, terminate the compute instance hosting the original self-managed node. See [Terminating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm).


Was this article helpful?
YesNo

