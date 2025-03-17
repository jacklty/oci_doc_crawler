Updated 2024-08-14
# Configuring DNS Servers for Kubernetes Clusters
_Find out how to configure DNS servers for Kubernetes clusters you've created using Kubernetes Engine (OKE)._
## Configuring Built-in DNS Servers (kube-dns, CoreDNS)
Clusters created by Kubernetes Engine include a DNS server as a built-in Kubernetes service that is launched automatically. The kubelet process on each worker node directs individual containers to the DNS server to translate DNS names to IP addresses.
Prior to Kubernetes version 1.14, Kubernetes Engine created clusters with kube-dns as the DNS server. However, from Kubernetes version 1.14 onwards, Kubernetes Engine creates clusters with CoreDNS as the DNS server. CoreDNS is a general-purpose authoritative DNS server that is modular and pluggable. 
Default CoreDNS behavior is controlled by a configuration file referred to as a Corefile. The Corefile is a Kubernetes ConfigMap, with a Corefile section that defines CoreDNS behavior. You cannot modify the Corefile directly. If you need to customize CoreDNS behavior, you create and apply your own ConfigMap to override settings in the Corefile (as described in this topic). Note that with basic clusters, if you do customize CoreDNS default behavior, the customizations are periodically deleted during internal updates to the cluster (with enhanced clusters, customizations are not deleted).
When you upgrade a cluster created by Kubernetes Engine from an earlier version to Kubernetes 1.14 or later, the cluster's kube-dns server is automatically replaced with the CoreDNS server. Note that if you customized kube-dns behavior using the original kube-dns ConfigMap, those customizations are not carried forward to the CoreDNS ConfigMap. You will have to create and apply a new ConfigMap containing the customizations to override settings in the CoreDNS Corefile.
For more information about CoreDNS customization and Kubernetes, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/#coredns) and the [CoreDNS documentation](https://coredns.io/explugins/forward/).
To create a ConfigMap to override the settings in the CoreDNS Corefile:
  1. Define a ConfigMap in a yaml file, in the format:
Copy
```
apiVersion: v1
kind: ConfigMap
metadata: 
 name: coredns-custom 
 namespace: kube-system 
data:
 <customization-options>
```

For example:
Copy
```
apiVersion: v1
kind: ConfigMap
metadata: 
 name: coredns-custom 
 namespace: kube-system 
data:
 example.server: | # All custom server files must have a ".server" file extension. 
  # Change example.com to the domain you wish to forward.
  example.com {
   # Change 1.1.1.1 to your customer DNS resolver.
   forward . 1.1.1.1
  }
```

For more information about the ConfigMap options to use to customize CoreDNS behavior, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/#coredns) and the [CoreDNS documentation](https://coredns.io/explugins/forward/).
  2. Create the ConfigMap by entering:
Command
CopyTry It
```
kubectl apply -f <filename>.yaml
```

  3. Verify the customizations have been applied by entering:
Command
CopyTry It
```
kubectl get configmaps --namespace=kube-system coredns-custom -o yaml
```

  4. Force CoreDNS to reload the ConfigMap by entering:
Command
CopyTry It
```
kubectl delete pod --namespace kube-system -l k8s-app=kube-dns
```



