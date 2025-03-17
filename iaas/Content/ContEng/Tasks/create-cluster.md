Updated 2025-01-15
# Creating a Cluster
_Find out how to create a cluster using Kubernetes Engine (OKE)._
You can use Kubernetes Engine to create new Kubernetes clusters. To create a cluster, you must either belong to the tenancy's Administrators group, or belong to a group to which a policy grants the CLUSTER_MANAGE permission. See [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#Policy_Configuration_for_Cluster_Creation_and_Deployment "Find out about the IAM policies to create before using Kubernetes Engine \(OKE\).").
To ensure high availability, Kubernetes Engine performs the following tasks:
  * Creates the Kubernetes control plane on multiple Oracle-managed control plane nodes, distributing the control plane nodes across different availability domains in a region (where supported).
  * Creates worker nodes in each of the fault domains in an availability domain, distributing the worker nodes as evenly as possible across the fault domains (subject to any other infrastructure restrictions).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment in which you want to create the cluster.
    3. On the **Clusters** page, click **Create cluster**.
    4. Select one of the following workflows to create the cluster:
       * **Quick Create:** Select this workflow when you only want to specify those properties that are absolutely essential for cluster creation. When you select this option, Kubernetes Engine uses default values for many cluster properties, and creates new network resources as required.
       * **Custom Create:** Select this workflow when you want to be able to specify all of the cluster's properties, use existing network resources, and select advanced options.
For more information about the different workflows, see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).").
    5. Click **Submit**.
    6. Complete the pages of the workflow you selected. For more information, see:
       * [Using the Console to create a Cluster with Default Settings in the 'Quick Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm#create-quick-cluster "Find out how to use the 'Quick Create' workflow to create a Kubernetes cluster with default settings and new network resources using Kubernetes Engine \(OKE\).")
       * [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).")
  * Use the [oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html) command and required parameters to create a cluster:
Command
CopyTry It
```
oci ce cluster create --compartment-id <compartment-ocid> --kubernetes-version <kubernetes-version> --name <cluster-name> --vcn-id <vcn-ocid> [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce cluster create --compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q --kubernetes-version v1.24.1 --name Finance-Cluster --vcn-id ocid1.vcn.oc1.iad.aaaaaae___yja
```

**To create a cluster with a virtual node pool and virtual nodes:**
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

  * Run the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create a cluster.


Was this article helpful?
YesNo

