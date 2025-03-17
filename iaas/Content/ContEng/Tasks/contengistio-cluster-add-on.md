Updated 2024-08-14
# Working with Istio as a Cluster Add-on
_Find out how to install, configure, and use Istio as a cluster add-on to simplify traffic management, security, connections, and observability in clusters you've created with Kubernetes Engine (OKE)._
Using Istio as a cluster add-on (the 'Istio add-on') rather than as a standalone program simplifies configuration and ongoing maintenance. You can more simply:
  * Enable or disable Istio.
  * Opt into, and out of, automatic version updates by Oracle.
  * Select Istio add-on versions.
  * Manage add-on specific customizations using approved key/value pair configuration arguments. 


When you deploy Istio as a cluster add-on using Kubernetes Engine, you can optionally create an Istio ingress gateway to route incoming HTTP and HTTPS requests. Alternatively, you can use other supported ingresses to route traffic to the appropriate service running on the cluster. Be aware that the accessibility of the Istio ingress gateway depends on the type of the load balancer subnet (public or private) specified for the cluster.
In the case of the Istio add-on, you use approved key/value pair configuration arguments to make add-on specific customizations for mesh-wide configuration parameters (see [Istio add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_Istio)). For other configuration tasks, such as managing mesh resources, you use istioctl (the Istio command line tool), or other tools supported by Istio. If you configure the Istio add-on using the approved arguments and you want to retain the customizations when the add-on version is updated automatically by Oracle, set the `customizeConfigMap` configuration argument to `true`. If you do not set the `customizeConfigMap` configuration argument to `true`, the customizations are discarded when Oracle updates the add-on. Any customizations you make using istioctl (or another tool supported by Istio) are always discarded when Oracle updates the add-on.
If you use Helm and Helm charts to configure and deploy Kubernetes applications, note that Helm can only update or delete resources that it has created. Therefore, to enable Helm to manage the Istio add-on:
  * Use Helm charts to generate the istio and istio-sidecar-injector configmaps.
  * Set the `customizeConfigMap` configuration argument to `true` when deploying the Istio add-on.


If you decide to have Oracle automatically update the Istio add-on, Oracle will perform an in-place upgrade when new Istio versions become available. During the upgrade, Oracle automatically updates the Istio control plane (istiod) and the ingress gateway to the newer version. Note that Oracle does not automatically update any Istio data plane sidecars, so these sidecars remain at the old version. It is your responsibility to manually update the Istio data plane by restarting any pods with Istio sidecars using the `kubectl rollout restart deployment` command. Even though the Istio control plane is backwardly compatible with older sidecar versions, if your priority is to ensure zero downtime, we recommend that you manually upgrade Istio yourself rather than having Oracle automatically update the Istio add-on for you. See [In-place Upgrades](https://istio.io/latest/docs/setup/upgrade/in-place/) in the Istio documentation. 
These sections describe how to work with the Istio add-on to manage communication and networking between services:
  * [Deploying the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on)
  * [Updating the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Updating_Cluster_Autoscaler_Add-on)
  * [Disabling (and Removing) the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Disabling_Removing_Istio_Add-on)


Note that service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).
Also note that you cannot use the Istio add-on with clusters that already have Istio installed as a standalone program, nor in clusters that have Oracle Cloud Infrastructure Service Mesh installed. 
**Note**
You can use Istio with managed node pools, but not with virtual node pools.
## Deploying the Istio Add-on 🔗 
The instructions in the steps below describe how to deploy Istio service mesh as a cluster add-on (the 'Istio add-on') to simplify traffic management, security, connections, and observability in clusters you've created with Kubernetes Engine:
  * [Step 1: Create the Istio add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on__section_create-config-file)
  * [Step 2: Deploy the Istio add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on__section_deploy-istio)
  * [Step 3: Enable Envoy sidecar injection](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on__section_enable-envoy-injection)
  * [Step 4: Deploy an application and observe Envoy sidecar containers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on__section_deploy-application-envoy)


For a worked example, see [Example: Deploying Istio as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on-Example).
### Step 1: Create the Istio add-on configuration file 🔗 
**Note**
These instructions describe how to create an Istio add-on configuration file to enable you to deploy the Istio add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the Istio add-on, in which case you specify configuration arguments in the UI. For more information about deploying the Istio add-on using the Console, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called `enableistio.json`) containing the following:
```
{
 "addonName": "Istio",
 "configurations": [
 ]
}
```

