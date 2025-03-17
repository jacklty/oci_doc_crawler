Updated 2024-12-16
# Creating an OKE Worker Node Pool
Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster. 
Nodes are Compute Cloud@Customer compute instances. When you create a worker node pool, you specify the number of nodes to create and other parameters that define instances.
**Note**
You can't customize the OKE `cloud-init` scripts.
If your network requires proxy settings to enable worker nodes to reach outside registries or repositories, for example, use the Oracle CLI or API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm)


  *     1. On the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") dashboard, click **Containers / View Kubernetes Clusters (OKE)**.
If the cluster to which you want to attach a node pool is not listed, select a different compartment from the compartment menu at the top of the page.
    2. Click the name of the cluster to which you want to add a node pool.
    3. On the cluster details page, under **Resources** , click **Node Pools**.
    4. On the **Node Pools** list, click **Add Node Pool**.
    5. In the **Add Node Pool** dialog box, provide the following information:
       * **Name** : The name of the new node pool. Avoid entering confidential information.
       * **Compartment** : The compartment in which to create the new node pool.
       * **Node pool options** : In the **Node Count** field, enter the number of nodes you want in this node pool. The default is 0. The maximum number is 128 per cluster, which can be distributed across multiple node pools.
       * **Network Security Group** : If you check the box to enable network security groups, click **Add Network Security Group** and select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
       * **Placement configuration**
         * **Worker Node Subnet** : Select a subnet that has configuration such as the "worker" subnet described in [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet."). Select only one subnet. The subnet must have rules set to communicate with the control plane endpoint. The subnet must use the private route table and must have a security list like the worker-seclist security list described in [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.").
         * **Fault domain** : Select a fault domain, or select **Automatically select the best fault domain** , which is the default option.
       * **Source Image** : Select an image.
         1. Select the **Platform Image Source Type**.
         2. Select an image from the list.
The image list has columns Operating System, OS Version, and Kubernetes Version. You can use the drop-down menu arrow to the right of the OS Version or Kubernetes Version to select a different version.
If the image that you want to use is not listed, use the CLI procedure and specify the OCID of the image. To get the OCID of the image you want, use the `ce node-pool get` command for a node pool where you used this image before.
**Note**
The image that you specify must not have a Kubernetes version that's newer than the Kubernetes version that you specified when you created the cluster. The Kubernetes Version for the cluster is in a column of the cluster list table.
       * **Shape** : Select a shape for the worker nodes. The shape is VM.PCAStandard.E5.Flex and you can't change it.
Specify the number of OCPUs you want. You can optionally specify the total amount of memory you want. The default value for gigabytes of memory is 16 times the number you specify for OCPUs. Click inside each value field to see the minimum and maximum allowed values.
       * **Boot Volume** : (Optional) Check the box to specify a custom boot volume size.
**Boot volume size (GB)** : The default boot volume size for the selected image is shown. To specify a larger size, enter a value from 50 to 16384 in gigabytes (50 GB to 16 TB) or use the increment and decrement arrows.
If you specify a custom boot volume size, you need to extend the partition to take advantage of the larger size. Oracle Linux platform images include the `oci-utils` package. Use the `oci-growfs` command from that package to extend the root partition and then grow the file system. See[oci-growfs](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs).
       * **Cordon and Drain** : (Optional) Use the arrows to decrease or increase the number of minutes of eviction grace duration. You cannot deselect "Force terminate after grace period." Nodes are deleted after their pods are evicted or at the end of the eviction grace duration, even if not all pods are evicted.
For descriptions of cordon and drain and eviction grace duration, click the CLI tab on this page, and see _Node and node pool deletion settings_.
       * **SSH Key** : The public SSH key for the worker nodes. Either upload the public key file or copy and paste the content of the file.
       * **Kubernetes Labels** : Click the Add Kubernetes Label button and enter a key name and value. You can use these labels to target pods for scheduling on specific nodes or groups of nodes. See the description and example in the CLI procedure.
       * **Node Pool Tags** : Defined or free-form tags for the node pool resource.
**Note**
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the node pool resource.
       * **Node Tags** : Defined or free-form tags that are applied to every node in the node pool.
**Important**
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated.
    6. Click **Add Node Pool**.
The details page for the node pool is displayed. Under **Resources** , click**Work Requests** to see the progress of the node pool creation and see nodes being added to the Nodes list.
To identify these nodes in a list of instances, note that the names of these nodes are in the format `oke-ID`, where `ID` is the first 32 characters after the `pca_name` in the node pool OCID. Search for the instances in the list whose names contain the `ID` string from this node pool OCID.
To identify these nodes in a list of instances, note that the names of these nodes contain the first 32 characters after the `ccc_name` of the node pool OCID, and they contain the cluster OCID in the OraclePCA-OKE/cluster_id tag.
**What's Next:**
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
  * Use the [oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html) command and required parameters to create a new node pool.
