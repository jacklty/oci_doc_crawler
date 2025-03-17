Updated 2024-08-14
# Example: Setting Up an Nginx Ingress Controller on a Cluster
_Find out how to set up and use an example Nginx ingress controller on a cluster you've created using Kubernetes Engine (OKE)._
You can set up different open source ingress controllers on clusters you have created with Kubernetes Engine to manage Kubernetes application traffic.
This topic explains how to set up an example Nginx ingress controller along with corresponding access control on an existing cluster. Having set up the ingress controller, this topic describes how to use the ingress controller with an example hello-world backend, and how to verify the ingress controller is working as expected. If you want to continue using the example ingress controller, follow the upgrade instructions. And when you have no further use for the example ingress controller, this topic shows you how to delete it.
## Example Components 🔗 
The example includes an ingress controller and a hello-world backend.
### Ingress Controller Components
The ingress controller comprises:
  * An ingress controller deployment called `ingress-nginx-controller`. The deployment deploys an image that contains the binary for the ingress controller and Nginx. The binary manipulates and reloads the `/etc/nginx/nginx.conf` configuration file when an ingress is created in Kubernetes. Nginx upstreams point to services that match specified selectors.
  * An ingress controller service called `ingress-nginx-controller`. The service exposes the ingress controller deployment as a service of type LoadBalancer. Because Kubernetes Engine uses an Oracle Cloud Infrastructure integration/cloud-provider, a load balancer will be dynamically created with the correct nodes configured as a backend set.


### Backend Components
The hello-world backend comprises:
  * A backend deployment called `docker-hello-world`. The deployment handles default routes for health checks and 404 responses. This is done by using a stock hello-world image that serves the minimum required routes for a default backend.
  * A backend service called `docker-hello-world-svc`.The service exposes the backend deployment for consumption by the ingress controller deployment.


