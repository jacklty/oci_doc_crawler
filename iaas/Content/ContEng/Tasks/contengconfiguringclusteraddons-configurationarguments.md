Updated 2024-12-19
# Cluster Add-on Configuration Arguments
_Find out about the configuration arguments that you can pass to cluster add-ons._
When you enable a cluster add-on, you can specify one or more key/value pairs to pass as arguments to the cluster add-on.
If the value of a key is required in JSON format, you can specify the value in plain text or Base64 encoded. For example, you could specify either of the following as the value of the `coreDnsContainerResources` key:
  * `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}` (plain text)
  * `eyJsaW1pdHMiOiB7ImNwdSI6ICI1MDBtIiwgIm1lbW9yeSI6ICIyMDBNaSIgfSwgInJlcXVlc3RzIjogeyJjcHUiOiAiMTAwbSIsICJtZW1vcnkiOiAiMTAwTWkifX0=` (Base64 encoded)


If the value of a key is required in JSON form, depending on the OCI tool you are using, you might have to escape double quotation marks in the key value with single backslash characters, as follows:
  * If you are specifying the value of a key when using the Console, do not escape double quotation marks in the key value. For example, when using the Console to specify the value of the `cluster-autoscaler container resources` key, enter the following:```
{"limits":{"cpu": "250m", "memory": "400Mi"}, "requests": {"cpu": "50m", "memory": "200Mi"}}
```

  * If you are specifying the value of a key when using the CLI or API, always escape double quotation marks in the key value with a single backslash. For example, when using the CLI to specify the value of the `cluster-autoscaler container resources` key, use the following notation:```
{ "key": "cluster-autoscaler.ContainerResources", "value": "{\"limits\":{\"cpu\": \"250m\", \"memory\": \"400Mi\"}, \"requests\": {\"cpu\": \"50m\", \"memory\": \"200Mi\"}}" }
```



## kube-proxy add-on configuration arguments 🔗 
When you enable the kube-proxy cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
customizeKubeProxyConfigMap | customize kube-proxy configMap |  If you want Oracle to manage Kube-proxy for you automatically, set **customizeKubeProxyConfigMap** to `false` (the default). If you want to customize Kube-proxy behavior, set **customizeKubeProxyConfigMap** to `true` and create a kube-proxy configMap in the kube-system namespace. | Required | `false` | `true`  
kube-proxy.ContainerResources | kube-proxy container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## CoreDNS add-on configuration arguments 🔗 
When you enable the CoreDNS cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
coreDnsContainerResources | CoreDNS container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
customizeCoreDNSConfigMap | customize CoreDNS configMap |  If you want Oracle to manage CoreDNS for you automatically, set **customizeCoreDNSConfigMap** to `false` (the default). If you want to customize CoreDNS behavior, set **customizeCoreDNSConfigMap** to `true` and create a coredns configMap in the kube-system namespace. | Required | `false` | `true`  
minReplica | min replica |  The minimum number of replicas of the CoreDNS deployment. | Required | `1`Creates a total of one pod in the cluster. | `2`Creates a total of two pods in the cluster.  
nodesPerReplica | nodes per replica |  The number of CoreDNS replicas per cluster node. | Required | `1`Creates a replica on every node. | `2`Creates a replica on every second node.  
## OCI VCN-Native Pod Networking CNI plugin add-on configuration arguments 🔗 
When you enable the OCI VCN-Native Pod Networking CNI plugin cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
install-cni-ips.ContainerResources | install-cni-ips container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## flannel add-on configuration arguments 🔗 
When you enable the flannel CNI plugin cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
kube-flannel.ContainerResources | kube-flannel container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Kubernetes Dashboard add-on configuration arguments 🔗 
When you enable the Kubernetes Dashboard cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
kubernetes-dashboard.ContainerResources | kubernetes-dashboard container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Tiller add-on configuration arguments (not recommended) 🔗 
When you enable the Tiller cluster add-on, you can pass the following key/value pairs as arguments.
Note that Tiller was removed from Helm in version 3 (and later versions) due to known security risks. Because of those security risks, we strongly recommend that you do not deploy Tiller on production clusters. For the same reason, the Tiller add-on is not shown in the Console. If you decide that you do want to deploy the Tiller add-on despite the security risks, use the OCI CLI or API.
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
tiller.ContainerResources | tiller container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Oracle Database Operator for Kubernetes add-on configuration arguments 🔗 
When you enable the Oracle Database Operator for Kubernetes cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
manager.ContainerResources | manager container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## WebLogic Kubernetes Operator add-on configuration arguments 🔗 
When you enable the WebLogic Kubernetes Operator cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
weblogic-operator.ContainerResources | weblogic-operator container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
weblogic-operator-webhook.ContainerResources | weblogic-operator-webhook container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Certificate Manager add-on configuration arguments 🔗 
When you enable the Certificate Manager cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
cert-manager-cainjector.ContainerResources | cert-manager-cainjector container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
cert-manager-controller.ContainerResources | cert-manager-controller container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
cert-manager-webhook.ContainerResources | cert-manager-webhook container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Cluster Autoscaler add-on configuration arguments 🔗 
When you enable the Cluster Autoscaler add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value  
---|---|---|---|---  
annotations | annotations |  Annotations to pass to the Cluster Autoscaler deployment. For example, `"{\"prometheus.io/scrape\":\"true\",\"prometheus.io/port\":\"8086\"}"` JSON format in plain text or Base64 encoded. | Optional | ""  
authType | authType | The authentication type the Cluster Autoscaler uses while making requests, as one of:
  * `instance` specifies instance principal
  * `workload` specifies workload identity

