Updated 2025-01-29
# Provisioning OCI Load Balancers for Kubernetes Services of Type LoadBalancer
_Find out how to provision an OCI load balancer for a Kubernetes service of type LoadBalancer using Kubernetes Engine (OKE)._
An OCI load balancer is an OSI layer 4 (TCP) and layer 7 (HTTP) proxy, which supports features such as SSL termination and advanced HTTP routing policies. It provides the utmost flexibility, with responsive scaling up and down. You choose a custom minimum bandwidth and an optional maximum bandwidth, both between 10 Mbps and 8,000 Mbps. The minimum bandwidth is always available and provides instant readiness for your workloads. 
For more information about OCI load balancers, see [Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm).
Provisioning an OCI load balancer for a Kubernetes service of type LoadBalancer enables you to:
  * load balance transport Layer 4 and Layer 7 (TCP and HTTP) traffic
  * terminate SSL/TLS at the load balancer


Note that when Kubernetes Engine provisions an OCI load balancer for a Kubernetes service of type LoadBalancer, security rules to allow inbound and outbound traffic to and from the load balancer's subnet are created automatically by default. See [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).
Use OCI load balancer metrics to monitor the health of an OCI load balancer provisioned for a Kubernetes service of type LoadBalancer (see [Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm)).
## Specifying the Annotation for an OCI Load Balancer 🔗 
To provision an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, define a service of type LoadBalancer that includes the following annotation in the metadata section of the manifest file:```
oci.oraclecloud.com/load-balancer-type: "lb"
```

Note that `lb` is the default value of the `oci.oraclecloud.com/load-balancer-type` annotation. If you do not explicitly include the annotation in the service definition, the default value of the annotation is used.
For example, consider the following configuration file, `nginx_lb.yaml`. It defines a deployment (`kind: Deployment`) for the `nginx` app, followed by a definition of a service of type of LoadBalancer (`type: LoadBalancer`) that balances http traffic on port 80 for the `nginx` app. 
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: my-nginx
 labels:
  app: nginx
spec:
 replicas: 3
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

The first part of the configuration file defines an Nginx deployment, requesting that it be hosted on 3 pods running the `nginx:latest` image, and accept traffic to the containers on port 80.
The second part of the configuration file defines the Nginx service, which uses type LoadBalancer to balance Nginx traffic on port 80 amongst the available pods.
To create the deployment and service defined in `nginx_lb.yaml` while connected to your Kubernetes cluster, enter the command:
Command
CopyTry It
```
kubectl apply -f nginx_lb.yaml
```

This command outputs the following upon successful creation of the deployment and the load balancer:
```
deployment "my-nginx" created
service "my-nginx-svc" created
```

The load balancer may take a few minutes to go from a pending state to being fully operational. You can view the current state of your cluster by entering:
Command
CopyTry It
```
kubectl get all
```

The output from the above command shows the current state:
Copy
```

NAME                 READY   STATUS  RESTARTS  AGE
po/my-nginx-431080787-0m4m8      1/1    Running  0     3m
po/my-nginx-431080787-hqqcr      1/1    Running  0     3m
po/my-nginx-431080787-n8125      1/1    Running  0     3m
NAME        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
svc/kubernetes   203.0.113.1   <NONE>      443/TCP    3d
svc/my-nginx-svc  203.0.113.7   192.0.2.22    80:30269/TCP  3m
NAME           DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
deploy/my-nginx      3     3     3      3      3m
NAME              DESIRED  CURRENT  READY   AGE
rs/my-nginx-431080787      3     3     3     3m

```