Copy
```
oci ce node-pool create --cluster-id <cluster_OCID> --compartment-id <compartment_OCID> --name <pool_name> --node-shape <node_shape_name> [OPTIONS]
```

    1. Get the information you need to run the command.
       * The OCID of the compartment where you want to create the node pool: `oci iam compartment list`
       * The OCID of the cluster for this node pool: `oci ce cluster                   list`
       * The name of the node pool. Avoid entering confidential information.
       * The placement configuration for the nodes, including the subnet and fault domain. See the "Placement configuration" description in the Console procedure. Use the following command to show the content and format of this option:
Copy
```
$ oci ce node-pool create --generate-param-json-input placement-configs
```

Use the following command to list fault domains: `oci iam                   fault-domain list`. Don't specify more than one fault domain or more than one subnet in the placement configuration. To allow the system to select the best fault domains, don't specify any fault domain.
       * The OCID of the image to use for the nodes in this node pool.
Use the following command to get the OCID of the image that you want to use:
Copy
```
$ oci compute image list --compartment-id compartment_OCID
           
```

If the image that you want to use isn't listed, you can get the OCID of the image from the output of the `ce node-pool get` command for a node pool where you used this image before.
**Note**
The image that you specify must have `-OKE-` in its `display-name` and must not have a Kubernetes version that's newer than the Kubernetes version that you specified when you created the cluster.
The Kubernetes version for the cluster is shown in `cluster list` output. The Kubernetes version for the image is shown in the `display-name` property in `image list` output. The Kubernetes version of the following image is 1.28. 8.
Copy
```
"display-name": "uln-pca-Oracle-Linux8-OKE-**1.28.8**-20240909.oci"
```

Don't specify the `--kubernetes-version` option in the `node-pool create` command.
You can specify a custom boot volume size in gigabytes. The default boot volume size is 50 GB. To specify a custom boot volume size, use the `--node-source-details` option to specify both the boot volume size and the image. You can't specify both `--node-image-id` and `--node-source-details`. Use the following command to show the content and format of the node source details option.
Copy
```
$ oci ce node-pool create --generate-param-json-input node-source-details
```

If you specify a custom boot volume size, you need to extend the partition to take advantage of the larger size. Oracle Linux platform images include the `oci-utils` package. Use the `oci-growfs` command from that package to extend the root partition and then grow the file system. See [oci-growfs](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs).
       * The name of the shape of the worker nodes in this node pool. For Compute Cloud@Customer X10 systems, the shape of the control plane nodes is VM.PCAStandard.E5.Flex.
Specify the shape configuration, as shown in the following example. You must provide a value for `ocpus`. The `memoryInGBs` property is optional; the default value in gigabytes is 16 times the number of `ocpus`.
Copy
```
--node-shape-config '{"ocpus": 32, "memoryInGBs": 512}'
```

       * (Optional) The OCID of the Network Security Group to use for the nodes in this node pool. Don't specify more than one NSG.
       * (Optional) Labels. Setting labels on nodes enables you to target pods for scheduling on specific nodes or groups of nodes. Use this functionality to ensure that specific pods only run on nodes with certain isolation, security, or regulatory properties.
