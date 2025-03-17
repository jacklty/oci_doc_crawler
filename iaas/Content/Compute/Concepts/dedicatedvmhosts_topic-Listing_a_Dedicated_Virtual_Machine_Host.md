Updated 2023-08-08
# Listing Dedicated Virtual Machine Hosts
List the instances on a dedicated virtual machine host.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm)


  * You can list the instances on a dedicated virtual machine host using the following steps.
    1. Open the navigation menu.
    2. Click **Compute**.
    3. Under **Compute** , click **Dedicated Virtual Machine Hosts**.
    4. Go to the **Details** page for the dedicated virtual machine host.
    5. Under **Resources** , click **Hosted Instances**. Perform this step for each compartment in your tenancy that has instances running on the dedicated virtual machine host. To change the compartment for the **Hosted Instances** list, select a different compartment from the **Table Scope** list.
  * To list the instances running on a dedicated virtual machine host, run the following command:
Command
CopyTry It
```
oci compute dedicated-vm-host list --compartment-id <compartment_OCID> --dedicated-vm-host-id <dedicatedVMhost_OCID>
```

Run this command for every compartment in your tenancy that has instances running on the dedicated virtual machine host that you want to delete.
  * Use the [ListDedicatedVmHostInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHostInstanceSummary/ListDedicatedVmHostInstances) operation.


Was this article helpful?
YesNo

