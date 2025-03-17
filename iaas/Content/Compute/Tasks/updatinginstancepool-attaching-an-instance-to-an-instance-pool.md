Updated 2025-02-03
# Attaching an Instance to an Instance Pool
Attach an existing instance to an instance pool, and then select which instances you want to manage as a group.
When you attach an instance to an instance pool, the pool size increases.
**Important** If an autoscaling configuration is associated with the instance pool, then ensure that the autoscaling policy defines a maximum pool size that's large enough for the expanded pool by [editing the autoscaling policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#Autoscaling). If you attach an instance and it causes the pool size to increase above the maximum autoscaling target, then a future autoscaling event might decrease the pool size and delete instances.
If load balancers are attached to the pool, then the instance is also added to the load balancers.
## Before You Begin
To attach an instance to an instance pool, all the following things must be true:
  * The instance and the pool are running.
  * The instance is the same machine type as the pool, either virtual machine or bare metal.
  * The instance is in the same availability domain and fault domain as the pool.
  * The instance's primary VNIC is in the same virtual cloud network (VCN) and subnet as the pool.
  * If secondary VNICs are defined, then the instance's secondary VNIC is in the same VCN and subnet as the secondary VNICs used by other instances in the pool.
  * The instance is not attached to another pool.


You must also have the name or **OCID** of the instance that you want to attach.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm)


  * To attach an instance to an instance pool:
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool to which you want to attach to an instance to display the details page.
    4. In the **Resources** section, click **Attached instances**.
    5. In the **Attached instances** section, click **Attach instance** to display the Attach instance to instance pool dialog.
    6. In the **Input type** list, select either **Instance pool name** or **Instance pool OCID**.
    7. In the **Instance in _compartment_** list, select the name of the instance or enter its OCID.
    8. Click **Attach instance**.
  * Use the [instance-pool-instance attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/attach.html) command to attach an existing instance to an instance pool.
Copy
```
oci compute-management instance-pool-instance attach --instance-id <INSTANCE_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [AttachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/AttachInstancePoolInstance) operation to attach an existing instance to an instance pool.


Was this article helpful?
YesNo

