Updated 2024-06-05
# Creating IngressClassParameters, IngressClass, and Ingress Resources
_Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller._
Having installed the OCI native ingress controller (either as a standalone program or as a cluster add-on), you have to create a number of different Kubernetes resources in order to use it:
  * **`IngressClassParameters`resource:** This custom resource specifies details of the OCI load balancer to create for the OCI native ingress controller. 
  * **`IngressClass`resource:** This resource is used to create a new load balancer. The `IngressClass` resource refers to the `IngressClassParameters` resource for the shape of the load balancer to create, and specifies whether the OCI native ingress controller is the default controller for `Ingress` resources. 
  * **`Ingress`resource:** This resource specifies rules to route external traffic to backend services.


Create each of the resources in turn by defining the resource in a .yaml file as shown in this topic, and then running the kubectl create command to create each resource.
## Create IngressClassParameters resource 🔗 
Use the custom `IngressClassParameters` resource to specify details of the OCI load balancer to create for the OCI native ingress controller.
Define the resource in a .yaml file. Here's a minimal example:
Copy
```
apiVersion: "ingress.oraclecloud.com/v1beta1"
kind: IngressClassParameters
metadata:
 name: <icp-name>
 namespace: <ns-name>
spec:
 compartmentId: "<compartment-ocid>"
 subnetId: "<subnet-ocid>"
 loadBalancerName: "<lb-name>"
 isPrivate: false
 maxBandwidthMbps: <max-bw>
 minBandwidthMbps: <min-bw>
 reservedPublicAddressId: <reserved-ip-ocid>
```

where:
  * `name: <icp-name>` is the name of the new `IngressClassParameters` resource
  * `name: <ns-name>` is the name of the namespace in which to create the new `IngressClassParameters` resource.
  * `compartmentId: "<compartment-ocid>"` is the OCID of the compartment that you want the new load balancer to belong to.
  * `subnetId: "<subnet-ocid>"` is the OCID of the load balancer's subnet.
  * `loadBalancerName: "<lb-name>"` is the name to give the new load balancer.
  * `maxBandwidthMbps: <max-bw>` is the upper amount of bandwidth that you want the new load balancer to support during time of peak workload.
  * `minBandwidthMbps: <min-bw>` is the amount of bandwidth that you want the new load balancer to always have available to provide instant readiness for workloads.
  * `reservedPublicAddressId: <reserved-ip-ocid>` is optionally the OCID of an existing reserved public IP address resource to use for the load balancer. If you don't specify a reserved public IP address, the load balancer is assigned a random IP address. For more information about creating a reserved public IP address, see [Creating a Reserved Public IP](https://docs.oracle.com/iaas/Content/Network/Tasks/reserved-public-ip-create.htm).


For example:
```
apiVersion: "ingress.oraclecloud.com/v1beta1"
kind: IngressClassParameters
metadata:
 name: native-ic-params
 namespace: acme-namespace
spec:
 compartmentId: "ocid1.compartment.oc1..aaaaaaaa______ddq"
 subnetId: "ocid1.subnet.oc1.iad.aaaaaaaa______dba"
 loadBalancerName: "native-ic-lb"
 isPrivate: false
 maxBandwidthMbps: 400
 minBandwidthMbps: 100
```

Create the resource by entering `kubectl create -f <filename>.yaml`
## Create IngressClass resource 🔗 
Use the `IngressClass` resource to associate an `Ingress` resource with the OCI native ingress controller and the `IngressClassParameters` resource. You can also use the `IngressClass` resource to specify whether the OCI native ingress controller is the default controller for `Ingress` resources.
Define the resource in a .yaml file. Here's a minimal example:
Copy
```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
 name: <ic-name>
 annotations:
  ingressclass.kubernetes.io/is-default-class: "<true|false>"
spec:
 controller: oci.oraclecloud.com/native-ingress-controller
 parameters:
  scope: Namespace
  namespace: <ns-name>
  apiGroup: ingress.oraclecloud.com
  kind: ingressclassparameters
  name: <icp-name>
```

where:
  * `name: <ic-name>` is the name of the new `IngressClass` resource
  * `ingressclass.kubernetes.io/is-default-class: "<true|false>"` indicates whether this `IngressClass` is the default `IngressClass` to use if an `Ingress` resource does not explicitly specify an `ingressClassName`. It is recommended to specify a default `IngressClass.`
  * `controller: oci.oraclecloud.com/native-ingress-controller` specifies the OCI native ingress controller as the ingress controller to use
  * `namespace: <ns-name>` is the name of the namespace containing the parameters to use when `.spec.parameters.scope` is set to `Namespace`.
  * `name: <icp-name>` is the name of the `IngressClassParameters` resource that specifies details of the OCI load balancer to create for the OCI native ingress controller.


For example:
```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
 name: native-ic-ingress-class
 annotations:
  ingressclass.kubernetes.io/is-default-class: "true"
spec:
 controller: oci.oraclecloud.com/native-ingress-controller
 parameters:
  scope: Namespace
  namespace: acme-namespace
  apiGroup: ingress.oraclecloud.com
  kind: ingressclassparameters
  name: native-ic-params
```

Create the resource by entering `kubectl create -f <filename>.yaml`
## Create Ingress resource 🔗 
Use the `Ingress` resource to specify rules to route external traffic to backend services.
Define the resource in a .yaml file. Here's a minimal example:
Copy
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 name: <i-name>
spec:
 ingressClassName: <ic-name>
 rules:
  <ingress-rule>

```

where:
  * `name: <i-name>` is the name of the `Ingress` resource.
  * `ingressClassName: <ic-name>` is the name of the `IngressClass` resource to use. The `IngressClass` resource specifies both the ingress controller to use, and the name of the `IngressClassParameters` resource that contains details of the OCI load balancer to create for the OCI native ingress controller. If `ingressClassName` is not specified, the cluster's default `IngressClass` is used (the `IngressClass `that has the annotation `ingressclass.kubernetes.io/is-default-class: "true"`).
  * `<ingress-rule>` is a rule optionally comprising a host and/or one (or more) path elements. Each path has a backend (a service name and port number). The ingress controller routes requests that match a rule's host name (if specified) and path to the associated backend. When specifying a path in a rule:
    * use `pathType: Exact` to indicate that the incoming request path must exactly match the path in the rule for the request to be routed to the rule's associated backend
    * use `pathType:Prefix` to indicate that the beginning portion of the incoming request path must match the path in the rule for the request to be routed to the rule's associated backend
See [Specifying Route Rules for the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-specifyingrouterules).


For example:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 name: native-ic-ingress
spec:
 ingressClassName: native-ic-ingress-class
 rules:
  - host: "foo.bar.com"
   http:
    paths:
     - pathType: Exact
      path: "/testecho1"
      backend:
       service:
        name: testecho1
        port:
         number: 80
```

Create the resource by entering `kubectl create -f <filename>.yaml`
Was this article helpful?
YesNo

