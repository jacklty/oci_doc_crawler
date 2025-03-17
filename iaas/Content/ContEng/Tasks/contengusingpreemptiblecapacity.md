Updated 2025-01-15
# Using Preemptible Capacity to Provision Worker Nodes
_Find out how to specify preemptible capacity for compute instances hosting worker nodes in the node pools of clusters you've created using Kubernetes Engine (OKE)._
When using Kubernetes Engine to define a node pool's placement configuration, you can specify preemptible capacity as the capacity type for compute instances hosting worker nodes in the node pool. Specifying preemptible capacity allows you to save money by using preemptible instances to run workloads that only need to run for brief periods or that can be interrupted when the capacity is reclaimed. 
Preemptible instances behave the same as regular compute instances, but the capacity is reclaimed when it's needed elsewhere, and the instances are terminated. If workloads are fault-tolerant and can withstand interruptions, then preemptible instances can reduce costs. For example, you can use preemptible instances to optimize costs for workloads that can tolerate interruptions, such as tests that can be stopped and resumed later. For more information, see [Preemptible Instances](https://docs.oracle.com/iaas/Content/Compute/Concepts/preemptible.htm).
When a preemptible instance hosting a worker node is to be terminated, Kubernetes Engine is notified. Before the node instance is terminated, Kubernetes Engine:
  * cordons the worker node to prevent the kube-scheduler from placing new pods onto that node
  * drains the worker node to safely evict pods, ensuring the pod's containers terminate gracefully and perform any necessary cleanup