The output shows that the `my-nginx` deployment is running on 3 pods (the po/my-nginx entries), that the load balancer is running (svc/my-nginx-svc) and has an external IP (192.0.2.22) that clients can use to connect to the app that's deployed on the pods.
## Terminating SSL/TLS at the Load Balancer 🔗 
When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can specify that you want to terminate SSL at the load balancer. This configuration is known as frontend SSL. To implement frontend SSL, you define a listener at a port such as 443, and associate an SSL certificate with the listener.
Note that you can implement full point-to-point SSL encryption between clients and application pods running on worker nodes. To do so, create a load balancer with SSL termination (as described in this section), and also associate an SSL certificate with the load balancer's backend set (see [Implementing SSL/TLS between the Load Balancer and Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-SSLbetweenLBandbackend)).
This example provides a walkthrough of the configuration and creation of a load balancer with SSL support.
Consider the following configuration file, `nginx-demo-svc-ssl.yaml`, which defines an Nginx deployment and exposes it via a load balancer that serves http on port 80, and https on port 443. This sample creates an Oracle Cloud Infrastructure load balancer, by defining a service with a type of LoadBalancer (`type: LoadBalancer`).
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
spec:
 replicas: 2
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx
    ports:
    - containerPort: 80
---
kind: Service
apiVersion: v1
metadata:
 name: nginx-service
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
  oci.oraclecloud.com/oci-load-balancer-listener-ssl-config: '{"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1", "Protocols":["TLSv1.3"]}'
  service.beta.kubernetes.io/oci-load-balancer-tls-secret: ssl-certificate-secret
spec:
 selector:
  app: nginx
 type: LoadBalancer
 ports:
 - name: http
  port: 80
  targetPort: 80
 - name: https
  port: 443
  targetPort: 80
```

The load balancer's annotations are of particular importance, as described here. 
The ports on which to support https traffic are defined by the value of the **service.beta.kubernetes.io/oci-load-balancer-ssl-ports** annotation. You can declare multiple SSL ports by using a comma-separated list for the annotation's value. For example, you could set the annotation's value to "443, 3000" to support SSL on ports 443 and 3000.
The cipher suite to use with the load balancer is defined by the value of the **oci.oraclecloud.com/oci-load-balancer-listener-ssl-config** annotation. Cipher suites determine the security, compatibility, and speed of HTTPS traffic (for more information, see [Cipher Suites for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites.htm)). You specify both the cipher suite name (for example, oci-default-http2-tls-12-13-ssl-cipher-suite-v1) and the TLS version (for example, TLSv1.3). You can specify a predefined cipher suite preconfigured by Oracle Cloud Infrastructure (see [Predefined Load Balancer Cipher Suites](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm)), or a cipher suite you have created yourself. If you don't include the **oci.oraclecloud.com/oci-load-balancer-listener-ssl-config** annotation but you do include the **service.beta.kubernetes.io/oci-load-balancer-tls-secret** annotation, the oci-default-ssl-cipher-suite-v1 cipher suite is used.
The required TLS secret, **ssl-certificate-secret** , needs to be created in Kubernetes. This example creates and uses a self-signed certificate. However, in a production environment, the most common scenario is to use a public certificate that's been signed by a certificate authority.
The following command creates a self-signed certificate, `tls.crt`, with its corresponding key, `tls.key`:
Command
CopyTry It
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=nginxsvc/O=nginxsvc"

```

Now that you created the certificate, you need to store both it and its key as a secret in Kubernetes. The name of the secret must match the name from the **service.beta.kubernetes.io/oci-load-balancer-tls-secret** annotation of the load balancer's definition. Use the following command to create a TLS secret in Kubernetes, whose key and certificate values are set by `--key` and `--cert`, respectively.
Command
CopyTry It
```
kubectl create secret tls ssl-certificate-secret --key tls.key --cert tls.crt

```

You must create the Kubernetes secret before you can create the service, since the service references the secret in its definition. Create the service using the following command:
Command
CopyTry It
```
kubectl create -f manifests/demo/nginx-demo-svc-ssl.yaml

```

Watch the service and wait for a public IP address (EXTERNAL-IP) to be assigned to the Nginx service (nginx-service) by entering:
Command
CopyTry It
```
kubectl get svc --watch
```

The output from the above command shows the load balancer IP to use to connect to the service.
Copy
```

NAME      CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
nginx-service  192.0.2.1   198.51.100.1   80:30274/TCP  5m

```

