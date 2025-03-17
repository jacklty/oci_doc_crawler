Updated 2025-01-15
# Installing a Cluster Add-on
_Find out how to install a cluster add-on using Kubernetes Engine (OKE)._
You can install a cluster add-on when creating a new cluster, or for an existing cluster.
For specific instructions to install:
  * the Cluster Autoscaler add-on, see [Deploying the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on)
  * the Istio add-on, see [Deploying the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Deploying_Istio_Cluster_Add-on)
  * the OCI native ingress controller add-on, see [Deploying the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying)
  * the Kubernetes Metrics Server add-on, see [Deploying the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying "Find out how to use kubectl to deploy the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine \(OKE\).")


For more information about cluster add-ons, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm)


  * **Deploy and Configure a Cluster Add-on When Creating a Cluster**
    1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a cluster.
    2. Display the **Configure cluster add-ons** section of the **Create Cluster** page to display the enabled and available cluster add-ons.
By default, when creating a new cluster:
       * Essential cluster add-ons (such as CoreDNS and kube-proxy) are shown as enabled, and automatically updated.
       * Optional cluster add-ons (such as Kubernetes Dashboard) are shown as disabled.
Note that you choose the CNI plugin for pod networking on the **Network setup** page, so the CNI plugin isn't shown in the **Configure cluster add-ons** section when creating a cluster.
    3. Click the name of the add-on that you want to deploy and configure.
    4. Select the **Enable <add-on name>** option to deploy and enable the cluster add-on when creating the cluster.
Note that you can't disable essential add-ons when creating a cluster.
    5. Configure the cluster add-on by specifying the following details:
       * **Automatic updates:** Select this option when you want Oracle to automatically update the add-on when a new version becomes available.
       * **Choose a version:** Select this option when you want to control the version of the add-on that Oracle deploys on the cluster. A warning indicates that you have taken responsibility for updating the add-on. If you choose this option, select the version of the add-on to deploy on the cluster from the **Version** list. See [Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm#contengconfiguringclusteraddons-supportedversions "This table lists the latest versions of essential and optional cluster add-ons for each version of Kubernetes that Kubernetes Engine \(OKE\) supports.").
       * **Option:** and **Value:** (Optional) Specify one or more key/value pairs to pass as arguments to the cluster add-on. For example, for the Kubernetes Dashboard, you might select the `numOfReplicas` option, and specify a value of `3`. See [Cluster Add-on Configuration Arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-supportedarguments "Find out about the configuration arguments that you can pass to cluster add-ons.").
**Deploy and Configure a Cluster Add-on for an Existing Enhanced Cluster**
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that you want to modify.
    4. Under **Resources** , click **Add-ons**.
    5. Click **Manage add-ons** , and then click the cluster add-on that you want to deploy and configure.
    6. Select the **Enable <add-on name>** option to deploy and enable a cluster add-on that hasn't been enabled on this cluster before, or to enable a cluster that has been deployed previously but is currently disabled.
    7. Configure the cluster add-on by specifying the following details:
       * **Automatic updates:** Choose this option when you want Oracle to automatically update the add-on when a new version becomes available.
       * **Choose a version:** Choose this option when you want to control the version of the add-on that Oracle deploys on the cluster. A warning indicates that you have taken responsibility for updating the add-on. If you choose this option, select the version of the add-on to deploy on the cluster from the **Version** list. See [Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm#contengconfiguringclusteraddons-supportedversions "This table lists the latest versions of essential and optional cluster add-ons for each version of Kubernetes that Kubernetes Engine \(OKE\) supports.").
       * **Option:** and **Value:** (Optional) Specify one or more key/value pairs to pass as arguments to the cluster add-on. For example, for the Kubernetes Dashboard, you might select the `numOfReplicas` option, and specify a value of `3`. See [Cluster Add-on Configuration Arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-supportedarguments "Find out about the configuration arguments that you can pass to cluster add-ons.").
    8. Click **Save changes**.
  * Use the [oci ce cluster install-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/install-addon.html) command and required parameters to deploy a cluster add-on:
Command
CopyTry It
```
oci ce cluster install-addon --cluster-id <cluster-ocid> --addon-name <addon-name> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci ce cluster install-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --addon-version v2.7.0-multiarch-1.25-2
```

You use the `--configurations` parameter to specify one or more key/value pairs to pass as arguments to the cluster add-on, in JSON format. You have to escape double quotation marks within the JSON using a single backslash. For example:
Command
CopyTry It
```
oci ce cluster install-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --addon-version v2.7.0-multiarch-1.25-2 --configurations "[{\"key\": \"numOfReplicas\", \"value\": \"3\"}]"
```

Note that if the value of a key is itself required in JSON format, you have to escape double quotation marks inside the nested JSON using three backslashes. For example:
Command
CopyTry It
```
oci ce cluster install-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --addon-version v2.7.0-multiarch-1.25-2 --configurations "[{\"key\": \"tolerations\", \"value\": \"[{\\\"key\\\":\\\"special\\\", \\\"value\\\":\\\"true\\\", \\\"effect\\\":\\\"noSchedule\\\",\\\"operator\\\":\\\"exists\\\"}]\"}]"
```

To make the `--configurations` parameter less unwieldy, surround key/value pairs with single quotation marks (rather than double quotation marks). When you surround the key/value pair with single quotation marks, you do not have to escape double quotation marks in the JSON with a single backslash. And if the value of a key itself contains JSON, you only have to escape double quotation marks in the nested JSON with a single backslash (rather than three backslashes). For example:
Command
CopyTry It
```
oci ce cluster install-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --addon-version v2.7.0-multiarch-1.25-2 --configurations '[{"key": "numOfReplicas", "value": "3"}]'
```

Command
CopyTry It
```
oci ce cluster install-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard --addon-version v2.7.0-multiarch-1.25-2 --configurations '[{"key": "tolerations", "value": "[{\"key\":\"special\", \"value\":\"true\", \"effect\":\"noSchedule\",\"operator\":\"exists\"}]"}]'
```

  * Run the [InstallAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/InstallAddon) operation to install a cluster add-on.


Was this article helpful?
YesNo