| Required | instance  
balanceSimilarNodeGroups | balanceSimilarNodeGroups | Detect similar node groups and balance the number of nodes between them. | Optional | false  
balancingIgnoreLabel | balancingIgnoreLabel | Define a node label that should be ignored when considering node group similarity. One label per flag occurrence. The format is `label1, label2`. | Optional | ""  
balancingLabel | balancingLabel | Define a node label to use when comparing node group similarity. If set, all other comparison logic is disabled, and only labels are considered when comparing groups. One label per flag occurrence. The format is `label1, label2`. | Optional | ""  
cluster-autoscaler.ContainerResources | cluster-autoscaler container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
cordonNodeBeforeTerminating | (Not shown in Console) | Should CA cordon nodes before terminating during downscale process. | Optional | false  
coresTotal | (Not shown in Console) | Minimum and maximum number of cores in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. | Optional | 0:320000  
daemonsetEvictionForEmptyNodes | (Not shown in Console) | Whether DaemonSet pods will be gracefully terminated from empty nodes. | Optional | false  
daemonsetEvictionForOccupiedNodes | (Not shown in Console) | Whether DaemonSet pods will be gracefully terminated from non-empty nodes. | Optional | true  
debuggingSnapshotEnabled | (Not shown in Console) | Whether the debugging snapshot of cluster autoscaler feature is enabled. | Optional | false  
emitPerNodegroupMetrics | (Not shown in Console) | If true, emit per node group metrics. | Optional | false  
enforceNodeGroupMinSize | (Not shown in Console) | Should CA scale up the node group to the configured min size if needed. | Optional | false  
estimator | (Not shown in Console) | Type of resource estimator to be used in scale up. | Optional | binpacking  
expander | expander | Type of node group expander to be used in scale up. Note that `expander=price` is not supported. | Optional | random  
expendablePodsPriorityCutoff | (Not shown in Console) | Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they don't cause scale up. Pods with null priority (PodPriority disabled) are non-expendable. | Optional | -10  
ignoreDaemonsetsUtilization | (Not shown in Console) | Whether DaemonSet pods will be ignored when calculating resource utilization for scaling down. | Optional | false  
ignoreMirrorPodsUtilization | (Not shown in Console) | Whether Mirror pods will be ignored when calculating resource utilization for scaling down. | Optional | false  
leaderElect | (Not shown in Console) | Start a leader election client and gain leadership before executing the main loop. Enable this when running replicated components for high availability. | Optional | true  
leaderElectLeaseDuration | (Not shown in Console) | The duration that non-leader candidates will wait after observing a leadership renewal until attempting to acquire leadership of a led but un-renewed leader slot. This is effectively the maximum duration that a leader can be stopped before it is replaced by another candidate. This is only applicable if leader election is enabled. | Optional | 15s  
leaderElectRenewDeadline | (Not shown in Console) | The interval between attempts by the active cluster autoscaler to renew a leadership slot before it stops leading. This must be less than or equal to the lease duration. This is only applicable if leader election is enabled. | Optional | 10s  
leaderElectResourceLock | (Not shown in Console) | The type of resource object that is used for locking during leader election. Supported options are `leases` (default), `endpoints`, `endpointsleases`, `configmaps`, and `configmapsleases`. | Optional | leases  
leaderElectRetryPeriod | (Not shown in Console) | The duration the clients should wait between attempting acquisition and renewal of a leadership. This is only applicable if leader election is enabled. | Optional | 2s  
maxAutoprovisionedNodeGroupCount | (Not shown in Console) | The maximum number of auto-provisioned groups in the cluster. | Optional | 15  
maxEmptyBulkDelete | maxEmptyBulkDelete | Maximum number of empty nodes that can be deleted at the same time. | Optional | 10  
maxFailingTime | (Not shown in Console) | Maximum time from last recorded successful autoscaler run before automatic restart. | Optional | 15m  
maxGracefulTerminationSec | (Not shown in Console) | Maximum number of seconds CA waits for pod termination when trying to scale down a node. | Optional | 600  
maxInactivity | (Not shown in Console) | Maximum time from last recorded autoscaler activity before automatic restart. | Optional | 10m  
maxNodeProvisionTime | maxNodeProvisionTime | Maximum time CA waits for node to be provisioned. | Optional | 15m  
maxNodesTotal | (Not shown in Console) | Maximum number of nodes in all node pools. Cluster autoscaler will not grow the cluster beyond this number. | Optional | 0  
maxTotalUnreadyPercentage | (Not shown in Console) | Maximum percentage of unready nodes in the cluster. After this is exceeded, CA halts operations. | Optional | 45  
memoryTotal | (Not shown in Console) | Minimum and maximum number of gigabytes of memory in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. | Optional | 0:6400000  
minReplicaCount | (Not shown in Console) | Minimum number or replicas that a replica set or replication controller should have to allow their pods deletion in scale down. | Optional | 0  
nodes | nodes |  A list of Minimum number of nodes, Maximum number of nodes, and the OCID of the nodepool to be managed by cluster autoscaler. The format is `<min>:<max>:<node-pool1-ocid>, <min>:<max>:<node-pool2-ocid>`. JSON format in plain text or Base64 encoded. | Required | ""  
okTotalUnreadyCount | (Not shown in Console) | Number of allowed unready nodes, irrespective of max-total-unready-percentage. | Optional | 3  
recordDuplicatedEvents | (Not shown in Console) | Enable the autoscaler to print duplicated events within a 5 minute window. | Optional | false  
scaleDownCandidatesPoolMinCount | (Not shown in Console) |  Minimum number of nodes that are considered as additional non empty candidates for scale down when some candidates from previous iteration are no longer valid. When calculating the pool size for additional candidates we take. ```
max(#nodes * scale-down-candidates-pool-ratio,
       scale-down-candidates-pool-min-count)
```
| Required | 50  
scaleDownCandidatesPoolRatio | (Not shown in Console) | A ratio of nodes that are considered as additional non-empty candidates for scale down when some candidates from previous iteration are no longer valid. Lower value means better CA responsiveness but possible slower scale down latency. Higher value can affect CA performance with big clusters (hundreds of nodes). Set to 1.0 to turn this heuristics off - CA will take all nodes as additional candidates. | Required | 0.1  
scaleDownDelayAfterAdd | scaleDownDelayAfterAdd | How long after scale up that scale down evaluation resumes. | Required | 10m  
scaleDownDelayAfterDelete | (Not shown in Console) | How long after node deletion that scale down evaluation resumes, defaults to scan-interval. | Required | 10s  
scaleDownDelayAfterFailure | (Not shown in Console) | How long after scale down failure that scale down evaluation resumes. | Required | 3m  
scaleDownEnabled | scaleDownEnabled | Should CA scale down the cluster. | Optional | true  
scaleDownNonEmptyCandidatesCount | (Not shown in Console) | Maximum number of non empty nodes considered in one iteration as candidates for scale down with drain. Lower value means better CA responsiveness but possible slower scale down latency. Higher value can affect CA performance with big clusters (hundreds of nodes). Set to non positive value to turn this heuristic off - CA will not limit the number of nodes it considers. | Required | 30  
scaleDownUnneededTime | scaleDownUnneededTime | How long a node should be unneeded before it is eligible for scale down. | Required | 10m  
scaleDownUnreadyTime | (Not shown in Console) | How long an unready node should be unneeded before it is eligible for scale down. | Required | 20m  
scaleDownUtilizationThreshold | (Not shown in Console) | Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. | Required | 0.5  
scanInterval | scanInterval | How often cluster is re-evaluated for scale up or down. | Optional | 10s  
skipNodesWithCustomControllerPods | (Not shown in Console) | If true, cluster autoscaler will never delete nodes with pods owned by custom controllers. | Optional | true  
skipNodesWithLocalStorage | (Not shown in Console) | If true, cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. | Optional | true  
skipNodesWithSystemPods | (Not shown in Console) | If true, cluster autoscaler will never delete nodes with pods from kube-system (except for DaemonSet or mirror pods). | Optional | true  
statusConfigMapName | (Not shown in Console) | The name of the status ConfigMap that CA writes. | Optional | cluster-autoscaler-status  
stderrthreshold | (Not shown in Console) | The log severity threshold, beyond which logs are sent to stderr. For example, if you set this to `error`, all logs with a severity higher than `error` are sent to stderr.  | Optional | info  
unremovableNodeRecheckTimeout | unremovableNodeRecheckTimeout | The timeout before we check again a node that couldn't be removed before. | Required | 5m  
v | (Not shown in Console) | The number for the verbosity of logging. | Optional | 0  
writeStatusConfigmap | (Not shown in Console) | Should CA write status information to a configmap. | Optional | true  
## Istio add-on configuration arguments 🔗 
When you enable the Istio cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
customizeConfigMap | customizeConfigMap |  If you want Oracle to manage Istio for you automatically, set **customizeConfigMap** to `false` (the default). If you want to customize Istio using istioctl (or another tool supported by Istio) and you want to retain the customizations when Oracle updates the add-on, set `customizeConfigMap` to `true`. | Required | `false` | `true`  
discovery.ContainerResources | discovery.ContainerResources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
discovery.EnvVariables  | discovery.EnvVariables |  List of Istio control plane discovery container environment variables, in JSON format. | Optional | null | `[{"name":"ISTIO_GPRC_MAXRECVMSGSIZE","value":"8388608"},{"name":"ISTIO_GPRC_MAXSTREAMS","value":"150000"}]`  
enableIngressGateway | enableIngressGateway | Enable Istio ingress gateway | Required | `false` | `true`  
istio-ingressgateway.Annotations | istio-ingressgateway.Annotations |  Annotations to pass to the Istio deployment.  For example, to specify the load balancer shape, or whether to create the load balancer as a network load balancer. For more annotations, see [Summary of Annotations for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer_topic-Summaryofannotations.htm#contengcreatingloadbalancer_topic_Summaryofannotations "Find out which annotations to use to define the Oracle Cloud Infrastructure load balancers and network load balancers that Kubernetes Engine \(OKE\) provisions for a Kubernetes service of type LoadBalancer."). JSON format in plain text or Base64 encoded. | Optional | `""` |  `{"service.beta.kubernetes.io/oci-load-balancer-shape":"400Mbps"}` `{"oci.oraclecloud.com/load-balancer-type": "nlb"}`  
istio-ingressgateway.HorizontalPodAutoscalerMinReplicas | istio-ingressgateway.HorizontalPodAutoscalerMinReplicas |  Minimum number of replicas of the Istio ingress gateway horizontal pod autoscaler. Must be an integer, with a value greater than zero. | Optional | null | `1`  
istio-ingressgateway.HorizontalPodAutoscalerMaxReplicas | istio-ingressgateway.HorizontalPodAutoscalerMaxReplicas |  Maximum number of replicas of the Istio ingress gateway horizontal pod autoscaler. Must be an integer, with a value greater than zero. | Optional | null | `3`  
istio-ingressgateway.PodDisruptionBudgetMinAvailable | istio-ingressgateway.PodDisruptionBudgetMinAvailable |  Minimum number or percentage of Istio ingress gateway pods available. | Optional | null |  `1` `10%`  
istiod.HorizontalPodAutoscalerMinReplicas | istiod.HorizontalPodAutoscalerMinReplicas |  Minimum number of replicas of the Istio controller. Must be an integer, with a value greater than zero. | Optional | null | `1`  
istiod.HorizontalPodAutoscalerMaxReplicas | istiod.HorizontalPodAutoscalerMaxReplicas |  Maximum number of replicas of the Istio controller. Must be an integer, with a value greater than zero. | Optional | null | `3`  
istiod.PodDisruptionBudgetMinAvailable | istiod.PodDisruptionBudgetMinAvailable |  Minimum number or percentage of Istio controller pods available. | Optional | null |  `1` `10%`  
profile | profile | Istio installation profile | Required | `"oke-default"` | `"oke-default"`  
## OCI Native Ingress Controller add-on configuration arguments 🔗 
When you enable the OCI native ingress controller cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
authSecretName | authSecretName | The name of the Kubernetes secret to use for user authentication when `authType` is set to `user`. | Optional | `""` | `oci-config`  
authType | authType | The authentication type that the OCI native ingress controller uses while making requests, as one of:
  * `instance` specifies instance principal (managed nodes only)
  * `user` specifies user principal (managed and virtual nodes)
  * `workloadIdentity` specifies workload identity (managed and virtual nodes)

| Optional | `instance` | `workloadIdentity`  
compartmentId | compartmentId | The OCID of the compartment in which the OCI native ingress controller is to create the OCI load balancer and certificate. | Required | `""` | `ocid1.compartment.oc1..aaaaaaaa______ddq`  
controllerClass | controllerClass | The name of the controller specified in your ingressClass that is to be managed by the oci-native-ingress-controller. | Optional | `oci.oraclecloud.com/native-ingress-controller` | `oci.oraclecloud.com/native-ingress-controller`  
leaseLockName | leaseLockName | The name of the lease to use for leader election. | Optional | `oci-native-ingress-controller` | `oci-native-ingress-controller`  
leaseLockNamespace | leaseLockNamespace | The namespace of the lease. | Optional | `native-ingress-controller-system` | `native-ingress-controller-system`  
loadBalancerSubnetId | loadBalancerSubnetId | The OCID of the load balancer's subnet. | Required | `""` | `ocid1.subnet.oc1.iad.aaaaaaaa______dba`  
logVerbosity | logVerbosity | The number for the verbosity of logging. | Optional | `4` | `2`  
metricsBackend | metricsBackend | The name of the metrics backend. | Optional | `prometheus` | `prometheus`  
metricsPort | metricsPort | The metrics port. | Optional | `2223` | `2223`  
oci-native-ingress-controller.ContainerResources | native-ingress-controller container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## Kubernetes Metrics Server add-on configuration arguments 🔗 
When you enable the Kubernetes Metrics Server cluster add-on, you can pass the following key/value pairs as arguments:
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
metrics-server.ContainerResources | metrics-server container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
## NVIDIA GPU Plugin add-on configuration arguments 🔗 
When you enable the NVIDIA GPU Plugin cluster add-on, you can pass the following key/value pairs as arguments.
Note that to ensure that workloads running on NVIDIA GPU worker nodes are not interrupted unexpectedly, we recommend that you choose the version of the NVIDIA GPU Plugin add-on to deploy, rather than specifying that you want Oracle to update the add-on automatically.
[Configuration Arguments Common to all Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
affinity | affinity |  A group of affinity scheduling rules. JSON format in plain text or Base64 encoded. | Optional | null | null  
nodeSelectors | node selectors |  You can use node selectors and node labels to control the worker nodes on which add-on pods run.  For a pod to run on a node, the pod's node selector must have the same key/value as the node's label. Set **nodeSelectors** to a key/value pair that matches both the pod's node selector, and the worker node's label. JSON format in plain text or Base64 encoded. | Optional | null | `{"foo":"bar", "foo2": "bar2"}`The pod will only run on nodes that have the `foo=bar` or `foo2=bar2` label.  
numOfReplicas | numOfReplicas | The number of replicas of the add-on deployment. | Required | `1`Creates one replica of the add-on deployment per cluster. | `2`Creates two replicas of the add-on deployment per cluster.  
rollingUpdate | rollingUpdate |  Controls the desired behavior of rolling update by maxSurge and maxUnavailable. JSON format in plain text or Base64 encoded. | Optional | null | null  
tolerations | tolerations |  You can use taints and tolerations to control the worker nodes on which add-on pods run. For a pod to run on a node that has a taint, the pod must have a corresponding toleration. Set **tolerations** to a key/value pair that matches both the pod's toleration, and the worker node's taint. JSON format in plain text or Base64 encoded. | Optional | null | `[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`Only pods that have this toleration can run on worker nodes that have the `tolerationKeyFoo=tolerationValBar:noSchedule` taint.  
topologySpreadConstraints | topologySpreadConstraints |  How to spread matching pods among the given topology. JSON format in plain text or Base64 encoded. | Optional | null | null  
[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm)
Key (API and CLI) | Key's Display Name (Console) | Description | Required/Optional | Default Value | Example Value  
---|---|---|---|---|---  
deviceIdStrategy | Device ID Strategy |  Which strategy to use for passing device IDs to the underlying runtime.  One of:
  * `uuid`
  * `index`

| Optional | `uuid`  
deviceListStrategy | Device List Strategy |  Which strategy to use for passing the device list to the underlying runtime.  Supported values:
  * `envvar`
  * `volume-mounts`
  * `cdi-annotations`
  * `cdi-cri`

Multiple values are supported, in a comma-separated list. | Optional | `envvar`  
driverRoot | Driver Root | The root path for the NVIDIA driver installation. | Optional | `/`  
failOnInitError | FailOnInitError |  Whether to fail the plugin if an error is encountered during initialization.  When set to `false`, blocks the plugin indefinitely instead of failing. | Optional | `true`  
gpu-device-plugin.ContainerResources | gpu-device-plugin container resources |  You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed. JSON format in plain text or Base64 encoded. | Optional | null | `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.  
migStrategy | MIG Strategy |  Which strategy to use for exposing MIG (Multi-Instance GPU) devices on GPUs that support it. One of:
  * `none`
  * `single`
  * `mixed`

| Optional | `none`  
passDeviceSpecs | Pass Device Specs | Whether to pass the paths and desired device node permissions for any NVIDIA devices being allocated to the container. | Optional | `false`  
useConfigFile | Use Config File from ConfigMap |  Whether to use a configuration file to configure the Nvidia Device Plugin for Kubernetes. The configuration file is derived from a ConfigMap. If set to `true`, you have to create a ConfigMap in the cluster, name the ConfigMap `nvidia-device-plugin-config`, and specify values for configuration arguments. See [Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons_configurationarguments_nvidiagpuplugin__example-configmap). The ConfigMap is referenced by the `nvidia-gpu-device-plugin` daemonset.  | Optional | `false`  
**Example of`nvidia-device-plugin-config` ConfigMap:**
```
apiVersion: v1
kind: ConfigMap
metadata: 
 name: nvidia-device-plugin-config 
 namespace: kube-system
data:
 config.yaml: |
  version: v1
  flags:
   migStrategy: "none"
   failOnInitError: true
   nvidiaDriverRoot: "/"
   plugin:
    passDeviceSpecs: false
    deviceListStrategy: envvar
    deviceIDStrategy: uuid
```

Was this article helpful?
YesNo

