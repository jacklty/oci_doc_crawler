Updated 2024-08-14
# Applying Tags to Node Pools
_Find out how to apply tags to node pools you create using Kubernetes Engine (OKE)._
When you create a managed node pool or a virtual node pool, you can optionally apply tags to the node pool resource. These tags are referred to as **node pool tags**. You can specify both defined tags and free-form tags as node pool tags.
Tag defaults with default values that are specified for the node pool's compartment are automatically applied to the node pool resource. Tag defaults with user-applied values are only applied to the node pool resource if the node pool is in a different compartment to the cluster. If that is the case, then you must specify a value for tag defaults with user-applied values by specifying node pool tags, as described in this section.
Note the following:
  * If you use the 'Quick Create' workflow to create a new cluster, the free-form tags `"OKEclusterName": <cluster-name>` and `"OKEnodePoolName": <node-pool-name>` are also automatically added to node pools in the new cluster. The tags are not added to node pools if you use the 'Custom Create' workflow to create the cluster. Note that the values of these tags do not change if you subsequently change the name of the cluster or node pool.
  * Node pool tags are not applied to worker nodes in the node pool. To apply tags to worker nodes, see [Applying Tags to Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-tags.htm#contengtaggingclusterresources_tagging_oke_resources_node_tags "Find out how to apply tags to worker nodes in node pools you create using Kubernetes Engine \(OKE\).").
  * To apply defined tags from a tag namespace belonging to one compartment to a node pool belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See [Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm#contengtaggingclusterresources_iam-tag-namespace-policy "Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine \(OKE\).").


## Using the Console to Specify Node Pool Tags
To add a node pool tag to a new node pool when creating a new cluster:
  1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a new cluster.
  2. Display the **Node pool tags** section of the **Node pools** page.
  3. To add a defined tag to the node pool: 
     * **Tag namespace:** Select the tag namespace to which the tag belongs.
     * **Tag key:** Select the name of the defined tag to apply to the node pool.
     * **Tag value:** Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
  4. To add a free-form tag to the node pool: 
     * **Tag namespace:** Set to None (free-form tags do not belong to a tag namespace).
     * **Tag key:** Enter a name for the free-form tag to apply to the node pool.
     * **Tag value:** Enter a value for the tag to apply to the node pool.


To update node pool tags applied to an existing node pool:
  1. Follow the instructions in [Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\).") to update an existing node pool.
  2. Display the **Node pool tags** tab of the **Node pool details** page.
  3. Click **Add tags** to add, remove, and change the value of defined tags and free-form tags applied to the node pool.


## Using the CLI to Specify Managed Node Pool Tags 🔗 
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--kubernetes-version <kubernetes-version> \
--name <node-pool-name> \
--node-shape <node-shape> \
--defined-tags <json-name-value-pairs> \
--freeform-tags <json-name-value-pairs>
```

For example:
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd \
--compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q \
--kubernetes-version v1.20.11 \
--name Finance-Node-Pool \
--node-shape VM.Standard2.1 \
--defined-tags {"Operations": {"CostCenter": "42"}} \
--freeform-tags {"Department": "Finance"}
```

## Using the CLI to Specify Virtual Node Pool Tags
```
oci ce virtual-node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--display-name <node-pool-name> \
--kubernetes-version <kubernetes-version> \
--placement-configurations "[{\"availabilityDomain\":\"<ad-name>\",\"faultDomain\":[\"FAULT-DOMAIN-<n>\"],\"subnetId\":\"<virtualnode-subnet-ocid>\"}]" \
--nsg-ids "[\"<virtual-node-nsg-ocid>\"]" \
--pod-configuration "{\"subnetId\":\"<pod-subnet-ocid>\",\"nsgIds\":[\"<pod-nsg-ocid>\"],\"shape\":\"<shape-name>\"}" \
--size <number-of-nodes> \
--defined-tags <json-name-value-pairs> \
--freeform-tags <json-name-value-pairs>
```

For example:
```
oci ce virtual-node-pool create \
--cluster-id ocid1.cluster.oc1.phx.aaaaaaaa______w5q \
--compartment-id ocid1.compartment.oc1..aaaaaaaa______n5q \
--display-name sales-vnp \
--kubernetes-version v1.24.1 \
--placement-configurations "[{\"availabilityDomain\":\"GMvH:PHX-AD-1\",\"faultDomain\":[\"FAULT-DOMAIN-1\"],\"subnetId\":\"ocid1.subnet.oc1.phx.aaaaaaaa______sra\"}]" \
--nsg-ids "[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______hpa\"]" \
--pod-configuration "{\"subnetId\":\"ocid1.subnet.oc1.phx.aaaaaaaa______o7q\",\"nsgIds\":[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______osq\"],\"shape\":\"Pod.Standard.E4.Flex\"}" \
--size 1 \
--defined-tags {"Operations": {"CostCenter": "43"}} \
--freeform-tags {"Department": "Sales"}
```

## Using the API to Specify Node Pool Tags
To add and update managed node pool tags, use the `freeformTags` and `definedTags` attributes of the `CreateNodePoolDetails` and `UpdateNodePoolDetails` objects used by the [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool) and [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool) operations.
To add and update virtual node pool tags, use the `freeformTags` and `definedTags` attributes of the `CreateVirtualNodePoolDetails` and `UpdateVirtualNodePoolDetails` objects used by the CreateVirtualNodePool and UpdateVirtualNodePool operations.
Was this article helpful?
YesNo

