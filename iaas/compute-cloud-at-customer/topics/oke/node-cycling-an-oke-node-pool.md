Updated 2024-12-16
# Node Cycling an OKE Node Pool
On Compute Cloud@Customer, when you update a node pool, only new nodes that are added during this update or that are added later receive the updates. To replace existing nodes with new nodes that use updated settings, enable the node cycling option.
Node cycling performs an in-place update of all existing nodes in the node pool to the latest specified configuration. New nodes are created, workloads moved onto them from existing nodes, current node pool updates applied, and the original nodes terminated.
You can set the maximum number of nodes that are starting or terminating at any particular time.
  * **Maximum surge**. The maximum number of new nodes that can be starting at any time during this update operation. Set this value to avoid adding too many new nodes before existing nodes are terminated, which could incur excessive cost. The default value is 1. The maximum value is 5.
  * **Maximum unavailable**. The maximum number of existing nodes that can be terminating at any time during this update operation. Set this value to ensure that enough nodes remain to handle the workload. The default value is 0. The maximum value is 7.


One of these values must be greater than 0.
Both of these values can be set to either a number (from 0 to the configured number of nodes in the node pool, but not greater than the maximum cited above) or a percentage (from 0% to 100%, but not a percentage that would result in a number greater than the maximum cited above). These values can be a maximum of four characters.
If you set either of these properties to a percent value that exceeds the maximum allowed number of nodes, the error message tells you the maximum allowed percent value for this node pool.
**Note**
If the node cycling operation fails (for example, the operation times out), try re-running the operation. You might need to run the node cycling operation multiple times if the system is loaded and running at scale.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm)


  * Follow the procedure in [Updating an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm#updating-a-node-pool "On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.") to update the node pool configuration.
    1. On the node pool details page, click the Cycle Nodes button.
    2. In the Cycle Nodes dialog, enter values for the Maximum Surge and Maximum Unavailable properties.
See the rules at the beginning of this topic.
    3. Click the Cycle Nodes button in the dialog to start the node pool update operation.
To monitor the progress of the update operation, view the status of the associated work request.
  * Use the [oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html) command and required parameters to update a node pool.
Copy
```
oci ce node-pool update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Construct a command to update the node pool configuration as described in [Updating an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-node-pool.htm#updating-a-node-pool "On Compute Cloud@Customer, you can update any configuration that you can set when you create a node pool except for the compartment where nodes are created.") under the CLI tab.
    2. In that same command (not later) include the `--node-pool-cycling-details` option.
In addition to setting `maximumUnavailable` and `maximumSurge`, enable node cycling by setting `isNodeCyclingEnabled` to `true`. By default, `isNodeCyclingEnabled` is `false`, and node cycling isn't performed regardless of setting other node cycling variables.
Copy
```
$ oci ce node-pool update --node-pool-id ocid1.nodepool.** _unique_ID_** \
**_new_configuration_settings_** \
--node-pool-cycling-details '{"isNodeCyclingEnabled":true,"maximumUnavailable":"**_value_**","maximumSurge":"**_value_**"}'
```

See the beginning of this topic for the possible values.
In the following example, the image is updated for all nodes in the node pool:
Copy
```
$ oci ce node-pool update --node-pool-id ocid1.nodepool.** _unique_ID_** \
--node-source-details '{"imageId":"ocid1.image.**_unique_ID_**","sourceType":"IMAGE"}' \
--node-pool-cycling-details '{"isNodeCyclingEnabled":true,"maximumUnavailable":"5%","maximumSurge":"5%"}'
```

To monitor the progress of the update operation, view the status of the associated work request.
Find the work request OCID:
Copy
```
oci ce work-request list --compartment-id ocid1.compartment.** _unique_ID_** \
--resource-id ocid1.nodepool.**_unique_ID_**
```

Show the current state of the work request:
Copy
```
oci ce work-request get --work-request-id ocid1.workrequest.** _unique_ID_**
```

  * Use the [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool) operation to update a node pool.
If you make changes that add new worker nodes, consider your next steps:
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

