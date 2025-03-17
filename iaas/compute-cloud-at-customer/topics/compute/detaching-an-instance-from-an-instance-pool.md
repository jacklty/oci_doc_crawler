Updated 2024-12-16
# Detaching an Instance from an Instance Pool
On Compute Cloud@Customer, when you detach an instance from a pool, you can choose whether to delete the instance or to retain the instance separate from the pool. 
Using the CLI, you can choose whether to replace the detached instance by creating a new instance in the pool. If you don't replace the detached instance, then the pool size is decremented.
If load balancers are attached to the pool, then the instance is removed from the load balancers.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/detaching-an-instance-from-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/detaching-an-instance-from-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/detaching-an-instance-from-an-instance-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Pools**.
    2. At the top of the page, select the compartment that contains the instance pool.
    3. Click the name of the instance pool from which you want to detach an instance.
    4. On the **Instance Pool** details page, under **Resources** , click **Attached Instances**.
    5. For the instance that you want to detach, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Detach**.
    6. (Optional) To delete the instance and its boot volume, click the button under "Permanently terminate (delete) this instance and its attached boot volume."
    7. Click **Confirm**.
The pool size is decreased.
  * Use the [oci compute-management instance-pool detach-lb](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/detach-lb.html) command and required parameters to detach an instance from an instance pool.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the information you need to run the command.
       * OCID of the instance pool that you want to update: `oci compute-management instance-pool list`
       * OCID of the instance that you want to detach: `oci compute-management instance-pool list-instances`
    2. Run the instance pool detach instance command.
Syntax:
```
oci compute-management instance-pool-instance detach \
--instance-pool-id **_instance_pool_OCID_** --instance-id **_instance_OCID_** \
--is-auto-terminate [true|false] --is-decrement-size [true|false]
```

Provide the following options if you don't want the default behavior: 

`--is-auto-terminate`
    
If `true`, permanently terminate (delete) the instance and its attached boot volume when the instance is detached from the instance pool. The default value is `false`. 

`--is-decrement-size`
    
If `true`, decrement the pool `size` when the instance is detached from the instance pool. This is the default.
If `false`, provision a new, replacement instance using the pool’s instance configuration after the existing instance is detached from the instance pool. The pool size remains the same as it was before you performed this detach operation.
Example:
In the following example, the specified instance is detached from the pool and terminated, and a new instance is provisioned for the pool.
```
$ oci compute-management instance-pool-instance detach \
--instance-pool-id ocid1.instancePool.**_unique_ID_** \
--instance-id ocid1.instance.**_unique_ID_** \
--is-auto-terminate true --is-decrement-size false
```

The output of this command is the same as the output of the `instance-pool get` command.
  * This operation can't be performed using the API.


Was this article helpful?
YesNo

