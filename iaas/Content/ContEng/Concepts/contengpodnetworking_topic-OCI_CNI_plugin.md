Updated 2025-02-12
# Using the OCI VCN-Native Pod Networking CNI plugin for pod networking
_Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine (OKE)._
The OCI VCN-Native Pod Networking CNI plugin provides IP addresses to pods from a VCN's CIDR block. The OCI VCN-Native Pod Networking CNI plugin enables other resources within the same subnet (or a different subnet) to communicate directly with pods in a Kubernetes cluster. Pod IP addresses are directly routable from other VCNs connected (peered) to that VCN, and from on-premise networks.
Since pods are directly routable, you can use 'native' VCN functionality to:
  * Control access to and from pods using security rules defined as part of network security groups (recommended) or security lists. The security rules apply to all pods in all the worker nodes connected to the pod subnet specified for a node pool. See [Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) and [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).
  * Observe the traffic to, from, and between pods using VCN flow logs for troubleshooting and compliance auditing purposes. See [VCN Flow Logs](https://docs.oracle.com/iaas/Content/Network/Concepts/vcn-flow-logs.htm).
  * Route incoming requests to pods based on routing policies specified by routing rules and route tables. See [VCN Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).


When using the OCI VCN-Native Pod Networking CNI plugin, worker nodes are connected to two subnets specified for the node pool:
  * **Worker Node Subnet:** The worker node subnet supports communication between processes running on the cluster control plane (such as kube-apiserver, kube-controller-manager, kube-scheduler) and processes running on the worker node (such as kubelet, kube-proxy). The worker node subnet can be private or public, and can be a regional subnet (recommended) or on different AD-specific subnets (one in each availability domain in the region). 
  * **Pod Subnet:** The pod subnet supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be private, and must be a regional subnet. The pod subnet enables pods to communicate with other pods on the same worker node, with pods on other worker nodes, with OCI services (through a service gateway) and with the internet (through a NAT gateway). You specify a single pod subnet for all the pods running on worker nodes in a node pool. You can specify the same pod subnet, or different pod subnets, for different node pools in a cluster. You can specify the same pod subnet for node pools in different clusters.


The worker node subnet and the pod subnet must be in the same VCN. In some situations, the worker node subnet and the pod subnet can be the same subnet (see [Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes)). If the worker node subnet and the pod subnet are the same subnet, Oracle recommends defining security rules in network security groups (rather than in security lists) to route network traffic to worker nodes and pods. The worker node subnet and the pod subnet are in addition to the Kubernetes API endpoint subnet and any load balancer subnets defined for the cluster. 
When using the OCI VCN-Native Pod Networking CNI plugin, a minimum of two VNICs are attached to each worker node. The first VNIC is connected to the worker node subnet. The second VNIC is connected to the pod subnet. By default, 31 IP addresses are assigned to the VNIC for use by pods running on the worker node. To avoid running out of IP addresses, the IP addresses are pre-allocated in the pod subnet before pods are created in the cluster.
If the shape you select for the node pool supports more than two VNICs, the additional VNICs can be connected to the pod subnet to provide further IP addresses to support more pods.
You can specify the maximum number of pods that you want to run on a single worker node in a node pool, up to a limit of 110. The limit of 110 is imposed by Kubernetes. If you want more than 31 pods on a single worker node, the shape you specify for the node pool must support three or more VNICs (one VNIC to connect to the worker node subnet, and at least two VNICs to connect to the pod subnet). See [Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes). 
If you want to conserve the pod subnet's address space, lower the maximum number of pods you want to run on a single worker node, and thereby reduce the number of IP addresses that are pre-allocated in the pod subnet.
Note the following when using the OCI VCN-Native Pod Networking CNI plugin:
  * You can use the OCI VCN-Native Pod Networking CNI plugin with both virtual node pools and managed node pools.
  * You can use the OCI VCN-Native Pod Networking CNI plugin with self-managed nodes, provided the cluster's control plane nodes are running Kubernetes version 1.27.10 (or later). For more information, see [Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm#contengworkingwithselfmanagednodes "Find out how to set up and use self-managed nodes with Kubernetes Engine.").
  * You can only use the OCI VCN-Native Pod Networking CNI plugin with clusters running Kubernetes 1.22 or later (see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).")). For more information, see [Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm#podnetworking "Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
  * If you are using the OCI VCN-Native Pod Networking CNI plugin and you want to specify an OKE image as the base image for worker nodes, do not select an OKE image released before June 2022.
  * If you are using the OCI VCN-Native Pod Networking CNI plugin and you want to route traffic from an on-premise network to a pod, note that the pod's IP address is not persistent if the pod is recreated. For example, an Nginx pod might initially have 10.0.0.5 as its IP address, but if the pod is deleted and recreated, the pod might have a different IP address (such as 10.0.0.8).
  * Service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).