## Configuring ExternalDNS to use Oracle Cloud Infrastructure DNS
ExternalDNS is an add-on to Kubernetes that can create DNS records for services in DNS providers external to Kubernetes . It sets up DNS records in an external DNS provider to make Kubernetes services discoverable via that DNS provider, and enables you to control DNS records dynamically. See [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) for more information.
Having deployed ExternalDNS on a cluster, you can expose a service running on the cluster by adding the `external-dns.alpha.kubernetes.io/hostname` annotation to the service. ExternalDNS creates a DNS record for the service in the external DNS provider you've configured for the cluster.
ExternalDNS is not itself a DNS server like CoreDNS, but a way to configure other external DNS providers. Oracle Cloud Infrastructure DNS is one such external DNS provider. See [Overview of DNS](https://docs.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm).
For convenience, instructions are included below to set up ExternalDNS on a cluster and configure it to use Oracle Cloud Infrastructure DNS. These instructions are a summary based on the [Setting up ExternalDNS for Oracle Cloud Infrastructure (OCI) tutorial](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/oracle.md), which is available on GitHub.
To set up ExternalDNS on a cluster and configure it to use Oracle Cloud Infrastructure DNS:
  1. Create a new DNS zone in Oracle Cloud Infrastructure DNS to contain the DNS records that ExternalDNS will create for the cluster. See [Creating a Zone](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm).
  2. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  3. Create a Kubernetes secret containing the Oracle Cloud Infrastructure user authentication details for ExternalDNS to use when connecting to the Oracle Cloud Infrastructure API to insert and update DNS records in the DNS zone you just created.
    1. In a text editor, create a credentials file containing the Oracle Cloud Infrastructure user credentials to use to access the DNS zone:
Copy
```
auth:
 region: <region-identifier>
 tenancy: <tenancy-ocid>
 user: <user-ocid>
 key: |
  -----BEGIN RSA PRIVATE KEY-----
  <private-key>
  -----END RSA PRIVATE KEY-----
 fingerprint: <fingerprint>
 # Omit if there is not a password for the key
 passphrase: <passphrase>
compartment: <compartment-ocid>
```

where:
       * `<region-identifer>` identifies the user's region. For example, `us-phoenix-1`
       * `<tenancy-ocid>` is the OCID of the user's tenancy. For example, `ocid1.tenancy.oc1..aaaaaaaap...keq` (abbreviated for readability).
       * `<user-ocid>` is the OCID of the user. For example, `ocid1.user.oc1..aaaaa...zutq` (abbreviated for readability).
       * `<private-key>` is an RSA key, starting with `-----BEGIN RSA PRIVATE KEY-----` and ending with `-----END RSA PRIVATE KEY-----`
       * `passphrase: <passphrase>` optionally provides the passphrase for the key, if one exists
       * `<compartment-ocid>` is the OCID of the compartment to which the DNS zone belongs
For example:
Copy
```
auth:
 region: us-phoenix-1
 tenancy: ocid1.tenancy.oc1..aaaaaaaap...keq
 user: ocid1.user.oc1..aaaaa...zutq
 key: |
  -----BEGIN RSA PRIVATE KEY-----
  this-is-not-a-secret_Ef8aiAk7+I0...
  -----END RSA PRIVATE KEY-----
 fingerprint: bg:92:82:9f...
 # Omit if there is not a password for the key
 passphrase: Uy2kSl...
compartment: ocid1.compartment.oc1..aaaaaaaa7______ysq
```

    2. Save the credentials file with a name of your choosing (for example, `oci-creds.yaml`). 
    3. Create a Kubernetes secret from the credentials file you just created, by entering:
Command
CopyTry It
```
kubectl create secret generic <secret-name> --from-file=<credential-filename>
```

For example:
Command
CopyTry It
```
kubectl create secret generic external-dns-config --from-file=oci-creds.yaml
```

  4. Deploy ExternalDNS on the cluster.
    1. In a text editor, create a configuration file (for example, called `external-dns-deployment.yaml`) to create the ExternalDNS deployment, and specify the name of the Kubernetes secret you just created. For example:
Copy
```
apiVersion: v1
kind: ServiceAccount
metadata:
 name: external-dns
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: external-dns
rules:
- apiGroups: [""]
 resources: ["services","endpoints","pods"]
 verbs: ["get","watch","list"]
- apiGroups: ["extensions","networking.k8s.io"]
 resources: ["ingresses"]
 verbs: ["get","watch","list"]
- apiGroups: [""]
 resources: ["nodes"]
 verbs: ["list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: external-dns-viewer
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: external-dns
subjects:
- kind: ServiceAccount
 name: external-dns
 namespace: default
---
apiVersion: apps/v1
kind: Deployment
metadata:
 name: external-dns
spec:
 strategy:
  type: Recreate
 selector:
  matchLabels:
   app: external-dns
 template:
  metadata:
   labels:
    app: external-dns
  spec:
   serviceAccountName: external-dns
   containers:
   - name: external-dns
    image: k8s.gcr.io/external-dns/external-dns:v0.7.3
    args:
    - --source=service
    - --source=ingress
    - --provider=oci
    - --policy=upsert-only # prevent ExternalDNS from deleting any records, omit to enable full synchronization
    - --txt-owner-id=my-identifier
    volumeMounts:
     - name: config
      mountPath: /etc/kubernetes/
   volumes:
   - name: config
    secret:
     secretName: external-dns-config
```

    2. Save and close the configuration file.
    3. Apply the configuration file to deploy ExternalDNS by entering:
Command
CopyTry It
```
kubectl apply -f <filename>
```

where `<filename>` is the name of the file you created earlier. For example:
Command
CopyTry It
```
kubectl apply -f external-dns-deployment.yaml
```

The output from the above command confirms the deployment:
```
serviceaccount/external-dns created
clusterrole.rbac.authorization.k8s.io/external-dns created
clusterrolebinding.rbac.authorization.k8s.io/external-dns-viewer created
deployment.apps/external-dns created

```

  5. Verify that ExternalDNS has been deployed successfully and can insert records in the DNS zone you created earlier in Oracle Cloud Infrastructure by creating an nginx deployment and an nginx service:
    1. In a text editor, create a configuration file (for example, called `nginx-externaldns.yaml`) to create an nginx deployment and an nginx service that includes the `external-dns.alpha.kubernetes.io/hostname` annotation. For example:
Copy
```
apiVersion: v1
kind: Service
metadata:
 name: nginx
 annotations:
  external-dns.alpha.kubernetes.io/hostname: example.com
spec:
 type: LoadBalancer
 ports:
 - port: 80
  name: http
  targetPort: 80
 selector:
  app: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx
spec:
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - image: nginx
    name: nginx
    ports:
    - containerPort: 80
     name: http
```

    2. Apply the configuration file to create the nginx service and deployment by entering:
Command
CopyTry It
```
kubectl apply -f <filename>
```

where `<filename>` is the name of the file you created earlier. For example:
Command
CopyTry It
```
kubectl apply -f nginx-externaldns.yaml
```

The output from the above command confirms the deployment:
```
service/nginx created
deployment.apps/nginx created

```

    3. Wait a couple of minutes, and then verify that a DNS record was created for the nginx service in the Oracle Cloud Infrastructure DNS zone (see [Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm)).


Was this article helpful?
YesNo

