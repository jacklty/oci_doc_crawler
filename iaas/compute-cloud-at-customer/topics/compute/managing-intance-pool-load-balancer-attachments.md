Updated 2024-01-18
# Managing Instance Pool Load Balancer Attachments
On Compute Cloud@Customer, you can attach a load balancer to an instance pool or detach a load balancer attachment from an instance pool.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/managing-intance-pool-load-balancer-attachments.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Pools**.
    2. At the top of the page, select the compartment that contains the instance pool for which you want to manage load balancer attachments.
    3. Click the name of the pool that you want to manage.
    4. Under **Resources** , click **Load Balancers**.
       * To attach a load balancer, click **Attach Load Balancer**.
On the **Attach Load Balancer** dialog box, specify the load balancer, backend set, port number, and VNIC as described in [Creating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm#creating-an-instance-pool "On Compute Cloud@Customer, you can create an instance pool of instances that are within the same region."), and click **Attach Load Balancer**.
       * To remove a load balancer attachment, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the load balancer attachment that you want to remove, and click **Detach**.
The load balancer attachment remains visible in the load balancers list in the Detached state for at least 24 hours, up to 24.5 hours. No further action is needed to detach the load balancer attachment.
  * Use the [oci compute-management instance-pool attach-lb](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/attach-lb.html) command and required parameters to attach a load balancer to the instance pool.
Copy
```
oci compute-management instance-pool attach-lb --backend-set-name <backend-set-name> --instance-pool-id <instance-pool_OCID> --load-balancer-id <load-balancer_OCID> --port <port_for_backend_set> --vnic-selection <VNIC_display_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    * **To attach a load balancer to an instance pool:**
      1. Get the following information:
         * OCID of the instance pool to which you want to attach a load balancer: `oci compute-management instance-pool                       list`
         * OCID of the load balancer and name of the backend set: `oci lb load-balancer list`
         * Port value to use when creating the backend set.
         * VNIC to associate with the load balancer. The value can be `PrimaryVnic` or the display name of one of the secondary VNICs on the instance configuration that's associated with the instance pool.
      2. Run the instance pool attach load balancer command.
Example:
```
$ oci compute-management instance-pool attach-lb --instance-pool-id ocid1.instancePool.unique_ID --load-balancer-id ocid1.loadbalancer.unique_ID --backend-set-name BES1 --port 80 --vnic-selection PrimaryVnic
```

    * **Remove or detach a load balancer from an instance pool:**
      1. Get the following information:
         * OCID of the instance pool
         * OCID of the load balancer
         * Backend set name
      2. Run the instance pool detach load balancer command.
Example:
```
$ oci compute-management instance-pool detach-lb --instance-pool-id ocid1.instancePool.unique_ID --load-balancer-id ocid1.loadbalancer.unique_ID --backend-set-name BES1
```

When you `get` or `list` the instance pool, the load balancer attachment remains visible in state `DETACHED` for at least 24 hours, up to 24.5 hours. No further action is needed to detach the load balancer attachment.
  * Use the following operations to attach or detach a load balancer to an instance pool.
    * [AttachLoadBalancer](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/AttachLoadBalancer)
    * [DetachLoadBalancer](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/DetachLoadBalancer)
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

