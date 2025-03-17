Updated 2024-10-25
# Working with the Kubernetes Metrics Server as a Standalone Program
_Find out how to use kubectl to deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools and virtual node pools that you've created using Kubernetes Engine (OKE)._
Using the Kubernetes Metrics Server as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
  * Installing a version of the Kubernetes Metrics Server that is compatible with the version of Kubernetes running on the cluster.
  * Specifying configuration arguments correctly.
  * Manually upgrading the Kubernetes Metrics Server when you upgrade a cluster to a new version of Kubernetes, to ensure the Kubernetes Metrics Server is compatible with the cluster's new Kubernetes version.


To deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools or virtual node pools that you've created with Kubernetes Engine:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. If your Oracle Cloud Infrastructure user is a tenancy administrator or cluster administrator, skip the next step and go straight to the following step.
  3. If your Oracle Cloud Infrastructure user is not a tenancy administrator or cluster administrator, ask a tenancy administrator or cluster administrator to grant your user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:
Command
CopyTry It
```

kubectl create clusterrolebinding <my-cluster-admin-binding> --clusterrole=cluster-admin --user=<user-OCID>
```

For more information, see [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
  4. Deploy the Kubernetes Metrics Server by entering the following command in a terminal window:
Command
CopyTry It
```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/<version-number>/components.yaml
```

where `<version-number>` is the Kubernetes Metrics Server version that you want to deploy. For example, `v0.6.1`.
Note that the Kubernetes Metrics Server is being actively developed, so the version number to specify will change over time. To find out the currently available versions, see the [Kubernetes Metrics Server documentation](https://github.com/kubernetes-sigs/metrics-server/releases).
**Tip** If the command fails to connect to `https://github.com/kubernetes-sigs/metrics-server/releases/download/<version-number>/components.yaml` , go to the url in a browser and download the manifest file `components.yaml` to a local directory. Repeat the `kubectl apply` command and specify the local location of the `components.yaml` file.
  5. Confirm that the Kubernetes Metrics Server has been deployed successfully and is available by entering:
Command
CopyTry It
```
kubectl get deployment metrics-server -n kube-system
```



Was this article helpful?
YesNo

