Updated 2025-02-28
# Large Cluster Best Practices
_Find out about best practices for managing large clusters you've created with Kubernetes Engine (OKE)._
This section contains best practices for large clusters and Kubernetes Engine.
## Best Practice: Limit burst scaling to approximately 10% of the pods and nodes in a cluster 🔗 
We recommend that both nodes and pods are added or removed from a large cluster in batches of approximately 10% of their total number.
Cluster scaling actions (such as changing the number of nodes in a node pool, configuring the number of replicas in a deployment, and spawning jobs in the cluster) can generate a high amount of API traffic for distributed coordination and scheduling of resources. The 10% recommendation is generally conservative enough to avoid encountering rate limits in the Kubernetes API server and other downstream cloud endpoints, and so avoid costly retries during a time of high traffic that might cause delays due to backoffs.
The 10% recommendation is a starting point, and depends on the size of the cluster and the types of workload it contains. Workloads with many operators that all communicate with the kube-apiserver might require more burst-smoothing, whereas empty nodes with minimal workload might be able to burst more quickly.
See [Considerations for large clusters](https://kubernetes.io/docs/setup/best-practices/cluster-large/) in the Kubernetes documentation.
## Best Practice: Configure FlowSchemas to optimize rate-limiting decisions when under load 🔗 
We recommend de-prioritizing requests that are not time-critical on large clusters.
The API Priority and Fairness (APF) feature in the kube-apiserver exposes some controls to rate-limit requests. You can configure the APF feature using priority levels, which define flexible configurations for the hand size and queue size allotted to a particular priority. Using priority levels enables advanced workloads to optimize request processing, and ensures high-priority requests are served.
A FlowSchema defines the priority level that a request belongs to. A common configuration, particularly in clusters with bursting workloads that require the addition or removal of large numbers of pods or nodes, is to use a FlowSchema that reduces the priority of `LIST /events` requests to the `catch-all` priority level. In Kubernetes, LIST calls are generally the most expensive for the kube-apiserver to serve, and in times of high churn, the number of events can become large. By installing a FlowSchema that lowers the priority level of these calls, more time-critical requests can be served. Lower priority requests receive HTTP 429 Too Many Requests errors, and will be retried later by the clients to become eventually consistent.
See [Isolate non-essential requests from starving other flows](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/#isolate-non-essential-requests-from-starving-other-flows) in the Kubernetes documentation.
You can use the metrics published by the kube-apiserver at `/metrics` to identify when throttling is occurring, and which flows might be good candidates for a custom schema:
  * Use the `apiserver_flowcontrol_rejected_requests_total` metric to see when requests are failing to be served and must be retried. If the value becomes non-zero, throttling has occurred, and you might want to take action.
  * Use the `apiserver_flowcontrol_request_wait_duration_seconds` metric to see which priority levels are a bottleneck.


See [Good practices for using API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/#good-practices-for-using-api-priority-and-fairness) in the Kubernetes documentation.
## Best Practice: Tune cluster add-ons to scale with cluster size 🔗 
We recommend configuring the CoreDNS and flannel add-ons in large clusters.
Enhanced clusters in Kubernetes Engine enable you to configure the add-ons that are installed in a cluster (see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).")). The defaults that are reasonable for smaller clusters are not necessarily optimal for large clusters. 
The default configuration for CoreDNS allocates 1 replica per node. However, in large clusters, fewer replicas might be more appropriate. For example, a configuration such as `{minReplica: 3, `nodesPerReplica`: 8}` might be more appropriate in a large cluster. A configuration with fewer replicas not only consumes fewer compute resources within the cluster, but also increases the likelihood of efficient cache hits by consolidating DNS requests to fewer replicas.
To avoid a single unavailable node halting the rollout of a change to the flannel DaemonSet, you can configure the rollout strategy to have a `maxUnavailable` value such as `25%`. Such a strategy enables the rollout of a flannel DaemonSet change to a large cluster that has thousands of nodes, even if a number of those nodes are unavailable.
For both the CoreDNS and flannel add-ons, in large clusters you might find it necessary to increase the allocated CPU and memory requests/limits to accommodate the load.
See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
## Best Practice: Configure Kubernetes clients to use the protobuf content type instead of JSON 🔗 
We recommend using the protobuf content type with large clusters, when available.
By default, Kubernetes clients use JSON as the content type for all requests. Using JSON as the content type is a user-friendly option, and sufficient for the majority of use cases. However, with large clusters, using protobuf rather than JSON as the content type can improve performance.
To specify the use of the protobuf content type:
  * For requests, use the `Content-Type: application/vnd.kubernetes.protobuf` header.
  * For responses, use the `Accept: application/vnd.kubernetes.protobuf, application/json` header. By specifying both `protobuf` and `json` in the `Accept` header, the Kubernetes API server can fall back to JSON if a protobuf representation does not exist for an object.


See [Alternate representations of resources](https://kubernetes.io/docs/reference/using-api/api-concepts/#alternate-representations-of-resources) in the Kubernetes documentation.
## Best Practice: Enable Service Logging for visibility into the Kubernetes control plane logs 🔗 
We recommend enabling service logs for large clusters.
The Kubernetes API server reports many problems to clients through warnings in server responses, as well as via events. However, the logs of the following Kubernetes control plane containers also capture additional information that can help you understand the behavior of large clusters:
  * kube-scheduler
  * kube-controller-manager
  * cloud-controller-manager
  * kube-apiserver


To enable and view these Kubernetes control plane logs as service logs in Oracle Cloud Infrastructure Logging, follow the instructions in [Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm#contengviewingservicelogs "Find out how to view the logs of Kubernetes processes \(such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver\) running on the control plane of clusters you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Allocate network CIDR blocks with sufficient IP addresses for the expected number of pods 🔗 
We recommend considering in advance how the size of the network CIDR block to specify for a large cluster, and which CNI plugin to select.
Subnet changes in a running cluster can be disruptive. In the case of pod CIDR blocks, you cannot change the pod CIDR block you initially specify for a cluster after the cluster has been created. Therefore, before you create a large cluster, to avoid network complications as a cluster scales, consider carefully which is the most appropriate CNI plugin to select, and which is the most appropriate CIDR block size to specify.
The flannel CNI plugin allows large private subnets to be allocated for use. We recommend a /12 CIDR block for the pod CIDR block. Due to the nature of VXLANs, the flannel CNI plugin can allocate/deallocate pods quickly, with the trade-off that pod traffic is now within VXLAN encapsulation. When choosing the size of a pod CIDR block, consider that Kubernetes Engine allocates a /25 CIDR block to each node. The size of the pod CIDR block that you specify can limit the number of nodes available to a cluster (for example, if you specify a /24 CIDR block as the pod CIDR block, then the cluster can only have 8 nodes). Depending on the pod-to-node ratio that you expect, a significant number of IP addresses might be allocated to each node that will be unused and not available to other nodes. If this is the case, specify a larger pod CIDR block (see [IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengcidrblocks.htm#CIDR_Blocks_and_Container_Engine_for_Kubernetes "Find out about the CIDR blocks to specify when using Kubernetes Engine \(OKE\).")).
The Native Pod Networking CNI plugin directly integrates with VCN networking using dedicated VNIC attachments. This approach removes limitations around per-node IP allocations, and eliminates the need for an additional VXLAN overlay networking layer in the cluster. However, VCN subnets are limited to a /16 CIDR block, which is a smaller address space than can be accommodated with flannel (see [Allowed VCN Size and Address Ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Allowed) ). Note that the number of VNICs that can be attached to a node is limited by the node size, so consider the shape selection for each node when evaluating how many pod IP addresses are needed (see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)).
The Kubernetes API endpoint subnet generally requires only a small CIDR block, because only a single endpoint IP address is required for each cluster that shares the subnet. For example, specifying a /29 CIDR block for the Kubernetes API endpoint subnet allows 6 clusters to share the subnet, while a /28 CIDR block allows 14 clusters to share the subnet.
## Best Practice: Preemptively request service limit increases 🔗 
We recommend reviewing the service limits configured for your tenancy, and submitting requests in advance to increase the service limits you expect large clusters to reach. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
Large clusters commonly reach the following limits:
  * The number and size of container image repositories.
  * The number of nodes allowed for a single cluster.
  * The number of gigabytes of block volumes that can be allocated.


To avoid possible disruption, we therefore recommend submitting requests to increase service limits in advance, especially for limits on block volumes that are used as boot volumes for nodes. 
See [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti)
## Best Practice: Leverage autoscaling to manage compute resources proportionally with workloads 🔗 
We recommend using autoscalers (such as the Kubernetes Cluster Autoscaler (CA), the Horizontal Pod Autoscaler (HPA), and the Vertical Pod Autoscaler (VPA)) with large clusters, to optimize resource usage.
Using an autoscaler enables you to set up rules that define when to provision more nodes, create more replicas, or scale down a cluster during a quiet period.
Automatic, rule-based scaling is an efficient way to manage large clusters with thousands of nodes and pods. 
See [Autoscaler Best Practices](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengbestpractices_topic-Autoscaler-best-practices.htm#contengbestpractices_topic-Autoscaler-best-practices "Find out about best practices for using the Kubernetes Cluster Autoscaler \(CA\), Horizontal Pod Autoscaler \(HPA\), and Vertical Pod Autoscaler \(VPA\) with clusters you've created by Kubernetes Engine \(OKE\).").
## Best Practice: Use stateless rules for security lists and network security groups to minimize connection tracking overhead 🔗 
We recommend using stateless rules when configuring security lists and network security groups for large clusters.
Tutorials and documentation often specify that you are to create security lists and network security groups with "stateful" rules. Stateful rules leverage connection tracking to ensure the return path for a request is automatically allowed, regardless of the presence of an egress rule (see [Connection Tracking](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#connection-tracking).). Although automatically allowing return paths is intended to simplify rule setup, these automatically allowed return paths are a potential overhead that can become an issue for large clusters. The number of connections that can be tracked is proportional to the shape of the instance used, but simply selecting a larger shape does not necessarily address the issue.
To eliminate the overhead of connection tracking and to avoid potential scaling limits, we therefore recommend that for each network path:
  1. you define an ingress rule and a corresponding egress rule as a pair.
  2. you specify the ingress and egress rules as "stateless".


See [Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful).
Was this article helpful?
YesNo