The load balancer is now running, which means the service can now be accessed as follows:
  * using http, by entering:
Command
CopyTry It
```
curl http://198.51.100.1
```

  * using https, by entering:
Command
CopyTry It
```
curl --insecure https://198.51.100.1
```

The "`--insecure`" flag is used to access the service using https due to the use of self-signed certificates in this example. Do not use this flag in a production environment where the public certificate was signed by a certificate authority.


**Note:** When a cluster is deleted, a load balancer that's dynamically created when a service is created will not be removed. Before deleting a cluster, delete the service, which in turn will result in the removal of the load balancer. The syntax for this command is:
Command
CopyTry It
```
kubectl delete svc  _SERVICE_NAME_
```

For example, to delete the service from the previous example, enter:
Command
CopyTry It
```
kubectl delete svc nginx-service

```

### Updating the TLS Certificates of Existing Load Balancers 🔗 
To update the TLS certificate of an existing load balancer:
  1. Obtain a new TLS certificate. In a production environment, the most common scenario is to use a public certificate that's been signed by a certificate authority.
  2. Create a new Kubernetes secret. For example, by entering:
Command
CopyTry It
```
kubectl create secret tls new-ssl-certificate-secret --key new-tls.key --cert new-tls.crt

```

  3. Modify the service definition to reference the new Kubernetes secret by changing the `service.beta.kubernetes.io/oci-load-balancer-tls-secret` annotation in the service configuration. For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: nginx-service
 annotations:
  service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
  service.beta.kubernetes.io/oci-load-balancer-tls-secret: new-ssl-certificate-secret
spec:
 selector:
  app: nginx
 type: LoadBalancer
 ports:
 - name: http
  port: 80
  targetPort: 80
 - name: https
  port: 443
  targetPort: 80
```

  4. Update the service. For example, by entering:
Command
CopyTry It
```
kubectl apply -f new-nginx-demo-svc-ssl.yaml
```



## Implementing SSL/TLS between the Load Balancer and Worker Nodes 🔗 
When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can specify that you want to implement SSL between the load balancer and the backend servers (worker nodes) in the backend set. This configuration is known as backend SSL. To implement backend SSL, you associate an SSL certificate with the load balancer's backend set.
Note that you can implement full point-to-point SSL encryption between clients and application pods running on worker nodes. To do so, associate an SSL certificate with the load balancer's backend set (as described in this section), and also create a load balancer with SSL termination (see [Terminating SSL/TLS at the Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps)).
Cipher suites determine the security, compatibility, and speed of HTTPS traffic (for more information, see [Cipher Suites for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites.htm)). To specify the cipher suite to use with the load balancer's backend set, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config: '{"CipherSuiteName":"<cipher-suite-name>", "Protocols":["<tls-version>"]}'
```

where:
  * `"CipherSuiteName":"<cipher-suite-name>"` is the name of a predefined cipher suite preconfigured by Oracle Cloud Infrastructure (see [Predefined Load Balancer Cipher Suites](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm)), or a cipher suite you have created yourself. For example, `"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1"`
  * `"Protocols":["<tls-version>"]` specifies one or more TLS versions, in a comma-delimited list. For example, `"Protocols":["TLSv1.2", "TLSv1.3"]`


For example:
```
oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config: '{"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1", "Protocols":["TLSv1.2", "TLSv1.3"]}'
```

