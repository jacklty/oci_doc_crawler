Updated 2024-08-14
# Viewing Application Logs on Virtual Nodes
_Find out how to view the logs of applications running on virtual nodes in a Kubernetes cluster you've created using Kubernetes Engine (OKE)._
Having created a cluster with virtual nodes using Kubernetes Engine, you have two options to access the logs of applications running on the virtual nodes: 
  * View the stdout and stderr logs from application containers using the `kubectl logs` command.
  * Send application logs to a persistent log server for viewing.


## Viewing stdout and stderr logs using the kubectl logs command
To view the stdout and stderr logs from an application's containers using the `kubectl logs` command:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. In a terminal window, run the `kubectl logs` command by entering:```
kubectl logs <pod-name>
```

For example:
```
kubectl logs nginx
```

When the pod contains more than one container, specify the container for which you want to view the logs. For example, if the `myapp` pod has two containers called `nginx` and `logging` and you want to display the logs of the `logging` container, enter:
```
kubectl logs myapp logging
```



## Sending logs to a persistent log server
You can send the logs of applications running on virtual nodes to a remote log server such as OpenSearch, and view the logs on that server. Since virtual nodes do not support the Kubernetes daemonset, you cannot run a logging agent at the node level. Instead, you can run a lightweight logging agent as a sidecar for each of the application's pods. You can use any logging agent that can run as a sidecar on a Kubernetes pod, such as [Fluent Bit](https://github.com/fluent/fluent-bit).
For example, to run Fluent Bit as a sidecar on a pod to send application logs to a remote OpenSearch log server: 
  1. Create a Kubernetes ConfigMap per cluster or per namespace, specifying the Fluent Bit configuration settings to use. In particular, note that you must specify the remote log server's IP address, port number, and authentication parameters. 
For example:
```
apiVersion: v1
kind: ConfigMap
metadata:
 name: fluentbit-config
data:
 fluent-bit.conf: |
  [SERVICE]
    flush    1
    daemon    Off
 
  [INPUT]
    Name       tail
    Path       /mnt/log/*
 
  [OUTPUT]
    name opensearch
    match *
    host <ip-address>
    port <port-number>
    tls On
    HTTP_User <username>
    HTTP_Passwd <example-password>
    Index fluent-bit
    Suppress_Type_Name On
```

where:
     * `host <ip-address>` specifies the IP address of the Opensearch server.
     * `port <port-number>` specifies the port of the Opensearch server (9200 by default).
     * `HTTP_User <username>` specifies the username for the Opensearch server.
     * `HTTP_Passwd <example-password>` specifies the password for the Opensearch server.
  2. Add a Fluent Bit sidecar to each pod. Note that you must configure all pods with a Fluent Bit sidecar to ensure that application logs are sent to the persistent log destination.
    1. In the `volumes` section of each pod spec, specify:
       * An emptyDir where application logs are written, as follows:```
- name: logs
 emptyDir: {}
```

       * A reference to the ConfigMap you created previously, as follows:```
- name: fluentbit-config
 configMap:
  name: fluentbit-config
```

    2. In the `containers` section of each pod spec, you must specify that the logging container:
       * Uses the `fluent/fluent-bit` image.
       * Mounts the `logs` emptyDir and the `fluentbit-config` ConfigMap.
For example:
```
- name: logging
 image: fluent/fluent-bit
 resources:
  requests:
   cpu: 100m
   memory: 50Mi
 volumeMounts:
 - name: logs
  mountPath: /mnt/log
 - name: fluentbit-config
  mountPath: /fluent-bit/etc 
```

Here's an example of a complete pod specification:
```
apiVersion: v1
kind: Pod
metadata:
 name: date-logging
spec:
 containers:
 - name: date
  image: busybox
  resources:
   requests:
    cpu: 500m
    memory: 200Mi
  command: ["sh", "-c"]
  args:
   - while [ 1 ]; do
    echo "Writing the date in /mnt/log/date.log";
    date >> /mnt/log/date.log;
    sleep 10;
    done
  volumeMounts:
  - name: logs
   mountPath: /mnt/log
 - name: logging
  image:
   resources:
   requests:
    cpu: 100m
    memory: 50Mi
  volumeMounts:
  - name: logs
   mountPath: /mnt/log
  - name: fluentbit-config
   mountPath: /fluent-bit/etc
 volumes:
 - name: logs
  emptyDir: {}
 - name: fluentbit-config
  configMap:
   name: fluentbit-config
```



Was this article helpful?
YesNo

