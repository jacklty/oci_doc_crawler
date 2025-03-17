Updated 2025-01-13
# Creating a Dedicated Virtual Machine Host
You must create a dedicated virtual machine host in Compute before you can place any instances on it.
When creating a dedicated virtual machine host, you select an availability domain and fault domain to launch it in. All the VM instances that you place on the host are subsequently created in this availability domain and fault domain.
You also select a compartment when you create the host, but you can move the host to a new compartment later without impacting any of the instances placed on it. You can also create the instances in a different compartment than the host, or move them to different compartments after they have been launched.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Dedicated Virtual Machine Hosts**. 
    2. Click **Create dedicated virtual machine host**.
    3. Enter a name for the host. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    4. Select the compartment to create the host in.
    5. Select the **availability domain** for the host.
    6. In the **Dedicated host shape** section, select the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#dedicatedvmhost) to use for the host. To see which VM shapes you can use to create instances on the host, click the down arrow in the row for a host shape.
    7. (Optional) If you want to configure the fault domain or add tags, click **Show Advanced Options**. Then enter the following information:
       * **Fault domain:** The fault domain for the host.
       * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    8. Click **Create**.
  * Open a command prompt and run:
Command
CopyTry It
```
oci compute dedicated-vm-host create --dedicated-vm-host-shape <shape_name> --wait-for-state ACTIVE --display-name <display_name> --availability-domain <availability_domain> --compartment-id <compartment_OCID>
```

<shape_name> is the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#dedicatedvmhost) for the dedicated virtual machine host.
It can take up to 15 minutes for the dedicated virtual machine host to be fully created. It must be in the `ACTIVE` state before you can launch an instance on it.
To query the current state of a dedicated virtual machine host using the CLI, run the following command:
Command
CopyTry It
```
oci compute dedicated-vm-host get --dedicated-vm-host-id <dedicatedVMhost_OCID>
```

  * Use the [CreateDedicatedVmHost](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/CreateDedicatedVmHost) operation.


Was this article helpful?
YesNo

