Updated 2024-08-14
# Autoscaling Kubernetes Node Pools and Pods
_Find out about autoscaling Kubernetes node pools and pods you've created using Kubernetes Engine (OKE)._
You can automatically scale the node pools and pods of clusters you create using Kubernetes Engine to optimize resource usage.
To enable cluster autoscaling by autoscaling node pools, you can deploy the Kubernetes Cluster Autoscaler (see [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).")). You can deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster in two ways:
  * as a standalone program (see [Working with the Cluster Autoscaler as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#Working_with_the_Cluster_Autoscaler "Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a standalone program to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine \(OKE\)."))
  * as a cluster add-on (see [Working with the Cluster Autoscaler as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on "Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a cluster add-on to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine \(OKE\)."))


To enable autoscaling by autoscaling pods, you deploy the Kubernetes Metrics Server to collect resource metrics from each worker node in the cluster (see [Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm#Deploying_Kubernetes_Metrics_Server_Using_Kubectl "Find out how to deploy the Kubernetes Metrics Server as a standalone program or as a cluster add-on, on a cluster you've created using Kubernetes Engine \(OKE\).")). You can deploy the Kubernetes Metrics Server on a Kubernetes cluster in two ways:
  * as a standalone program, on clusters with managed node pools or virtual node pools (see [Working with the Kubernetes Metrics Server as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_standalone.htm#contengdeployingmetricsserver_standalone "Find out how to use kubectl to deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools and virtual node pools that you've created using Kubernetes Engine \(OKE\)."))
  * as a cluster add-on, on clusters with managed node pools (see [Working with the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengdeployingmetricsserver_cluster-add-on "Find out how to use the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine \(OKE\)."))


Having deployed the Kubernetes Metrics Server, you can then use:
  * the Kubernetes Horizontal Pod Autoscaler to adjust the number of pods in a deployment (see [Using the Kubernetes Horizontal Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm#Using_Kubernetes_Horizontal_Pod_Autoscaler "Find out how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods on a cluster you've created using Kubernetes Engine \(OKE\)."))
  * the Kubernetes Vertical Pod Autoscaler to adjust the resource requests and limits for containers running in a deployment's pods (see [Using the Kubernetes Vertical Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingverticalpodautoscaler.htm#Using_the_Kubernetes_Vertical_Pod_Autoscaler "Find out how to use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in pods on a cluster you've created using Kubernetes Engine \(OKE\)."))


You can use the Kubernetes Cluster Autoscaler in a cluster with both the Kubernetes Horizontal Pod Autoscaler and the Kubernetes Vertical Pod Autoscaler.
**Note**
You can use the Kubernetes Cluster Autoscaler, the Kubernetes Metrics Server (as a cluster add-on), and the Kubernetes Vertical Pod Autoscaler with managed node pools only. You can use the Kubernetes Metrics Server (as a standalone program) and the Kubernetes Horizontal Pod Autoscaler with both virtual node pools and managed node pools.
Was this article helpful?
YesNo

