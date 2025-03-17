Updated 2025-02-12
# Creating Virtual Nodes and Virtual Node Pools in a New Cluster
_Find out how to create virtual nodes and virtual node pools in a new cluster using Kubernetes Engine (OKE)._
You can create virtual nodes by creating a virtual node pool in a new cluster. You can only create virtual nodes and virtual node pools in enhanced clusters.
See also [Creating a Virtual Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm#create-virtual-node-pool "Find out how to create a virtual node pool using Kubernetes Engine \(OKE\).").
You can create virtual nodes and virtual node pools using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm)


  * To create a cluster with a virtual node pool and virtual nodes using the Console:
    1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a new cluster.
    2. On the **Network Setup** page, specify **VCN-native pod networking** as the network type for the cluster.
    3. On the **Node Pools** page, specify a **Name** and **Compartment** for the virtual node pool you want to create.
    4. Specify the **Node Type:** of worker nodes in this node pool as **Virtual**.
    5. Define the virtual node pool:
      1. Specify configuration details for the virtual node pool:
         * **Node Placement Configuration:**
           * **Availability domain:** An availability domain in which to place virtual nodes.
           * **Fault domains:** (Optional) One or more fault domains in the availability domain in which to place virtual nodes.
Optionally click **Another Row** to select additional domains and subnets in which to place virtual nodes.
When the virtual nodes are created, they are distributed as evenly as possible across the availability domains and fault domains you select. If you don't select any fault domains for a particular availability domain, the virtual nodes are distributed as evenly as possible across all the fault domains in that availability domain.
         * **Node count:** The number of virtual nodes to create in the virtual node pool, placed in the availability domains you select, and in the regional subnet (recommended) or AD-specific subnet you specify for each availability domain. 
         * **Pod shape:** The shape to use for pods running on virtual nodes in the virtual node pool. The shape determines the processor type on which to run the pod.
