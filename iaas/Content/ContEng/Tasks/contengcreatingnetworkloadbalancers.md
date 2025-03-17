Updated 2024-11-18
# Provisioning OCI Network Load Balancers for Kubernetes Services of Type LoadBalancer
_Find out how to provision an OCI network load balancer for a Kubernetes service of type LoadBalancer using Kubernetes Engine (OKE)._
This section describes how to provision an OCI network load balancer for a Kubernetes service of type LoadBalancer.
An Oracle Cloud Infrastructure network load balancer is a non-proxy load balancing solution that performs pass-through load balancing of OSI layer 3 and layer 4 (TCP/UDP/ICMP) workloads. It offers an elastically scalable regional virtual IP (VIP) address that can scale up or down based on client traffic with no minimum or maximum bandwidth configuration requirement. It also provides the benefits of flow high availability, source and destination IP address, and port preservation.
For more information about Oracle Cloud Infrastructure network load balancers, see [Overview of Flexible Network Load Balancer](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/overview.htm).
Provisioning an OCI network load balancer for a Kubernetes service of type LoadBalancer enables you to: 
  * load balance traffic with a high throughput and low latency
  * preserve source and destination IP addresses and ports
  * handle TCP and UDP traffic


Note that when Kubernetes Engine provisions an OCI network load balancer for a Kubernetes service of type LoadBalancer, security rules to allow inbound and outbound traffic to and from the network load balancer's subnet are not created automatically by default. You must define appropriate security rules to allow inbound and outbound traffic to and from the load balancer's or network load balancer's subnet. See [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).
Use OCI network load balancer metrics to monitor the health of an OCI network load balancer provisioned for a Kubernetes service of type LoadBalancer (see [Network Load Balancer Metrics](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/Metrics/metrics.htm)).
## Specifying the Annotation for an OCI Network Load Balancer  🔗 
To provision a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
```
oci.oraclecloud.com/load-balancer-type: "nlb"
```

For example:```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "nlb"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that `lb` is the default value of the `oci.oraclecloud.com/load-balancer-type` annotation. If you do not explicitly include the annotation in the service definition, the default value of the annotation is used and a load balancer (rather than a network load balancer) is provisioned.
## Terminating Requests at the Receiving Node 🔗 
When provisioning a network load balancer for a Kubernetes service of type LoadBalancer, you can specify that requests terminate at the client IP address specified in the headers of IP packets, rather than being proxied to other worker nodes in the cluster. 
By default, requests are proxied to other worker nodes in the cluster.
Specifying that requests terminate at the client IP address (rather than being proxied) can improve performance in very large clusters with thousands of worker nodes by eliminating traffic between worker nodes. Specifying that requests terminate at the client IP address can also simplify implementation and remove potential security concerns by enabling you to set up security rules (in a network security group (recommended) and/or a security list) for the worker nodes in the cluster that only allow ingress traffic from the network load balancer's CIDR block.
To terminate requests at the client IP address, add the following setting in the spec section of the manifest file:
```
externalTrafficPolicy: Local
```

To proxy requests to other worker nodes in the cluster, add the following setting in the spec section of the manifest file:
```
externalTrafficPolicy: Cluster
```

Note that `Cluster` is the default value of the `externalTrafficPolicy` setting. If you do not explicitly include the setting in the service definition, the default value of the setting is used. 
Also note that if `externalTrafficPolicy` is set to `Cluster`, client IP addresses are not preserved regardless of the value of the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation. Requests fail with an error if `externalTrafficPolicy` is set to `Cluster` and the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation is explicitly set to either `true` or `false`. See [Preserving The Client IP Address](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic_Preserving_client_IP).
To terminate requests at the client IP address, you must also have set up the following security rules:
  * You must have set up a security rule (in a network security group (recommended) and/or a security list) for the worker nodes in the cluster to allow ingress traffic from the CIDR block where the client connections are made, to all node ports (`30000 to 32767`). If the application is exposed to the Internet, set the security rule's **Source** CIDR block to 0.0.0.0/0. Alternatively, set the security rule's **Source** CIDR block to a specific CIDR block (for example, if the client connections come from a specific subnet).
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or subnet CIDR | ALL/30000-32767 | Allow worker nodes to receive connections through OCI Network Load Balancer.  
  * You must have set up the ingress and egress security rules for the network load balancer, as described in [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).


For example, here is a Kubernetes service definition to terminate requests at the client IP address (rather than being proxied):
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "nlb"
  oci-network-load-balancer.oraclecloud.com/oci-network-security-groups: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....vdfw"
spec:
 type: LoadBalancer
 externalTrafficPolicy: Local
 ports:
 - port: 80
 selector:
  app: nginx
```

