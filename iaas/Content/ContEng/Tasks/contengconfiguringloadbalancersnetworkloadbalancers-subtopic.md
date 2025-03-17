Updated 2025-02-12
# Configuring Load Balancers and Network Load Balancers
_Find out how to define the Oracle Cloud Infrastructure load balancers and network load balancers that Kubernetes Engine (OKE) provisions for a Kubernetes service of type LoadBalancer._
## Creating Internal Load Balancers 🔗 
You can create Oracle Cloud Infrastructure load balancers and network load balancers to control access to services running on a cluster:
  * When you create a cluster in the 'Custom Create' workflow you select an existing VCN that contains the network resources to be used by the new cluster. If you want to use a load balancer or network load balancer to control traffic into the VCN, you select an existing public or private subnet in that VCN to host it. 
  * When you create a cluster in the 'Quick Create' workflow, the VCN that's automatically created contains a public regional subnet to host a load balancer or network load balancer. If you want to host a load balancer or a network load balancer in a private subnet, you can add a private subnet to the VCN later.


Alternatively, you can define an internal Kubernetes service of type LoadBalancer (often referred to simply as an 'internal load balancer') in a cluster to enable other programs running in the same VCN as the cluster to access services in the cluster. An internal load balancer can be provisioned:
  * as a load balancer, or as a network load balancer
  * with a public IP address, or with a private IP address (assigned by the Load Balancer service or the Network Load Balancer service)
  * in a public subnet, or in a private subnet


