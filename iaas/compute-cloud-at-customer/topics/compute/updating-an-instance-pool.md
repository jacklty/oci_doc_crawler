Updated 2024-01-18
# Updating an Instance Pool
On Compute Cloud@Customer, when you update an instance pool, you can change the name of the pool, the size of the pool, the instance configuration that's used to create new instances, the fault domains, VCN, and subnet.
To attach or detach an instance, see [Attaching an Instance to an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/attaching-an-instance-to-an-instance-pool.htm#attaching-an-instance-to-an-instance-pool "On Compute Cloud@Customer, when you attach an instance to an instance pool, the pool size increases.") and [Detaching an Instance from an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/detaching-an-instance-from-an-instance-pool.htm#detaching-an-instance-from-an-instance-pool "On Compute Cloud@Customer, when you detach an instance from a pool, you can choose whether to delete the instance or to retain the instance separate from the pool.").
To attach load balancers or detach load balancer attachments, see [Managing Instance Pool Load Balancer Attachments](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm#managing-intance-pool-load-balancer-attachments "On Compute Cloud@Customer, you can attach a load balancer to an instance pool or detach a load balancer attachment from an instance pool.").
Configuration changes don't affect existing instances; configuration changes only affect new instances. New instances will be provisioned using the new instance configuration and placement configuration.
If you increase the size of the pool, new instances are provisioned. The new instances are created evenly across the fault domains specified by the instance configuration or the placement configuration.
If you decrease the size of the pool, instances are deleted evenly across the fault domains specified by the instance configuration or the placement configuration. In each fault domain, instances are deleted in creation date order, oldest first.
You can't select which instances to delete when you decrease the size of a pool. If you delete an individual instance that's a member of a pool, as described in [Deleting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-an-instance.htm#deleting-an-instance "On Compute Cloud@Customer, you can delete instances using the Compute Cloud@Customer Console, CLI, and API."), a new instance is automatically provisioned to keep the pool at the specified pool size.
If you increase the size of the pool, and some new instances can't be provisioned because of resource constraints, those instances remain in Provisioning state and the pool remains in Scaling state until all instances are provisioned. See the suggested remedies in [Creating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm#creating-an-instance-pool "On Compute Cloud@Customer, you can create an instance pool of instances that are within the same region.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Pools**.
    2. At the top of the page, select the compartment that contains the instance pool that you want to update.
    3. For the instance pool that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. In the **Update Instance Pool** dialog box, make the changes.
    5. Click **Update Instance Pool**.
  * Use the [oci compute-management instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command and required parameters to update the specified instance pool.
Copy
```
oci compute-management instance-pool update --instance-pool-id instance_pool_OCID options_with_values_to_update[OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to update the specified instance pool.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

