Updated 2024-11-26
# Installing the OCI Native Ingress Controller as a Cluster Add-on
_Find out how to install the OCI native ingress controller as a cluster add-on._
When you have completed the prerequisites, you can deploy the OCI native ingress controller as a cluster add-on. See [Deploying the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying).
Note that having installed the OCI native ingress controller cluster add-on, before you can use it you also have to create the necessary Kubernetes ingress-related resources. See [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources "Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller.")
## Deploying the OCI Native Ingress Controller Add-on 🔗 
The instructions in the steps below describe how to deploy the OCI native ingress controller as a cluster add-on (the 'OCI native ingress controller add-on') to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
  * [Step 1: Create the OCI native ingress controller add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying__section_create-config-file)
  * [Step 2: Deploy the OCI native ingress controller add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying__section_deploy-native-ingress-controller)


### Step 1: Create the OCI native ingress controller add-on configuration file 🔗 
**Note**
These instructions describe how to create an OCI native ingress controller add-on configuration file to enable you to deploy the OCI native ingress controller add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the OCI native ingress controller add-on, in which case you specify configuration arguments in the UI. For more information about deploying the OCI native ingress controller add-on using the Console, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called `native-ingress-controller-addon.json`) containing the following:
```
{
 "addonName": "NativeIngressController",
 "configurations": [
  {
   "key": "compartmentId",
   "value": "<compartment-ocid>"
  },
  {
   "key": "loadBalancerSubnetId",
   "value": "<load-balancer-subnet-ocid>"
  }  
 ]
}
```

where:
     * `<compartment-id>` is the OCID of the compartment in which the OCI native ingress controller is to create the OCI load balancer and certificate.
     * `<load-balancer-subnet-ocid>` is the OCID of the load balancer's subnet.
For example:
```
{
 "addonName": "NativeIngressController",
 "configurations": [
  {
   "key": "compartmentId",
   "value": "ocid1.compartment.oc1..aaaaaaaa______ddq"
  },
  {
   "key": "loadBalancerSubnetId",
   "value": "ocid1.subnet.oc1.iad.aaaaaaaa______dba"
  }  
 ]
}
```

  2. In the `native-ingress-controller-addon.json` file you just created, use the `authType` parameter to specify how you have set up the OCI native ingress controller to access OCI services and resources: 
     * If you have set up an instance principal to enable the OCI native ingress controller to access OCI services and resources, set the `authType` parameter to `instance`. 
     * If you have set up a workload identity principal to enable the OCI native ingress controller to access OCI services and resources, set the `authType` parameter to `workloadIdentity`.
     * If you have set up a user principal to enable the OCI native ingress controller to access OCI services and resources, set the `authType` parameter to `user`.
For example:
Copy
```
   "key": "authType",
   "value": "workloadIdentity"
```

Note that `instance` is the default value of the `authType` parameter, so if you do not explicitly specify a value for `authType`, the OCI native ingress controller uses the identity of the instance on which it is running to access OCI services and resources. For more information, see [Setting Up an Instance Principal, User Principal, or Workload Identity Principal to Enable Access to OCI Services and Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-auth).
  3. In the `native-ingress-controller-addon.json` file you created, specify other parameters for the OCI native ingress controller. For information about the parameters you can set, see [OCI Native Ingress Controller add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_NIC).
For example:
```
{
 "addonName": "NativeIngressController",
 "configurations": [
  {
   "key": "compartmentId",
   "value": "ocid1.compartment.oc1..aaaaaaaa______ddq"
  },
  {
   "key": "loadBalancerSubnetId",
   "value": "ocid1.subnet.oc1.iad.aaaaaaaa______dba"
  },
  {
   "key": "authType",
   "value": "workloadIdentity"
  },
  {
   "key": "logVerbosity",
   "value": "2"
  }    
 ]
}
```

  4. Save and close the `native-ingress-controller-addon.json` file.


### Step 2: Deploy the OCI native ingress controller add-on on the cluster and confirm successful deployment 🔗 
**Note**
These instructions describe how to deploy the OCI native ingress controller add-on using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Confirm that the OCI native ingress controller add-on has not already been installed on the cluster by entering:```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

where `<cluster-ocid>` is the OCID of the cluster on which you want to deploy the OCI native ingress controller add-on.
  3. Deploy the OCI native ingress controller add-on on the cluster by entering:
```
oci ce cluster install-addon --addon-name NativeIngressController --cluster-id <cluster-ocid> --from-json file://./<path-to-config-file>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to deploy the OCI native ingress controller add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the OCI native ingress controller add-on configuration file you created earlier. For example, `--from-json file://./native-ingress-controller-addon.json`
For example:
```
oci ce cluster install-addon --addon-name NativeIngressController --from-json file://./native-ingress-controller-addon.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to deploy the OCI native ingress controller add-on.
  4. Confirm successful deployment of the OCI native ingress controller add-on by entering:
```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

Assuming successful deployment, the output shows the OCI native ingress controller add-on with a lifecycle-state of ACTIVE. For example:
```
{
 "data": [
  {
   "addon-error": null,
   "current-installed-version": "v1.19.0",
   "lifecycle-state": "ACTIVE",
   "name": "NativeIngressController",
   "time-created": "2023-11-06T11:21:11+00:00",
   "version": null
  }
 ]
}
```



## Updating the OCI Native Ingress Controller Add-on 🔗 
**Note**
These instructions describe how to update the OCI native ingress controller add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Open the OCI native ingress controller add-on configuration file in a suitable editor.
  2. Add, remove, or change configuration arguments in the configuration file as required. For information about the arguments you can set, see [OCI Native Ingress Controller add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_NIC).
  3. Update the OCI native ingress controller add-on using the [oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html) command, by entering:
Copy
```
oci ce cluster update-addon --addon-name NativeIngressController --from-json file://<path-to-config-file> --cluster-id <cluster-ocid>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to update the OCI native ingress controller add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the OCI native ingress controller add-on configuration file to use when updating the add-on. For example, `--from-json file://./native-ingress-controller-addon.json`
For example:
Copy
```
oci ce cluster update-addon --addon-name NativeIngressController --from-json file://./native-ingress-controller-addon.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to update the OCI native ingress controller add-on.


## Disabling (and Removing) the OCI Native Ingress Controller Add-on 🔗 
**Note**
These instructions describe how to disable and remove the OCI native ingress controller add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#disable-add-on "Find out how to disable \(and remove\) a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Disable (and optionally remove) the OCI native ingress controller add-on using the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command, by entering:
Copy
```
oci ce cluster disable-addon --addon-name NativeIngressController --cluster-id <cluster-ocid> --is-remove-existing-add-on <true|false>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to disable (and optionally remove) the OCI native ingress controller add-on.
     * `--is-remove-existing-add-on <true|false>` specifies either to completely remove the OCI native ingress controller add-on (when set to `true`), or to not remove the add-on but simply disable it and not use it (when set to `false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available. 
For example:
Copy
```
oci ce cluster disable-addon --addon-name NativeIngressController --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr --is-remove-existing-add-on true
```

A work request is created to disable (and optionally remove) the OCI native ingress controller add-on.
  2. (Optional) Remove Kubernetes ingress-related resources (such as the IngressClassParameters, IngressClass, and Ingress resources), which aren't managed by the OCI native ingress controller add-on, using the `kubectl delete` command. 


Was this article helpful?
YesNo

