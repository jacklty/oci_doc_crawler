Updated 2024-08-06
# Creating an Instance Pool
On Compute Cloud@Customer, you can create an instance pool of instances that are within the same region.
Performing operations such as reset or delete on the pool object performs that operation on all instances that are members of the pool. Performing these operations on an individual instance that's a member of the pool doesn't affect any other member instances.
Creating an instance pool requires an instance configuration and a placement configuration. Instances that are added to the pool in a pool update can be created with different instance and placement configurations.
For instances in a pool, the value of the `displayName` property in the instance configuration is ignored. Instances in a pool are named `inst-**_aaaaa_**-**_pool_name_**`, where`** _aaaaa_**`is five random alphanumeric characters.
**Placement Configuration**
In addition to an instance configuration, pool creation requires a placement configuration. Values specified in a placement configuration override values specified in the instance configuration.
A placement configuration can specify fault domains, primary subnet, and secondary VNIC subnets.
**Fault Domains**
If you don't specify a fault domain in either the instance configuration or the placement configuration, the system automatically selects the best fault domains for the pool instances. If you specify only a single fault domain, all instances will be placed in only that fault domain. If you specify more than one fault domain, pool instances are placed in those fault domains evenly, providing better High Availability for the pool. If one fault domain can't accommodate additional instances, instance creation stops. The system will not place more instances in one fault domain than in another fault domain.
If some instances can't launch because of resource constraints, those instances remain in the Provisioning state and the pool remains in the Scaling state. After `size` instances are launched, the pool can transition to the Running state. While the pool is in the Scaling state, pool instances that are in the Running state are available to use.
The following are examples of actions you can take if a pool instance fails to launch because of resource constraints:
  * Update the pool and reduce the "Number of instances" or `size` value.
  * Update the pool and change the Fault Domain specification in the Compute Cloud@Customer Console or in a new instance or placement configuration.
  * Update the pool to specify a new instance configuration that creates instances that require fewer resources.
  * Stop an instance that isn't a member of a pool in the same fault domain where the pool instance is failing to launch because of resource constraints.
  * Delete an instance that isn't a member of a pool in the same fault domain where the pool instance is failing to launch because of resource constraints.


