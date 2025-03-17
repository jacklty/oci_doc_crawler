Updated 2025-01-15
# Migrating to VCN-Native Clusters
_Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine (OKE)._
In earlier releases (before March 16, 2021), Kubernetes Engine provisioned clusters with Kubernetes API endpoints that were not integrated into your own VCN. The Kubernetes API endpoint was public, and you could not restrict access to it. You can continue to create such clusters using the CLI or API, but not the Console.
After March 16, 2021, Kubernetes Engine can provision clusters with their Kubernetes API endpoints in a subnet in your own VCN (these clusters are known as "VCN-native clusters"). You have more flexibility to configure VCN-native clusters to meet your own security and networking requirements. You can configure the Kubernetes API endpoint to make it privately accessible within your VCN (and a peered on-premise network), or to make it publicly accessible from the internet:
  * To make the Kubernetes API endpoint privately accessible, host the Kubernetes API endpoint in a private subnet and do not assign a public IP address to it. 
  * To make the Kubernetes API endpoint publicly accessible from the internet, host the Kubernetes API endpoint in a public subnet and assign a public IP address to it.


You can control access to the Kubernetes API endpoint subnet using security rules defined for network security groups (recommended) or security lists.
To take advantage of the security control offered by VCN-native clusters, you can migrate an existing cluster to integrate its Kubernetes API endpoint into your own VCN.
Cluster migration has the following stages:
  * **Stage 1: Migration in progress**
You start the migration by selecting the cluster to migrate, and then specifying the existing VCN and the private or public subnet to host the new Kubernetes API endpoint. The migration usually takes around 15 minutes. 
During this time, the Kubernetes API continues to be accessible via the public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable.
  * **Stage 2: Migration is complete, and pending decommission of the public Kubernetes API endpoint that is not integrated into your own VCN**
When migration is complete, the cluster becomes accessible via the new Kubernetes API endpoint in your own VCN, as well as via the public Kubernetes API endpoint that is not integrated into your VCN. During this decommissioning period, update the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint. By default, you have 30 days to complete the updates, but you can reduce the decommissioning period to as little as 5 days, or increase it to more than 30 days. File a [support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) if you want to reduce or increase the time before the public Kubernetes API endpoint that is not integrated into your own VCN is decommissioned.
  * **Stage 3: The public Kubernetes API endpoint that is not integrated into your own VCN is decommissioned**
At the end of the decommissioning period (30 days after migration, or the time you request), the cluster ceases to be accessible via the public Kubernetes API endpoint that is not integrated into your VCN. The cluster is only accessible via the new Kubernetes API endpoint integrated into your VCN.


## Migrating an Existing Cluster to be VCN-native 🔗 
To migrate an existing cluster to integrate its Kubernetes API endpoint into your own VCN:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
**Migration required** labels appear on the **Cluster List** page beside the names of clusters with Kubernetes API endpoints that are not integrated into your VCN.
  3. On the **Cluster List** page, click the name of the cluster that you want to migrate.
When you select a cluster that you can migrate, the **Migrate Cluster** button appears at the top of the **Cluster Details** page. 
  4. If you want the cluster's Kubernetes API endpoint to be publicly accessible from the internet and hosted in a new public subnet in the same VCN as the cluster (creating and configuring new network resources as required), perform an **Automatic Migration** as follows:
    1. At the top of the **Cluster Details** page, click **Migrate Cluster** to integrate the cluster's Kubernetes API endpoint into your own VCN.
    2. In the **Migrate to VCN-Native Cluster** dialog box, select **Automatic Migration** to create a new regional subnet in the cluster's VCN with a 10.0.0.0/28 CIDR block, along with security lists and route tables.
    3. Click **Launch Workflow** and review the migration summary in the **VCN-Native Endpoint Cluster Migration** dialog box.
    4. Click **Migrate** to create new network resources and migrate the cluster.