A load balancer or network load balancer with a public IP address is referred to as public. A public load balancer or network load balancer can be hosted in a public subnet or in a private subnet.
A load balancer or network load balancer with a private IP address is referred to as private. A private load balancer or network load balancer can be hosted in a public subnet or in a private subnet.
By default, internal load balancers are provisioned with public IP addresses and hosted in public subnets.
For more information:
  * about Oracle Cloud Infrastructure public and private load balancers, see [Load Balancer Types](https://docs.oracle.com/iaas/Content/Balance/Concepts/load_balancer_types.htm).
  * about Oracle Cloud Infrastructure public and private network load balancers, see [Network Load Balancer Types](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#NetworkLoadBalancerTypes)


[Create an internal load balancer as an OCI load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To create an internal load balancer as an OCI load balancer with a private IP address, hosted on the subnet specified for load balancers when the cluster was created, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-internal: "true"
```

To create an internal load balancer as an OCI load balancer with a private IP address hosted, hosted on an alternative subnet to the one specified for load balancers when the cluster was created, add both the following annotations in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-internal: "true"
```

Copy
```
service.beta.kubernetes.io/oci-load-balancer-subnet1: "ocid1.subnet.oc1..aaaaaa....vdfw"
```

where `ocid1.subnet.oc1..aaaaaa....vdfw` is the OCID of the alternative subnet. The alternative subnet can be a private subnet or a public subnet.
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
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-internal: "true"
  service.beta.kubernetes.io/oci-load-balancer-subnet1: "ocid1.subnet.oc1..aaaaaa....vdfw"
spec:
 type: LoadBalancer
 ports:
 - port: 8100
 selector:
  app: nginx
```

[Create an internal network load balancer as an OCI network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To create an internal network load balancer as an OCI network load balancer with a private IP address, hosted on the subnet specified for load balancers when the cluster was created, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/internal: "true"
```

To create an internal network load balancer as an OCI network load balancer with a private IP address, hosted on an alternative subnet to the one specified for load balancers when the cluster was created, add both of the following annotations in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/internal: "true"
```

Copy
```
oci-network-load-balancer.oraclecloud.com/subnet: "ocid1.subnet.oc1..aaaaaa....vdfw"
```

where `ocid1.subnet.oc1..aaaaaa....vdfw` is the OCID of the private subnet. The alternative subnet can be a private subnet or a public subnet.
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
  oci-network-load-balancer.oraclecloud.com/internal: "true"
  oci-network-load-balancer.oraclecloud.com/subnet: "ocid1.subnet.oc1..aaaaaa....vdfw"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

## Specifying Reserved Public IP Addresses 🔗 
When a Kubernetes service of type LoadBalancer is deployed on a cluster, Kubernetes Engine creates an Oracle Cloud Infrastructure public load balancer or network load balancer to accept traffic into the cluster. By default, the Oracle Cloud Infrastructure public load balancer or network load balancer is assigned an ephemeral public IP address. However, an ephemeral public IP address is temporary, and only lasts for the lifetime of the public load balancer or network load balancer.
If you want the Oracle Cloud Infrastructure public load balancer or network load balancer that Kubernetes Engine creates to have the same public IP address deployment after deployment, you can assign it a reserved public IP address from the pool of reserved public IP addresses. For more information about creating and viewing reserved public IP addresses, see [Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
To assign a reserved public IP address to the Oracle Cloud Infrastructure public load balancer or network load balancer that Kubernetes Engine creates, add the `LoadBalancerIP` property in the spec section of the manifest file that defines the service of type LoadBalancer, and specify the reserved public IP address.
[Assign a reserved public IP address to a public load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
Example:
Copy
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
spec:
 loadBalancerIP: 144.25.97.173
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

[Assign a reserved public IP address to a public network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
Example:
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
 loadBalancerIP: 144.25.97.173
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note the following:
  * If you do set the `loadBalancerIP` property of the `LoadBalancer` service, you cannot later directly change the IP address of the Oracle Cloud Infrastructure public load balancer or network load balancer that Kubernetes Engine creates. If you do want to change the IP address, delete the `LoadBalancer` service, specify a different reserved public IP address in the manifest file, and deploy the `LoadBalancer` service again.
  * If you don't set the `loadBalancerIP` property of the `LoadBalancer` service, you cannot later directly switch the IP address of the Oracle Cloud Infrastructure public load balancer or network load balancer that Kubernetes Engine creates from an ephemeral IP address to a reserved public IP address. If you do want to switch the ephemeral IP address to a reserved public IP address, delete the service of type LoadBalancer, set the `loadBalancerIP` property to a reserved public IP address in the manifest file, and deploy the service of type LoadBalancer again.
  * You can delete the service of type LoadBalancer and release the reserved public IP address for other uses (for example, to assign it to another service of type LoadBalancer).
  * You cannot specify a reserved public IP address for a service of type LoadBalancer if the same IP address is already assigned to another resource (such as a compute instance, or another service of type LoadBalancer).
  * You cannot add the `loadBalancerIP` property to the manifest file for an internal load balancer service (that is, a manifest file that includes the `service.beta.kubernetes.io/oci-load-balancer-internal: "true"` or `oci-network-load-balancer.oraclecloud.com/internal: "true"` annotation).
  * By default, the reserved public IP address that you specify as the `loadBalancerIP` property of a service of type LoadBalancer in the manifest file is expected to be a resource in the same compartment as the cluster. If you want to specify a reserved public IP address in a different compartment: 
    * for public load balancers, add the following policy to the tenancy: 
Copy
```
ALLOW any-user to read public-ips in tenancy where request.principal.type = 'cluster'
ALLOW any-user to manage floating-ips in tenancy where request.principal.type = 'cluster'
```

    * for network load balancers, add the following policy to the tenancy:
Copy
```
ALLOW any-user to use private-ips in TENANCY where ALL {request.principal.type = 'cluster', request.principal.compartment.id = 'target.compartment.id'}
ALLOW any-user to manage public-ips in TENANCY where ALL {request.principal.type = 'cluster', request.principal.compartment.id = 'target.compartment.id'}
```



## Specifying Network Security Groups (recommended) 🔗 
Oracle Cloud Infrastructure network security groups (NSGs) enable you to control traffic into and out of resources, and between resources. The security rules defined for an NSG ensure that all the resources in that NSG have the same security posture. For more information, see [Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
You can use NSGs to control access to the Oracle Cloud Infrastructure load balancer or network load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer.
When using NSGs to control access, appropriate security rules must exist to allow inbound and outbound traffic to and from the load balancer's or network load balancer's subnet. See [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).
If you decide to use NSGs to control access to load balancers or network load balancers:
  * You can have the NSGs and security rules entirely managed for you by the oci-cloud-controller-manager (see [Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options)).
  * You can manage the NSGs and security rules yourself, and add the load balancer or network load balancer to the existing NSGs (as described in this section).
  * You can have the oci-cloud-controller-manager manage some security rules in one NSG, whilst you manage other security rules in a different NSG.


To control access using an NSG that you manage, you include annotations in the manifest file to specify the NSG to which you want to add the load balancer or network load balancer.
[Add a load balancer to an existing NSG](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To add the Oracle Cloud Infrastructure load balancer created by Kubernetes Engine to an NSG that you manage, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/oci-network-security-groups: "<nsg-ocid>"
```

where `<nsg-ocid>` is the OCID of an existing NSG.
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
  oci.oraclecloud.com/load-balancer-type: "lb"
  oci.oraclecloud.com/oci-network-security-groups: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....vdfw"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

[Add a network load balancer to an existing NSG](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To add the Oracle Cloud Infrastructure network load balancer created by Kubernetes Engine to an NSG that you manage, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/oci-network-security-groups: "<nsg-ocid>"
```

where `<nsg-ocid>` is the OCID of an existing NSG.
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
  oci-network-load-balancer.oraclecloud.com/oci-network-security-groups: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....vdfw"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note the following:
  * The NSG you specify must be in the same VCN as the Oracle Cloud Infrastructure load balancer or network load balancer.
  * If the NSG you specify belongs to a different compartment to the cluster, you must include a policy statement similar to the following in an IAM policy:```
ALLOW any-user to use network-security-groups in TENANCY where ALL { request.principal.type = 'cluster' }
```

If you consider this policy statement to be too permissive, you can restrict the permission to explicitly specify the compartment to which the NSG belongs, and/or to explicitly specify the cluster. For example:
```
Allow any-user to use network-security-groups in compartment <compartment-ocid> where all { request.principal.id = '<cluster-ocid>' }
```

  * You can specify up to five NSGs, in a comma-separated list, in the format:
Copy
```
oci.oraclecloud.com/oci-network-security-groups: "<nsg1-ocid>,<nsg2-ocid>,<nsg3-ocid>,<nsg4-ocid>,<nsg5-ocid>"
```

  * To remove a load balancer or network load balancer from an NSG, or to change the NSG that the load balancer or network load balancer is in, update the annotation and re-apply the manifest.
  * If you decide to control access to an Oracle Cloud Infrastructure load balancer or network load balancer using an NSG that you manage, Oracle recommends that you disable Kubernetes security list management by adding one of the following annotations in the metadata section of the manifest file for the load balancer or network load balancer respectively:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "None"
```

```
oci-network-load-balancer.oraclecloud.com/security-list-management-mode: "None"
```

Alternatively, you can add the following equivalent annotation:
```
oci.oraclecloud.com/security-rule-management-mode: "None" 
```

If you do follow the recommendation and add the annotation, Kubernetes security list management is not enabled. You have to set up NSGs with ingress and egress security rules for node pools and for the Kubernetes API endpoint (for more information, see [Security Rule Configuration in Network Security Groups and/or Security Lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).")). You also have to set up NSGs with ingress and egress security rules for the kube-proxy health port, for the health check port range, and for load balancers.


## Specifying Security Rule Management Options for Load Balancers and Network Load Balancers 🔗 
Security rules control access to the Oracle Cloud Infrastructure load balancers and network load balancers that are provisioned for Kubernetes services of type LoadBalancer. The security rules can be managed (that is, created, updated, and deleted) in the following ways:
  * **In a network security group, or NSG (recommended)** The security rules in an NSG apply to any Kubernetes resource added to the NSG. As such, NSGs can provide fine-grained access control to individual resources.
  * **In a security list.** The security rules in a security list apply to all the Kubernetes resources in a subnet. Security lists don't provide fine-grained access control to individual resources in the subnet.


For important information about how security rules work, and a general comparison of security lists and network security groups, see [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm#rules).
**Note**
If security rules are managed in security lists, security configuration and management can become complicated when the infrastructure is complex and when using tools like Terraform. Also note that the ability to use security lists to manage security rules will be deprecated in a future release. For these reasons, Oracle recommends the use of network security groups (NSGs) and the `oci.oraclecloud.com/security-rule-management-mode` annotation to manage security rules.
You can manage the security rules yourself, creating, updating, and deleting rules as required. Alternatively, you can specify that the oci-cloud-controller-manager (which runs on the cluster control plane) is to manage some, or all, of the security rules for you. Kubernetes Engine uses the oci-cloud-controller-manager to provision load balancers and network load balancers for Kubernetes services of type LoadBalancer. 
You use different annotations to specify whether the oci-cloud-controller-manager manages security rules for a load balancer or network load balancer in an NSG or in a security list, as follows:
  * **To manage security rules in an NSG, use the`oci.oraclecloud.com/security-rule-management-mode: "NSG"` annotation (recommended).**
If you want the oci-cloud-controller-manager to manage security rules in an NSG (as recommended by Oracle), you must use the `oci.oraclecloud.com/security-rule-management-mode: "NSG"` annotation. For more information about using this annotation, see [Using the oci.oraclecloud.com/security-rule-management-mode annotation to manage security rules in NSGs and security lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation).
  * **To manage security rules in a security list, use either the`oci.oraclecloud.com/security-rule-management-mode` annotation, or use the `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` and `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` annotations.**
If you want the oci-cloud-controller-manager to manage security rules in the security list of a load balancer or network load balancer's subnet, do one of the following:
    * Use the `oci.oraclecloud.com/security-rule-management-mode` annotation, set to `"SL-All"` or `"SL-Frontend"`. For more information about using this annotation, see [Using the oci.oraclecloud.com/security-rule-management-mode annotation to manage security rules in NSGs and security lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation).
    * Use the `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` and `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` annotations respectively, set to `"All"` or `"Frontend"`. For more information about using these two annotations, see [Specifying Security List Management Options When Provisioning an OCI Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#listmgmt) and [Specifying Security List Management Options When Provisioning an OCI Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingloadbalancer_topic_Specifying_Network_Load_Balancer_Security_List_Management_Options) respectively.


Regardless of the annotations you use, and regardless of whether you or the oci-cloud-controller-manager manages security rules in a security list or in an NSG, you can also specify the OCID of one or more additional NSGs to which you want the oci-cloud-controller-manager to add the load balancer or network load balancer. In this case, you use the `oci.oraclecloud.com/oci-network-security-groups` or `oci-network-load-balancer.oraclecloud.com/oci-network-security-groups` annotation. Note that the oci-cloud-controller-manager does not manage the security rules in the additional NSGs specified by these annotations, so it is your responsibility to manage the security rules. For more information about using the `oci.oraclecloud.com/oci-network-security-groups` or `oci-network-load-balancer.oraclecloud.com/oci-network-security-groups` annotations, see [Specifying Network Security Groups (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Network_Security_Group).
### Using the `oci.oraclecloud.com/security-rule-management-mode` annotation to manage security rules in NSGs and security lists 🔗 
#### Required IAM Policies for Managing Security Rules in NSGs 🔗 
To enable the oci-cloud-controller-manager to manage the security rules for a cluster's load balancer in NSGs, you must give the cluster permission to manage NSGs. For example, to grant this permission in a particular compartment:
```
ALLOW any-user to manage network-security-groups in compartment <compartment-name> where request.principal.type = 'cluster' 

```

In addition, to enable the oci-cloud-controller-manager to create a network security group, you must also give the cluster permission to manage VCNs or to manage virtual network families. For example, by specifying one or other of the following policy statements:
  * `ALLOW any-user to manage vcns in compartment <compartment-name> where request.principal.type = 'cluster'`
  * `ALLOW any-user to manage virtual-network-family in compartment <compartment-name> where request.principal.type = 'cluster'`


#### Using the `oci.oraclecloud.com/security-rule-management-mode` annotation
To specify that the oci-cloud-controller-manager is to manage security rules for a load balancer or network load balancer in an NSG (as recommended by Oracle), you must first set up the necessary IAM policies. See [Required IAM Policies for Managing Security Rules in NSGs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation__section_required-iam-policies-for-nsgs). Having set up the prerequisite IAM policies, you can then add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/security-rule-management-mode: "NSG"
```

The oci-cloud-controller-manager manages all required security rules for ingress to the load balancer or network load balancer service, in an NSG that the oci-cloud-controller-manager creates for the purpose. This NSG is known as the frontend NSG, and allows inbound traffic to the load balancer or network load balancer from 0.0.0.0/0, or from the source CIDR block (and on the source port range) if specified in the manifest file. The oci-cloud-controller-manager creates the following security rules in the frontend NSG:
Direction | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Ingress | 0.0.0.0/0 (or source CIDR block if specified in the manifest file) | Ports specified in the manifest file. | Allow inbound traffic to OCI load balancer.  
Egress | Backend NSG (if the OCID of a backend NSG is specified in the manifest file) | ALL/(Nodeports for service) | Allow traffic to worker nodes.  
Egress | Backend NSG (if the OCID of a backend NSG is specified in the manifest file) | TCP/ health check port (10256)If source IP address is preserved, health check port is automatically picked by the service. | Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes for health check port.  
If you want the oci-cloud-controller-manager to manage security rules for ingress traffic to the worker nodes in the backend set, along with egress traffic from the load balancer or network load balancer service, you have to specify the OCID of an existing NSG to use for that purpose. This NSG is known as the backend NSG. The oci-cloud-controller-manager only adds egress rules to the frontend NSG if you specify a backend NSG. To specify the NSG to use as the backend NSG, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/oci-backend-network-security-group: "<nsg-ocid>"
```

where <nsg-ocid> is the OCID of an existing NSG that is both in the same VCN as the cluster, and also an NSG to which the compute instances hosting worker nodes have already been added. For example:
Copy
```
oci.oraclecloud.com/oci-backend-network-security-group: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....cwex"
```

You can specify the OCIDs of multiple backend NSGs in a comma-delimited list. For example:
Copy
```
oci.oraclecloud.com/oci-backend-network-security-group: "ocid1.networksecuritygroup.oc1.phx.aaaaaa....cwex,ocid1.networksecuritygroup.oc1.phx.aaaaaa....jfle,ocid1.networksecuritygroup.oc1.phx.aaaaaa....pkrj"
```

Note that the compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation. You can add the compute instances to the backend NSG in one of the following ways:
  * By specifying the NSG when creating a node pool (in the case of managed nodes and virtual nodes).
  * By manually adding the primary VNICs of the compute instances hosting the worker nodes to the NSG using the Compute service (in the case of managed nodes). For example, by using the Compute service's Console pages (or the Compute service's CLI or API).


The oci-cloud-controller-manager creates the following security rules in the backend NSG:
Direction | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Ingress | Frontend NSG OCID | TCP/ health check port (10256)If source IP address is preserved, health check port is automatically picked by the service. | Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes for health checks.  
Ingress | Frontend NSG OCID | ALL/(Nodeports for service) | Allow OCI load balancer or network load balancer to communicate with worker nodes.  
If you do not specify an OCID for the backend NSG, the oci-cloud-controller-manager does not manage either the security rules for ingress traffic to the worker nodes in the backend set, or the security rules for egress traffic from the load balancer or network load balancer. 
You can also set the `oci.oraclecloud.com/security-rule-management-mode` annotation to other values to specify that you want to manage security rules yourself, or you want the oci-cloud-controller-manager to manage security rules in security lists. The complete syntax for the annotation is as follows:
Copy
```
oci.oraclecloud.com/security-rule-management-mode: <value>
```

where `<value>` is one of:
  * `"NSG"`: (recommended) The oci-cloud-controller-manager manages all required security rules for ingress to the load balancer or network load balancer service, in a network security group (NSG) that it creates for that purpose. 
  * `"None"`: (default for network load balancers) No security list management is enabled, and the oci-cloud-controller-manager does not manage security rules. It is your responsibility to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. Additionally, you have to set up security rules to allow inbound traffic to load balancers and network load balancers (see [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers)). This is equivalent to setting `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` or `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` to `"None"`.
  * `"SL-All"`: (default for load balancers) The oci-cloud-controller-manager manages all required security rules for ingress and egress to and from the load balancer or network load balancer service, in a security list. This is equivalent to setting `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` or `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` to `"All"`.
  * `"SL-Frontend"`: The oci-cloud-controller-manager only manages security rules for ingress to load balancer and network load balancer services, in a security list. It is your responsibility to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. This is equivalent to setting `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` or `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` to `"Frontend"`.


In clusters with managed nodes, if you don't explicitly specify a management mode or you specify an invalid value, the oci-cloud-controller-manager manages all required security rules for ingress and egress to and from the load balancer or network load balancer service, in a security list (equivalent to `"SL-All"`). Be aware that in this case, the oci-cloud-controller-manager creates a security rule that allows inbound traffic from 0.0.0.0/0 (or from the source port ranges specified in the manifest file) to listener ports. In clusters with virtual nodes, security list management is never enabled and you always have to manually configure security rules (equivalent to `"None"`).
Note the following:
  * If you include both the `oci.oraclecloud.com/security-rule-management-mode` annotation and either of the `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` or `oci-network-load-balancer.oraclecloud.com/security-list-management-mode` annotations in the manifest, the oci-cloud-controller-manager always uses the `oci.oraclecloud.com/security-rule-management-mode` and ignores the other annotation.
  * There are limits to the number of ingress and egress rules that are allowed in both security lists and network security groups (see [Security List Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#sec_list_limits) and [Network Security Group Limits](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#nsg_limits) respectively). If the number of ingress or egress rules exceeds the limit, creating or updating the load balancer or network security group fails.
  * A load balancer or network load balancer can be added to a maximum of five NSGs. If the number of NSGs exceeds the limit, an error is returned.
  * If the Kubernetes service of type LoadBalancer is deleted, the OCI resources created by the oci-cloud-controller-manager (the frontend NSG, and security rules created in either the frontend NSG or the backend NSG) are removed. The backend NSG, and any security rules that the oci-cloud-controller-manager did not create, are not removed.
  * When provisioning a network load balancer for a Kubernetes service of type LoadBalancer, you can use the `is-preserve-source: "true"` annotation to specify the preservation of the client IP address in the headers of IP packets (only valid when the `externalTrafficPolicy` annotation is set to `"Local"`). In this case, the oci-cloud-controller-manager creates security rules in the backend NSG to allow access to the worker nodes in the backend set from the CIDR blocks specified by `loadBalancerSourceRanges` in the LoadBalancer service manifest. Note that if CIDR blocks are not specified by `loadBalancerSourceRanges`, the oci-cloud-controller-manager creates a security rule to allow access from the internet (0.0.0.0/0) on the port number specified by `nodePort`. 
  * The backend NSG that you specify as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation must be in the same VCN as the cluster.
  * The compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation.


### Examples of security rule management annotations 🔗 
#### Example 1: Create a new frontend NSG with managed security rules, and have managed security rules in an existing backend NSG
In this example: 
  * You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
  * You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG.


You specify `"NSG"` as the value of the `oci.oraclecloud.com/security-rule-management-mode` annotation, and specify the OCID of the existing NSG as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation:
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"  
  oci.oraclecloud.com/security-rule-management-mode: "NSG"
  oci.oraclecloud.com/oci-backend-network-security-group: <nsg_ocid> 
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

In this case:
  * The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules. 
  * The oci-cloud-controller-manager manages the security rules of the backend NSG that has the OCID specified by the `oci-backend-network-security-group` annotation.


Note the following:
  * The backend NSG that you specify as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation must be in the same VCN as the cluster.
  * The compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation.


#### Example 2: Create a new frontend NSG with managed security rules, and manually manage security rules in an existing backend NSG
In this example: 
  * You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
  * You want to manually define security rules to control traffic from the load balancer's front end to the back end in an NSG that you create and manage. For example, you might want to create security rules to prevent traffic being routed from the LB to the worker nodes.


You specify `"NSG"` as the value of the `oci.oraclecloud.com/security-rule-management-mode` annotation:
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"  
  oci.oraclecloud.com/security-rule-management-mode: "NSG"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

In this case:
  * The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules. 
  * You are responsible for creating and managing security rules in a backend NSG to control traffic from the frontend NSG to the backend NSG.


#### Example 3: Create a new frontend NSG with managed security rules, and have managed security rules in an existing backend NSG (but annotations used incorrectly)
In this example: 
  * You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
  * You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG. However, you specify the annotations incorrectly.


You correctly specify `"NSG"` as the value of the `oci.oraclecloud.com/security-rule-management-mode` annotation. However, you mistakenly include the `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` annotation, and omit the `oci.oraclecloud.com/oci-backend-network-security-group` annotation:
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"  
  oci.oraclecloud.com/security-rule-management-mode: "NSG"
  service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "All"
 spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

In this case:
  * The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules.
  * The oci-cloud-controller-manager ignores the `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` annotation (because the `oci.oraclecloud.com/security-rule-management-mode` annotation is present).
  * You are responsible for creating and managing security rules in a backend NSG to control traffic from the frontend NSG to the backend NSG (because the `oci.oraclecloud.com/oci-backend-network-security-group` annotation is not present).


#### Example 4: Create a new frontend NSG with managed security rules, have managed security rules in an existing backend NSG, and add the load balancer to an existing NSG
In this example:
  * You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
  * You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG.
  * You want the oci-cloud-controller-manager to add the load balancer to an existing NSG that has security rules that you manage.


You specify:
  * `"NSG"` as the value of the `oci.oraclecloud.com/security-rule-management-mode` annotation.
  * The OCID of the existing NSG that you want the oci-cloud-controller-manager to use, as the value of the `oci.oraclecloud.com/oci-backend-network-security-group` annotation.
  * The OCID of the existing NSG to which you want the oci-cloud-controller-manager to add the load balancer.


The manifest is as follows:
```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"  
  oci.oraclecloud.com/security-rule-management-mode: "NSG"
  oci.oraclecloud.com/oci-backend-network-security-group: <nsg_ocid>
  oci.oraclecloud.com/oci-network-security-groups: "<nsg-ocid>"
 spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

In this case:
  * The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules. 
  * The oci-cloud-controller-manager manages the security rules of the backend NSG that has the OCID specified by the `oci.oraclecloud.com/oci-backend-network-security-group` annotation.
  * The oci-cloud-controller-manager adds the load balancer to the NSG specified by the `oci.oraclecloud.com/oci-network-security-groups` annotation.


## Specifying Health Check Parameters 🔗 
Oracle Cloud Infrastructure load balancers and network load balancers apply a health check policy to continuously monitor backend servers. A health check is a test to confirm backend server availability, and can be a request or a connection attempt. If a server fails the health check, the load balancer or network load balancer takes the server temporarily out of rotation. If the server subsequently passes the health check, the load balancer or network load balancer returns it to the rotation.
Health check policies include a number of parameters, which each have a default value. When Kubernetes Engine provisions an OCI load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can override health check parameter default values by including annotations in the metadata section of the manifest file. You can later add, modify, and delete those annotations. If you delete an annotation that specified a value for a health check parameter, the load balancer or network load balancer uses the parameter's default value instead.
[Configure health check parameters for load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To configure health check parameters when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotations in the metadata section of the manifest file:
  * To specify how many unsuccessful health check requests to attempt before a backend server is considered unhealthy, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-health-check-retries: "<value>"
```

where `<value>` is the number of unsuccessful health check requests.
  * To specify the interval between health check requests, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-health-check-interval: "<value>"
```

where `<value>` is a numeric value in milliseconds. The minimum is 1000.
  * To specify the maximum time to wait for a response to a health check request, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-health-check-timeout: "<value>"
```

where `<value>` is a numeric value in milliseconds. A health check is successful only if the load balancer receives a response within this timeout period.


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
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-health-check-retries: "5"
  service.beta.kubernetes.io/oci-load-balancer-health-check-interval: "15000"
  service.beta.kubernetes.io/oci-load-balancer-health-check-timeout: "4000"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

[Configure health check parameters for network load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To configure health check parameters when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotations in the metadata section of the manifest file:
  * To specify how many unsuccessful health check requests to attempt before a backend server is considered unhealthy, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/health-check-retries: "<value>"
```

where `<value>` is the number of unsuccessful health check requests.
  * To specify the interval between health check requests, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/health-check-interval: "<value>"
```

where `<value>` is a numeric value in milliseconds. The minimum is 1000.
  * To specify the maximum time to wait for a response to a health check request, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/health-check-timeout: "<value>"
```

where `<value>` is a numeric value in milliseconds. A health check is successful only if the network load balancer receives a response within this timeout period.


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
  oci-network-load-balancer.oraclecloud.com/health-check-retries: "5"
  oci-network-load-balancer.oraclecloud.com/health-check-interval: "15000"
  oci-network-load-balancer.oraclecloud.com/health-check-timeout: "4000"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you don't explicitly specify health check parameter values by including annotations in the metadata section of the manifest file, the following defaults are used:
Load Balancer Annotation | Network Load Balancer Annotation |  Default Value Used  
---|---|---  
`service.beta.kubernetes.io/oci-load-balancer-health-check-retries` | `oci-network-load-balancer.oraclecloud.com/health-check-retries` | "3"  
`service.beta.kubernetes.io/oci-load-balancer-health-check-interval` | `oci-network-load-balancer.oraclecloud.com/health-check-interval` | "10000"  
`service.beta.kubernetes.io/oci-load-balancer-health-check-timeout` | `oci-network-load-balancer.oraclecloud.com/health-check-timeout` | "3000"  
For more information about Oracle Cloud Infrastructure load balancer and network load balancer health check policies, see:
  * [Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)
  * [Health Check Policies for Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/health-check-policy-management.htm)


## Selecting Worker Nodes To Include In Backend Sets 🔗 
Incoming traffic to an Oracle Cloud Infrastructure load balancer or network load balancer is distributed between the backend servers in a backend set. By default, when Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, all the worker nodes in the cluster are included in the backend set. 
However, you have the option to select only a subset of worker nodes in a cluster to include in the backend set of a given load balancer or network load balancer. Including subsets of a cluster's worker nodes in the backend sets of different load balancers and network load balancers enables you to present a single Kubernetes cluster as multiple logical clusters (services).
[Select worker nodes to include in load balancer backend set](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To select the worker nodes to include in the backend set when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/node-label-selector: <label>
```

where `<label>` is one or more label keys and values, identified using standard Kubernetes label selector notation. For example, `lbset=set1`
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
  oci.oraclecloud.com/load-balancer-type: "lb"
  oci.oraclecloud.com/node-label-selector: lbset=set1
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

[Select worker nodes to include in network load balancer backend set](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To select the worker nodes to include in the backend set when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/node-label-selector: <label>
```

where `<label>` is one or more label keys and values, identified using standard Kubernetes label selector notation. For example, `lbset=set1`
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
  oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset=set1
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Use standard Kubernetes label selector notation to specify the label keys and values in the annotations in the metadata section of the manifest file. For more information about standard Kubernetes label selector notation, see [Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) in the Kubernetes documentation. 
The table gives some examples of standard Kubernetes label selector notation.
Load Balancer Annotation | Network Load Balancer Annotation |  Include in the backend set:  
---|---|---  
`oci.oraclecloud.com/node-label-selector: lbset=set1` | `oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset=set1` |  All worker nodes with the label key `lbset` that has the value `set1`  
`oci.oraclecloud.com/node-label-selector: lbset in (set1, set3)` | `oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset in (set1, set3)` |  All worker nodes with the label key `lbset` that has the value `set1` or `set3`  
`oci.oraclecloud.com/node-label-selector: lbset` | `oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset` | All worker nodes with the label key `lbset`, regardless of its value.  
`oci.oraclecloud.com/node-label-selector: env=prod,lbset in (set1, set3)` | `oci-network-load-balancer.oraclecloud.com/node-label-selector: env=prod,lbset in (set1, set3)` |  All worker nodes with the label key `env` that has the value `prod`, and with the label key `lbset` that has the value `set1` or the value `set3`  
`oci.oraclecloud.com/node-label-selector: env!=test` | `oci-network-load-balancer.oraclecloud.com/node-label-selector: env!=test` |  All worker nodes with the label key `env` that does not have the value `test`  
## Specifying Backend Set Policies 🔗 
When Kubernetes Engine provisions a load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can define a policy for the backend set to specify how to distribute incoming traffic to the backend servers.
For more information:
  * About load balancers and backend set policies, see [Load Balancer Policies](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).
  * About network load balancers and backend set policies, see [Network Load Balancer Policies](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies)


[Specifying a backend set policy for a load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To specify a policy for the backend set when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/loadbalancer-policy: <value>
```

where `<value>` is one of:
  * `"ROUND_ROBIN"`: Routes incoming traffic sequentially to each server in a backend set list.
  * `"LEAST_CONNECTIONS"`: Routes incoming non-sticky request traffic to the backend server with the fewest active connections.
  * `"IP_HASH"`: Routes incoming non-sticky request traffic from the same client to the same backend server as long as that server is available, using the incoming request's source IP address as a hashing key. 


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
  oci.oraclecloud.com/load-balancer-type: "lb"
  oci.oraclecloud.com/loadbalancer-policy: "LEAST_CONNECTIONS"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you don't explicitly specify a policy for the backend set, "ROUND_ROBIN" is used as the default value.
[Specifying a backend set policy for a network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To specify a policy for the backend set when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/backend-policy: <value>
```

where `<value>` is one of:
  * `"TWO_TUPLE"`: Routes incoming traffic based on 2-Tuple (source IP, destination IP) Hash.
  * `"THREE_TUPLE"`: Routes incoming traffic based on 3-Tuple (source IP, destination IP, protocol) Hash.
  * `"FIVE_TUPLE"`: Routes incoming traffic based on 5-Tuple (source IP and port, destination IP and port, protocol) Hash.


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
  oci-network-load-balancer.oraclecloud.com/backend-policy: "THREE_TUPLE"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you don't explicitly specify a policy for the backend set, "FIVE_TUPLE" is used as the default value.
## Specifying Pod Readiness Gates 🔗 
**Note** You can specify pod readiness gates for clusters with virtual nodes, but not for clusters with managed nodes.
When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can use a pod readiness gate to ensure traffic is only routed to pods that have both been successfully added to the backend set, and that are ready to receive traffic. Note that you can specify pod readiness gates for pods running on virtual nodes, but not for pods running on managed nodes. Do not define pod readiness gates for pods running on managed nodes.
Pod readiness gates are additional conditions to indicate that a pod is ready to receive traffic. Pod readiness gates enable you to implement complex custom readiness checks, and can help to achieve zero downtime during rolling deployments. For more information, see [pod readiness details in the Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate).
When provisioning a load balancer or network load balancer, the backend set comprises the IP addresses of a deployment's pod replicas that have a condition of `Ready`. Updating the deployment (for example, to use a new image) triggers the replacement of existing pod replicas with new pod replicas. However, replacing all of the pod replicas can take some time and cause backend unavailability because:
  * The existing pod replicas might be terminated before the backend set has been updated with the IP addresses of the new pod replicas.
  * The backend set might be updated with the IP addresses of the new pod replicas before the new pod replicas are ready to receive traffic.


Specifying the use of a pod readiness gate ensures that backends are always available for the load balancer or network load balancer. Existing pods are not terminated until new pods have been added to the backend set, and the new pods are ready to receive traffic. 
To specify that Kubernetes Engine is to inject a pod readiness gate into the pod spec of every pod created in a particular namespace, add the `loadbalancer.oci.oraclecloud.com/pod-readiness-gate-inject=enabled` label to the namespace by entering:
```
kubectl label ns <namespace> loadbalancer.oci.oraclecloud.com/pod-readiness-gate-inject=enabled
```

The following example shows you how to create a load balancer with a pod readiness gate.
First, label the `pdr` namespace to specify the pod readiness gate for the namespace, by entering:
```
kubectl label ns pdr loadbalancer.oci.oraclecloud.com/pod-readiness-gate-inject=enabled
```

The output from the command confirms the namespace has been labeled:
```
namespace/pdr labeled
```

Then, deploy Nginx in the `pdr` namespace by entering: 
```
kubectl apply -f https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/nginx-svc/nginx.yaml -n pdr
```

List the pods in the `pdr` namespace by entering: 
```
kubectl get pods -n pdr
```

Now you can demonstrate the use of the pod readiness gate by updating the image version in the Nginx manifest and reapplying the manifest, so that existing pods are replaced with new pods. 
Download the Nginx manifest from <https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/nginx-svc/nginx.yaml>, and change the image version to `nginx:1.25.1`, as shown:```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx
spec:
 replicas: 3
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx:1.25.1
...
```

Re-apply the manifest by entering:
```
kubectl apply -f ./nginx.yaml -n pdr
```

Observe the new pods being rolled out by entering:
```
kubectl get pods -o wide -n pdr
```

For example:
```
NAME           READY  STATUS  RESTARTS  AGE  IP      NODE     NOMINATED NODE  READINESS GATES
nginx-678976847c-8bqs7  1/1   Running  0     44m  10.0.10.153  10.0.10.253  <none>      1/1
nginx-678976847c-ttqms  1/1   Running  0     47m  10.0.10.201  10.0.10.253  <none>      1/1
```

Observe the status of one of the new pods by entering:
```
kubectl describe pod <pod-name> -n pdr
```

For example:
```
kubectl describe pod nginx-678976847c-ttqms -n pdr
```

The output from the command confirms the status of the `podreadiness.loadbalancer.oraclecloud.com` readiness gate. For example:
```
...
Readiness Gates:
 Type                               Status
 podreadiness.loadbalancer.oraclecloud.com/f913fe603a9be9b5d51f  True 
Conditions:
 Type                               Status
 podreadiness.loadbalancer.oraclecloud.com/f913fe603a9be9b5d51f  True 
 PodScheduled                           True 
 Initialized                           True 
 Ready                              True 
 ContainersReady                         True 
```

## Specifying IPMode to adjust traffic routing 🔗 
When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can specify how to route traffic originating from within a cluster to the load balancer's or network load balancer's IP address.
In clusters running Kubernetes version 1.30 or later, the `LoadBalancerIPMode` Kubernetes feature gate is enabled, and the `ipMode` field of a service of type LoadBalancer has the default value of "VIP". When `ipMode` has the value of "VIP", traffic sent to the IP address of a service of type LoadBalancer from a pod within the cluster is routed straight to application pods to optimize performance, bypassing the LoadBalancer service. For more information, see [Specifying IPMode of load balancer status](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-ip-mode) in the Kubernetes documentation. 
However, in some situations, you might decide that routing traffic straight to application pods is not appropriate. For example, if traffic that originates within a cluster is routed straight to application pods, you cannot implement SSL termination at the load balancer level.
To specify how to route traffic that is sent to the load balancer's or network load balancer's IP address from within the cluster, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/ingress-ip-mode: <value>
```

where `<value>` is one of:
  * `"VIP"` : All traffic originating from within the cluster and sent to the IP address of a service of type LoadBalancer is routed straight to the application pods to optimize performance, bypassing the LoadBalancer service.
  * `"proxy"` : All traffic originating from within the cluster and sent to the IP address of a service of type LoadBalancer is routed to the Oracle Cloud Infrastructure load balancer or network load balancer that has been provisioned for the LoadBalancer service. The load balancer or network load balancer then forwards the traffic to the application pods.


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
  oci.oraclecloud.com/load-balancer-type: "lb"
  oci.oraclecloud.com/ingress-ip-mode: "proxy"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you do not specify the `oci.oraclecloud.com/ingress-ip-mode` annotation, or subsequently remove the annotation, the `ipMode` property of a service of type LoadBalancer has the default value of `"VIP"`. 
Also note that when using a private network load balancer with the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation set to `true`, the network load balancer has a known limitation that does not allow traffic where the source node and the destination backend node are the same node. This limitation prevents communication between pods on the same node via the network load balancer when the following conditions are all met:
  * The `oci.oraclecloud.com/ingress-ip-mode` annotation is set to `proxy` .
  * The `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation is set to `true` .
  * The network load balancer is private.


## Specifying IP Address Families for Load Balancers and Network Load Balancers 🔗 
When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, the load balancer subnet determines the control you have over the IP address family of the IP address on which the load balancer or network load balancer receives traffic.
  * If the subnet is an IPv4 single stack subnet, the subnet is configured for IPv4 addressing only. The load balancer or network load balancer is only allocated an IPv4 address on which to receive external traffic. You cannot change the IP address family of the IP address on which the load balancer or network load balancer receives external traffic.
  * If the subnet is an IPv4/IPv6 dual stack subnet, the subnet is configured for both IPv4 and IPv6 addressing. The load balancer or network load balancer can be allocated either or both an IPv4 address and an IPv6 address on which to receive external traffic. In this situation, you can use the Kubernetes `spec.ipFamilyPolicy` and `spec.ipFamilies` fields in the service manifest to specify whether the load balancer or network load balancer receives external traffic on the IPv4 address only, or on the IPv6 address only, or on both the IPv4 address and the IPv6 address.


Note that the IP address family used for traffic between the listener and the backend set is determined differently for load balancers and network load balancers:
  * **Load balancers:** The traffic between a load balancer listener and the backend set always uses IPv4 addresses. 
  * **Network load balancers:** The traffic between a network load balancer listener and the backend set uses the same IP address family as the IP address on which the network load balancer listener receives external traffic.


The table shows the interaction between the load balancer subnet's IP address family, the settings of `spec.ipFamilyPolicy` and `spec.ipFamilies`, the IP address family from which IP addresses are allocated to the load balancer or network load balancer, and the IP protocol between the listener and the backend set. Note that only valid combinations are shown.
Subnet IP Address Family | `ipFamilyPolicy` set to: | `ipFamilies` set to: | IP address family of the network load balancer endpoint | IP address family of the load balancer | Network load balancer listener to backend set traffic | Load balancer listener to backend set traffic  
---|---|---|---|---|---|---  
IPv4 | `SingleStack` | `IPv4` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4/IPv6 | `SingleStack` | `IPv4` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4/IPv6 | `SingleStack` | `IPv6` | IPv6 | not supported | IPv6 | not supported  
IPv4 | `PreferDualStack` | `IPv4` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4 | `PreferDualStack` | `IPv6` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4 | `PreferDualStack` | `IPv4,IPv6` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4 | `PreferDualStack` | `IPv6,IPv4` | IPv4 | IPv4 | IPv4 | IPv4  
IPv4/IPv6 | `PreferDualStack` | `IPv4` | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4  
IPv4/IPv6 | `PreferDualStack` | `IPv6` |  IPv6(primary) and IPv4 | IPv6(primary) and IPv4 | IPv6(primary) and IPv4  | IPv4  
IPv4/IPv6 | `PreferDualStack` | `IPv4,IPv6` | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4  
IPv4/IPv6 | `PreferDualStack` | `IPv6,IPv4` | IPv6(primary) and IPv4 | IPv6(primary) and IPv4 | IPv6(primary) and IPv4 | IPv4  
IPv4/IPv6 | `RequireDualStack` | `IPv4,IPv6` | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4(primary) and IPv6 | IPv4  
IPv4/IPv6 | `RequireDualStack` | `IPv6,IPv4` | IPv6(primary) and IPv4 | IPv6(primary) and IPv4 | IPv6(primary) and IPv4 | IPv4  
Note that if you use the `service.beta.kubernetes.io/oci-load-balancer-subnet1` annotation to specify an alternative subnet to the subnet specified for load balancers when the cluster was created, make sure the alternative subnet's address family is compatible with the `spec.ipFamilyPolicy` and `spec.ipFamilies` fields in the service manifest.
For more information about IPv4 and IPv6 support in Kubernetes, see [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/) in the Kubernetes documentation. 
### Example 1: 
In this example:
  * You want to use the subnet specified for load balancers when the cluster was created.
  * You only want to deploy the service of type LoadBalancer if it can be assigned both an IPv4 and an IPv6 address, so you set `ipFamilyPolicy: RequireDualStack`.
  * You want the load balancer's primary IP address to be an IPv6 address (and its secondary address to be an IPv4 address), so you set `spec.ipFamilies: IPv6,IPv4`.


Copy
```
apiVersion: v1
kind: Service
metadata:
 name: nginx-lb
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb" 
spec:
 type: LoadBalancer
 ipFamilyPolicy: RequireDualStack
 ipFamilies:
 - IPv6
 - IPv4
 ports:
 - name: http
  port: 80
  targetPort: 80
 selector:
  app: nginx
```

In this example, the cluster's load balancer subnet is a dual stack IPv4/IPv6 subnet, so the deployment is successful. The load balancer is assigned an IPv6 address as its primary address, and an IPv4 address as its secondary address.
### Example 2: 
In this example:
  * You want to host the service of type LoadBalancer on an alternative subnet to the one specified for load balancers when the cluster was created, so you use the `service.beta.kubernetes.io/oci-load-balancer-subnet1` annotation to specify the alternative subnet's OCID.
  * You want to allocate both IPv4 and IPv6 addresses to the service of type LoadBalancer if the service is hosted on a dual stack IPv4/IPv6 subnet. Otherwise, if the service is hosted on a single stack IPv4 subnet, you want an IP address allocated to the service from that IP address family. So you set `ipFamilyPolicy: PreferDualStack`.
  * You want the load balancer's primary IP address to be an IPv4 address (and its secondary address to be an IPv6 address, if supported by the subnet), so you set `spec.ipFamilies: IPv4,IPv6`.


Copy
```
apiVersion: v1
kind: Service
metadata:
 name: nginx-lb
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-subnet1: "ocid1.subnet.oc1..aaaaaa....vdfw" 
spec:
 type: LoadBalancer
 ipFamilyPolicy: PreferDualStack
 ipFamilies:
 - IPv4
 - IPv6
 ports:
 - name: http
  port: 80
  targetPort: 80
 selector:
  app: nginx
```

In this example, the alternative subnet is a dual stack IPv4/IPv6 subnet, so the deployment is successful. The load balancer is assigned an IPv4 address as its primary address, and an IPv6 address as its secondary address.
## Concealing a Network Load Balancer's Private IP Address 🔗 
When Kubernetes Engine provisions a public Oracle Cloud Infrastructure network load balancer for a Kubernetes service of type LoadBalancer, the Network Load Balancer service assigns both a public IP address and a private IP address to the network load balancer. The private IP address is used for health checks and port address translation (PAT), but cannot receive external traffic from outside the VCN (including from the public internet).
To see the public and private IP addresses that the Network Load Balancer service has assigned to the network load balancer, enter the `kubectl get service` command (or similar). For example:
```
kubectl get service my-nginx-svc -o json | jq .status
{
 "loadBalancer": {
  "ingress": [
   {
    "ip": "203.0.113.2"
   },
   {
    "ip": "10.30.3.24"
   }
  ]
 }
}
```

In some situations, you might only want to expose the network load balancer's public IP address, and hide the private IP address. For example:
  * You might specify a friendly DNS name for the network load balancer when using the ExternalDNS add-on, by including the `external-dns.alpha.kubernetes.io/hostname` annotation in the manifest of the Kubernetes service of type LoadBalancer. ExternalDNS creates a DNS record for the network load balancer in the external DNS provider you've configured for the cluster. The DNS record maps the DNS name to both the public IP address and the private IP address. As a result, if external traffic uses the DNS name, there is a possibility that traffic might be routed to the network load balancer's private IP address, even though the private IP address cannot receive external traffic.
  * You might set up automation that uses the `kubectl get service` command (or similar) to obtain the IP address of the network load balancer. If your usecase includes routing external traffic, you only want the network load balancer's public IP address. However, by default, the `kubectl get service` command returns both the network load balancer's public IP address and its private IP address. 


To specify that the `kubectl get service` command (or similar) only returns the network load balancer's public IP address, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/external-ip-only: "true"
```

Note that `"false"` is the default value of the `oci-network-load-balancer.oraclecloud.com/external-ip-only` annotation. If you do not explicitly include the annotation in the service definition, the `kubectl get service` command (or similar) returns both the network load balancer's public IP address and private IP address
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
  oci-network-load-balancer.oraclecloud.com/external-ip-only: "true"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

If you include the `oci-network-load-balancer.oraclecloud.com/external-ip-only: "true"` annotation in the manifest, when you enter the `kubectl get service` command (or similar), only the public IP address is returned. For example:
```
kubectl get service my-nginx-svc -o json | jq .status
{
 "loadBalancer": {
  "ingress": [
   {
    "ip": "203.0.113.2"
   }
  ]
 }
}
```

## Preventing Nodes from Handling Traffic 🔗 
You can exclude particular worker nodes from the list of backend servers in the backend set of an Oracle Cloud Infrastructure load balancer or network load balancer. For more information, see [node.kubernetes.io/exclude-from-external-load-balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengsupportedlabelsusecases.htm#exclude-from-external-load-balancers).
## Tagging Load Balancers and Network Load Balancers 🔗 
You can add tags to a load balancer or network load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See [Applying Tags to Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm#contengtaggingclusterresources_tagging_oke_resources_load_balancer_tags "Find out how to apply tags to load balancer resources, and how to override initial load balancer tags, when using Kubernetes Engine \(OKE\).").
## Enabling Proxy Protocol 🔗 
When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can specify whether to enable the proxy protocol feature with TCP-based listeners. Enabling proxy protocol allows transport connection information such as a client's IP address to be securely transported across multiple layers of proxies to the backend server. The following proxy protocol versions are available:
  * Version 1, which uses a text-based header to pass information across proxies, and is best for small implementations.
  * Version 2, which uses a text-based and binary header for greater efficiency in producing and parsing, and is best for larger implementations.


Load balancers provisioned by Kubernetes Engine support proxy protocol version 1 and version 2. Network load balancers provisioned by Kubernetes Engine support proxy protocol version 2.
For more information:
  * About load balancers and the proxy protocol feature, see [Proxy Protocol for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm#proxy-protocol).
  * About network load balancers and the proxy protocol feature, see [Proxy Protocol for Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm#proxy-protocol).


[Enabling proxy protocol for load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To enable proxy protocol for load balancers provisioned by Kubernetes Engine, add the following annotation in the metadata section of the manifest file:
```
service.beta.kubernetes.io/oci-load-balancer-connection-proxy-protocol-version: "<value>"
```

where `"<value>"` is one of:
  * `"1"` to specify that you want to enable proxy protocol version 1 on all listeners of the load balancer.
  * `"2"` to specify that you want to enable proxy protocol version 2 on all listeners of the load balancer. 


Having enabled the proxy protocol feature for load balancers, note the following:
  * You cannot disable the proxy protocol feature on load balancer listeners.
  * You can switch between proxy protocol version 1 and proxy protocol version 2 by updating the annotation.
  * If you subsequently remove the annotation from the manifest, or unset the annotation (by setting `"<value>"` to `""`), the last successfully applied setting for `"<value>"` is retained on all listeners.


[Enabling and disabling proxy protocol for network load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm)
To enable proxy protocol for network load balancers provisioned by Kubernetes Engine, add the following annotation in the metadata section of the manifest file:
```
oci-network-load-balancer.oraclecloud.com/is-ppv2-enabled: "<value>"
```

where `"<value>"` is one of:
  * `"true"` to specify that you want to enable proxy protocol version 2 on all listeners of the network load balancer.
  * `"false"` to specify that you want to disable proxy protocol version 2 on all listeners of the network load balancer.


Having enabled the proxy protocol feature for network load balancers, note the following:
  * You can disable the proxy protocol feature on network load balancer listeners by setting `"<value>"` to `"false"`.
  * If you subsequently remove the annotation from the manifest, or unset the annotation (by setting `"<value>"` to `""`), or specify an invalid value (such as `"enable"`) for the annotation, the last successfully applied setting for `"<value>"` is retained on all listeners.


Was this article helpful?
YesNo

