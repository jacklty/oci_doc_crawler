Updated 2024-08-14
# Working with Istio as a Standalone Program
_Find out how to install Istio as a standalone program on clusters you've created with Kubernetes Engine (OKE)._
This topic provides an example of how to install Istio as a standalone program on clusters you've created with Kubernetes Engine (OKE). In addition, key features of OKE and Istio are demonstrated.
Topics covered include:
  * [Installing Istio as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke)
  * [Exploring Istio Observability](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#exploring_istio_observability)
  * [Managing Traffic](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#managing_traffic)
  * [Securing Istio](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#securing_istio)


Note that service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).
**Note**
You can use Istio with managed node pools, but not with virtual node pools.
## Installing Istio as a Standalone Program 🔗 
To get started using Istio, create an OKE cluster or use an existing OKE cluster, then install Istio. The sections provided below discuss the steps to install and test your Istio setup. For a complete list of installation options, [see here](https://istio.io/latest/docs/setup/install/).
### Creating an OKE cluster
Create an OKE cluster.
  1. If you have not already done so, create an OKE cluster within your OCI tenancy. [Multiple options](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm) are available to create an OKE cluster . The simplest option is the [Quick Create](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm) wizard in the web console.
  2. To access the OKE cluster on your local machine, install [kubectl](https://kubernetes.io/docs/tasks/tools/) and [oci-cli ](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliupgrading.htm).
  3. [Access the OKE cluster](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload) from the command line using `kubectl` by setting up the `kubeconfig` file and ensure that `kubectl` can access the cluster.


### Downloading Istio from the Command Line
Follow these steps to download Istio from the command line.
  1. Download Istio by running the following command: 
Copy
```
curl -L https://istio.io/downloadIstio | sh -
```

  2. Move to the Istio package directory. For example, if the package is istio-1.11.2: 
Copy
```
cd istio-1.11.2
```

  3. Add the `istioctl` client tool to the `PATH` for your workstation. 
Copy
```
export PATH=$PWD/bin:$PATH
```

  4. Validate if the cluster meets Istio install requirements by running the precheck: 
Copy
```
istioctl x precheck
```



### Installing Istio with istioctl
Install Istio with `istioctl` using the following command: 
Copy
```
istioctl install
```

### Running the Bookinfo Application 🔗 
The Istio project provides the Bookinfo application as a way to demonstrate Istio features. The application displays information about a book, similar to a single catalog entry of an online book store. Each book page contains a description of the book, details about the book (ISBN, number of pages), and a few book reviews. For more information on the Bookinfo application, see [the Bookinfo docs here](https://istio.io/latest/docs/examples/bookinfo/).
![A diagram of the Bookinfo application](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/bookinfo.jpg)
As you can see from the diagram, the Bookinfo application is composed of four microservices.
  * **Product Page Service:** Calls the **Details** and **Reviews** services to create a product page.
  * **Details Service:** Returns book information.
  * **Reviews Service:** Returns book reviews and calls the **Ratings** service.
  * **Ratings Service:** Returns ranking information for a book review.


To install and run the Bookinfo application, follow these steps.
  1. Label the namespace that hosts the application with `istio-injection=enabled`. 
Copy
```
kubectl label namespace default istio-injection=enabled
```

  2. Deploy the sample Bookinfo application. 
Copy
```
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
```

  3. Verify that all services and pods are running. 
Copy
```
kubectl get services
kubectl get pods
```

  4. Confirm that the application is running by sending a curl command from a pod. 
Copy
```
kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
```

  5. Make the application accessible from outside the cluster. 
Copy
```
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
```

  6. Verify that the application is using the gateway. Determine the `INGRESS_HOST` and `INGRESS_PORT` using [these instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports). 
Copy
```
curl -s "http://${INGRESS_HOST}:${INGRESS_PORT}/productpage" | grep -o "<title>.*</title>"
```



Also, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser to view the Bookinfo web page. Refresh the page several times to see different versions of reviews shown on the product page.
### Adding Istio Integration Applications
Istio integrates well with several popular Kubernetes related applications.
**Prometheus**
Istio provides a basic sample installation to quickly get Prometheus up and running.
Copy
```
kubectl apply -f samples/addons/prometheus.yaml
```

Alternatively, install prometheus and [configure](https://istio.io/latest/docs/ops/integrations/prometheus/#configuration) it to scrape Istio metrics.
For production-scale monitoring using Prometheus, see [Using Prometheus for production-scale monitoring](https://istio.io/latest/docs/ops/best-practices/observability/#using-prometheus-for-production-scale-monitoring).
**Grafana**
Istio provides a basic sample installation to get Grafana up and running quickly. All the Istio dashboards are included in the installation.
Copy
```
kubectl apply -f samples/addons/grafana.yaml
```

Alternatively, [install Grafana separately](https://grafana.com/docs/grafana/latest/installation/kubernetes/). In addition, [Istio's preconfigured dashboards](https://istio.io/latest/docs/ops/integrations/grafana/) can be imported.
**Jaeger**
Istio provides a basic sample installation to quickly get Jaeger up and running.
Copy
```
kubectl apply -f samples/addons/jaeger.yaml
```

Alternatively, install Jaeger separately and [configure](https://istio.io/latest/docs/ops/integrations/jaeger/) Istio to send traces to the Jaeger deployment.
**Zipkin**
Istio provides a basic sample installation to quickly get zipkin up and running.
Copy
```
kubectl apply -f samples/addons/extras/zipkin.yaml
```

Alternatively, install zipkin separately and [configure](https://istio.io/latest/docs/ops/integrations/zipkin/#installation) Istio to send traces to the zipkin deployment.
**Kiali**
Istio provides a basic sample installation to quickly get Kiali up and running:
Copy
```
kubectl apply -f samples/addons/kiali.yaml
      
```

Alternatively, [install and configure Kiali separately](https://kiali.io/documentation/latest/installation-guide/).
## Exploring Istio Observability 🔗 
In this section, explore the performance metrics and tracing features provided by the Istio integration applications.
### Querying Metrics from Prometheus for Bookinfo application
With Prometheus and Istio, the Bookinfo performance data is analyzed in several ways.
First, verify that Prometheus is installed.
Copy
```
kubectl -n istio-system get svc prometheus
```

Start the Prometheus UI with the following command:
Copy
```
istioctl dashboard prometheus
```

Click Graph to the right of Prometheus in the header. To see some data, generate traffic for product page using a browser or `curl`. The traffic is reflected in the Prometheus dashboard.
  * For viewing results, follow the [instructions here](https://istio.io/latest/docs/tasks/observability/metrics/querying-metrics/#querying-istio-metrics).
  * For more on querying Prometheus, read the Istio [querying docs](https://prometheus.io/docs/querying/basics/).


### Visualizing Metrics for Bookinfo Application with Grafana
Combining Prometheus with Grafana provides some nice performance dashboards for applications. To use the dashboards, first verify that both Prometheus and Grafana are installed.
Copy
```
kubectl -n istio-system get svc prometheus
kubectl -n istio-system get svc grafana
```

Start the Istio Grafana dashboard.
Copy
```
istioctl dashboard grafana
```

**Managing Grafana Dashboards**
The Istio service mesh delivers six Grafana dashboards. The Istio service mesh Grafana dashboard snapshots are captured here.
**Note** Generate traffic to the product page using a browser or `curl` and see it reflected in the Grafana dashboard.
**Istio Mesh Dashboard**
[![Snapshot of Istio Mesh Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaMeshDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaMeshDashboard.png)
**Istio Service Dashboard**
[![Snapshot of Istio Service Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaServiceDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaServiceDashboard.png)
**Istio Workload Dashboard**
[![Snapshot of Istio Workload Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaWorkloadDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaWorkloadDashboard.png)
**Istio Performance Dashboard**
[![Snapshot of Istio Performance Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaPerformanceDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaPerformanceDashboard.png)
**Istio Control Pane Dashboard**
[![Snapshot of Istio Control Pane Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaControlPlanDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioGrafanaControlPlanDashboard.png)
For more on how to create, configure, and edit dashboards, see the [Grafana documentation](https://docs.grafana.org/).
### Performing Distributed Tracing using Jaeger
Use the Jaeger open source framework to perform application tracing with Istio.
  1. Enable and configure tracing using `istioctl`: 
Copy
```
istioctl install --set meshConfig.enableTracing=true
```

  2. With the Bookinfo application deployed, open the Jaeger UI using `istioctl`. 
Copy
```
istioctl dashboard jaeger
```

  3. To generate traces, send in requests to the product page.
Copy
```
for i in $(seq 1 100); do curl -s -o /dev/null "http://$INGRESS_HOST:$INGRESS_PORT/productpage"; done
```



You see that the traces reflected in the Jaeger dashboard.
**Jaeger Dashboard**
[![Snapshot of Istio Jaeger Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerDashboard.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerDashboard.png)
**Jaeger Application Trace**
[![Snapshot of Istio Jaeger application trace](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerTrace.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerTrace.png)
### Performing Distributed Tracing using zipkin
Use the zipkin open source framework to perform application tracing with Istio.
  1. Enable and configure tracing using `istioctl`. 
Copy
```
istioctl install --set meshConfig.enableTracing=true
```

  2. With the Bookinfo application deployed, open the zipkin UI using `istioctl`. 
Copy
```
istioctl dashboard zipkin
```

  3. To generate traces, send in requests to the product page. 
Copy
```
for i in $(seq 1 100); do curl -s -o /dev/null "http://$INGRESS_HOST:$INGRESS_PORT/productpage"; done
```



You see that the traces reflect in the zipkin dashboard.
**Sample zipkin Dashboard**
[![Snapshot of Istio Zipkin dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerTrace.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioJaegerTrace.png)
### Performing Distributed Tracing with OCI Application Performance Monitoring
OCI [Application Performance Monitoring (APM)](https://docs.oracle.com/iaas/application-performance-monitoring/doc/application-performance-monitoring.html) integrates with open source tracing system tools such as Jaeger and zipkin. APM enables you to upload trace data in OCI. To integrate with OCI APM, create an APM domain by following the instructions mentioned [here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-apm-domain.html). An APM domain is an OCI resource which contains the systems monitored by APM.
After the domain is created, view the domain details and [obtain the data upload endpoint](https://docs.oracle.com/iaas/application-performance-monitoring/doc/obtain-data-upload-endpoint-and-data-keys.html), private key, and public key to construct the APM Collector URL. The APM collector URL is required when configuring open source tracers to communicate with the APM service. The Collector URL format requires a URL constructed using the data upload endpoint as the base URL and generates the path based on choices including values from our private or public key. The format is documented [here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/configure-open-source-tracing-systems.html#GUID-B5EDE254-C854-436D-B844-B986A4E077AA). With the URL path constructed, plug the URL into the Istio config.
**Note** For more detailed information on configuring APM service policies, see: 
  * [APM Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/apmpolicyreference.htm)
  * [APM Policy Example](https://docs-uat.us.oracle.com/en/cloud/paas/application-performance-monitoring/apmgn/perform-oracle-cloud-infrastructure-prerequisite-tasks.html)


**Configuring Istio to Send Traces to APM**
  1. Enable tracing with `istioctl`. 
Copy
```
istioctl install --set meshConfig.defaultConfig.tracing.zipkin.address=aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com:443
```

**Note** The endpoint address of `aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com` is an example and not an actual endpoint.
  2. Configure Envoy to [send the zipkin traces](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/trace/v3/zipkin.proto) to APM. Replace the code in `samples/custom-bootstrap/custom-bootstrap.yaml` with the following code block. 
Copy
```
apiVersion: v1
kind: ConfigMap
metadata:
 name: istio-custom-bootstrap-config
 namespace: default
data:
 custom_bootstrap.json: |
  {
    "tracing": {
      "http": {
        "name": "envoy.tracers.zipkin",
        "typed_config": {
          "@type": "type.googleapis.com/envoy.config.trace.v3.ZipkinConfig",
          "collector_cluster": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
          "collector_endpoint": "/20200101/observations/private-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=2C6YOLQSUZ5Q7IGN", // [Replace with the private datakey of your apm domain. You can also use public datakey but change the observation type to public-span]
          "collectorEndpointVersion": "HTTP_JSON",
          "trace_id_128bit": true,
          "shared_span_context": false
        }
      }
    },
    "static_resources": {
      "clusters": [{
        "name": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain:443]
        "type": "STRICT_DNS",
        "lb_policy": "ROUND_ROBIN",
        "load_assignment": {
          "cluster_name": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
          "endpoints": [{
            "lb_endpoints": [{
              "endpoint": {
                "address": {
                  "socket_address": {
                    "address": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
                    "port_value": 443
                  }
                }
              }
            }]
          }]
        },
        "transport_socket": {
          "name": "envoy.transport_sockets.tls",
          "typed_config": {
            "@type": "type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext",
            "sni": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com" // [Replace this with data upload endpoint of your apm domain]
          }
        }
      }]
    }
  }
EOF
```

  3. Apply the custom config. 
Copy
```
kubectl apply -f samples/custom-bootstrap/custom-bootstrap.yaml
```

  4. For all our services in Bookinfo to use this custom bootstrap configuration, add an annotation `sidecar.istio.io/bootstrapOverride` with the name of custom ConfigMap as the value. In the following example, an annotation is added for product page under `samples/bookinfo/platform/kube/bookinfo.yaml`. Add a similar annotation to other services. 
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: productpage-v1
 labels:
  app: productpage
  version: v1
spec:
 replicas: 1
 selector:
  matchLabels:
   app: productpage
   version: v1
 template:
  metadata:
   labels:
    app: productpage
    version: v1
   annotations:
    sidecar.istio.io/bootstrapOverride: "istio-custom-bootstrap-config" #[Name of custom configmap]
  spec:
   serviceAccountName: bookinfo-productpage
   containers:
    - name: productpage
     image: docker.io/istio/examples-bookinfo-productpage-v1:1.16.2
     imagePullPolicy: IfNotPresent
     ports:
      - containerPort: 9080
     volumeMounts:
      - name: tmp
       mountPath: /tmp
     securityContext:
      runAsUser: 1000
   volumes:
    - name: tmp
     emptyDir: {}
---
```

  5. Apply the yaml, all the restarted pods start sending traces to APM. 
Copy
```
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
```

  6. To enable an ingress-gateway to send traces, create a `configmap` named `custom-bootstrap.yaml` in the istio-system namespace: 
Copy
```
apiVersion: v1
kind: ConfigMap
metadata:
 name: istio-custom-bootstrap-config
 namespace: istio-system
data:
 custom_bootstrap.json: |
  {
    "tracing": {
      "http": {
        "name": "envoy.tracers.zipkin",
        "typed_config": {
          "@type": "type.googleapis.com/envoy.config.trace.v3.ZipkinConfig",
          "collector_cluster": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
          "collector_endpoint": "/20200101/observations/private-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=2C6YOLQSUZ5Q7IGN", // [Replace with the private datakey of your apm domain. You can also use public datakey but change the observation type to public-span]
          "collectorEndpointVersion": "HTTP_JSON",
          "trace_id_128bit": true,
          "shared_span_context": false
        }
      }
    },
    "static_resources": {
      "clusters": [{
        "name": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain:443]
        "type": "STRICT_DNS",
        "lb_policy": "ROUND_ROBIN",
        "load_assignment": {
          "cluster_name": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
          "endpoints": [{
            "lb_endpoints": [{
              "endpoint": {
                "address": {
                  "socket_address": {
                    "address": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com", // [Replace this with data upload endpoint of your apm domain]
                    "port_value": 443
                  }
                }
              }
            }]
          }]
        },
        "transport_socket": {
          "name": "envoy.transport_sockets.tls",
          "typed_config": {
            "@type": "type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext",
            "sni": "aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com" // [Replace this with data upload endpoint of your apm domain]
          }
        }
      }]
    }
  }
EOF
```

  7. Create a patch named `gateway-patch.yaml` for the ingress-gateway to start using custom-bootstrap config: 
Copy
```
spec:
 template:
  spec:
   containers:
   - name: istio-proxy
    env:
    - name: ISTIO_BOOTSTRAP_OVERRIDE
     value: /etc/istio/custom-bootstrap/custom_bootstrap.json
    volumeMounts:
    - mountPath: /etc/istio/custom-bootstrap
     name: custom-bootstrap-volume
     readOnly: true
   volumes:
   - configMap:
     name: istio-custom-bootstrap-config
     defaultMode: 420
     optional: false
    name: custom-bootstrap-volume
```

  8. Apply the previous patch for the ingress gateway: 
Copy
```
kubectl --namespace istio-system patch deployment istio-ingressgateway --patch "$(cat gateway-patch.yaml)"
```

  9. To generate traces, send in requests to the product page.
Copy
```
for i in $(seq 1 100); do curl -s -o /dev/null "http://$INGRESS_HOST:$INGRESS_PORT/productpage"; done
```



You see that the traces reflect in the APM dashboard by following the steps [here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/monitor-traces-trace-explorer.html).
**Zipkin Trace Explorer**
[![Screenshot of the Zipkin Trace Explorer](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinTraceExplorer.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinTraceExplorer.png)
**Zipkin Trace**
[![Screenshot of a Zipkin Trace](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinTrace.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinTrace.png)
**Zipkin Spans**
To see the spans, click Home in the APM list.
[![Screenshot of a Zipkin span](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinSpan.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinSpan.png)
**Zipkin App Dashboard**
APM provides functionality to create dashboards and explore the spans generated over time. Dashboards can be created by following the steps [here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-custom-dashboard.html).
[![Screenshot of a Zipkin app dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinBookinfoApp.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinBookinfoApp.png)
**Zipkin Metrics Explorer**
APM allows you to monitor the health, capacity, and performance of your applications by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#Notifications_Overview). Follow to steps [here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/application-performance-monitoring-metrics.html) to configure metrics.
[![Screenshot of a Zipkin metrics explorer](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinMetricExplorer.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioZipkinMetricExplorer.png)
### Observing Logs with OCI Logging
[OCI Logging](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm) is a central component for analyzing and searching log file entries for tenancies in OCI. Kubernetes container logs from OKE worker nodes can be published as [custom logs](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm) to OCI Logging. Follow the [steps described here to configure OCI Logging](https://www.ateam-oracle.com/observabitiliy-on-oracle-oci-using-custom-logs-in-oci-logging-to-monitor-and-analyze-cloud-native-applications) to ingest container logs.
  1. Enable envoy access logging in Istio with `istioctl`. 
Copy
```
istioctl install --set meshConfig.accessLogFile=/dev/stdout
```

  2. Access the Bookinfo product page using a browser or curl. The generated access logs can be viewed using the `kubectl` command. 
Copy
```
kubectl logs -l app=productpage -c istio-proxy
```



If OCI Logging is configured for the cluster, these logs can be queried and analyzed using OCI console's log search page.
**OCI Logging Search**
[![Screenshot of a OCI Logging search](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioOciLoggingSearch.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioOciLoggingSearch.png)
**OCI Logging Search Expanded**
[![Screenshot of an expanded OCI Logging search](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioOciLoggingExpanded.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioOciLoggingExpanded.png)
### Visualizing Mesh Using Kiali
Verify that Kiali is installed.
Copy
```
kubectl -n istio-system get svc kiali
```

Open the Kiali UI in the browser.
Copy
```
istioctl dashboard kiali
```

Send some traffic to the product page.
Copy
```
for i in $(seq 1 100); do curl -s -o /dev/null "http://$INGRESS_HOST:$INGRESS_PORT/productpage"; done
```

Visualize your mesh in Kiali by following step 5 [from here](https://istio.io/latest/docs/tasks/observability/kiali/#generating-a-graph).
## Managing Traffic 🔗 
Istio's traffic routing rules lets you control the flow of traffic between services and simplifies configuration of service-level properties like circuit breakers, timeouts, and retries. Istio makes it easy to set up important tasks like A/B testing, canary rollouts, and staged rollouts with percentage-based traffic splits.
Istio's traffic management API resources:
  * [Virtual Services](https://istio.io/latest/docs/concepts/traffic-management/#virtual-services)
  * [Destination Rules](https://istio.io/latest/docs/concepts/traffic-management/#destination-rules)
  * [Gateways](https://istio.io/latest/docs/concepts/traffic-management/#gateways)


For Istio to control the Bookinfo application version routing, define all the available versions of your service, called subsets, in destination rules. Create default destination rules for the Bookinfo services: 
Copy
```
kubectl apply -f samples/bookinfo/networking/destination-rule-all.yaml
```

### Shifting Traffic
Istio allows us to migrate traffic gradually from one version of a microservice to another version using Istio's weighted routing feature. The following example shows how to configure to send 50% of traffic to `reviews:v1` and 50% to `reviews:v3`. After that, complete the migration by sending 100% of traffic to `reviews:v3`.
  1. Route all traffic to the v1 version of each microservice. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser. Notice that the reviews part of the page displays with no rating stars, no matter how many times you refresh. Istio is configured to route all traffic for the reviews service to `reviews:v1` and this version of the service does not access the star ratings service.
  2. Transfer 50% of the traffic from `reviews:v1` to `reviews:v3` with the following command, and wait for the new rules to propagate. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-reviews-50-v3.yaml
```

Refresh the `/productpage` URL in your browser and see red colored star ratings approximately 50% of the time. The `reviews:v3` accesses the star ratings service, but the `reviews:v1` version does not.
  3. Now route 100% of the traffic to `reviews:v3`. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-reviews-v3.yaml
```

  4. Refresh the `/productpage` URL in your browser and see red colored star ratings all the time for each review.


### Managing Request Routing
Istio can route traffic in several ways. To start, configure Istio to route all traffic through v1 of each microservice. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser . Notice that the reviews part of the page displays with no rating stars, no matter how many times you refresh. Because Istio is configured to route all traffic for the reviews service to the version `reviews:v1`. This version of the service does not access the star ratings service.
[![Screenshot of a sample Booinfo book.](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_1.png)
**Routing based on User Identity**
To route based on user identity:
  1. Change the route configuration so that all traffic from a specific user named `jason` is routed to `reviews:v2`. Istio doesn't have any special, built-in understanding of user identity. In this example, the `productpage` service adds a custom end-user header to all outbound HTTP requests to the reviews service. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-reviews-test-v2.yaml
```

  2. To view the Bookinfo web page and login as user `jason`, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser. Refresh the browser to see that star ratings appear next to each review.
[![Screenshot of a sample Booinfo book with stars](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_2.png)
  3. Open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser to view the Bookinfo web page and login as user other than `jason`. Refresh the browser to see no stars for each review.
[![Screenshot of a sample Booinfo book without stars](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_3.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestRouting_3.png)


**Routing based on URL Rewriting**
In this example, HTTP requests with a path that starts with `/products` or `/bookinfoproductpage` are rewritten to `/productpage`. HTTP requests are sent to pods with `productpage` running on port 9080. For more information on Istio URL rewriting, [see here](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRewrite).
  1. Apply the following yaml: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: bookinfo
spec:
 hosts:
 - "*"
 gateways:
 - bookinfo-gateway
 http:
 - match:
  - uri:
    prefix: /products
  - uri:
    prefix: /bookinfoproductpage
  rewrite:
   uri: /productpage
  route:
  - destination:
    host: productpage
    port:
     number: 9080
EOF
```

  2. To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/products` and `http://${INGRESS_HOST}:${INGRESS_PORT}/bookinfoproductpage` in a browser. In both the cases, a rewrite is performed before forwarding the request.
Rewrite /bookproductpage
[![Screenshot of a sample Booinfo book with /bookproductpage](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_2.png)
Rewrite /products
[![Screenshot of a sample Booinfo book with /products](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_1.png)
  3. Clean up the yaml file to the original version provided by Istio and apply it. 
Copy
```
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
```

  4. Open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/bookinfoproductpage` or `http://${INGRESS_HOST}:${INGRESS_PORT}/products` to not see the product page because the yaml doesn't rewrite the request.
404 Error /products
[![Screenshot of a sample Booinfo book with /products 404](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_4.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_4.png)
404 Error /booksproductpage
[![Screenshot of a sample Booinfo book with /booksproductpage 404](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_3.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRewriteUrl_3.png)


### Testing Network Resilience
Istio allows you to configure your installation for request timeouts, fault injection, and circuit breakers. These settings allow manage and test the fault tolerance of deployed applications.
**Setting Request Timeouts**
A timeout is the amount of time an Envoy proxy waits for replies from a given service. The timeout ensures that services don't wait for replies indefinitely and ensures that calls succeed or fail within a predictable timeframe. For more information on timeouts, [see here](https://istio.io/latest/docs/concepts/traffic-management/#timeouts).
A timeout for HTTP requests can be specified using the timeout field of the [route rule](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRoute). By default, the request timeout is disabled.
  1. Initialize the application version routing by running the following command: 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

  2. Route requests to `reviews:v2` service, in effect, a version that calls the ratings service: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: reviews
spec:
 hosts:
  - reviews
 http:
 - route:
  - destination:
    host: reviews
    subset: v2
EOF
```

  3. Add a 2-second delay to calls to the ratings service: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: ratings
spec:
 hosts:
 - ratings
 http:
 - fault:
   delay:
    percent: 100
    fixedDelay: 2s
  route:
  - destination:
    host: ratings
    subset: v1
EOF
```

  4. To view the Bookinfo web page with ratings stars displayed, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser . A 2-second delay occurs whenever you refresh the page. 
[![Screenshot of book product web page.](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestTimeoutDelay_1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestTimeoutDelay_1.png)
  5. Add a half second request timeout for calls to the reviews service: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: reviews
spec:
 hosts:
 - reviews
 http:
 - route:
  - destination:
    host: reviews
    subset: v2
  timeout: 0.5s
EOF
```

  6. To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser. Notice the page returns in about 1 second, instead of 2, and the reviews are unavailable. 
[![Screenshot of book product web page.](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestTimeoutDelay_2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioRequestTimeoutDelay_2.png)


The reason that the response takes 1 second, even though the timeout is configured at half a second, is because a hard-coded retry in the `productpage` service. The service calls the timed out reviews service twice before returning.
In addition to overriding them in route rules, the timeout can also be overridden on a per-request basis if the application adds an `x-envoy-upstream-rq-timeout-ms` header on outbound requests.
**Managing Fault Injection**
Fault injection is a testing method that introduces errors into a system to ensure that the system withstands and recovers from error conditions. Istio allows fault injection at the application layer such as HTTP error codes. Istio injects two types of faults, both configured using a virtual service. For more information on fault injection, [see here](https://istio.io/latest/docs/concepts/traffic-management/#fault-injection).
  * **Delays:** Delays are timing failures that mimic increased network latency or an overloaded upstream service.
  * **Aborts:** Aborts are crash failures that mimic failures in upstream services. Aborts manifest in the form of HTTP error codes or TCP connection failures.


To test fault injection, run the following command to initialize the application version routing:
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
kubectl apply -f samples/bookinfo/networking/virtual-service-reviews-test-v2.yaml
```

**Injecting an HTTP Delay Fault**
To inject a delay fault, follow these steps:
  * Create a fault injection rule to delay traffic coming from the user `jason`. The following command injects a 7-second delay between the `reviews:v2` and ratings microservices for user `jason`. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-ratings-test-delay.yaml
```

**Note** The `reviews:v2` service has a 10-s hard-coded connection timeout for calls to the ratings service. With 7-second delay, expect the end-to-end flow to continue without any errors.
  * To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser. 
[![Snapshot of Bookinfo page showing delay errors](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioHttpDelayFault.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioHttpDelayFault.png)
The Bookinfo home page loads without any errors in approximately seven seconds. However, the reviews section displays an error message: _Sorry, product reviews are currently unavailable for this book_. A bug exists in the application code. The hard-coded timeout between the `productpage` and the `reviews` service results in a 6-second delay, 3 seconds plus 1 retry. As a result, the `productpage` call to `reviews` times out prematurely and throws an error after 6 seconds.
To fix the bug, increase the `productpage` to `reviews` service timeout, or decrease the `reviews` to `ratings` timeout to less than 3 seconds.
  * Let's fix the bug by adding a 2-second delay to the `ratings` service for user `jason`. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: ratings
spec:
 hosts:
 - ratings
 http:
 - match:
  - headers:
    end-user:
     exact: jason
  fault:
   delay:
    percentage:
     value: 100.0
    fixedDelay: 2s
  route:
  - destination:
    host: ratings
    subset: v1
 - route:
  - destination:
    host: ratings
    subset: v1
EOF
```

  * Now that the bug is fixed, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser to view the Bookinfo web page. Sign in as `jason` with ratings stars displayed. 
[![Snapshot of Bookinfo page without dely errors](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioHttpDelayFaultFix.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioHttpDelayFaultFix.png)


**Injecting an HTTP Abort Fault**
Follow these steps to inject an abort fault:
  1. Create a fault injection rule to send an HTTP abort response for user `jason`: 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-ratings-test-abort.yaml
```

  2. To view the Bookinfo web page, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser. Login as user `jason`. A message indicates the `ratings` service is unavailable. 
[![Screenshot of the Bookinfo Page with Rating Service Unavailable](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioAbort_1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioAbort_1.png)
Logout from user `jason` or login with any other user to not see any error message.
[![creenshot of the Bookinfo Page without errors](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioAbort_2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioAbort_2.png)


**Creating Circuit Breakers**
Circuit breaking allows us to write applications that limit the impact of failures, latency spikes, and other undesirable effects of network peculiarities. For more information on circuit breakers, [see here](https://istio.io/latest/docs/concepts/traffic-management/#circuit-breakers).
  1. Create a [destination rule](https://istio.io/latest/docs/reference/config/networking/destination-rule/) to apply circuit breaking settings when calling the product service. The following rule sets the maximum number of connections to be not more than one and have a maximum of one HTTP pending requests. In addition, the rules configure hosts to be scanned every 1 second. Any host that fails one time with a 5XX error code is ejected for 3 minutes. Also, 100% of hosts in the load balancing pool for the upstream service are ejected. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
 name: productpage
spec:
 host: productpage
 trafficPolicy:
  connectionPool:
   tcp:
    maxConnections: 1
   http:
    http1MaxPendingRequests: 1
    maxRequestsPerConnection: 1
  outlierDetection:
   consecutive5xxErrors: 1
   interval: 1s
   baseEjectionTime: 3m
   maxEjectionPercent: 100
 subsets:
 - name: v1
  labels:
   version: v1
EOF
```

  2. Route all traffic to the v1 version of each microservice. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

  3. Create a client to send traffic to the product service. Fortio lets you control the number of connections, concurrency, and delays for outgoing HTTP calls. If you have enabled [automatic sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection), deploy the `fortio` service: 
Copy
```
kubectl apply -f samples/httpbin/sample-client/fortio-deploy.yaml
```

Alternatively, manually inject the sidecar before deploying the `fortio` application. 
Copy
```
kubectl apply -f <(istioctl kube-inject -f samples/httpbin/sample-client/fortio-deploy.yaml)
```

  4. Log in to the client pod and use the `fortio` tool to call `productpage` and verify the response status code to be 200 with the following commands. 
Copy
```
export FORTIO_POD=$(kubectl get pods -l app=fortio -o 'jsonpath={.items[0].metadata.name}')
kubectl exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio curl http://productpage:9080

```

The following output is produced: 
Copy
```
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-length: 1683
server: envoy
date: Tue, 07 Sep 2021 11:01:02 GMT
x-envoy-upstream-service-time: 5
```

  5. Call the service with 2 concurrent connections (-c 2) and send 20 requests (-n 20). Interestingly, 16 requests passthrough and 4 fail. 
Copy
```
kubectl exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio load -c 2 -qps 0 -n 20 -loglevel Warning http://productpage:9080
```

The command produces output similar to the following. 
Copy
```
11:03:43 I logger.go:127> Log level is now 3 Warning (was 2 Info)
Fortio 1.11.3 running at 0 queries per second, 128->128 procs, for 20 calls: http://productpage:9080
Starting at max qps with 2 thread(s) [gomax 128] for exactly 20 calls (10 per thread + 0)
11:03:43 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:03:43 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:03:43 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:03:43 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
Ended after 51.340006ms : 20 calls. qps=389.56
Aggregated Function Time : count 20 avg 0.0045031997 +/- 0.002036 min 0.000387421 max 0.007704444 sum 0.090063995
# range, mid point, percentile, count
>= 0.000387421 <= 0.001 , 0.000693711 , 15.00, 3
> 0.003 <= 0.004 , 0.0035 , 20.00, 1
> 0.004 <= 0.005 , 0.0045 , 65.00, 9
> 0.005 <= 0.006 , 0.0055 , 75.00, 2
> 0.006 <= 0.007 , 0.0065 , 95.00, 4
> 0.007 <= 0.00770444 , 0.00735222 , 100.00, 1
# target 50% 0.00466667
# target 75% 0.006
# target 90% 0.00675
# target 99% 0.00756356
# target 99.9% 0.00769036
Sockets used: 5 (for perfect keepalive, would be 2)
Jitter: false
Code 200 : 16 (80.0 %)
Code 503 : 4 (20.0 %)
Response Header Sizes : count 20 avg 133.6 +/- 66.8 min 0 max 167 sum 2672
Response Body/Total Sizes : count 20 avg 1528.2 +/- 643.6 min 241 max 1850 sum 30564
All done 20 calls (plus 0 warmup) 4.503 ms avg, 389.6 qps
```

  6. Increase the number of concurrent connections to 3. 
Copy
```
kubectl exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio load -c 3 -qps 0 -n 30 -loglevel Warning http://productpage:9080
```

Only 26.7% of the requests succeeded and circuit breaking traps the rest. 
Copy
```
11:10:19 I logger.go:127> Log level is now 3 Warning (was 2 Info)
Fortio 1.11.3 running at 0 queries per second, 128->128 procs, for 30 calls: http://productpage:9080
Starting at max qps with 3 thread(s) [gomax 128] for exactly 30 calls (10 per thread + 0)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
11:10:19 W http_client.go:693> Parsed non ok code 503 (HTTP/1.1 503)
Ended after 28.105508ms : 30 calls. qps=1067.4
Aggregated Function Time : count 30 avg 0.0024256753 +/- 0.003264 min 0.000261072 max 0.010510116 sum 0.07277026
# range, mid point, percentile, count
>= 0.000261072 <= 0.001 , 0.000630536 , 66.67, 20
> 0.001 <= 0.002 , 0.0015 , 73.33, 2
> 0.005 <= 0.006 , 0.0055 , 76.67, 1
> 0.006 <= 0.007 , 0.0065 , 83.33, 2
> 0.007 <= 0.008 , 0.0075 , 93.33, 3
> 0.009 <= 0.01 , 0.0095 , 96.67, 1
> 0.01 <= 0.0105101 , 0.0102551 , 100.00, 1
# target 50% 0.000805545
# target 75% 0.0055
# target 90% 0.00766667
# target 99% 0.0103571
# target 99.9% 0.0104948
Sockets used: 25 (for perfect keepalive, would be 3)
Jitter: false
Code 200 : 8 (26.7 %)
Code 503 : 22 (73.3 %)
Response Header Sizes : count 30 avg 44.533333 +/- 73.85 min 0 max 167 sum 1336
Response Body/Total Sizes : count 30 avg 670.06667 +/- 711.5 min 241 max 1850 sum 20102
All done 30 calls (plus 0 warmup) 2.426 ms avg, 1067.4 qps
```

  7. Query the `istio-proxy` stats to gain more information. 
Copy
```
kubectl exec "$FORTIO_POD" -c istio-proxy -- pilot-agent request GET stats | grep productpage | grep pending
```

Circuit breaking flags 32 calls by looking at the metric `upstream_rq_pending_overflow`. 
Copy
```
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.circuit_breakers.default.remaining_pending: 1
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.circuit_breakers.default.rq_pending_open: 0
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.circuit_breakers.high.rq_pending_open: 0
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.upstream_rq_pending_active: 0
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.upstream_rq_pending_failure_eject: 0
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.upstream_rq_pending_overflow: 32
cluster.outbound|9080|v1|productpage.default.svc.cluster.local.upstream_rq_pending_total: 39
```

  8. Clean up the client. 
Copy
```
kubectl apply -f samples/bookinfo/networking/destination-rule-all.yaml
kubectl delete deploy fortio-deploy
kubectl delete svc fortio
```



### Mirroring
Traffic mirroring, also called shadowing, allows teams to bring changes to production with as little risk as possible. Mirroring sends a copy of live traffic to a mirrored service. The mirrored traffic occurs outside of the critical request path for the primary service.
  1. Route all traffic to the v1 version of each microservice. 
Copy
```
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

  2. Change the route rule to mirror traffic to `reviews:v2`. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: reviews
spec:
 hosts:
  - reviews
 http:
 - route:
  - destination:
    host: reviews
    subset: v1
   weight: 100
  mirror:
   host: reviews
   subset: v2
  mirrorPercentage:
   value: 100.0
EOF
```

The previous route rule sends 100% of the traffic to `reviews:v1` and mirrors 100% of the same traffic to the `reviews:v2` service.
When traffic gets mirrored, the requests are sent to the mirrored service with their Host/Authority headers appended with `-shadow`. For example, reviews become `reviews-shadow.Mirrored` requests considered as "fire and forget." The mirrored responses are discarded.
Instead of mirroring all requests, change the value field under the `mirrorPercentage` field to mirror a fraction of the traffic. If this field is absent, all traffic is mirrored.
  3. Send in some traffic by refreshing the url `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser.
  4. Logs of `reviews:v1` service. Note v1 service does not call the ratings service. 
[![Screeshot of the reviews:v1 service](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioMirroring_1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioMirroring_1.png)
  5. Logs of `reviews:v2` mirrored service. Note for the v2 service, the header is appended with `-shadow`. 
[![Screeshot of the reviews:v2 service with -shadow](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioMirroring_2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/non-dita/istio/IstioMirroring_2.png)


### Managing Gateways
Gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateway configurations are applied to standalone Envoy proxies that are running at the edge of the mesh, rather than sidecar Envoy proxies running alongside your service workloads. Istio provides some preconfigured gateway proxy deployments `istio-ingressgateway` and `istio-egressgateway`.
If you haven't setup the Istio gateways as part of the installation, run the following command to install them. 
Copy
```
istioctl install
```

The command deploys Istio using the default settings which includes a gateway. For more information, [see here](https://istio.io/latest/docs/setup/additional-setup/gateway/).
**Note** Determine the `INGRESS_HOST` and `INGRESS_PORT` using [these instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports).
**Configuring Ingress using Istio Gateway**
The ingress gateway configures exposed ports and protocols, but unlike Kubernetes Ingress Resources, does not include any traffic routing configuration. Traffic routing for ingress traffic is instead configured using Istio routing rules. For more information on Istio ingress, [see here](https://kubernetes.io/docs/concepts/services-networking/ingress/).
**Note** If you have already deployed the Bookinfo application, the following steps are not required.
  1. Create an Istio gateway that configures on port 80 for HTTP traffic. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
 name: bookinfo-gateway
spec:
 selector:
  istio: ingressgateway # use istio default controller
 servers:
  - port:
    number: 80
    name: http
    protocol: HTTP
   hosts:
    - "*"
EOF
```

  2. Configure routes for traffic entering through the Gateway: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: bookinfo
spec:
 hosts:
 - "*"
 gateways:
 - bookinfo-gateway
 http:
 - match:
  - uri:
    exact: /productpage
  - uri:
    prefix: /static
  - uri:
    exact: /login
  - uri:
    exact: /logout
  - uri:
    prefix: /api/v1/products
  route:
  - destination:
    host: productpage
    port:
     number: 9080
EOF
```

  3. To deploy the Bookinfo application, see the "Running the Bookinfo Application" section of the [Installing Istio and OKE page](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke).
  4. Access the `productpage` service using curl: 
Copy
```
curl -s -I http://$INGRESS_HOST:$INGRESS_PORT/productpage
```

The command produces the following output:
Copy
```
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-length: 4183
server: istio-envoy
date: Tue, 07 Sep 2021 13:48:39 GMT
x-envoy-upstream-service-time: 36
```

  5. Access any other URL that has not been explicitly exposed. You see an HTTP 404 error. 
Copy
```
curl -s -I http://$INGRESS_HOST:$INGRESS_PORT/any
```

The command produces the following output:
```
HTTP/1.1 404 Not Found
date: Tue, 07 Sep 2021 13:49:45 GMT
server: istio-envoy
transfer-encoding: chunked
```

  6. For explicit hosts in gateways, use the -H flag to set the Host HTTP header. The flag is needed because your ingress gateway and virtual service are configured to handle the host. For example, your host is example.com and the name is specified in both gateways and virtual service. 
Copy
```
curl -s -I -HHost:example.com http://$INGRESS_HOST:$INGRESS_PORT/productpage
```

  7. Also, open the URL `http://${INGRESS_HOST}:${INGRESS_PORT}/productpage` in a browser to view the Bookinfo web page.


**Configuring Ingress using Kubernetes Ingress Resource**
The reader assumes that Bookinfo application is deployed into the cluster. To deploy the Bookinfo application, see the "Running the Bookinfo Application" section of the [Installing Istio and OKE page](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke).
  1. Remove the Istio gateway if the configuration is already applied. 
Copy
```
kubectl delete -f samples/bookinfo/networking/bookinfo-gateway.yaml
```

  2. Create an Ingress resource on port 80 for HTTP traffic. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 annotations:
  kubernetes.io/ingress.class: istio
 name: ingress
spec:
 rules:
 - http:
   paths:
   - path: /productpage
    pathType: Prefix
    backend:
     service:
      name: productpage
      port:
       number: 9080
EOF
```

The `kubernetes.io/ingress.class[](https://kubernetes.io/docs/concepts/services-networking/ingress/)` annotation is required to tell the Istio gateway controller to handle this `Ingress`.
  3. Verify accessing the Bookinfo application by following the instructions from previous section.
  4. Delete the resource and enable Istio gateway for further tasks. 
Copy
```
kubectl delete ingress ingress
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
```



**Accessing External Services with Egress**
By default, all outbound traffic from an Istio enabled pod is redirected to its sidecar proxy and Istio configures the Envoy proxy to pass through requests for unknown services. Istio configures the sidecar handling of external services through a configuration field `meshConfig.outboundTrafficPolicy.mode`. If this option is set to:
  * `ALLOW_ANY` (default): Istio proxy lets calls to unknown services pass through.
  * `REGISTRY_ONLY`: Istio proxy blocks any host without an HTTP service or service entry defined within the mesh.


The reader assumes that the Bookinfo application is deployed into the cluster. If not, follow the steps to deploy the Bookinfo application.
**Managing Envoy Passthrough to External Services**
To enable passthrough to external services, follow these steps.
  1. Change the `meshConfig.outboundTrafficPolicy.mode` option to `ALLOW_ANY` with `istioctl`. 
Copy
```
istioctl install --set meshConfig.outboundTrafficPolicy.mode=ALLOW_ANY
```

**Note** This step is required only if you have explicitly set the option to `REGISTRY_ONLY` during the installation.
  2. To confirm successful 200 responses, make a request to external services from the `SOURCE_POD`: 
Copy
```
export SOURCE_POD=$(kubectl get pod -l app=ratings -o jsonpath='{.items..metadata.name}')
kubectl exec $SOURCE_POD -c ratings -- curl -sI http://httpbin.org/headers | grep "HTTP"
```

The command produces the following output: ```
HTTP/1.1 200 OK
```



However, the drawback with this approach is that Istio monitoring and control for traffic to external services is lost.
**Controlling Access to External Services [Recommended]**
To set up controlled access to external services, follow these steps:
  1. Change the `meshConfig.outboundTrafficPolicy.mode` option to `REGISTRY_ONLY`. This step is required only if you haven't explicitly set the option to `REGISTRY_ONLY` during the installation.
  2. Follow only step 1 from the "Envoy Passthrough to External Services" section. The only change to make here is that replace `ALLOW_ANY` with `REGISTRY_ONLY`.
  3. To verify that the external services are blocked, make a couple of requests to external HTTPS services from the `SOURCE_POD`. Configuration changes take several seconds to propagate, so successful connections are possible. Wait for several seconds and then retry the last command. 
Copy
```
export SOURCE_POD=$(kubectl get pod -l app=ratings -o jsonpath='{.items..metadata.name}')
kubectl exec $SOURCE_POD -c ratings -- curl -sI http://httpbin.org/headers | grep "HTTP"
```

The command produces the following output:
```
HTTP/1.1 502 Bad Gateway
```

  4. Create a `ServiceEntry` to allow access to an external HTTP service. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
 name: httpbin-ext
spec:
 hosts:
 - httpbin.org
 ports:
 - number: 80
  name: http
  protocol: HTTP
 resolution: DNS
 location: MESH_EXTERNAL
EOF
```

  5. Make a request to the external HTTP service from `SOURCE_POD`. Notice that the headers added by the Istio sidecar proxy: `X-Envoy-Decorator-Operation`. 
Copy
```
kubectl exec $SOURCE_POD -c ratings -- curl -sI http://httpbin.org/headers | grep "HTTP"
```

The command produces the following output: ```
HTTP/1.1 200 OK
```

Remove the `grep` command to see all the headers.
Copy
```
kubectl exec $SOURCE_POD -c ratings -- curl -sS http://httpbin.org/headers
```

The command produces the following output:
```
{
 "headers": {
  "Accept": "*/*",
  "Host": "httpbin.org",
  "User-Agent": "curl/7.52.1",
  "X-Amzn-Trace-Id": "Root=1-61384b41-2d3cf8b5571ba7504ab9a834",
  "X-B3-Sampled": "0",
  "X-B3-Spanid": "6983ef0cec914f83",
  "X-B3-Traceid": "d510c4d190cb099d6983ef0cec914f83",
  "X-Envoy-Attempt-Count": "1",
  "X-Envoy-Decorator-Operation": "httpbin.org:80/*",
  "X-Envoy-Peer-Metadata": "ChsKDkFQUF9DT05UQUlORVJTEgkaB3JhdGluZ3MKGgoKQ0xVU1RFUl9JRBIMGgpLdWJlcm5ldGVzChkKDUlTVElPX1ZFUlNJT04SCBoGMS4xMS4xCtQBCgZMQUJFTFMSyQEqxgEKEAoDYXBwEgkaB3JhdGluZ3MKIAoRcG9kLXRlbXBsYXRlLWhhc2gSCxoJYzk5NDdiOTlmCiQKGXNlY3VyaXR5LmlzdGlvLmlvL3Rsc01vZGUSBxoFaXN0aW8KLAofc2VydmljZS5pc3Rpby5pby9jYW5vbmljYWwtbmFtZRIJGgdyYXRpbmdzCisKI3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLXJldmlzaW9uEgQaAnYxCg8KB3ZlcnNpb24SBBoCdjEKGgoHTUVTSF9JRBIPGg1jbHVzdGVyLmxvY2FsCiQKBE5BTUUSHBoacmF0aW5ncy12MS1jOTk0N2I5OWYtbGN4bHQKFgoJTkFNRVNQQUNFEgkaB2RlZmF1bHQKTgoFT1dORVISRRpDa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2RlZmF1bHQvZGVwbG95bWVudHMvcmF0aW5ncy12MQoXChFQTEFURk9STV9NRVRBREFUQRICKgAKHQoNV09SS0xPQURfTkFNRRIMGgpyYXRpbmdzLXYx",
  "X-Envoy-Peer-Metadata-Id": "sidecar~10.244.0.11~ratings-v1-c9947b99f-lcxlt.default~default.svc.cluster.local"
 }
}
```

  6. For accessing HTTPS calls, replace the port and protocol when creating service entries.
  7. The approach adds external service traffic management features like timeouts and fault injection. The following request returns 200 (OK) in approximately five seconds. 
Copy
```
kubectl exec $SOURCE_POD -c ratings -- curl http://httpbin.org/delay/5
```

Use `kubectl` to set a 3-second timeout on calls to the [httpbin.org](http://httpbin.org/) external service: 
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: httpbin-ext
spec:
 hosts:
  - httpbin.org
 http:
 - timeout: 3s
  route:
   - destination:
     host: httpbin.org
    weight: 100
EOF
```

This time a timeout appears after 3 seconds. Although [httpbin.org](http://httpbin.org/) was waiting five seconds, Istio cut off the request at 3 seconds: 
Copy
```
kubectl exec $SOURCE_POD -c ratings -- curl http://httpbin.org/delay/5
```

  8. Clean up the resources for further future tasks. 
Copy
```
kubectl delete serviceentry httpbin-ext
kubectl delete virtualservice httpbin-ext --ignore-not-found=true
```



**Directing Access to External Services**
This approach bypasses the Istio sidecar proxy, giving services direct access to any external server. However, configuring the proxy this way does require cluster-provider specific knowledge and configuration. Similar to the first approach, we lose monitoring of access to external services and can't apply Istio features on traffic to external services. Follow [these steps](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-control/#direct-access-to-external-services) to provide direct access to external services. 
## Securing Istio 🔗 
The Istio security features provide strong identity, powerful policy, transparent TLS encryption, and authentication, authorization, and audit (AAA) tools to protect your services and data.
### Configuring Authentication
Istio offers mutual TLS as a full-stack solution for transport authentication, which is enabled without requiring service code changes.
Deploy `sleep` and `httpbin` services in the default namespace. 
Copy
```
kubectl apply -f samples/sleep/sleep.yaml
kubectl apply -f samples/httpbin/httpbin.yaml
```

By default, Istio performs several tasks. Istio tracks the server workloads migrated to Istio proxies. Istio configures client proxies to send mutual TLS traffic to those workloads automatically. Istio sends plain text traffic to workloads without sidecars.
To verify that certs are sent, send a request from a `sleep` pod to `httpbin` pod and look for the X-Forwarded-Client-Cert header. 
Copy
```
kubectl exec "$(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name})" -c sleep -- curl -s http://httpbin.default:8000/headers -s | grep X-Forwarded-Client-Cert | sed 's/Hash=[a-z0-9]*;/Hash=<redacted>;/'
```

Deploy another instance of the `sleep` and `httpbin` services without the sidecar enabled. 
Copy
```
kubectl create ns legacy
kubectl apply -f samples/sleep/sleep.yaml -n legacy
kubectl apply -f samples/httpbin/httpbin.yaml -n legacy
```

The request from the `sleep` pod in the default namespace to `httpbin` pod in the legacy namespace is plaintext because the destination is not sidecar enabled. Verify that plain text is sent by running the following command. 
Copy
```
kubectl exec "$(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name})" -c sleep -- curl http://httpbin.legacy:8000/headers -s | grep X-Forwarded-Client-Cert
```

The request from the `sleep` pod in the legacy namespace to `httpbin` in the default namespace also succeeds with a plaintext connection. The can be verified with the following command.
Copy
```
kubectl exec "$(kubectl get pod -l app=sleep -n legacy -o jsonpath={.items..metadata.name})" -n legacy -c sleep -- curl http://httpbin.default:8000/headers
```

To prevent non-mutual TLS traffic for the whole mesh, set a mesh-wide peer authentication policy with the mutual TLS mode set to `STRICT`. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
 name: "default"
 namespace: "istio-system"
spec:
 mtls:
  mode: STRICT
EOF
```

The connection from a `sleep` pod in the legacy namespace to `httpbin` in default namespace no longer works when mutual TLS mode is set to `STRICT`. 
Copy
```
kubectl exec "$(kubectl get pod -l app=sleep -n legacy -o jsonpath={.items..metadata.name})" -n legacy -c sleep -- curl http://httpbin.default:8000/headers
```

Revert the `STRICT` peer authentication setting by deleting the CR. 
Copy
```
kubectl delete peerauthentication -n istio-system default
```

In addition to the global mutual TLS setting, it can also be set at a namespace or workload level. Follow [the Istio documentation for detailed authentication configurations](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/).
### Configurating Authorization
Istio allows you to configure authorization policies for your applications.
First, configure a simple `allow-nothing` policy that rejects all requests to the workload, and then grants more access to the workload gradually and incrementally. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: allow-nothing
 namespace: default
spec:
 {}
EOF
```

Open the Bookinfo product page in your browser. It shows "`RBAC: access denied`" error confirming that the `deny-all` policy is working as intended.
Create a policy to grant to all users and workloads access to the product page using the following command. 
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: "productpage-viewer"
 namespace: default
spec:
 selector:
  matchLabels:
   app: productpage
 action: ALLOW
 rules:
 - to:
  - operation:
    methods: ["GET"]
EOF
```

You see the "Bookinfo Sample" page but the `productpage` service cannot access the details and reviews page.
Add the following policies to grant `productpage` workload access to the details and reviews workloads and reviews workload access to the `ratings` workload. 
Set Details Viewer
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: "details-viewer"
 namespace: default
spec:
 selector:
  matchLabels:
   app: details
 action: ALLOW
 rules:
 - from:
  - source:
    principals: ["cluster.local/ns/default/sa/bookinfo-productpage"]
  to:
  - operation:
    methods: ["GET"]
EOF
```

Set Reviews Viewer
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: "reviews-viewer"
 namespace: default
spec:
 selector:
  matchLabels:
   app: reviews
 action: ALLOW
 rules:
 - from:
  - source:
    principals: ["cluster.local/ns/default/sa/bookinfo-productpage"]
  to:
  - operation:
    methods: ["GET"]
EOF
```

Set Ratings Viewer
Copy
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: "ratings-viewer"
 namespace: default
spec:
 selector:
  matchLabels:
   app: ratings
 action: ALLOW
 rules:
 - from:
  - source:
    principals: ["cluster.local/ns/default/sa/bookinfo-reviews"]
  to:
  - operation:
    methods: ["GET"]
EOF
```

View the product page from a browser without any errors.
To revert the applied policies, enter the following commands.
Copy
```
kubectl delete authorizationpolicy.security.istio.io/allow-nothing
kubectl delete authorizationpolicy.security.istio.io/productpage-viewer
kubectl delete authorizationpolicy.security.istio.io/details-viewer
kubectl delete authorizationpolicy.security.istio.io/reviews-viewer
kubectl delete authorizationpolicy.security.istio.io/ratings-viewer
```

### Securing Gateways with TLS
We can expose the Bookinfo application as a secure HTTPS service using either simple or mutual TLS. To sign the certificates for your services, create a root certificate and private key:
Copy
```
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=example Inc./CN=example.com' -keyout example.com.key -out example.com.crt
```

Create a certificate and a private key for `productpage.bookinfo.com`.
Copy
```
openssl req -out bookinfo.example.com.csr -newkey rsa:2048 -nodes -keyout bookinfo.example.com.key -subj "/CN=bookinfo.example.com/O=bookinfo organization"
openssl x509 -req -days 365 -CA example.com.crt -CAkey example.com.key -set_serial 0 -in bookinfo.example.com.csr -out bookinfo.example.com.crt
```

Ensure you have deployed the Bookinfo application. Create a secret for the ingress gateway certificates.
Copy
```
kubectl create -n istio-system secret tls bookinfo-credential --key=bookinfo.example.com.key --cert=bookinfo.example.com.crt
```

Update the Bookinfo gateway to include a secure port.
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
 name: bookinfo-gateway-https
spec:
 selector:
  istio: ingressgateway
 servers:
 - port:
   number: 443
   name: https
   protocol: HTTPS
  tls:
   mode: SIMPLE
   credentialName: bookinfo-credential
  hosts:
  - bookinfo.example.com
EOF
```

Create Bookinfo destination rules if not already created.
Copy
```
kubectl apply -f samples/bookinfo/networking/destination-rule-all.yaml
```

Create a virtual service bound to the gateway.
Copy
```
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: bookinfo-https
spec:
 hosts:
 - "bookinfo.example.com"
 gateways:
 - bookinfo-gateway-https
 http:
 - route:
  - destination:
    host: productpage
    subset: v1
EOF
```

You can verify TLS connection to the gateway with the following `curl` command.
Copy
```
curl -v -HHost:bookinfo.example.com --resolve "bookinfo.example.com:443:$INGRESS_HOST" --cacert example.com.crt "https://bookinfo.example.com/productpage"
```

Was this article helpful?
YesNo