Kubernetes Engine starts migrating the cluster, as shown in the **Migrating Cluster** dialog.
    5. Click **Close** to close the **Migrating Cluster** dialog.
  5. If you want the cluster's Kubernetes API endpoint to be privately accessible within your VCN or publicly accessible from the internet, and hosted in an existing regional public or private subnet in the same VCN as the cluster, perform a **Custom Migration** as follows:
    1. Confirm the following network resources already exist in the VCN and are configured correctly to host the Kubernetes API endpoint (if not, create and configure them appropriately):
       * a regional public or private subnet (see [Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b))
       * if the subnet is public, an internet gateway (see [Internet Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#internetgatewayconfig))
       * if the subnet is private, a NAT gateway (see [NAT Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#natgatewayconfig)) and a service gateway (see [Service Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#servicegatewayconfig))
       * a route table with the necessary route rules (see [Route Table for Kubernetes API Endpoint Subnets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#routetableconfig__section_dpd_wwv_r4b))
       * a network security group (recommended) and/or security list with the necessary ingress and egress rules (see [Security Rules for the Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__section_jsz_kqw_r4b))
For example configurations, see [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
    2. At the top of the **Cluster Details** page, click **Migrate Cluster** to integrate the cluster's Kubernetes API endpoint into your own VCN.
    3. In the **Migrate to VCN-Native Cluster** dialog box, select **Custom Migration**. 
    4. Click **Launch Workflow** and specify:
       * **Kubernetes API Endpoint Subnet:** A regional subnet to host the cluster's Kubernetes API endpoint. The subnet you specify can be public or private. The Kubernetes API endpoint is always assigned a private IP address. If you specify a public subnet, you can optionally expose the Kubernetes API endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). To simplify access management, Oracle recommends the Kubernetes API endpoint is in a different subnet to worker nodes and load balancers. For more information, see [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
       * **Use network security groups to control traffic:** Optionally, restrict the access to the cluster's Kubernetes API endpoint using one or more network security groups (NSGs) that you specify. For more information about the security rules to specify for the NSG, see [Security Rules for the Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__section_jsz_kqw_r4b).
       * **Assign a public IP address to the API endpoint:** If you selected a public subnet for the Kubernetes API endpoint, you can optionally expose the endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). If you do not assign a public IP address, update route rules and security rules to enable access to the endpoint using a service gateway and a NAT gateway (see [Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b)).
    5. Click **Migrate** to create new network resources and migrate the cluster.
Kubernetes Engine starts migrating the cluster.


Migration usually takes around 15 minutes to complete. During this time, the Kubernetes API continues to be accessible via the public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable.
When migration is complete, the **Cluster Details** page shows the name of the **Kubernetes API Endpoint Subnet** , the IP address of the **Kubernetes API Private Endpoint** , and (if you assigned a public IP address to the Kubernetes API endpoint) the IP address of the **Kubernetes API Public Endpoint**.
The **Cluster Details** page also indicates that you have 30 days to update the configuration of your kubectl, tools, and CI/CD pipelines to access the new Kubernetes API endpoint (see [Setting Up Access to a Migrated Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#Configuring_migrated_cluster)). During this decommissioning period, the newly migrated cluster is accessible via both the new Kubernetes API endpoint in your VCN, and via the public Kubernetes API endpoint that is not integrated into your own VCN.
## Setting Up Access to a Migrated Cluster 🔗 
Having migrated a cluster to integrate its Kubernetes API endpoint into your own VCN, you have to update the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint. At a minimum, you'll want to update the cluster's Kubernetes configuration file (commonly known as the 'kubeconfig' file) to enable access to the migrated cluster using kubectl, as described in this topic. You also need to update any manifest files that include references to the cluster's Kubernetes API endpoint IP address.
Follow the instructions in this topic to generate a new kubeconfig file. These instructions assume the cluster's kubeconfig file is saved in the default location (`$HOME/.kube`) and with the default name (`config`). If that is not the case, adapt the instructions accordingly.
  1. In the terminal window where you normally run Oracle Cloud Infrastructure CLI commands, run the following command to update the cluster's existing kubeconfig file:
Copy
```
oci ce cluster create-kubeconfig --cluster-id <cluster-ocid> --file <kubeconfig-file-location> --region <region-name> --token-version 2.0.0 --kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the existing cluster you want to make VCN-native.
     * `--file <kubeconfig-file-location>` is the location of the cluster's kubeconfig file.
     * `--region <region-name>` is the region in which the cluster is located.
     * `--kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT` specifies whether to add the private IP address or the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
For example:
Copy
```
oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.phx.aaaaaaaaae... --file $HOME/.kube/config --region us-phoenix-1 --token-version 2.0.0 --kube-endpoint PUBLIC_ENDPOINT
```

Assuming the kubeconfig file already exists in the location you specify, details about the cluster are added as a new context to the existing kubeconfig file, including the cluster's new Kubernetes API endpoint in your own VCN. The `current-context:` element in the kubeconfig file is set to point to the newly-added context.
For more information about setting up the kubeconfig file, see [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Verify that kubectl can connect to the cluster using the Kubernetes API endpoint in your own VCN by entering the following command:
Copy
```
kubectl get nodes
```

Information about the nodes in the cluster is shown. 
You can now use kubectl to perform operations on the cluster using the Kubernetes API endpoint in your own VCN.


**Note** Until the original API endpoint that is not integrated into your VCN is decommissioned, you can continue to generate the original kubeconfig file by omitting the `--kube-endpoint` option from the `oci ce cluster         create-kubeconfig` command.
## Frequently Asked Questions about Cluster Migration 🔗 
### What are VCN-native clusters?
Kubernetes Engine creates Kubernetes clusters that are completely integrated into your Oracle Cloud Infrastructure Virtual Cloud Network (VCN). Worker nodes, load balancers, and the Kubernetes API endpoint are part of your own VCN, and you can configure them as public or private. Such clusters that are fully integrated into your own VCN are known as "VCN-native clusters".
### How can I tell if a cluster is already a VCN-native cluster?
If you're not sure whether a cluster is already a VCN-native cluster, view information about the cluster (for example, on the **Cluster Details** page in the Console). If the cluster is already a VCN-native cluster, the cluster details include **Kubernetes API Endpoint** information. If the cluster is not yet a VCN-native cluster, the cluster details simply include the **Kubernetes Address**.
### Do I have to migrate all my existing clusters?
No, you only have to migrate existing clusters that you want to turn into VCN-native clusters. If you don't want to integrate a cluster's Kubernetes API endpoint into your own VCN, simply don't migrate that cluster.
### Does the migration involve any downtime?
While a cluster is being migrated to a VCN-native cluster, the cluster's Kubernetes API continues to be accessible via the public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable. 
### Should I choose automatic migration or custom migration?
Automatic migration creates a regional subnet in the cluster's VCN with a 10.0.0.0/28 CIDR block, along with security lists and route tables. The subnet is public and the API endpoint is assigned a public IP address. Automatic migration only supports clusters with node pools in the same compartment as the cluster. For clusters with node pools in different compartments, perform a custom migration.
Custom migration enables you to choose an existing public or private regional subnet to host the cluster's Kubernetes API endpoint. If you choose a public regional subnet, you can optionally expose the Kubernetes API endpoint to the internet by assigning a public IP address to the endpoint. You can optionally choose to use network security groups.
### How do I configure a subnet in my VCN to host the Kubernetes API endpoint?
Refer to [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm) for details about configuring the Kubernetes API endpoint subnet, security lists, and route table.
### I want to test the migration to a VCN-native cluster. How can I create a cluster with a Kubernetes API endpoint that is not integrated into my VCN?
In the terminal window where you normally run Oracle Cloud Infrastructure CLI commands, run the following command to create a test cluster with a Kubernetes API endpoint that is not integrated into your VCN:
Copy
```
oci ce cluster create --compartment-id <compartment-ocid> --kubernetes-version v<kubernetes-version-number> --name <cluster-name> --vcn-id <vcn-ocid>
```

where:
  * `--compartment-id <compartment-ocid>` is the OCID of the compartment to which you want the test cluster to belong.
  * `--kubernetes-version v<kubernetes-version-number>` is a supported version of Kubernetes (see [Currently Supported Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions)). For example, `--kubernetes-version v1.19.7`
  * `--name <cluster-name>` is a name of your choice for the test cluster. For example, `--name test-vcn-native-migration`
  * `--vcn-id <vcn-ocid>` is the OCID of the VCN in which to create the test cluster.


Having created a test cluster with a Kubernetes API endpoint that is not integrated into your VCN, you can now migrate the test cluster to make it a VCN-native cluster. See [Migrating an Existing Cluster to be VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#contengmigratingclusters_topic_Using_the_Console).
Remember to delete the test cluster when you no longer need it.
### How do I increase or reduce the time until the decommission of the public Kubernetes API endpoint that is not integrated into my own VCN?
The decommissioning period is the length of time during which a newly migrated cluster is accessible via both the new Kubernetes API endpoint in your own VCN, and via the public API endpoint that was not integrated into your VCN. The decommissioning period ensures there is no downtime while you update the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint.. 
The decommissioning period starts as soon as Kubernetes Engine has migrated the cluster to integrate its Kubernetes API endpoint into your own VCN. By default, you have 30 days to complete the updates, but you can reduce the decommissioning period to as little as 5 days or increase it to more than 30 days. File a [support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) if you want to reduce or increase the decommissioning period, and specify:
  * **Summary:** `Request to modify Reclamation Extension in           <region-name>`
  * **Region:** `<region-name>`
  * **Component:** `Control Plane`
  * **Details:** Include the following:
    * `Tenancy: <tenancy-name>`
    * `Tenancy Id: <tenancy-ocid>`
    * `Cluster: <cluster-name>`
    * `Cluster Id: <cluster-ocid>`
    * `Requested expiration date/time: <date-and-time>`


Was this article helpful?
YesNo

