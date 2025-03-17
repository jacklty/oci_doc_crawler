Updated 2024-10-28
# Comparing Virtual Nodes with Managed Nodes
_Find out about the differences between the virtual nodes and managed nodes you can create using Kubernetes Engine (OKE)._
When creating a node pool with Kubernetes Engine, you specify the type of worker nodes to create in the node pool as one or other of the following:
  * **Virtual nodes:** Virtual nodes are fully managed by Oracle. See [Virtual Nodes and Virtual Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-virtualnodes).
  * **Managed nodes:** Managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy, and are at least partly managed by you. See [Managed Nodes and Managed Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-managednodes).


You can only create virtual nodes in enhanced clusters. You can create managed nodes in both basic clusters and enhanced clusters.
All references to 'nodes' and 'worker nodes' in the Kubernetes Engine documentation refer to both virtual nodes and managed nodes, unless explicitly stated otherwise.
## Virtual Nodes and Virtual Node Pools 🔗 
Virtual nodes run in the Kubernetes Engine tenancy. You create virtual nodes by creating a virtual node pool. Virtual nodes and virtual node pools are fully managed by Oracle. 
Virtual nodes provide a 'serverless' Kubernetes experience, enabling you to run containerized applications at scale without the operational overhead of upgrading the data plane infrastructure and managing the capacity of clusters.
You can only create virtual nodes and node pools in enhanced clusters.
### Notable features supported differently by virtual nodes 🔗 
Some features are supported differently when using virtual nodes rather than managed nodes:
  * **Resource Allocation:** Resource allocation is at the pod level, rather than at the worker node level. Consequently, you specify CPU and memory resource requirements (as requests and limits) in the pod specification, rather than for the worker nodes in a node pool. See [Resources Allocated to Pods Provisioned by Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengvirtualnodepodresourceallocation.htm#contengvirtualnodepodresourceallocation "Find out about limits and other factors to consider in the allocation of CPU, memory, and storage resources to pods provisioned by virtual nodes when using Kubernetes Engine \(OKE\).").
  * **Load Balancing:** Load balancing is between pods, rather than between worker nodes (as is the case with managed nodes). In clusters with virtual nodes, load balancer security list management is never enabled and you always have to manually configure security rules. Load balancers distribute traffic among pods' IP addresses and an assigned node port. When connecting to pods running on virtual nodes, use the syntax `<pod-ip>:<nodeport>`, rather than `<node-ip>:<nodeport>`. If you use different subnets for pods and nodes, configure node port ingress on the pod subnet.
  * **Pod Networking:** Only VCN-Native Pod Networking is supported (the flannel CNI plugin is not supported). Moreover, support is slightly different when using virtual nodes:
    * Only one VNIC is attached to each virtual node.
    * IP addresses are not pre-allocated before pods are created.
    * The VCN-Native Pod Networking CNI plugin is not shown as running in the kube-system namespace.
    * Since only VCN-Native Pod Networking is supported, the pod subnet route table must have route rules defined for a NAT gateway (not an internet gateway) and a service gateway.
  * **Autoscaling:** Virtual nodes automatically scale to support 500 pods. Because Oracle manages the underlying resources for virtual nodes, it is easier to work with the Kubernetes Horizontal Pod Autoscaler. It's not necessary to use the Kubernetes Cluster Autoscaler (which is not yet supported with virtual nodes in any case). The Kubernetes Vertical Pod Autoscaler is not supported with virtual nodes.


### Notable Kubernetes features and capabilities not supported when using virtual nodes 🔗 
Some Kubernetes features and capabilities are not supported, or not yet available, when using virtual nodes rather than managed nodes.
Kubernetes features not supported | Additional information  
---|---  
Flannel and other third party CNI plugins are not supported. | Virtual nodes only support the OCI VCN-Native Pod Networking CNI plugin.  
Kubernetes daemonsets are not supported. |  For example, the following is not supported: ```
apiVersion: apps/v1
kind: DaemonSet
```
  
Persistent volume claims (PVCs) are not supported. | No additional information.  
Network providers that support NetworkPolicy resources alongside the CNI plugin used in the cluster (such as Calico and Cilium) are not supported. | No additional information.  
Network policies (the Kubernetes NetworkPolicy resource) are not supported. | No additional information.  
Service mesh products are not supported. | Products such as Oracle Cloud Infrastructure Service Mesh and Istio Service Mesh are not supported.  
Liveness and readiness probes of type HTTP _are_ supported. HTTPS and exec probes are supported. Startup probes are supported. gRPC probes are _not_ supported. probe.terminationGracePeriodSeconds is _not_ supported. | For example, the following are supported:```
livenessProbe:
 httpGet:
  path: /healthz
  port: 8080
 initialDelaySeconds: 3
 periodSeconds: 3
```
```
livenessProbe:
 exec:
  command:
  - cat
  - /tmp/healthy
```
```
livenessProbe:
 httpGet:
  path: /healthz
  port: 8080
  scheme: "HTTPS"
```
```
startupProbe:
 httpGet:
  path: /healthz
  port:8080
```
However, the following is not supported:```
livenessProbe:
 grpc:
   port: 8080
 initialDelaySeconds: 5
 periodSeconds: 5
```
  
The `kubectl logs` command _is_ supported. The `kubectl logs -p` command _is_ supported. The `kubectl logs -f` command is _not_ supported. | For example, the following are supported:```
kubectl logs workload1-589578899f-lwzm9
```
```
kubectl logs workload1-589578899f-lwzm9 -p
```
However, the following is not supported:```
kubectl logs workload1-589578899f-lwzm9 -f 
```
  
Ephemeral containers are not supported. | No additional information.  
Init-containers are not supported. | No additional information.  
The following Volume Types _are_ supported:
  * emptyDir
  * ConfigMap
  * Secret
  * ProjectedVolume of the following types:
    * ServiceAccount
    * ConfigMap
    * Secret

The following Volume Types are _not_ supported:
  * hostPath
  * persistentVolumeClaim
  * local
  * nfs
  * iscsi
  * cephfs

|  For example, the following is not supported: ```
volumes:
- name: test-volume
 hostPath:
  path: /data
```
  
Maximum of 1 volume of type emptyDir can currently be defined in the pod spec.  | No additional information.  
The following Pod fields are not supported:
  * hostIPC
  * hostNetwork
  * hostPid
  * hostName
  * podOS
  * Overhead
  * setHostNameAsFqdn
  * shareProcessNamespace

| For example, the following is not supported:```
spec:
 hostIPC: true
 hostNetwork: true
 hostPID: false
 setHostnameAsFQDN : true
 shareProcessNamespace : true
```
  
The following Pod security contexts _are_ supported:
  * runAsNonRoot
  * runAsUser
  * runAsGroup

The following Pod security contexts are _not_ supported:
  * fsGroup
  * fsGroupChangePolicy
  * supplementalGroups
  * seLinuxOptions
  * sysctls
  * seccompProfile

| For example, the following is not supported:```
spec:
 securityContext:
  seLinuxOptions:
   type: dummy_container.proces
```
  
The following Container security contexts _are_ supported:
  * readOnlyRootFilesystem
  * allowPrivilegeEscalation:false
  * capabilities

The following Container security contexts are _not_ supported:
  * allowPrivilegeEscalation:true
  * privileged
  * procMount

| For example, the following is supported:```
containers:
 - name: openssh-1
  securityContext:
   capabilities:
    add:
    - CAP_NET_ADMIN
```
However, the following is not supported:```
containers:
 - name: openssh-1
  securityContext:
   procMount: Unmasked
```
  
Container.Port
  * Host IP
  * Host Port

| For example, the following is not supported:```
ports:
 - name: test
  containerPort: 81
  hostPort: 80
```
  
Container
  * TerminationMessagePolicy
  * TerminationMessagePath
  * VolumeDevices
  * VolumeMount.MountPropagation
  * VolumeMount.Subpath Expression

| Note that Kubernetes adds TerminationMessagePolicy and TerminationMessagePath by default.  
Container port range (1, 65535) cannot conflict with NodePort range (30000-32767). | For example, the following is not supported:```
containers:
 - name: my-nginx
  image: nginx
  ports:
  - containerPort: 30002
```
  
Pod.Volumes.EmptyDirVolumeSource:SizeLimit | For example, the following is not supported:```
emptyDir:
 sizeLimit: 500Mi
```
  
Pod.Volumes.EmptyDirVolumeSource:Medium - can only be "" or "Memory" | For example, the following is not supported:```
emptyDir:
 medium: "Memory1"
```
  
Pod:Volumes - Mode must be specified as 0644 for the following:
  * ConfigMapVolumeSource:KeyToPath:Mode
  * SecretVolumeSource:KeyToPath:Mode
  * ProjectedVolumeSource:SecretProjection:KeyToPath:Mode
  * ProjectedVolumeSource:ConfigMapProjection:KeyToPath:Mode

| For example, the following is not supported:```
- name: myconfigmap
 configMap:
  name: kube-root-ca.crt
  items:
  - key: ca.crt
   path: abc
   mode: 0400
```
  
Pod:Volumes - if DefaultMode specified for the following, DefaultMode must be 0644:
  * ConfigMapVolumeSource:DefaultMode
  * ProjectedVolumeSource:DefaultMode
  * SecretVolumeSource:DefaultMode

| For example, the following is not supported:```
- name: workload-volume
  configMap:
   name: myconfigmap
   defaultMode: 0400
```
  
Resources.Requests cannot be different from Resources.Limits | For example, the following is not supported:```
resources:
 requests:
  cpu: 50m
  memory: 200Mi
 limits:
  cpu: 100m
  memory: 400Mi
```
  
Volumes:DownwardAPI:ResourceFieldRef | For example, the following is not supported:```
resourceFieldRef:
 containerName: openssh
 resource: limits.cpu
```
  
TerminationGracePeriodSeconds | For example, the following is not supported:```
terminationGracePeriodSeconds: 30
```
  
DeletionGracePeriodSeconds | For example, the following is not supported:```
metadata:
 DeletionGracePeriodSeconds: 30
```
  
Exec Container | For example, the following is not supported:```
kubectl exec workload1-589578899f-lwzm9 -- sh
```
  
Kubectl port-forward command | Use `kubectl proxy` instead (see [Troubleshooting Pod and Service Issues on Virtual Nodes Using kubectl proxy Rather Than kubectl port-forward](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingpodsonvirtualnodesusingkubectlproxy.htm#contengaccessingpodsonvirtualnodesusingkubectlproxy "Find out how to use kubectl proxy \(rather than kubectl port-forward\) to view application output to help you resolve issues with pods running on virtual nodes.")).  
UpdatePod requests with mutations to pod.spec.containers[].image | No additional information.  
Propagation to pods of updates to mounted configmaps and secrets | No additional information.  
The following container-level metrics in the virtual kubelet metrics endpoint _are_ supported:
  * container_cpu_usage_seconds_total
  * container_memory_working_set_bytes

Other container-level metrics in the virtual kubelet metrics endpoint are _not_ supported. | No additional information.  
Container:ResourceRequirements Subcore | No additional information.  
Container stdin/stdinOnce, tty | No additional information.  
Preserve client IP addresses when externalTrafficPolicy: Local | No additional information.   
ImagePullSecret types other than config and configJson | No additional information.   
ProjectedVolumeSource:ServiceAccountTokenProjection:ExpirationSeconds | No additional information.  
The `kubectl attach` command to interact with a process that is already running inside an existing container. | No additional information.  
### Notable Kubernetes Engine (OKE) features and capabilities not supported when using virtual nodes 🔗 
Some Kubernetes Engine features and capabilities are not available, or not yet available, when using virtual nodes rather than managed nodes.
Kubernetes Engine features not supported | Additional information  
---|---  
SSH connections to worker nodes (including via a bastion) | Not available.  
Use of custom cloud-init scripts | Not available.  
Node Doctor script | Not available.  
Support for Kubernetes versions prior to version 1.25 | Virtual nodes require the cluster to be running at least Kubernetes version 1.25.  
Mixed clusters, containing both virtual nodes and managed nodes. | Not yet available.  
Autoscale the number of virtual nodes. | Not yet available.  
Capacity reservations to provision virtual nodes. | Not yet available.  
Pods with Intel and GPU shapes. | Not yet available.  
Credential rotation, as described in [Rotating Cluster Credentials](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials "Find out how to rotate the credentials of clusters you've created using Kubernetes Engine \(OKE\).") | Not yet available.  
### Common deployments not supported, and supported differently, when using virtual nodes 🔗 
The following common deployments are not supported when using virtual nodes rather than managed nodes, or are supported differently:
Deployment | Notes  
---|---  
kube-proxy in the kube-system namespace, and the kube-proxy cluster add-on | kube-proxy runs in pods scheduled on virtual nodes, but is not deployed in the kube-system namespace.  
Kubernetes Dashboard | Not supported when using virtual nodes.  
Nginx ingress controller | Deploy differently when using virtual nodes (see [Setting Up the Example Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm#settingupcontroller)).  
Kubernetes Cluster Autoscaler | Not supported when using virtual nodes.  
Vertical Pod Autoscaler | Not supported when using virtual nodes.  
Kubernetes Metrics Server | Deploy differently when using virtual nodes (see [Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm#Deploying_Kubernetes_Metrics_Server_Using_Kubectl "Find out how to deploy the Kubernetes Metrics Server as a standalone program or as a cluster add-on, on a cluster you've created using Kubernetes Engine \(OKE\).")).  
## Managed Nodes and Managed Node Pools 🔗 
Managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy. You create managed nodes by creating a managed node pool. Managed nodes and managed node pools are managed by you. 
As you are responsible for managing managed nodes, you have the flexibility to configure them to meet your specific requirements. You are responsible for upgrading Kubernetes on managed nodes, and for managing cluster capacity.
When using managed nodes, you pay for the compute instances that execute applications.
You can create managed nodes and node pools in both basic clusters and enhanced clusters.
For more information, see [Comparing Managed Nodes with Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingmanagednodeswithvirtualnodes_topic.htm#contengcomparingmanagednodeswithvirtualnodes_topic "Find out about the differences between the managed nodes and virtual nodes you can create using Kubernetes Engine \(OKE\).")
Was this article helpful?
YesNo

