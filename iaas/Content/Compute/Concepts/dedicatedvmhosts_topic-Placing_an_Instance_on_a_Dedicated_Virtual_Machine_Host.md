Updated 2023-08-08
# Placing Instances on a Dedicated Virtual Machine Host
You place an instance on a dedicated virtual machine host at the time that you create the instance.
## Checking the Capacity of a Dedicated Virtual Machine Host
The dedicated virtual machine host must have [sufficient capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#ocpu) for the shape of instance that you want to create. In the Console, when you create an instance, you can only select from the dedicated virtual machine hosts that have enough capacity for the shape that you specify.
You can use the API, CLI, or SDKs to determine which dedicated virtual machine hosts have capacity for a particular shape. Use the [ListDedicatedVmHosts](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHostSummary/ListDedicatedVmHosts) API operation, passing the name of the shape that you want to use when launching the instance. For flexible shapes, you can also include the minimum number of OCPUs and amount of memory you want to provision.
The following example shows how to use the CLI to return all the dedicated virtual machine hosts with enough capacity for you to place an instance using the `VM.Standard.E4.Flex` shape with 8 OCPUs and 10 GB memory:
Command
CopyTry It
```
oci compute dedicated-vm-host list --compartment-id <compartment_OCID> --instance-shape-name VM.Standard.E4.Flex --remaining-ocpus-greater-than-or-equal-to 8 --remaining-memory-in-gbs-greater-than-or-equal-to 10
```

For more information, see [Optimizing Capacity on a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#ocpu).
## Placing an Instance
To place an instance on a dedicated host, follow these steps using the Console or API.
## Using the Console
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the **Placement** section.
  2. In the **Placement** section, click **Show advanced options**.
  3. For **Capacity type** , select **Dedicated host**.
  4. Select the dedicated virtual machine host that you want to place the instance on.
  5. Finish configuring the instance, and then click **Create**.


## Using the API
Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation to create the instance, passing the OCID of the dedicated virtual machine host in the `dedicatedVmHostId` parameter.
Was this article helpful?
YesNo

