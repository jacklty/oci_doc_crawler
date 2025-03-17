Updated 2024-06-05
# Installing the OCI Native Ingress Controller as a Standalone Program
_Find out how to install the OCI native ingress controller as a standalone program._
When you have completed the prerequisites, you can deploy the OCI native ingress controller as a standalone program. See [Installing the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm#contengsettingupnativeingresscontroller-deployment).
Note that having installed the OCI native ingress controller cluster add-on as a standalone program, before you can use it you also have to create the necessary Kubernetes ingress-related resources. See [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources "Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller.").
## Installing the OCI Native Ingress Controller 🔗 
You can use the Helm CLI in two ways to install the OCI native ingress controller and deploy the required resources:
  * **Use Helm to install the OCI native ingress controller.** With this approach, you use the `helm install` command. Helm manages OCI native ingress controller releases for initial installation and subsequent upgrades. During installation, the required resources are deployed on the cluster using parameter values obtained from the values.yaml file where available.
  * **Use Helm to generate .yaml manifest files.** With this approach, you use the Helm CLI to generate a list of manifest .yaml files to hold all Kubernetes resources required for the OCI native ingress controller installation. You can use these .yaml files with any API server client, such as kubectl. The manifest .yaml files are populated with parameter values obtained from the values.yaml file where available. This method of installation enables you to subsequently customize the manifest .yaml files and override parameter values obtained from the values.yaml file.


### Installing the OCI native ingress controller using the helm install command
To install the OCI native ingress controller using the `helm install` command:
  1. In the local Git repository, navigate to the `oci-native-ingress-controller` directory.
  2. Install the OCI native ingress controller using Helm by entering:
Copy
```
helm install oci-native-ingress-controller helm/oci-native-ingress-controller
```

During installation, the required Kubernetes resources are deployed on the cluster using parameter values obtained from the values.yaml file where available.
  3. Confirm that you have successfully installed the OCI native ingress controller by entering:
Copy
```
kubectl get pods -n native-ingress-controller-system --selector='app.kubernetes.io/name in (oci-native-ingress-controller)' -o wide
```

Example output:```

NAME                       READY  STATUS  RESTARTS  AGE  IP      NODE     NOMINATED NODE  READINESS GATES
oci-native-ingress-controller-54795499fd-6xlhn  1/1   Running  0     11s  10.0.10.57  10.0.10.182  <none>      <none>
```



### Installing the OCI native ingress controller using generated manifest files
To install the OCI native ingress controller using generated manifest files:
  1. In the local Git repository, navigate to the `oci-native-ingress-controller` directory.
  2. Generate the manifest .yaml files for the required resources into a `/manifests` directory, by entering: 
Copy
```
helm template --include-crds oci-native-ingress-controller helm/oci-native-ingress-controller --output-dir deploy/manifests
```

The manifest .yaml files are created for the required resources, populated with parameter values obtained from the values.yaml file where available.
If necessary, you can customize the manifest .yaml files before deploying the required resources.
  3. Deploy the required resources using the manifest .yaml files:
    1. Deploy the required resources defined in the crd .yaml files by entering:
Copy
```
kubectl apply -f deploy/manifests/oci-native-ingress-controller/crds
```

    2. Deploy the required resources defined in the template .yaml files by entering:
Copy
```
kubectl apply -f deploy/manifests/oci-native-ingress-controller/templates
```

  4. Confirm that you have successfully installed the OCI native ingress controller by entering:
Copy
```
kubectl get pods -n native-ingress-controller-system --selector='app.kubernetes.io/name in (oci-native-ingress-controller)' -o wide
```

Example output:```

NAME                       READY  STATUS  RESTARTS  AGE  IP      NODE     NOMINATED NODE  READINESS GATES
oci-native-ingress-controller-54795499fd-6xlhn  1/1   Running  0     11s  10.0.10.57  10.0.10.182  <none>      <none>
```



Was this article helpful?
YesNo

