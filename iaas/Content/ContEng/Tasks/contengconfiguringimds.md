Updated 2024-08-14
# Configuring IMDS for Kubernetes Clusters
_Find out how to configure IMDS for Kubernetes clusters you've created using Kubernetes Engine (OKE)._
The instance metadata service (IMDS) can provide information about compute instances hosting managed nodes in clusters you've created using Kubernetes Engine. The instance metadata service is available in two versions, version 1 and version 2. IMDSv2 offers increased security for metadata requests when compared with IMDSv1. For more information about IMDS, see [Getting Instance Metadata](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm).
The image you specify for a managed node pool determines whether the compute instances hosting managed nodes in the node pool have IMDSv1 and/or IMDSv2 endpoints. If the image supports both IMDSv1 and IMDSv2, requests are allowed to both IMDSv1 and IMDSv2 endpoints by default. Where IMDSv2 is supported, we strongly recommend that you increase security by disabling requests to the IMDSv1 endpoint and only allow requests to the IMDSv2 endpoint. 
To disable the IMDSv1 endpoint on compute instances hosting managed nodes when you create or update node pools that use images that support IMDSv1, see:
  * [Using the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringimds.htm#contengconfiguringimds_using-the-cli)
  * [Confirming the IMDSv1 endpoint is disabled on compute instances hosting Kubernetes worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringimds.htm#contengconfiguringimds_confirming-imdsv1-disabled)


## Using the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
To use the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes when creating a new node pool, specify ` "areLegacyImdsEndpointsDisabled" : "true"` as a value of the `--node-metadata` parameter when using the `oci ce node-pool create` command. For example:
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaa______m4w \
--name my-idmsv2-only-nodepool \
--node-image-id ocid1.image.oc1.iad.aaaa______zpq \
--compartment-id ocid1.tenancy.oc1..aaa______q4a \
--kubernetes-version v1.24.1 \
--node-shape VM.Standard2.1 \
--placement-configs "[  { \"availabilityDomain\": \"PKGK:US-ASHBURN-AD-1\", \"subnetId\": \"ocid1.subnet.oc1.iad.aaaa______kfa\"  }  ]" \
--size 1 \
--region=us-ashburn-1 \
--node-metadata={"areLegacyImdsEndpointsDisabled" : "true"}
```

To use the CLI to disable the IMDSv1 endpoint on compute instances hosting new managed nodes when updating an existing node pool, specify ` "areLegacyImdsEndpointsDisabled" : "true"` as a value of the `--node-metadata` parameter when using the `oci ce node-pool update` command. For example:
```
oci ce node-pool update \
--node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya
--node-metadata={"areLegacyImdsEndpointsDisabled" : "true"}
```

Having updated an existing node pool, the IMDSv1 endpoint is disabled on compute instances hosting new managed nodes from now on. However, note that compute instances already hosting existing managed nodes are not updated, and their IMDSv1 endpoints remain enabled.
**Important** Any changes you make to worker node properties will only apply to new worker nodes. You cannot change the properties of existing worker nodes. If you want the changes to take effect immediately, consider creating a new node pool with the necessary settings and shift work from the original node pool to the new node pool (see [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\)."))
## Confirming the IMDSv1 endpoint is disabled on compute instances hosting Kubernetes worker nodes 🔗 
To confirm that the IMDSv1 endpoint is disabled on a compute instance hosting a Kubernetes worker node:
  1. Connect to the compute instance hosting the worker node using SSH. For example, by entering: `ssh opc@192.0.2.254`
For more information, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\).").
  2. Enter the following command:```
curl -H 'Authorization: Bearer Oracle' http://169.254.169.254/opc/v1/instance/
```

When an IMDSv1 endpoint is not available on a compute instance, an HTTP 404 Not Found error is returned.


Was this article helpful?
YesNo