Only those shapes available in your tenancy that are supported by Kubernetes Engine are shown. See [Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#Supported_Images_Including_Custom_Images_and_Shapes_for_Worker_Nodes "Find out about the images and shapes you can specify for worker nodes in clusters created by Kubernetes Engine \(OKE\).").
Note that you explicitly specify the CPU and memory resource requirements for virtual nodes in the pod spec (see [Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/) and [Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/) in the Kubernetes documentation).
         * **Virtual node communication:**
           * **Subnet:** A regional subnet (recommended) or AD-specific subnet configured to host virtual nodes. If you specified load balancer subnets, the virtual node subnets must be different. The subnets you specify can be private (recommended) or public, and can be regional (recommended) or AD-specific. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, the virtual node subnet must be private). See [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig). 
           * **Use security rules in Network Security Group (NSG):** Control access to the virtual node subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see [Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
         * **Pod communication:** Pods running on virtual nodes use VCN-native pod networking. Specify how pods in the node pool communicate with each other using a pod subnet: 
           * **Subnet:** A regional subnet configured to host pods. The pod subnet you specify for virtual nodes must be private. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). See [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig).
           * **Use security rules in Network Security Group (NSG):** Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see [Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
For more information about pod communication, see [Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm#podnetworking "Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
      2. Either accept the defaults for advanced virtual node pool options, or click **Show advanced options** and specify alternatives as follows:
         * **Node pool tags:** (Optional) One or more tags to add to the virtual node pool. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See [Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm#contengtaggingclusterresources "Find out about tagging cluster-related resources you create using Kubernetes Engine \(OKE\).").
         * **Kubernetes labels and taints:** (Optional) Enable the targeting of workloads at specific node pools by adding labels and taints to virtual nodes:
           * **Labels:** One or more labels (in addition to a default label) to add to virtual nodes in the virtual node pool to enable the targeting of workloads at specific node pools. 
           * **Taints:** One or more taints to add to virtual nodes in the virtual node pool. Taints enable virtual nodes to repel pods, thereby ensuring that pods do not run on virtual nodes in a particular virtual node pool. Note that you can only apply taints to virtual nodes.
For more information, see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
    6. Click **Next** to review the details you entered for the new cluster.
    7. Click **Create Cluster** to create the new cluster.
  * Use the [oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html) and [oci ce virtual-node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/create.html) commands (and required parameters) to create a new cluster with a virtual node pool and virtual nodes:
    1. Create a new cluster, specifying the OCI VCN-Native Pod Networking CNI plugin for pod networking:
Copy
```
oci ce cluster create \
--compartment-id <compartment-ocid> \
--name <cluster-name> \
--vcn-id <vcn-ocid> \
--type ENHANCED_CLUSTER \
--kubernetes-version <kubernetes-version> \
--service-lb-subnet-ids "[\"<lb-subnet-ocid>\"]" \
--endpoint-subnet-id <api-endpoint-subnet-ocid> \
--endpoint-public-ip-enabled <true|false> \
--endpoint-nsg-ids "[\"<api-endpoint-nsg-ocid>"]" \
--cluster-pod-network-options '[{"cniType":"OCI_VCN_IP_NATIVE"}]'
```

For example:
Copy
```
oci ce cluster create \
--compartment-id ocid1.compartment.oc1..aaaaaaaa______n5q \
--name sales \
--vcn-id ocid1.vcn.oc1.phx.aaaaaaaa______lhq \
--type ENHANCED_CLUSTER \
--kubernetes-version v1.25.4 \
--service-lb-subnet-ids "[\"ocid1.subnet.oc1.phx.aaaaaaaa______g7q"]" \
--endpoint-subnet-id ocid1.subnet.oc1.phx.aaaaaaaa______sna \
--endpoint-public-ip-enabled true \
--endpoint-nsg-ids "[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______5qq\"]" \
--cluster-pod-network-options '[{"cniType":"OCI_VCN_IP_NATIVE"}]'
```

    2. Obtain the OCID of the new cluster for use in the next step.
    3. Create a new virtual node pool in the cluster:
Copy
```
oci ce virtual-node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--display-name <node-pool-name> \
--kubernetes-version <kubernetes-version> \
--placement-configurations "[{\"availabilityDomain\":\"<ad-name>\",\"faultDomain\":[\"FAULT-DOMAIN-<n>\"],\"subnetId\":\"<virtualnode-subnet-ocid>\"}]" \
--nsg-ids "[\"<virtual-node-nsg-ocid>\"]" \
--pod-configuration "{\"subnetId\":\"<pod-subnet-ocid>\",\"nsgIds\":[\"<pod-nsg-ocid>\"],\"shape\":\"<shape-name>\"}" \
--size <number-of-nodes>
```

where:
       * `<ad-name>` is the name of the availability domain in which to place virtual nodes. To find out the availability domain name to use, run:
Copy
```
oci iam availability-domain list
```

       * `<shape-name>` is one of `Pod.Standard.E3.Flex`, `Pod.Standard.E4.Flex`.
For example:
Copy
```
oci ce virtual-node-pool create \
--cluster-id ocid1.cluster.oc1.phx.aaaaaaaa______w5q \
--compartment-id ocid1.compartment.oc1..aaaaaaaa______n5q \
--display-name sales-vnp \
--kubernetes-version v1.24.1 \
--placement-configurations "[{\"availabilityDomain\":\"GMvH:PHX-AD-1\",\"faultDomain\":[\"FAULT-DOMAIN-1\"],\"subnetId\":\"ocid1.subnet.oc1.phx.aaaaaaaa______sra\"}]" \
--nsg-ids "[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______hpa\"]" \
--pod-configuration "{\"subnetId\":\"ocid1.subnet.oc1.phx.aaaaaaaa______o7q\",\"nsgIds\":[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______osq\"],\"shape\":\"Pod.Standard.E4.Flex\"}" \
--size 1
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/CreateVirtualNodePool) operation to create a virtual node pool and virtual nodes in an existing cluster.


Was this article helpful?
YesNo

