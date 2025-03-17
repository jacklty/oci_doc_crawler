Updated 2025-01-15
# Prerequisites for Self-Managed Node Creation
Find out the prerequisites for creating self-managed nodes.
Before you create a self-managed node and add it to a cluster:
  * Confirm the cluster to which you want to add a self-managed node is configured appropriately (see [Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs)).
  * Make sure you select an appropriate image for the compute instance hosting the self-managed node (see [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs)).


## Cluster Requirements 🔗 
The cluster to which you add a self-managed node must be an enhanced cluster.
The cluster's control plane nodes must be running Kubernetes version 1.25 (or later). To use the OCI VCN-Native Pod Networking CNI plugin for pod networking (instead of the flannel CNI plugin), the cluster's control plane nodes must be running Kubernetes version 1.27.10 (or later).
Bear in mind that the versions of Kubernetes running on control plane nodes and on worker nodes (including self-managed nodes) must be compatible, as described in the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/) in the Kubernetes documentation. That is, the Kubernetes version on control plane nodes must be no more than two minor versions (or three minor versions, starting from Kubernetes version 1.28) ahead of the Kubernetes version on worker nodes . See [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
## Image Requirements 🔗 
The Oracle Linux image you specify for a self-managed node must be one of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) images, and the image must have a Release Date of March 28, 2023 or later. 
Obtain the image OCID from [OKE Worker Node Oracle Linux 7.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-7x/) and [OKE Worker Node Oracle Linux 8.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-8x/).
Note that when creating a self-managed node, it is your responsibility to specify an image containing a Kubernetes version that complies with the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/) described in the Kubernetes documentation. Kubernetes Engine does not check that the Kubernetes version in the image you specify for a self-managed node is compatible with the Kubernetes version running on the cluster's control plane nodes. See [Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs).
**Note** For information about creating self-managed nodes that run Ubuntu, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
Was this article helpful?
YesNo

