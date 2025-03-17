Updated 2025-01-15
# Updating a Cluster
_Find out how to update a cluster using Kubernetes Engine (OKE)._
For more information about updating clusters, see [Updating Cluster Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingcluster.htm#top "Find out how to modify properties of existing Kubernetes clusters you've created using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that you want to modify.
On the **Cluster Details** tab, information about the cluster is displayed, including the following details:
       * The status of the cluster and the node pools in the cluster.
       * The cluster's OCID.
       * The Kubernetes version running on the control plane nodes in the cluster. 
       * The address of the Kubernetes API endpoint.
       * Whether pod security policies are being enforced.
    4. Click **Edit** and make the following changes as necessary: 
**Note** If you change the cluster's name or whether pod security policies are being enforced, save those changes before changing access details for the Kubernetes API endpoint.
       * Change the name of the cluster.
       * **(Kubernetes versions earlier than 1.25)** Change whether pod security policies are being enforced by enabling the cluster's PodSecurityPolicy admission controller. You must create pod security policies before enabling the PodSecurityPolicy admission controller of an existing cluster that is already in production. We also strongly recommend you first verify the cluster's pod security policies in a development or test environment. That way, you can ensure that the pod security policies work as you expect and correctly allow or refuse pods to start on the cluster. If you disable a cluster's PodSecurityPolicy admission controller, any pod security policies (along with roles, rolebindings, clusterroles, and clusterrolebindings) that you've defined aren't deleted, they're simply not enforced. See [Using Pod Security Policies with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Using_Pod_Security_Polices_with_Container_Engine_for_Kubernetes "Find out how to use pod security policies with Kubernetes clusters you've created using Kubernetes Engine \(OKE\).").
       * Change access details for the Kubernetes API endpoint, including the use of network security groups and whether to assign a public IP address to the Kubernetes API endpoint subnet. See [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
If you change whether a public IP address is assigned to the Kubernetes API endpoint subnet, you must also update route rules and security rules accordingly. See [Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b).
       * Change whether the cluster is enabled for OIDC Discovery, so that application pods running on the cluster can authenticate using OIDC Discovery when accessing APIs hosted on an external cloud provider. See [Authorizing Pods to Access Non-OCI Resources Using OpenID Connect (OIDC) Discovery](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery "Find out about using OpenID Connect \(OIDC\) Discovery to authenticate application pods running on clusters you create with Container Engine for Kubernetes \(OKE\), so that the pods can call service APIs on external cloud providers.").
       * Change cluster add-on configuration. See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
    5. If a newer version of Kubernetes is available than the one running on the control plane nodes in the cluster, the **New Kubernetes version available** button is enabled. If you want to upgrade the control plane nodes to a newer version, click **New Kubernetes version available**. For more information, see [Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#top "Find out how to upgrade the version of Kubernetes running on the control plane nodes of clusters that you create using Kubernetes Engine \(OKE\).").
    6. Use the **Cluster tags** tab, the **Initial load balancer tags** tab, and the **Initial block volume tags** tab, to add or modify the following tags as needed:
       * Tags applied to the cluster.
       * Tags applied to load balancers created by Kubernetes services of type LoadBalancer.
       * Tags applied to block volumes created by Kubernetes persistent volume claims.
Tagging enables you to group disparate resources across compartments, and enables you to annotate resources with your own metadata. For more information, see [Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm#contengtaggingclusterresources "Find out about tagging cluster-related resources you create using Kubernetes Engine \(OKE\)."). 
    7. Under **Resources** , click **Metrics** to monitor the health, capacity, and performance of the cluster. For more information, see [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").
    8. Under **Resources** , click **Node pools** to perform the following actions:
       * View information about each of the node pools in the cluster, including the following details:
         * The status of the node pool.
         * The node pool's OCID.
         * The configuration currently used when starting new worker nodes in the node pool, including the Kubernetes version, the shape, and the image.
         * The availability domains, and different regional subnets (recommended) or AD-specific subnets hosting worker nodes.
You can change some of these node pool and worker node properties. For more information, see [Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\)."). 
       * Scale the cluster up or down to increase or decrease the number of node pools in the cluster by performing the following actions:
         * Add a new node pool to the cluster by clicking the **Add Node Pool** button and entering details for the new node pool.
         * Delete a node pool by selecting **Delete Node Pool** from the **Actions** menu.
For more information, see [Adding and Removing Node Pools to Scale Clusters Up and Down](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm#contengscalingclusters "Find out how to add and remove node pools to scale up and scale down the Kubernetes clusters you've created using Kubernetes Engine \(OKE\).").
    9. Under **Resources** , click **Work requests** to perform the following actions:
       * Get the details of a particular work request for the cluster resource.
       * List the work requests for the cluster resource.
For more information, see [Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.").
    10. Under **Resources** , click **Image verification** to configure clusters to only allow the deployment of images from Container Registry that have been signed by specific master encryption keys. For more information, see [Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengenforcingsignedimagesfromocir.htm#Enforcing_Use_of_Signed_Images_from_Registry "Find out how to enforce the use of signed images from Oracle Cloud Infrastructure Registry when deploying applications to a cluster you've created using Kubernetes Engine \(OKE\).").
    11. Under **Resources** , click **Quick Start** to perform the following actions:
       * Set up access to the cluster. For more information, see [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
       * Download and deploy a sample Nginx application by using the Kubernetes command line tool kubectl, from the instructions in a manifest file. For more information, see [Deploying a Sample Nginx App on a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingsamplenginx.htm#Deploying_a_Sample_Nginx_App_on_a_Cluster_Using_Kubectl "Find out how to use kubectl to deploy an Nginx app on a cluster you've created using Kubernetes Engine \(OKE\).").
    12. Under **Resources** , click **Add-ons** to perform the following actions:
       * Manage essential cluster add-ons. Essential cluster add-ons are core components of a Kubernetes cluster, and are required for a cluster to operate correctly.
       * Manage optional cluster add-ons. Optional cluster add-ons are components that you can choose to deploy on a Kubernetes cluster. Optional add-ons extend core Kubernetes functionality to improve cluster manageability and performance.
For more information, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * Use the [oci ce cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update.html) command and required parameters to update a cluster:
Command
CopyTry It
```
oci ce cluster update --cluster-id <cluster-ocid> [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce cluster update --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --name Finance-Cluster
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operation to update an existing Kubernetes cluster.


Was this article helpful?
YesNo

