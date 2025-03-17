Updated 2024-12-16
# Attaching an Instance to an Instance Pool
On Compute Cloud@Customer, when you attach an instance to an instance pool, the pool size increases.
**Important**
If an autoscaling configuration is associated with the instance pool, then ensure that the autoscaling policy defines a target pool size that's large enough for the expanded pool. The next time the scheduled autoscaling policy runs, the target pool size is reset to the value that's set in the policy; if the policy size is smaller than the current size, instances are deleted.
If load balancers are attached to the pool, then the instance is also added to the load balancers.
Ensure the following conditions before you attach an instance to an instance pool:
  * Both the pool and the instance to be attached are running.
  * The instance isn't attached to another pool.
  * The instance is in the same fault domain as the pool.
  * The primary VNIC of the instance is in the same VCN and subnet as the pool.
  * If secondary VNICs are defined, then the secondary VNIC of the instance is in the same VCN and subnet as the secondary VNICs used by other instances in the pool.


To attach an instance that's in a fault domain that's not included in the pool instance configuration, or is using a VCN and subnet that aren't specified by the pool instance configuration, first update the instance configuration, then attach the instance. To update the instance configuration, create and attach a new instance configuration as shown in [Updating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm#updating-an-instance-pool "On Compute Cloud@Customer, when you update an instance pool, you can change the name of the pool, the size of the pool, the instance configuration that's used to create new instances, the fault domains, VCN, and subnet.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/attaching-an-instance-to-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/attaching-an-instance-to-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/attaching-an-instance-to-an-instance-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Pools**.
    2. At the top of the page, select the compartment that contains the instance pool.
    3. Click the name of the instance pool to which you want to attach an instance.
    4. On the instance pool details page, under **Resources** , click **Attached Instances**.
    5. Click **Attach Instance** on the **Attached Instances** table.
    6. In the **Input type** field of the **Attach Instance** dialog box, select either **Instance name** or **Instance OCID**.
       * If you select **Instance name** , a list of instances is displayed. The list of instances is labeled **Potentially attachable instances** because instances must meet certain criteria to be eligible to be attached. For example, the instance must be in the same VCN and subnet that's specified by the instance pool configuration, and the instance must not already be attached to this pool or any other pool. See the list of criteria at the top of the **Attach Instance** dialog box.
If an instance that you think should be attachable isn't shown, try using**Instance OCID**.
       * If you select **Instance OCID** , a text field labeled **Instance OCID** is displayed where you can paste the OCID of the instance that you want to attach.
    7. Click **Attach**.
Even if the criteria listed in the dialog are met, the instance could fail to attach for some other reason. Under **Resources** , click **Work Requests** , then click the applicable work request in the list to troubleshoot any problems.
  * Use the [oci compute-management instance-pool-instance attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/attach.html) command and required parameters to attach an instance to an instance pool. 
    1. Get the information you need to run the command.
       * OCID of the instance pool that you want to update: `oci compute-management instance-pool list`
       * OCID of the instance that you want to attach: `oci compute instance list`
    2. Run the instance pool attach instance command.
```
oci compute-management instance-pool-instance attach --instance-pool-id <instance_pool_OCID> --instance-id <instance_ocid>
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This operation can't be performed using the API.


Was this article helpful?
YesNo