Use the `--initial-node-labels` option to add labels to the nodes. Labels are a list of key/value pairs to add to nodes after they join the Kubernetes cluster. There are metadata key restrictions. See [Metadata Key Restrictions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-instances.htm#compute-instances__metadata-key-restrictions).
The following is an example label to apply to the nodes in the node pool:
```
--initial-node-labels '[{"key":"disktype","value":"ssd"}]
```

An easy way to select nodes based on their labels is to use `nodeSelector` in the pod configuration. Kubernetes only schedules the pod onto nodes that have each of the labels that are specified in the `nodeSelector` section.
The following example excerpt from a pod configuration specifies that pods that use this configuration must be run on nodes that have the `ssd` disk type label:
```
nodeSelector:
 disktype: ssd
```

       * (Optional) Node metadata. Use the ``--node-metadata`` option to attach custom user data to nodes. See the following proxy settings item for a specific example.
You can use the ``--node-metadata`` option to set node labels, as an alternative to using the `--initial-node-labels` option. In the following example, the value of the `oke-initial-node-labels` key is a list of key/value pairs:
```
--node-metadata '{"oke-initial-node-labels" : "disktype=ssd, environment=production"}'
```

See [Metadata Key Restrictions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-instances.htm#compute-instances__metadata-key-restrictions).
       * (Optional) Proxy settings. If your network requires proxy settings to enable worker nodes to reach outside registries or repositories, for example, create an argument for the ``--node-metadata`` option.
In the ``--node-metadata`` option argument, provide values for `crio-proxy` and `crio-noproxy` as shown in the following example file argument:
Copy
```
{
 "crio-proxy": "http://<your_proxy>.<your_domain_name>:<your_port>",
 "crio-noproxy": "localhost,127.0.0.1,<your_domain_name>,ocir.io,<Kubernetes_cidr>,<pods_cidr>"
}
```

       * (Optional) Node and node pool deletion settings. You can specify how to handle node deletion when you delete a node pool, delete a specified node, decrement the size of the node pool, or change the node pool nodes placement configuration. These node deletion parameters can also be set or changed when you update the node pool, delete a specified node, or delete the node pool.
To specify node pool deletion settings, create an argument for the `--node-eviction-node-pool-settings` option. You can specify the eviction grace duration (`evictionGraceDuration`) for nodes. Nodes are always deleted after their pods are evicted or at the end of the eviction grace duration.
         * Eviction grace duration. This value specifies the amount of time to allow to cordon and drain worker nodes.
A node that's cordoned can't have new pods placed on it. Existing pods on that node aren't affected.
When a node is drained, each pod's containers terminate gracefully and perform any necessary cleanup.
The eviction grace duration value is expressed in ISO 8601 format. The default value and the maximum value are 60 minutes (PT60M). The minimum value is 20 seconds (PT20S). OKE always tries to drain nodes for at least 20 seconds.
         * Force delete. Nodes are always deleted after their pods are evicted or at the end of the eviction grace duration. After the default or specified eviction grace duration, the node is deleted, even if one or more pod containers aren't completely drained.
The following shows an example argument for the `--node-eviction-node-pool-settings` option. If you include the `isForceDeleteAfterGraceDuration` property, then its value must be `true`. Nodes are always deleted after their pods are evicted or at the end of the eviction grace duration.
Copy
```
--node-eviction-node-pool-settings '{"evictionGraceDuration": "PT30M", "isForceDeleteAfterGraceDuration": true}'
```

**Note**
If you use Terraform and you specify `node_eviction_node_pool_settings`, then you must explicitly set `is_force_delete_after_grace_duration` to `true`, even though true is the default value. The `is_force_delete_after_grace_duration` property setting isn't optional if you're using Terraform.
       * (Optional) Tags. Add free-form tags for the node pool resource by using the `--defined-tags` or `--freeform-tags` options. Do not specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the node pool resource.
To add free-form tags to all nodes in the node pool, use the `--node-defined-tags` and `--node-freeform-tags` options.
**Important**
Do not specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated.
    2. Run the create node pool command.
Example:
See the [Using the Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pool-using-the-console) procedure for information about the options shown in this example, and other options such as `--node-boot-volume-size-in-gbs` and `nsg-ids`.
Copy
```
$ oci ce node-pool create \
--cluster-id ocid1.cluster.unique_ID --compartment-id ocid1.compartment.unique_ID \
--name node_pool_name --node-shape shape_name --node-image-id ocid1.image.unique_ID \
--placement-configs '[{"availabilityDomain":"AD-1","subnetId":"ocid1.subnet.unique_ID"}]' \
--size 10 --ssh-public-key "public_key_text"
```

Use the `work-request get` command to check the status of the node pool create operation. The work request OCID is in `created-by-work-request-id` in the `metadata` section of the `cluster get` output.
Copy
```
$ oci ce work-request get --work-request-id workrequest_OCID
        
```

To identify these nodes in a list of instances, note that the names of these nodes are in the format `oke- ID `, where ` ID ` is the first 32 characters after the name in the node pool OCID. Search for the instances in the list whose names contain the ` ID ` string from this node pool OCID.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next:**
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.
  * Use the [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool) operation to create a new node pool.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
    1. Configure any registries or repositories that the worker nodes need. Ensure you have access to a self-managed public or intranet container registry to use with the OKE service and your application images.
    2. Create a service to expose containerized applications outside the Compute Cloud@Customer. See [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.").
    3. Create persistent storage for applications to use. See [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.").
To change the properties of existing nodes, you could instead create a new node pool with the new settings and move the work to the new nodes.


Was this article helpful?
YesNo

