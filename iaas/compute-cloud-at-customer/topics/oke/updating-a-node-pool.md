Updated 2024-12-16
# Updating an OKE Node Pool
On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.
When you update node properties, by default existing nodes aren't updated. The updated values only apply to new nodes that are created. New nodes are created when you increase the node count, change the fault domain, or change the subnet.
**Important**
If you change the fault domain or subnet of a node pool, existing worker nodes are terminated and new worker nodes are created using the updated configuration.
To replace existing nodes with new nodes that use these updated settings, see [Node Cycling an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm#node-cycling-an-oke-node-pool "On Compute Cloud@Customer, when you update a node pool, only new nodes that are added during this update or that are added later receive the updates. To replace existing nodes with new nodes that use updated settings, enable the node cycling option.").
If you make changes that add new worker nodes, perform the following steps:
  1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
  2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
  3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").


To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. Click the name of the cluster that contains the node pool that you want to update.
    3. On the cluster details page, under **Resources** , click **Node Pools**.
    4. For the node pool that you want to update in the **Node Pools** list, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
The **Edit Node Pool** dialog box opens. You can change any configuration except the compartment where new nodes are created. 
In the **Cordon and Drain** settings: Enter the number of minutes of eviction grace duration, or use the arrows to decrease or increase the number of minutes of eviction grace duration. The maximum value and default value is 60 minutes.
You can't clear **Force terminate after grace period**. For descriptions of cordon and drain and eviction grace duration, go to [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster."), click the CLI tab, and see _Node and node pool deletion settings_.
**Note**
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the node pool resource.
    5. When you're finished making changes, click **Save Changes**.
The details page for the node pool is displayed. In addition to **Node Pool Information** and **Tags** tabs, the node pool details page has a **Placement Configuration** tab.
The updated configuration only applies to new nodes that are created by this procedure or in the future.
To replace existing nodes with new nodes that use these updated settings, see [Node Cycling an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm#node-cycling-an-oke-node-pool "On Compute Cloud@Customer, when you update a node pool, only new nodes that are added during this update or that are added later receive the updates. To replace existing nodes with new nodes that use updated settings, enable the node cycling option.").
**What's Next:**
If you make changes that add new worker nodes, consider your next steps:
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
  * Use the [oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html) command and required parameters to update a node pool.
Copy
```
oci ce node-pool update --node-pool-id <node-pool_OCID> [OPTIONS]
```

    1. Get the information you need to run the command.
       * The OCID of the node pool that you want to update: `oci ce node-pool list`
       * (Optional) Node and node pool deletion settings. Use the `--node-eviction-node-pool-settings` option or the `--override-eviction-grace-duration` option to set the eviction grace duration for nodes. Nodes are always deleted after their pods are evicted or at the end of the eviction grace duration. See the description in [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.").
       * (Optional) Labels. To add labels to new nodes, use the `--initial-node-labels` option. Labels on existing nodes cannot be changed by using the `--initial-node-labels` option. Labels on existing nodes can be modified using `kubectl`. For more information about node labels, see [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.").
       * (Optional) Tags. Add, change, or delete defined or free-form tags for the node pool resource by using the `--defined-tags` and `--freeform-tags` options. Do not specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the node pool resource.
To add tags to nodes that are newly added to the node pool, use the `--node-defined-tags` and `--node-freeform-tags` options.
    2. (Optional) Create an argument for the `--node-pool-cycling-details` option, and use that option to apply these updates to all of the nodes in the node pool.
Without the `--node-pool-cycling-details` option, the updated configuration specified in this `node-pool update` command only applies to new nodes that are created by this command or in the future, as described at the beginning of this topic.
To replace existing nodes with new nodes that use these updated settings, specify the `--node-pool-cycling-details` option as described in [Node Cycling an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm#node-cycling-an-oke-node-pool "On Compute Cloud@Customer, when you update a node pool, only new nodes that are added during this update or that are added later receive the updates. To replace existing nodes with new nodes that use updated settings, enable the node cycling option.").
    3. Run the update node pool command.
Copy
```
$ oci ce node-pool update --node-pool-id ocid1.nodepool.unique_ID \
<new_configuration_settings>
```

**What's Next:**
If you make changes that add new worker nodes, consider your next steps: 
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool) operation to update a node pool.
If you make changes that add new worker nodes, consider your next steps:
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

