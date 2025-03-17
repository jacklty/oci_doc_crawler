Updated 2024-08-14
# Resources Allocated to Pods Provisioned by Virtual Nodes
_Find out about limits and other factors to consider in the allocation of CPU, memory, and storage resources to pods provisioned by virtual nodes when using Kubernetes Engine (OKE)._
When using virtual nodes, resource allocation is at the pod level (rather than at the worker node level). 
## CPU and Memory Resource Allocation
To calculate the number of CPUs (expressed in Oracle CPUs, or OCPUs) and the amount of memory to allocate to pods provisioned by virtual nodes, Kubernetes Engine considers:
  * the CPU and memory requests and limits for each container specified in the pod spec, if present
  * the number of containers in the pod
  * the kube-proxy and container runtime requirements (0.25GB of memory, negligible CPU)


The following minimums apply to pod CPU and memory requests:
  * 0.125 OCPU
  * 0.5GB of memory


With regards CPU and memory limits and requests specified in the pod spec for containers, Kubernetes Engine applies the following rules when calculating OCPU and memory allocation:
  * If a limit is specified in the pod spec but no request, Kubernetes Engine uses the limit value.
  * If a request is specified but no limit, Kubernetes Engine uses the request value.
  * If both a request and a limit are specified, Kubernetes Engine uses the limit value.
  * If neither a request nor a limit are specified, Kubernetes Engine uses 0.125 OCPU and 0.5GB per container.


Since pods provisioned by virtual nodes always come with an assured capacity, we recommend setting limits and requests to the same value.
The maximum number of CPUs that can be allocated to pods provisioned by virtual nodes depends on the shape (and processor) specified for the virtual node pool. For example, in the case of Pod.Standard.E3.Flex and Pod.Standard.E4.Flex (AMD) shapes, the maximum number is 64 cores (128 vCPUs).
The number of OCPUs allocated to pods provisioned by virtual nodes also determines the network bandwidth available to the pods, with 1Gbps available per OCPU subject to the following limits:
  * a maximum bandwidth limit of 40Gbps
  * a minimum bandwidth limit of 1Gbps


**Note**
When calculating OCPU and memory allocation, Kubernetes Engine currently:
  * rounds up the CPU allocation to the nearest whole number of OCPUs
  * rounds up the memory allocation to the nearest whole number of GBs


## Storage Allocation
Pods provisioned by virtual nodes are each allocated 15GB of storage space, in which to store the root file systems of containers running on the pod. Note that container images consume some of that 15GB storage allocation. The remaining allocation is available to the application for use as temporary storage.
## Resource Billing
When running a Kubernetes job on virtual nodes, note that you continue to be billed for resources that the job uses for as long as the job exists, even when the job has completed or has failed. Therefore, to avoid being billed for resources unnecessarily, delete the job after it has finished. For example, by using a command such as `kubectl delete job <job-name>` or `kubectl delete -f <job-spec>.yaml`.
Was this article helpful?
YesNo

