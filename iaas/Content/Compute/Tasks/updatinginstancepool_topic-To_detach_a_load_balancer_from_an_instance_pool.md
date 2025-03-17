Updated 2025-02-03
# Detaching a Load Balancer from an Instance Pool
Detach a load balancer or network load balancer from an instance pool.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool from which you want to detach a load balancer or network load balancer to display the details page..
    4. In the **Resources** section, click **Load balancers**.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the load balancer or network load balancer you want to detach and then click **Detach load balancer**.
    6. Click **Detach** to confirm.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that might occur, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [instance-pool detach-lb](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/detach-lb.html) command to detach a load balancer from an instance pool.
Copy
```
oci compute-management instance-pool detach-lb --backend-set-name <NAME> --instance-pool-id <INSTANCE_POOL_OCID> --load-balancer-id <LOAD_BALANCER_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [DetachLoadBalancer](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/DetachLoadBalancer) operation to detach a load balancer from an instance pool.


Was this article helpful?
YesNo

