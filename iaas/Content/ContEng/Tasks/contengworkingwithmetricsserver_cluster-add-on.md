Updated 2024-08-23
# Working with the Kubernetes Metrics Server as a Cluster Add-on
_Find out how to use the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine (OKE)._
Using the Kubernetes Metrics Server as a cluster add-on rather than as a standalone program simplifies configuration and ongoing maintenance. You can more simply:
  * Enable or disable the Kubernetes Metrics Server.
  * Opt into, and out of, automatic updates by Oracle.
  * Select Kubernetes Metrics Server add-on versions.
  * Manage add-on specific customizations using approved key/value pair configuration arguments.


These sections describe how to work with the Kubernetes Metrics Server add-on:
  * [Deploying the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying "Find out how to use kubectl to deploy the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine \(OKE\).")
  * [Updating the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_updating)
  * [Disabling (and Removing) the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_disabling-removing)


## Deploying the Kubernetes Metrics Server as a Cluster Add-on 🔗 
_Find out how to use kubectl to deploy the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine (OKE)._
These instructions describe how to deploy the Kubernetes Metrics Server as a cluster add-on:
  * [Step 1: Create the Kubernetes Metrics Server add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying__section_create-config-file)
  * [Step 2: Deploy the Kubernetes Metrics Server add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying__section_deploy)


### Step 1: Create the Kubernetes Metrics Server add-on configuration file 🔗 
**Note**
These instructions describe how to create a Kubernetes Metrics Server add-on configuration file to enable you to deploy the Kubernetes Metrics Server add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the Kubernetes Metrics Server add-on, in which case you specify configuration arguments in the UI. For more information about deploying the Kubernetes Metrics Server add-on using the Console, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called `enablemetrics-server.json`) containing the following:
```
{
 "addonName": "KubernetesMetricsServer",
 "configurations": [
 ]
}
```

This content is sufficient to enable the Kubernetes Metrics Server add-on.
  2. (Optional) In the `enablemetrics-server.json` file you created, specify other configuration arguments to customize the Kubernetes Metrics Server add-on. For information about the configuration arguments you can set, see [Kubernetes Metrics Server add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_metrics-server).
  3. Save and close the `enablemetrics-server.json` file.


### Step 2: Deploy the Kubernetes Metrics Server add-on on the cluster and confirm successful deployment 🔗 
**Note**
These instructions describe how to deploy the Kubernetes Metrics Server add-on on clusters with managed node pools, using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Confirm that the Kubernetes Metrics Server add-on has not already been installed on the cluster by entering:```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

where `<cluster-ocid>` is the OCID of the cluster on which you want to deploy the Kubernetes Metrics Server add-on.
  3. If your Oracle Cloud Infrastructure user is a tenancy administrator or cluster administrator, skip the next step and go straight to the following step.
  4. If your Oracle Cloud Infrastructure user is not a tenancy administrator or cluster administrator, ask a tenancy administrator or cluster administrator to grant your user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:
Command
CopyTry It
```

kubectl create clusterrolebinding <my-cluster-admin-binding> --clusterrole=cluster-admin --user=<user-OCID>
```

For more information, see [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
  5. Deploy the Kubernetes Metrics Server add-on on the cluster by entering:
```
oci ce cluster install-addon --addon-name KubernetesMetricsServer --cluster-id <cluster-ocid> --from-json file://./<path-to-config-file>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to deploy the Kubernetes Metrics Server add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Kubernetes Metrics Server add-on configuration file you created earlier. For example, `--from-json file://./enablemetrics-server.json`
For example:
```
oci ce cluster install-addon --addon-name KubernetesMetricsServer --from-json file://./enablemetrics-server.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to deploy the Kubernetes Metrics Server add-on.
  6. Confirm that the Kubernetes Metrics Server has been deployed successfully and is available by entering:
Command
CopyTry It
```
kubectl get deployment metrics-server -n kube-system
```



## Updating the Kubernetes Metrics Server Add-on 🔗 
**Note**
These instructions describe how to update the Kubernetes Metrics Server add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Open the Kubernetes Metrics Server add-on configuration file in a suitable editor
  2. Add, remove, or change configuration parameters in the configuration file as required. For information about the parameters you can set, see [Kubernetes Metrics Server add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_metrics-server).
  3. Update the Kubernetes Metrics Server add-on using the [oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html) command, by entering:
Copy
```
oci ce cluster update-addon --addon-name KubernetesMetricsServer --from-json file://<path-to-config-file> --cluster-id <cluster-ocid>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to update the Kubernetes Metrics Server add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Kubernetes Metrics Server add-on configuration file to use when updating the add-on. For example, `--from-json file://./`enablemetrics-server.json``
For example:
Copy
```
oci ce cluster update-addon --addon-name KubernetesMetricsServer --from-json file://./enablemetrics-server.json.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to update the Kubernetes resources required by the Kubernetes Metrics Server.
  4. **Optional:** View the status of the Kubernetes Metrics Server pods to observe progress, by entering:```
kubectl get pods -n kube-system | grep metrics-server
```



## Disabling (and Removing) the Kubernetes Metrics Server Add-on 🔗 
**Note**
These instructions describe how to disable and remove the Kubernetes Metrics Server add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#disable-add-on "Find out how to disable \(and remove\) a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Disable (and optionally remove) the Kubernetes Metrics Server add-on using the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command, by entering:
Copy
```
oci ce cluster disable-addon --addon-name KubernetesMetricsServer --cluster-id <cluster-ocid> --is-remove-existing-add-on <true|false>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to disable (and optionally remove) the Kubernetes Metrics Server add-on.
     * `--is-remove-existing-add-on <true|false>` specifies either to completely remove the Kubernetes Metrics Server add-on (when set to `true`), or to not remove the add-on but simply disable it and not use it (when set to `false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available. 
For example:
Copy
```
oci ce cluster disable-addon --addon-name KubernetesMetricsServer --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr --is-remove-existing-add-on true
```

A work request is created to disable (and optionally remove) the Kubernetes Metrics Server.
  2. **Optional:** View the status of the Kubernetes Metrics Server pods to observe progress, by entering:```
kubectl get pods -n kube-system | grep metrics-server
```



Was this article helpful?
YesNo