If you don't include the `oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config` annotation but you do include the `service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret` annotation, the oci-wider-compatible-ssl-cipher-suite-v1 cipher suite is used.
To specify the certificate to associate with the backend set, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret: <value>
```

where `<value>` is the name of a Kubernetes secret you've created to contain a signed certificate and the private key to the certificate. Note that you must create the Kubernetes secret before you can create the service, since the service references the secret in its definition.
The following example creates and uses a self-signed certificate, which is usually acceptable for internal communication between the load balancer and the backend set. However, if you prefer, you could use a public certificate that's been signed by a certificate authority.
For example:
  1. Generate a private key by entering:
`openssl genrsa -out ca.key 2048`
  2. Generate a certificate by entering:
`openssl req -x509 -new -nodes -key ca.key -subj "/CN=nginxsvc/O=nginxsvc" -days 10000 -out ca.crt`
  3. Store the certificate and the key as a secret in Kubernetes by entering:
`kubectl create secret generic ca-ser-secret --from-file=tls.crt=tls.crt --from-file=tls.key=tls.key --from-file=ca.crt=ca.crt`
  4. Define an Nginx deployment and expose it via a load balancer that serves http on port 80, and https on port 443. 


This example creates an Oracle Cloud Infrastructure load balancer, by defining a service with a type of LoadBalancer `(type: LoadBalancer`). ```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
spec:
 replicas: 2
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx
    ports:
    - containerPort: 80
---
apiVersion: v1
metadata:
 name: nginx-service
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config: '{"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1", "Protocols":["TLSv1.2", "TLSv1.3"]}'
  service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret: ca-ser-secret
  service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443" 
spec:
 selector:
  app: nginx
 type: LoadBalancer
 ports:
 - name: http
  port: 80
  targetPort: 80
 - name: https
  port: 443
  targetPort: 443
```

Communication between the load balancer and the worker nodes in the backend set is encrypted using the key and certificate stored in the `ca-ser-secret` Kubernetes secret that you created earlier.
## Specifying Alternative Load Balancer Shapes 🔗 
The shape of an Oracle Cloud Infrastructure load balancer specifies its maximum total bandwidth (that is, ingress plus egress). By default, load balancers are created with a shape of 100Mbps. Other shapes are available, including 400Mbps and 8000Mbps. 
To specify an alternative shape for a load balancer, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-shape: <value>
```

where `value` is the bandwidth of the shape (for example, 100Mbps, 400Mbps, 8000Mbps).
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-shape: 400Mbps
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Sufficient load balancer quota must be available in the region for the shape you specify. Enter the following kubectl command to confirm that load balancer creation did not fail due to lack of quota:
Command
CopyTry It
```
kubectl describe service <service-name>
```

Note that Oracle recommends you implement Kubernetes services of type LoadBalancer as cost-efficient flexible load balancers rather than as fixed-shape (dynamic) load balancers (see [Specifying Flexible Load Balancer Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#flexible)). 
## Specifying Flexible Load Balancer Shapes 🔗 
The shape of an Oracle Cloud Infrastructure load balancer specifies its maximum total bandwidth (that is, ingress plus egress). As described in [Specifying Alternative Load Balancer Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#Specifyi), you can specify different load balancer shapes.
In addition, you can also specify a flexible shape for an Oracle Cloud Infrastructure load balancer, by defining a minimum and a maximum bandwidth for the load balancer.
To specify a flexible shape for a load balancer, add the following annotations in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-shape: "flexible"
service.beta.kubernetes.io/oci-load-balancer-shape-flex-min: "<min-value>"
service.beta.kubernetes.io/oci-load-balancer-shape-flex-max: "<max-value>"
```

where:
  * `"<min-value>"` is the minimum bandwidth for the load balancer, in Mbps (for example, "10")
  * `"<max-value>"` is the maximum bandwidth for the load balancer, in Mbps (for example, "100")


Note that you do not include a unit of measurement when specifying bandwidth values for flexible load balancer shapes (unlike for pre-defined shapes). For example, specify the minimum bandwidth as `10` rather than as `10Mbps`.
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-shape: "flexible"
  service.beta.kubernetes.io/oci-load-balancer-shape-flex-min: "10"
  service.beta.kubernetes.io/oci-load-balancer-shape-flex-max: "100"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

## Specifying Load Balancer Connection Timeout 🔗 
When provisioning an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, you can specify the maximum idle time (in seconds) allowed between two successive receive or two successive send operations between the client and backend servers. 
To explicitly specify a maximum idle time, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-connection-idle-timeout: <value>
```

where `value` is the number of seconds.
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-connection-idle-timeout: 100
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you don't explicitly specify a maximum idle time, a default value is used. The default value depends on the type of listener:
  * for TCP listeners, the default maximum idle time is 300 seconds
  * for HTTP listeners, the default maximum idle time is 60 seconds


## Specifying Listener Protocols 🔗 
When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can define the type of traffic accepted by the listener by specifying the protocol on which the listener accepts connection requests.
Note that if you don't explicitly specify a protocol, "TCP" is used as the default value.
To explicitly specify the load balancer listener protocol when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-backend-protocol: <value>
```

where `<value>` is the protocol that defines the type of traffic accepted by the listener. For example, "HTTP". Valid protocols include "HTTP", "TCP", and "GRPC". 
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-backend-protocol: "HTTP"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note that if you specify GRPC as the protocol, you must configure both of the following:
  * Frontend SSL, using the **service.beta.kubernetes.io/oci-load-balancer-ssl-ports** , **oci.oraclecloud.com/oci-load-balancer-ssl-listener-config** , and **service.beta.kubernetes.io/oci-load-balancer-tls-secret** annotations. For more information, see [Terminating SSL/TLS at the Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps). 
  * Backend SSL, using the **oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config** and**service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret** annotations. For more information, see [Implementing SSL/TLS between the Load Balancer and Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-SSLbetweenLBandbackend). 


For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: hello-grpc-service
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
  service.beta.kubernetes.io/oci-load-balancer-tls-secret: ssl-certificate-secret
  service.beta.kubernetes.io/oci-load-balancer-backend-protocol: "GRPC"
  oci.oraclecloud.com/oci-load-balancer-listener-ssl-config: '{"CipherSuiteName":"oci-default-http2-ssl-cipher-suite-v1", "Protocols":["TLSv1.2"]}'
  oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config: '{"CipherSuiteName":"oci-default-http2-ssl-cipher-suite-v1", "Protocols":["TLSv1.2"]}'
  service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret: ca-ser-secret
spec:
 type: LoadBalancer
 selector:
  app: hello-grpc
 ports:
  - port: 443
   name: grpc
   targetPort: 50051
```

## Specifying Security List Management Options When Provisioning an OCI Load Balancer 🔗 
**Note**
You might encounter scalability and other issues if you use the Kubernetes security list management feature in complex deployments, and with tools like Terraform. For these reasons, Oracle does not recommend using the Kubernetes security list management feature in production environments.
Also note that the ability to use security lists to manage security rules will be deprecated in a future release. For this reason, Oracle recommends the use of network security groups (NSGs) and the `oci.oraclecloud.com/security-rule-management-mode` annotation (see [Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options)).
You can use the security list management feature to configure how security list rules are managed for an Oracle Cloud Infrastructure load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer. This feature is useful if you are new to Kubernetes, or for basic deployments.
To specify how the Kubernetes security list management feature manages security lists when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:
Copy
```
service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: <value>
```

where `<value>` is one of:
  * `"None"`: (recommended) No security list management is enabled. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. Additionally, you have to set up security rules to allow inbound traffic to load balancers (see [Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers)).
  * `"All"`: (default) All required security list rules for load balancer services are managed.
  * `"Frontend"`: Only security list rules for ingress to load balancer services are managed. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges.


Oracle recommends that you explicitly set `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode` to `None`.
In clusters with managed nodes, if you don't explicitly specify a management mode or you specify an invalid value, all security list rules are managed (equivalent to `"All"`). Be aware that in this case, Kubernetes Engine creates a security rule that allows inbound traffic from 0.0.0.0/0 (or from the source port ranges specified in the manifest file) to listener ports. In clusters with virtual nodes, security list management is never enabled and you always have to manually configure security rules (equivalent to `"None"`).
Note that there are limits to the number of ingress and egress rules that are allowed in a security list (see [Security List Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#sec_list_limits)). If the number of ingress or egress rules exceeds the limit, and `<value>` is set to `"All"` or `"Frontend"`, creating or updating the load balancer fails.
For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/load-balancer-type: "lb"
  service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "Frontend"
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Was this article helpful?
YesNo

