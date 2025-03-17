Updated 2024-12-16
# Exposing Containerized Applications
To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.
Ensure that the load balancer shape parameter has one of the following values: 
  * `400Mbps`
  * `flexible` – Requires that you also provide `flex-min` and `flex-max` annotations.


You might need to edit the application deployment file to modify the load balancer shape value. See [Specifying Alternative Load Balancer Shapes](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#Specifyi) and [Specifying Flexible Load Balancer Shapes](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#flexible) for more information and examples of how to set these values.
Use the following command to create the external load balancer:
Copy
```
# kubectl create -f expose_lb
```

The following is the content of the `expose_lb` file:
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
  service.beta.kubernetes.io/oci-load-balancer-shape: "400Mbps"
spec:
 type: LoadBalancer
 ports:
  - port: 80
 selector:
  app: nginx
```

The following command shows more information about this external load balancer. The LoadBalancer Ingress IP address is the IP address that's used to reach node applications from outside the Compute Cloud@Customer. In the Compute Cloud@Customer Console, the LoadBalancer Ingress IP address is shown under the heading "IP Address" at the bottom of the first column on load balancer details page, followed by the label "(Public)."
Copy
```
# kubectl describe svc my-nginx-svc
Name:           my-nginx-svc
Namespace:        default
Labels:          app=nginx
Annotations:       oci.oraclecloud.com/load-balancer-type: lb
             service.beta.kubernetes.io/oci-load-balancer-shape: 400Mbps
Selector:         app=nginx
Type:           LoadBalancer
IP Family Policy:     SingleStack
IP Families:       IPv4
IP:            IP_address
IPs:           IP_address
LoadBalancer Ingress:   Load_Balancer_IP_address
Port:           <unset> 80/TCP
TargetPort:        80/TCP
NodePort:         <unset> 32145/TCP
Endpoints:        IP_address:port, IP_address+1:port, IP_address+2:port
Session Affinity:     None
External Traffic Policy: Cluster
Events:
 Type  Reason        Age  From        Message
 ----
 Normal EnsuringLoadBalancer 7m48s service-controller Ensuring load balancer
 Normal EnsuredLoadBalancer  6m40s service-controller Ensured load balancer
```

For descriptions of traffic policies, see [Preserving the client source IP](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip).
Use the following command to list IP addresses and ports for the external load balancer:
Copy
```
# kubectl get svc
NAME     TYPE     CLUSTER-IP EXTERNAL-IP        PORT(S)    AGE
kubernetes  ClusterIP   IP_address <none>          443/TCP    6h17m
my-nginx-svc LoadBalancer IP_address
     Load_Balancer_IP_address 80:32145/TCP 5h5m
```

**What's Next:**
[Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.")
Was this article helpful?
YesNo

