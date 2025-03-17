Updated 2025-01-15
# Listing Cluster Add-ons
_Find out how to list the cluster add-ons deployed on a cluster using Kubernetes Engine (OKE)._
You can list the cluster add-ons deployed on a cluster using the Console, the CLI, and the API.
For more information about cluster add-ons, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm)


  * To list the cluster add-ons deployed on a cluster using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
The **Cluster List** page shows the clusters in the selected compartment.
    3. On the **Cluster List** page, click the name of the cluster on which the cluster add-ons are deployed.
    4. Under **Resources** , click **Add-ons**.
The cluster add-ons deployed on the cluster are shown.
  * Use the [oci ce cluster list-addons](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/list-addons.html) command and required parameters to list the cluster add-ons deployed on a cluster:
Command
CopyTry It
```
oci ce cluster list-addons --cluster-id <cluster-ocid> [OPTIONS]
```

Use the [oci ce addon-option list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/addon-option/list.html) command to:
    * List available versions of all cluster add-ons supported on a given Kubernetes version:
Command
CopyTry It
```
oci ce addon-option list --kubernetes-version <k8s-version>
```

For example:
Command
CopyTry It
```
oci ce addon-option list --kubernetes-version v1.25.4
```

    * List available versions of a cluster add-on supported on a given Kubernetes version:
Command
CopyTry It
```
oci ce addon-option list --kubernetes-version <k8s-version> --addon-name <addon-name>
```

For example:
Command
CopyTry It
```
oci ce addon-option list --kubernetes-version v1.25.4 --addon-name KubernetesDashboard
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAddons](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/ListAddons) operation to list the cluster add-ons deployed on a cluster.
Run the [ListAddonOptions](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/AddonOptionSummary/ListAddonOptions) operation to list available versions of cluster add-ons.


Was this article helpful?
YesNo

