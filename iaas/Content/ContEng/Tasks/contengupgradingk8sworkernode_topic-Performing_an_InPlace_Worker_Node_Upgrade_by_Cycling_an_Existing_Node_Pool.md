Updated 2025-01-15
# Performing an In-Place Managed Node Kubernetes Upgrade by Cycling Nodes in an Existing Node Pool
_Find out how to upgrade the Kubernetes version on managed nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes, using Kubernetes Engine (OKE)._
**Note** You can only cycle nodes to perform an in-place managed node Kubernetes upgrade when using enhanced clusters. See [Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm#contengworkingwithenhancedclusters "Find out about enhanced clusters and basic clusters, the differences between them, and how to create them using Kubernetes Engine \(OKE\).").
You cannot cycle nodes with bare metal shapes. Instead, upgrade nodes with bare metal shapes by manually replacing existing nodes or the existing node pool. See [Performing an In-Place Managed Node Kubernetes Upgrade by Manually Replacing Nodes an Existing Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Updating_an_Existing_Node_Pool.htm#Performi "Find out how to upgrade the Kubernetes version on managed nodes in a node pool by changing properties of the existing node pool, and then manually replacing each managed node in turn, using Kubernetes Engine \(OKE\).") and [Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_OutofPlace_Worker_Node_Upgrade_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm#Performi2 "Find out how to upgrade the Kubernetes version on managed nodes in a node pool by replacing the original node pool with a new node pool that has managed nodes with a more recent Kubernetes version, using Kubernetes Engine \(OKE\).").
This section applies to managed nodes only. For information about upgrading self-managed nodes, see [Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm#contengupgradingselfmanagednodes "Find out how to upgrade the version of Kubernetes running on a self-managed node in an enhanced cluster created with Kubernetes Engine.").
You can upgrade the version of Kubernetes running on managed nodes in a node pool by specifying a more recent Kubernetes version for the existing node pool, and then cycling the nodes. Before cycling the nodes, you can specify both a maximum allowed number of new nodes that can be created during the upgrade operation, and a maximum allowed number of nodes that can be unavailable. 
When you cycle the nodes, Kubernetes Engine automatically replaces all existing managed nodes with new nodes that run the more recent Kubernetes version you specified. 
When cycling nodes, Kubernetes Engine cordons, drains, and terminates nodes according to the node pool's **Cordon and drain** options. 
## Balancing service availability and cost when cycling managed nodes 🔗 
Kubernetes Engine uses two strategies when cycling nodes:
  * **Create new (additional) nodes, and then remove existing nodes:** Kubernetes Engine adds an additional node (or nodes) to the node pool, running the more recent version of Kubernetes. When the additional node is active, Kubernetes Engine cordons an existing node, drains the node, and removes the node from the node pool. This strategy maintains service availability, but costs more.
  * **Remove existing nodes, and then create new nodes:** Kubernetes Engine cordons an existing node (or nodes) to make it unavailable, drains the node, and removes the node from the node pool. When the node has been removed, Kubernetes Engine adds a new node to the node pool to replace the node that has been removed. This strategy costs less, but might compromise service availability.


To tailor Kubernetes Engine behavior to meet your own requirements for service availability and cost, you can control and balance the two strategies by specifying:
  * The number of additional nodes to temporarily allow during the upgrade operation (referred to as **maxSurge**). The greater the number of additional nodes that you allow, the more nodes Kubernetes Engine can upgrade in parallel without compromising service availability. However, the greater the number of additional nodes that you allow, the greater the cost. 
  * The number of nodes to allow to be unavailable during the upgrade operation (referred to as **maxUnavailable**). The greater the number of nodes that you allow to be unavailable, the more nodes Kubernetes Engine can upgrade in parallel without increasing costs. However, the greater the number of nodes that you allow to be unavailable, the more service availability might be compromised.


In both cases, you can specify the allowed number of nodes as an integer, or as a percentage of the number of nodes shown in the node pool's **Node count** property in the Console (the node pool's **Size** property in the API). If you don't explicitly specify allowed numbers for additional nodes (**maxSurge**) and unavailable nodes (**maxUnavailable**), then the following defaults apply:
  * If you don't specify a value for either **maxSurge** or **maxUnavailable** , then **maxSurge** defaults to 1, and **maxUnavailable** defaults to 0.
  * If you only specify a value for **maxSurge** , then **maxUnavailable** defaults to 0.
  * If you only specify a value for **maxUnavailable** , then **maxSurge** defaults to 1.


You cannot specify 0 as the allowed number for both additional nodes (**maxSurge**) and unavailable nodes (**maxUnavailable**).
Note the following:
  * At the end of the upgrade operation, the number of nodes in the node pool returns to the number specified by the node pool's **Node count** property shown in the Console (the node pool's **Size** property in the API).
  * If you specify a value for **maxSurge** during the upgrade operation, your tenancy must have sufficient quota for the number of additional nodes you specify.
  * If you specify a value for **maxUnavailable** during the ugrade operation, but the node pool cannot make that number of nodes unavailable (for example, due to a pod disruption budget), the upgrade operation fails.
  * If you enter a percentage as the value of either **maxSurge** or **maxUnavailable** , Kubernetes Engine rounds up the percentage to the closest integer when calculating the allowed number of nodes.
  * If you have used `kubectl` to update nodes directly (for example, to apply a custom tag to a node), such changes are lost when Kubernetes Engine cycles the nodes.
  * When upgrading large node pools, be aware that the values you specify for **maxSurge** and **maxUnavailable** might result in unacceptably long cycle times. For example, if you specify 1 as the value for **maxSurge** when cycling the nodes of a node pool with 1000 nodes, Kubernetes Engine might take several days to cycle all the nodes in the node pool. If the node cycling operation does not complete within 30 days, the status of the associated work request is set to **Failed**. Submit another node cycling request to resume the operation.


## Using the Console 🔗 
To perform an 'in-place' upgrade of a node pool in a cluster, by specifying a more recent Kubernetes version for the existing node pool and then cycling nodes:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster where you want to change the Kubernetes version running on managed nodes.
  4. On the **Cluster** page, display the **Node Pools** tab, and click the name of the node pool where you want to upgrade the Kubernetes version running on the managed nodes.
  5. On the **Node Pool** page, click **Edit** and in the **Version** field, specify the required Kubernetes version for managed nodes.
The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.
  6. Click **Save changes** to save the change.
You now cycle nodes to automatically delete existing managed nodes, and start new managed nodes running the Kubernetes version you specified.
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the upgrade operation. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation.
  7. On the **Node Pool** page, click **Cycle nodes**.
  8. In the **Cycle nodes** dialog:
    1. Control the number of nodes to upgrade in parallel, and balance service availability and cost, by specifying:
       * **Maximum number or percentage of additional nodes (maxSurge):** The maximum number of additional nodes to temporarily allow in the node pool during the upgrade operation (expressed either as an integer or as a percentage). Additional nodes are nodes over and above the number specified in the node pool's **Node count** property. If you specify an integer for the number of additional nodes, do not specify a number greater than the value of **Node count**. 
       * **Maximum number or percentage of unavailable nodes (maxUnavailable):** The maximum number of nodes to allow to be unavailable in the node pool during the upgrade operation (expressed either as an integer or as a percentage). If you specify an integer for the number of unavailable nodes, do not specify a number greater than the value of **Node count**.
See [Balancing service availability and cost when cycling managed nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Cycling_an_Existing_Node_Pool.htm#contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Cycling_an_Existing_Node_Pool__section_balancing-service-availability-and-cost-when-cycling-nodes).
    2. Click **Cycle nodes** to start the upgrade operation.
  9. Monitor the progress of the upgrade operation by viewing the status of the associated work request (see [Getting Work Request Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#conteng-GetWorkRequest "Get the details of a work request for a cluster or node pool resource.")).


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
### To perform an 'in-place' managed node upgrade by cycling nodes 🔗 
Update the node pool's worker node Kubernetes version property, and specify the OCID of the corresponding image. Include the `--node-pool-cycling-details` parameter in the command to specify that you want to cycle the nodes in the node pool, optionally specifying a maximum allowed number of new nodes that can be created during the upgrade operation, and a maximum allowed number of nodes that can be unavailable:
Command
CopyTry It
```
oci ce node-pool update --node-pool-id <node-pool-ocid> --kubernetes-version <version> --node-source-details "{\"imageId\":\"<image-ocid>\",\"sourceType\":\"IMAGE\"}" --node-pool-cycling-details "{\"isNodeCyclingEnabled\":true,\"maximumUnavailable\":\"<value>\",\"maximumSurge\":\"<value>\"}"
```

Monitor the progress of the upgrade operation by viewing the status of the associated work request:
```
oci ce work-request list --compartment-id <compartment-ocid> --resource-id <node-pool-ocid>
```

Command
CopyTry It
```
oci ce work-request get --work-request-id <work-request-ocid>
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool) operation to upgrade nodes by specifying a more recent Kubernetes version for the existing node pool and then cycling nodes
Was this article helpful?
YesNo

