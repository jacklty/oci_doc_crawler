Updated 2024-07-23
# Setting Up the OCI Native Ingress Controller on a Kubernetes Cluster
_Find out how to set up the OCI native ingress controller to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster._
The OCI native ingress controller implements the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster. The OCI native ingress controller creates an OCI flexible load balancer to handle requests, and configures the OCI load balancer to route requests according to the rules defined in the ingress resource. If there are changes to the routing rules, or to other supporting resources, the OCI native ingress controller updates the load balancer configuration accordingly. The OCI native ingress controller runs as a single pod, on a randomly selected worker node in the cluster.
The OCI native ingress controller creates OCI load balancer resources as follows:
  * A load balancer for each `IngressClass` resource where you have specified the OCI native ingress controller as the controller.
  * A load balancer backend set for each unique Kubernetes service name and port number combination that you include in routing rules in `Ingress` resources in the cluster. 
  * A load balancer listener for each unique port that you include in routing rules in `Ingress` resources in the cluster. The OCI native ingress controller determines the protocol (HTTP, HTTPS, HTTP/2) for each listener based on the ingress backend configuration.


The OCI native ingress controller adds as backends to a backend set either the pods that serve as endpoints for the respective Kubernetes service name and port, or the worker nodes on which those pods can run, depending on the CNI plugin that the cluster uses for pod networking:
  * If the cluster uses the OCI VCN-Native Pod Networking CNI plugin for pod networking, the OCI native ingress controller adds the pods as backends.
  * If the cluster uses the flannel CNI plugin for pod networking, the OCI native ingress controller adds the worker nodes as backends. In this case, the OCI native ingress controller uses the `externalTrafficPolicy` setting in the service's manifest to determine which worker nodes to add to the backend set, as follows:
    * If `externalTrafficPolicy: Cluster`, the OCI native ingress controller adds to the backend set all the worker nodes in the cluster.
    * If `externalTrafficPolicy: Local`, the OCI native ingress controller adds to the backend set only those worker nodes on which the service's pods have been deployed.


The OCI native ingress controller creates OCI load balancer resources subject to the normal Load Balancer service limits regarding total number of IP addresses, backend sets, listeners, and backend servers. For more information, see [Limits on Load Balancing Resources](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#LimitsResources).
You can deploy the OCI native ingress controller on a Kubernetes cluster in either one or other of the following ways:
  * as a standalone program (see [Working with the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-standalone-top-level.htm#contengsettingupnativeingresscontroller-standalone-top-level "Find out how to set up the OCI native ingress controller as a standalone program, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster."))
  * as a cluster add-on (see [Working with the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-cluster-addon-top-level.htm#contengsettingupnativeingresscontroller-cluster-addon-top-level "Find out how to set up the OCI native ingress controller as a cluster add-on, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster."))


When using the OCI native ingress controller to load balance and route incoming traffic, note the following:
  * If you install the OCI native ingress controller as a standalone program, the cluster must be running Kubernetes version 1.26, or later. If you install the OCI native ingress controller as a cluster add-on, the cluster must be running Kubernetes version 1.28, or later.
  * The cluster must have load balancer subnet security rules configured.
  * The cluster can be using either the OCI VCN-Native Pod Networking CNI plugin or the flannel CNI plugin for pod networking. Note that if the cluster uses the flannel CNI plugin for pod networking, the OCI native ingress controller only supports backend services of `type: NodePort`, as specified in the service's manifest.
  * The use of instance principals to enable the OCI native ingress controller to access OCI services and resources is not supported in clusters with virtual nodes.
  * You can specify workload identity principals with enhanced clusters, but not with basic clusters.
  * If the OCI native ingress controller has already been deployed on a cluster as a standalone program, do not also deploy the OCI native ingress controller cluster add-on on the cluster .


Was this article helpful?
YesNo

