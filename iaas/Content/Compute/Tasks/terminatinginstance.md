Updated 2025-01-13
# Terminating an Instance
You can permanently delete (terminate) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.
By default, the instance's boot volume is preserved when you terminate the instance. You can attach the boot volume to a different instance as a data volume, or use it to launch a new instance. If you no longer need the boot volume, you can permanently delete it at the same time that you terminate the instance.
**Caution** If your instance has NVMe storage, terminating the instance securely erases the NVMe drives. Any data that was on the NVMe drives becomes unrecoverable. Ensure that you back up any important data before you terminate an instance. For more information, see [Protecting Data on NVMe Devices](https://docs.oracle.com/en-us/iaas/Content/Compute/References/nvmedeviceinformation.htm#Protecting_Data_on_NVMe_Devices).
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. Click **Terminate**.
       * Select **Permanently delete the attached boot volume** if you want to delete the boot volume that is associated with the instance.
       * Select **Permanently delete Block Volume(s) that were created with this instance** to permanently delete any block volumes that were created when this instance was created.
    4. Click **Terminate**.
The instance is permanently deleted. The record remains visible in the list of instances with the state **Terminated** for at least 12 hours, but no further action is needed.
  * Use the [instance terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/terminate.html) command and required parameters to terminate an instance:
Copy
```
oci compute instance terminate --instance-id <instance_OCID> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Use the [TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance) operation to terminate an instance.


Was this article helpful?
YesNo

