Updated 2024-08-14
# Common Issues with Nodes and Pods
_Find out how to identify and fix common problems with nodes and pods on clusters you've created using Kubernetes Engine (OKE)._
You might encounter these issues with nodes and pods on clusters you've created using Kubernetes Engine.
## Unresponsive worker nodes and/or pods stuck in Pending state due to insufficient resources 🔗 
You might see the following issues with nodes and pods on clusters you've created using Kubernetes Engine:
  * Unresponsive worker nodes.
  * Worker nodes with a status shown as NotReady in response to the `kubectl get node` command.
  * Pods stuck in a Pending state, with messages such as `FailedScheduling due to Insufficient cpu` or ` FailedScheduling due to Insufficient memory`.


A likely cause of these issues is insufficient system resources for the Kubernetes and OS system daemons.
We recommend that you use the `--kube-reserved` and `--system-reserved` kubelet flags to reserve CPU and memory resources for Kubernetes system daemons (such as `kubelet` and `container runtime`) and OS system daemons (such as `sshd` and `systemd`) respectively. For example:
  * `--kube-reserved=cpu=500m,memory=1Gi`
  * `--system-reserved=cpu=100m,memory=100Mi`


Pods running on a worker node can consume all available CPU and memory resources, and so prevent other essential processes (such as the Kubernetes and OS system daemons) from running on the node. When Kubernetes and OS system daemons cannot run, the worker node can become unresponsive, unstable, and unexpectedly crash under heavy load. 
To prevent pods requesting resources that are required by the Kubernetes and OS system daemons, include the `--kube-reserved` and `--system-reserved` kubelet flags as `kubelet-extra-args` options in a custom cloud-init script. For more information and an example, see [Example 4: Using a Custom Cloud-init Script to Reserve Resources for Kubernetes and OS System Daemons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases__CustomCloudinitScriptExampleReserveResources).
When using the `--kube-reserved` kubelet flag to reserve a portion of a worker node's CPU and memory resources for use by Kubernetes system daemons, consider the following recommendations:
  * The amount of CPU resource that we recommend you reserve for Kubernetes system daemons depends on the number of CPU cores on the worker node, as shown in the following table:
Number of CPU cores on worker node | 1 | 2 | 3 | 4 | 5 | More than 5  
---|---|---|---|---|---|---  
Recommended CPU to reserve, in millicore (m) | 60 m | 70 m | 80 m | 85 m | 90 m | An additional 2.5 m for every additional core on worker node  
  * The amount of memory resource that we recommend you reserve for Kubernetes system daemons depends on the amount of memory on the worker node, as shown in the following table:
Memory on worker node, in GiB | 4 GiB | 8 GiB | 16 GiB | 128 GiB | More than 128 GiB  
---|---|---|---|---|---  
Recommended memory to reserve, in GiB |  1 GiB | 1 GiB | 2 GiB | 9 GiB | An additional 20 MiB for every additional GiB of worker node memory  


When using the `--system-reserved` kubelet flag to reserve a portion of a node's CPU and memory resources for use by OS system daemons, consider the following recommendations:
  * The amount of CPU resource that we recommend you reserve for OS system daemons (regardless of node shape) is 100 m (millicore).
  * The amount of memory resource that we recommend you reserve for OS system daemons (regardless of node shape) is 100 Mi (mebibytes).


Note that our CPU and memory recommendations for the `--kube-reserved` and `--system-reserved` kubelet flags might not be optimal for the workloads you intend to run, so you might need to alter the values accordingly. You might also need to adjust the values over time.
To see the difference between the total resources on a worker node and the resources on the node that workloads can use, run the following command:
```
kubectl get node <NODE_NAME> -o=yaml | grep -A 6 -B 7 capacity
```

Example output:
```
 allocatable:
  cpu: 15743m
  ephemeral-storage: "34262890849"
  hugepages-1Gi: "0"
  hugepages-2Mi: "0"
  memory: 234972476Ki
  pods: "110"
 capacity:
  cpu: "16"
  ephemeral-storage: 37177616Ki
  hugepages-1Gi: "0"
  hugepages-2Mi: "0"
  memory: 257197372Ki
  pods: "110"
```

The difference between the "capacity" and "allocatable" CPU and memory in the example output includes the CPU and memory reservations for the Kubernetes and OS system daemons.
**Note**
From June 2024, the recommendations for the CPU and memory resource reservations for Kubernetes and OS system daemons described in this section are used as the defaults for all OKE images, for all supported Kubernetes versions. The recommendations are also used as the defaults for all platform images for Kubernetes version 1.30 and later. The defaults apply both when you specify an OKE image released in June 2024 (or later), and when you upgrade the version of Kubernetes running on a cluster to version 1.30 (or later). If you specify an OKE image released in June 2024 (or later) or if you upgrade a cluster to Kubernetes version 1.30, we recommend that you check the default reservations are appropriate for the workloads you intend to run. 
## Creating virtual node pools displays an "API Server unreachable" message 🔗 
When creating a virtual node pool in a cluster you've created using Kubernetes Engine, you might see the following message if you view the work request logs or work request errors for the operation's work request id:
```
API Server Unreachable, Check network configuration and ensure network path between Virtual Node and API Server exist
```

This message indicates a network configuration problem. Double-check that the network is configured correctly to allow virtual nodes in the virtual node pool to communicate with the Kubernetes API server. For a suitable network configuration, see [Example Network Resource Configuration for Cluster with Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig-virtualnodes.htm#contengnetworkconfig-virtualnodes "Find out about how you might configure network resources for a cluster with virtual nodes when using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

