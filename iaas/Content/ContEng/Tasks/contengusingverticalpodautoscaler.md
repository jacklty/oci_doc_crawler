Updated 2024-08-14
# Using the Kubernetes Vertical Pod Autoscaler
_Find out how to use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in pods on a cluster you've created using Kubernetes Engine (OKE)._
**Note** You cannot use the Kubernetes Vertical Pod Autoscaler with virtual node pools.
You can use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in a deployment's pods. The Vertical Pod Autoscaler can improve cluster resource utilization by:
  * Setting the requests automatically based on usage to make sure the appropriate resource amount is available for each pod.
  * Maintaining ratios between limits and requests that were specified in containers' initial configurations.
  * Scaling down pods that are over-requesting resources, based on their usage over time.
  * Scaling up pods that are under-requesting resources, based on their usage over time.


The Vertical Pod Autoscaler has three components:
  * [Recommender](https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/pkg/recommender/README.md): Monitors the current and past resource consumption and provides recommended CPU and memory request values for a container. 
  * [Updater](https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/pkg/updater/README.md): Checks for pods with incorrect resources and deletes them, so that the pods can be recreated with the updated request values. 
  * [Admission Plugin](https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/pkg/admission-controller/README.md): Sets the correct resource requests on new pods (that is, pods just created or recreated by their controller due to changes made by the Updater).


