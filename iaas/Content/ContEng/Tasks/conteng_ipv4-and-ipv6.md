Updated 2025-02-12
# Enabling Clusters for IPv4 and IPv6
_Find out what you need to know about IPv4 and IPv6 addresses when using Kubernetes Engine (OKE)._
When you use Kubernetes Engine to create Kubernetes clusters (version 1.29 or later), you specify which IP address family to use when allocating IP addresses to enable communication with the cluster and within the cluster. You can specify:
  * just the IPv4 address family
  * both the IPv4 and the IPv6 address family


## About IPv4 🔗 
The IPv4 internet protocol is a standard for identifying devices on a network by assigning a unique IP address to each device. IPv4 has an address space of 32 bits (232), which provides more than 4.2 billion unique IP addresses. An IPv4 address is a 32 bit value, commonly formatted as four segments of 8 bits (known as octets) separated by a dot, where each segment is a decimal value between 0 and 255. For example, 203.0.113.2. 
An IPv4 address has two parts, a network part (or 'prefix') to identify a network, and a host part to identify an individual device on that network. How much of the IPv4 address is available for use as the network part is indicated by a CIDR suffix appended to the IPv4 address after a slash character. For example, /24 indicates that the first 24 bits (the first three segments of eight bits) of the IPv4 address form the network part of the address, leaving the remaining 8 bits (the final segment) available to form the host part of the address. 
Taking 203.0.113.2/24 as an example:
  * 203.0.113 is the network part (or 'prefix') of the address
  * .2 is the host part of the address
  * 203.0.113.2 is the address of an individual device
  * 203.0.113.0/24 is a 'CIDR block',which represents the entire range of addresses that can share the same network prefix. In this case, the CIDR block includes all the IP addresses between 203.0.113.0 and 203.0.113.255


The proliferation of internet-connected devices is exhausting the pool of available IPv4 addresses, and is one reason for the wide-scale adoption of IPv6. 
## About IPv6 🔗 
IPv6 is the successor to IPv4 and has a much larger address space of 128 bits (2128), which provides 3.4 x 1038 unique IP addresses. An IPv6 address is a 128 bit value, formatted as eight groups of 16 bits (known as hectets), separated by colons, where each group is a hexadecimal value between 0000 and ffff. For example, 2001:0db8:0123:1111:abcd:ef01:2345:6789. 
An IPv6 address has two parts, a network part (or 'prefix') to identify a network, and a host part to identify an individual device on that network. How much of the IPv6 address is available for use as the network part is indicated by a CIDR suffix appended to the IPv6 address after a slash character. For example, /64 indicates that the first 64 bits (the first four groups of 16 bits) form the network part of the address, leaving the remaining 64 bits (the second four groups of 16 bits) available to form the host part of the address. 
Taking 2001:0db8:0123:1111:abcd:ef01:2345:6789/64 as an example:
  * 2001:0db8:0123:1111 is the network part (or 'prefix') of the address
  * abcd:ef01:2345:6789 is the host part of the address
  * 2001:0db8:0123:1111:abcd:ef01:2345:6789 is the address of an individual device
  * 2001:0db8:0123:1111:0000:0000:0000:0000/64 is a 'CIDR block', which represents the entire range of addresses that can share the same network prefix. In this case, the CIDR block includes all the IP addresses between 2001:0db8:0123:1111:0000:0000:0000:0000 and 2001:0db8:0123:1111:ffff:ffff:ffff:ffff


The IPv6 address space is organized into categories, such as the unicast category The unicast category includes:
  * Global unicast addresses (GUAs), which are globally unique and internet routable.
  * Unique-local unicast addresses (ULAs), which are for local communication within a network.


As well as having a much larger address space that resolves the issue of IPv4 address exhaustion, IPv6 has other benefits over IPv4, including:
  * IPv6 is more secure than IPv4, with built-in support for data encryption and authentication.
  * IPv6 offers more efficient routing than IPv4.
  * IPv6 offers faster data transmission speeds than IPv4.


