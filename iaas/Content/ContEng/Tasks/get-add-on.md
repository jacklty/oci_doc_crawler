Updated 2025-01-15
# Getting a Cluster Add-on's Details
_Find out how to get details of a specific cluster add-on using Kubernetes Engine (OKE)._
You can get details of a specific cluster add-on deployed on a cluster using the Console, the CLI, and the API.
For more information about cluster add-ons, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm)


  * To get details of a cluster add-on deployed on a cluster using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
The **Cluster List** page shows the clusters in the selected compartment.
    3. On the **Cluster List** page, click the name of the cluster on which the cluster add-on is deployed.
    4. Under **Resources** , click **Add-ons**.
Detailed information about the enabled cluster add-ons deployed on the cluster are shown in tabular form.
    5. Click **Manage add-ons** , and then click the cluster add-on that you want to get more detailed information about.
  * Use the [oci ce cluster get-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/get-addon.html) command and required parameters to get details of a cluster add-on deployed on a cluster (for example, to verify successful deployment of a cluster add-on):
Command
CopyTry It
```
oci ce cluster get-addon --cluster-id <cluster-ocid> --addon-name <addon-name> [OPTIONS]
```

For example:
Command
CopyTry It
```
oci ce cluster get-addon --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --addon-name KubernetesDashboard
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/GetAddon) operation to get details of a cluster add-on deployed on a cluster.


Was this article helpful?
YesNo