This content is sufficient to enable the Istio add-on.
  2. (Optional) In the `enableistio.json` file, specify whether to install the Istio ingress gateway, as follows:
     * To install the Istio ingress gateway, update the `enableistio.json` file as follows:```
{
 "addonName": "Istio",
 "configurations": [
  {
   "key": "enableIngressGateway",
   "value": "true"
  }
 ]
}
```

     * If you don't want to install the Istio ingress gateway, update the `enableistio.json` file as follows:```
{
 "addonName": "Istio",
 "configurations": [
  {
   "key": "enableIngressGateway",
   "value": "false"
  }
 ]
}
```

Note that if you don't include `enableIngressGateway` in the configuration file, the default behavior is not to install the Istio ingress gateway (equivalent to setting `enableIngressGateway` to `false`)
  3. (Optional) In the `enableistio.json` file you created, specify other configuration arguments to customize the Istio add-on. For information about the configuration arguments you can set, see [Istio add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_Istio).
  4. (Optional) If you want to retain customizations you make to the Istio add-on if the add-on version is updated automatically by Oracle, set the `customizeConfigMap` argument to `true`. For example:
     * To install the Istio ingress gateway and retain customizations, update the `enableistio.json` file as follows:```
{
 "addonName": "Istio",
 "configurations": [
  {
   "key": "enableIngressGateway",
   "value": "true"
  },
  {
   "key": "customizeConfigMap",
   "value": "true"
  }
 ]
}
```

     * If you don't want to install the Istio ingress gateway but you do want to retain customizations, update the `enableistio.json` file as follows:```
{
 "addonName": "Istio",
 "configurations": [
  {
   "key": "enableIngressGateway",
   "value": "false"
  },
  {
   "key": "customizeConfigMap",
   "value": "true"
  }
 ]
}
```

Note that if you don't include `customizeConfigMap` in the configuration file, the default behavior is to discard customizations if the add-on version is updated automatically by Oracle (equivalent to setting `customizeConfigMap` to `false`)
  5. Save and close the `enableistio.json` file.


### Step 2: Deploy the Istio add-on on the cluster and confirm successful deployment 🔗 
**Note**
These instructions describe how to deploy the Istio add-on using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Confirm that the Istio add-on has not already been installed on the cluster by entering:```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

where `<cluster-ocid>` is the OCID of the cluster on which you want to deploy the Istio add-on.
  3. Deploy the Istio add-on on the cluster by entering:
```
oci ce cluster install-addon --addon-name Istio --cluster-id <cluster-ocid> --from-json file://./<path-to-config-file>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to deploy the Istio add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Istio add-on configuration file you created earlier. For example, `--from-json file://./enableistio.json`
For example:
```
oci ce cluster install-addon --addon-name Istio --from-json file://./enableistio.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to deploy the Istio add-on.
  4. Confirm successful deployment of the Istio add-on (and the Istio ingress gateway, if you specified it in the Istio add-on configuration file), as follows:
    1. Confirm that the Istio add-on has been installed on the cluster by entering:```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

Assuming successful deployment, the output shows the Istio add-on with a lifecycle-state of ACTIVE. For example:
```
{
 "data": [
  {
   "addon-error": null,
   "current-installed-version": "v1.19.0",
   "lifecycle-state": "ACTIVE",
   "name": "Istio",
   "time-created": "2023-11-06T11:21:11+00:00",
   "version": null
  }
 ]
}
```

    2. Confirm that the istiod pod (the Istio control plane), and also the istio-ingressgateway pod if you specified it in the configuration file, are running in the istio-system namespace by entering:```
kubectl get pods -n istio-system
```

Assuming successful deployment, the output shows the pods with a status of Running. For example:
```
NAME                  READY  STATUS  RESTARTS  AGE
istio-ingressgateway-df7d86548-n2vxr  1/1   Running  0     102s
istiod-65d95bd5f9-vb2qk        1/1   Running  0     101s
```

    3. If you specified the Istio ingress gateway in the configuration file, confirm that the istio-ingressgateway service has been deployed successfully by entering:```
kubectl get svc istio-ingressgateway -n istio-system
```