## OCI Support for IPv6 🔗 
Oracle Cloud Infrastructure supports both IPv4 addressing and IPv6 addressing. 
OCI VCNs support IPv4-only addressing, and also 'dual stack' IPv4 and IPv6 addressing. Every VCN always has at least one private IPv4 CIDR, and you can enable IPv6 during VCN creation. You can also add an IPv6 prefix to an IPv4-only VCN while enabling IPv6. When creating a subnet of an IPv6-enabled VCN, you can enable the subnet to have:
  * IPv4 addresses only (referred to as a single stack IPv4 subnet)
  * both IPv4 and IPv6 addresses (referred to as a dual stack IPv4/IPv6 subnet)
  * IPv6 addresses only (referred to as a single stack IPv6 subnet)


An IPv6-enabled VCN can have a mix of single stack IPv4 subnets, single stack IPv6 subnets, and dual stack IPv4/IPv6 subnets. 
For more information about IPv6 and OCI in general, see [IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
## Kubernetes support for IPv4 and IPv6 🔗 
Kubernetes provides support for single-stack IPv4 networking, single-stack IPv6 networking, or dual stack networking.
For more information about IPv4 and IPv6 support in Kubernetes, see [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/) in the Kubernetes documentation. 
## Kubernetes Engine support for IPv4 and IPv6 🔗 
In earlier versions of Kubernetes Engine (supporting clusters running Kubernetes versions prior to version 1.29), you can only create clusters enabled for IPv4. In an IPv4-enabled cluster, the cluster's Kubernetes API endpoint, load balancer, worker nodes, and pods and services running in the cluster, are assigned IPv4 addresses. Communication with the cluster, and within the cluster, uses IPv4 addressing only (any assigned IPv6 addresses are ignored).
In versions of Kubernetes Engine supporting clusters running Kubernetes versions 1.29 or later, you can create:
  * IPv4 single stack clusters, enabled for IPv4 only. 
  * IPv4/IPv6 dual stack clusters, enabled for both IPv4 and IPv6 (sometimes referred to simply as dual stack clusters).


When you create a cluster, you specify the cluster's IP address family:
  * If you specify just IPv4 as the cluster's IP address family, you create an IPv4 single stack cluster.
  * If you specify both IPv4 and IPv6 as the cluster's IP address families, you create an IPv4/IPv6 dual stack cluster.


When creating an IPv4 single stack cluster, you can specify an IPv4-enabled VCN for the cluster, or you can specify a VCN that is enabled for both IPv4 and IPv6. 
When creating an IPv4/IPv6 dual stack cluster, the VCN you specify for the cluster must be enabled for both IPv4 and IPv6. In addition, to create an IPv4/IPv6 dual stack cluster:
  * Control plane nodes and worker nodes must be running Kubernetes version 1.29 or later.
  * Worker nodes must be based on an OKE image with a build number of 754 or greater.
  * Any dual stack IPv4/IPv6 subnets you specify for the Kubernetes API endpoint, load balancer, worker nodes, and pod communication must be public subnets.
  * The cluster must be a new cluster, or a "VCN-native cluster". That is, a cluster that has its Kubernetes API endpoint integrated into your own VCN (see [Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#migrating_clusters_to_native_vcns "Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine \(OKE\).")). Clusters with Kubernetes API endpoints that are not integrated into your own VCN cannot be IPv4/IPv6 dual stack clusters.


## Creating IPv4 single stack clusters and IPv4/IPv6 dual stack clusters 🔗 
When you create a cluster, you specify the cluster's IP address family as either just IPv4, or as both IPv4 and IPv6.
You can create IPv4 single stack clusters and IPv4/IPv6 dual stack clusters using:
  * **the Console:** Use the [Custom Create workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create the cluster. The cluster's IP address families are inferred from the selections you make.
  * **the CLI:** Use the [oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html) command to create the cluster and include the `--ip-families` parameter to explicitly specify the cluster's IP address families, in the format:
Copy
```
 oci ce cluster create --compartment-id <compartment-ocid> --kubernetes-version <kubernetes-version> --name <cluster-name> --vcn-id <vcn-ocid> --ip-families='["<ip-family-1>", "<ip-family-2>"]' [OPTIONS]
```

For example:
Command
CopyTry It
```
oci ce cluster create --compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q --kubernetes-version v1.31.1 --name Finance-Cluster --vcn-id ocid1.vcn.oc1.iad.aaaaaae___yja --ip-families='["IPv4", "IPv6"]'
```

  * **the API:** Run the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create the cluster and specify the cluster's IP address families.


## Cluster-related resources and IP addresses 🔗 
A cluster's Kubernetes API endpoint, worker nodes, and pod communication inherit the IP address family specified for the cluster. So in an IPv4/IPv6 dual stack cluster, the Kubernetes API endpoint, worker nodes, and pod communication all use both the IPv4 address family and the IPv6 address family.
The subnets you specify for the cluster's Kubernetes API endpoint, for its worker nodes, and for pod communication, must be compatible with the cluster's IP address family as follows:
  * An IPv4 single stack cluster is compatible both with an IPv4 single stack subnet, and with an IPv4/IPv6 dual stack subnet. So you can specify an IPv4 single stack subnet, or an IPv4/IPv6 dual stack subnet, for the cluster's Kubernetes API endpoint, for its worker nodes, and for pod communication.
  * An IPv4/IPv6 dual stack cluster is only compatible with an IPv4/IPv6 dual stack subnet. So you must specify an IPv4/IPv6 dual stack public subnet for the cluster's Kubernetes API endpoint, for its worker nodes, and for pod communication. You cannot specify an IPv4 single stack subnet for an IPv4/IPv6 dual stack cluster's Kubernetes API endpoint, for its worker nodes, and for pod communication.


Having specified subnets for the cluster's Kubernetes API endpoint, worker nodes, and pod communication that are compatible with the IP address family of the cluster:
  * If you select a single stack IPv4 subnet for the resource, the resource is only given an IPv4 address.
  * If you select a dual stack IPv4/IPv6 subnet for the resource, the resource is given both an IPv4 address and an IPv6 address.


Note the following:
  * You can specify the IP address family of a cluster's load balancer independently of the cluster's IP address family. For example, you can create an IPv4/IPv6 dual stack load balancer for an IPv4 single stack cluster (see [Specifying IP Address Families for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_IPAddressfamily)). 
  * Any dual stack IPv4/IPv6 subnet you specify for the Kubernetes API endpoint, load balancer, worker nodes, and pod communication must be a public subnet. The public subnet requires a NAT gateway for IPv4 addressing, and an internet gateway for IPv6 addressing.
  * If multiple IPv6 prefixes are assigned to a dual stack IPv4/IPv6 subnet Kubernetes Engine uses the first IPv6 prefix defined for the subnet.
  * Kubernetes Engine supports both GUA and ULA IPv6 prefixes.


## Additional IAM policy to access resources with IPv6 addresses 🔗 
To enable a cluster to use IPv6 addresses to access resources, include a policy statement similar to the following in an IAM policy:
Copy
```
Allow any-user to use ipv6s in compartment <compartment-ocid-of-network-resources> where all { request.principal.id = '<cluster-ocid>' }
```

## Kubernetes API endpoint IP addresses 🔗 
A cluster's Kubernetes API endpoint inherits the IP address family specified for the cluster. So in an IPv4/IPv6 dual stack cluster, the Kubernetes API endpoint uses both the IPv4 address family and the IPv6 address family.
Therefore, specify a subnet for the Kubernetes API endpoint that is compatible with the IP address family of the cluster:
  * When you specify a subnet for the Kubernetes API endpoint that is configured to support IPv4 addressing (either an IPv4 single stack subnet, or an IPv4/IPv6 dual stack subnet) an available IPv4 address in the subnet is automatically assigned to the Kubernetes API endpoint as a **private** address.
  * To assign a **public** IPv4 address to the Kubernetes API endpoint, you must specify a **public** subnet for the Kubernetes API endpoint that is configured to support IPv4 addressing (either an IPv4 single stack subnet, or an IPv4/IPv6 dual stack subnet). Having specified such a public subnet, if you specify that you want to assign a public IPv4 address, an available IPv4 address in the subnet is automatically assigned to the Kubernetes API endpoint as a public address. 
  * To assign both an IPv4 address and an IPv6 address to the Kubernetes API endpoint, you must specify an IPv4/IPv6 dual stack public subnet for the Kubernetes API endpoint. An available IPv4 address and IPv6 address in the subnet are automatically assigned to the Kubernetes API endpoint.


Note that the address family of the subnet you specify for the Kubernetes API endpoint must be compatible with the cluster's IP address family. An IPv4 single stack cluster is compatible with both an IPv4 single stack subnet and an IPv4/IPv6 dual stack subnet. An IPv4/IPv6 dual stack cluster is only compatible with an IPv4/IPv6 dual stack subnet.
## Load Balancer IP addresses 🔗 
By default, a cluster's load balancer inherits the IP address family specified for the cluster. So in an IPv4/IPv6 dual stack cluster, the load balancer uses both the IPv4 address family and the IPv6 address family.
Specify a subnet for the cluster's load balancer as follows:
  * To assign just an IPv4 address to the load balancer, specify an IPv4 single stack subnet or an IPv4/IPv6 dual stack subnet. An available IPv4 address in the subnet is automatically assigned to the load balancer.
  * To assign both an IPv4 address and an IPv6 address to the load balancer, specify an IPv4/IPv6 dual stack subnet. An available IPv4 address and IPv6 address in the subnet are automatically assigned to the load balancer.


Note that the address family of the subnet you specify for a load balancer need not be compatible with the cluster's IP address family. You can create an IPv4/IPv6 dual stack load balancer for an IPv4 single stack cluster (see [Specifying IP Address Families for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_IPAddressfamily)). 
For more information, see [Specifying IP Address Families for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_IPAddressfamily).
## Worker node IP addresses 🔗 
A cluster's node pools and worker nodes inherit the IP address family specified for the cluster. So in an IPv4/IPv6 dual stack cluster, a node pool and its worker nodes use both the IPv4 address family and the IPv6 address family.
Therefore, specify a subnet for the worker nodes that is compatible with the IP address family of the cluster:
  * To assign just IPv4 addresses to worker nodes, specify an IPv4 single stack subnet or an IPv4/IPv6 dual stack subnet for the node pool. Available IPv4 addresses in the subnet are automatically assigned to the worker nodes.
  * To assign both IPv4 addresses and IPv6 addresses to the worker nodes, specify an IPv4/IPv6 dual stack subnet for the node pool. Available IPv4 and IPv6 addresses in the subnet are automatically assigned to the worker nodes.


Note that the address family of the subnet you specify for worker nodes must be compatible with the cluster's IP address family. An IPv4 single stack cluster is compatible with both an IPv4 single stack subnet and an IPv4/IPv6 dual stack subnet. An IPv4/IPv6 dual stack cluster is only compatible with an IPv4/IPv6 dual stack subnet.
## Pod communication IP addresses 🔗 
A cluster pod's use the IP address family specified for the cluster for pod communication. So in an IPv4/IPv6 dual stack cluster, pod communication uses both the IPv4 address family and the IPv6 address family. 
Therefore, specify a subnet for pod communication that is compatible with the IP address family of the cluster:
  * If you want the pods to have and use just IPv4 addresses, specify an IPv4 single stack subnet or an IPv4/IPv6 dual stack subnet. Available IPv4 addresses in the subnet are automatically assigned to the pods.
  * If you want the pods to have and use both IPv4 and IPv6 addresses, specify an IPv4/IPv6 dual stack subnet. Available IPv4 and IPv6 addresses in the subnet are automatically assigned to the pods.


Note that the address family of the subnet you specify for pod communication must be compatible with the cluster's IP address family. An IPv4 single stack cluster is compatible with both an IPv4 single stack subnet and an IPv4/IPv6 dual stack subnet. An IPv4/IPv6 dual stack cluster is only compatible with an IPv4/IPv6 dual stack subnet.
## Deploying services on IPv4-enabled clusters and IPv6-enabled clusters 🔗 
When you deploy a service on a Kubernetes cluster, the service is allocated an IP address (and address family) from the cluster's service cluster IP range. A service cluster IP range is a range of IP addresses from which virtual IP addresses (ClusterIPs) can be assigned to services, enabling the services to be accessed within the cluster. A Kubernetes cluster can have:
  * just an IPv4 service cluster IP range
  * both an IPv4 service cluster IP range and an IPv6 service cluster IP range


Kubernetes Engine creates service cluster IP ranges for a cluster according to the IP address families that you specified when you defined the cluster:
  * If you specified IPv4 as the cluster's IP family, Kubernetes Engine creates an IPv4 service cluster IP range for the cluster.
  * If you specified both IPv4 and IPv6 as the cluster's IP families, Kubernetes Engine creates both an IPv4 service cluster IP range and an IPv6 service cluster IP range for the cluster. 


By default, new services deployed on a cluster are allocated an IP address from the first service cluster IP range specified for the cluster. However, you can use the `spec.ipFamilyPolicy` field in the service manifest to specify which service cluster IP range is used (IPv4 or IPv6):
  * Set `ipFamilyPolicy: SingleStack` to allocate IP addresses for the service from the first service cluster IP range specified for the cluster. If the cluster has both an IPv4 service cluster IP range and an IPv6 service cluster IP range, set the `spec.ipFamilies` field in the service manifest if you want to explicitly specify which service cluster IP range to use.
  * Set `ipFamilyPolicy: PreferDualStack` to allocate both IPv4 and IPv6 addresses to the service if the service is deployed on a cluster with both an IPv4 and an IPv6 service cluster IP range. Set the `spec.ipFamilies` field in the service manifest if you want to explicitly specify which of the two IP addresses to use as the service's primary IP address.
Otherwise, if the service is deployed on a cluster that only has one service cluster IP range, an IP address is allocated to the service from that service cluster IP range.
  * Set `ipFamilyPolicy: RequireDualStack` to allocate both IPv4 and IPv6 addresses to the service if the service is deployed on a cluster with both an IPv4 and an IPv6 service cluster IP range. Set the `spec.ipFamilies` field in the service manifest if you want to explicitly specify which of the two IP addresses to use as the service's primary IP address. 
Otherwise, if the cluster only has one service cluster IP range, do not deploy the service.


The table shows the interaction between the cluster's IP address family, the settings of `spec.ipFamilyPolicy` and `spec.ipFamilies` in the service manifest, and the IP address family from which IP addresses are allocated to the service. Note that only valid combinations are shown.
Cluster's IP Address Family | `ipFamilyPolicy` set to: | `ipFamilies` set to: | Service allocated IP addresses from this IP address family  
---|---|---|---  
IPv4 | `SingleStack` | `IPv4` | IPv4  
IPv4 and IPv6 | `SingleStack` | `IPv4` | IPv4  
IPv4 and IPv6 | `SingleStack` | `IPv6` | IPv6  
IPv4 | `PreferDualStack` | `IPv4` | IPv4  
IPv4 and IPv6 | `PreferDualStack` | `IPv4` | IPv4  
IPv4 and IPv6 | `PreferDualStack` | `IPv6` | IPv6  
IPv4 and IPv6 | `PreferDualStack` | `IPv4,IPv6` | IPv4(primary) and IPv6  
IPv4 and IPv6 | `PreferDualStack` | `IPv6,IPv4` | IPv6(primary) and IPv4  
IPv4 and IPv6 | `RequireDualStack` | `IPv4,IPv6` | IPv4(primary) and IPv6  
IPv4 and IPv6 | `RequireDualStack` | `IPv6,IPv4` | IPv6(primary) and IPv4   
Note that the kubernetes.default and kube-dns.kube-system services, which are automatically deployed on every cluster, are allocated IP addresses that match the cluster's IP family.
For more information about IPv4 and IPv6 support in Kubernetes, see [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/) in the Kubernetes documentation. 
Was this article helpful?
YesNo

