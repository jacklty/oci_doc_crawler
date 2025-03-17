Updated 2024-08-14
# Deploying a Sample Nginx App on a Cluster Using Kubectl
_Find out how to use kubectl to deploy an Nginx app on a cluster you've created using Kubernetes Engine (OKE)._
Having created a Kubernetes cluster using Kubernetes Engine, you'll typically want to try it out by deploying an application on the nodes in the cluster. For convenience, the **Quick Start** tab (available from the **Cluster** page) makes it easy to view and copy the commands to:
  * set up access to the cluster
  * download and deploy a sample Nginx application using the Kubernetes command line tool kubectl from the instructions in a manifest file


To deploy the sample nginx application:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. In a terminal window, deploy the sample Nginx application by entering:
Command
CopyTry It
```
kubectl create -f https://k8s.io/examples/application/deployment.yaml
```

**Tip** If the command fails to connect to `https://k8s.io/examples/application/deployment.yaml` , go to the url in a browser and download the manifest file `deployment.yaml` to a local directory. Repeat the `kubectl create` command and specify the local location of the `deployment.yaml` file.
  3. Confirm that the sample application has been deployed successfully by entering:
Command
CopyTry It
```
kubectl get pods
```



You can see the Nginx sample application has been deployed as two pods, on two nodes in the cluster.
Was this article helpful?
YesNo

