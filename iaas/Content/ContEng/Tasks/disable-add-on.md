Updated 2025-01-15
# Disabling (and Removing) a Cluster Add-on
_Find out how to disable (and remove) a cluster add-on using Kubernetes Engine (OKE)._
You can disable a cluster add-on deployed on a cluster using the Console, the CLI, and the API. If you also want to remove the cluster add-on from the cluster, use the CLI or the API.
For specific instructions to disable (and remove):
  * the Cluster Autoscaler add-on, see [Disabling (and Removing) the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Disabling_Removing_Cluster_Autoscaler_Add-on)
  * the Istio add-on, see [Disabling (and Removing) the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Disabling_Removing_Istio_Add-on)
  * the OCI native ingress controller add-on, see [Disabling (and Removing) the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Disabling_Removing)
  * the Kubernetes Metrics Server add-on, see [Disabling (and Removing) the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_disabling-removing)


For more information about cluster add-ons, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster on which the cluster add-on is deployed.
    4. Under **Resources** , click **Add-ons**.
Detailed information about the enabled cluster add-ons deployed on the cluster is shown in tabular form.
    5. Click **Manage add-ons** , and then click the enabled cluster add-on that you want to disable.
    6. Clear the **Enable <add-on name>** option. 
If you disable an essential cluster add-on, a warning indicates that you have taken responsibility for deploying and configuring an alternative add-on to provide equivalent functionality.
    7. Click **Save changes**.
The cluster add-on is disabled, but not removed from the cluster. To completely remove the add-on, use the CLI or the API.
  * Use the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command and required parameters to disable (and optionally remove) a cluster-add-on deployed on a cluster:
Command
CopyTry It
```
oci ce cluster disable-addon --cluster-id <cluster-ocid> --addon-name <addon-name> --is-remove-existing-add-on <true|false> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci ce cluster disable-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --is-remove-existing-add-on true
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DisableAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DisableAddon) operation to disable (and optionally remove) a cluster add-on deployed on a cluster.


Was this article helpful?
YesNo

