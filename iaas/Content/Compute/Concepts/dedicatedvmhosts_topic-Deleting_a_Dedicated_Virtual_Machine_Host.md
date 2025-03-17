Updated 2025-01-13
# Deleting Dedicated Virtual Machine Hosts
You can delete a dedicated virtual machine host after you terminate (delete) the instances that are placed on it.
See [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Deleting_a_Dedicated_Virtual_Machine_Host.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Deleting_a_Dedicated_Virtual_Machine_Host.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Deleting_a_Dedicated_Virtual_Machine_Host.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Dedicated Virtual Machine Hosts**. 
    2. Click the dedicated virtual machine host that you're interested in.
    3. Click **Delete** , and then confirm when prompted.
  * Open a command prompt and run:
```
oci compute dedicated-vm-host delete --dedicated-vm-host-id <dedicated_VM_host_OCID>
```

  * Use the [DeleteDedicatedVmHost](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/DeleteDedicatedVmHost) operation.


Was this article helpful?
YesNo