## Prerequisite 🔗 
Before you can create an instance pool, you need an instance configuration. An instance configuration is a template that defines the settings to use when creating instances. See [Working with Instance Configurations](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-configurations.htm#working-with-instance-configurations "On Compute Cloud@Customer, an instance configuration contains settings that are used to create compute instances. Instance configurations enable you to consistently create instances with the same configuration without reentering configuration values. You can use an instance configuration to create a single instance or to create an instance pool.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Configurations**.
    2. At the top of the page, select the compartment that contains the instance configuration that you want to use to create the pool.
    3. Click the instance configuration that you want to use for the instances in this pool.
    4. Under **Resources** , click **Attached Instance Pools**. 
    5. At the top of the page, select other compartments to list pools in other compartments.
Click **Create Instance Pool**.
    6. In the **Attach Instance Pool to** `**_instance_configuration_name_**`dialog box, enter the following information:
       * **Name** : Enter a name for the instance pool. The name doesn't need to be unique. This name is used in the names of the created instances. If you don't provide a name for the pool, the default name of the instance pool is `instancepool**_YYYYMMDDhhmmss_**`, where`** _YYYYMMDDhhmmss_**`is the creation date and time.
       * **Create in Compartment** : Select a compartment for this instance pool definition. Note that the instances in the pool will be created in the compartment that's specified in the instance configuration.
       * **Number of instances** : Specify the number of instances to create in this instance pool.
       * **Pool Placement** : Select the Fault Domains, VCN, and Subnet for instances in this instance pool. You can select a different compartment from which to choose the VCN and Subnet. See the descriptions of Placement Configuration and Fault Domains at the beginning of this section.
       * **Load Balancers** : Click the **Attach Load Balancers** box to specify load balancing for this pool. For information about load balancing, see [Load Balancer as a Service](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-as-a-service.htm#load-balancer-as-a-service "On Compute Cloud@Customer, you can configure the Load Balancing service \(LBaaS\) to automatically distribute network traffic."). Provide the following information:
         * Select the load balancer to attach to this pool.
         * Select the backend set to which to add these pool instances.
         * Enter the port number on the instances to which the load balancer must direct traffic.
         * Select the VNIC to use when adding the instance to the backend set. The private IP address is used.
To attach another load balancer, click **Add Load Balancer**. To attach a load balancer after the instance pool is created, see [Managing Instance Pool Load Balancer Attachments](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm#managing-intance-pool-load-balancer-attachments "On Compute Cloud@Customer, you can attach a load balancer to an instance pool or detach a load balancer attachment from an instance pool.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Create Instance Pool**.
The details page of the new pool is displayed. The requested instances are listed in the **Attached Instances** table in the **Resources** section as they're created. The new instances are named `inst-**_aaaaa_**-**_pool_name_**`, where`** _aaaaa_**`is five random alphanumeric characters. If you change the name of the pool and then add new instances to the pool, the new instances have the new name.
Click **Work Requests** in the **Resources** box to check the status of the instance pool create.
  * Use the [oci compute-management instance-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/create.html) command and required parameters to create an instance pool.
Copy
```
oci compute-management instance-pool create --compartment-id <compartment_OCID> --instance-configuration-id <instance-configuration_OCID> --placement-configurations <placement_configurations.json> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the following information:
       * The OCID of the compartment where you want to create the instance pool definition: `oci iam compartment list`
Note that the instances in the pool are created in the compartment specified in the instance configuration.
       * The OCID of the instance configuration that you want to use: `oci compute-management instance-configuration                     list`
       * The size of the instance pool. This is the number of compute instances in the instance pool.
       * If you want load balancing for this pool, get the following information:
         * OCID of the load balancer to attach to this pool and name of the backend set to which to add these pool instances: `oci lb load-balancer list`
         * Port value to use when creating the backend set.
         * VNIC to associate with the load balancer. The value can be `PrimaryVnic` or the display name of one of the secondary VNICs on the instance configuration associated with the instance pool.
    2. Construct an argument for the `--placement-configurations` option.
See the descriptions of Placement Configuration and Fault Domains at the beginning of this section.
Use the following command to show the content of the placement configurations argument:
```
$ oci compute-management instance-pool create --generate-param-json-input placement-configurations
```

    3. If you want load balancing for this pool, construct an argument for the `--load-balancers` option.
Use the following command to show the content of the load balancers argument:
```
$ oci compute-management instance-pool create --generate-param-json-input load-balancers
```

To attach a load balancer after the instance pool is created, see [Managing Instance Pool Load Balancer Attachments](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm#managing-intance-pool-load-balancer-attachments "On Compute Cloud@Customer, you can attach a load balancer to an instance pool or detach a load balancer attachment from an instance pool.").
    4. Run the instance pool create command.
Syntax:
```
oci compute-management instance-pool create -c compartment_OCID --instance-configuration-id instance_configuration_OCID --placement-configurations file://placement_configuration.json --size number_of_instances
```

Example:
```
$ oci compute-management instance-pool create --compartment-id ocid1.compartment.unique_ID --display-name support-pool --instance-configuration-id ocid1.instanceConfiguration.unique_ID --placement-configurations file://./placement_configurations.json --load-balancers file://./load_balancers.json --size 10
```

The value of the `--display-name` option is the name of the pool. The pool name isn't required to be unique. If you don't provide a value for the `--display-name` option, the default name of the instance pool is `instancepool**_YYYYMMDDhhmmss_**`, where`** _YYYYMMDDhhmmss_**`is the creation date and time.
The pool name is used in the names of the instances. Instances in a pool are named `inst-**_aaaaa_**-**_pool_name_**`, where`** _aaaaa_**`is five random alphanumeric characters. If you change the name of the pool and then add new instances to the pool, the new instances will have the new name.
The output of this command is the same as the output of the `instance-pool get` command. The list of instances in the pool isn't shown.
To list the instances that belong to this pool, use the following command:
```
$ oci compute-management instance-pool list-instances -c <compartment_OCID> --instance-pool-id <instance_pool_OCID>
```

The output for each instance is abbreviated compared with the output from the `instance get` command.
The following command shows the same abbreviated output for only the specified instance:
```
$ oci compute-management instance-pool-instance get --instance-id ocid1.instance.unique_ID \
--instance-pool-id ocid1.instancePool.unique_ID
```

  * Use the [CreateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/CreateInstancePool) operation to create an instance pool.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