## Setting Up the Example Ingress Controller 🔗 
In this section, you create the access rules for ingress. You then create the example ingress controller components, and confirm they are running.
### Creating the Access Rules for the Ingress Controller
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. If your Oracle Cloud Infrastructure user is a tenancy administrator, skip the next step and go straight to [Deploying the Ingress Controller and associated resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm#settingupcontroller__creatingserviceaccount).
  3. If your Oracle Cloud Infrastructure user is not a tenancy administrator, in a terminal window, grant the user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:
Command
CopyTry It
```
kubectl create clusterrolebinding <my-cluster-admin-binding> --clusterrole=cluster-admin --user=<user-OCID>
```

where:
     * `<my-cluster-admin-binding>` is a string of your choice to be used as the name for the binding between the user and the Kubernetes RBAC cluster-admin clusterrole. For example, `jdoe_clst_adm`
     * `<user-OCID>` is the user's OCID (obtained from the Console ). For example, `ocid1.user.oc1..aaaaa...zutq` (abbreviated for readability).
For example:
Command
CopyTry It
```
kubectl create clusterrolebinding jdoe_clst_adm --clusterrole=cluster-admin --user=ocid1.user.oc1..aaaaa...zutq
```



### Deploying the Ingress Controller and associated resources 🔗 
How to deploy the ingress controller and associated resources (including the Kubernetes RBAC roles and bindings, and the `ingress-nginx-controller` ingress controller service of type LoadBalancer) depends on whether you are deploying into a cluster with managed/self-managed nodes, or into a cluster with virtual nodes:
  * **Managed nodes and self-managed nodes**
To deploy the Nginx ingress controller, run the following command:
Command
CopyTry It
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v<vnum>/deploy/static/provider/cloud/deploy.yaml
```

where `<vnum>` is the version number of the latest version of the `ingress-nginx-controller` ingress controller deployment script. For example, at the time of writing, the latest version of the script has the version number 1.1.3, so the command to run is:
Command
CopyTry It
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.3/deploy/static/provider/cloud/deploy.yaml
```

To find out the version number of the latest version of the script, see the [kubernetes/ingress-nginx documentation on GitHub](https://github.com/kubernetes/ingress-nginx).
  * **Virtual nodes**
On virtual nodes, you have to modify the ingresss controller's deployment manifest and comment out the `fsgroup`, `allowprivilegeEscalation`, and `capabilities` security contexts. For an example of such a modified deployment manifest, see <https://github.com/oracle-devrel/oci-oke-virtual-nodes/tree/main/ingress-nginx>.
To deploy the Nginx ingress controller based on this modified manifest, run the following command:
Command
CopyTry It
```
kubectl apply -f https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/ingress-nginx/deploy.yaml
```



### Verifying the `ingress-nginx-controller` Ingress Controller Service is Running as a Load Balancer Service
  1. View the list of running services by entering:
Command
CopyTry It
```
kubectl get svc -n ingress-nginx
```

The output from the above command shows the services that are running:
Copy
```

NAME            TYPE      CLUSTER-IP   EXTERNAL-IP  PORT(S)            AGE
ingress-nginx-controller  LoadBalancer  10.96.229.38  <pending>   80:30756/TCP,443:30118/TCP  1h

```

The EXTERNAL-IP for the `ingress-nginx-controller` ingress controller service is shown as `<pending>` until the load balancer has been fully created in Oracle Cloud Infrastructure.
  2. Repeat the `kubectl get svc` command until an EXTERNAL-IP is shown for the `ingress-nginx-controller` ingress controller service:
Command
CopyTry It
```
kubectl get svc -n ingress-nginx

```

The output from the above command shows the EXTERNAL-IP for the `ingress-nginx-controller` ingress controller service:
Copy
```

NAME            TYPE      CLUSTER-IP   EXTERNAL-IP    PORT(S)            AGE
ingress-nginx-controller  LoadBalancer  10.96.229.38  129.146.214.219  80:30756/TCP,443:30118/TCP  1h
```



### Creating the TLS Secret
A TLS secret is used for SSL termination on the ingress controller. 
  1. Output a new key to a file. For example, by entering:
Command
CopyTry It
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=nginxsvc/O=nginxsvc"
```

To generate the secret for this example, a self-signed certificate is used. While this is okay for testing, for production, use a certificate signed by a Certificate Authority.
**Note** Under Windows, you may need to replace `"/CN=nginxsvc/O=nginxsvc"` with `"//CN=nginxsvc\O=nginxsvc"` . For example, this is necessary if you run the `openssl` command from a Git Bash shell.
  2. Create the TLS secret by entering:
Command
CopyTry It
```
kubectl create secret tls tls-secret --key tls.key --cert tls.crt
```



## Setting Up the Example Backend 🔗 
In this section, you define a hello-world backend service and deployment.
### Creating the docker-hello-world Service Definition
  1. Create the file `hello-world-ingress.yaml` containing the following code. This code uses a publicly available hello-world image from Docker Hub. You can substitute another image of your choice that can be run in a similar manner.
Copy
```

apiVersion: apps/v1
kind: Deployment
metadata:
 name: docker-hello-world
 labels:
  app: docker-hello-world
spec:
 selector:
  matchLabels:
   app: docker-hello-world
 replicas: 3
 template:
  metadata:
   labels:
    app: docker-hello-world
  spec:
   containers:
   - name: docker-hello-world
    image: scottsbaldwin/docker-hello-world:latest
    ports:
    - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
 name: docker-hello-world-svc
spec:
 selector:
  app: docker-hello-world
 ports:
  - port: 8088
   targetPort: 80
 type: ClusterIP

```

Note the docker-hello-world service's type is ClusterIP, rather than LoadBalancer, because this service will be proxied by the `ingress-nginx-controller` ingress controller service. The docker-hello-world service does not need public access directly to it. Instead, the public access will be routed from the load balancer to the ingress controller, and from the ingress controller to the upstream service.
  2. Create the new hello-world deployment and service on nodes in the cluster by running the following command:
Command
CopyTry It
```
kubectl create -f hello-world-ingress.yaml
```



## Using the Example Ingress Controller to Access the Example Backend 🔗 
In this section you create an ingress to access the backend using the ingress controller.
### Creating the Ingress Resource
  1. Create the file `ingress.yaml` and populate it with this code:
Copy
```

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 name: hello-world-ing
 annotations:
  kubernetes.io/ingress.class: "nginx"
spec:
 tls:
 - secretName: tls-secret
 rules:
 - http:
   paths:
    - path: /
     pathType: Prefix
     backend:
      service:
       name: docker-hello-world-svc
       port:
        number: 8088

```

Note that the above example YAML works with clusters running Kubernetes version 1.19.x and later.
  2. Create the resource by entering:
Command
CopyTry It
```
kubectl create -f ingress.yaml
```



## Verifying that the Example Components are Working as Expected 🔗 
In this section, you confirm that all of the example components have been successfully created and are operating as expected. The `docker-hello-world-svc` service should be running as a ClusterIP service, and the `ingress-nginx-controller` service should be running as a LoadBalancer service. Requests sent to the ingress controller should be routed to nodes in the cluster.
### Obtaining the External IP Address of the Load Balancer
To confirm the `ingress-nginx-controller` service is running as a LoadBalancer service, obtain its external IP address by entering:
Command
CopyTry It
```
kubectl get svc --all-namespaces
```

The output from the above command shows the services that are running:
Copy
```

NAMESPACE    NAME             TYPE      CLUSTER-IP   EXTERNAL-IP   PORT(S)           AGE
default     docker-hello-world-svc   ClusterIP   10.96.83.247  <none>      8088/TCP           16s
default     kubernetes         ClusterIP   10.96.0.1    <none>      443/TCP           1h
ingress-nginx  ingress-nginx-controller  LoadBalancer  10.96.229.38  129.146.214.219 80:30756/TCP,443:30118/TCP  5m			
kube-system   kube-dns          ClusterIP   10.96.5.5    <none>      53/UDP,53/TCP        1h
```

### Sending cURL Requests to the Load Balancer
  1. Use the external IP address of the `ingress-nginx-controller` service (for example, 129.146.214.219) to curl an http request by entering:
Command
CopyTry It
```
curl -I http://129.146.214.219

```

Example output from the above command:
Copy
```
HTTP/1.1 301 Moved Permanently
Via: 1.1 10.68.69.10 (McAfee Web Gateway 7.6.2.10.0.23236)
Date: Thu, 07 Sep 2017 15:20:16 GMT
Server: nginx/1.13.2
Location: https://129.146.214.219/
Content-Type: text/html
Content-Length: 185
Proxy-Connection: Keep-Alive
Strict-Transport-Security: max-age=15724800; includeSubDomains;

```

The output shows a 301 redirect and a Location header that suggest that http traffic is being redirected to https. 
  2. Either cURL against the https url or add the `-L` option to automatically follow the location header. The `-k` option instructs cURL to not verify the SSL certificates. For example, by entering:
Command
CopyTry It
```
curl -ikL http://129.146.214.219
```

Example output from the above command:
Copy
```
HTTP/1.1 301 Moved Permanently
Via: 1.1 10.68.69.10 (McAfee Web Gateway 7.6.2.10.0.23236)
Date: Thu, 07 Sep 2017 15:22:29 GMT
Server: nginx/1.13.2
Location: https://129.146.214.219/
Content-Type: text/html
Content-Length: 185
Proxy-Connection: Keep-Alive
Strict-Transport-Security: max-age=15724800; includeSubDomains;
HTTP/1.0 200 Connection established
HTTP/1.1 200 OK
Server: nginx/1.13.2
Date: Thu, 07 Sep 2017 15:22:30 GMT
Content-Type: text/html
Content-Length: 71
Connection: keep-alive
Last-Modified: Thu, 07 Sep 2017 15:17:24 GMT
ETag: "59b16304-47"
Accept-Ranges: bytes
Strict-Transport-Security: max-age=15724800; includeSubDomains;
<h1>Hello webhook world from: docker-hello-world-1732906117-0ztkm</h1>

```

The last line of the output shows the HTML that is returned from the pod whose hostname is `docker-hello-world-1732906117-0ztkm`. 
  3. Issue the cURL request several times to see the hostname in the HTML output change, demonstrating that load balancing is occurring:
Copy
```
$ curl -k https://129.146.214.219
<h1>Hello webhook world from: docker-hello-world-1732906117-6115l</h1>
$ curl -k https://129.146.214.219
<h1>Hello webhook world from: docker-hello-world-1732906117-7r89v</h1>
$ curl -k https://129.146.214.219
<h1>Hello webhook world from: docker-hello-world-1732906117-0ztkm</h1>
```



### Inspecting nginx.conf
The `ingress-nginx-controller` ingress controller deployment manipulates the `nginx.conf` file in the pod within which it is running. 
  1. Find the name of the pod running the `ingress-nginx-controller` ingress controller deployment by entering:
Command
CopyTry It
```
kubectl get po -n ingress-nginx

```

The output from the above command shows the name of the pod running the `ingress-nginx-controller` ingress controller deployment:
Copy
```

NAME                    READY   STATUS  RESTARTS  AGE
ingress-nginx-controller-110676328-h86xg  1/1    Running  0     1h

```

  2. Use the name of the pod running the `ingress-nginx-controller` ingress controller deployment to show the contents of `nginx.conf` by entering the following `kubectl exec` command:
Command
CopyTry It
```
kubectl exec -n ingress-nginx -it ingress-nginx-controller-110676328-h86xg -- cat /etc/nginx/nginx.conf

```

  3. Look for `proxy_pass` in the output. There will be one for the default backend and another that looks similar to:
Copy
```
proxy_pass http://upstream_balancer;

```

This shows that Nginx is proxying requests to an upstream called `upstream_balancer`. 
  4. Locate the upstream definition in the output. It will look similar to:
Copy
```
upstream upstream_balancer {
        server 0.0.0.1:1234; # placeholder
        balancer_by_lua_block {
            tcp_udp_balancer.balance()
        }
    }

```

The upstream is proxying via Lua. 


## (Optional) Upgrading the Example Ingress Controller 🔗 
In this optional section, you find out how to carry on using the example ingress controller for Kubernetes application traffic management, rather than removing it immediately. 
If you want to, you can continue using the example ingress controller you created earlier. However, note that new versions of Nginx are released periodically. Therefore, if you do continue using the example ingress controller, you will periodically have to upgrade the version of Nginx that the ingress controller uses. Typically, you'll want to preserve the ingress controller's existing EXTERNAL-IP address when upgrading Nginx.
To upgrade the existing ingress controller without deleting the existing Oracle Cloud Infrastructure load balancer (and thereby preserve its existing EXTERNAL-IP address), follow the [Upgrading Nginx Without Helm](https://kubernetes.github.io/ingress-nginx/deploy/upgrade/#without-helm) instructions in the Nginx documentation. 
To determine which Nginx image to reference when upgrading Nginx, see the [Nginx Changelog](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md) in the Nginx documentation.
## (Optional) Removing the Example Ingress Controller 🔗 
In this optional section, you remove the example ingress controller you created earlier, including:
  * the `ingress-nginx-controller` ingress controller deployment
  * the Kubernetes RBAC roles and bindings
  * the `ingress-nginx-controller` ingress controller service of type LoadBalancer


Note that if you later decide to apply the ingress controller deployment script for a second time to re-create the example ingress controller, a new `ingress-nginx-controller` service of type LoadBalancer is created that has a different EXTERNAL-IP address to the previous service.
You do not have to remove the example ingress controller if you want to continue using it. However, if you do continue using the example ingress controller, you will periodically have to upgrade the version of Nginx that the ingress controller uses. See [(Optional) Upgrading the Example Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm#contengsettingupingresscontroller_topic-Housekeeping-Upgrade-ingress-controller).
### Removing the Example Ingress Controller
  1. Run the following command to remove the example ingress controller you created earlier:
Command
CopyTry It
```
kubectl delete -f <deployment-script-location>
```

where `<deployment-script-location>` is the location of the deployment script that you previously used to create the example ingress controller.
For example:
Command
CopyTry It
```
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.3/deploy/static/provider/cloud/deploy.yaml
```



Was this article helpful?
YesNo