For more information, see [Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) and [Managing Resources for Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the Kubernetes documentation.
You configure the Vertical Pod Autoscaler using the `VerticalPodAutoscaler` custom resource definition object. The `VerticalPodAutoscaler` object enables you to specify the pods to vertically autoscale, and which resource recommendations to apply (if any). For more information, see [VerticalPodAutoscaler](https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/pkg/apis/autoscaling.k8s.io/v1/types.go) and [Custom Resource Definition object](https://kubernetes.io/docs/concepts/api-extension/custom-resources/) in the Kubernetes documentation. 
The Vertical Pod Autoscaler requires the installation of a metrics source, such as the Kubernetes Metrics Server, in the cluster. For more information, see [Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm#Deploying_Kubernetes_Metrics_Server_Using_Kubectl "Find out how to deploy the Kubernetes Metrics Server as a standalone program or as a cluster add-on, on a cluster you've created using Kubernetes Engine \(OKE\).").
## Overriding Limit Ranges
The Vertical Pod Autoscaler attempts to make recommendations within the minimum and maximum values specified by a limit range, if one has been defined. However, if the applicable limit range conflicts with the values specified in the `resourcePolicy` section of the `VerticalPodAutoscaler` manifest, the Vertical Pod Autoscaler gives priority to the resource policy and makes recommendations accordingly (even if the values fall outside the limit range). For more information, see [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/) and [Resource Policy Overriding Limit Range](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler#resource-policy-overriding-limit-range) in the Kubernetes documentation. 
## Creating Recommendations without Applying them
You can use the Vertical Pod Autoscaler to create and apply recommendations, or simply to create recommendations (without updating pods). To simply create recommendations without applying them, set `updateMode: "Off"` in the `updatePolicy` section of the `VerticalPodAutoscaler` manifest. 
When pods are created, the Vertical Pod Autoscaler analyzes the CPU and memory needs of the containers and records those recommendations in its `Status` field. The Vertical Pod Autoscaler does not take any action to update the resource requests for the running containers.
## Excluding Specific Containers
You can use the Vertical Pod Autoscaler to create and apply recommendations to all the containers in a pod, or you can selectively exclude particular containers. To turn off recommendations for a particular container, in the`           resourcePolicy` section of the `VerticalPodAutoscaler` manifest, specify a `containerName` and set `mode:           "Off"` in the `containerPolicies` section.
## Notes about the Vertical Pod Autoscaler
Note the following:
  * Currently, you are recommended not to use the Vertical Pod Autoscaler with the Horizontal Pod Autoscaler on CPU or memory utilization metrics. However, note that you can use the Vertical Pod Autoscaler with the Horizontal Pod Autoscaler on custom and external metrics. See [Support for custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-custom-metrics) in the Kubernetes documentation.
  * The Vertical Pod Autoscaler recommendations might exceed available resources (for example, node size, available size, available quota). Note that applying the recommendations might cause pods to go into a pending status.
  * Whenever the Vertical Pod Autoscaler updates pod resources, the pod is recreated, which causes all running containers to be restarted. Note that the pod might be recreated on a different node.
  * You can use the Kubernetes Vertical Pod Autoscaler with managed node pools, but not with virtual node pools.


## Working with the Vertical Pod Autoscaler 🔗 
The instructions below walk you through deploying the Vertical Pod Autoscaler on a cluster. They describe how to:
  * Verify that the Kubernetes Metrics Server has been installed on a cluster.
  * Download and deploy the Vertical Pod Autoscaler.
  * Deploy a sample application.
  * View the scaling operation in action.
  * View the recommendation.
  * Clean up, by removing the sample application and the Vertical Pod Autoscaler.


### Step 1: Verify the Kubernetes Metrics Server Installation
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Confirm that the Kubernetes Metrics Server has been deployed successfully on the cluster and is available by entering:
Command
CopyTry It
```
kubectl -n kube-system get deployment/metrics-server
```

If the command returns a `Not Found` error, then you must deploy the Kubernetes Metrics Server on the cluster before proceeding. See [Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm#Deploying_Kubernetes_Metrics_Server_Using_Kubectl "Find out how to deploy the Kubernetes Metrics Server as a standalone program or as a cluster add-on, on a cluster you've created using Kubernetes Engine \(OKE\).").


### Step 2: Download and Deploy the Vertical Pod Autoscaler
  1. Download the Vertical Pod Autoscaler source code from GitHub. For example, by entering:
Command
CopyTry It
```
git clone -b vpa-release-0.8 https://github.com/kubernetes/autoscaler.git
```

  2. Change to the `vertical-pod-autoscaler` directory:
Command
CopyTry It
```
cd autoscaler/vertical-pod-autoscaler
```

  3. If you have previously deployed the Vertical Pod Autoscaler, delete it by entering:
Command
CopyTry It
```
./hack/vpa-down.sh
```

  4. Deploy the Vertical Pod Autoscaler by entering: 
Command
CopyTry It
```
./hack/vpa-up.sh
```

  5. Verify that the Vertical Pod Autoscaler pods have been created successfully by entering:
Command
CopyTry It
```
kubectl get pods -n kube-system
```

The output from the above command shows the pods:
```
vpa-admission-controller-59d9965cfb-bzs8l 1/1 Running 0 6m34s
vpa-recommender-5bcb58569-mqdds 1/1 Running 0 6m43s
vpa-updater-5979cbf757-scw2d 1/1 Running 0 6m46s
```

Note that you will probably see different names and numbers.


### Step 3: Deploy the Sample Application
  1. Deploy the sample hamster application to create a deployment and a corresponding Vertical Pod Autoscaler by entering:
Command
CopyTry It
```
kubectl apply -f examples/hamster.yaml
```

The output from the above command confirms the deployment and creation:
```
verticalpodautoscaler.autoscaling.k8s.io/hamster-vpa created
deployment.apps/hamster created
```

Deploying the hamster application creates a deployment with two pods and a Vertical Pod Autoscaler pointing at the deployment. 
  2. Verify that the hamster pods have been created successfully by entering:
Command
CopyTry It
```
kubectl get pods -l app=hamster
```

The output from the above command confirms the creation:
```
NAME           READY STATUS RESTARTS AGE
hamster-7cbfd64f57-mqqnk 1/1  Running 0    54s
hamster-7cbfd64f57-rq6wv 1/1  Running 0    55s
```

Note that you will probably see different names for the hamster pods.
  3. View the CPU and memory reservations using the `kubectl describe             pod` command and one of the hamster pod names returned in the previous step. For example:
Command
CopyTry It
```
kubectl describe pod hamster-7cbfd64f57-rq6wv
```

Note that the above command is an example only. You must use one of the hamster pod names that was returned when you ran the `kubectl get pods -l               app=hamster` command in the previous step.
In the requests section of the output, you can see the pod's current CPU and memory reservations. For example: 
```
Requests:
   cpu:    100m
   memory:   50Mi
```

The Vertical Pod Autoscaler (specifically, the Recommender) analyzes the pods and observes their behavior to determine whether these CPU and memory reservations are appropriate. Note that you might see different CPU and memory reservations.
The reservations are not sufficient because the sample hamster application is deliberately under-resourced. Each pod runs a single container that:
     * requests 100 millicores, but tries to utilize more than 500 millicores
     * reserves much less memory than it needs to run


### Step 4: View the Scaling Operation
Having analyzed the original pods in the sample hamster application and determined that the CPU and memory reservations are inadequate, the Vertical Pod Autoscaler (specifically the Updater) relaunches the pods with different values as proposed by the Recommender. Note that the Vertical Pod Autoscaler does not modify the template in the deployment, but updates the actual requests of the pods.
  1. Monitor the pods in the sample hamster application, and wait for the Updater to start a new hamster pod with a new name, by entering:
Command
CopyTry It
```
kubectl get --watch pods -l app=hamster
```

  2. When you see that a new hamster pod has started, view its CPU and memory reservations using the `kubectl describe pod` command and the pod's name. For example:
Command
CopyTry It
```
kubectl describe pod hamster-7cbfd64f57-wmg4
```

In the requests section of the output, you can see the new pod's CPU and memory reservations: 
```
  Requests:
   cpu:    587m
   memory:   262144k
```

In the above example, notice that the CPU reservation has increased to 587 millicores and the memory reservation has increased to 262,144 Kilobytes. The original pod was under-resourced and the Vertical Pod Autoscaler has corrected the original reservations with more appropriate values. Note that you might see different CPU and memory reservations.


### Step 5: View the Recommendation
View the recommendations made by the Vertical Pod Autoscaler (specifically, by the Recommender) by entering:
Command
CopyTry It
```
kubectl describe vpa/hamster-vpa
```

The output from the above command shows the recommendations:
```
Name:     hamster-vpa
Namespace:  default
Labels:    <none>
Annotations: kubectl.kubernetes.io/last-applied-configuration:
        {"apiVersion":"autoscaling.k8s.io/v1beta2","kind":"VerticalPodAutoscaler","metadata":{"annotations":{},"name":"hamster-vpa","namespace":"d...
API Version: autoscaling.k8s.io/v1
Kind:     VerticalPodAutoscaler
Metadata:
 Creation Timestamp: 2020-09-22T18:08:09Z
 Generation:     27
 Resource Version:  19466955
 Self Link:      /apis/autoscaling.k8s.io/v1/namespaces/default/verticalpodautoscalers/hamster-vpa
 UID:         689cee90-6fed-404d-adf9-b6fa8c1da660
Spec:
 Resource Policy:
  Container Policies:
   Container Name: *
   Controlled Resources:
    cpu
    memory
   Max Allowed:
    Cpu:   1
    Memory: 500Mi
   Min Allowed:
    Cpu:   100m
    Memory: 50Mi
 Target Ref:
  API Version: apps/v1
  Kind:     Deployment
  Name:     hamster
 Update Policy:
  Update Mode: Auto
Status:
 Conditions:
  Last Transition Time: 2020-09-22T18:10:10Z
  Status:        True
  Type:         RecommendationProvided
 Recommendation:
  Container Recommendations:
   Container Name: hamster
   Lower Bound:
    Cpu:   519m
    Memory: 262144k
   Target:
    Cpu:   587m
    Memory: 262144k
   Uncapped Target:
    Cpu:   587m
    Memory: 262144k
   Upper Bound:
    Cpu:   1
    Memory: 500Mi
Events:     <none>
```

Note that you might see different recommendations.
### Step 6: Clean Up
  1. Remove the sample application by entering: 
Command
CopyTry It
```
kubectl delete -f examples/hamster.yaml
```

  2. In the `vertical-pod-autoscaler` directory, delete the Vertical Pod Autoscaler deployment by entering: 
Command
CopyTry It
```
./hack/vpa-down.sh
```



Was this article helpful?
YesNo

