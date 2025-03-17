Updated 2024-08-23
# Kubernetes Versions and Kubernetes Engine (OKE)
_Find out about the Kubernetes versioning scheme and Kubernetes Engine (OKE) support for different Kubernetes versions._
Kubernetes version numbers have the format `x.y.z` where `x` is a major version, `y` is a minor version, and `z` is a patch version. For example, 1.30.1.
The Kubernetes project supports the most recent three minor versions of Kubernetes.
When you create a new Kubernetes cluster using Kubernetes Engine, you specify:
  * The version of Kubernetes to run on the control plane nodes in the cluster.
  * The version of Kubernetes to run on the worker nodes in the cluster. Different worker nodes in the same node pool can run different versions of Kubernetes. Different node pools in a cluster can run different versions of Kubernetes.


The version of Kubernetes that you specify for the worker nodes in a cluster must be either the same Kubernetes version as that running on the control plane nodes, or an earlier Kubernetes version that is still compatible. As described in the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/), a certain amount of version variation is permissible between control plane nodes and worker nodes in a cluster:
  * The control plane nodes must run the same version of Kubernetes as the version running on worker nodes, or must be no more than two versions (or three versions, starting from Kubernetes version 1.28) ahead. 
  * The worker nodes can run a version of Kubernetes that lags behind the version on the control plane nodes by up to two versions (or three versions, starting from Kubernetes version 1.28), but no more. If the version on the worker nodes is more than two versions (or three versions, starting from Kubernetes version 1.28) behind the version on the control plane nodes, the Kubernetes versions on the worker nodes and the control plane nodes are incompatible.
  * The worker nodes in a cluster must not run a more recent version of Kubernetes than the associated control plane nodes.


The restrictions ensure that the oldest supported minor version of the kubelet and kube-proxy components running on a cluster's worker nodes are always compatible with the newest supported minor version of the kube-apiserver, kube-scheduler, kube-controller-manager, and cloud-controller-manager components running on the cluster's control plane nodes.
For more information, see the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).
## Kubernetes Minor Version Support 🔗 
Kubernetes minor versions typically introduce new features and other improvements. The Kubernetes project regularly releases minor versions, three times a year.
Oracle monitors and validates the minor versions released by the Kubernetes project, and releases Kubernetes Engine support for minor versions in a timely fashion.
Kubernetes Engine supports three minor versions of Kubernetes for new clusters. For a minimum of 30 days after the announcement of support for a new Kubernetes version, Kubernetes Engine continues to support the fourth oldest available Kubernetes minor version. After that time, the older Kubernetes version ceases to be supported.
When a minor version is no longer supported, you cannot: 
  * Create new clusters running that minor version.
  * Add new node pools running that minor version.


Oracle therefore recommends that you upgrade any existing clusters that are currently running a soon-to-be unsupported minor version to run a minor version that Kubernetes Engine does support. Clusters that are not upgraded will continue to function as expected. However, they will no longer be supported.
You can upgrade control plane nodes through unsupported minor versions. Kubernetes requires that you upgrade control plane nodes one minor version at a time. However, you do not have to upgrade worker nodes one minor version at a time.
## Kubernetes Patch Version Support 🔗 
Kubernetes patch versions typically address critical bugs or security vulnerabilities that have been recently identified in a Kubernetes minor version. The Kubernetes project frequently releases patch versions, typically once a month, but sometimes more frequently.
Oracle monitors and validates the patch versions released by the Kubernetes project, and releases Kubernetes Engine support for critical patch versions in a timely fashion.
When Oracle notifies you of Kubernetes Engine support for a new Kubernetes patch version, we recommend that you upgrade any clusters running the corresponding minor version of Kubernetes to the latest available patch version as soon as possible. You have thirty days after the announcement of Kubernetes Engine support for a new Kubernetes patch version to upgrade clusters from an older patch version to the new patch version. After thirty days, clusters running the older patch version are no longer supported. 
Note that although clusters running an older patch version cease to be supported after thirty days, the older patch version might continue to be available for selection. However, Oracle strongly recommends you select the latest patch version.
Was this article helpful?
YesNo