## Security Rules for Worker Nodes and Pods 🔗 
When using the OCI VCN-Native Pod Networking CNI plugin for pod networking, certain security rules are required for the pod subnet and the worker node subnet. See [Security Rules for Pod Subnets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__section_rules_for_pod_subnets).
## Maximum Number of VNICs and Pods Supported by Different Shapes 🔗 
The maximum number of VNICs (and therefore the maximum number of pods) for worker nodes in a node pool depends on the shape you select for the node pool.
To find out the maximum number of VNICs for a particular shape, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
To calculate the maximum number of pods in a node pool of a particular shape, use the following equation:
```
Maximum number of Pods per node = MIN( (Number of VNICs - 1) * 31 ), 110)
```

## Additional IAM policy to access resources with IPv6 addresses
To use the OCI VCN-Native Pod Networking CNI plugin where a cluster's related resources (such as Kubernetes API endpoint, load balancer, and worker nodes) have IPv6 addresses, include a policy statement similar to the following in an IAM policy:
Copy
```
Allow any-user to use ipv6s in compartment <compartment-ocid-of-network-resources> where all { request.principal.id = '<cluster-ocid>' }
```

## Additional IAM Policy when a Cluster and its Related Resources are in Different Compartments
To use the OCI VCN-Native Pod Networking CNI plugin in the uncommon scenario where a cluster's related resources (such as node pools, VCN, and VCN resources) are in a different compartment to the cluster itself, you must include policy statements similar to the following in an IAM policy:
```
Allow any-user to manage instances in tenancy where all { request.principal.type = 'cluster' }
```
```
Allow any-user to use private-ips in tenancy where all { request.principal.type = 'cluster' }
```
```
Allow any-user to use network-security-groups in tenancy where all { request.principal.type = 'cluster' }
```

If you consider these policy statements to be too permissive, you can restrict the permissions to explicitly specify the compartment to which the related resources belong, and/or to explicitly specify the cluster that has related resources in a different compartment. For example:
```
Allow any-user to manage instances in compartment <compartment-ocid-of-nodepool> where all { request.principal.id = '<cluster-ocid>' }
```
```
Allow any-user to use private-ips in compartment <compartment-ocid-of-network-resources> where all { request.principal.id = '<cluster-ocid>' }
```
```
Allow any-user to use network-security-groups in compartment <compartment-ocid-of-network-resources> where all { request.principal.id = '<cluster-ocid>' }
```

where:
  * `<compartment-ocid-of-nodepool>` is the OCID of the compartment to which nodepools and compute instances belong.
  * `<compartment-ocid-of-network-resources>` is the OCID of the compartment to which the VCN and subnets belong.


## Updating the OCI VCN-Native Pod Networking CNI plugin 🔗 
When you specify VCN-native pod networking as a cluster's network type, the cluster and its node pools initially use the latest version of the OCI VCN-Native Pod Networking CNI plugin.
Updates to the OCI VCN-Native Pod Networking CNI plugin are released periodically. You can specify that you want Oracle to deploy the updates on the cluster automatically (the default). Alternatively, you can specify that you want to choose the version to deploy. If you decide to choose the version, you are taking responsibility for keeping the add-on up-to-date. See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
Regardless of whether you or Oracle is responsible for deploying updates to the OCI VCN-Native Pod Networking CNI plugin, the updates are only applied when worker nodes are next rebooted. To determine whether updates have been deployed and are waiting to be applied, inspect the `vcn-native-ip-cni` Daemonset logs by entering:
```
kubectl logs -n kube-system -l app=vcn-native-ip-cni --prefix | grep "reboot required"
```

Interpret the response to the command as follows:
  * If there is output in response to the command, updates to the OCI VCN-Native Pod Networking CNI plugin have been deployed to the worker nodes associated with the pods shown in the response, but the updates are waiting to be applied. The updates will be applied when the worker nodes are next rebooted.
  * If there is no output in response to the command, no updates to the OCI VCN-Native Pod Networking CNI plugin are waiting to be applied.


Was this article helpful?
YesNo