Assuming successful deployment, the output shows the istio-ingressgateway service as a service of type LoadBalancer and (if the cluster's load balancer subnet is public) with a publicly accessible IP address. For example:
```
NAME          TYPE      CLUSTER-IP   EXTERNAL-IP   PORT(S)                   AGE
istio-ingressgateway  LoadBalancer  10.96.31.174  <EXTERNAL-IP>  15021:30089/TCP,80:31662/TCP,443:32217/TCP  2m50s
```



### Step 3: Enable Envoy sidecar injection 🔗 
To enable Istio to inject the Envoy sidecar into each service to provide communication, configuration, and security:
  1. Create the namespace in which to deploy applications (if the namespace doesn't exist already) by entering:```
kubectl create namespace <namespace-name>
```

  2. Make the namespace in which to deploy applications the default namespace by entering:```
kubectl config set-context --current --namespace=<namespace-name>
```

  3. Confirm that the namespace in which to deploy applications is the default namespace by entering:```
kubectl config view --minify | grep namespace
```

  4. Add the `istio-injection=enabled` label to the namespace to automatically install the Envoy sidecar into any new application pods deployed in the namespace by entering:```
kubectl label namespace <namespace-name> istio-injection=enabled
```

  5. Confirm that the namespace is labelled correctly by entering:```
kubectl get namespace -L istio-injection
```



### Step 4: Deploy an application and observe Envoy sidecar containers 🔗 
To confirm that Istio is being used to provide communication, configuration, and security for an application:
  1. Deploy the application. For example, by entering:```
kubectl apply -f <manifest-name>
```

  2. Confirm that the application's services were created successfully by entering:```
kubectl get services
```

  3. Confirm that the application's pods have a status of Running by entering:```
kubectl get pods
```

The output shows that each application pod has two containers. For each pod, one container is the application container, and the other container is the Envoy sidecar that Istio injected.
  4. Confirm that one of the application's pods has two containers (one of which is the application container, and the other is the Envoy sidecar injected by Istio) by entering:```
kubectl get pods <application-pod-name> -o jsonpath='{.spec.containers[*].name}'
```

Note that applications aren't accessible from outside the cluster by default after enabling the ingress gateway. For an example of how to make an application accessible, see [Example: Deploying Istio as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on-Example).


### Example: Deploying Istio as a Cluster Add-on 🔗 
In this example, you install the Istio add-on and the Istio ingress gateway on a cluster you've created with Kubernetes Engine. Having installed the Istio add-on and ingress gateway, you deploy Istio's sample Bookinfo application and make the application accessible from outside the cluster:
  1. For convenience, set an environment variable named CLUSTER_ID to the value of the cluster's OCID by entering:```
export CLUSTER_ID=<cluster-ocid>
```

  2. Create a JSON file named `enableistio-ig.json` that contains the following:```
{
 "addonName": "Istio",
 "configurations": [
  {
   "key": "enableIngressGateway",
   "value": "true"
  }
 ]
}
```

This configuration file installs the Istio add-on and the Istio ingress gateway.
  3. Install the Istio add-on and the Istio ingress gateway on the cluster by entering:```
oci ce cluster install-addon --addon-name Istio --cluster-id $CLUSTER_ID --from-json file://./enableistio-ig.json
```

A work request is created to install the Istio add-on.
  4. Verify successful installation of the Istion add-on and the Istio ingress gateway:
    1. Confirm that the Istio add-on has been installed successfully by entering:```
oci ce cluster list-addons --cluster-id $CLUSTER_ID
```

Assuming successful deployment, the output shows the Istio add-on with a lifecycle-state of ACTIVE. For example, the following outputs shows the Istio add-on, along with a number of essential cluster add-ons:
```
{
 "data": [
  {
   "addon-error": null,
   "current-installed-version": "v1.10.1-multiarch-7",
   "lifecycle-state": "ACTIVE",
   "name": "CoreDNS",
   "time-created": "2023-11-06T10:35:26+00:00",
   "version": null
  },
  {
   "addon-error": null,
   "current-installed-version": "v1.19.0",
   "lifecycle-state": "ACTIVE",
   "name": "Istio",
   "time-created": "2023-11-06T11:21:11+00:00",
   "version": null
  },
  {
   "addon-error": null,
   "current-installed-version": "v1.27.2-oke.0.2.20-multiarch-98",
   "lifecycle-state": "ACTIVE",
   "name": "KubeProxy",
   "time-created": "2023-11-06T10:35:26+00:00",
   "version": null
  },
  {
   "addon-error": null,
   "current-installed-version": "v2.0.1",
   "lifecycle-state": "ACTIVE",
   "name": "OciVcnIpNative",
   "time-created": "2023-11-06T10:35:26+00:00",
   "version": null
  }
 ]
}
```

    2. Confirm that the Istio control plane (istiod) pod and the istio-ingressgateway pod are both running in the istio-system namespace by entering:```
kubectl get pods -n istio-system
```

Assuming successful deployment, the output shows both pods with a status of Running. For example:
```
NAME                  READY  STATUS  RESTARTS  AGE
istio-ingressgateway-df7d86548-n2vxr  1/1   Running  0     102s
istiod-65d95bd5f9-vb2qk        1/1   Running  0     101s
```

    3. Confirm that the istio-ingressgateway service has been deployed successfully by entering:```
kubectl get svc istio-ingressgateway -n istio-system
```

Assuming successful deployment, the output shows the istio-ingressgateway service as a service of type LoadBalancer and (if the cluster's load balancer subnet is public) with a publicly accessible IP address. For example:
```
NAME          TYPE      CLUSTER-IP   EXTERNAL-IP   PORT(S)                   AGE
istio-ingressgateway  LoadBalancer  10.96.31.174  <EXTERNAL-IP>  15021:30089/TCP,80:31662/TCP,443:32217/TCP  2m50s
```

  5. Create a new namespace in which to deploy the Bookinfo sample application: 
    1. Create the `bookinfo` namespace by entering:```
kubectl create namespace bookinfo
```

    2. Make the `bookinfo` namespace the default namespace by entering:```
kubectl config set-context --current --namespace=bookinfo
```

    3. Confirm that bookinfo is the default namespace by entering:```
kubectl config view --minify | grep namespace
```

  6. Add the `istio-injection=enabled` label to the bookinfo namespace to automatically install the Envoy sidecar into any new application pods deployed in the namespace:
    1. Add the label to the bookinfo namespace by entering:```
kubectl label namespace bookinfo istio-injection=enabled
```

    2. Confirm that the bookinfo namespace is labelled correctly by entering:```
kubectl get namespace -L istio-injection
```

  7. Deploy the Bookinfo sample application by entering:```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/bookinfo/platform/kube/bookinfo.yaml
```

Assuming successful deployment, the output shows several deployments and services created on the cluster, as follows:
```
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
```

  8. Verify successful deployment of the Bookinfo sample application:
    1. Confirm that services were created successfully by entering:```
kubectl get services
```

Assuming successful deployment, the output shows the services created on the cluster, similar to the following:
```
NAME     TYPE    CLUSTER-IP   EXTERNAL-IP  PORT(S)  AGE
details    ClusterIP  10.96.72.219  <none>    9080/TCP  54s
productpage  ClusterIP  10.96.65.83  <none>    9080/TCP  54s
ratings    ClusterIP  10.96.101.51  <none>    9080/TCP  54s
reviews    ClusterIP  10.96.14.9   <none>    9080/TCP  54s
```

    2. Confirm that all the pods have the status of Running by entering:```
kubectl get pods
```

Assuming successful deployment, the output shows the pods that are running, similar to the following:
```
NAME               READY  STATUS  RESTARTS  AGE
details-v1-5f4d584748-hcm9t   2/2   Running  0     81s
productpage-v1-564d4686f-48lpw  2/2   Running  0     80s
ratings-v1-686ccfb5d8-bpl8t   2/2   Running  0     81s
reviews-v1-86896b7648-6c8d4   2/2   Running  0     81s
reviews-v2-b7dcd98fb-fsv7c    2/2   Running  0     81s
reviews-v3-5c5cc7b6d-qgrv2    2/2   Running  0     81s
```

The output shows that each application pod has two containers. For each pod, one container is the application container, and the other container is the Envoy sidecar injected by Istio.
    3. Confirm that the `ratings` pod has two containers (one of which is the application container, and the other is the Envoy sidecar injected by Istio). For example, by entering:```
kubectl get pods ratings-v1-686ccfb5d8-bpl8t -o jsonpath='{.spec.containers[*].name}'
```

The output shows two containers, the application container (ratings) and the Envoy sidecar container injected by Istio (istio-proxy):
```
ratings istio-proxy
```

    4. Confirm that the application is running by sending a curl command from a pod:```
kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

Note that the Bookinfo sample application is not yet accessible from outside the cluster, even after enabling the ingress gateway. Note also that the accessibility of the Istio ingress gateway depends on the type of the load balancer subnet (public or private) specified for the cluster.
  9. Make the Bookinfo sample application accessible from outside the cluster:
    1. Map the sample deployment's ingress to the Istio ingress gateway by entering:```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/bookinfo/networking/bookinfo-gateway.yaml
```

The output shows that the Kubernetes Gateway and VirtualService resources have been created:
```
gateway.networking.istio.io/bookinfo-gateway created
virtualservice.networking.istio.io/bookinfo created
```

  10. Verify that the Bookinfo sample application is accessible and using the Istio ingress gateway:
    1. Set environment variables for the ingress host and the ingress port by entering:```
export INGRESS_NAME=istio-ingressgateway
```
```
export INGRESS_NS=istio-system
```
```
export INGRESS_HOST=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```
```
export INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
```

    2. Confirm that the Bookinfo sample application is accessible and using the Istio ingress gateway by entering:```
curl -s "http://${INGRESS_HOST}:${INGRESS_PORT}/productpage" | grep -o "<title>.*</title>"
```

Assuming successful deployment, the output shows the services created on the cluster, similar to the following:
```
<title>Simple Bookstore App</title>
```

    3. View the Bookinfo web page in a browser by opening the following URL:```
http://${INGRESS_HOST}:${INGRESS_PORT}/productpage
```

    4. In the browser, refresh the Bookinfo web page several times to see different versions of reviews shown on the page.
  11. (Optional) Having completed the example, you can now delete the resources that you created: 
    1. Delete the Bookinfo sample application by entering:```
kubectl delete -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/bookinfo/platform/kube/bookinfo.yaml
```

    2. Disable (and optionally remove) the Istio add-on using the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command, by entering:
Copy
```
oci ce cluster disable-addon --addon-name Istio --cluster-id $CLUSTER_ID --is-remove-existing-add-on <true|false>
```

where `--is-remove-existing-add-on <true|false>` specifies either to completely remove the Istio add-on (when set to `true`), or to not remove the add-on but simply disable it and not use it (when set to `false`). If you disable the add-on, Oracle no longer updates the add-on version automatically when new versions become available. 
For example:
Copy
```
oci ce cluster disable-addon --addon-name Istio --cluster-id $CLUSTER_ID --is-remove-existing-add-on true
```

A work request is created to disable (and optionally remove) the Istio add-on.
    3. Remove Istio CustomResourceDefinitions (CRDs), which aren't deleted by default, by entering:```
kubectl delete crd $(kubectl get crd -A | grep "istio.io" | awk '{print $1}')
```

    4. Remove Istio mesh resources (such as the Kubernetes Gateway and VirtualService resources), which aren't managed by the Istio add-on, by entering:```
kubectl delete -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/bookinfo/networking/bookinfo-gateway.yaml
```



## Updating the Istio Add-on 🔗 
**Note**
These instructions describe how to update the Istio add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Open the Istio add-on configuration file in a suitable editor.
  2. Add, remove, or change configuration arguments in the configuration file as required. For information about the arguments you can set, see [Istio add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_Istio).
  3. If you have specified that you want Oracle to automatically update the Istio add-on version and you want to retain the configuration changes, set the `customizeConfigMap` configuration argument to `true` (if it is not already set).
  4. Update the Istio add-on using the [oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html) command, by entering:
Copy
```
oci ce cluster update-addon --addon-name Istio --from-json file://<path-to-config-file> --cluster-id <cluster-ocid>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to update the Istio add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Istio add-on configuration file to use when updating the add-on. For example, `--from-json file://./istio-add-on.json`
For example:
Copy
```
oci ce cluster update-addon --addon-name Istio --from-json file://./istio-add-on.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to update the Istio add-on.
  5. (Optional) View the status of the istiod and istio-ingressgateway pods to observe progress, by entering:```
kubectl get pods -n istio-system
```



## Disabling (and Removing) the Istio Add-on 🔗 
**Note**
These instructions describe how to disable and remove the Istio add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#disable-add-on "Find out how to disable \(and remove\) a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Disable (and optionally remove) the Istio add-on using the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command, by entering:
Copy
```
oci ce cluster disable-addon --addon-name Istio --cluster-id <cluster-ocid> --is-remove-existing-add-on <true|false>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to disable (and optionally remove) the Istio add-on.
     * `--is-remove-existing-add-on <true|false>` specifies either to completely remove the Istio add-on (when set to `true`), or to not remove the add-on but simply disable it and not use it (when set to `false`). If you disable the Istio add-on, Oracle no longer updates the add-on version automatically when new versions become available. 
For example:
Copy
```
oci ce cluster disable-addon --addon-name Istio --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr --is-remove-existing-add-on true
```

A work request is created to disable (and optionally remove) the Istio add-on.
  2. (Optional) View the status of the istiod and istio-ingressgateway pods to observe progress, by entering:```
kubectl get pods -n istio-system
```

  3. (Optional) Remove Istio CustomResourceDefinitions (CRDs), which aren't deleted by default, by entering:```
kubectl delete crd $(kubectl get crd -A | grep "istio.io" | awk '{print $1}')
```

  4. (Optional) Remove Istio mesh resources (such as the Kubernetes Gateway and VirtualService resources), which aren't managed by the Istio add-on, using the `kubectl delete` command. 


Was this article helpful?
YesNo

