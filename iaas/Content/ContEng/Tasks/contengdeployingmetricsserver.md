Updated 2024-08-14
# Deploying the Kubernetes Metrics Server on a Cluster
_Find out how to deploy the Kubernetes Metrics Server as a standalone program or as a cluster add-on, on a cluster you've created using Kubernetes Engine (OKE)._
You can deploy the Kubernetes Metrics Server on clusters you create using Kubernetes Engine to enable autoscaling.
The Kubernetes Metrics Server is a cluster-wide aggregator of resource usage data. The Kubernetes Metrics Server collects resource metrics from the kubelet running on each worker node and exposes them in the Kubernetes API server through the Kubernetes Metrics API. Other Kubernetes add-ons require the Kubernetes Metrics Server, including:
  * the Horizontal Pod Autoscaler (see [Using the Kubernetes Horizontal Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm#Using_Kubernetes_Horizontal_Pod_Autoscaler "Find out how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods on a cluster you've created using Kubernetes Engine \(OKE\)."))
  * the Vertical Pod Autoscaler (see [Using the Kubernetes Vertical Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingverticalpodautoscaler.htm#Using_the_Kubernetes_Vertical_Pod_Autoscaler "Find out how to use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in pods on a cluster you've created using Kubernetes Engine \(OKE\)."))


You can deploy the Kubernetes Metrics Server on a Kubernetes cluster in two ways:
  * as a standalone program, on clusters with managed node pools or virtual node pools (see [Working with the Kubernetes Metrics Server as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_standalone.htm#contengdeployingmetricsserver_standalone "Find out how to use kubectl to deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools and virtual node pools that you've created using Kubernetes Engine \(OKE\)."))
  * as a cluster add-on, on clusters with managed node pools (see [Working with the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengdeployingmetricsserver_cluster-add-on "Find out how to use the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine \(OKE\)."))


Note that the Kubernetes Metrics Server is not intended to be used for anything other than autoscaling. For example, it is not recommended that you use the Kubernetes Metrics Server to forward metrics to monitoring solutions, nor as a source of monitoring solution metrics. For more information, see the [Kubernetes Metrics Server documentation on GitHub](https://github.com/kubernetes-sigs/metrics-server).
Was this article helpful?
YesNo

