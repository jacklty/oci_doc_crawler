Updated 2024-08-23
# Multi-tenancy Best Practices
_Find out about best practices for sharing one or more clusters between tenants when using Kubernetes Engine (OKE)._
This section contains best practices for multi-tenancies and Kubernetes Engine.
In Kubernetes Engine, multi-tenancy is the name given to the sharing of one or more clusters between tenants. A tenant is a workload, or several related workloads, or a team responsible for those workloads. We recommend that you consider having separate clusters if you have multiple tenants, teams, or users with differing levels of trust all accessing the same cluster. 
## Best Practice: Use RBAC Authorizer for additional fine-grained access 🔗 
We recommend that you use the Kubernetes RBAC Authorizer to enforce fine-grained access control for users on specific clusters via Kubernetes RBAC roles and clusterroles.
A Kubernetes RBAC role is a collection of permissions. For example, a role might include read permission on pods and list permission for pods. A Kubernetes RBAC clusterrole is just like a role, but can be used anywhere in the cluster. A Kubernetes RBAC rolebinding maps a role to a user or group, granting that role's permissions to the user or group for resources in that namespace. Similarly, a Kubernetes RBAC clusterrolebinding maps a clusterrole to a user or group, granting that clusterrole's permissions to the user or group across the entire cluster.
See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Use namespaces if multiple clusters are not an option 🔗 
We recommend that you create separate namespaces for each team if a Kubernetes cluster is large (with hundreds of nodes) and there are multiple teams working on the cluster. For example, you will typically create different namespaces for development, testing, and production teams.
A Kubernetes cluster can be organized into namespaces, to divide the cluster's resources between multiple users. Initially, a cluster has the following namespaces:
  * default, for resources with no other namespace
  * kube-system, for resources created by the Kubernetes system
  * kube-node-lease, for one lease object per node to help determine node availability
  * kube-public, usually used for resources that have to be accessible across the cluster


Namespaces play an important role in keeping a cluster secure when multiple users and teams are working on the same cluster. 
See [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.
## Best Practice: Use a namespace naming convention to ease deployment across multiple environments 🔗 
We recommend that you establish and use a namespace naming convention that makes it easy to create deployments across multiple environments and hosted in different clusters.
For example, avoid including environment names in namespace names. Instead, use the same namespace name across all environments. By using the same namespace name, you can use the same config files in all environments, and you avoid having to create a config file specific to each environment. 
See [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.
## Best Practice: Isolate workloads in dedicated node pools 🔗 
We recommend that you implement strong infrastructure isolation by using dedicated node pools to isolate tenants. For example, for a multi-tenanted application running each tenant on a dedicated compute resource, separated by node pools. 
Many multi-tenanted SaaS applications require tenants to run on dedicated compute resources, and require the ability to control network traffic via security lists per tenant. The two most common strategies for such a SaaS application tenancy model are to:
  * Leverage namespaces and network policies to isolate tenants.
  * Leverage dedicated compute/security lists to isolate tenants.


## Best Practice: Enforce resource quotas 🔗 
We recommend that you create and enforce Kubernetes resource quotas to ensure that all tenants sharing a cluster have fair access to the cluster resources.
Create a resource quota for each namespace, based on the number of pods deployed by each tenant, and the amount of memory and CPU required by each pod.
For example, the following `ResourceQuota` config:
  * allows pods in the `tenant-a` namespace to request up to 16 CPUs, and up to 64 GB of memory
  * limits the maximum number of CPUs to 32, and the maximum memory to 72 GB


```
apiVersion: v1
kind: ResourceQuota
metadata:
 name: tenant-a
spec:
 hard: "1"
  requests.cpu: "16"
  requests.memory: 64Gi
  limits.cpu: "32"
  limits.memory: 72Gi
```

See [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) in the Kubernetes documentation.
## Best Practice: Autoscale worker nodes and pods 🔗 
We recommend that you enable autoscaling to accommodate tenant demand by automatically scaling the node pools and pods in a cluster.
Autoscaling ensures that the system continues to appear responsive and healthy, even when different tenants deploy heavy workloads in their own namespaces. Autoscaling also helps the system to respond to outages. 
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\)."), [Using the Kubernetes Horizontal Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm#Using_Kubernetes_Horizontal_Pod_Autoscaler "Find out how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Use a flexible load balancer 🔗 
We recommend that you specify a flexible shape for Oracle Cloud Infrastructure load balancers to accommodate tenant demand.
Using a flexible shape for OCI load balancers that Kubernetes Engine provisions for Kubernetes services of type LoadBalancer enables you to:
  * Avoid the restrictions associated with fixed bandwidth load balancer shapes, because you can specify minimum and maximum values to create an upper and lower size range for the load balancer's bandwidth shape.
  * Avoid the limitations associated with scaling based only on general traffic patterns.


See [Specifying Flexible Load Balancer Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#flexible).
## Best Practice: Centralize network control (Optional) 🔗 
We recommend that you maintain centralized control over network resources using a **dynamic routing gateway (DRG)** and (optionally) a hub VCN.
Using a DRG enables you to route traffic through a centralized network virtual appliance. 
Optionally creating a hub VCN enables you to configure the main routing and firewalls. Resources in a hub VCN can communicate with other VCNs securely and efficiently using internal IPs. Using a hub VCN and IAM ensures only network administrators have access to the centralized VCN. This separation helps you implement the principle of least privilege. 
For example:
  * The centralized network team can administer the network without having any permissions to access Kubernetes clusters (which reside in spoke VCNs). 
  * The Kubernetes Engine administrators can manage clusters without having any permissions to manipulate the shared network. 


See [Routing traffic through a central network virtual appliance](https://docs.oracle.com/iaas/Content/Network/Tasks/scenario_g.htm).
Was this article helpful?
YesNo