After a preemptible instance hosting a worker node has been terminated, Kubernetes Engine attempts to create a new preemptible instance as a replacement. If Kubernetes Engine is unable to create a replacement preemptible instance after multiple attempts, a message is output.
When you choose preemptible capacity as the capacity type for a node pool:
  * Kubernetes Engine automatically adds a Kubernetes label `oci.oraclecloud.com/oke-is-preemptible=true` to the worker nodes hosted on preemptible instances. You can use the label with Kubernetes node selectors and node affinity/anti-affinity to control which pods are scheduled on those worker nodes. See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
  * Kubernetes Engine automatically adds a Kubernetes taint `oci.oraclecloud.com/oke-is-preemptible` to the worker nodes hosted on preemptible instances. You can use the taint with Kubernetes tolerations to control which pods are scheduled on those worker nodes. See [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation.
  * You can specify whether the boot volumes attached to the preemptible instances hosting worker nodes are permanently deleted if the instances are terminated. 


Note the following:
  * Many, but not all, compute shapes support preemptible instances. In particular, note that preemptible instances are not supported by bare metal shapes. You cannot create a node pool with a capacity type of preemptible capacity if the node pool's shape does not support preemptible instances. Similarly, you cannot change a node pool's capacity type to preemptible capacity if the node pool's shape does not support preemptible instances.
  * Preemptible instances have a number of limitations and restrictions. See [Support and Limitations](https://docs.oracle.com/iaas/Content/Compute/Concepts/preemptible.htm#howitworks__support).
  * Any changes you make to worker node properties only apply to new worker nodes. Updating the capacity type associated with a node pool does not impact the properties of existing worker nodes.


## Required IAM Policies for Using Preemptible Capacity 🔗 
The policies that enable you to create instances using Kubernetes Engine also allow you to create preemptible instances. See [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#Policy_Configuration_for_Cluster_Creation_and_Deployment "Find out about the IAM policies to create before using Kubernetes Engine \(OKE\).")
## Best Practices When Using Preemptible Capacity 🔗 
When you choose preemptible capacity as the capacity type for a node pool, consider the following best practices:
  * Preemptible instances are best suited for fault tolerant containerized workloads. When designing applications that might run on preemptible instances, assume that the preemptible capacity could be reclaimed (and the preemptible instances terminated) at any time.
  * Use Kubernetes node selectors and node affinity/anti-affinity, along with Kubernetes taints and tolerations, to ensure that only fault tolerant workloads are scheduled to run on preemptible instances. See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
  * Oracle recommends you do not specify preemptible capacity as the capacity type for the primary node pool in a cluster. Instead, only specify preemptible capacity for additional node pools that supplement the cluster's primary node pool.
  * Oracle recommends you avoid the situation where a node pool has a mix of capacity types. Although a mix of capacity types in the same node pool is supported, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier. For example, Oracle recommends you:
    * avoid specifying on-demand capacity in one availability domain and preemptible capacity in a second availability domain
    * avoid changing the capacity type from on-demand capacity to preemptible capacity when scaling up a node pool to add more nodes


## Using the Console 🔗 
### Creating A Cluster and Specifying Preemptible Capacity
  1. Follow the instructions to create a cluster using the 'Custom Create' workflow. See [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).").
  2. When specifying the **Placement Configuration** for a node pool in the cluster:
    1. Specify the first availability domain and subnet:
       * **Availability Domain:** Select the availability domain in which to place worker nodes.
       * **Fault Domain:** (Optional) One or more fault domains in the availability domain in which to place worker nodes.
       * **Subnet:** Select the subnet configured to host worker nodes.
    2. Click **Show Advanced Options** and specify that you want to use preemptible instances to provision worker nodes in the node pool:
       * **Capacity Type:** Select **Preemptible Capacity**.
       * **When reclaimed, permanently delete the attached boot volume:** Choose whether to permanently delete the attached boot volume when the capacity is reclaimed. 
    3. Optionally click **Another Row** to add additional availability domains, subnets, and capacity types to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.


### Creating A Node Pool and Specifying Preemptible Capacity
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster where you want to create a new node pool.
  4. On the **Cluster** page, display the **Node Pools** tab, and then click **Add Node Pool** to create a new node pool and specify the required properties for its worker nodes.
  5. When specifying the **Placement Configuration** for a node pool in the cluster:
    1. Specify the first availability domain and subnet:
       * **Availability Domain:** Select the availability domain in which to place worker nodes.
       * **Fault Domain:** (Optional) One or more fault domains in the availability domain in which to place worker nodes.
       * **Subnet:** Select the subnet configured to host worker nodes.
    2. Click **Show Advanced Options** and specify that you want to use preemptible instances to provision worker nodes in the node pool:
       * **Capacity Type:** Select **Preemptible Capacity**.
       * **When reclaimed, permanently delete the attached boot volume:** Choose whether to permanently delete the attached boot volume when the capacity is reclaimed.
    3. Optionally click **Another Row** to add additional availability domains, subnets, and capacity types to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.


### Updating A Node Pool and Specifying Preemptible Capacity
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster you want to modify.
  4. Click **Node Pools** under **Resources** , and click the name of the node pool you want to modify.
  5. On the **Node Pool Details** page, click **Edit**.
  6. When specifying the **Placement Configuration** for a node pool in the cluster:
    1. Specify the first availability domain and subnet:
       * **Availability Domain:** Select the availability domain in which to place worker nodes.
       * **Fault Domain:** (Optional) One or more fault domains in the availability domain in which to place worker nodes.
       * **Subnet:** Select the subnet configured to host worker nodes.
    2. Click **Show Advanced Options** and specify that you want to use preemptible instances to provision worker nodes in the node pool:
       * **Capacity Type:** Select **Preemptible Capacity**.
       * **When reclaimed, permanently delete the attached boot volume:** Choose whether to permanently delete the attached boot volume when the capacity is reclaimed.
    3. Optionally click **Another Row** to add additional availability domains, subnets, and capacity types to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.
  7. Save the changes.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
### Creating A Node Pool and Specifying Preemptible Capacity
To use the CLI to create a node pool that uses preemptible capacity to provision worker nodes, include the `preemptibleNodeConfig` argument in the `--placement-configs` parameter.
For example: 
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd \
--name test-node \
--node-image-id ocid1.image.oc1.iad.aaaaaaaa6______nha \
--compartment-id oocid1.compartment.oc1..aaaaaaaay______t6q \
--kubernetes-version v1.21.5 \
--node-shape VM.Standard2.1 \
--placement-configs "[{\"availability-domain\":\"IqDk:US-ASHBURN-AD-2\", \"preemptibleNodeConfig\": {\"preemptionAction\":{\"isPreserveBootVolume\":false, \"type\":\"TERMINATE\"}}, \"subnet-id\":\"ocid1.subnet.oc1.iad.aaaaaaaa2xpk______zva\", \"faultDomains\":[\"FAULT-DOMAIN-3\", \"FAULT-DOMAIN-1\"]}, {\"availability-domain\":\"IqDk:US-ASHBURN-AD-1\", \"preemptibleNodeConfig\": {\"preemptionAction\":{\"isPreserveBootVolume\":false, \"type\":\"TERMINATE\"}}, \"subnet-id\":\"ocid1.subnet.oc1.iad.aaaaaaaauhls______bpq\", \"faultDomains\": [\"FAULT-DOMAIN-1\", \"FAULT-DOMAIN-2\"]}]" \
--size 1 \
--region=us-ashburn-1 \
```

If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the `placementConfigs` attribute of the `nodeConfigDetails` object to specify capacity type when creating or updating node pools. 
If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.
Was this article helpful?
YesNo

