Updated 2024-12-16
# Deleting an OKE Node Pool Node
Learn how to explicitly delete an OKE worker node on Compute Cloud@Customer. 
Worker nodes are also deleted when you update a node pool to scale down the node pool or change the subnet or fault domains of the node pool. See [Updating an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm#updating-a-node-pool "On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.").
**Caution**
Deleting a worker node permanently deletes the node. You can't recover a deleted worker node.
When you delete a node, by default a new node is created to satisfy the node count set for the pool. To override this behavior, select the option to decrease node pool size.
**Important**
Don't use the `kubectl delete node` command to terminate worker nodes in an OKE cluster. The `kubectl delete           node` command removes the worker node from the cluster's etcd key-value store, but the command doesn't terminate the underlying compute instance.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool-node.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool-node.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool-node.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. Click the name of the cluster that contains the node that you want to delete.
    3. On the cluster details page, under **Resources** , click **Node Pools**.
    4. Click the name of the node pool that contains the node that you want to delete.
    5. On the node pool details page, under **Resources** , click **Nodes**.
    6. For the node that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    7. Confirm the deletion.
      1. If you don't want a new node to be automatically created to replace the deleted node, select **Decrease node pool size**.
      2. Check the box to override the eviction grace duration in the cordon and drain settings for the node. See the description of this field in [Updating an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm#updating-a-node-pool "On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.").
Use the arrows to decrease or increase the number of minutes of eviction grace duration.
You can't clear "Force terminate after grace period." The node is deleted after its pods are evicted or at the end of the eviction grace duration, even if not all pods are evicted.
For descriptions of cordon and drain and eviction grace duration, go to [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster."), click the CLI tab, and see _Node and node pool deletion settings_.
      3. Click **Delete**.
  * Use the [oci ce node-pool delete-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete-node.html) command and required parameters to delete a node pool node.
Copy
```
oci ce node-pool delete-node --node-id <node_OCID> --node-pool-id <node-pool_OCID> [OPTIONS]
```

    1. Get the information you need to run the command.
       * OCID of the node pool: `oci ce node-pool list`
       * OCID of the node: `oci ce node-pool list`
    2. Run the delete node pool node command.
If you don't want a new node to be automatically created to replace the deleted node, specify the `--is-decrement-size` option.
Example:
Copy
```
$ oci ce node-pool delete-node --node-pool-id ocid1.nodepool. _unique_ID_ \
--node-id ocid1.instance._unique_ID_ --is-decrement-size true --force
```

You can use the `--override-eviction-grace-duration` option to set a new value for `evictionGraceDuration` for this node deletion. See the description of `--node-eviction-node-pool-settings` in [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster."). For `node-pool delete-node`, this new eviction grace duration value only applies to the node being deleted.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNode) operation to delete a node pool node.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

