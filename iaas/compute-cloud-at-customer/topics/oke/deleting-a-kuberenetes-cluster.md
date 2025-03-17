Updated 2024-12-16
# Deleting an OKE Cluster
On Compute Cloud@Customer, deleting an OKE cluster deletes the cluster control plane nodes, worker nodes, and node pools. Other cluster resources such as VCNs, internet gateways, NAT gateways, route tables, security lists, load balancers, and block volumes aren't deleted when you delete the cluster. Those resources must be deleted separately.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-kuberenetes-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-kuberenetes-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-kuberenetes-cluster.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. For the cluster that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click **Delete**.
    3. Confirm that you want to delete the cluster.
Enter the cluster name, and click **Delete**.
  * Use the [oci ce cluster delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/delete.html) command and required parameters to delete a cluster.
Copy
```
oci ce cluster delete --cluster-id <cluster_OCID> [OPTIONS]
```

**Procedure**
    1. Get the OCID of the cluster that you want to delete: `oci ce cluster               list`
    2. Run the delete cluster command.
Example:
Copy
```
$ oci ce cluster delete --cluster-id ocid1.cluster. _unique_ID_ --force
```

The `--force` option performs the deletion without prompting for confirmation.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DeleteCluster) operation to delete a cluster.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

