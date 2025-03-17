Updated 2024-06-25
# Troubleshooting Pod and Service Issues on Virtual Nodes Using kubectl proxy Rather Than kubectl port-forward
_Find out how to use kubectl proxy (rather than kubectl port-forward) to view application output to help you resolve issues with pods running on virtual nodes._
When testing and debugging an application running in pods in a Kubernetes cluster, and to access the cluster's internal resources without exposing them to the public internet, it's often useful to view the application's output as if it is running locally on your computer.
When using managed node pools, you can use the `kubectl port-forward` command on your local machine to view the output of applications running in pods on managed nodes. Using the `kubectl port-forward` command creates a secure tunnel between a local machine and an application running on a Kubernetes cluster. The tunnel allows traffic to flow between the two endpoints, enabling you to view the application's output from the local machine.
However, when using virtual node pools, you cannot use the `kubectl port-forward` command to view the output of applications running in pods on virtual nodes. As an alternative, use the `kubectl proxy` command for the same purpose.
For example:
  1. If you haven't already done so, install kubectl (see the [kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
  2. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file for use locally, and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. You might also need to set the OCI_CLI_PROFILE environment variable to the name of the profile defined in the CLI configuration file before running kubectl commands. See [Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload).
  3. Create a deployment on the cluster in the default namespace. For example, by entering:```
kubectl create -f https://k8s.io/examples/application/deployment.yaml
```

  4. Obtain the list of pods by entering:```
kubectl get pods
```

  5. In a local terminal window, start a proxy by entering:```
kubectl proxy --port=8080
```

  6. In a different local terminal window, you can now:
     * View pod output by entering:```
curl http://localhost:8080/api/v1/namespaces/<namespace-name>/pods/<pod-name>/proxy/
```

For example:
```
curl http://localhost:8080/api/v1/namespaces/default/pods/nginx-5b6b9d4766-qs9tc/proxy/
```

     * View service output by entering:```
curl http://localhost:8080/api/v1/namespaces/<namespace-name>/services/<service-name>/proxy/
```

For example:
```
curl http://localhost:8080/api/v1/namespaces/default/services/nginx-service/proxy/
```

In both cases, note the forward slash ( / ) at the end of the command.


Was this article helpful?
YesNo

