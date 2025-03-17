Updated 2025-01-15
# Running Applications on Arm-based Nodes
_Find out how to run applications on Arm-based worker nodes in clusters created using Kubernetes Engine (OKE)._
To run applications on Arm-based worker nodes, you select a managed node pool and an Arm-based shape. The shape determines the number of CPUs and the amount of memory allocated to each node in the node pool. You can select Arm-based bare metal shapes and flexible VM shapes. These Ampere A1 Compute instances are based on the Ampere Altra processor (see [Arm-Based Compute](https://docs.oracle.com/iaas/Content/Compute/References/arm.htm)). For information about the OCPU count, memory, storage, and networking details of these shapes, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
You can specify an Arm-based shape for a node pool using the Console, the API, and the CLI when you create a new cluster. You can also specify an Arm-based shape when you create a new node pool. See the node pool configuration steps in [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).") and [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\).") respectively.
To view the number of reservable Arm-based cores available to you, use the Console. Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Limits, Quotas and Usage**.
Compared to other shapes, Arm-based shapes provide better price-performance, greater security isolation (because each core is single-threaded), and more consistent performance. Typically, developers use Arm-based worker nodes in Kubernetes clusters to develop and test applications.
When you deploy an application on a cluster you've created with Kubernetes Engine, you have to specify in the pod spec the compute resources that are required. To deploy the application, the kube-scheduler determines which node has the necessary resources. If a cluster has node pools with Arm-based shapes and also node pools with other shapes (for example, AMD64 shapes), you can use a nodeSelector in the pod spec to specify that an application is to run on Arm-based worker nodes. See [Defining a pod to run only on Arm-based nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrunningarmnodes.htm#contengrunningarmnodes_topic_Defining_a_pod_to_run_only_on_arm_nodes). 
If you want to deploy an application on both Arm-based and non-Arm-based worker nodes in the same cluster, use multi-architecture images (sometimes known as manifest lists) stored in an [ Open Container Initiative](https://opencontainers.org/)-compliant registry like Oracle Cloud Infrastructure Registry (see [Overview of Container Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)). You build multi-architecture images from a single source tree, with one image tag that includes images for both x86 and Arm architectures. You can build multi-architecture images using [Docker Buildx](https://github.com/docker/buildx), [Podman](https://github.com/containers/podman), and [Buildah](https://github.com/containers/buildah).
Note the following:
  * You can specify Arm-based shapes for node pools in clusters running Kubernetes version 1.19.7 or later. Do not specify an Arm-based shape for node pools running earlier versions of Kubernetes.
  * Having created a node pool with an Arm-based shape, you cannot change the node pool to have a non-Arm-based shape. Likewise, you cannot change a node pool with a non-Arm-based shape to have an Arm-based shape.
  * When you specify an Arm-based shape for a node pool, you also specify an image that is compatible with the shape. See [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).


## Defining a pod to run only on Arm-based nodes 🔗 
If a cluster has node pools with Arm-based shapes and also node pools with other shapes (for example, AMD64 shapes), you can use a nodeSelector in the pod spec to specify that an application is to run only on Arm-based worker nodes. For example, the following configuration file defines a pod to run on any Arm-based node in the cluster:
Copy
```

apiVersion: v1
kind: Pod
metadata:
 name: nginx
 labels:
  env: test
spec:
 containers:
 - name: nginx
  image: nginx
  imagePullPolicy: IfNotPresent
 nodeSelector:
  kubernetes.io/arch: arm64
```

Was this article helpful?
YesNo

