Updated 2025-01-15
# Updating a Cluster Add-on
_Find out how to update a cluster add-on using Kubernetes Engine (OKE)._
For specific instructions to update:
  * the Cluster Autoscaler add-on, see [Updating the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Updating_Cluster_Autoscaler_Add-on)
  * the Istio add-on, see [Updating the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Updating_Cluster_Autoscaler_Add-on)
  * the OCI native ingress controller add-on, see [Updating the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Updating)
  * the Kubernetes Metrics Server add-on, see [Updating the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_updating)


For more information about cluster add-ons, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm)


  * To update the configuration of a cluster add-on deployed on an existing enhanced cluster using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the enhanced cluster on which the cluster add-on is deployed.
    4. Under **Resources** , click **Add-ons**.
    5. Click **Manage add-ons** , and then click the deployed cluster add-on that you want to update.
    6. To update the configuration of the cluster add-on, specify the following details:
       * **Automatic updates:** Choose this option when you want Oracle to automatically update the add-on when a new version becomes available.
       * **Choose a version:** Choose this option when you want to control the version of the add-on that Oracle deploys on the cluster. A warning indicates that you have taken responsibility for updating the add-on. If you choose this option, select the version of the add-on to deploy on the cluster from the **Version** list. See [Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm#contengconfiguringclusteraddons-supportedversions "This table lists the latest versions of essential and optional cluster add-ons for each version of Kubernetes that Kubernetes Engine \(OKE\) supports.").
       * **Option:** and **Value:** (optional) Specify one or more key/value pairs to pass as arguments to the cluster add-on. For example, for the Kubernetes Dashboard, you might select the `numOfReplicas` option, and specify a value of `3`. See [Cluster Add-on Configuration Arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-supportedarguments "Find out about the configuration arguments that you can pass to cluster add-ons.").
    7. Click **Save changes**.
  * Use the [oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html) command and required parameters to update a cluster add-on deployed on a cluster:
Command
CopyTry It
```
oci ce cluster update-addon --cluster-id <cluster-ocid> --addon-name <addon-name> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateAddon) operation to update a cluster add-on deployed on a cluster.


Was this article helpful?
YesNo

