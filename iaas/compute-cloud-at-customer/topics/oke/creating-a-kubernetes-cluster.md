Updated 2024-12-16
# Creating an OKE Cluster
Learn how to create OKE Clusters on Compute Cloud@Customer.
The Network Load Balancer and public IP address are created and assigned as part of cluster creation.
**Important**
Before you can create a cluster, the following conditions must be met:
  * The `OraclePCA-OKE.cluster_id` defined tag must exist in the tenancy. See [Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.")
The OraclePCA-OKE/cluster_id defined tag is required to create or update an OKE cluster or node pool. This tag also is used to identify instances that need to be in a dynamic group. 
  * All fault domains must be healthy.
  * Each fault domain must have at least one healthy compute instance.
  * Sufficient resources must be available to create a cluster. See [Compute Cloud@Customer Metrics](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/metrics.htm#metrics "You can monitor Compute Cloud@Customer infrastructure resources using metrics. Compute Cloud@Customer metrics provide you with the total and available OCPU, memory, and storage resources for the infrastructure.").
  * Ensure that no infrastructure upgrade is scheduled during the cluster create. See [Managing Upgrade Schedules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/managing-upgrade-schedules.htm#managing-upgrade-schedules "Use Upgrade Schedules to define time periods when a Compute Cloud@Customer infrastructure may be upgraded by Oracle.").


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-cluster.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. On the clusters list page, click **Create Cluster**.
    3. In the **Create Cluster** dialog box, provide the following information:
       * **Name** : Enter a name for the new cluster. Avoid entering confidential information.
       * **Compartment** : Select the compartment in which to create the new cluster.
       * **Kubernetes Version** : Select the version of Kubernetes to run on the control plane nodes. Accept the default version or select a different version.
If the Kubernetes version that you want to use isn't listed, use the CLI or the API to create the cluster and specify the Kubernetes version.
       * **Tagging** : Add the following free-form tags for the cluster resource.
**Note**
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the cluster resource.
Use `OraclePCA` defined tags to provide the following information for control plane nodes. If these tags aren't listed in the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") Tagging menus, you must create them. See [Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.").
**Note**
None of these values - SSH key, number of nodes, node shape, or node shape configuration - can be set or changed after the cluster is created. If you set these tags when you update the cluster, the new values are ignored.
         * **Your public SSH key**.
Specify `sshkey` for the tag key (`OraclePCA.sshkey`). Paste your public SSH key into the Value field.
**Important**
You can't add an SSH key after the cluster is created.
         * **Number of nodes**.
By default, the number of nodes in the control plane is 3. You can specify 1, 3, or 5 nodes. To specify the number of control plane nodes, specify `cp_node_count` for the tag key (`OraclePCA.cpNodeCount`), and select `1`, `3`, or `5` in the **Value** field.
         * **Node shape**.
For Compute Cloud@Customer X10 systems, the shape of the control plane nodes is VM.PCAStandard.E5.Flex and you can't change it. 
         * **Node shape configuration**.
You can change the default shape configuration. 
To provide shape configuration information, specify `cp_node_shape_config` for the tag key (`OraclePCA.cpNodeShapeConfig`). You must specify the number of OCPUs (`ocpus`) you want. You can optionally specify the total amount of memory you want (`memoryInGBs`). The default value for gigabytes of memory is 16 times the number you specify for OCPUs.
**Note**
If the cluster will have 1-10 worker nodes, specify at least 16 GB memory. If the cluster will have 11-128 worker nodes, specify at least 2 OCPUs and 32 GB memory. You can't change the number of OCPUs or amount of memory when you update the cluster.
In the **Value** field for the tag, enter the node shape configuration value as shown in the following examples.
In the following example, the default amount of memory is be configured:
Copy
```
{"ocpus":1}
```

In the following example, the amount of memory is specified:
Copy
```
{"ocpus":2, "memoryInGBs":48}
```

**Note**
If you use Terraform to specify a complex value (a value that's a key/value pair), then you must escape the double quotation marks in the value as shown in the following example:
Copy
```
"OraclePCA.cpNodeShapeConfig"="{\"ocpus\":2,\"memoryInGBs\":48}"
```

    4. Click **Next**.
    5. On the **Network** page in the **Create Cluster** dialog box, provide the following information:
       * **Network Type**. Specifies how pods running on nodes in the cluster communicate with each other, with the cluster's control plane nodes, with pods on other clusters, with other services (such as storage services), and with the internet.
The **Flannel overlay** network type encapsulates communication between pods in the flannel overlay network. The flannel overlay network is a simple private overlay virtual network that satisfies the requirements of the Kubernetes networking model by attaching IP addresses to containers. The pods in the private overlay network are only accessible from other pods in the same cluster.
       * **VCN**. Select the VCN that has the configuration of the "oke_vcn" VCN described in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route.").
       * **Kubernetes Service LB Subnet**. The subnet that's configured to host the load balancer in a Kubernetes cluster. Select the subnet that has a configuration such as the "service-lb" subnet described in [Creating an OKE Worker Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a security list and a worker load balancer subnet.").
       * **Kubernetes API Endpoint Subnet**. The regional subnet in which to place the cluster endpoint. Select the subnet that has configuration such as the "control-plane-endpoint" subnet described in [Creating an OKE Control Plane Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-subnet.htm#creating-a-control-plane-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating external and internal access security lists and a control plane subnet."). 
       * **Kubernetes Service CIDR Block**. (Optional) The default value is 10.96.0.0/16.
       * **Pods CIDR Block**. (Optional) The default value is 10.244.0.0/16.
       * **Network Security Group**. If you check the box to enable network security groups, click **Add Network Security Group** and select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
    6. Click **Next**.
    7. Review your entries and click **Submit**.
The details page for the cluster is displayed. 
Under **Resources** , click **Work Requests** to see the progress of the cluster creation. When the cluster is in the **Active** state, click **Node Pools** to add a node pool. See [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.").
The cluster details page doesn't list `OraclePCA` tags on the Tags tab (and you can't filter a list of clusters by the values of `OraclePCA` tags). To review the settings of the `OraclePCA` tags, use the CLI.
The cluster details page doesn't list the cluster control plane nodes. To view the control plane nodes, view the list of instances in the compartment where you created this cluster. Names of control plane nodes are in the following format:
Copy
```
oke-ID1-control-plane-ID2
        
```

       * ` ID1 ` - The first 32 characters after the ` ** _ccc_name_ ** `is the cluster OCID.
       * ` ID2 ` - A unique identifier added when the cluster has more than one control plane node.
Search for the instances in the list whose names contain the ` ID1 ` string from this cluster OCID.
**What's Next:**
[Create a Kubernetes Configuration File](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file__create-config-file)
  * Use the [oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html) command and required parameters to create a new cluster.
Copy
```
oci ce cluster create --compartment-id <coompartment_OCID> --kubernetes-version <version-to-install> --name <cluster_name> --vcn-id <VCN_OCID> [OPTIONS]
```

**Procedure**
    1. Get the information you need to run the command:
       * The OCID of the compartment where you want to create the cluster: `oci iam compartment list`
       * The name of the cluster. Avoid entering confidential information.
       * The Kubernetes version that you want to use. Use the following command to show a list of available Kubernetes versions:
```
oci ce cluster-options get --cluster-option-id all
```

You might can list more Kubernetes versions by using the `compute image list` command and looking in the display name. In the following example, the Kubernetes version in the image is 1.28.3:
```
"display-name": "uln-pca-Oracle-Linux8-OKE-**1.28.3**-20240210.oci"
```

Another way to specify a version that's not listed is to use the OCID of an older cluster instead of the keyword `all` as the argument of the `--cluster-option-id` option to list the Kubernetes version used for that specified cluster:
```
oci ce cluster-options get --cluster-option-id **_cluster_OCID_**
```

       * OCID of the virtual cloud network (VCN) in which you want to create the cluster. Specify the VCN that has the configuration of the "oke_vcn" VCN described in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route.").
       * OCID of the OKE service LB subnet. Specify the subnet that has configuration such as the "service-lb" subnet described in [Creating an OKE Worker Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a security list and a worker load balancer subnet."). Specify only one OKE service LB subnet.
       * OCID of the Kubernetes API endpoint subnet. Specify the subnet that has configuration such as the "control-plane-endpoint" subnet described in [Creating an OKE Control Plane Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-load-balancer-subnet.htm#creating-a-control-plane-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a control plane security list and a control plane load balancer subnet.").
       * OKE service CIDR block. (Optional) The default value is 10.96.0.0/16.
       * Pods CIDR block. (Optional) The default value is 10.244.0.0/16.
       * (Optional) The OCID of the Network Security Group to apply to the cluster endpoint. Don't specify more than one NSG. If you specify an NSG, use the following syntax:
Copy
```
--endpoint-nsg-ids '["ocid1.networksecuritygroup. _unique_ID_"]'
```

       * (Optional) Your public SSH key in RSA format. You can't add or update an SSH key after the cluster is created.
       * The network type. You don't need to specify the network type because `FLANNEL_OVERLAY` is used by default. If you specify the network type, you must specify the following:
Copy
```
--cluster-pod-network-options '{"cniType":"FLANNEL_OVERLAY"}'
```

    2. (Optional) Add free-form tags for the cluster resource by using the `--defined-tags` or `--freeform-tags` options.
**Note**
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the cluster resource.
Define an argument for the `--defined-tags` option to provide the following information for control plane nodes. Specify `OraclePCA` as the tag namespace.
**Note**
None of these values - SSH key, number of nodes, node shape, or node shape configuration - can be set or changed after the cluster is created. If you set these tags when you update the cluster, the new values are ignored.
       * Your public SSH key
Specify `sshkey` for the tag key, and paste your public SSH key as the value.
**Important**
You can't add an SSH key after the cluster is created.
       * Number of nodes
By default, the number of nodes in the control plane is 3. You can specify 1, 3, or 5 nodes. To specify the number of control plane nodes, specify `cpNodeCount` for the tag key, and enter `1`, `3`, or `5` for the value.
       * Node shape
For Compute Cloud@Customer, the shape of the control plane nodes is `VM.PCAStandard.E5.Flex` and you can't change it.
       * Node shape configuration
Specify the shape configuration. 
The default configuration is 1 OCPU and 10 gigabytes of memory.
To provide shape configuration information, specify `cpNodeShapeConfig` for the tag key. You must specify the number of OCPUs (`ocpus`) you want and you can specify the total amount of memory you want (`memoryInGBs`). The default value for gigabytes of memory is 16 times the number you specify for OCPUs.
**Note**
If the cluster will have 1-10 worker nodes, specify at least 16 GB memory. If the cluster will have 11-128 worker nodes, specify at least 2 OCPUs and 32 GB memory. You can't change the number of OCPUs or amount of memory when you update the cluster.
Specify defined tags, either inline, or in a file in JSON format, such as the following example file:
Copy
```
{
 "OraclePCA": {
  "sshkey": "ssh-rsa <remainder_of_key_text>",
  "cpNodeCount": 1,
  "cpNodeShape": "VM.PCAStandard1.Flex",
  "cpNodeShapeConfig": {
   "ocpus": 2,
   "memoryInGBs": 48
  }
 }
}
```

Use the following syntax to specify a file of tags. Specify the full path to the `.json` file unless the file is in the same directory where you're running the command.
Copy
```
--defined-tags file://cluster_tags.json
```

    3. Run the create cluster command.
Example:
The `--endpoint-public-ip-enabled true` option is required when `--endpoint-subnet-id` or `--endpoint-nsg-ids` is specified.
Copy
```
$ oci ce cluster create \
--compartment-id ocid1.compartment.unique_ID --kubernetes-version version \
--name "Cluster One" --vcn-id ocid1.vcn.unique_ID \
--endpoint-public-ip-enabled true \
--endpoint-subnet-id control-plane-endpoint_subnet_OCID \
--service-lb-subnet-ids '["service-lb_subnet_OCID"]' \
--defined-tags '{"OraclePCA":{"sshkey":"ssh-rsa remainder_of_key_text"}}'
```

The output from this `cluster create` command is the same as the output from the `cluster get` command.
Use the `work-request get` command to check the status of the create operation. The work request OCID is in `created-by-work-request-id` in the `metadata` section of the `cluster create` output.
Copy
```
$ oci ce work-request get --work-request-id workrequest_OCID

```

When the cluster is in the `ACTIVE` state, you can add a node pool.
To identify the control plane nodes for this cluster, list instances in the compartment where you created the cluster. Names of control plane nodes are in the following format:
Copy
```
oke-ID1-control-plane-ID2
```

       * ` ** _ID1_ ** `- The first 32 characters after the` **  _pca_name_ ** `in the cluster OCID.
       * ` ** _ID2_ ** `- A unique identifier added when the cluster has more than one control plane node.
Search for the instances in the list whose names contain the ` ** _ID1_ ** `string from this cluster OCID.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next:**
[Create a Kubernetes Configuration File](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file__create-config-file)
  * Use the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create a new cluster.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
**What's Next:**
[Create a Kubernetes Configuration File](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file__create-config-file)


Was this article helpful?
YesNo

