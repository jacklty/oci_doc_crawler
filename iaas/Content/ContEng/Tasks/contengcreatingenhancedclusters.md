Updated 2024-08-14
# Creating an Enhanced Cluster
_Find out how to create an enhanced cluster using Kubernetes Engine (OKE)._
You can create enhanced clusters using the Console, the CLI, and the API. Regardless of how you create it, the cluster you create must be [VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters). 
Note the following when creating clusters:
  * When using the Console to create a cluster, if you don't select any enhanced features during cluster creation, you have the option to create the new cluster as a basic cluster. A new cluster is created as an enhanced cluster by default, unless you explicitly choose to create a basic cluster.
  * When using the CLI or the API to create a cluster, you can specify whether to create a basic cluster or an enhanced cluster. If you don't explicitly specify the type of cluster to create, a new cluster is created as a basic cluster by default.


Note that once you have created an enhanced cluster, you cannot downgrade the enhanced cluster to a basic cluster.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingenhancedclusters.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingenhancedclusters.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingenhancedclusters.htm)


  * To create an enhanced cluster using the Console:
    1. Follow the instructions in either of the following topics to create the cluster:
       * [Using the Console to create a Cluster with Default Settings in the 'Quick Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm#create-quick-cluster "Find out how to use the 'Quick Create' workflow to create a Kubernetes cluster with default settings and new network resources using Kubernetes Engine \(OKE\).")
       * [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).")
    2. If you select one or more of the enhanced cluster features in the 'Quick Create' or 'Custom Create' workflows, skip the remaining steps in this task because the new cluster is automatically created as an enhanced cluster.
Enhanced cluster features include:
       * Virtual node pools and virtual nodes (both 'Quick Create' and 'Custom Create' workflows). See [Working with Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithvirtualnodes.htm#contengspecifyingvirtualnodes "Find out about virtual nodes, the differences between virtual nodes and managed nodes, and how to create virtual nodes using Kubernetes Engine \(OKE\).").
       * Cluster add-on management ('Custom Create' workflow only). See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
When you have not selected any of the enhanced cluster features, the **Create a Basic cluster** option is shown on the **Review** page of the workflow. By default, the **Create a Basic cluster** option is not selected, so the new cluster is created as an enhanced cluster unless you explicitly specify that you want to create a basic cluster.
    3. If you want to create the new cluster as an enhanced cluster even though you did not select any enhanced cluster features, simply ensure that you do not choose the **Create a Basic cluster** option on the **Review** page of the workflow.
    4. Click **Create cluster** to create the new cluster as an enhanced cluster.
    5. Verify that you have created the new cluster as an enhanced cluster by confirming that the **Cluster Details** page shows **Cluster type: Enhanced**.
  * Use the [oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html) command and required parameters to create an enhanced cluster:
Command
CopyTry It
```
oci ce cluster create --compartment-id <compartment-ocid> --kubernetes-version <kubernetes-version> --name <cluster-name> --vcn-id <vcn-ocid> --endpoint-subnet-id <subnet-id> --type ENHANCED_CLUSTER [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce cluster create --compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q --kubernetes-version v1.25.4 --name Finance-Cluster --vcn-id ocid1.vcn.oc1.iad.aaaaaae___yja --endpoint-subnet-id ocid1.subnet.oc1.phx.aaaaaaaa______sna --type ENHANCED_CLUSTER
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create an enhanced cluster.


Was this article helpful?
YesNo

