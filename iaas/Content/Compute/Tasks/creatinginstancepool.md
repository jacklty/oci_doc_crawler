Updated 2025-01-13
# Creating Instance Pools
Use instance pools to create and manage multiple compute instances within the same region as a group.
When you create an instance pool, you use an [instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) as the template to create instances in the pool. You can also [attach existing instances to a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm#attach-instance "Attach an existing instance to an instance pool, and then select which instances you want to manage as a group.") by updating the pool.
Optionally, you can associate one or more [load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm) and [network load balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/overview.htm) with an instance pool. If you do this, when you add an instance to the instance pool, the instance is automatically added to the load balancer's or network load balancer's **backend set**. After the instance reaches a healthy state (the instance is listening on the configured port number), incoming traffic is automatically routed to the new instance.
To determine whether capacity is available for a specific shape before you create an instance pool, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
## Before You Begin 🔗 
Before you can create an instance pool, you need:
  * An instance configuration. An instance configuration is a template that defines the settings to use when creating instances. When you create the instance pool, [monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) by default on instances that support monitoring, regardless of the settings in the instance configuration. For more information, see [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration).
**Note** You cannot create an instance pool from an instance configuration where the image source is a boot volume.
  * If you want to associate the instance pool with a load balancer or network load balancer, you need a load balancer or network load balancer and backend set. For steps to create a load balancer, see [Load Balancer Management](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm). For steps to create a network load balancer, see [Network Load Balancer Management](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm)


  * To create an instance pool:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**. 
    2. Click **Create instance pool**.
    3. On the **Create instance pool** page, do the following:
**Caution** Avoid entering confidential information when assigning descriptions, tags, or friendly names to cloud resources through the Oracle Cloud Infrastructure Console, API, or CLI.
      1. Enter a name for the instance pool. It doesn't have to be unique, and you can change it later. 
      2. Select the compartment to create the instance pool in.
      3. From the **Instance configuration in _compartment_** menu, select an instance configuration that you want to use.
      4. Specify the target number of instances in the **Number of instances** field for the instance pool.
      5. Click **Show advanced options** to display tagging and instance display and host name formatter options.
         * On the **Tags** tab, add tags for the instance pool.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
         * On the **Formatter options** tab, customize instance display name and instance host name for instances you create in the pool.
           * In the **Instance display name formatter** field, to customize the display name of an instance that you create for this pool, enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the `${launchCount}` token. For example: `my-string-${launchCount}`.
           * In the **Instance host name formatter** field, enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the `${launchCount}` token. For example: `my-string-${launchCount}`.
    4. Click **Next**.
    5. On the **Configure pool placement** page, select the location where you want to place the instances:
      1. Select the **Availability domain** to create the instances in.
      2. For the **Fault domains** field, perform one of the following actions:
         * If you want the system to make a best effort to distribute instances across fault domains based on capacity, then leave the field empty.
         * If you want to require that the instances in the pool are distributed evenly in one or more fault domains, then select the fault domains to place the instances in. If sufficient capacity is unavailable in the selected fault domains, then the pool won't launch or scale successfully. For more information, see [Distributing Instances Across Fault Domains for High Availability](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#faultdomains).
      3. In the **Primary VNIC** section, configure the network details for the instances:
         * **Virtual cloud network:** The virtual cloud network (VCN) to create the instances in.
         * **Subnet:** A subnet within the cloud network to attach the instances to. The subnets are either public or private. Private means the instances in that subnet can't have public IP addresses. For more information, see [Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/internetaccess.htm). Subnets are either specific to an availability domain or regional (regional ones have "regional" after the name). We recommend using [regional subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet). 
For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
      4. If secondary VNICs are defined by the instance configuration, then a **Secondary VNIC** section appears. Select the secondary VCN and subnet for the instance pool.
      5. If you want the instance pool to create instances in more than one availability domain, then click **+ Another availability domain**. Then, repeat the previous steps.
    6. If you want to associate a load balancer or network load balancer with the instance pool, then select the **Attach a load balancer** check box and proceed as follows:
      1. Specify the type of load balancer you want to associate with the instance pool.
For more information, see [Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm) or [Overview of Flexible Network Load Balancer](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/overview.htm).
      2. Select the load balancer or network load balancer from the **Load Balancer** list.
The choices available in this list are determined by the load balancer type that you selected and what is available in the current compartment. Click **Change Compartment** and select another compartment to display the load balancer or network load balancer choices available there.
      3. Select the backend set on the load balancer or network load balancer to add instances to.
      4. In the **Port** field, enter the server port on the instances to which the load balancer or network load balancer must direct traffic. This value applies to all instances that use this load balancer or network load balancer attachment.
         * Load balancer port values range from 1 to 65535.
         * Network load balancer ports range from 1 to 65535 when the load balancer is configured for a specific port. If the network load balancer is configured for all ports, then the value in the **Port** field defaults to **Any** and cannot be changed.
      5. In the **VNIC** list, select the **VNIC** to use when adding the instance to the backend set. Instances that belong to a backend set are also called backend servers. The private IP address is used. This value applies to all instances that use this load balancer or network load balancer attachment.
      6. If you want to associate additional load balancers and network load balancers with the instance pool, then click **+ Another load balancer** and repeat the previous steps.
For background information about load balancers, see [Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm).
    7. Click **Next**.
    8. Review the instance pool details, and then click **Create**.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * To create an instance pool, use the [instance-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/create.html) command:
Command
CopyTry It
```
oci compute-management instance-pool create --compartment-id <COMPARTMENT_OCID> --instance-configuration-id <INSTANCE_CONFIGURATION_OCID> --placement-configurations <file://path/to/file.json> --size <NUMBER_OF_INSTANCES>
```

<file://path/to/file.json> is the path to a JSON file that defines the placement configuration. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [CreateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/CreateInstancePool) operation to create an instance pool.


Was this article helpful?
YesNo

