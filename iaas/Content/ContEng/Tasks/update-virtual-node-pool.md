Updated 2025-01-15
# Updating a Virtual Node Pool
_Find out how to update a virtual node pool using Kubernetes Engine (OKE)._
For general information about updating node pools, see [Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that you want to modify.
    4. On the **Cluster details** page, under **Resources** , click **Node pools**.
    5. Click the name of the virtual node pool that you want to modify.
On the **Virtual node pool details** tab, information about the virtual node pool is displayed, including the following details:
       * The status of the node pool.
       * The node pool's OCID.
       * The type of the worker nodes in the node pool (virtual).
       * The configuration currently used when starting new virtual nodes in the node pool, including the following details:
         * The version of Kubernetes to run on worker nodes.
         * The shape to use for worker nodes.
       * The availability domains, fault domains, and different regional subnets (recommended) or AD-specific subnets hosting worker nodes.
    6. Change virtual node pool and virtual node properties as follows:
      1. Click **Edit** and specify:
         * **Name:** A different name for the node pool. Avoid entering confidential information.
         * **Node count:** A different number of virtual nodes to create in the virtual node pool, placed in the availability domains you select, and in the regional subnet (recommended) or AD-specific subnet you specify for each availability domain. See [Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm#contengscalingnodepools "Find out how to scale up and scale down the node pools you've created using Kubernetes Engine \(OKE\).").
         * **Node Placement Configuration:**
           * **Availability domain:** An availability domain in which to place virtual nodes.
           * **Fault domains:** (Optional) One or more fault domains in the availability domain in which to place virtual nodes.
Optionally click **Another Row** to select more domains and subnets in which to place virtual nodes.
When the virtual nodes are created, they're distributed as evenly as possible across the availability domains and fault domains you select. If you don't select any fault domains for a particular availability domain, the virtual nodes are distributed as evenly as possible across all the fault domains in that availability domain.
         * **Virtual Node Communication:**
           * **Subnet:** A different regional subnet (recommended) or AD-specific subnet configured to host virtual nodes. If you specified load balancer subnets, the virtual node subnets must be different. The subnets you specify can be private (recommended) or public, and can be regional (recommended) or AD-specific. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, the virtual node subnet must be private). For more information, see [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig). 
           * **Use security rules in Network Security Group (NSG):** Control access to the virtual node subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see [Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
         * **Pod Communication:**
           * **Subnet:** A different regional subnet configured to host pods. The pod subnet you specify for virtual nodes must be private. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). For more information, see [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig).
           * **Use security rules in Network Security Group (NSG):** Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see [Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
For more information about pod communication, see [Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm#podnetworking "Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
         * **Kubernetes labels and taints:** (Optional) Enable the targeting of workloads at specific node pools by adding labels and taints to virtual nodes:
           * **Labels:** One or more labels (in addition to a default label) to add to virtual nodes in the virtual node pool to enable the targeting of workloads at specific node pools. 
           * **Taints:** One or more taints to add to virtual nodes in the virtual node pool. Taints enable virtual nodes to repel pods, and so ensure that pods don't run on virtual nodes in a particular virtual node pool. You can apply taints only to virtual nodes.
For more information, see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
      2. Click **Save Changes** to save the updated properties.
    7. Use the **Node pool tags** tab to add or modify the tags applied to the virtual node pool. Tagging enables you to group disparate resources across compartments, and enables you to annotate resources with your own metadata. For more information, see [Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm#contengtaggingclusterresources "Find out about tagging cluster-related resources you create using Kubernetes Engine \(OKE\).").
    8. Under **Resources** , click the following resources to perform more actions:
       * Click **Virtual Nodes** to see information about specific worker nodes in the virtual node pool.
       * Click **Work requests** to perform the following tasks:
         * Get the details of a particular work request for the virtual node pool resource.
         * List the work requests for the virtual node pool resource.
For more information, see [Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.").
  * Use the [oci ce virtual-node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/update.html) command and required parameters to update a virtual node pool:
Command
CopyTry It
```
oci ce virtual-node-pool update --virtual-node-pool-id <virtual-node-pool-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/UpdateVirtualNodePool) operation to update a virtual node pool.


Was this article helpful?
YesNo