## Preserving The Client IP Address 🔗 
When provisioning a network load balancer for a Kubernetes service of type LoadBalancer, you can specify whether to preserve, or prevent the preservation of, the client IP address in the headers of IP packets. 
You only have the option to preserve client IP addresses when requests are terminated at the client IP addresses specified in the IP packet headers. That is, when the `externalTrafficPolicy` setting is set to `Local`. If `externalTrafficPolicy` is set to `Cluster`, client IP addresses are not preserved. See [Terminating Requests at the Receiving Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic-Preserve_source_destination).
To prevent the preservation of client IP addresses, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/is-preserve-source: "false"
```

To preserve the client IP address, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/is-preserve-source: "true"
```

Note that `true` is the default value of the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation. If you do not explicitly include the annotation in the service definition, the default value of the annotation is used.
Also note that if `externalTrafficPolicy` is set to `Cluster`, client IP addresses are not preserved regardless of the value of the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation. Requests fail with an error if `externalTrafficPolicy` is set to `Cluster` and the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation is explicitly set to either `true` or `false`. Therefore do not add the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation if `externalTrafficPolicy` is set to `Cluster`.
You can preserve client IP addresses when using managed node pools, but not when using virtual node pools.
To preserve the client IP address, you must also have set up the following security rules:
  * You must have set up a security rule (in a network security group (recommended) and/or a security list) for the worker nodes in the cluster to allow ingress traffic from the CIDR block where the client connections are made, to all node ports (`30000 to 32767`). If the application is exposed to the Internet, set the security rule's **Source** CIDR block to 0.0.0.0/0. Alternatively, set the security rule's **Source** CIDR block to a specific CIDR block (for example, if the client connections come from a specific subnet).
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or subnet CIDR | ALL/30000-32767 | Allow worker nodes to receive connections through OCI Network Load Balancer.  
  * You must have set up the ingress and egress security rules for the network load balancer, as described in [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).


For example, here is a Kubernetes service definition that prevents the preservation of the client IP address:
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "nlb"
  oci-network-load-balancer.oraclecloud.com/oci-network-security-groups: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....vdfw"
  oci-network-load-balancer.oraclecloud.com/is-preserve-source: "false"
spec:
 type: LoadBalancer
 externalTrafficPolicy: Local
 ports:
 - port: 80
 selector:
  app: nginx
```

## Exposing TCP and UDP Applications 🔗 
When Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, you can define the type of traffic accepted by the listener by specifying the protocol on which the listener accepts connection requests.
Note that if you don't explicitly specify a protocol, "TCP" is used as the default value.
To explicitly specify the listener protocol when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following setting in the spec section of the manifest file:
Copy
```
protocol: <value>
```

where `<value>` is the protocol that defines the type of traffic accepted by the listener. For example, "UDP". Valid protocols include "UDP" and "TCP". 
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "nlb"
spec:
 type: LoadBalancer
 ports:
 - port: 80
  protocol: UDP
 selector:
  app: nginx
```

## Specifying the Backend Set Policy 🔗 
When Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, you can define a policy for the backend set to specify how to distribute incoming traffic to the backend servers. 
For more information, see [Specifying Backend Set Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_backend_set_policy).
## Specifying Security List Management Options When Provisioning an OCI Network Load Balancer 🔗 
**Note**
You might encounter scalability and other issues if you use the Kubernetes security list management feature in complex deployments, and with tools like Terraform. For these reasons, Oracle does not recommend using the Kubernetes security list management feature in production environments.
Also note that the ability to use security lists to manage security rules will be deprecated in a future release. For this reason, Oracle recommends the use of network security groups (NSGs) and the `oci.oraclecloud.com/security-rule-management-mode` annotation (see [Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options)).
You can use the security list management feature to configure how security list rules are managed for an Oracle Cloud Infrastructure network load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer. This feature is useful if you are new to Kubernetes, or for basic deployments.
To specify how the Kubernetes security list management feature manages security lists when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/security-list-management-mode: <value>
```

where `<value>` is one of:
  * `"None"`: (default, and recommended) No security list management is enabled. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. Additionally, you have to set up security rules to allow inbound traffic to network load balancers (see [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers)).
  * `"All"`: All required security list rules for network load balancer services are managed.
  * `"Frontend"`: Only security list rules for ingress to network load balancer services are managed. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges.


Oracle recommends that you explicitly set `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` to `None`.
In clusters with managed nodes, if you don't explicitly specify a management mode, security list management is not enabled (equivalent to `"None"`). In clusters with virtual nodes, security list management is never enabled and you always have to manually configure security rules (equivalent to `"None"`).
Note that there are limits to the number of ingress and egress rules that are allowed in a security list (see [Security List Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#sec_list_limits)). If the number of ingress or egress rules exceeds the limit, and `<value>` is set to `"All"` or `"Frontend"`, creating or updating the load balancer fails.
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "nlb"
  oci-network-load-balancer.oraclecloud.com/security-list-management-mode: "Frontend"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Was this article helpful?
YesNo

