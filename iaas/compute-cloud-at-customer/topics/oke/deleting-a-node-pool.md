Updated 2024-12-16
# Deleting an OKE Node Pool
Learn how to delete an OKE node pool on Compute Cloud@Customer.
**Caution**
Deleting a node pool permanently deletes the node pool. You can't recover a deleted node pool.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-node-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. Click the name of the cluster that contains the node pool that you want to delete.
    3. On the cluster details page, under **Resources** , click **Node Pools**.
    4. For the node pool that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    5. Confirm the deletion.
      1. Enter the name of the node pool to confirm that you want to delete the node pool.
      2. Check the box to override the eviction grace duration in the cordon and drain settings for the nodes in the pool.
Use the arrows to decrease or increase the number of minutes of eviction grace duration. See the description of this field in [Updating an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm#updating-a-node-pool "On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.").
You can't clear **Force terminate after grace period**. Nodes are deleted after their pods are evicted or at the end of the eviction grace duration, even if not all pods are evicted.
For descriptions of cordon and drain and eviction grace duration, go to [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster."), click the CLI tab, and see _Node and node pool deletion settings_.
      3. Click **Delete**.
  * Use the [oci ce node-pool delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete.html) command and required parameters to delete a node pool.
Copy
```
oci ce node-pool delete --node-pool-id <node-pool_OCID> [OPTIONS]
```

    1. Get the OCID of the node pool that you want to delete: `oci ce               node-pool list`
    2. Run the delete node pool command. You can use the optional `--force               option` to delete the node pool without prompting for confirmation.
Example:
Copy
```
$ oci ce node-pool delete --node-pool-id ocid1.nodepool. _unique_ID_ --force
```

You can use the `--override-eviction-grace-duration` option to set a new value for `evictionGraceDuration` for this node pool deletion. See the description of `--node-eviction-node-pool-settings` in [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.").
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNodePool) operation to delete a node pool.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

